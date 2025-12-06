---
domain: assets
concept: fonts
version: 1.14+
requires: [localisation]
relates: [sprites, interface]
---

# Font System

Fonts in HOI4 use bitmap font format with separate `.fnt` definition files and `.dds` texture files. The system supports multiple language-specific bitmap overrides and custom color definitions per font.

## Font File Structure

### Bitmapfont Definition

Fonts are defined in `interface/*.gfx` files using the `bitmapfont` block:

```hoi4
bitmapfont = {
    name = "Main_14"
    path = "gfx/fonts/main_14"
    color = 0xFFFFFFFF
    fontfiles = {
        "gfx/fonts/main_14.fnt"
    }
}
```

Font attributes:

- `name`: Font identifier used in interface and localization
- `path`: Base path for font bitmaps (without extension)
- `color`: Default text color in ARGB format (0xAARRGGBB)
- `fontfiles`: Array of `.fnt` definition files

> [!CRITICAL] The `color` attribute uses ARGB format where the first two hex digits are alpha channel, not red. Full opacity white is `0xFFFFFFFF`, not `0x00FFFFFF`. The `0x` prefix is required.

### File Matching Priority

The game uses filename matching before internally-defined bitmap paths. When loading fonts, the system first checks for files matching the `path` attribute, then falls back to paths defined inside the `.fnt` file. This means the bitmapfont definition `name` does not need to match font filenames - the `path` attribute controls file lookup.

## Font Bitmaps

### Bitmap Size Limits

Each individual font graphic has a hard limit of 16 MB. Paradox Chinese fonts demonstrate the practical maximum: they use exactly 16,001 KB as the maximum size with 11 linked bitmaps totaling approximately 176 MB across all languages.

> [!CRITICAL] Compression=None on large exports may prevent HOI4 from processing the bitmap entirely. Always use DXT compression for font textures to stay within memory constraints.

### Character Spacing Requirements

> [!CRITICAL] Missing blank box characters from Latin/Latin-1 Supplement (Unicode blocks) causes words to render without spaces. If characters 1-3 (blank boxes) are not selected during font export, there is no spacing workaround - words concatenate with zero separation. This effect is absolute and cannot be fixed without re-exporting with proper blank characters.

The spacing system relies on these invisible characters being present in the font bitmap. Omitting them breaks all word separation.

## Multiple Bitmaps

### Splitting Fonts Across Files

Large character sets can be split across multiple bitmap files:

```hoi4
bitmapfont = {
    name = "Large_Font"
    fontfiles = {
        "gfx/fonts/large_font_latin.fnt"
        "gfx/fonts/large_font_cyrillic.fnt"
        "gfx/fonts/large_font_cjk.fnt"
    }
}
```

> [!CRITICAL] BMFont multi-page exports cannot be used directly. The tool does not automatically split character definitions - you must manually define each bitmap separately in the fontfiles array. Multiple bitmaps in one font must have zero overlapping characters defined or the game will fail to render characters correctly.

The override system enables organizational flexibility. Split fonts by alphabet, quality tier, or language-specific character sets. Each `.fnt` file references its own bitmap texture.

## Kerning

Kerning data defines spacing between specific character pairs. Some fonts export without `kerning first=` lines in the `.fnt` file, causing character overlaps in-game. This is not a crash but produces visual corruption where characters render too close together or overlap.

If BMFont doesn't generate kerning data automatically, manual addition is required. The `.fnt` format uses:

```text
kerning first=<char1_id> second=<char2_id> amount=<pixels>
```

Missing kerning won't prevent the font from loading but degrades readability significantly.

## Language Overrides

### bitmapfont_override

Language-specific font variants use `bitmapfont_override` blocks:

```hoi4
bitmapfont_override = {
    name = "Main_14"
    languages = { "l_simp_chinese" "l_japanese" }
    fontfiles = {
        "gfx/fonts/main_14_cjk.fnt"
    }
}
```

Override activation occurs only when game language matches entries in the `languages` array. Language codes must match folder names in `localisation/` directory: `l_english`, `l_french`, `l_german`, `l_spanish`, `l_braz_por`, `l_polish`, `l_russian`, `l_japanese`, `l_simp_chinese`.

The override replaces the entire font definition for matching languages. The original font remains unchanged for other locales. This enables optimized bitmaps per language - Latin fonts can be smaller while CJK fonts include thousands of characters.

## Map Font

> [!CRITICAL] The map font is hardcoded to always use bitmapfont name `tahoma_60`. This name cannot be changed. The game automatically loads this font for map text rendering.

Default map font links to `gfx/fonts/hoi_mapfont4` with Chinese and Japanese variants. Mods can override map font appearance by defining a new `tahoma_60` bitmapfont, but the name must remain `tahoma_60`.

## Color Definitions

### Custom Text Colors

Fonts can define custom colors for localization `§` codes through the `textcolors` block:

```hoi4
bitmapfont = {
    name = "Custom_Font"
    path = "gfx/fonts/custom"
    textcolors = {
        { 255 0 0 }    # §R - Custom red
        { 0 255 0 }    # §G - Custom green
    }
}
```

The `§` symbol in localization requires matching textcolors entry. Each entry in the array corresponds to a single character code. When used in a bitmapfont definition, these colors override global textcolors only for that specific font.

The `fontfiles` array replaces the `path` attribute if specified - they are mutually exclusive. Use either `path` for single-file fonts or `fontfiles` for multi-file fonts, not both.

## Export Workflow

### BMFont Tool Quirks

> [!CRITICAL] BMFont appends `_0` suffix to generated `.dds` files. This suffix must be manually removed before the font will load. The `.dds` and `.fnt` filenames must be identical (excluding extensions) or the game cannot match definition to texture.

BMFont export workflow:

1. Export font from BMFont with chosen settings
2. Locate generated `.dds` file (typically named `fontname_0.dds`)
3. Rename to remove `_0` suffix (e.g., `fontname.dds`)
4. Verify `.fnt` and `.dds` have matching names
5. Place both files in appropriate `gfx/fonts/` directory
6. Create or update bitmapfont definition in interface file

Filename mismatch between `.dds` and `.fnt` breaks font loading entirely. The game logs an error but provides no clear indication of the filename problem.

## Related Systems

Fonts integrate with localization for text rendering and interface elements for text display. Custom color definitions in fonts override global text colors. See [Localization](/assets/localisation.md) for color code usage and [Interface](/assets/interface.md) for text element definitions.
