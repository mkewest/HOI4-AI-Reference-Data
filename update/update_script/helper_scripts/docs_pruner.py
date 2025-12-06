from __future__ import annotations

import hashlib
import json
import shutil
import zipfile
from datetime import date
from pathlib import Path
from typing import Dict, Iterable, List, Tuple
from difflib import unified_diff
import re


def _hash_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def _version_tuple(v: str) -> Tuple[int, ...]:
    return tuple(int(x) for x in v.split(".") if x.strip().isdigit())


def _crop_changelog(changelog: Path, last_version: str, out_path: Path) -> List[str]:
    """
    Keep only sections whose header version > last_version.
    Header format example:
    ########           Update 1.17.2.0 "Musketeer"         #########
    """
    if not changelog.exists():
        return []

    baseline = _version_tuple(last_version)
    keep_lines: List[str] = []
    current_block: List[str] = []
    current_ver: Tuple[int, ...] | None = None
    header_re = re.compile(r"Update\s+([\d\.]+)")

    with changelog.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            m = header_re.search(line)
            if m:
                # flush previous block
                if current_block and current_ver and current_ver > baseline:
                    keep_lines.extend(current_block)
                # start new block
                current_block = [line]
                current_ver = _version_tuple(m.group(1))
            else:
                current_block.append(line)

    # flush final block
    if current_block and current_ver and current_ver > baseline:
        keep_lines.extend(current_block)

    if keep_lines:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text("".join(keep_lines), encoding="utf-8")
    return keep_lines


def _diff_files(a: Path, b: Path, name: str) -> str:
    a_lines = a.read_text(encoding="utf-8", errors="ignore").splitlines(keepends=True)
    b_lines = b.read_text(encoding="utf-8", errors="ignore").splitlines(keepends=True)
    diff = unified_diff(
        a_lines,
        b_lines,
        fromfile=str(a),
        tofile=str(b),
        lineterm="",
    )
    return "\n".join(diff)


def _write_changes(changed: List[Tuple[str, Path, Path | None]], out_file: Path) -> None:
    """
    changed: list of (name, new_path, old_path|None)
    """
    out_file.parent.mkdir(parents=True, exist_ok=True)
    parts: List[str] = []
    for name, new_path, old_path in sorted(changed, key=lambda x: x[0]):
        parts.append(f"## {name}")
        if old_path is None:
            content = new_path.read_text(encoding="utf-8", errors="ignore")
            parts.append("```\n" + content + "\n```")
        else:
            diff = _diff_files(old_path, new_path, name)
            parts.append("```\n" + diff + "\n```")
        parts.append("")  # blank line between entries
    out_file.write_text("\n".join(parts), encoding="utf-8")


def _clean_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def _archive_snapshot(archive_dir: Path, database_dir: Path, last_patch_dir: Path) -> None:
    archive_dir.mkdir(parents=True, exist_ok=True)
    archive_name = archive_dir / f"{date.today()}.zip"
    with zipfile.ZipFile(archive_name, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for root in [database_dir, last_patch_dir]:
            if not root.exists():
                continue
            for path in root.rglob("*"):
                if path.is_file():
                    zf.write(path, arcname=path.relative_to(root.parent))

    # keep only 2 newest
    archives = sorted(archive_dir.glob("*.zip"), key=lambda p: p.stat().st_mtime, reverse=True)
    for old in archives[2:]:
        old.unlink()


def prune_and_diff(
    current_patch_dir: Path,
    last_patch_dir: Path,
    changes_dir: Path,
    archive_dir: Path,
    database_dir: Path,
    master_index_path: Path,
) -> None:
    current_patch_dir.mkdir(parents=True, exist_ok=True)
    last_patch_dir.mkdir(parents=True, exist_ok=True)
    changes_dir.mkdir(parents=True, exist_ok=True)

    # load baseline version
    if not master_index_path.exists():
        raise FileNotFoundError(f"master_index.json not found: {master_index_path}")
    with master_index_path.open(encoding="utf-8") as f:
        master_index = json.load(f)
    last_version = master_index.get("last_patch_version", "0.0.0")

    # crop changelog
    cropped = _crop_changelog(
        current_patch_dir / "changelog.txt",
        last_version,
        changes_dir / "changelog_cropped.txt",
    )
    # remove original changelog
    changelog_path = current_patch_dir / "changelog.txt"
    if changelog_path.exists():
        changelog_path.unlink()

    # compute hashes for identical pruning
    changed: List[Tuple[str, Path, Path | None]] = []
    for new_path in current_patch_dir.glob("*"):
        if not new_path.is_file():
            continue
        name = new_path.name
        old_path = last_patch_dir / name
        if old_path.exists() and _hash_file(new_path) == _hash_file(old_path):
            # identical; discard
            new_path.unlink()
            continue
        changed.append((name, new_path, old_path if old_path.exists() else None))

    if not changed and not cropped:
        print("[docs_pruner] No changes detected; skipping archive and rotation.")
        return

    # write changes.md
    _write_changes(changed, changes_dir / "changes.md")

    # archive snapshot BEFORE rotating last_patch
    _archive_snapshot(archive_dir, database_dir, last_patch_dir)

    # rotate: replace last_patch with current_patch contents
    _clean_dir(last_patch_dir)
    for src in current_patch_dir.glob("*"):
        if src.is_file():
            shutil.copy2(src, last_patch_dir / src.name)

    # clear current_patch after move
    _clean_dir(current_patch_dir)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 6:
        print(
            "Usage: python docs_pruner.py <current_patch_dir> <last_patch_dir> "
            "<changes_dir> <archive_dir> <database_dir> <master_index_path>"
        )
        raise SystemExit(1)

    prune_and_diff(
        Path(sys.argv[1]),
        Path(sys.argv[2]),
        Path(sys.argv[3]),
        Path(sys.argv[4]),
        Path(sys.argv[5]),
        Path(sys.argv[6]),
    )

