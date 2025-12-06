---
domain: core
concept: metadata
version: 1.14+
requires: [mod_structure]
relates: [load_order, achievements]
---

# Metadata

HOI4 uses several metadata systems to track mod compatibility, validate content integrity, and control special game features. Understanding checksums and special files helps ensure proper mod behavior.

## Checksum System

The checksum is a 4-character hash that determines multiplayer compatibility and achievement eligibility.

### Checksum Calculation

The checksum incorporates content from:

- `common/`
- `events/`
- `history/`
- `map/` (except terrain files)

Changes to these directories modify the checksum, while modifications to interface, graphics, and sound files do not affect it.

### Checksum Purpose

The checksum serves two critical functions:

**Multiplayer compatibility:** Players must have identical checksums to join the same multiplayer game. Different checksums indicate incompatible game rules or content.

**Achievement eligibility:** Modified checksums disable achievement earning. Only cosmetic mods (interface, graphics, sound) that don't change the checksum allow achievements.

### Checksum Manifest

The game creates `checksum_manifest.txt` in the game directory, listing all files and content that contribute to checksum calculation. This file helps identify what changes will affect multiplayer compatibility.

## Order Matters Rules

Different content types have varying sensitivity to definition order.

### Order-Sensitive Content

**Effects:** Execute sequentially in written order. Earlier effects modify state for later effects.

**Triggers:** Evaluate sequentially. Earlier triggers can set temporary variables used by later ones.

**Dynamic modifiers:** Order affects tooltip display and evaluation priority.

**Database entries:** Creation order affects evaluation order when the game iterates through entries.

### Order-Irrelevant Content

**Modifiers:** Static modifiers apply simultaneously regardless of definition order (except dynamic modifiers, which follow code order for tooltips).

### Duplicate Handling

When the same attribute appears multiple times, behavior varies by content type:

**National focus duplicates:** Break prerequisite line generation in the focus tree

**Event immediate blocks:** Each executes as a separate sequential block

**Idea category ideas:** Each becomes a separate idea

**Scripted localisation text blocks:** First valid one is used

Understanding duplicate handling helps diagnose unexpected behavior when content appears multiple times.

## Special Files

Several files have unique handling:

### Settings File

**Location:** `<user_dir>/settings.txt`

**Format:** Binary (only settings file uses binary format)

**Purpose:** Stores user preferences, graphics settings, and game options

This is the only file in the game that uses binary serialization rather than text format. Corruption of this file causes graphics and control setting resets.

### DLC Load File

**File:** `dlc_load.json`

**Purpose:** Lists enabled mods and DLC

**Format:** JSON array of enabled content identifiers

The launcher modifies this file when enabling or disabling mods. Manual editing can force specific mod combinations.

### Launcher Database

**File:** `launcher-v2.sqlite`

**Purpose:** Mod database for launcher interface

**Corruption handling:** Delete this file to force database rebuild

When the launcher shows "invalid path" errors that persist after fixing mod descriptors, deleting the SQLite database and allowing it to rebuild often resolves the issue.

## Related Systems

- Mod structure and descriptors: See [Mod Structure](/core/mod_structure.md)
- Load order determination: See [Load Order](/core/load_order.md)
- Load order determination: See [Load Order](/core/load_order.md)
- Multiplayer considerations: See multiplayer documentation
