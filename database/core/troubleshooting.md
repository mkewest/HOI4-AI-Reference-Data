---
domain: core
concept: troubleshooting
version: 1.14+
requires: [mod_structure, file_syntax]
relates: [debug_tools, provinces, states, military]
---

# Troubleshooting

Diagnosing HOI4 crashes and errors requires understanding crash types, common failure patterns, and systematic debugging strategies. Most crashes leave diagnostic traces in log files that point to the underlying issue.

## Crash Types

### Fatal Crashes

Fatal crashes terminate the game immediately and write stack traces to `exceptions.log`. These occur during loading or when specific actions trigger critical failures.

Fatal crashes typically happen at:

- **Loading:** File parsing errors, memory exhaustion, missing required data
- **Specific actions:** Invalid state references, null pointers, overflow conditions

### Non-Fatal Errors

Non-fatal errors appear in `error.log` but don't crash the game. The game continues running with degraded functionality or visual glitches.

## Loading Phase Crashes

### Main Menu Crashes

Crashes during main menu loading indicate fundamental content errors:

**cosmetic.txt crash:** Caused by complete overwrite of `common/national_focus/` or `common/continuous_focus/` directories using replace_path without providing replacement files. The game expects at minimum one focus tree and crashes when none exist.

**rocketsites.txt crash:** Caused by complete overwrite of `history/states/` or `common/unit_leader/` directories. Similar to cosmetic.txt, the game requires baseline content and crashes when completely empty.

**railroad.shader crash:** BMP file format errors in map files. Occurs when:

- Provinces.bmp dimensions are not multiples of 256
- File size exceeds 40 MiB
- Dimension mismatch between files that should share dimensions
- Wrong DIB header type (must be BITMAPINFOHEADER, not BITMAPV5HEADER)

**general_countries_rocketsites crash:** Victory points referencing non-existent province IDs. The game tries to place the VP marker and crashes when the province doesn't exist.

**savegame_cities crash:** Too many countries exist (limit is 40-80, varies inconsistently). Requires sufficient dynamic countries to be defined in game files.

### File Loading Order

Files load sequentially:

1. `history/general/*.txt`
2. `history/countries/*.txt`
3. `map/rocketsites.txt`

Understanding this sequence helps identify which file category caused crashes when setup.log shows partial loading.

## Country Selection Crashes

Crashes when selecting a country indicate country-specific initialization issues:

**set_controller crash:** Country lacks a valid capital definition in its `history/countries/TAG*.txt` file. Every country must have a capital province assigned.

**history/units crash:** Two primary causes:

- Carrier with airwings directly inside (pre-1.12 format) rather than using the 1.12+ carrier air wing structure
- Division template without matching entry in `common/ai_templates/`

**supply_files crash:** Buildings defined on invalid or non-existent province IDs in `map/buildings.txt`.

**tutorial.txt crash:** Invalid state ID referenced in tutorial definitions, or missing `tutorial = {}` block in the tutorial file. Note that tutorial.txt is the last file read after country selection, but this doesn't mean it caused the crash - check earlier files first.

## Mid-Game Crashes

Crashes during gameplay have different patterns than loading crashes:

**client_ping_hourly crash:** AI-related issues, primarily:

- Division template without `common/ai_templates/` entry added during gameplay
- State with no owner (ownerless states are always unstable)
- Incomplete `map/buildings.txt` missing required coastal connections

**buildings_incomplete crash:** Missing naval base connections cause infinite pathfinding loops. The game repeatedly attempts to obtain naval base information, overloading CPU and GPU until crash. Error message: "Province <id> is setup as coastal but has no port building in the nudger."

## Specialized Crash Patterns

### State Without Owner

> [!CRITICAL] States with no owner are always unstable, not just for AI crashes. Actions that crash include: right-clicking the state, transferring the state ownership, and running air missions over the state. AI evaluating air mission value over an ownerless state causes instant CTD.

Always ensure every state has an owner defined in history files. Temporary ownerless states during civil wars or dynamic country creation should last only a single tick.

### AI Template Crash

Division templates without matching `common/ai_templates/` entries crash at two distinct times:

