# Recording Reader

The workspace root includes `read-recording.ps1`, a wrapper for extracting
useful information from AoE2 DE `.aoe2record` files.

## Commands

```powershell
# Newest replay in the normal user recordings folder
.\read-recording.ps1 -Latest

# The same; latest is the default
.\read-recording.ps1

# Specific replay
.\read-recording.ps1 -Path "C:\path\to\match.aoe2record"

# Extracted machine-readable summary
.\read-recording.ps1 -Latest -Format json

# Complete parser output
.\read-recording.ps1 -Latest -Format raw

# Search another recordings tree
.\read-recording.ps1 -Latest -RecordingsRoot "D:\AoE2\recordings"
```

## Dependencies

Node.js 18 or newer and npm are required. The first invocation installs the
pinned `agelens` dependency under `recording-tools`; later invocations reuse it.

## Extracted Data

- Game duration and version
- Player slots, runtime AI names, and civilizations
- Age completion times found in system chat
- Chat timeline
- Explicit resignations
- Last command time per player
- Unit queue, building placement, research, and market command counts
- A cautiously inferred winner when only one AI remains active at the end

## Limitations

Recorded games are command logs, not final save states. Queue commands can be
cancelled, building placement can fail, and units can die after training. These
counts must not be described as a simultaneous army or final inventory.

Exact scores, kills, losses, resource totals, and population require an
achievements block. If the recording omits it, the reader reports those fields
as unavailable and clearly labels any result inferred from terminal activity.
