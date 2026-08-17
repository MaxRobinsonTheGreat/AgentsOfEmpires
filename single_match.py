import pyautogui
import pydirectinput
import time
import os
import json
import random
import tkinter as tk
from sys import exit

# make coordinates consistent on scaled/multi-monitor setups (must run before any pyautogui calls)
import ctypes
ctypes.windll.user32.SetProcessDPIAware()

# the bot deliberately clicks near screen edges; the corner fail-safe would kill runs
pyautogui.FAILSAFE = False
pydirectinput.FAILSAFE = False

Images_Folder: str = os.getcwd() + "\\Images\\"

f = open("settings.txt",'r')
Settings = f.read().split("\n")
AI_Path: str = Settings[0].replace("\\","/") + "/"
if "FALSE" in Settings[1]:
    debug = False
else:
    debug = True
Command_Delay = float( Settings[2].split("=")[1] )

f.close()

# hardcoded coordinates below were designed for 1920x1080; scale to actual screen
SCALE = pyautogui.size().height / 1080
def sx(x): return int(x * SCALE)


def focus_game_window() -> None:
    """Bring AoE2DE to the foreground so bot input reaches the game, not other windows.

    Without this, clicks can land on whatever window is on top (e.g. a terminal),
    and stray Esc presses go to that app instead of the game.
    """
    user32 = ctypes.windll.user32
    kernel32 = ctypes.windll.kernel32
    hwnd = user32.FindWindowW(None, "Age of Empires II: Definitive Edition")
    if not hwnd:
        print("WARNING: game window not found - is AoE2DE running?")
        return
    for attempt in range(5):
        if user32.GetForegroundWindow() == hwnd:
            print("game window focused")
            time.sleep(1)
            return
        # SW_RESTORE only if minimized - on a maximized/fullscreen window it would
        # un-maximize and shrink it
        if user32.IsIconic(hwnd):
            user32.ShowWindow(hwnd, 9)  # SW_RESTORE
        # brief Alt tap satisfies Windows' rules for changing the foreground window
        pydirectinput.keyDown("alt")
        pydirectinput.keyUp("alt")
        user32.SetForegroundWindow(hwnd)
        time.sleep(0.5)
        if user32.GetForegroundWindow() == hwnd:
            continue  # verified on next loop pass
        # plain call failed: attach to the foreground window's input thread to
        # bypass focus-stealing prevention, then try again
        fg = user32.GetForegroundWindow()
        if fg:
            fg_thread = user32.GetWindowThreadProcessId(fg, None)
            cur_thread = kernel32.GetCurrentThreadId()
            user32.AttachThreadInput(fg_thread, cur_thread, True)
            if user32.IsIconic(hwnd):
                user32.ShowWindow(hwnd, 9)
            user32.SetForegroundWindow(hwnd)
            user32.AttachThreadInput(fg_thread, cur_thread, False)
        time.sleep(0.5)
    if user32.GetForegroundWindow() == hwnd:
        print("game window focused")
    else:
        print("WARNING: could not bring game window to foreground")
    time.sleep(1)

# ---- JSON status / results ----
STATUS_PATH = "Outputs/status.json"
STATUS: dict = {"tournament_done": False, "games": [], "standings": {}}
LAST_ERROR_SHOTS: list = []  # error screenshots from the current game


def find_replays_folder() -> str:
    """Locate the DE savegame folder containing .aoe2record files."""
    base = os.path.expanduser("~") + "/Games/Age of Empires 2 DE"
    best = None
    best_time = -1
    if os.path.isdir(base):
        for profile in os.listdir(base):
            candidate = os.path.join(base, profile, "savegame")
            if not os.path.isdir(candidate):
                continue
            for name in os.listdir(candidate):
                if name.endswith(".aoe2record"):
                    t = os.path.getmtime(os.path.join(candidate, name))
                    if t > best_time:
                        best_time = t
                        best = candidate
    return best


REPLAYS_FOLDER = find_replays_folder()