1. **Country selection:** If the template exists in OOB files, crash shows `history/units/filename.txt` as last read
2. **Mid-game:** If the template is added during gameplay, crash shows `client_ping` or `hourly_tick`

The crash timing depends on when the country obtains the template. The file shown as last read is not necessarily the crashing file - it's the file being processed when the crash occurred.

### Naval Base Building Crash

Incomplete `map/buildings.txt` doesn't cause immediate crashes. Instead, it creates an infinite loop where the game repeatedly attempts to obtain naval base information. This appears as CPU/GPU overload followed by eventual crash or freeze.

The diagnostic error appears in logs: "Province <id> is setup as coastal but has no port building in the nudger."

### Countries Limit Crash

The game handles between 40-80 countries, but the exact limit is non-consistent across different configurations. Exceeding this limit shows as crashes referencing `savegame.hoi4` or `map/cities.txt`.

This requires sufficient dynamic countries to be defined in `common/country_tags/`. Without enough dynamic tag definitions, the game can't handle civil wars and dynamic country creation.

### Bitmap Constraints Crash

Province bitmap files have strict technical requirements:

- **provinces.bmp:** Dimensions must be divisible by 256 (both width and height)
- **provinces.bmp:** File size must be under 40 MiB
- **trees.bmp:** Allowed to have different dimensions than provinces.bmp (controls static model density)
- **DIB header:** Must be BITMAPINFOHEADER type (not BITMAPV5HEADER)
- **DIB header:** Must not specify encoding usage

Violating these constraints causes railroad.shader crashes during main menu loading.

### Special Case Crashes

**Non-existent province in victory_points:** Crashes during main menu loading when `history/countries/` or `history/states/` files reference non-existent provinces in victory_points blocks.

**shared_focus crash:** Using `shared_focus = <n>` with a non-existent focus ID only crashes if it's the last line of the last national focus file parsed. Earlier occurrences or mid-file occurrences don't crash.

## Debugging Strategies

### Binary Search

Remove or add files in chunks to isolate the problematic content. Start by disabling half your mod, then narrow down by halves until you identify the specific file.

### Error Log Cleaning

Clean error.log before debugging sessions. Launch the game, let it load fully, then check for new errors. This isolates current issues from historical noise.

### Empty File Handling

Empty files are skipped entirely by the game reader. Don't create empty placeholder files expecting them to load - the game treats them as non-existent.

### Defines Override

When overriding defines, create a separate file with only the specific defines you need to change. Never copy the entire `00_defines.lua` or `00_graphics.lua` files - they change in minor updates, and missing defines cause crashes.

## Crash Data Log Analysis

When using `-crash_data_log`, the `crashes/meta.yml` file shows:

- **LastRead:** File and line number where parsing stopped
- **debug_enabled:** Whether debug mode was active

> [!CRITICAL] If LastRead shows the last line of a file, the crash likely occurred during the NEXT file's loading, not the shown file. The log indicates where parsing stopped, not necessarily what crashed.

The game can report "script" instead of a filename, indicating the crash occurred in savefile processing or client_ping events rather than file loading.

## Common Error Patterns

### Crash Cascade Pattern

Complete overwrites of certain directories trigger crashes in seemingly unrelated files:

- Overwriting `common/national_focus/` or `common/continuous_focus/` → crashes in cosmetic.txt
- Overwriting `history/states/` or `common/unit_leader/` → crashes in rocketsites.txt

This occurs because the game loads files in sequence and expects baseline content from earlier loads. When that content is missing, later files that depend on it crash.

### Silent Failures

Some errors don't generate log entries:

- **Encoding mismatches:** Files load but content is ignored
- **Missing dependencies:** Referenced content doesn't exist but no error
- **Invalid cross-references:** Broken links between files

Use systematic testing to identify silent failures - enable features one at a time and verify they work.

## Related Systems

- Debug tools and logging: See [Debug Tools](/core/debug_tools.md)
- Crash data log usage: See [Debug Tools](/core/debug_tools.md#crash-data-log)
- Map file constraints: See [Provinces](/map/provinces.md)
- State definitions: See [States](/entities/states.md)
- Building system: See [Buildings](/map/buildings.md)
