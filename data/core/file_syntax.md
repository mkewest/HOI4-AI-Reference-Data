---
domain: core
concept: file_syntax
version: 1.14+
relates: [mod_structure, assets]
---

# File Syntax

HOI4 uses a custom scripting format with specific syntax rules, encoding requirements, and directory conventions. Understanding these fundamentals is essential for creating valid mod files.

## Basic Syntax

### Format Structure

The core syntax pattern is attribute-argument pairs:

```hoi4
attribute = argument
```

Whitespace delimiters include spaces, newlines, and tabs - all are treated identically. An entire file can be written on one line if desired, though this reduces readability.

Comments use the hash symbol:

```hoi4
# This is a comment
attribute = value  # Inline comment
```

There is no multi-line comment block notation. Each comment line requires a `#` prefix.

### String Handling

Strings require quotation marks only if they contain whitespace:

```hoi4
simple_string = value
complex_string = "value with spaces"
```

Strings have a maximum length of 255 characters including the null terminator. Special characters require escape sequences:

- `\"` for literal quotation marks
- `\\` for literal backslashes

### Block Structure

Curly braces define nested blocks:

```hoi4
national_focus = {
    id = my_focus
    icon = GFX_goal_generic
    cost = 10
}
```

> [!CRITICAL] Extra closing brackets stop file parsing immediately. Everything after a stray `}` is ignored, which can create confusing bugs where the end of your file appears to have no effect.

Empty arguments break attribute parsing. When an attribute has no argument, the next attribute becomes its argument:

```hoi4
icon = 
x = 2
# Results in: icon = x, with 2 left dangling
```

Always provide explicit arguments or remove the attribute entirely.

## Encoding Standards

### File Type Requirements

Different file types require specific encodings:

| File Type | Encoding | BOM |
|-----------|----------|-----|
| .txt (scripts) | UTF-8 | No |
| .yml (localisation) | UTF-8 | Yes (required) |
| descriptor.mod | UTF-8 | No |
| User .mod files | UTF-8 | No |

> [!CRITICAL] Encoding mismatches cause silent load failures. The game reads the file but ignores all content without error messages. Localisation files must use UTF-8-BOM (opposite of descriptor files), or every localisation key fails to load.

Some text editors like Atom don't fully support BOM handling, making them unsuitable for localisation file editing. Use editors that explicitly support UTF-8-BOM for .yml files.

## Directory Structure

Standard mod directories serve specific purposes:

**common/**: Database definitions for countries, technologies, ideas, focuses, and game rules

**events/**: Event files for dynamic narrative content

**history/**: Starting state including country setup, state ownership, and unit deployment

**map/**: Map data files including provinces, terrain, and strategic regions

**localisation/**: Language text files for displaying names and descriptions

**gfx/**: Image files that require sprite definitions (except auto-loaded directories)

**interface/**: Sprite definitions and UI layout files

**music/**: Radio station definitions and audio files

**sound/**: Sound effect files

**portraits/**: Generic character portrait images

## Localisation Format

Localisation files follow a strict pattern:

```yml
l_english:
 key:0 "value"
 another_key:1 "another value"
```

The first line must be `l_<lang>:` where `<lang>` matches the filename pattern `*_l_<lang>.yml`. The version number (`:0`, `:1`) is purely cosmetic and can be any value or omitted entirely.

### Localisation Features

Empty localisation keys cause the game to display the key itself as fallback text, making typos immediately visible.

Localisation supports several advanced features:

**Newlines:** Use `\n` in localisation strings for line breaks

**Colors:** Use color codes like `§Y` for yellow text

**Dynamic text:** Reference scopes with brackets like `[GER.GetName]` to insert dynamic country names

Note that dynamic text using square brackets works in localisation files but not in plain string attributes. Direct string attributes only accept literal text.

## Sprite System

### Supported Formats

The game supports multiple image formats:

- **DDS (ARGB8):** Recommended for textures
- **TGA:** Required for flags
- **PNG:** Supported for general use
- **BMP:** Supported but rarely used

### Sprite Definitions

Most sprites require definitions in `interface/*.gfx` files before use. Three directories auto-load without definitions:

- `gfx/flags/`
- `gfx/loadingscreens/`
- `portraits/`

### Flag Requirements

Flag images have strict technical requirements:

- **Format:** 32-bit TGA
- **Compression:** No RLE encoding
- **Origin:** Bottom-left corner

Violating these requirements causes rendering errors or invisible flags.

### Sprite Errors

Common sprite-related issues:

**Transparent sprite:** File path is wrong or image file is corrupted

**Default image appears:** Sprite name is wrong or definition doesn't exist

**Random portrait:** Either of the above issues for character portraits

The palette error in rivers.bmp is the only MAP_ERROR that appears without debug mode enabled, typically occurring when GIMP saves indexed BMPs incorrectly.

## Constants System

Constants allow defining reusable values with the `@` prefix:

```hoi4
@PP_COST = 150
@XP_COST = 25

idea = {
    cost = @PP_COST
}
```

Constants are file-local in scope and can be defined anywhere in the file, not just at the top. Both numeric and string constants are supported.

> [!CRITICAL] String constants only work in triggers and element attributes. Using them in effects causes "invalid database object" errors. This limitation makes string constants primarily useful for GUI files and conditional checks.

Constants work in both `.txt` script files and `.gui` interface files.

## Related Systems

- Mod structure and encoding rules: See [Mod Structure](/core/mod_structure.md)
- Scripting data types: See [Scripting Data Types](/core/scripting_data_types.md)
- Sprite definitions in detail: See [Assets Domain](/assets/)
