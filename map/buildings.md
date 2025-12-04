---
domain: map
concept: buildings
version: 1.14+
requires: [provinces, states, coordinates]
relates: [entities]
---

# Positioned Map Objects

HOI4 defines three types of positioned objects on the map: buildings (state infrastructure), unitstacks (unit positions and victory points), and ambient objects (decorative 3D models). All use the same coordinate system and rotation conventions.

## Buildings

The `map/buildings.txt` file defines positions for all constructed buildings. Format:

```csv
StateID;BuildingID;X;Y;Z;Rotation;AdjacentSeaProvince
```

### Position Fields

**StateID:** The state ID where the building is located. Note that buildings.txt uses state IDs even for provincial buildings - the XYZ coordinates determine the actual province placement.

**BuildingID:** Integer identifying the building type. These correspond to building definitions in `common/buildings/*.txt`.

**X, Y, Z:** World coordinates for building placement. See [Coordinates](/map/coordinates.md) for axis definitions.

**Rotation:** Measured in radians (0 to approximately 6.28 for full rotation). Positive values rotate counter-clockwise, negative values rotate clockwise. Zero is the default orientation.

**AdjacentSeaProvince:** Required for naval_base and floating_harbor buildings. Specifies which sea province the building connects to. Must be a valid sea province ID that borders the province where the building is placed.

### Critical Requirements

> [!CRITICAL] A completely empty buildings.txt file causes the game to crash. The file must contain at least one building definition or be omitted entirely.

> [!CRITICAL] Missing definitions for naval_base or floating_harbor buildings cause crashes several hours into gameplay. The crash manifests as a RAM/CPU-eating infinite loop with `client_ping` or `hourly_ping` appearing in crash logs.

This bug occurs because the building definition is incorrectly used for both 3D model assignment and sea province assignment logic. The workaround is to either turn off AI (which triggers the pathfinding bug) or ensure all required building definitions exist.

## Unitstacks

The `map/unitstacks.txt` file defines positions for unit rendering and victory points. Format:

```csv
ProvinceID;Type;X;Y;Z;Rotation;Offset
```

### Position Fields

**ProvinceID:** The province where this unitstack appears.

**Type:** Integer defining the unit state or special marker type.

**X, Y, Z:** World coordinates. Note that Y is height (not Z).

**Rotation:** In radians, same convention as buildings.

**Offset:** Additional positioning adjustment.

### Unitstack Types

| Type | Description |
|------|-------------|
| 0 | Standstill |
| 1-8 | Moving (8 rotation levels) |
| 9 | Attacking |
| 10 | Defending |
| 11-18 | Disembark (8 variants) |
| 19 | Ship in port |
| 20 | Ship in port moving |
| 21-29 | RG variants |
| 30-37 | Disembark RG (8 variants) |
| 38 | Victory point |

### Victory Points

Victory points use type 38 in unitstacks.txt for position only. The actual victory point value and name are defined in the state's history file (`history/states/*.txt`), not in unitstacks.txt.

This split means adding a new victory point requires editing both files: unitstacks.txt for position and the state history file for the value/name.

## Ambient Objects

The `map/ambient_object.txt` file defines decorative 3D models placed on the map. These use entity definitions from `gfx/entities/*.asset`.

### Configuration Structure

```hoi4
ambient_object = {
    type = "tree_oak_large"
    use_animation = yes
    time_duration = 0
    scale = 1.0
    always_visible = no
    
    object = {
        name = "oak_01"
        position = { 1234.5 10.0 5678.9 }
        rotation = { 0.0 1.57 0.0 }
    }
    
    object = {
        name = "oak_02"
        position = { 1240.0 10.2 5680.0 }
        rotation = { 0.0 0.0 0.0 }
    }
}
```

### Ambient Object Attributes

**type:** Entity name defined in `gfx/entities/*.asset`.

**use_animation:** Boolean controlling whether the entity's animation plays.

**time_duration:** Integer for animation timing (if animated).

**scale:** Float multiplier for object size. Default is 1.0.

**always_visible:** Boolean controlling whether the object renders at all zoom levels.

**object:** Array defining individual instances. Each has a name (identifier), position (X Y Z), and rotation (X Y Z) in radians.

### Nudger Limitations

The nudger tool can edit existing ambient objects but cannot create new ones. To add new ambient objects, you must manually edit ambient_object.txt.

## Rotation Conventions

All rotation values across buildings, unitstacks, and ambient objects use radians:
- 0 = default orientation
- Positive values = counter-clockwise rotation
- Negative values = clockwise rotation  
- Full rotation = π×2 ≈ 6.28

To convert degrees to radians: radians = degrees × (π/180)

## Related Defines

Building-specific defines are documented in their respective building definition files in `common/buildings/*.txt`.
