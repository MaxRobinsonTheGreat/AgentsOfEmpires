# NOTES.md

## Mission (from AgentsOfEmpires.md brief)
Arabia, Teutons mirror, standard victory, 1-hour limit (2x speed). Beat extreme-ai
(PromiDE = default DE AI) in repeated 3-way tournaments: extreme-ai vs last-best vs new.

## Harness tips (learned the hard way)
- `python tournament.py [rounds] [max_secs]` - run FOREGROUND and wait.
- smoke test new strats first: `python smoke.py <file.per> 45 teutons`.
- Tech constant gotcha: it's `ri-wheel-barrow` NOT `ri-wheelbarrow`.
  Full correct names in docs/aoe2-ai-parser/airef-command-inventory.json - check before smoke.
- Validated working identifiers: militia-line, spearman-line, teutonic-knight-line, monk,
  battering-ram-line, ri-man-at-arms, ri-champion, ri-scale-mail, ri-chain-mail,
  ri-plate-mail, ri-forging, ri-iron-casting, ri-blast-furnace, ri-squires, ri-loom,
  ri-elite-teutonic-knight, ri-sanctity, ri-fervor, ri-block-printing, ri-illumination,
  ri-heavy-plow, ri-horse-collar, ri-double-bit-axe, ri-bow-saw, ri-wheel-barrow,
  ri-hand-cart, ri-capped-ram. Also: attack-now, enable-timer (ids 1-32),
  sn-food/wood/gold/stone-gatherer-percentage, sn-enable-boar-hunting.
- Do not alt-tab / use the mouse during runs - game must stay focused.

## Round 1 strats
- strat_maa_rush.per ("maa-rush"): 21-pop feudal, 2 rax M@A pressure, castle into
  Teutonic Knights + monks, attack waves every 45-60s. Smoke: OK.
- strat_tk_boom.per ("tk-boom"): 27-pop castle, castle + 3 TCs boom to 80 vills,
  TK + rams + monks, attacks only at 20+ military. Smoke: OK (after wheel-barrow fix).
- PromiDE.per ("extreme-ai"): untouched default baseline.

## Results log
- R1: extreme 2-0 | tk-boom 1-1 | maa-rush 0-2 (never castled - villager-cap deadlock bug)
- R2: extreme 2-0 | tk-boom 1-1 | teu-trush 0-2 (same deadlock: age-up gated on food bank + villager floor while training nonstop)
- R3: extreme 2-0 | promi-tk 1-1 (Promisory+TK layer, first real fight vs default) | tk-boom 0-2 OUT
- R4 (4-way, cav left in by accident): cav BEAT extreme-ai (knights counter trash comp!) | circle: ai>cav? no - ai>tk, tk>cav, cav>ai
- R5 (4-way): promi-halb BEAT extreme-ai (115 pikes) | halb 2-1 | cav 0-2 (variance!)
- R6: extreme 2-0 | halb 1-1 | scorp 0-2 OUT (scorpions flopped)
LESSON: single-game matchups swing wildly - cav beat ai in R4, lost in R5. Consider 2 rounds when close.
LESSON: layers that beat extreme-ai: knight mass (vs skirm/archer trash), pike mass (vs knights).
"Object 25" in queues = unrecognized unit id (probably elite TK upgrade id quirk).

## Round 7
- strat_promi_mix.per went 2-0: beat BOTH extreme-ai (53:16) and promi-halb (48:34)
- promi-halb beat extreme-ai again (55:46) - extreme-ai went 0-2 this round!

## Round 8 (4-way: extreme, promi-mix, + 2 new; runs/20260806_124813)
- **landsknecht 3-0 NEW CHAMPION**: Promisory + TK16/spear8/mangonel5/monk4/BBC4,
  castle<2, siege-workshop<2, monastery, full melee-BS/siege/monk research layer.
  Beat extreme (1:54:22 marathon! 247 TK queued), blitz (37:36), promi-mix (51:16).
- extreme 2-1 | promi-mix 1-2 (lost to extreme 40:13 - R7 dominance didn't repeat, variance again)
- blitz 0-3 OUT: Promisory + feudal M@A layer. FAILED: never left Feudal all game.
  92 militia queued in feudal (cap-14 + constant retrain) drained food -> Promisory's
  castle age-up starved. SAME deadlock as R1 maa-rush, now proven to happen through
  a layer too. LESSON: only add unit-training layers at castle-age+.
- blitz's taunt-31-on-timer-50 mechanism: ZERO taunt events in recording. Timer 50
  never fired (DE timer range suspect / unverified) - do not trust timer 50; Promisory
  occupies 1-49. Taunt-31 self-trigger for forcing Promisory attacks remains UNTESTED.
- "Object 25" in queue parses = Teutonic Knight (confirmed via landsknecht).
- extreme-ai countered TKs with 19 Hand Cannoneers in the marathon - HC is the anti-TK
  tech in the mirror; a challenger could mass HC + siege vs landsknecht.
- Marathon warning: 1:54:22 in-game ~= 57 min real at 2x, just under the 3600s cap.
  TK-mirror slugfests may hit timeout; consider raising max_game_time.

## Harness changes (this session)
- main.py RENAMED to single_match.py (tournament.py/smoke.py exec it; refs updated).
- focus_game_window() in single_match.py: forces game window foreground before every
  game (verified w/ GetForegroundWindow, AttachThreadInput fallback, only restores
  if IsIconic - do NOT SW_RESTORE a maximized window, it shrinks it).
- smoke.py: accepts a filepath (auto-copies into AI folder), default timeout 10s,
  skips post-game stats capture (game_loop capture_stats=False). Error dialogs
  persist, so short timeouts still catch load errors.
- Root cause of mystery aborts: bot input landing on non-game windows (opencode,
  Explorer) when they covered the game - Esc aborted the agent's own command.

## Human observations (after R8, verbatim)
Combat is poor. Early rushes consistently fail to rush, they stay home and are often
attacked first. You likely need to override promisory behavior. Micro is poor. Units
die under buildings, fail to take shots at vils. They ignore taking damage for long
periods and are slow to respond. Large numbers are often distracted and killed by
small numbers. They get stuck attacking low value buildings, like houses, and take
heavy hits. I suspect you will gain much here.
- Also from human: variance makes single-game results unreliable - landsknecht's 3-0
  may be luck. Long tests are a pain until game speed can be raised without changing
  gameplay. Human may follow up with a dedicated battle AI.

## Where to resume
- last-best = landsknecht; next round: extreme-ai vs landsknecht vs new challenger
- challenger ideas: HC+siege-onager anti-TK comp; fixed blitz (castle-age-only
  aggression, maybe taunt-31 every pass instead of timers); monk-mass conversions
  (steal the TK deathball); bigger-numbers landsknecht mirror.
- per human observations above: biggest untapped edge is COMBAT CONTROL - overriding
  Promisory's attack/micro behavior (target prioritization: units > vils > military
  buildings >> houses; retreat when taking damage; don't chase small bait groups;
  don't melt under TC/castle fire).

