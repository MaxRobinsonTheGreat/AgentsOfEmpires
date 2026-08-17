# Agents of Empires ⚔️🛡️

You are an AI agent attempting to build the best possible Age of Empires 2: Definitive Edition AI script for the following setting:
- **Map**: Arabia
- **Playing As**: Teutons
- **Playing Against**: Teutons
- **Victory Mode**: Standard 
- **Starting Resources**: Standard
- **Time Limit**: 1 hour (2x speed)
This is extremely important to me, do your absolute best.


You want to build a fair strategy that can win against other Teutons scripts in a round-robin tournament. You will be able to test your strategy using the provided automation tools, which will run matches and provide detailed results. 

### First Round
Check in with the human, and on their word begin an endless research loop. 
Start by reading the default extreme AI script and its dependencies in `tournament/` `docs/Promisory/`. You can borrow from it, but do not modify it.
Copy or import it or create new strats from scratch. Write 2 new strategies, with high diversity. 
Run a Tournament between all 3. Do not run detached or in a shell, but in the foreground so you must wait for completion. 
### Next Rounds
Then, analyze results and find the one with the most wins that is not the default strategy. Keep it for the next round. 
Replace the other with a new strategy that tries to beat the other two. So default extreme AI vs Last Best Strategy vs New Strategy. 
Run a Tournament between all 3. Repeat this process, iterating and improving your strategies based on the results of each tournament.


All strategies are saved automatically, don't worry about overwriting old strats in the AI folder. But don't touch the default ai script.
If you encounter bugs, try to fix them and continue. Don't cheat or game the mechanism or sabotage other strats, you will only sabotage yourself.
Reread this file on every iteration! Make notes in NOTES.md for future agents.


NEVER STOP ITERATING. If you can't beat the best strategy, try something else.
Throw a hail mary. Brainstorm 5 new maximum diversity strategies and pick the most promising or weird ones. 
Don't be frustrated by worse performance, treat it as a curiosity. You can always go back to the best strategy later. 
Just keep iterating! KEEP GOING!! GLHF!!!!

## Technical Overview

This project automates running 1v1 matches and tournaments between AI scripts (`.per` files) in
Age of Empires 2: Definitive Edition. It drives the real game UI via screen
capture and simulated input. An agent can write strategies, test them, run
tournaments, and read detailed results - all through the tooling below.

## Critical operational rules

- **Never touch the mouse or keyboard while a run is active.** The bot drives the
  real cursor. Input from a human will break it.
- The game must be running, fullscreen, and visible. It cannot run in the background.
- If you (the agent) need to inspect state, read the log/status files or take a
  screenshot with pyautogui; do not move the mouse unnecessarily.
- Long-running commands: run the tournament in the **foreground** and simply wait
  for it to finish, however long it takes. If you get interrupted, the state on
  disk (status.json, logs) always shows where things stand - just re-read it.

## Key paths

- Game AI folder (where playable .per files live):
  `C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\ai`
- `settings.txt` - line 1 is the AI folder path, line 2 debug flag, line 3 command delay.
- Game recordings (.aoe2record) land in:
  `C:\Users\maxdr\Games\Age of Empires 2 DE\76561198055489377\savegame`

## How matches work (single_match.py)

A single game only accepts `AI_One.per` / `AI_Two.per` in the lobby.
The harness copies the chosen strats' contents into those two slots before each
game, navigates the menus by image template matching (Images/), starts the game,
watches for the end (Leave Map), reads the winner from the post-game stats
screen (crown icon), screenshots every stats tab, parses the game recording,
then returns to the main menu. It recovers automatically from leftover dialogs,
the lobby, the civ picker, and AI error popups between games.

Notes for writing strats:
- An in-game display name can be set from inside a script with
  `(up-change-name "myname")` - do this so recordings/screenshots show who is who. Use unique names to avoid confusion.
- A `.per` with no rules is a load error (ERR8001). Always include at least one rule.
- See `tournament/strat_alpha.per` for a minimal example.

### Round-robin tournament
```
python tournament.py [rounds] [max_game_time_seconds]
```
- Plays every pairing of .per files found in `tournament/` (no mirror matches),
  `rounds` times each. Fixed civ is the `CIV` constant at the top of tournament.py.
- Copies strats into the game AI folder automatically.
- Archives each run to `runs/<timestamp>/`: strat copies, run_info.json,
  final status.json, all screenshots, and raw .aoe2record recordings.

## Tools

### Smoke test one strategy (fast error check)
```
python smoke.py <name.per> [timeout_seconds]      # default timeout 30
```
Self-vs-self game; auto-quits after the timeout. Result in `Outputs/smoke_result.json`:
- `result: "ai_error"` -> the script failed to load. `error_screenshots` points to a
  PNG of the exact in-game error dialog (player, file, line, error code). Read the
  image and fix the script.
- `result: "timeout"` -> the script loaded and survived. Good.
- The .per must exist in the game AI folder first.

### Wait for completion
```
python wait.py [poll_seconds] [stale_minutes]
```
Blocks until `Outputs/status.json` has `tournament_done: true`, then prints
standings. Exits 2 if the heartbeat goes stale (runner died; check Failures/ and logs).

### Results (Outputs/status.json)
Updated after every game. Per game: the two strats/civs, `result`
(`win_ai_one` | `win_ai_two` | `timeout` | `ai_error` | `crash` | `harness_error`),
error screenshots, **stats_screenshots** (six PNGs, one per stats tab: score,
military, economy, technology, society, timeline), and a parsed **recording**
summary: game duration, resignation times, age-up times, unit queue / building /
research command counts, market activity, and an inferred winner. `standings`
aggregates wins/losses/errors per strat. `heartbeat` is the liveness timestamp.

### Recording parser (standalone)
```
node tools/recording-tools/read-recording.mjs --path <file.aoe2record> --format json
```
Parses a DE replay into a JSON summary (same data embedded in status.json).
Caveats: queue/building counts are commands issued, not surviving units; exact
scores are unavailable (no achievements block) - use the stats screenshots for those.

### Writing valid .per scripts (docs/)
`docs/aoe2-ai-parser/` contains the reference pack from the AOE2 AI Parser VS Code
extension: full symbol reference, command/parameter/strategic-number inventories,
and validator diagnostic codes (use it to lint mentally before smoke-testing -
load errors waste a full game cycle). `docs/recording-reader.md` documents the
recording tool's output and limitations. `docs/Promisory/` is a full copy of the
default DE AI ("extreme-ai") source - the strongest baseline to read, borrow from,
or build on. Its loader is `tournament/PromiDE.per`; dependencies live in the game
AI folder (Promisory/, ailib under resources\_common\xs), and `(load "Promisory\...")`
works from any strat because the game resolves loads relative to the AI folder.

### GUI / CSV mode (legacy)
`python single_match.py` opens a small GUI: enter two AI names, civs, game count, timeout,
or list matchups in `parameters.csv` and press "Run from csv". The GUI minimizes
itself while running. Headless tools above are preferred for agent use.

## Failure artifacts
- `Failures/` - on any UI failure: a full screenshot, an annotated copy showing
  the best template match, and the template itself. Check here when a run dies.
- `Outputs/errors/` - AI script error dialog screenshots (also linked per-game
  in status.json).

## Templates

Menu matching uses image templates in `Images/` captured at 3840x2160; screen
coordinates scale from a 1920x1080 baseline, so any 16:9 resolution works. If DE
updates its UI art, matching breaks (confidence drops below 0.9) - re-capture the
offending button from a Failures/ screenshot and overwrite the template.
`Images_old/` holds the original (now non-matching) templates.
