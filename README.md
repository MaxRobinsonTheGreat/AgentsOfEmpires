This is a automatic game runner for Age of Empires 2: DE. **This runs via screen capture, it cannot run in the background.**

> [!WARNING]
> This repo is a mess, scrapped together to collect footage for a youtube video. I uploaded it more or less as is. You'll have to hand this off to an agent to get it running for your purposes, they'll figure it out.

Before running:
- backup your AI folder
  - (this **will** overwrite all .ai files in your ai directory. .per files will be untouched. A backup of all .ai files will be saved to /ai_backup, but to be safe I suggest you backup your ai folder before running)
- open AoE2 DE and set the game settings to how you want them (difficulty, map, cheats, etc.) A future release may allow you to change settings via the auto-DE GUI, but this is not supported for now.

How to run:
- download and extract git code to anywhere on your computer
- copy `settings.example.txt` to `settings.txt`, then update its AI directory for your installation.
  - you can also enable debugging in this file, and change the macro delay in case your machine struggles.
- run AOE2 DE at full screen. Resolution-independent: screen coordinates scale from a 1920x1080 baseline, and UI button templates (Images/) were captured at 3840x2160. If the game UI changes, templates must be re-captured.
- either:
  - enter ai names (eg Bambi_v030.per) matching their .per name in your directory (case senstitive)
  - enter ai civs
  - set timeout time and game count
  - set speedup hotkey for sped up games or leave blank.
  - Make sure DE is on screen, open to main menu, and the auto-DE GUI is not blocking the single player button (it minimizes itself during runs).
  - Press run and wait!
- or:
  - copy `parameters.example.csv` to `parameters.csv` and list every matchup you would like tested
  - press "run from csv"

The results print in the CMD window, save to a csv in the outputs folder, and to a machine-readable Outputs/status.json (updated after every game, with a heartbeat timestamp).

## Headless / agent tools

- `python smoke.py <name.per> [timeout]` - quick self-vs-self test of one script (default 30s). Result JSON in Outputs/smoke_result.json; AI script error dialogs are screenshotted to Outputs/errors/.
- `python tournament.py [rounds] [max_game_time]` - round robin over every .per in the tournament/ folder (no mirror matches). Archives strats, results, screenshots, and game recordings to runs/<timestamp>/. Fixed civ is the CIV constant at the top of tournament.py.
- `python wait.py [poll_seconds]` - blocks until Outputs/status.json reports tournament_done, then prints standings. Exits 2 if the heartbeat goes stale (runner died).

Recordings: every game's .aoe2record is copied to Outputs/recordings/ and parsed (tools/recording-tools, requires Node.js) - duration, resignations, age-up times, queue/building/research command counts, and an inferred winner are included in status.json.

Note: tournament/smoke run fine without the GUI (it minimizes). While any run is active, do not use the mouse - the bot drives the real cursor.

## Strategies

- `tournament/` contains the final battle-scenario lineup and self-contained Promisory forks. `strat_pure_promi` is the strongest strategy from the recorded final round.
- `saved_strats/` contains earlier Arabia and battle-control experiments.
- `NOTES.md` and `NOTES_arabia_1v1.md` document the experiments and results.
- Generated recordings, screenshots, and run archives stay local under `Outputs/` and `runs/` and are not tracked.

Debugging:
- check the console log; on any failure a screenshot (plus an annotated best-match version and the template) is saved to Failures/.
- try increasing the command delay in the settings file
- check AI names, check debug log (cmd window) to see if it is getting stuck trying to find a button
