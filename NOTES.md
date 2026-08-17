# NOTES.md

## MISSION (2026-08-06)
Mirror 1v1 battle, Post-Imperial Japanese fixed armies (custom scenario lobby,
Fast speed): 8 Cavaliers, 16 Elite Samurai, 12 Halberdiers, 12 Arbalests,
12 Elite Skirmishers, 1 Siege Onager, 2 Heavy Scorpions. NO economy - pure combat
control. Games last 1-4 in-game minutes. Beat default extreme-ai (PromiDE) in
round-robin tournaments. Cap: 300s. Old Teuton-mirror strats in saved_strats/.

### Scenario unit change (2026-08-07, human edit)
- Mounted Samurai -> Cavaliers, Heavy Pikemen -> Halberdiers.
- Cavaliers are still cavalry-class, so existing cavalry selectors keep working.
- Halberdiers ARE spearman-line (unlike the old Heavy Pikemen), so both
  spearman-line and the infantry-class-minus-samurai selector now work for pikes.
- Old probe findings about Mounted Samurai / Heavy Pikemen ids are obsolete.

## Harness notes (battle mission)
- Scenario lobby works: AI/civ pickers clickable, scenario forces civ/units anyway.
- Scenario end screen = "Continue" (continue.png), not "Leave Map" - check_game
  tries leave_map.png then continue.png.
- Slot randomization: set_ais coin-flips AI_One/AI_Two assignment each game;
  winner mapped back via slot_one/slot_two + winner fields. Verified vs human.
- Recording parser shows "winner None" for battle games (ends by elimination,
  no resign/commands to infer from) - crown detection is authoritative.
- smoke.py takes a filepath (auto-copies to AI folder), 10s default timeout,
  skips stats-tab capture. single_match.py = former main.py.
- Strategy packages are supported: `name.per` plus optional sibling `name/`.
  tournament.py and smoke.py recursively copy the package; tournament archives it.
  Static package namespaces are slot-randomization safe. Generate a full editable
  Promisory fork with `python create_strategy_package.py strat_name`.

## Critical diagnostic result (after Round 3 repeat)
- Human correctly observed that lancer/guardian/raider looked identical.
- A temporary post-loader probe proved:
  - appended rules execute
  - timer 50 fires
  - Mounted Samurai are detectable as cavalry-class
  - own siege-onager and heavy-scorpion ids work
  - BUT sn-target-player-number remains 0 in this custom scenario
  - therefore remote Siege Onager search never succeeds
  - Heavy Pikemen are NOT spearman-line
- Consequence: lancer/raider cavalry target rules and guardian pike rules were no-ops.
  Their different tournament records were almost entirely combat variance from the
  same underlying Promisory behavior, not evidence that the intended layers worked.
- Do not build more remote DUC layers until enemy focus is set explicitly (player 1
  targets 2; player 2 targets 1) and the Heavy Pikeman's actual unit id/class is found.
- Preferred direction: fork Promisory into per-strategy packages and edit TSA/orb
  directly so custom scenario units and targeting are first-class, not appended hopes.

## .per battle-control primitives (verified)
- DUC: up-find-remote needs sn-focus-player-number (sync it from
  sn-target-player-number each pulse). up-set-target-object search-remote c: 0
  picks first found enemy; up-target-objects 1 action-default -1 -1 = all local
  units focus-fire that object. up-find-local c: all-units-class c: 100 = whole army.
- Search lists ACCUMULATE across rules within a pass: every independent DUC rule
  must start with up-full-reset-search.
- attack-now must run BEFORE DUC rules in file order (later orders in a pass win).
- Attack-group SNs: sn-number-attack-groups 40, sn-min/max-attack-group-size 1/200,
  sn-percent-attack-soldiers 100, sn-attack-intelligence 1.
- Stances: up-set-attack-stance <base-unit-id> c: stance-defensive/stand-ground/
  aggressive. Unit LINES don't work there - use base ids (samurai, elite-samurai,
  spearman, pikeman, halberdier, arbalest, elite-skirmisher).
