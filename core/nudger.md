---
domain: core
concept: nudger
version: 1.14+
requires: [debug_tools, map_structure]
relates: [states, strategic_regions, supply]
---

# Nudger

The nudger is a map editing tool accessible in debug mode that allows direct manipulation of states, strategic regions, provinces, weather, buildings, and supply networks. Understanding its output behavior and limitations is critical for avoiding crashes and data corruption.

## Accessing the Nudger

Two access methods exist:

**Main menu (debug mode):** Launch with `-debug` flag and access from main menu. This is the recommended method.

**Console command:** Type `nudge` in the console. This method avoids some crashes but causes a CTD when exiting the nudger.

To exit the nudger, use the "Leave nudge" button. Exiting via console entry causes a crash.

## Output Location and Loading Priority

> [!CRITICAL] The nudger outputs files directly to the user directory, not to your mod directory. These files load in the base game unless moved to your mod folder. Leaving nudger output in the user directory causes crashes and map errors when launching without debug mode.

Generated files that overwrite or unload mod content appear to revert during development, but the files remain in the user directory and continue loading. Always check `<user_dir>/` after using the nudger and move files to your mod directory.

## States Section

The states editor modifies state definitions, strategic region assignments, and generates localisation.

### Output Files

The states section generates three file types:

- **history/states/**: State definition files
- **map/strategicregions/**: Strategic region updates
- **localisation/english/state_names_l_english.yml**: State name localisation

### State Operations

**Select (click):** Choose single state

**Shift+click:** Add or remove state from selection

**create_state:** Generate new state from selected provinces

**delete_state:** Remove state definition

**open_file:** Open state file in text editor

**find_collision:** Identify province assignment conflicts

### State Naming

> [!CRITICAL] State names must be ASCII filename-safe characters only. Using non-ASCII or special characters causes the game to crash after removing provinces from the old state but before creating the new state file.

Creating a new state requires subsequent adjustment of building positions and airport/rocket locations in the buildings section.

### State File Quirks

The nudger removes quotation marks from state files except for the `name` attribute. This breaks `has_dlc` checks since DLC names require quotation marks.

The nudger writes `version=-1` for versionless localisation values, causing "Expected quotation mark" errors in the localisation file. Manually correct these to `version:0` or remove the version number entirely.

### State Deletion

The "Delete state" operation doesn't actually delete if loaded mod files contain the same state ID. Instead, the game reloads that version from the mod files, making deletion appear to fail.

### Open File Behavior

The "Open file" operation creates a copy from memory if the user directory lacks the file. This copy lacks any recent nudger changes, creating confusion about which version is authoritative.

The "Save" operation purges memory and reloads files from disk, so mod files that overwrite user directory files make changes appear to revert even though the user directory file was modified correctly.

## Strategic Regions Section

Strategic region assignments update automatically when state borders change. This ensures provinces remain properly assigned to regions.

### Unassigned Province Handling

> [!CRITICAL] When adding a province not currently in any state to a new state, the nudger adds it to a strategic region without checking if it's already assigned. This can cause provinces to be defined in multiple strategic regions, breaking the game's assumption of single-region assignment.

Always verify strategic region assignments after creating new states from unassigned provinces.

## Database Section

The database editor manipulates province definitions in `map/definition.csv`.

### Output Files

- **definition.csv.cache:** Binary cache of province data
- **definition.csv.fixed.csv:** Auto-generated corrected definitions

The game prioritizes `definition.csv.fixed.csv` over `definition.csv` if both exist. After manually fixing issues in definition.csv, you must delete the .fixed.csv file or the game continues loading the old corrected version.

### Database Operations

**generate_rgb:** Auto-generate unused RGB colors for new provinces

**type (sea/lake/land):** Change province type

**coastal:** Toggle coastal status

**continent:** Assign continental region

**show_colors:** Display color-to-province mapping

### Critical Crash Pattern

> [!CRITICAL] Most database buttons crash if no playthrough has been started first. Workaround: start the game, begin a playthrough, exit to menu, then use the nudger. Console entry to nudger avoids this crash but causes a crash when leaving the nudger.

The world map stays static after the first change is made. Refresh the display by switching tabs or exiting and re-entering the nudger.

## Weather Section

The weather editor modifies strategic region weather patterns.

### Output Files

- **map/strategic_regions/**: Updated region weather blocks
- **map/weatherpositions.txt**: Weather visualization positions

### Critical Design Flaw

> [!CRITICAL] Weather periods are GLOBAL, not region-specific. Editing weather in the nudger affects ALL strategic regions simultaneously, not just the currently selected one.

This makes the nudger unsuitable for creating region-specific weather variations. Manual editing of strategic region files is necessary for differentiated weather patterns.

### Weather Position Generation

Random position generation creates 2 large weather visualization positions if the region has none. These positions determine where weather effects render on the map.

A strategic region must be selected before accessing weather editing, or the operation fails.

## Buildings Section

The buildings editor positions 3D models, assigns naval provinces, and sets airbase/rocket site locations.

### Purpose

This section serves three primary functions:

- Positioning building models on the map
- Assigning naval provinces for ports and naval bases
- Setting airbase and rocket site locations for states

### Crash Risk

> [!CRITICAL] Creating a new state without adjusting building positions causes crashes. New states require building position initialization before they can be used safely.

The crashes occur because the game expects building position data for all states, and uninitialized states have null or invalid position references.

## Supply Section

The supply editor creates and modifies supply nodes and railway networks.

### Output Files

- **map/supply_nodes.txt:** Supply hub positions
- **map/railways.txt:** Railway network definitions

### Critical Control Issue

> [!CRITICAL] Releasing the Ctrl key immediately exits railway edit mode and loses all unsaved path changes. Hold Ctrl throughout the entire railway path creation process.

### Supply Node Operations

**Update:** Rereads `supply_nodes.txt` only, ignores railways.txt, cannot delete nodes from memory

**Load:** Rereads both files but cannot delete supply nodes from memory

**Save:** Writes changes, purges railway memory, rereads files, but cannot delete supply nodes

The only way to remove a supply node from memory is individual deletion using the delete operation. The Update, Load, and Save operations all preserve nodes in memory regardless of file contents.

### Railway Behavior

Created railways don't exist until the "Add Railway" button is used. Railway paths can cross impassable borders between individual provinces, which may create connectivity the game doesn't support.

Railway level settings above the maximum reset to level 1 when creating the railway. Always verify level values before confirming creation.

Railway selection on overlap only selects the first-defined railway in the file. To edit overlapping segments, temporarily remove or rename earlier railways.

### Building Priority

The gizmo display prioritizes buildings in this order: capital > naval_base > supply_hub. Lower-priority buildings may be difficult to select when higher-priority ones occupy the same province.

### Supply Node Crashes

> [!CRITICAL] The supply tab crashes on selection if supply_nodes.txt or railways.txt reference non-existent provinces. Verify all province IDs exist in definition.csv before opening the supply section.

## Supply Areas (Removed)

The supply areas system was removed in version 1.11. References to supply areas in older content are deprecated and non-functional.

## Related Systems

- Debug mode access: See [Debug Tools](/core/debug_tools.md)
- State definitions: See [States](/map/states.md)
- Strategic regions: See [Strategic Regions](/map/strategic_regions.md)
- Supply system: See [Supply](/map/supply.md)
- Province definitions: See [Provinces](/map/provinces.md)
