"""
Round-robin tournament runner.

Usage:  python tournament.py [rounds] [max_game_time_seconds]

- Reads all .per files from the `tournament/` folder.
- Copies them into the game AI folder so they can be played.
- Archives everything to `runs/<timestamp>/` (strats, results, screenshots).
- Every pairing plays `rounds` games (default 1). No mirror matches.
- Progress is written to Outputs/status.json after every game (poll that).
"""
import sys
import os
import time
import shutil
import itertools
from pathlib import Path

from strategy_packages import copy_strategy, package_path

CIV = "japanese"  # fixed civ for the post-Imperial Japanese battle scenario

rounds = int(sys.argv[1]) if len(sys.argv) > 1 else 1
max_game_time = int(sys.argv[2]) if len(sys.argv) > 2 else 3600

exec(open("single_match.py").read().replace("root.mainloop()", "pass"))

strats = sorted(f for f in os.listdir("tournament") if f.endswith(".per"))
if len(strats) < 2:
    print("need at least 2 .per files in tournament/")
    sys.exit(1)

# archive folder
ts = time.strftime("%Y%m%d_%H%M%S")
run_dir = "runs/" + ts
os.makedirs(run_dir)

# copy strats into game AI folder + archive
for s in strats:
    source = Path("tournament") / s
    packaged = copy_strategy(source, Path(AI_Path))
    copy_strategy(source, Path(run_dir))
    if packaged:
        print("copied package: %s/" % package_path(source).name)
    if s not in AIs_Available:
        AIs_Available.append(s)  # single_match.py scanned the AI folder before we copied

matchups = list(itertools.combinations(strats, 2))
run_info = {"civ": CIV, "rounds": rounds, "max_game_time": max_game_time,
            "strats": strats,
            "packages": [Path(s).stem for s in strats
                         if package_path(Path("tournament") / s).is_dir()],
            "matchups": [list(m) for m in matchups]}
f = open(run_dir + "/run_info.json", "w")
json.dump(run_info, f, indent=2)
f.close()

print("tournament: %d strats, %d matchups, %d round(s)" % (len(strats), len(matchups), rounds))

STATUS = {"tournament_done": False, "games": [], "standings": {}}
write_status()

tournament_start = time.time()

for (a, b) in matchups:
    for r in range(rounds):
        print("matchup: %s vs %s (round %d/%d)" % (a, b, r + 1, rounds))
        try:
            game_loop(a, b, 1, max_game_time, "", CIV, CIV)
        except SystemExit:
            raise  # intentional aborts still stop the tournament
        except Exception as e:
            print("GAME FAILED UNEXPECTEDLY: " + str(e))
            record_game({"ai_one": a, "civ_one": CIV, "ai_two": b, "civ_two": CIV,
                         "result": "harness_error", "error_screenshots": list(LAST_ERROR_SHOTS),
                         "error": str(e)})
            LAST_ERROR_SHOTS.clear()
            save_failure_screenshot(Images_Folder + "single_player.PNG")

STATUS["tournament_done"] = True
write_status()

# archive results + screenshots/recordings created during this run
shutil.copy(STATUS_PATH, run_dir + "/status.json")
shot_dir = run_dir + "/screenshots"
os.makedirs(shot_dir)
for folder in ("Outputs", "Outputs/errors"):
    if not os.path.isdir(folder):
        continue
    for name in os.listdir(folder):
        p = os.path.join(folder, name)
        if os.path.isfile(p) and name.lower().endswith(".png") and os.path.getmtime(p) >= tournament_start:
            shutil.copy(p, shot_dir + "/" + name)
rec_src = "Outputs/recordings"
if os.path.isdir(rec_src):
    rec_dir = run_dir + "/recordings"
    os.makedirs(rec_dir)
    for name in os.listdir(rec_src):
        p = os.path.join(rec_src, name)
        if os.path.isfile(p) and os.path.getmtime(p) >= tournament_start:
            shutil.copy(p, rec_dir + "/" + name)

print("tournament complete. archived to " + run_dir)