- Scenario unit ids: samurai-line (elite-samurai), spearman-line (halberdier),
  arbalest, elite-skirmisher, cavalry-class (mounted samurai), siege-weapon-class
  (onager + scorpions), all-units-class (-1).
- Timers 1-50 free in from-scratch strats (Promisory occupies 1-49 if loaded).

## Round 1 (runs/20260806_172028) - 5 strats, 10 games, ~20 min total
- IMPORTANT: tournament.py still had CIV="teutons" during this round. The custom
  scenario supplied the fixed army, but the lobby civ was wrong. Treat Round 1 as
  provisional/noncanonical; tournament.py is now fixed to CIV="japanese".
- **PromiDE 4-0** - default's combat handling beat everything, incl. stonewall.
- **stonewall 3-1** - best non-default. Hold 45s (melee defensive, ranged
  stand-ground) then counterattack. Beat blob/counter/headhunter, lost to PromiDE.
- blob 1-3 (attack-group pulse), counter 1-3 (DUC counter-targeting),
  headhunter 1-3 (all-in siege focus). All lost to PromiDE AND stonewall.
- Open questions for next round: WHY does PromiDE win (watch a recording - its
  ORB micro may kite/retreat)? Did counter/headhunter DUC actually fire (check
  recording chat/commands - remote search needs enemy visible)?

## Round 2 (runs/20260807_105851) - corrected Japanese civ, 4 strats, 6 games
- **promi-lancer 3-0 - NEW CHAMPION.** Full Promisory plus a surgical DUC layer:
  every 5s, only four cavalry-class units focus the enemy Siege Onager, then Heavy
  Scorpions, in stagger formation. Timer 50 works with full Promisory (which reserves
  1-49). Beat extreme-ai, promi-screen, and stonewall.
- promi-screen 2-1. Full Promisory ranged/siege micro remained active while Samurai
  and pikes were forced defensive for the first 32s. Beat extreme-ai and stonewall,
  lost decisively to lancer.
- extreme-ai 1-2. Beat only stonewall. stonewall 0-3.
- Military screenshots prove decisive margins (kills/losses):
  - lancer 61/38 vs extreme 40/63 (1:07)
  - screen 65/52 vs extreme 50/63 (1:28)
  - lancer 63/29 vs screen 29/63 (1:02)
  - lancer 61/18 vs stonewall 20/63 (0:53)
  - screen 64/17 vs stonewall 16/63 (0:58)
  - extreme 64/50 vs stonewall 49/63 (1:25)
- Record Game was enabled for this round and all six raw replays were archived.
  The parser still reports inferredWinner=None because scenario elimination does
  not create a resignation; crown detection + military screenshots are authoritative.
- Core lesson: preserve Promisory's reload-aware ranged orb/onager micro. Broad
  attack-now or all-army DUC orders destroy its advantage. A narrow four-unit flank
  closes a real coverage gap and outperforms default Promisory by a large margin.

## Round 3 (runs/20260807_113446) - 4 strats, 6 games
- **promi-raider 3-0 - NEW CHAMPION.** Full Promisory plus six cavalry-class units
  sent at the enemy Siege Onager every 3s. Unlike lancer, it does NOT chase Heavy
  Scorpions after the onager dies. Beat extreme-ai, guardian, and prior champion.
- promi-guardian 2-1. Lancer's four-cavalry siege dive plus six pikes assigned to
  intercept enemy cavalry. Beat extreme-ai and lancer, lost to raider.
- extreme-ai 1-2. Beat lancer only. Prior champion promi-lancer collapsed to 0-3.
- Military screenshot margins (kills/losses):
  - guardian 63/53 vs extreme 53/63 (1:51; close)
  - extreme 63/50 vs lancer 50/63 (1:34)
  - raider 64/38 vs extreme 37/63 (1:09)
  - guardian 63/33 vs lancer 33/63 (1:07)
  - raider 64/44 vs guardian 43/63 (1:10)
  - raider 63/37 vs lancer 37/63 (1:05)
- Raider's 3-0 was supported by decisive military margins, not marginal crowns.
  Its crucial differences from lancer are earlier launch (3s vs 5s), six cavalry
  instead of four, and stopping custom control after the onager rather than chasing
  scorpions through the enemy pike screen.
