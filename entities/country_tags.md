---
domain: entities
concept: country_tags
version: 1.14+
requires: [file_structure]
relates: [country_history, flags, colors, localization]
---

# Country Tag System

Country tags are three-character identifiers that uniquely identify nations in HOI4. Tags reference country definition files that specify visual attributes like colors, graphical cultures, and flag sprites.

## Tag Definition

Tags are defined in `common/country_tags/*.txt` using the format:

```hoi4
TAG = "countries/filename.txt"
```

Each tag must be exactly 3 characters long and unique across all loaded files. Tags are case-insensitive internally but convention uses uppercase.

### Reserved Tags

The following tags are reserved and cannot be used: `NOT`, `AND`, `TAG`, `OOB`, `LOG`, `NUM`, `RED`.

### Naming Restrictions

Tag names cannot begin with numeric characters, though numbers are allowed within the tag. For example, `D01` is valid but `123` is not.

> [!CRITICAL] Insufficient dynamic tags causes the game to crash with a misleading error message that references `map/cities.txt` or savegame files rather than the actual tag system issue.

### Dynamic Tags

Dynamic tags enable civil war mechanics by creating temporary country copies. Enable dynamic tags in any country_tags file:

```hoi4
dynamic_tags = yes
```

The number of dynamic tags allocated affects certain visual systems:
- Medium flags (41×26px) require approximately 10 dynamic tags or become transparent
- Small flags (10×7px) require approximately 20 dynamic tags or become transparent

These transparency issues occur for all countries when dynamic tags are insufficient, and no error is logged to help diagnose the problem.

### Multiple Countries Per File

Multiple country tags can reference the same `common/countries/` file. This is useful for creating country variants that share graphical culture and base color definitions.

## Country File Structure

Country files in `common/countries/` define visual and cultural attributes:

```hoi4
graphical_culture = western_european_gfx
graphical_culture_2d = western_european_2d

color = { 255 0 0 }  # RGB format
# OR
color = hsv { 0.0 1.0 1.0 }  # HSV format
```

### Graphical Culture

The `graphical_culture` attribute determines 3D unit models and interface styling. Valid values are defined in `common/graphicalculturetype.txt`.

The `graphical_culture_2d` attribute controls 2D assets like advisor portraits and ace pilot images.

### Color System

Country colors use either RGB (0-255 per channel) or HSV (hue: 0-360, saturation: 0-1, value: 0-1) color models.

> [!CRITICAL] The game applies hidden modifiers to all color definitions: saturation is multiplied by 0.6 and value is multiplied by 0.8. These modifiers are defined in `NDefines.NGraphics.HSV_*` defines.

To achieve high saturation or value in the final rendered color, you must specify values greater than 1.0 in the definition. The engine clamps the result after applying modifiers. For example, to achieve pure red (HSV 0° 100% 100%):

```hoi4
color = hsv { 0 1.66 1.25 }
```

The `tag_color` console command displays colors without applying these modifiers, which can cause confusion during testing.

## Colors File Override

The `common/countries/colors.txt` file overrides color definitions from individual country files. This centralized file uses the format:

```hoi4
TAG = {
    color = rgb { 255 0 0 }
    color_ui = rgb { 200 0 0 }
}
```

### Color Attribute Usage

- `color`: Used for the political map mode (F1)
- `color_ui`: Used for the F10 intelligence map, history viewer, and division backgrounds

If `color_ui` is undefined, the game defaults to a gray shade rather than falling back to the `color` value.

## Flag System

Country flags are stored as TGA image files in `gfx/flags/`.

### Flag Naming Convention

Flags follow either ideology-specific or generic naming:
- Ideology-specific: `TAG_ideology.tga` (e.g., `GER_democratic.tga`)
- Generic fallback: `TAG.tga`

The game selects the ideology-specific flag when available, falling back to the generic flag otherwise.

### Flag Format Requirements

Flags must be 32-bit ARGB uncompressed TGA files with the origin point set to bottom-left.

**Common format issues:**

24-bit TGA files load successfully but generate performance warnings in the error log. Always use 32-bit ARGB format.

Top-left origin point causes flags to render upside down. Most online TGA converters incorrectly set the origin to top-left. Use Paint.NET, GIMP, or Photoshop to ensure proper bottom-left origin.

Paint.NET adds approximately 500 bytes of metadata to TGA files which some modding tools may interpret as a watermark.

### Flag Size Requirements

Flags come in three sizes with specific dimension and file size requirements:

| Size | Dimensions | File Size Range | Notes |
|------|------------|-----------------|-------|
| Standard | 82×52 | 16,998-17,510 bytes | Always required |
| Medium | 41×26 | 4,300-4,802 bytes | Requires ~10 dynamic tags |
| Small | 10×7 | 324-819 bytes | Requires ~20 dynamic tags |

Medium and small flags appear transparent for all countries when insufficient dynamic tags are allocated, with no error logged to help diagnose the issue.

## Related Defines

- `HSV_SATURATION_MODIFIER`: See [NGraphics](/defines_list/NGraphics.md)
- `HSV_VALUE_MODIFIER`: See [NGraphics](/defines_list/NGraphics.md)
