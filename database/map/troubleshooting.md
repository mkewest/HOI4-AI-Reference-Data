---
domain: map
concept: troubleshooting
version: 1.14+
relates: [provinces, terrain, heightmap, rivers]
---

# Map Troubleshooting

Map modding errors often manifest as crashes, visual glitches, or cryptic error messages. This guide covers common issues, diagnostic tools, and fixes.

## Debug Mode

> [!CRITICAL] Debug mode is essential for map modding. Without it, many errors only appear after country selection, wasting significant testing time.

Enable debug mode by launching the game with the `-debug` flag or adding it to the launch options. Debug mode provides:

- MAP_ERROR visibility before country selection
- Access to the nudger tool
- Detailed error logging
- Console command access

Without debug mode, the game may fail to load with no visible error information. Some MAP_ERROR entries don't appear until after selecting a country in singleplayer, making debugging nearly impossible.

## BMP File Handling

BMP format requirements are strict and many image editors don't handle indexed BMPs correctly.

### Compatible Editors

**GIMP:** Reliable for all BMP types

- Export settings: Check "do not write color space information"
- Indexed BMP editing: Use "use custom palette" with base game file open
- This preserves the colormap structure

**Photoshop:** Can handle indexed BMPs with proper workflow

- Save/load .ACT color table files to preserve colormaps
- Greyscale mode internally saves as indexed with greyscale color table (acceptable)

**Incompatible editors:**

- Paint.net: Cannot edit indexed BMPs (regenerates colormap on save)
- MS Paint: Cannot edit indexed BMPs (regenerates colormap on save)

### Fixing Broken Indexed BMPs

If an indexed BMP's colormap is broken (wrong colors after editing):

1. Convert the broken indexed BMP to RGB mode
2. Open the base game's corresponding indexed BMP
3. Copy pixels from your RGB version into the base game indexed file
4. This preserves the original colormap while updating pixel index values

The game reads colormap index values, not RGB values. Changing RGB values at the same colormap index has no effect. Converting indexed→RGB→indexed breaks colormap order in memory.

### Detecting Wrong Bitdepth

Wrong bitdepth is typically indicated by large filesize differences compared to base game files:

- 24-bit RGB should be roughly 3× map dimensions in pixels
- 8-bit indexed should be roughly 1× map dimensions in pixels
- 32-bit RGBA is 4× and indicates an error (alpha channel present)

Alpha channels appear from accidentally creating layers in image editors. Always flatten to a single layer before exporting provinces.bmp.

### Header Format Issues

The BMP header must be BITMAPINFOHEADER, not BITMAPV5HEADER. GIMP's "do not write color space information" export option ensures the correct header type.

## Common Errors

### X4008 Float Division Error

**Symptom:** Game crashes immediately on launch with X4008 error.

**Causes:**

- provinces.bmp is 32-bit RGBA instead of 24-bit RGB (alpha channel present)
- provinces.bmp exceeds 13,238,272 pixel maximum area
- Wrong BITMAPINFOHEADER type (use GIMP export option)

**Fix:**

1. Open provinces.bmp in GIMP
2. Image → Mode → RGB (not RGBA) - flatten any layers first
3. Resize if area exceeds limit
4. Export with "do not write color space information" checked
5. Verify filesize matches expected dimensions × 3 bytes per pixel

### MAP_ERROR: X Crossing

**Symptom:** Error reports four provinces sharing a common corner at specific coordinates.

**Cause:** Province borders create a four-way intersection point. The coordinates reported use left-to-right then down-to-up ordering (not standard Z-axis convention).

**Detection:** Can occur at horizontal map edge where looping creates wraparound corners.

**Fix:** Adjust province borders so no more than three provinces meet at any point. Add small buffer pixels to break up four-way corners.

### Province Has Only N Pixels

**Symptom:** MAP_ERROR reports province ID below minimum size (default 2 pixels).

**Causes:**

- Anti-aliasing created single-pixel provinces during editing
- Color picker grabbed wrong RGB value, creating unintended province
- Image manipulation left isolated pixels

**Detection:** Use color select tool with 0% tolerance to find all instances of the province color. Global flood mode (GIMP) or magic wand (Paint.net) can highlight all pixels.

**Fix:**

1. Find the tiny province using color selection
2. Flood fill with adjacent province color, or
3. Manually paint over the artifact pixels

### No Continent Error

**Symptom:** Every land province shows "no continent" error despite definition.csv having continent values.

**Cause:** Line endings are LF (Unix format) instead of CRLF (Windows format). The parser fails to read the continent column.

**Fix:** Convert definition.csv to CRLF line endings. On Linux/Mac: `unix2dos definition.csv`

