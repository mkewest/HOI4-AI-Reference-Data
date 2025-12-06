---
domain: map
concept: rivers
version: 1.14+
requires: [provinces]
relates: [railways, supply]
---

# River System

Rivers are defined using `map/rivers.bmp`, an 8-bit indexed bitmap where colormap indices control river properties, flow direction, and rendering width. Rivers affect both visual appearance and gameplay mechanics through pathfinding costs.

## River Requirements

Rivers must be exactly 1 pixel thick and use only orthogonal lines (no diagonal pixels). The game detects river crossings when the path between province centers overlaps one or more river pixels.

## Colormap Indices

| Index | Color | Role | Width |
|-------|-------|------|-------|
| 0 | Green | Source | N/A |
| 1 | Red | Flow-in | N/A |
| 2 | Yellow | Flow-out | N/A |
| 3-6 | Cyan shades | Small rivers | Uses small width |
| 7-11 | Blue shades | Large rivers | Uses large width |

### Source Requirements

> [!CRITICAL] Each contiguous river requires exactly one green source pixel (index 0). Multiple green sources in the same river system cause undefined behavior.

Red flow-in pixels (index 1) allow tributaries to join paths without needing their own green source. Only the main branch requires a green source pixel - connected branches can use red flow-in pixels to merge into the main path.

### Flow Direction

Yellow flow-out pixels (index 2) indicate where rivers branch outward from the main path. This is used for deltas or distributaries where a single river splits into multiple channels.

### Width Categories

Indices 3-6 (cyan shades) render as small rivers using the width defined by `RIVER_SMALL_START_INDEX` through `RIVER_SMALL_STOP_INDEX` defines.

Indices 7-11 (blue shades) render as large rivers using the width defined up to `RIVER_LARGE_STOP_INDEX`.

The different shades within each category (4 cyan shades, 5 blue shades) allow visual variation in the same river without changing width - this can represent different flow rates or water clarity.

## Pathfinding Impact

Rivers count as level 1 railways in the pathfinding system. Very long rivers can contribute to performance degradation because they add railway path calculations across the entire river length. Consider breaking extremely long rivers into separate segments for better performance.

## Colormap Preservation

Rivers.bmp uses an 8-bit indexed format. Paint.net and MS Paint cannot edit indexed BMPs reliably as they regenerate the colormap on save. Use Photoshop (with .ACT color table preservation) or GIMP (with "use custom palette" option) to maintain the colormap.

If a palette error occurs, you may see: "Palette in rivers.bmp probably not correct" in the error log. This is a GIMP-specific issue and safe to ignore - the game will still load correctly. The error can be fixed by hex editing addresses 0x2F and 0x33, changing values from 01 to 00, though this is unnecessary unless the error prevents loading.

## Related Defines

- `RIVER_RAILWAY_LEVEL`: See [NSupply](/defines_list/NSupply.md) - Default value 1
- `RIVER_SMALL_START_INDEX`: See [NMilitary](/defines_list/NMilitary.md) - Default value 0
- `RIVER_SMALL_STOP_INDEX`: See [NMilitary](/defines_list/NMilitary.md) - Default value 6
- `RIVER_LARGE_STOP_INDEX`: See [NMilitary](/defines_list/NMilitary.md) - Default value 11
