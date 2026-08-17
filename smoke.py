import os
import sys
from pathlib import Path

from strategy_packages import copy_strategy

if len(sys.argv) < 2:
    print("usage: python smoke.py <AI name.per | path/to/file.per> [timeout seconds] [civ]")
    sys.exit(1)

per_name = sys.argv[1]
timeout = int(sys.argv[2]) if len(sys.argv) > 2 else 10
civ = sys.argv[3] if len(sys.argv) > 3 else "teutons"

# If given a path to an existing .per file, copy it into the game AI folder
# (settings.txt line 1, same as single_match.py) so the scan below picks it up.
if os.path.isfile(per_name):
    with open("settings.txt") as f:
        ai_path = f.readline().strip().replace("\\", "/") + "/"
    source = Path(per_name)
    base_name = source.name
    packaged = copy_strategy(source, Path(ai_path))
    print("copied %s -> %s" % (per_name, ai_path + base_name))
    if packaged:
        print("copied package %s/ -> %s" % (source.stem, ai_path + source.stem + "/"))
    per_name = base_name

exec(open("single_match.py").read().replace("root.mainloop()", "pass"))
smoke_test(per_name, timeout, civ)
