---
domain: map
concept: provinces
version: 1.14+
requires: [coordinates]
relates: [terrain, strategic_regions, states]
---

# Province System

Provinces are the fundamental geographic units in HOI4, defined by RGB colors in provinces.bmp and detailed in definition.csv. Each unique color represents a distinct province, with attributes controlling terrain, type, and continental assignment.

## Province Bitmap

The `map/provinces.bmp` file is a 24-bit RGB bitmap where each unique color represents a province. Dimensions must be multiples of 256 pixels (both width and height), with a maximum total area of 13,238,272 pixels.

> [!CRITICAL] Exceeding the maximum area of 13,238,272 pixels causes an X4008 float division error on launch. Keep map dimensions conservative or reduce province count.

The practical limit is approximately 21,000 provinces due to the 65,536 border limit. Each disjointed section of a province counts as a separate border - for example, an island touching the mainland at three points creates three separate borders.

Very disjointed provinces with accidentally identical colors can crash the game. When possible, keep provinces contiguous to minimize border count and improve performance.

### BMP Format Requirements

The bitmap must use 24-bit RGB format without alpha channels. Accidentally including an alpha channel (for example, by creating a layer in an image editor) results in a 32-bit RGBA file, which triggers the X4008 error.

The header must be BITMAPINFOHEADER, not BITMAPV5HEADER. When exporting from GIMP, check "do not write color space information" to ensure the correct header type. Wrong bitdepth is typically indicated by large filesize differences compared to base game files.

## Province Definition Format

The `map/definition.csv` file maps RGB colors to province attributes:

```csv
ProvinceID;R;G;B;Type;Coastal;Terrain;Continent
```

> [!CRITICAL] Province IDs must be sequential starting from 1 with no gaps. Skipping any number causes all subsequent provinces to inherit properties from the next ID, creating offset bugs where provinces have wrong terrain, type, or continent values.

Line endings must be CRLF (Windows format). Using LF (Unix format) causes the parser to fail reading the continent column, resulting in "no continent" errors for every land province.

### Automatic Fixes

The game creates `definition.csv.fixed` in the user directory (`Documents/Paradox Interactive/Hearts of Iron IV/`) to auto-correct ID gaps. This file persists even after manual fixes and will continue loading instead of your corrected definition.csv - you must delete it manually after fixing the source file.

### Province Types

Three province types exist:

**land:** Normal playable provinces with terrain and buildings
**sea:** Naval provinces for ship movement  
**lake:** Impassable water provinces that block naval movement

> [!CRITICAL] Type assignment must match between definition.csv and the bitmap's coastal detection. When they disagree, the bitmap's coastal status always wins, preventing border rendering between mismatched types.

This means if the bitmap detects water but definition.csv marks it as land (or vice versa), borders won't render correctly. The bitmap's detection is authoritative.

### Coastal Attribute

The Coastal column in definition.csv is a boolean (true/false) indicating whether land provinces can build naval bases. This attribute is independent of the Type column - a land province can be coastal or inland.

## Continental Assignment

Continents are defined in `map/continent.txt` as a list:

```hoi4
continents = { europe north_america south_america australia africa asia middle_east }
```

IDs are assigned in definition order starting from 1. All land provinces must have `continent > 0` in definition.csv. Value 0 is reserved for water provinces (sea and lake types).

Base game continent IDs:

- 1 = Europe
- 2 = North America  
- 3 = South America
- 4 = Australia
- 5 = Africa
- 6 = Asia
- 7 = Middle East

### Continental Boundaries

The Ural Mountains split states between Europe (continent 1) and Asia (continent 6). The Caucasus Mountains split states between Europe and Middle East (continent 7). The Suez Canal marks the boundary where Sinai enters the Middle East.

Note that North Epirus in Albania is erroneously assigned to North America (continent 2) in the base game. Pacific islands are mostly Asian, while the Australia continent includes only the mainland and specific archipelagos.

## State Requirements

All provinces must be assigned to exactly one state (defined in `history/states/*.txt`). Unassigned provinces cause crashes. Additionally, all provinces within a single state must belong to the same strategic region.

## Common Errors

**no_pixels:** The RGB color defined in definition.csv does not exist in provinces.bmp, or duplicate RGB colors exist for different province IDs.

**province_has_only_N_pixels:** Province is below the minimum size threshold defined in `MINIMUM_PROVINCE_SIZE_IN_PIXELS`. This commonly occurs from anti-aliasing artifacts or color picker errors. Use the color select tool with 0% tolerance to detect unintended colors, then flood fill the artifact pixels.

**TOO_LARGE_BOX:** Province exceeds 1/8 of the total map size, or duplicate colors exist for different provinces creating very disjointed sections.

## Related Defines

- `MINIMUM_PROVINCE_SIZE_IN_PIXELS`: See [NGraphics](/defines_list/NGraphics.md)
- `PROVINCE_AREA_LIMIT`: See [NGraphics](/defines_list/NGraphics.md)
- `BORDER_LIMIT`: See [NGraphics](/defines_list/NGraphics.md)
