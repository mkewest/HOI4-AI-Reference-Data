from __future__ import annotations

import json
from pathlib import Path

from helper_scripts.docs_grabber import grab_docs
from helper_scripts.docs_pruner import prune_and_diff


def prompt_game_path() -> Path:
    while True:
        user_input = input("Path to HOI4 game folder (must contain hoi4.exe): ").strip('" ')
        if not user_input:
            continue
        path = Path(user_input).expanduser().resolve()
        if (path / "hoi4.exe").exists():
            return path
        print(f"hoi4.exe not found in {path}. Try again.\n")


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent.parent
    update_root = repo_root / "update"

    current_patch_dir = update_root / "current_patch"
    last_patch_dir = update_root / "last_patch"
    changes_dir = update_root / "changes"
    archive_dir = update_root / "archive"
    database_dir = repo_root / "database"
    master_index = database_dir / "master_index.json"

    print("[update] Working directories:")
    print(f"  repo_root:        {repo_root}")
    print(f"  current_patch:    {current_patch_dir}")
    print(f"  last_patch:       {last_patch_dir}")
    print(f"  changes:          {changes_dir}")
    print(f"  archive:          {archive_dir}")
    print(f"  database:         {database_dir}")
    print(f"  master_index:     {master_index}")

    game_root = prompt_game_path()

    # Clean current_patch before grab
    if current_patch_dir.exists():
        for p in current_patch_dir.glob("*"):
            if p.is_file():
                p.unlink()
    else:
        current_patch_dir.mkdir(parents=True, exist_ok=True)

    # Step 1: grab docs
    print("\n[update] Step 1/2: grabbing documentation...")
    grab_docs(game_root, current_patch_dir)

    # Step 2: prune and diff
    print("\n[update] Step 2/2: pruning and diffing...")
    prune_and_diff(
        current_patch_dir=current_patch_dir,
        last_patch_dir=last_patch_dir,
        changes_dir=changes_dir,
        archive_dir=archive_dir,
        database_dir=database_dir,
        master_index_path=master_index,
    )

    print("\n[update] Done.")


if __name__ == "__main__":
    main()

