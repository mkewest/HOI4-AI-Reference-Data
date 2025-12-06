---
domain: core
concept: mod_structure
version: 1.14+
requires: [file_syntax]
conflicts: [deprecated_workshop_archives_pre_1.9]
relates: [load_order]
---

# Mod Structure

HOI4 mods use a dual-descriptor system with separate files for the launcher and the mod itself. Understanding the relationship between user directory paths, descriptors, and the replace_path mechanism is essential for proper mod loading.

## Directory Paths

### User Directory

The user directory location varies by operating system:

- **Windows:** `C:/Users/<Username>/Documents/Paradox Interactive/Hearts of Iron IV/`
- **Mac:** `~/Documents/Paradox Interactive/Hearts of Iron IV/`
- **Linux:** `~/.local/share/Paradox Interactive/Hearts of Iron IV/`

Local mods are placed in `<user_dir>/mod/`, while Workshop mods install to Steam's workshop directory at `<steam>/steamapps/workshop/content/394360/<remote_file_id>`. Paradox Mods uses an alternative path at `<paradox>/Hearts of Iron IV/workshop/content/394360`.

> [!CRITICAL] Non-ASCII characters in the user directory path block ALL local mods from loading and prevent error log files from opening. Non-ASCII in the mod path itself causes that specific mod to fail loading entirely.

### Path Constraints

All paths must use forward slashes (`/`) as separators regardless of operating system. Non-ASCII characters are forbidden in multiple file types including leader traits and adjacency rules. Linux and Mac systems use case-sensitive file systems, so `Generic.txt` and `GENERIC.txt` are treated as different files and will both load even with replace_path active.

## Descriptor System

### Dual Descriptor Architecture

Every mod requires two descriptor files:

**User descriptor:** Located at `<user_dir>/mod/<name>.mod`, contains the `path` attribute pointing to mod files. Load order is determined by ASCII alphabetical sorting of the filename.

**Mod descriptor:** Located at `<mod_root>/descriptor.mod`, defines mod metadata but lacks the `path` attribute.

Both files must use UTF-8 encoding without BOM. Using UTF-8-BOM in descriptor files causes crashes or load failures. The launcher automatically removes attributes from the user descriptor if they're not present in the mod descriptor, so critical attributes must exist in both files.

### Descriptor Attributes

Common attributes shared between both descriptors:

**name** (required, string): Mod display name. Must be unique - if multiple mods share the same name, only the first loaded has any effect. Used for dependency matching, which requires exact character matches including special characters like en dashes versus hyphens.

**version** (optional, string): Mod version displayed in launcher.

**supported_version** (optional, string): Game version compatibility. Supports wildcards only in the third digit position (e.g., `1.5.*` is valid, but `1.*` is invalid).

**tags** (optional, array): Categories for launcher filtering. Values include "Alternative History", "Balance", "Gameplay", and others.

**dependencies** (optional, array): Forces this mod to load after specified mods. Matches by exact name string including special characters. Submods load after their dependencies regardless of alphabetical order.

**picture** (optional, string, max 1MB): Thumbnail image path relative to mod root. Works for Steam and Paradox Mods but is broken for local mods. Image must be located in mod root directory.

**User descriptor exclusive attributes:**

**path** (required, string): Points to mod folder using format `mod/<folder>`. Mandatory for local mods.

**Workshop exclusive attributes:**

**archive** (string): Path to mod archive file for older Workshop mods (pre-1.9.0 used .zip archives, now extracted).

**remote_file_id** (string): Workshop item ID.

**Special attributes:**

**user_dir** (string): Isolates save files to prevent conflicts. Mods using this attribute store saves separately.

### Encoding Requirements

Descriptor files follow strict encoding rules that differ from other file types:

- **descriptor.mod and user .mod files:** UTF-8 without BOM (opposite of localisation files)
- **Game script files (.txt):** UTF-8 without BOM
- **Localisation files (.yml):** UTF-8 with BOM required

Encoding mismatches cause silent load failures where the file appears present but content doesn't apply. Some editors like Atom don't fully support BOM, making them unsuitable for localisation editing.

## Replace Path System

The `replace_path` attribute unloads entire vanilla folders at main menu, allowing complete replacement of game databases.

### Basic Behavior

```hoi4
replace_path = "history/states/"
replace_path = "map/strategicregions"
```

Replace path must be specified in both descriptors or the launcher removes it from the user descriptor. The attribute only affects indexed files loaded at startup, not direct-linked files referenced by specific attributes.

Files load normally first, then get unloaded by replace_path at main menu. This means duplicate filename errors still appear in logs even if replace_path would theoretically prevent the conflict.

### Scope Limitations

Replace path does not affect subfolders - it only unloads files in the exact folder specified. To replace nested structures, you must specify each subfolder individually.

Replace path is useless for certain directories:

- **history/units:** Files are direct-linked via `oob = "TAG_1936"` attributes, not indexed
- **gfx/flags:** Flags load dynamically on ideology change, not during startup indexing
- **Main menu background:** Defined as sprite with explicit texture path, not indexed

Replace path does not change load order - it only unloads content. Use the `dependencies` attribute to control load sequencing.

### Critical Crash Risk

> [!CRITICAL] Replace path crashes the game if the resulting folder is completely empty. Folders that must never be empty include: common/national_focus, common/continuous_focus, history/states, and common/unit_leader. Complete overwrites of national_focus or continuous_focus cause crashes in cosmetic.txt parsing, while complete overwrites of history/states or unit_leader cause crashes in rocketsites.txt parsing.

This occurs because the game expects at minimum one valid entry in these databases. When using replace_path on essential folders, always ensure at least one file with valid content exists.

## Thumbnail

Mod thumbnails are defined by placing a `thumbnail.png` file in the mod root directory. The image must use PNG format with a 1:1 aspect ratio (recommended) and remain under 1MB file size. Thumbnails display in the launcher's mod selection interface.

## File Loading Behavior

### Load Sequence

The user directory loads before mods, which has implications for debugging. When the nudger outputs files directly to the user directory, they load in the base game even if mod files should override them. The files are created correctly but appear to be ignored due to this loading priority.

Empty files are skipped entirely by the game reader, which can mislead crash debugging efforts. If you create a placeholder file without content, the game behaves as if the file doesn't exist.

### File Parsing

Extra closing brackets stop file interpretation immediately - everything after the stray bracket is ignored. Empty arguments cause the next attribute to become the argument value. For example:

```hoi4
icon = 
x = 2
```

This makes `icon = x` and leaves `2` as a dangling value that breaks the next attribute.

Newlines are treated identically to spaces and tabs, so the entire file can technically be written on one line. The syntax does not support multi-line comment blocks.

### Debug Mode Limitations

Files in history/countries, history/states, and map/ do not auto-reload in debug mode even when modified. You must restart the game to see changes to these directories. Image loading in debug mode appears distorted until a full restart, not just a reload.

DLC files cannot be overridden in mod/dlc/ - you must match the actual load location where the game expects DLC content.

## Related Systems

- File syntax rules: See [File Syntax](/core/file_syntax.md)
- Load order determination: See [Load Order](/core/load_order.md)
- Checksum calculation: See [Metadata](/core/metadata.md)
