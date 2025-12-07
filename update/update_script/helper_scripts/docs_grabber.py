from __future__ import annotations

import os
import shutil
from pathlib import Path
from typing import Iterable, Tuple


def _iter_targets(game_root: Path) -> Iterable[Tuple[Path, str]]:
    """
    Yield (source_path, new_filename) for every documentation file we want to grab.

    Rules:
    - Root-level "changelog.txt" if present, copied as "changelog.txt".
    - Exact filename match: "_documentation.md" anywhere under game_root.
      Destination filename is "{parent}_{original}" where parent is the containing
      folder name.
    - Any ".md" file under game_root / "documentation" (recursively).
      Destination filename is "{parent}_{original}" (parent is the immediate folder).
    """
    # 0) changelog.txt at root (if present)
    changelog = game_root / "changelog.txt"
    if changelog.exists() and changelog.is_file():
        yield changelog, "changelog.txt"

    # 1) Exact match "_documentation.md"
    for path in game_root.rglob("_documentation.md"):
        if not path.is_file():
            continue
        parent = path.parent.name or "root"
        # Avoid double underscore when the filename itself starts with "_"
        yield path, f"{parent}_documentation.md"

    # 2) All .md inside game_root / documentation (keep original filenames)
    docs_root = game_root / "documentation"
    if docs_root.exists():
        for path in docs_root.rglob("*.md"):
            if not path.is_file():
                continue
            yield path, path.name


def _unique_destination(dest_dir: Path, filename: str) -> Path:
    """
    Ensure no collisions. If filename exists, append _1, _2, ...
    """
    candidate = dest_dir / filename
    if not candidate.exists():
        return candidate
    stem, suffix = os.path.splitext(filename)
    counter = 1
    while True:
        candidate = dest_dir / f"{stem}_{counter}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def grab_docs(game_root: Path, output_dir: Path) -> None:
    """
    Copy (not move) documentation files from the HOI4 install into output_dir.
    """
    game_root = game_root.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"[docs_grabber] Game root: {game_root}")
    print(f"[docs_grabber] Output dir: {output_dir}")

    count = 0
    for source_path, new_name in _iter_targets(game_root):
        dest_path = _unique_destination(output_dir, new_name)
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, dest_path)
        count += 1
        print(f"  copied: {source_path.relative_to(game_root)} -> {dest_path.name}")

    if count == 0:
        print("  no documentation files found.")
    else:
        print(f"[docs_grabber] Done. Files copied: {count}")


if __name__ == "__main__":
    import sys

    """
    Standalone usage:
      python docs_grabber.py <hoi4_game_root> [output_dir]

    - <hoi4_game_root> must contain hoi4.exe
    - [output_dir] is optional; defaults to ./documentation_out in the current
      working directory when omitted.
    """
    if len(sys.argv) not in (2, 3):
        print("Usage: python docs_grabber.py <hoi4_game_root> [output_dir]")
        raise SystemExit(1)

    game_root_arg = Path(sys.argv[1])
    output_dir_arg = Path(sys.argv[2]) if len(sys.argv) == 3 else Path.cwd() / "documentation_out"

    grab_docs(game_root_arg, output_dir_arg)