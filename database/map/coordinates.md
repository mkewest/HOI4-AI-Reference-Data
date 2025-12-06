---
domain: map
concept: coordinates
version: 1.14+
relates: [provinces, heightmap, buildings, strategic_regions]
---

# Coordinate System

HOI4 uses a three-dimensional coordinate system for positioning objects on the map. Understanding the coordinate system is essential for placing buildings, units, ambient objects, and editing heightmaps.

## Axis Definitions

**X axis:** Horizontal axis running left-to-right

- Origin: Left edge of the map
- Direction: Increases from west to east
- Looping: The map loops horizontally, so X coordinates wrap around

**Y axis:** Vertical axis representing height

- Scale: 0 = sea level (black on heightmap), 25.5 = maximum height (white on heightmap)
- Water level: Exactly 9.5
- Precision: 1 Y coordinate = 10 in decimal heightmap value

**Z axis:** Depth axis running south-to-north

- Origin: South edge of the map
- Direction: Increases from south to north
- Note: This is opposite most 3D editors where Z typically represents height

### Coordinate System Differences

The Z-as-north convention differs from standard 3D modeling software (Blender, Maya, 3ds Max) where Z typically represents the vertical axis. When importing/exporting models or positions, axis mappings may need adjustment.

## Position Formats

Different files use coordinates in different orders:

**Buildings and unitstacks:** X, Y, Z format

```csv
StateID;BuildingID;X;Y;Z;Rotation;AdjacentSeaProvince
```

**Adjacency positions:** X, Y (actually X and Z - Y is omitted as it's calculated from terrain)

```csv
StartProvID;EndProvID;Type;ThroughProvID;StartX;StartY;EndX;EndY;Rule;Comment
```

**Ambient objects and weather positions:** Use standard X, Y, Z in object blocks

```hoi4
position = { 1234.5 10.0 5678.9 }
```

**Adjacency rule offsets:** X, Z, Y format (different from standard)

```hoi4
offset = { 10.0 15.0 5.0 }  # X, Z, Y
```

## Rotation Conventions

All rotation values use radians (not degrees):

- Full rotation = π × 2 ≈ 6.28 radians
- 0 = default orientation
- Positive values = counter-clockwise rotation
- Negative values = clockwise rotation

### Degree to Radian Conversion

To convert degrees to radians:

```text
radians = degrees × (π / 180)
```

Common conversions:

- 90° = 1.57 radians (π/2)
- 180° = 3.14 radians (π)
- 270° = 4.71 radians (3π/2)
- 360° = 6.28 radians (2π)

Rotation applies in files like buildings.txt, unitstacks.txt, and ambient_object.txt.

## X Crossing Error

The X crossing error occurs when four provinces share a common corner point. This creates an ambiguous situation where the game cannot determine valid borders.

The error is reported in map coordinates using left-to-right, then down-to-up ordering (not the game's standard Z-axis convention). When debugging X crossing errors, convert the reported coordinates to understand which provinces are involved.

X crossing can also occur at the horizontal map edge where the map loops. Provinces at X=0 and X=max can share corners with provinces at the opposite edge, creating wraparound X crossing errors.

## Automatic Position Calculation

Many files allow `-1` as a coordinate value to trigger automatic calculation:

- Adjacencies: Set StartX, StartY, EndX, EndY to `-1` for auto-calculated positions
- The game determines optimal positions based on province centers and borders

## Related Systems

The coordinate system interacts with:

- **Heightmap:** Y values correspond directly to heightmap brightness (0-255 → 0-25.5)
- **Provinces:** Province centers are used for pathfinding and positioning calculations
- **Buildings:** All buildings use world coordinates within their assigned state
- **Strategic regions:** Weather positions use world coordinates within regions

## Related Defines

- `WATER_HEIGHT`: Defined in `gfx/FX/constants.fxh` as 9.5
