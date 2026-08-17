"""Create an independently editable strategy package from docs/Promisory.

Usage:
    python create_strategy_package.py strat_my_idea
    python create_strategy_package.py strat_my_idea --output saved_strats
"""

import argparse
from pathlib import Path
import re
import shutil


def loader_text(name: str) -> str:
    prefix = name + "\\Promisory\\"
    display_name = name.removeprefix("strat_")[:30]
    return f'''(defrule
    (true)
=>
    (up-change-name "{display_name}")
)

(load "{prefix}defaultConstants")
(load "{prefix}finalingConstants")
(load "{prefix}customConstants")
#load-if-not-defined BATTLE-ROYALE
(load "{prefix}init")
(load "{prefix}threats")
(load "{prefix}escrow")
(load "{prefix}dawn")
(load "{prefix}gatherers")
(load "{prefix}scoutcontrol")
(load "{prefix}tsa")
(load "{prefix}watercontrol")
(load "{prefix}general")
(load "{prefix}orb")
#load-if-not-defined DIFFICULTY-EASIEST
#load-if-not-defined DIFFICULTY-EASY
#load-if-not-defined DIFFICULTY-MODERATE
#load-if-not-defined INFINITE-RESOURCES-START
(load "{prefix}boarhunting")
#end-if
#end-if
#end-if
#end-if
(load "{prefix}researches")
(load "{prefix}interaction")
(load "{prefix}buildings")
(load "{prefix}units")
(load "{prefix}trade")
(load "{prefix}resign")
#else
(load "{prefix}finaling")
#end-if
(load "{prefix}event")

(include "ailib/Geometry.xs")
'''


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Fork docs/Promisory into a self-contained strategy package")
    parser.add_argument("name", help="strategy stem, e.g. strat_micro_v1")
    parser.add_argument("--output", default="tournament",
                        help="directory for name.per and name/ (default: tournament)")
    parser.add_argument("--source", default="docs/Promisory",
                        help="Promisory source directory (default: docs/Promisory)")
    parser.add_argument("--force", action="store_true",
                        help="replace an existing loader/package with this name")
    args = parser.parse_args()

    if not re.fullmatch(r"[A-Za-z0-9_-]+", args.name):
        parser.error("name may contain only letters, numbers, underscores, and hyphens")

    source = Path(args.source).resolve()
    output = Path(args.output).resolve()
    loader = output / (args.name + ".per")
    package = output / args.name
    fork = package / "Promisory"

    if not source.is_dir():
        parser.error("source directory does not exist: %s" % source)
    if (loader.exists() or package.exists()) and not args.force:
        parser.error("strategy already exists; choose another name or pass --force")

    output.mkdir(parents=True, exist_ok=True)
    if package.exists():
        shutil.rmtree(package)
    if loader.exists():
        loader.unlink()

    shutil.copytree(source, fork)

    # All AI load paths resolve from the game's root AI directory, not relative
    # to the currently loaded file. Namespace every internal dependency load.
    for per_file in fork.rglob("*.per"):
        text = per_file.read_text(encoding="utf-8")
        text = text.replace("Promisory\\", args.name + "\\Promisory\\")
        text = text.replace("Promisory/", args.name + "/Promisory/")
        per_file.write_text(text, encoding="utf-8")

    loader.write_text(loader_text(args.name), encoding="utf-8")
    print("created loader: " + str(loader))
    print("created package: " + str(package))
    print("edit combat behavior under: " + str(fork))


if __name__ == "__main__":
    main()
