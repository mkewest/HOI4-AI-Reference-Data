---
domain: map
concept: heightmap
version: 1.14+
requires: [provinces, coordinates]
relates: [terrain]
---

# Height and Visual Mapping

HOI4's map uses three interconnected visual layers: heightmap for terrain elevation, normal map for surface detail, and colormap for world coloring and city lights. These layers share the same coordinate system and must be kept synchronized.

## Heightmap

The `map/heightmap.bmp` file defines terrain elevation as an 8-bit grayscale or indexed grayscale bitmap. Each pixel's brightness value maps directly to world Y coordinate height.

### Height Scale

The heightmap uses a linear scale where:

- Black (0) = Y:0.0
- White (255) = Y:25.5
- Water level = Y:9.5 (value 95/255)

Precision is 1 Y coordinate per 10 heightmap values. This means Y:1.0 = heightmap value 10, Y:2.0 = value 20, and so on.

Water level is exactly 9.5 on the Y axis, corresponding to heightmap value 95 out of 255. This value is also defined in `gfx/FX/constants.fxh` as `WATER_HEIGHT = 9.5`.

### Format Requirements

The heightmap must be 8-bit format - either grayscale or indexed with a grayscale color table. Photoshop's grayscale mode internally saves as indexed with a grayscale color table, which the game accepts.

When exporting from GIMP, check "do not write color space information" to avoid BITMAPV5HEADER format, which causes compatibility issues. The file must use BITMAPINFOHEADER.

## Normal Map

The `map/world_normal.bmp` file defines surface normals for lighting calculations. It's a 24-bit RGB bitmap where each channel represents a vector component.

### Channel Mapping

**Red channel:** X vector component

- 0 = -1 (west)
- 128 = 0 (perpendicular)
- 255 = 1 (east)

**Green channel:** Y vector component  

- 0 = -1 (south)
- 128 = 0 (perpendicular)
- 255 = 1 (north)

**Blue channel:** Z vector component

- 128 = perpendicular to surface (not 0)
- 255 = toward viewer
- Range is 0 to -1 (not -1 to 1 like X/Y)

The Z vector uses an inverted range compared to standard normal map conventions. A value of 128 represents a surface perpendicular to the viewer, while 255 represents a surface angled toward the viewer.

## Colormap

The colormap system provides world coloring and city lighting through two DDS files.

### World Colormap

The `map/terrain/colormap_rgb_cityemissivemask_a.dds` file is an 8.8.8.8 ARGB 32-bit texture without mipmaps. Dimensions are half the provinces.bmp dimensions in each axis.

**RGB channels:** World coloring applied over terrain textures
**Alpha channel:** City light opacity (separate from RGB)

Paint.net cannot edit this file format as it lacks separate RGB/Alpha channel editing. Use Photoshop or GIMP for editing.

### Water Colormap

The `map/terrain/colormap_water_0.dds` file uses the same format (8.8.8.8 ARGB 32-bit, no mipmaps) and dimensions (half provinces.bmp size). It controls water coloring and appearance.

### Synchronization Requirements

Adjusting terrain.bmp or heightmap.bmp without updating the colormap creates visual errors where colors don't match the underlying terrain type or elevation. The colormap must be manually updated to reflect terrain changes - there is no automatic synchronization.

## Related Defines

- `WATER_HEIGHT`: Defined in `gfx/FX/constants.fxh` as 9.5
