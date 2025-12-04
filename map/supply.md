---
domain: map
concept: supply
version: 1.11+
requires: [provinces]
conflicts: [supply_areas_pre_1.11]
relates: [strategic_regions, railways]
---

# Supply System

The supply system defines how resources and equipment flow from capital cities to front-line units. The system was completely redesigned in patch 1.11, replacing supply areas with supply nodes and railways.

## Current System (1.11+)

The modern supply system uses two files to define supply infrastructure:

### Supply Nodes

The `map/supply_nodes.txt` file defines provinces with supply hubs. Format:

```
Level ProvinceID
```

**Level:** Currently only level 1 is supported. Higher values are ignored.

**ProvinceID:** The province where this supply node is located. Must be a valid land province defined in definition.csv.

> [!CRITICAL] Invalid supply node definitions cause crashes when opening singleplayer games or accessing the Supply section in the nudger. Invalid definitions include non-existent provinces, provinces without state assignment, or very disjointed railway connections.

### Railways

The `map/railways.txt` file defines railway connections between provinces. Format:

```
Level ProvinceCount ProvinceID1 ProvinceID2 ProvinceID3 ...
```

**Level:** Railway level from 1 to 5. Higher levels provide better supply throughput. The maximum level is defined by `MAX_RAILWAY_LEVEL` in defines.

**ProvinceCount:** Number of provinces in this railway segment.

**ProvinceIDs:** Sequential list of connected provinces forming the railway path.

Example:
```
3 4 123 124 125 126
```
This creates a level 3 railway connecting provinces 123→124→125→126.

> [!CRITICAL] Invalid railway definitions cause crashes when opening singleplayer games or accessing the Supply nudger. Very disjointed railways (connecting provinces across the map without continuous paths) are particularly prone to crashing.

Railways must form logical paths between provinces. Each province in the list should be adjacent to or near the next province - extremely long jumps between non-adjacent provinces create pathfinding issues.

### Rivers as Railways

Rivers automatically count as level 1 railways in the pathfinding system. This is defined by `RIVER_RAILWAY_LEVEL` in defines. Very long rivers effectively create long level 1 railway paths, which can impact pathfinding performance.

## Legacy System (≤1.10)

> [!NOTE] **Deprecated in patch 1.11**
> The supply areas system was replaced by supply nodes and railways. This information is preserved for mod compatibility and understanding pre-1.11 mods.

### Supply Areas

Pre-1.11 versions used `map/supplyareas/*.txt` files to define supply regions. Multiple supply areas could exist in a single file.

```hoi4
supply_area = {
    id = 1
    name = "Supply Area 1"
    value = 10
    states = { 1 2 3 4 }
}
```

**id:** Integer identifying the supply area.

> [!CRITICAL] Supply area IDs must be sequential starting from 1 with no gaps. Skipping any number causes crashes in pre-1.11 versions.

**name:** Display name for the supply area.

**value:** Supply capacity for this area. Base game values ranged from 0 to 16.

**states:** Array of state IDs included in this supply area.

### Design Patterns

Supply areas were designed to cover multiple contiguous states sharing a supply network. Islands typically needed separate supply areas due to disconnected supply paths.

Single-state supply areas technically worked but violated the intended design pattern where supply areas represented regional logistics networks. The modern system's supply nodes better represent this per-province granularity.

## Migration Notes

When converting pre-1.11 mods to 1.11+:
1. Remove `map/supplyareas/*.txt` files or use `replace_path` to unload them
2. Create `map/supply_nodes.txt` with supply hubs in major cities
3. Create `map/railways.txt` connecting supply nodes to provinces
4. Test thoroughly as supply flow mechanics changed significantly

The new system provides more granular control but requires more detailed railway mapping.

## Related Defines

- `MAX_RAILWAY_LEVEL`: See [NSupply](/defines_list/NSupply.md) - Default value 5
- `RIVER_RAILWAY_LEVEL`: See [NSupply](/defines_list/NSupply.md) - Default value 1
