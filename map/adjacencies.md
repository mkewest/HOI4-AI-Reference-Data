---
domain: map
concept: adjacencies
version: 1.14+
requires: [provinces]
relates: [strategic_regions]
---

# Province Adjacencies

Adjacencies define conditional or non-standard connections between provinces. They enable features like straits, canals, and restricted naval passages that depend on diplomatic relations or technology.

## Adjacencies File

The `map/adjacencies.csv` file defines special connections between provinces. Format:

```csv
StartProvID;EndProvID;Type;ThroughProvID;StartX;StartY;EndX;EndY;Rule;Comment
```

### File Terminator

> [!CRITICAL] The last line must be exactly `-1;-1;-1;-1;-1;-1;-1;-1;-1` or the file doesn't terminate correctly, causing parsing errors.

### Adjacency Fields

**StartProvID, EndProvID:** The two provinces being connected. Both must exist in definition.csv.

**Type:** Either `sea` (conditional border) or `impassable` (fully blocks connection).

**ThroughProvID:** Required if the two provinces don't directly border each other. This province acts as the path between them.

> [!CRITICAL] Enemy control of the Through province blocks adjacency use. If the specified province is controlled by a hostile nation, units cannot use the adjacency.

**StartX, StartY, EndX, EndY:** Coordinate positions for adjacency endpoints. Use X and Z coordinates (not Y, which is height). Set to `-1` for automatic calculation.

**Rule:** References an adjacency rule name defined in `map/adjacency_rules.txt`. Leave empty if no rule applies.

**Comment:** Optional text for documentation purposes. Ignored by the game.

### Adjacency Types

**sea:** Creates a conditional border that can use adjacency rules. Both provinces must be the same type (both land or both sea).

> [!CRITICAL] Sea adjacencies must be between provinces of the same type. Mixing land and sea types causes the adjacency to fail silently.

**impassable:** Fully blocks connection between provinces regardless of other conditions. Used for permanent barriers like mountain ranges or island isolation.

### Land-to-Land Sea Adjacencies

For land provinces connected by sea adjacencies, the provinces must NOT directly border each other in provinces.bmp. If they share a land border, the sea adjacency is ignored and the land border takes precedence.

The Through province is mandatory when provinces don't directly border - it defines the path units take when using the adjacency.

## Adjacency Rules

The `map/adjacency_rules.txt` file defines conditional logic for when adjacencies are usable. File encoding must be UTF-8 without BOM.

### Rule Structure

```hoi4
my_strait = {
    contested = {
        army = no
        navy = yes
        submarine = yes
        trade = no
    }
    
    enemy = {
        army = no
        navy = no
        submarine = yes
        trade = no
    }
    
    friend = {
        army = yes
        navy = yes
        submarine = yes
        trade = yes
    }
    
    neutral = {
        army = no
        navy = yes
        submarine = yes
        trade = yes
    }
    
    required_provinces = { 123 456 }
    
    is_disabled = {
        # trigger block
        has_tech = canal_technology
    }
    
    icon = 789
    offset = { 10.0 15.0 5.0 }
}
```

### Relation States

Each rule defines permissions for four diplomatic relations:

**contested:** When the adjacency is actively being fought over by multiple nations.

**enemy:** When provinces on both sides are controlled by hostile nations.

**friend:** When provinces are controlled by allied nations.

**neutral:** When diplomatic relations don't fall into other categories.

### Permission Types

For each relation state, you specify which unit types can use the adjacency:

**army:** Land units can cross.

**navy:** Naval units can cross.

**submarine:** Submarines specifically can cross (overrides navy if different).

**trade:** Trade convoys can use the route.

### Rule Attributes

**required_provinces:** Array of province IDs that must be controlled to use the adjacency. Typically both endpoint provinces, but can include additional control requirements.

**is_disabled:** Trigger block that disables the adjacency when conditions are met. For example, canals that require technology to open.

**icon:** Sea province ID where the adjacency icon appears on the map.

**offset:** Position adjustment for the icon in {X Z Y} format.

## Related Systems

Adjacency rules interact with strategic region control and diplomatic relations. When provinces in different strategic regions are connected by adjacencies, the region boundary affects how control is calculated for determining which relation state applies.

## Related Defines

Adjacency-related defines are in the naval and military categories of the defines files.
