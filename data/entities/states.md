---
domain: entities
concept: states
version: 1.14+
requires: [provinces, strategic_regions]
relates: [buildings, victory_points, manpower, state_categories]
---

# State System

States are the primary administrative and economic units in HOI4. They group multiple provinces together for resource management, building construction, and manpower recruitment. States are defined in `history/states/*.txt` files.

## State File Structure

```hoi4
state = {
    id = 1
    name = "STATE_1"
    manpower = 1000000
    
    state_category = city
    
    provinces = {
        1 2 3 4 5
    }
    
    history = {
        owner = TAG
        buildings = {
            infrastructure = 5
            industrial_complex = 3
        }
        victory_points = {
            1 10
        }
    }
}
```

Files are encoded in UTF-8 without BOM. The entire state definition wraps in a `state = { ... }` block.

## Mandatory Attributes

Five attributes are required in every state:

```yaml
id: Unique sequential integer identifier
name: Localization key for state name
manpower: Integer population value
state_category: Reference to common/state_category/*.txt
provinces: Array of province IDs that compose the state
```

States without these attributes fail to load or cause errors during initialization.

## State ID Management

> [!CRITICAL] State IDs must be sequential starting from 1 with no gaps. Missing or skipped IDs cause the game to crash on load in non-debug mode. The crash occurs during state initialization before the main menu.

When deleting states from a mod:
1. Renumber all remaining states to fill gaps
2. Search and replace all references to renumbered states across the entire mod
3. Check history files, events, decisions, focuses, and scripted effects

State IDs in filenames are not parsed. Both base game files and mod files load if `replace_path` is not defined in the mod descriptor. Filename-based organization is cosmetic only.

## State Ownership

```hoi4
history = {
    owner = TAG
    controller = TAG
}
```

**Owner:** The owning country controls the state's resources, manpower, and buildings. States require an owner for most functionality.

> [!CRITICAL] States without an owner appear to function normally during gameplay, but any effect that targets the state causes an immediate crash. Avoid creating ownerless states unless they are strictly cosmetic wasteland that no scripting can reference.

**Controller:** The controlling country has military control of the state. The `controller` attribute is optional when it matches the owner. Only specify controller when it differs from owner (military occupation scenarios).

## Province Assignment

```hoi4
provinces = {
    1 2 3 4 5
}
```

The `provinces` array lists all province IDs that belong to this state. Provinces cannot be shared between states; each province belongs to exactly one state.

> [!CRITICAL] All provinces in a state must be in the same strategic region. Any province in a different strategic region than the state's other provinces causes a MAP_ERROR on launch and crashes in non-debug mode.

Strategic region boundaries and state boundaries must align exactly. Use the nudger or error log to verify strategic region assignment matches state groupings.

## State Categories

State categories determine building slot availability and are defined in `common/state_category/*.txt`:

```hoi4
state_category = large_city
```

Categories function as modifiers with a `local_building_slots` attribute:

| Category | Building Slots |
|----------|---------------|
| wasteland | 0 |
| pastoral | 1 |
| rural | 2 |
| town | 4 |
| large_town | 5 |
| city | 6 |
| large_city | 8 |
| metropolis | 10 |
| megalopolis | 12 |

Higher categories provide more building slots for infrastructure, factories, and military installations. Categories can define custom modifiers beyond slot counts.

## Manpower

```hoi4
manpower = 5000000
```

The manpower value applies to all scenarios without growth simulation between bookmarks. When a scenario starts, a single tick of 0.25% monthly growth applies once.

The 1936 and 1939 scenarios start with the same base manpower values plus one application of the monthly growth modifier. This means population increases slightly between bookmarks but does not simulate continuous growth.

Manpower represents recruitment pool size and limits how many divisions can be trained from the state.

## Resources

```hoi4
resources = {
    steel = 10
    aluminium = 5
    oil = 20
}
```

The optional `resources` block defines strategic resource deposits in the state. Resource amounts are integers representing daily production when the state is fully controlled and has sufficient infrastructure.

## Local Supplies

```hoi4
local_supplies = 5.0
```

The optional `local_supplies` attribute affects supply calculations. The value converts at a rate of 1.0 = 0.2 supply. This represents local supply generation beyond infrastructure-based supply.

## Buildings

Buildings in states are defined within the history block and can use datestamps for scenario-specific configurations.

### Building Declaration

```hoi4
history = {
    buildings = {
        infrastructure = 5
        industrial_complex = 3
        air_base = 2
        anti_air_building = 1
        
        12 = {
            naval_base = 4
            coastal_bunker = 2
        }
    }
}
```

**State-level buildings** (infrastructure, factories, etc.) are specified directly with their level.

**Province-level buildings** (naval bases, coastal bunkers, etc.) are nested under province ID blocks.

> [!CRITICAL] Coastal buildings (naval_base, coastal_bunker, dockyard) cannot be defined in landlocked states even with level 0. Including these buildings in a landlocked state's definition causes errors or crashes. Only include coastal buildings in states with at least one coastal province.