- Guardian proves pike interception works: it crushed lancer 63-33 and beat default,
  but six faster raiders still overwhelmed it. A stronger raider counter likely needs
  more than six pikes, better distance-based interception, or delayed/decoy cavalry.
- Variance warning remains severe: lancer went 3-0 in Round 2 then 0-3 unchanged in
  Round 3, including reversal against default. Single-game standings are hypotheses;
  military margins help, but repeated games are needed for confidence.

## Round 3 exact repeat (runs/20260807_115847) - variance experiment
- Same four unchanged scripts, same Japanese scenario, same 300s cap.
- Repeat standings inverted: **lancer 3-0**, guardian 2-1, raider 1-2,
  extreme-ai 0-3. Prior standings were raider 3-0, guardian 2-1, extreme 1-2,
  lancer 0-3.
- Only 2 of 6 matchup winners repeated:
  - guardian beat extreme twice (stable)
  - raider beat extreme twice (stable)
  - extreme/lancer, guardian/lancer, guardian/raider, and lancer/raider all flipped
- Repeat military margins (kills/losses):
  - guardian 63/60 vs extreme 60/63 (2:07; extremely close)
  - lancer 63/56 vs extreme 56/63 (1:40; close)
  - raider 61/55 vs extreme 57/63 (1:27; close)
  - lancer 62/15 vs guardian 16/63 (0:50; huge flip from prior guardian 63/33)
  - guardian 62/30 vs raider 31/63 (1:02; huge flip from prior raider 64/44)
  - lancer 62/27 vs raider 28/63 (0:56; huge flip from prior raider 63/37)
- Combined over both identical tournaments:
  - guardian 4-2, raider 4-2, lancer 3-3, extreme-ai 1-5
  - guardian and raider are the only consistent default beaters (both 2-0)
  - all custom-vs-custom pairs split 1-1; lancer/default also split 1-1
- Conclusion: first projectile hits, pathing, formation geometry, and/or scenario
  starting state dominate one-game outcomes. Even large military margins can reverse
  on an exact rerun. Prefer aggregate records across multiple tournaments; no single
  3-0 sweep is credible by itself.

## Where to resume
- Latest-round protocol winner = promi-lancer (3-0), but aggregate leaders are
  promi-guardian and promi-raider at 4-2 each. Do not claim a robust sole champion.
- For confidence, run at least 2-3 repetitions per matchup if runtime permits.
- Next ideas: raider + larger pike interceptor (8-10); split cavalry roles (4 dive,
  4 intercept); protect/move own onager away from enemy raiders; use a sacrificial
  cavalry decoy to pull raiders through pikes; distance-gate the onager dive; test a
  slightly smaller/faster 5-cavalry raider to preserve more cavalry for the main fight.

## Independent strategy package architecture
- Strategies may now be `name.per` plus optional sibling `name/`. tournament.py and
  smoke.py recursively copy packages to the game AI folder; runs archive them.
- `python create_strategy_package.py strat_name` creates a fully namespaced editable
  Promisory fork under `tournament/strat_name/Promisory/` and rewrites internal loads.
- Full generated fork passed an in-game Japanese smoke test.
- Promisory's internal jump flow can skip rules appended to the end of tsa.per.
  Final tactical orders are safest in the top-level package loader after all loads;
  internal modules remain independently editable for replacing existing rules.
- Extended goals must be explicitly initialized; do not assume initial value 0.
- Duplicate timer rules consume/rearm a trigger before later rules can see it. Each
  strategy must have exactly one owner for timer 50.

## Scenario diagnostics before independent-strategy round
- Scenario never initializes sn-target-player-number (remains 0).
- `up-find-player enemy find-closest` returns -1 because scenario diplomacy is not
  exposed as expected to that API. Deterministic fix: scenario-player-1 targets 2;
  scenario-player-2 targets 1. This is color based and survives randomized AI slots.
- Heavy Pikemen are not spearman-line. Reliable selector: find infantry-class, remove
  object-data-type samurai and elite-samurai. Probe measured exactly 12 remaining.
