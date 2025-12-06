---
domain: database
concept: buildings
version: 1.14+
requires: [states, provinces]
relates: [supply, infrastructure, technologies_core]
---

# Buildings System

Buildings are defined in `common/buildings/*.txt` within a `buildings = {...}` root block. They represent constructible structures in states and provinces.

## Basic Structure

```hoi4
buildings = {
    building_id = {
        base_cost = 5000
        per_level_extra_cost = 1000
        
        shares_slots = no
        state_max = 10
        
        show_on_map = 1
        has_destroyed_mesh = yes
        
        modifiers = {
            production_speed_buildings_factor = 0.1
        }
        
        is_port = yes
    }
}
```

## Cost System

### base_cost

Required integer value representing the base construction cost in industrial capacity. This is the cost for level 1 or the initial level.

### per_level_extra_cost

Optional integer that uses arithmetic progression for multi-level buildings:

```text
Level 1 cost: base_cost
Level 2 cost: base_cost + per_level_extra_cost
Level 3 cost: base_cost + (per_level_extra_cost × 2)
Level n cost: base_cost + (per_level_extra_cost × (n-1))
```

Example with `base_cost = 1000` and `per_level_extra_cost = 500`:

- Level 1: 1000
- Level 2: 1500
- Level 3: 2000
- Level 4: 2500

### infrastructure_construction_effect

Boolean attribute. When enabled, infrastructure in the state provides a construction speed bonus:

- +10% construction speed per infrastructure level
- Maximum +50% bonus at infrastructure level 5

Note that production speed modifiers (e.g., `production_speed_buildings_factor`) with values >1.0 still count as only 1 factory for production purposes - the bonus doesn't add extra factory slots.

## Slot Categories

Buildings use three slot category systems:

### Shared Slots

```hoi4
shares_slots = yes
```

Shared slot buildings compete for space in the state's shared building pool, limited by the `MAX_SHARED_SLOTS` define.

> [!CRITICAL] `MAX_SHARED_SLOTS` is a per-state total, not a per-building-type limit. If `MAX_SHARED_SLOTS = 25`, a state can have any combination of shared-slot buildings totaling 25 (e.g., 15 civilian factories + 10 military factories).

### Non-Shared State Slots

```hoi4
state_max = 10
```

Each building type has its own independent cap. A `state_max = 10` means up to 10 of this specific building per state, regardless of other buildings.

If `state_max` is undefined, it defaults to `MAX_BUILDING_LEVELS` from defines.

### Provincial Buildings

```hoi4
province_max = 5
```

Provincial buildings are built in specific provinces rather than states. The building is positioned using `map/buildings.txt` (see Positioning section below).

Provincial buildings use `state_id` in the `buildings.txt` file to reference which state they belong to for ownership purposes.

## Level Caps and Relationships

### group_by

```hoi4
group_by = shared_slots
```

Groups buildings together for slot calculations. Buildings with the same `group_by` value share slot limitations.

### exclusive_with

```hoi4
exclusive_with = other_building_id
```

Prevents this building from coexisting with the specified building in the same state. Building one excludes the other.

## Technology Requirements

```hoi4
required_technologies = { tech_id }
```

Technologies can unlock buildings using the `enable_building` block in the tech definition. However, tech requirements only block manual construction through the GUI.

> [!CRITICAL] Buildings can be constructed via `add_building_construction` effects and state history files BEFORE technologies unlock them. Tech requirements are GUI restrictions only, not hard dependencies.

## Modifiers

### Country Modifiers

```hoi4
modifiers = {
    production_speed_buildings_factor = 0.1
    local_resources = 2
}
```

Modifiers apply to the state or country. They use standard country modifier syntax.

### enable_for_controllers

```hoi4
enable_for_controllers = { GER ITA }
```

Restricts modifiers to specific country tags. With an empty list `{}`, modifiers apply to ALL controllers (including occupation).

### show_modifier

```hoi4
show_modifier = no
```

Boolean. When `no`, hides the modifier in tooltips despite it being active. Useful for behind-the-scenes modifiers.

## Building Attributes

### value

Affects three separate systems:

1. **Base health:** Health for air bombing damage calculations
2. **Peace conference cost:** Points required to take in peace deals  
3. **PP occupation cost:** Political power needed to occupy states with these buildings

Higher values make buildings more expensive across all three dimensions.

### damage_factor

```hoi4
damage_factor = 0
```

Multiplier for damage received from strategic bombing. A value of 0 makes the building invulnerable to bombing. Default is 1 (normal damage).

### allied_build

```hoi4
allied_build = yes
```

Boolean. When `yes`, allows construction by:

- Subjects (puppets, dominions, etc.)
- Overlord (for their subjects)
- Faction members

This enables cooperative building within alliances.

### only_costal

```hoi4
only_costal = yes
```

> [!CRITICAL] The correct attribute spelling is "only_costal" (not "only_coastal"). This is a typo in the game's code that has become the standard spelling.

Boolean. When `yes`, the building can only be constructed in states with at least one coastal province. Any coastal province satisfies this requirement - it doesn't need to be a port or specific coastal type.

### disabled_in_dmz

```hoi4
disabled_in_dmz = yes
```

Boolean. When `yes`, the building cannot be constructed in demilitarized zones AND existing buildings become non-functional in DMZs.

This blocks both construction and usage, unlike tech requirements which only block construction.

### hide_if_missing_tech

