---
domain: map
concept: terrain
version: 1.14+
requires: [provinces]
relates: [heightmap, entities]
---

# Terrain System

HOI4 uses two parallel terrain systems: provincial terrain for combat modifiers and graphical terrain for visual appearance. These systems operate independently but can be linked through the nudger's auto-generation feature.

## Provincial Terrain

Provincial terrain is defined in `common/terrain/*.txt` using the `categories` block. Each terrain type provides combat modifiers, AI evaluation factors, and movement costs.

### Configuration Structure

```hoi4
categories = {
    plains = {
        color = { 255 200 150 }
        movement_cost = 1.0
        combat_width = 90
        combat_support_width = 30
        ai_terrain_importance_factor = 1.0
        match_value = 5
        
        units = {
            attack = -0.05
        }
    }
}
```

### Terrain Attributes

**color:** RGB values for simplified map mode visualization. Has no gameplay effect beyond UI display.

**movement_cost:** Float multiplier for unit movement speed. Higher values slow movement (e.g., 2.0 = half speed).

**combat_width:** Integer defining maximum division width in battles. Only applies to land terrain.

**combat_support_width:** Integer for support company width calculation in combat.

**supply_flow_penalty_factor:** Float affecting supply throughput in provinces with this terrain.

**match_value:** Integer used for terrain border calculations. Must be unique per terrain type.

> [!CRITICAL] The `match_value` attribute must be unique per terrain type. Duplicate values cause the game to randomly assign terrain during province border calculations, creating visual artifacts.

**ai_terrain_importance_factor:** Float affecting AI evaluation of terrain for strategic decisions.

**units:** Sub-block for unit-scoped modifiers. These apply only when units are located in provinces with this terrain type.

### Terrain Assignment

Provincial terrain assignment differs by province type:

**Land provinces:** Assigned in `map/definition.csv`'s terrain column. Each province has exactly one terrain type.

**Sea provinces:** Assigned per strategic region using the `naval_terrain` attribute. All sea provinces in a region share the same naval terrain.

## Graphical Terrain

Graphical terrain controls visual appearance only and has no gameplay effect. It's defined in `common/terrain/*.txt` using the `terrain` block, separate from provincial terrain definitions.

### Configuration Structure

```hoi4
terrain = {
    desert = {
        type = desert
        color = { 4 5 6 }
        texture = 2
        spawn_city = no
        perm_snow = no
    }
}
```

### Graphical Attributes

**type:** Links to a provincial terrain type for nudger auto-generation. When the nudger's database menu setting is enabled, it uses this attribute to automatically assign provincial terrain based on graphical terrain.

**color:** Array of colormap indices that map to this terrain type. Multiple indices allow variation without creating new terrain definitions. For example, `color = { 4 5 6 }` means colormap indices 4, 5, and 6 all render as this terrain.

**texture:** Integer specifying which tile from the atlas to use (0-indexed). For a 4×4 atlas, valid values are 0-15.

**spawn_city:** Boolean controlling whether city models automatically spawn in provinces with this graphical terrain type. Terrain type 13 (urban) in the base game has this enabled.

**perm_snow:** Boolean for permanent snow coverage, independent of weather system snow.

### Texture Assignment

Graphical terrain is assigned via `map/terrain.bmp`, an 8-bit indexed bitmap where each pixel's colormap index determines which terrain texture renders. The game reads the index value, not the RGB color - changing RGB values at the same colormap index has no effect on terrain rendering.

When editing terrain.bmp in indexed mode, the colormap must be preserved. Paint.net and MS Paint cannot reliably edit indexed BMPs as they regenerate the colormap on save. Photoshop can preserve colormaps by saving/loading .ACT color table files. GIMP preserves colormaps when using "use custom palette" with the base game file open.

If the colormap is broken, the fix is to copy pixels from an RGB version into the base game's indexed file, preserving the original colormap structure. Converting from indexed to RGB and back to indexed breaks colormap order in memory.

## Texture Atlas System

Textures are stored in `map/terrain/atlas0.dds` as a 4×4 grid of 512×512px tiles. Tiles are indexed left-to-right, top-to-bottom starting from 0:

```text
 0  1  2  3
 4  5  6  7
 8  9 10 11
12 13 14 15
```

The game also uses half-resolution (`atlas1.dds`) and quarter-resolution (`atlas2.dds`) variants, switching based on zoom level and graphics settings. All atlas files must use DXT5 compression with mipmaps.

A corresponding normal map atlas exists at `map/terrain/atlas_normal0.dds` (and atlas_normal1/2 variants) using the same tile indexing system.

## Trees

Trees are defined using `map/trees.bmp`, an 8-bit indexed bitmap. Tree density and type are determined by colormap index values. Default dimensions are (75/256) × provinces.bmp dimensions, but this can be configured.

### Tree Colormap Indices

| Index | Type | Density |
|-------|------|---------|
| 2 | Palm | Sparse |
| 3 | Palm | Dense |
| 5 | Forest | Sparse |
| 6 | Forest | Dense |
| 11 | Jungle | Impassable |
| 28 | Jungle | Sparse |
| 29 | Jungle | Dense |

Tree models are referenced as pdxmesh with naming convention `mapobject_{id}`, where id corresponds to the colormap index. These models are defined in `gfx/entities/*.asset` files.

## Terrain Interaction

The nudger can auto-generate provincial terrain from graphical terrain using the `type` attribute in graphical terrain definitions. This links graphical terrain back to a provincial terrain type for automated assignment during state creation.

When provincial and graphical terrain assignments conflict, both systems operate independently - provincial terrain affects combat while graphical terrain affects visuals only. There is no automatic synchronization between the two systems. Updating terrain.bmp changes graphical appearance but does not modify combat modifiers assigned in definition.csv.

## Related Defines

- `MINIMUM_PROVINCE_SIZE_IN_PIXELS`: See [NGraphics](/defines_list/NGraphics.md)