- Mounted Samurai are cavalry-class; own siege-onager/heavy-scorpion ids are valid.
- Remote DUC type searches remain unreliable: hunter controller marker fires, but its
  SIEGE DIVE marker did not appear in recorded player-1 games. Explicit target SN still
  materially improves full Promisory behavior.

## Independent-strategy round (runs/20260807_135323) - 3 rounds/matchup, 18 games
- **deep-hunter 8-1 - NEW CHAMPION.** Independent Promisory package with explicit
  scenario target fix and a six-cavalry onager controller. Beat extreme 2-1,
  deep-fortress 3-0, direct-counter 3-0.
- extreme-ai 5-3. Beat fortress 1-1 with one timeout/no-result, lost hunter 1-2,
  swept direct-counter 3-0.
- deep-fortress 4-4 plus one timeout. Independent Promisory package; hard stand-ground
  hold for 15s then release, with filtered pike interception. Split baseline 1-1 plus
  timeout, lost hunter 0-3, swept direct 3-0.
- direct-counter 0-9. Ground-up attack-now + per-class DUC. Distinct behavior but
  catastrophically worse than Promisory micro; sample losses: extreme 62/23 vs
  direct 24/63, fortress 62/21 vs direct 22/63, hunter 65/14 vs direct 12/63.
- Hunter vs extreme military examples: one loss 31/63 vs 63/31, then wins 63/42
  and 63/45. Still meaningful variance, but 8-1 aggregate is much stronger evidence.
- Fortress/default timeout lasted 8:45 game time: fortress killed 56/lost 62,
  extreme killed 62/lost 56. Harness records no winner; stats favored extreme.
- Replay markers prove hunter controller loop and fortress hold-release executed.
  Fortress visually differs by holding; direct controller differs and loses. Hunter's
  siege-dive marker remains absent, so credit the target-player fix first.

## CRITICAL: remote search works by CLASS, not by TYPE-ID (2026-08-07)
- Diagnostic probe inside backline_reaper (P1 chat, mid-fight):
  focus=2 and target=2 were correct; type-id searches (siege-onager,
  heavy-scorpion, arbalest, elite-skirmisher) found 0; cavalry-class found 7
  enemy AND 7 self. Plumbing fine; type-id matching is what fails for
  scenario-placed units in this scenario.
- Consequence: deep_hunter's siege dive NEVER fired in any game (type-id
  search). Its 8-1 record = target-player fix + Promisory only.
- Fix that works: accumulate (up-find-remote c: siege-weapon-class c: 3) +
  (up-find-remote c: archery-class c: 24), up-get-search-state guard
  (goal+2 = remote-total), sort by distance, dive.
- Verified live: "REAPER: DIVE ACTIVE, 25 targets" in smoke recording.

## Final round (runs/20260807_151407) - Cavalier/Halberdier armies, 45 games
Lineup accidentally included the two retirees (fortress, direct_counter were
still in tournament/), so it was a full 6-way round robin, 3 rounds/matchup.
- **pure_promi 14-1 - FINAL CHAMPION.** Promisory fork + explicit scenario
  target fix ONLY, no unit controller. Swept PromiDE 3-0, reaper 3-0,
  fortress 3-0, counter 3-0; beat hunter 2-1.
- deep_hunter 9-5, PromiDE 9-6, backline_reaper 8-6 (+1 timeout vs hunter),
  fortress 4-11, direct_counter 0-15.
- reaper's dive was CONFIRMED live in-game ("DIVE ACTIVE, 25 targets" at 0:02
  - the scenario has full visibility, class searches see everything at start).
  It still lost 0-3 to pure_promi and split with hunter.
- A/B CONCLUSION: all value comes from fixing sn-target/focus-player.
  Pulling 6 cavalry out of Promisory's micro for backline dives is NET
  NEGATIVE in this scenario - the front fight loses more than the dive gains.
  hunter's constant re-orders (dead dive rule still ran up-full-reset-search
  + reissued orders every 3s) also cost it vs the clean fix.
- Champion recipe: fork Promisory, set sn-target-player-number and
  sn-focus-player-number by scenario color, and DO NOT touch the units.