def parse_latest_recording(since: float) -> dict:
    """Parse the newest .aoe2record modified after `since`. Returns summary dict or {}."""
    import subprocess
    if not REPLAYS_FOLDER:
        print("no replays folder found, skipping recording parse")
        return {}
    candidates = [os.path.join(REPLAYS_FOLDER, n) for n in os.listdir(REPLAYS_FOLDER)
                  if n.endswith(".aoe2record") and os.path.getmtime(os.path.join(REPLAYS_FOLDER, n)) >= since - 5]
    if not candidates:
        print("no new recording found, skipping recording parse")
        return {}
    newest = max(candidates, key=os.path.getmtime)
    os.makedirs("Outputs/recordings", exist_ok=True)
    import shutil as _shutil
    dest = "Outputs/recordings/" + os.path.basename(newest)
    _shutil.copy(newest, dest)
    try:
        proc = subprocess.run(
            ["node", "tools/recording-tools/read-recording.mjs", "--path", dest, "--format", "json"],
            capture_output=True, text=True, timeout=120)
        summary = json.loads(proc.stdout)
        summary["recording_file"] = dest
        print("recording parsed: duration %s, winner %s" % (
            summary.get("duration"), (summary.get("inferredWinner") or {}).get("name")))
        return summary
    except Exception as e:
        print("recording parse failed: " + str(e))
        return {"recording_file": dest, "parse_error": str(e)}


def write_status() -> None:
    os.makedirs("Outputs", exist_ok=True)
    STATUS["heartbeat"] = time.strftime("%Y-%m-%dT%H:%M:%S")
    f = open(STATUS_PATH, "w")
    json.dump(STATUS, f, indent=2)
    f.close()


def record_game(rec: dict) -> None:
    STATUS["games"].append(rec)
    st = STATUS["standings"]
    for name in (rec["ai_one"], rec["ai_two"]):
        st.setdefault(name, {"wins": 0, "losses": 0, "errors": 0})
    # slots are coin-flipped at game start; when a mapped winner name exists it
    # identifies the winning STRAT regardless of which on-screen slot it sat in
    if "winner" in rec and rec["winner"] in (rec["ai_one"], rec["ai_two"]):
        winner = rec["winner"]
        loser = rec["ai_two"] if winner == rec["ai_one"] else rec["ai_one"]
        st[winner]["wins"] += 1
        st[loser]["losses"] += 1
    elif rec["result"] == "win_ai_one":
        st[rec["ai_one"]]["wins"] += 1
        st[rec["ai_two"]]["losses"] += 1
    elif rec["result"] == "win_ai_two":
        st[rec["ai_two"]]["wins"] += 1
        st[rec["ai_one"]]["losses"] += 1
    elif rec["result"] == "ai_error":
        st[rec["ai_one"]]["errors"] += 1
        st[rec["ai_two"]]["errors"] += 1
    write_status()

AIs_Available: list = []
All_AI_Files : list = os.listdir(AI_Path)
for i in range(len(All_AI_Files)):
    if ".per" in All_AI_Files[i]:
        AIs_Available.append(All_AI_Files[i])

def clean_directory() -> None:
    for i in range(len(All_AI_Files)):
        if ".ai" in All_AI_Files[i]:

            f = open("AI_Backup/" + All_AI_Files[i],'w+')
            f.write("saved this for you")
            f.close()

            #easier to catch the error here than try to mess with the list above
            try:
                os.remove(AI_Path + All_AI_Files[i])
            except FileNotFoundError:
                pass

    f = open(AI_Path + "AI_One.ai","w+")
    f.write("isn't matty the best?")
    f.close()

    f = open(AI_Path + "AI_Two.ai","w+")
    f.write("isn't matty the best?")
    f.close()

def set_ais(AI_One: str, AI_Two: str) -> tuple:
    """Copy the two strats into the AI_One/AI_Two slots. Slot assignment is
    coin-flipped to cancel any player-1/player-2 positional advantage.
    Returns (slot_one_ai, slot_two_ai) - the names actually in each slot."""
    if AI_One not in AIs_Available:
        print("AI NOT AVAILABLE: " + AI_One)
        exit()
    elif AI_Two not in AIs_Available:
        print("AI NOT AVAILABLE: " + AI_Two)
        exit()

    slot_one, slot_two = AI_One, AI_Two
    if random.random() < 0.5:
        slot_one, slot_two = AI_Two, AI_One
    print("slot assignment: AI_One.per <- %s | AI_Two.per <- %s" % (slot_one, slot_two))

    f = open(AI_Path + slot_one,'r')
    n = open(AI_Path + "AI_One.per","w+")
    n.write(f.read())
    f.close()
    n.close()

    f = open(AI_Path + slot_two,'r')
    n = open(AI_Path + "AI_Two.per","w+")
    n.write(f.read())
    f.close()
    n.close()

    return slot_one, slot_two