### Building Datestamps

```hoi4
history = {
    buildings = {
        infrastructure = 3
    }
    
    1939.1.1 = {
        buildings = {
            infrastructure = 5
            industrial_complex = 2
        }
    }
}
```

Buildings inside datestamp blocks follow special rules:
- Undefined buildings keep their current value (they do not reset to 0)
- Defined buildings set to their specified value
- This allows incremental building changes between scenarios

### Related Map Files

> [!CRITICAL] The `map/buildings.txt` file defines 3D model positions for buildings separately from state definitions. Mismatches between state building definitions and building position files create errors in the log and can cause crashes.

Required consistency with map files:
- `map/buildings.txt`: Building 3D model positions
- `map/airports.txt`: Airport positions and connectivity
- `map/rocketsites.txt`: Rocket site positions

> [!CRITICAL] Missing or incorrect entries in `map/airports.txt` or `map/rocketsites.txt` prevent the game from opening in non-debug mode. These files must exist and have valid entries for every state with airports or rocket sites.

Use the nudger's building section to generate and verify building positions match state definitions.

### Naval Base Crashes

> [!CRITICAL] Naval base or floating harbor mismatches between state definitions and `map/buildings.txt` cause "client_ping" crashes. This crash occurs when the game attempts to render naval units at positions that don't match building data.

Ensure every naval base defined in state files has a corresponding entry in `map/buildings.txt` with correct province ID and positioning.

## Victory Points

```hoi4
history = {
    victory_points = {
        12 5
    }
    victory_points = {
        15 10
    }
}
```

Victory points are assigned per province with the format `{ province_id amount }`.

> [!CRITICAL] Each `victory_points` block can contain only one province. Use multiple separate blocks to assign victory points to multiple provinces. Placing multiple provinces in a single block causes parsing errors.

Victory point icon positions are defined in `map/unitstacks.txt` and can be placed outside the province boundaries. The icon position does not need to be within the province's pixel area.

## Impassable States

```hoi4
impassable = yes
```

The optional `impassable` attribute marks states as completely impassable to land units. These states typically represent oceans, extreme mountains, or other terrain that cannot be traversed.

Impassable states still require valid province and strategic region assignments but do not need buildings or manpower values.

## Building Max Level Factor

```hoi4
buildings_max_level_factor = 1.5
```

The optional `buildings_max_level_factor` modifier affects maximum building levels in the state. A factor of 1.5 allows 50% more building levels than the base state category permits.

This modifier is multiplicative with other building slot modifiers from technologies, national spirits, and state modifiers.

## Date-Dependent History

States support date blocks for scenario-specific configurations:

```hoi4
history = {
    owner = GER
    buildings = {
        infrastructure = 5
    }
    
    1939.1.1 = {
        owner = POL
        buildings = {
            infrastructure = 6
            industrial_complex = 2
        }
    }
}
```

Date blocks use the format `YYYY.MM.DD = { ... }` and apply when the scenario start date is strictly later than the specified date. Starting exactly on the date does not trigger the date block.

## State Effects

States serve as scopes in effects and can be targeted directly:

```hoi4
123 = {  # State ID
    add_core_of = TAG
    add_claim_by = TAG
    add_building_construction = {
        type = industrial_complex
        level = 3
        instant_build = yes
    }
}
```

State scope enables localized effects, building construction, and ownership changes.

## Common State Issues

### MAP_ERROR on Launch

**Symptom:** The error log shows MAP_ERROR entries mentioning specific states.

**Cause:** Province in state is assigned to different strategic region than other provinces in state.

**Fix:** Verify all provinces in the state are in the same strategic region using the nudger or by checking `map/strategicregions/*.txt` files.

### Game Won't Open (Non-Debug)

**Symptom:** Game crashes before main menu with no error log.

**Causes:**
- State IDs are non-sequential or have gaps
- `map/airports.txt` is missing or has incorrect entries
- `map/rocketsites.txt` is missing or has incorrect entries

**Fix:** Verify state IDs are sequential from 1, check airport/rocketsite files exist and are properly formatted.

### Client_Ping Crash

**Symptom:** Game crashes with "client_ping" error when naval units spawn or move.

**Cause:** Naval base in state definition does not match entry in `map/buildings.txt`.

**Fix:** Use nudger to regenerate building positions or manually verify naval base positions match between state files and `map/buildings.txt`.

## Related Defines

- `STATE_VALUE_INFRASTRUCTURE`: See [NGame](/defines_list/NGame.md)
- `SUPPLY_FROM_LOCAL_SUPPLIES`: See [NSupply](/defines_list/NSupply.md)

## Related Systems

For province definitions and strategic region boundaries, see [Provinces](/map/provinces.md).

For strategic region configuration, see [Strategic Regions](/map/strategic_regions.md).

For building types and construction mechanics, see [Buildings](/map/buildings.md).