The game creates `definition.csv.fixed` in the user directory when auto-fixing. This file loads even after fixing the original - delete it manually after corrections.

### TOO_LARGE_BOX Error

**Symptom:** MAP_ERROR reports province exceeding size limits.

**Causes:**

- Single province exceeds 1/8 of total map size
- Duplicate RGB colors for different province IDs creating very disjointed sections

**Fix:**

- Split large provinces into multiple smaller provinces
- Check for duplicate colors in definition.csv
- Verify no accidental color collisions in provinces.bmp

### Bitmap Coastal Disagree

**Symptom:** Borders don't render correctly between certain provinces.

**Causes:**

- definition.csv Type column doesn't match bitmap's water detection
- Earlier province IDs are missing, causing property offset bug

**Fix:**

- Verify Type column matches actual province rendering (land/sea/lake)
- Check for sequential province IDs with no gaps
- Remember: bitmap coastal status always wins over definition.csv

### No Pixels Error

**Symptom:** Province ID exists in definition.csv but game reports no pixels found.

**Causes:**

- RGB color in definition.csv doesn't exist in provinces.bmp
- Duplicate RGB colors assigned to multiple province IDs

**Fix:**

- Verify exact RGB match between definition.csv and provinces.bmp
- Check for duplicate color definitions
- Use color picker to confirm bitmap colors match definition

## Nudger Tool

The nudger is accessed through debug mode and provides tools for editing map data in-engine.

### Capabilities

- Edit existing ambient objects (position, rotation, scale)
- Assign strategic regions to newly-created states
- Auto-generate provincial terrain from graphical terrain (database menu setting)

### Limitations

> [!CRITICAL] The nudger cannot create new ambient objects - it can only edit existing ones defined in ambient_object.txt.
>
> [!CRITICAL] The nudger removes ALL quotes from state history files. This breaks DLC checks like `has_dlc = "Waking the Tiger"`. You must manually restore quotes after using the nudger.
>
> [!CRITICAL] The nudger crashes if state names contain multi-byte UTF-8 characters (non-English alphabet characters like Chinese, Cyrillic, or accented letters).

### Output Location

The nudger outputs to the user directory: `Documents/Paradox Interactive/Hearts of Iron IV/`

Files are organized in subdirectories:

- `history/states/` - State files
- `map/` - Map configuration files  
- `localisation/` - Localization files

These files have lower loading priority than mod files. If your mod uses `replace_path` or has its own copies of these files, nudger changes may appear invisible. Check the user directory to verify nudger output.

### Newly-Created States

States created through the nudger have no strategic region assignments initially. You must use the nudger to assign them to strategic regions, or manually edit the state files and strategic region files.

## File Encoding Issues

### CSV Line Endings

CSV files (definition.csv, adjacencies.csv) require CRLF line endings. LF line endings cause parsing failures where the game can't read later columns in the row.

### UTF-8 BOM

The `map/adjacency_rules.txt` file must be UTF-8 without BOM. Including the BOM causes parsing errors.

### DDS Files

When exporting DDS files from GIMP, check "do not write color space information" to avoid compatibility issues. The game expects specific DDS formats:

- Atlas files: DXT5 compression with mipmaps
- Colormap files: 8.8.8.8 ARGB 32-bit without mipmaps

## Replace Path Behavior

The `replace_path` directive only affects a single folder, not subfolders. It's commonly used to unload base game strategic regions or states when doing total conversion mods.

Replace path is indexed at main menu loading. Changes to replace_path require restarting the game to take effect.

Using replace_path on map folders can make nudger changes invisible if mod files override the user directory output. Always check both locations when debugging.

## Colormap Index Detection

For indexed BMPs (rivers.bmp, terrain.bmp, trees.bmp), use the color select tool with 0% tolerance to find unintended index values. This reveals:

- Anti-aliasing artifacts (unexpected intermediate colors)
- Wrong color picker selection (grabbed wrong index)
- Compression artifacts if file was saved as JPEG then converted

Global flood mode highlights all pixels with the same index, making it easy to spot isolated mistakes.

## Palette Error (Rivers)

The error "Palette in rivers.bmp probably not correct" is a GIMP-specific issue and safe to ignore. The game loads correctly despite the warning.

If the error prevents loading (rare), fix by hex editing addresses 0x2F and 0x33, changing values from 01 to 00. This corrects a header flag that GIMP sets incorrectly.

## Related Systems

Troubleshooting often requires understanding:

- [Provinces](/map/provinces.md) - Definition format and ID constraints
- [Terrain](/map/terrain.md) - Indexed BMP colormap preservation
- [Heightmap](/map/heightmap.md) - Format requirements and coordinate mapping
- [Coordinates](/map/coordinates.md) - Position calculation and axis definitions