def find_on_screen(template_path: str):
    """Returns (x, y, confidence) of best match, or (None, None, confidence)."""
    import cv2, numpy as np
    haystack = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)
    needle = cv2.imread(template_path)
    if needle is None:
        print("ERROR: could not load template file " + template_path)
        return None, None, 0.0
    res = cv2.matchTemplate(haystack, needle, cv2.TM_CCOEFF_NORMED)
    _, conf, _, loc = cv2.minMaxLoc(res)
    if conf >= 0.9:
        h, w = needle.shape[:2]
        return loc[0] + w // 2, loc[1] + h // 2, conf
    return None, None, conf


def save_failure_screenshot(image: str) -> None:
    import cv2, numpy as np
    os.makedirs("Failures", exist_ok=True)
    name = os.path.basename(image).replace(".", "_")
    stamp = str(int(time.time()))
    shot = pyautogui.screenshot()
    path = "Failures/" + stamp + "_" + name + ".png"
    shot.save(path)

    # save the template that was being searched for, for side-by-side comparison
    needle = cv2.imread(image)
    if needle is not None:
        cv2.imwrite("Failures/" + stamp + "_" + name + "_template.png", needle)

        # annotated copy: rectangle at the best-match location with its confidence
        haystack = cv2.cvtColor(np.array(shot), cv2.COLOR_RGB2BGR)
        res = cv2.matchTemplate(haystack, needle, cv2.TM_CCOEFF_NORMED)
        _, conf, _, loc = cv2.minMaxLoc(res)
        h, w = needle.shape[:2]
        cv2.rectangle(haystack, loc, (loc[0] + w, loc[1] + h), (0, 0, 255), 3)
        cv2.putText(haystack, "best match: %.3f" % conf, (loc[0], max(30, loc[1] - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)
        cv2.imwrite("Failures/" + stamp + "_" + name + "_annotated.png", haystack)
        print("best match was %.3f at %s" % (conf, loc))

    print("FAILURE: giving up on " + image)
    print("Screenshot saved to " + path)


def click_at(cx: int, cy: int) -> None:
    """Deliberate click: move, settle, press. More reliable than instant click."""
    pydirectinput.moveTo(cx, cy)
    time.sleep(0.2)
    pydirectinput.mouseDown()
    time.sleep(0.1)
    pydirectinput.mouseUp()


def try_press(image: str) -> bool:
    """Single match attempt; clicks and returns True if found."""
    x, y, conf = find_on_screen(Images_Folder + image)
    if x is None:
        return False
    ox, oy = CLICK_OFFSETS.get(os.path.basename(image), (0, 0))
    cx, cy = x + sx(ox), y + sx(oy)
    print("FOUND " + image + " (confidence %.3f) - clicking at %d,%d" % (conf, cx, cy))
    time.sleep(.1)
    click_at(cx, cy)
    return True


# click offsets (1080p pixels) for templates whose clickable area isn't the template center
CLICK_OFFSETS = {"single_player.PNG": (0, 58)}


def press_button_or_crash(image: str) -> None:
    image = Images_Folder + image

    time.sleep(Command_Delay)

    ox, oy = CLICK_OFFSETS.get(os.path.basename(image), (0, 0))
    max_attempts = 3
    for attempt in range(1, max_attempts + 1):
        x, y, conf = find_on_screen(image)
        if x is not None:
            cx, cy = x + sx(ox), y + sx(oy)
            print("FOUND " + os.path.basename(image) + " (confidence %.3f) - clicking at %d,%d" % (conf, cx, cy))
            time.sleep(.1)
            click_at(cx, cy)
            return
        print("MISS  " + os.path.basename(image) + " - best match confidence %.3f (need 0.900), attempt %d/%d" % (conf, attempt, max_attempts))
        time.sleep(1)

    save_failure_screenshot(image)
    raise SystemExit(1)

def wait_until_seen(image: str) -> None:
    image = Images_Folder + image

    max_attempts = 3600  # ~1 hour at 1 check/second
    for attempt in range(1, max_attempts + 1):
        x, y, conf = find_on_screen(image)
        if x is not None:
            print("SAW " + os.path.basename(image) + " (confidence %.3f)" % conf)
            time.sleep(.1)
            return
        if attempt % 60 == 1:
            print("waiting for " + os.path.basename(image) + " - best confidence %.3f, attempt %d/%d" % (conf, attempt, max_attempts))
        time.sleep(1)

    save_failure_screenshot(image)
    raise SystemExit(1)


def reset_to_main_menu() -> None:
    """Best-effort navigation back to the main menu from known screens."""
    for i in range(10):
        x, y, conf = find_on_screen(Images_Folder + "single_player.PNG")
        if x is not None:
            print("at main menu")
            return
        print("not at main menu, backing out (attempt %d/10)" % (i + 1))

        # AI script error dialog blocking the screen: capture + dismiss
        x, y, conf = find_on_screen(Images_Folder + "AI_error.png")
        if x is not None:
            print("AI error dialog up, dismissing")
            dismiss_ai_errors()
            quit_game()
            time.sleep(3)
            continue

        # post-game stats screen: "Return to Main Menu" button
        x, y, conf = find_on_screen(Images_Folder + "main_menu.PNG")
        if x is not None:
            print("on stats screen, clicking Return to Main Menu")
            pydirectinput.click(x, y)
            time.sleep(2)
            continue

        # skirmish lobby: "Return to Main Menu" is visible iff Start Game is
        x, y, conf = find_on_screen(Images_Folder + "start_game.PNG")
        if x is not None:
            print("in lobby, clicking Return to Main Menu")
            pydirectinput.click(sx(457), sx(963))
            time.sleep(2)
            continue

        # civ picker: CONFIRM visible -> click CANCEL
        x, y, conf = find_on_screen(Images_Folder + "confirm.png")
        if x is not None:
            print("in civ picker, clicking Cancel")
            pydirectinput.click(sx(1438), sx(1052))
            time.sleep(1.5)
            continue

        # unknown menu screen: try back arrow (top-left), then escape
        pydirectinput.click(sx(45), sx(38))
        time.sleep(1)
        pydirectinput.press("escape")
        time.sleep(1.5)

    save_failure_screenshot(Images_Folder + "single_player.PNG")
    raise SystemExit(1)

def set_players(civ_1: str, civ_2: str) -> None:

    player_one_img: str = Images_Folder + "player_1.png"
    player_two_img: str = Images_Folder + "player_2.png"

    #player 1
    pydirectinput.click(sx(390),sx(390))
    press_button_or_crash("AI_One.png")
    time.sleep(.1)

    pydirectinput.click(sx(1000),sx(390))
    press_button_or_crash("random.png")
    if civ_1.lower() != "random":
        press_button_or_crash(civ_1.lower() + ".png")
    press_button_or_crash("confirm.png")

    #player 2
    time.sleep(1)  # let player 1's civ-confirm fully close or this click is swallowed
    pydirectinput.click(sx(390),sx(430))
    press_button_or_crash("AI_Two.png")
    pydirectinput.press("enter")

    pydirectinput.click(sx(1000),sx(430))
    press_button_or_crash("random.png")
    if civ_2.lower() != "random":
        press_button_or_crash(civ_2.lower() + ".png")
    press_button_or_crash("confirm.png")

def capture_stats_screens() -> dict:
    """Screenshot every tab of the post-game statistics screen. Returns {tab: path}."""
    os.makedirs("Outputs", exist_ok=True)
    tabs = [("score", 420), ("military", 620), ("economy", 880),
            ("technology", 1100), ("society", 1340), ("timeline", 1550)]
    shots = {}
    stamp = str(int(time.time()))
    for name, x_1080 in tabs:
        click_at(sx(x_1080), sx(45))
        time.sleep(1.2)
        path = "Outputs/" + stamp + "_stats_" + name + ".png"
        pyautogui.screenshot().save(path)
        shots[name] = path
    # return to score tab so winner-crown detection works afterwards
    click_at(sx(420), sx(45))
    time.sleep(1.2)
    return shots


def quit_game() -> None:
    """Quit the current game via Escape -> Quit Current Game -> Yes."""
    pydirectinput.press("escape")
    time.sleep(1.5)
    press_button_or_crash("quit.PNG")
    press_button_or_crash("yes.PNG")
    time.sleep(2)


def dismiss_ai_errors() -> int:
    """Screenshot and dismiss any AI Script Error dialogs. Returns number found."""
    os.makedirs("Outputs/errors", exist_ok=True)
    count = 0
    for i in range(10):
        x, y, conf = find_on_screen(Images_Folder + "AI_error.png")
        if x is None:
            break
        count += 1
        path = "Outputs/errors/" + str(int(time.time())) + "_ai_error_" + str(count) + ".png"
        pyautogui.screenshot().save(path)
        LAST_ERROR_SHOTS.append(path)
        print("AI ERROR dialog captured: " + path)
        press_button_or_crash("ok.png")
        time.sleep(1.5)
    return count


def check_game(max_game_time: int) -> str:
    game_ended = False
    start = time.time()
    current = start

    while not game_ended:
        current = time.time()

        #print(current - start)

        if current - start < max_game_time:


            try:
                x, y = pyautogui.locateCenterOnScreen(Images_Folder + "AI_error.png", confidence=0.9)

                dismiss_ai_errors()
                quit_game()

                return "ai_error"

            except (pyautogui.ImageNotFoundException, TypeError):
                pass

            try:
                x, y = pyautogui.locateCenterOnScreen(Images_Folder + "error.png", confidence=0.9)
                for i in range (10):
                    try:
                        x, y = pyautogui.locateCenterOnScreen(Images_Folder + "dont_send.png", confidence=0.9)
                        time.sleep(.25)
                        pydirectinput.click(x, y)
                    except (pyautogui.ImageNotFoundException, TypeError):
                        pass

                return "crash"
            except (pyautogui.ImageNotFoundException, TypeError):
                pass

            time.sleep(1)

            # game end screen button: "Leave Map" (random map) or "Continue" (custom scenario)
            end_clicked = False
            for end_button in ("leave_map.png", "continue.png"):
                try:
                    x, y = pyautogui.locateCenterOnScreen(Images_Folder + end_button, confidence=0.8)
                    print("game ended - clicking " + end_button)
                    pyautogui.click(x, y)
                    end_clicked = True
                    break
                except (pyautogui.ImageNotFoundException, TypeError):
                    pass
            if end_clicked:
                game_ended = True
                return False

        #timed_out
        else:

            quit_game()

            return "time out"

def game_loop(AI_One: str, AI_Two: str, games: int, max_game_time: int, Speedup: str, civ_1: str, civ_2: str, capture_stats: bool = True) -> dict:

    AI_One_Wins = 0
    AI_Two_Wins = 0
    timed_out = 0
    start_time = time.time()

    for i in range(games):

        focus_game_window()
        reset_to_main_menu()
        clean_directory()
        # set_ais coin-flips which strat occupies which slot to cancel any
        # player-1/player-2 advantage; slot_one/slot_two are the real assignments.
        # Civs follow the AI into its slot.
        slot_one, slot_two = set_ais(AI_One, AI_Two)
        ai_civ = {AI_One: civ_1, AI_Two: civ_2}
        slot_civ = {slot_one: ai_civ[slot_one], slot_two: ai_civ[slot_two]}

        pydirectinput.press("escape")

        # menu transition can swallow the first click; retry a few times
        opened = False
        for nav_attempt in range(4):
            press_button_or_crash("single_player.PNG")
            time.sleep(1)
            if try_press("skirmish.PNG"):
                opened = True
                break
            print("single player menu did not open, retrying (%d/4)" % (nav_attempt + 1))
        if not opened:
            save_failure_screenshot(Images_Folder + "skirmish.PNG")
            raise SystemExit(1)
        time.sleep(1)
        set_players(slot_civ[slot_one], slot_civ[slot_two])
        press_button_or_crash("start_game.PNG")
        game_started_at = time.time()

        print("game loading, waiting 20s before monitoring")
        time.sleep(20)

        if Speedup != "":
            for i in range(10):
                try:
                    pydirectinput.press(Speedup)
                    time.sleep(.1)
                except:
                    print("invalid key! takes win32 key codes")

        result = check_game(max_game_time)
        time.sleep(5)

        os.makedirs("Outputs", exist_ok=True)
        game_record = {"ai_one": AI_One, "civ_one": civ_1, "ai_two": AI_Two, "civ_two": civ_2,
                       "slot_one": slot_one, "slot_two": slot_two,
                       "error_screenshots": list(LAST_ERROR_SHOTS)}
        LAST_ERROR_SHOTS.clear()

        # stats screens only exist after a normal end or a quit (timeout)
        if result == "crash":
            stats_shot = "Outputs/" + str(int(time.time())) + "_postgame.png"
            pyautogui.screenshot().save(stats_shot)
            game_record["stats_screenshot"] = stats_shot
        elif capture_stats:
            game_record["stats_screenshots"] = capture_stats_screens()
            game_record["stats_screenshot"] = game_record["stats_screenshots"]["score"]

        game_record["recording"] = parse_latest_recording(game_started_at)

        if result == "crash":
            game_record["result"] = "crash"
            record_game(game_record)
            try:
                reset_game()
            except NameError:
                pass
            return {"GAME CRASH" : 1}
        elif result == "ai_error":
            game_record["result"] = "ai_error"
            record_game(game_record)
            return {"AI CRASH" : 1}
        elif result == "time out":
            game_record["result"] = "timeout"
            record_game(game_record)
            press_button_or_crash("main_menu.PNG")
            timed_out += 1

        else:
            x = 0
            y = 0
            try:
                x, y = pyautogui.locateCenterOnScreen(Images_Folder + 'won_1.PNG', confidence=0.8)
            except (pyautogui.ImageNotFoundException, TypeError):
                try:
                    x, y = pyautogui.locateCenterOnScreen(Images_Folder + 'won_2.PNG', confidence=0.8)
                except (pyautogui.ImageNotFoundException, TypeError):
                    print("could not identify winner")

            # crown y-position says which on-screen slot won; map slot back to strat
            if y < sx(337) and result != "time out" and y != 0:
                game_record["result"] = "win_ai_one"
                game_record["winner"] = slot_one
                if slot_one == AI_One:
                    AI_One_Wins += 1
                else:
                    AI_Two_Wins += 1

            elif result != "time out" and y != 0:
                game_record["result"] = "win_ai_two"
                game_record["winner"] = slot_two
                if slot_two == AI_One:
                    AI_One_Wins += 1
                else:
                    AI_Two_Wins += 1

            else:
                game_record["result"] = "unknown"

            record_game(game_record)
            press_button_or_crash("main_menu.PNG")

    return {AI_One: AI_One_Wins, AI_Two: AI_Two_Wins, "TIMED OUT" : timed_out, "Total time" : time.time() - start_time}

def run_games(AI_One: str, AI_Two: str, games: int, max_game_time: int, Speedup: str, civ_1: str, civ_2: str) -> None:

    root.iconify()  # hide GUI so it doesn't cover the game
    try:
        output = game_loop(AI_One, AI_Two, games, max_game_time, Speedup, civ_1, civ_2)
    finally:
        root.deiconify()
    f = open("Outputs/" + str(time.time()) + ".csv","w+")
    f.write("AI,score\n")
    for entry in output:
        f.write(entry + "," + str( output[entry] ) + "\n")
    f.close()

    print_string = ""
    for entry in output:
        print_string += entry + "," + str(output[entry]) + ","
    print(print_string)

def run_from_csv() -> None:

    root.iconify()  # hide GUI so it doesn't cover the game
    try:
        _run_from_csv_impl()
    finally:
        root.deiconify()


def _run_from_csv_impl() -> None:

    global STATUS
    STATUS = {"tournament_done": False, "games": [], "standings": {}}
    write_status()

    f = open("parameters.csv",'r')
    params = f.read().split("\n")
    f.close()

    #validate AIS
    for i in range(1,len(params)):
        matchup = params[i].split(",")
        if len(matchup) > 5:
            AI_One = matchup[0]
            AI_Two = matchup[2]

            try:
                f = open(AI_Path + AI_One,'r')
                f.read()
                f.close()
            except UnicodeDecodeError:
                print(str(AI_One) + " has invalid non-unicode characters. Remove from the csv or modify the .per to resolve.")
                exit()

            try:
                f = open(AI_Path + AI_Two,'r')
                f.read()
                f.close()
            except UnicodeDecodeError:
                print(str(AI_Two) + " has invalid non-unicode characters. Remove from the csv or modify the .per to resolve.")
                exit()

    output_filename = "Outputs/" + str(time.time())
    f = open(output_filename + ".csv","w+")
    f.write("AI One,Civ,Score,AI Two,Civ,Score,\n")
    f.close()

    for i in range(1,len(params)):
        matchup = params[i].split(",")

        if len(matchup) > 5:

            AI_One = matchup[0]
            civ_1 = matchup[1]
            AI_Two = matchup[2]
            civ_2 = matchup[3]
            games = int(matchup[4])
            max_game_time = int(matchup[5])
            Speedup = matchup[6]

            f = open(output_filename + ".csv","a")
            local_result = game_loop(AI_One, AI_Two, games, max_game_time, Speedup, civ_1, civ_2)

            civ_index = 0
            civs = [civ_1, civ_2,"",""]
            print_string = ""
            for entry in local_result:
                if civs[civ_index] != "":
                    print_string += entry + "," + civs[civ_index] + "," + str(local_result[entry]) + ","
                    f.write(entry + "," + civs[civ_index] + "," + str(local_result[entry]) + ",")
                else:
                    print_string += entry + "," + str(local_result[entry]) + ","
                    f.write(entry + "," + str(local_result[entry]) + ",")
                civ_index += 1
            print(print_string)
            f.write("\n")
            f.close()

    STATUS["tournament_done"] = True
    write_status()


def smoke_test(per_name: str, max_game_time: int = 30, civ: str = "teutons") -> dict:
    """Quick self-vs-self test of one AI script. Writes Outputs/smoke_result.json."""
    global STATUS
    STATUS = {"tournament_done": False, "games": [], "standings": {}}
    write_status()

    if per_name not in AIs_Available:
        result = {"ai": per_name, "result": "file_not_found"}
        print("SMOKE RESULT: " + json.dumps(result))
        return result

    game_loop(per_name, per_name, 1, max_game_time, "", civ, civ, capture_stats=False)

    STATUS["tournament_done"] = True
    write_status()

    game = STATUS["games"][-1] if STATUS["games"] else {}
    result = {"ai": per_name,
              "result": game.get("result", "unknown"),
              "error_screenshots": game.get("error_screenshots", []),
              "stats_screenshot": game.get("stats_screenshot")}
    os.makedirs("Outputs", exist_ok=True)
    f = open("Outputs/smoke_result.json", "w")
    json.dump(result, f, indent=2)
    f.close()
    print("SMOKE RESULT: " + json.dumps(result))
    return result



#print(game_loop("best.per","HD.per",3))

root = tk.Tk()

Label_1 = tk.Label(root, text = "AI One:  (include .per)")
Label_1.pack()

AI_One_Input = tk.Text(root, height = 1, width = 15)
AI_One_Input.insert(tk.INSERT, "EXAMPLE.per")
AI_One_Input.pack()

civ_1_label = tk.Label(root, text = "Civ One:")
civ_1_label.pack()

Civ_One_Input = tk.Text(root, height = 1, width = 15)
Civ_One_Input.insert(tk.INSERT, "huns")
Civ_One_Input.pack()

Label_2 = tk.Label(root, text = "AI Two:  (include .per)")
Label_2.pack()

AI_Two_Input = tk.Text(root, height = 1, width = 15)
AI_Two_Input.insert(tk.INSERT, "EXAMPLE_2.per")
AI_Two_Input.pack()

civ_2_label = tk.Label(root, text = "Civ Two:")
civ_2_label.pack()

Civ_Two_Input = tk.Text(root, height = 1, width = 15)
Civ_Two_Input.insert(tk.INSERT, "huns")
Civ_Two_Input.pack()

Label_3 = tk.Label(root, text = "Games to run")
Label_3.pack()

Game_Count = tk.Text(root, height = 1, width = 15)
Game_Count.insert(tk.INSERT, "3")
Game_Count.pack()

Label_4 = tk.Label(root, text = "Timeout time (real life seconds)")
Label_4.pack()

Timeout_Time = tk.Text(root, height = 1, width = 15)
Timeout_Time.insert(tk.INSERT, "10000")
Timeout_Time.pack()

Label_5 = tk.Label(root, text = "(Optional) Speed-up Hotkey")
Label_5.pack()

Speedup = tk.Text(root, height = 1, width = 15)
Speedup.insert(tk.INSERT, "blank for no speed up")
Speedup.pack()

button1 = tk.Button(root, text = "Run", command = lambda: run_games(AI_One_Input.get(1.0,"end-1c"), AI_Two_Input.get(1.0,"end-1c"), int( Game_Count.get(1.0,"end-1c") ), int( Timeout_Time.get(1.0,"end-1c")) , Speedup.get(1.0,"end-1c"), Civ_One_Input.get(1.0,"end-1c"), Civ_Two_Input.get(1.0,"end-1c")))
button1.pack()

button2 = tk.Button(root, text = "Run from csv", command = lambda: run_from_csv())
button2.pack()


root.mainloop()
