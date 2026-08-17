"""Copy a strategy loader and its optional sibling dependency package."""

from pathlib import Path
import shutil


def package_path(loader_path: Path) -> Path:
    """Return the optional package directory next to a strategy loader."""
    return loader_path.with_suffix("")


def copy_strategy(loader_path: Path, destination: Path) -> bool:
    """Copy ``name.per`` and optional sibling ``name/`` into destination.

    Existing copies of that exact package are replaced so removed or renamed
    dependency files cannot linger between smoke tests or tournament runs.
    Returns True when a package directory was copied.
    """
    loader_path = loader_path.resolve()
    destination = destination.resolve()
    destination.mkdir(parents=True, exist_ok=True)

    loader_dest = destination / loader_path.name
    if loader_path != loader_dest:
        shutil.copy2(loader_path, loader_dest)

    source_package = package_path(loader_path)
    if not source_package.is_dir():
        return False

    package_dest = destination / source_package.name
    if source_package == package_dest:
        return True
    if package_dest.is_dir():
        shutil.rmtree(package_dest)
    elif package_dest.exists():
        package_dest.unlink()
    shutil.copytree(source_package, package_dest)
    return True
