"""
Update defines_list markdown files from HOI4 00_defines.lua / 00_graphics.lua.

Steps (per Instructions_update_defines_python_script.md):
- Prompt for HOI4 root directory and verify hoi4.exe exists.
- Read common/defines/00_defines.lua and 00_graphics.lua.
- Split by root categories (NGame, NAI, NGraphics, etc.).
- Convert each category's entries into a YAML code block.
- Update existing database/defines_list/NCategory.md codeblocks (preserve frontmatter).
- If a category file is missing, create it under update/defines_update/new_files/
  with template frontmatter and the YAML block.
"""
from __future__ import annotations

import re
import textwrap
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional


DEFINE_FILES = ["00_defines.lua", "00_graphics.lua"]


@dataclass
class DefineEntry:
    key: str
    value: str
    dtype: str
    comment: Optional[str] = None


def prompt_root() -> Path:
    """Ask for HOI4 root until hoi4.exe is found."""
    while True:
        raw = input("Enter HOI4 root directory: ").strip().strip('"')
        root = Path(raw)
        exe = root / "hoi4.exe"
        if exe.exists():
            return root
        print(f"hoi4.exe not found in {root}. Try again.")


def infer_type(value: str) -> str:
    """Infer a simple type from the value string."""
    val = value.strip()
    val_no_quotes = val.strip("'\"").strip()
    lower = val_no_quotes.lower()

    if lower in {"true", "false"}:
        return "bool"
    if re.match(r"^-?\d+$", lower):
        return "int"
    if re.match(r"^-?\d*\.\d+(e[+-]?\d+)?$", lower) or re.match(
        r"^-?\d+e[+-]?\d+$", lower
    ):
        return "float"
    if val_no_quotes.startswith("{") and val_no_quotes.endswith("}"):
        return "table"
    return "string"


def clean_value(value: str) -> str:
    """Strip trailing commas and surrounding quotes; keep inner content."""
    trimmed = re.sub(r",\s*$", "", value.strip())
    if (trimmed.startswith('"') and trimmed.endswith('"')) or (
        trimmed.startswith("'") and trimmed.endswith("'")
    ):
        return trimmed[1:-1]
    return trimmed


def wrap_comment(comment: str) -> List[str]:
    """Wrap comment text with YAML indentation."""
    wrapped = textwrap.fill(
        comment,
        width=88,
        initial_indent="  cmt: ",
        subsequent_indent="    ",
    )
    return wrapped.splitlines()


def parse_defines_file(path: Path) -> Dict[str, List[DefineEntry]]:
    """Parse a defines lua file into category -> entries."""
    categories: Dict[str, List[DefineEntry]] = {}
    current: Optional[str] = None
    in_root = False

    for raw_line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("--"):
            continue

        root_match = re.match(r"NDefines(_Graphics)?\s*=\s*\{\s*$", line)
        if root_match:
            in_root = True
            continue

        if current is None and in_root:
            cat_match = re.match(r"([A-Za-z0-9_]+)\s*=\s*\{\s*$", line)
            if cat_match:
                cat = cat_match.group(1)
                if cat in {"NDefines", "NDefines_Graphics"}:
                    continue
                current = cat
                categories.setdefault(current, [])
            elif line.startswith("}"):
                in_root = False
            continue

        if line.startswith("}"):
            current = None
            continue

        kv_match = re.match(r"([A-Za-z0-9_]+)\s*=\s*(.+)", line)
        if not kv_match or current is None:
            continue

        key = kv_match.group(1)
        remainder = kv_match.group(2)

        comment: Optional[str] = None
        if "--" in remainder:
            remainder, comment = remainder.split("--", 1)
            comment = comment.strip().rstrip(",")

        value = remainder.strip()
        if value.endswith(","):
            value = value[:-1].rstrip()

        clean_val = clean_value(value)
        dtype = infer_type(clean_val)

        categories[current].append(
            DefineEntry(key=key, value=clean_val, dtype=dtype, comment=comment or None)
        )

    return categories


def build_yaml_block(entries: Iterable[DefineEntry]) -> str:
    """Build the YAML code block content for a category."""
    lines: List[str] = []
    for entry in entries:
        lines.append(f"{entry.key}:")
        lines.append(f"  def: '{entry.value}'")
        lines.append(f"  type: {entry.dtype}")
        if entry.comment:
            lines.extend(wrap_comment(entry.comment))
    return "\n".join(lines) + "\n"


def replace_codeblock(content: str, yaml_block: str) -> str:
    """Replace the first ```yaml ... ``` block; append if not present."""
    fenced = f"```yaml\n{yaml_block}```"
    pattern = re.compile(r"```yaml\s*.*?```", re.DOTALL)
    if pattern.search(content):
        return pattern.sub(fenced, content, count=1)
    return content.rstrip() + "\n\n" + fenced + "\n"


def write_new_file(path: Path, category: str, yaml_block: str) -> None:
    """Create a new category file with template frontmatter."""
    template = (
        "---\n"
        "domain: defines_list\n"
        f"concept: {category}\n"
        "version: !UPDATE THIS!\n"
        "requires: [!UPDATE THIS!]\n"
        "relates: [!UPDATE THIS!]\n"
        "---\n\n"
        f"```yaml\n{yaml_block}```\n"
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(template, encoding="utf-8")


def process_category(
    category: str,
    entries: List[DefineEntry],
    defines_dir: Path,
    new_files_dir: Path,
) -> None:
    """Update or create the markdown file for a category."""
    if not entries:
        return

    yaml_block = build_yaml_block(entries)
    target = defines_dir / f"{category}.md"

    if target.exists():
        original = target.read_text(encoding="utf-8")
        updated = replace_codeblock(original, yaml_block)
        target.write_text(updated, encoding="utf-8")
        print(f"Updated {target.relative_to(defines_dir.parent)}")
    else:
        new_path = new_files_dir / f"{category}.md"
        write_new_file(new_path, category, yaml_block)
        print(f"Created {new_path.relative_to(new_files_dir.parent)}")


def main() -> None:
    root = prompt_root()
    defines_paths = []
    for name in DEFINE_FILES:
        path = root / "common" / "defines" / name
        if path.exists():
            defines_paths.append(path)
        else:
            print(f"Warning: {path} not found; skipping.")

    if not defines_paths:
        print("No defines files found. Nothing to do.")
        return

    repo_root = Path(__file__).resolve().parents[2]
    defines_dir = repo_root / "database" / "defines_list"
    new_files_dir = repo_root / "update" / "defines_update" / "new_files"

    aggregated: Dict[str, List[DefineEntry]] = {}
    for path in defines_paths:
        parsed = parse_defines_file(path)
        for category, items in parsed.items():
            aggregated.setdefault(category, []).extend(items)

    for category, entries in aggregated.items():
        process_category(category, entries, defines_dir, new_files_dir)

    print("Done.")


if __name__ == "__main__":
    main()