```hoi4
hide_if_missing_tech = yes
```

Boolean. When `yes`, the building doesn't appear in the construction menu until unlocked by technology.

### is_buildable

```hoi4
is_buildable = no
```

Boolean. Default is `yes`. When `no`, the building cannot be manually constructed but can exist through history files or effects.

## Visual Display

### show_on_map

```hoi4
show_on_map = 2
```

Integer. Controls how many 3D models appear on the map:

- `0`: No models (building is invisible)
- `1-5`: Number of models to spawn
- Higher values spawn more models as the building level increases

### show_on_map_meshes

```hoi4
show_on_map_meshes = 3
```

Integer. Default is 1. Defines how many different mesh variations exist for this building.

### has_destroyed_mesh

```hoi4
has_destroyed_mesh = yes
```

Boolean. When `yes`, a destroyed variant of the model displays when the building takes damage.

### Entity Naming Convention

Building models follow specific naming patterns:

- **Undamaged:** `building_name_1`, `building_name_2`, `building_name_3` (starts at 1, not 0)
- **Destroyed:** `building_name_1_destroyed`, `building_name_2_destroyed`

The number suffix corresponds to mesh variations. If `show_on_map_meshes = 3`, you need models `_1`, `_2`, and `_3`.

### spawn_point (v1.16+)

```hoi4
spawn_point = {
    type = province
    max = 10
    only_costal = yes
}
```

Version 1.16+ feature that controls spawning behavior:

- `type`: `state` or `province`
- `max`: Maximum number of spawn points
- `only_costal`: Boolean, restricts to coastal provinces

## Positioning (buildings.txt)

The `map/buildings.txt` file defines 3D positions for buildings:

```text
<state_id>;<building_id>;<x>;<y>;<z>;<rotation>;<sea_province>
```

Example:

```text
1;naval_base;2500.5;12.3;1800.2;1.57;3456
```

### Coordinates

- **x, z:** Horizontal position on the map (in map units)
- **y:** Vertical height from heightmap
  - Range: [0, 25.5]
  - Values outside this range may cause visual glitches

### rotation

Rotation in radians. Full rotation = 2π ≈ 6.28.

Common values:

- 0: North (0°)
- 1.57: East (90°)  
- 3.14: South (180°)
- 4.71: West (270°)

### sea_province

For naval and coastal buildings, specifies which sea province the building connects to. Leave blank for land-only buildings.

> [!CRITICAL] The `buildings.txt` file must NOT be empty or the game crashes on load. If you have no positioned buildings, create a dummy entry or comment line to ensure the file isn't completely empty.

## Special Building Types

### Railways and Supply Nodes

```hoi4
railways = yes
supply_node = yes
```

> [!CRITICAL] Railways and supply nodes CANNOT use `add_building_construction` effects - attempting this causes crashes. Use the `build_railway` effect instead.

Railways and supply nodes require special handling through dedicated railway effects and supply system mechanics.

### Port Buildings

```hoi4
is_port = yes
```

Boolean flag indicating this is a port building. Ports have special naval mechanics and convoy interactions.

### Infrastructure

```hoi4
infrastructure = yes
```

Boolean flag for infrastructure buildings. Infrastructure affects construction speed, supply throughput, and movement speed.

### Production Buildings

```hoi4
military_production = 1.0
general_production = 1.0
naval_production = 1.0
```

Float values [0, 1] indicating what fraction of factory production this building provides. Standard factories use `1.0`.

### Specialized Buildings

```hoi4
air_base = yes
refinery = yes
fuel_silo = yes
radar = yes
nuclear_reactor = yes
```

Boolean flags for specialized building types. Each has unique game mechanics associated with it.

## Icon System

```hoi4
icon_frame = 3
```

The `icon_frame` attribute references a frame in the `GFX_buildings_strip` sprite.

The `GFX_buildings_strip` is a horizontal spritesheet divided by `noOfFrames`. Frame indexing typically starts at 1:

```text
Frame 1: Civilian factory
Frame 2: Military factory
Frame 3: Naval dockyard
...etc
```

The `noOfFrames` attribute must match the number of building types requiring icons.

## Localisation

Localisation keys for buildings:

- `<building>`: Building name
- `<building>_desc`: Building description

### Auto-Generated Modifiers

The game automatically creates modifier localisation for:

- `production_speed_<building>_factor`: State production speed
- `state_production_speed_<building>_factor`: State-specific production speed

These modifiers are auto-generated and don't need manual definition - just define the localisation keys.

## Common Issues

### Building Not Appearing on Map

If positioned buildings don't appear:

1. **Check buildings.txt:** Verify the file isn't empty and entries are formatted correctly
2. **Verify coordinates:** Y values must be [0, 25.5]
3. **Check show_on_map:** Value must be >0
4. **Verify models exist:** Entity names must match the building ID

### Construction Crashes

Railway and supply node construction via `add_building_construction` causes crashes. Use `build_railway` effect instead.

### Slot Limits Exceeded

If buildings can't be constructed despite available IC:

1. **Check MAX_SHARED_SLOTS:** Total shared buildings hitting the limit
2. **Check state_max:** Individual building type at cap
3. **Check exclusive_with:** Another building blocking this one

## Related Systems

For supply system integration, see the supply documentation.

For construction speed modifiers, see [Technologies Core](/database/technologies_core.md).

For state slot management, see the states documentation.
