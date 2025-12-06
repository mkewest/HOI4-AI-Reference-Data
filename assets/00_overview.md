---
domain: assets
concept: overview
version: 1.14+
relates: [core, scripting, database, map, military]
---

# Assets Domain Structure

## Overview

The assets domain contains 10 markdown files covering all visual, audio, and interface systems in Hearts of Iron IV. Files are organized by semantic cohesion rather than strict technical boundaries.

## File Structure

```
/assets/
├── sprites.md          - Visual asset definitions and animation
├── interface.md        - GUI containers and elements
├── localisation.md     - Text translation and formatting
├── scripted_gui.md     - Dynamic GUI logic and interactions
├── fonts.md            - Font bitmaps and definitions
├── sound.md            - Audio system and mixing
├── portraits.md        - Character portrait system
├── entities.md         - 3D models and animation states
├── particles.md        - Particle effects editor
└── posteffects.md      - Visual filters and color grading
```

## File Descriptions

### sprites.md (~1800 tokens)
**Purpose**: Visual asset definitions for GUI elements  
**Covers**: spriteType, frameAnimatedSpriteType, progressbartype, corneredTileSpriteType, maskedShieldType, animation system, map text  
**Key relationships**: Required by interface elements, relates to fonts and localization

### interface.md (~2400 tokens)
**Purpose**: GUI layout and element rendering  
**Covers**: containerWindowType, element types, scrollbars, drag scrolling, clipping, background, rendering order, scripted GUI compatibility  
**Key relationships**: Requires sprites, relates to scripted_gui and localisation

### localisation.md (~2600 tokens)
**Purpose**: Text translation and dynamic content formatting  
**Covers**: File structure, color codes, variable formatting, namespaces, nesting, text icons, flags, bindable localization, contextual localization, formatters, scripted localization, replace folders  
**Key relationships**: Requires scripted_loc, relates to interface, sprites, and scripted_gui  
**Note**: Largest file due to high edge case density and feature interaction complexity

### scripted_gui.md (~1600 tokens)
**Purpose**: Links interface to game logic  
**Covers**: Window assignment, parent window integration, context system, effects, triggers, dynamic lists, properties, dirty evaluation, AI system, localization commands  
**Key relationships**: Requires interface and localisation, relates to effects, triggers, and scopes

### fonts.md (~1400 tokens)
**Purpose**: Text rendering system  
**Covers**: Bitmapfont definitions, bitmap size limits, character spacing, multiple bitmaps, kerning, language overrides, map font, color definitions, BMFont export workflow  
**Key relationships**: Requires localisation, relates to sprites and interface

### sound.md (~800 tokens)
**Purpose**: Audio playback and mixing  
**Covers**: Sound definitions, audio format requirements, behavior attributes, compressor system (global and category-specific)  
**Key relationships**: Operates independently, relates to general assets

### portraits.md (~700 tokens)
**Purpose**: Character image display  
**Covers**: Portrait priority (tag > continent > default), gender fallback, portrait categories, ideology-specific portraits, portrait pools, GFX dependency  
**Key relationships**: Requires sprites and characters, relates to countries and ideologies

### entities.md (~1100 tokens)
**Purpose**: 3D model animation and behavior  
**Covers**: State availability, state selection, state inheritance, animation reference chain, attachments, events, timing, particle persistence  
**Key relationships**: Requires animations and particles, relates to units, buildings, and 3d_models

### particles.md (~500 tokens)
**Purpose**: Particle effect creation  
**Covers**: Particle editor version requirement (exactly 1.11), editor access, editing workflow limitations, integration with entities  
**Key relationships**: Relates to entities and visual_effects  
**Note**: Smallest file - focused on critical editor usage constraints

### posteffects.md (~800 tokens)
**Purpose**: Map visual atmosphere  
**Covers**: Posteffect values, seasonal variants, inheritance, position volumes, height volumes, volume overlap, console commands, coordinate system  
**Key relationships**: Relates to map and graphics_settings

## Dependency Graph

```
sprites.md
    ↓ (required by)
interface.md ←→ localisation.md
    ↓ (both required by)
scripted_gui.md

fonts.md → localisation.md

portraits.md → sprites.md
portraits.md → characters (external)

entities.md → animations (external)
entities.md → particles.md

sound.md (independent)

posteffects.md → map (external)
```

## Semantic Groupings

### Core GUI Stack (interdependent)
- sprites.md: Visual assets
- interface.md: Layout and rendering
- localisation.md: Text and formatting
- scripted_gui.md: Logic and interactivity

These four files form the complete GUI system and frequently reference each other.

### Text Rendering
- fonts.md: Font system
- localisation.md: Text formatting

Font system depends on localization for color codes and text rendering.

### Visual Assets
- sprites.md: 2D assets
- portraits.md: Character images
- entities.md: 3D models
- particles.md: Effects
- posteffects.md: Filters

Each handles a different visual domain but all contribute to overall presentation.

### Audio
- sound.md: Standalone audio system

## Token Distribution

| File | Token Count | Percentage |
|------|-------------|------------|
| localisation.md | ~2600 | 20.3% |
| interface.md | ~2400 | 18.8% |
| sprites.md | ~1800 | 14.1% |
| scripted_gui.md | ~1600 | 12.5% |
| fonts.md | ~1400 | 10.9% |
| entities.md | ~1100 | 8.6% |
| sound.md | ~800 | 6.3% |
| posteffects.md | ~800 | 6.3% |
| portraits.md | ~700 | 5.5% |
| particles.md | ~500 | 3.9% |
| **Total** | **~12,800** | **100%** |

Average: ~1,280 tokens per file

## Edge Case Integration

All edge cases from `assets_EdgeCases.txt` have been integrated inline at their point of relevance:

- **File encoding issues**: Integrated into localisation.md and sound.md
- **Interface container visibility**: Integrated into interface.md
- **Scrollbar requirements**: Integrated into interface.md
- **Localization syntax errors**: Integrated into localisation.md
- **Color code behavior**: Integrated into localisation.md
- **Font spacing requirements**: Integrated into fonts.md
- **Portrait GFX dependency**: Integrated into portraits.md
- **Entity state inheritance**: Integrated into entities.md
- **Particle editor version**: Integrated into particles.md
- **Posteffect overlap behavior**: Integrated into posteffects.md

No separate edge case files exist - all warnings and gotchas appear in context where users encounter them.

## Usage Patterns

### For New Modders
Start with: sprites.md → interface.md → localisation.md sequence to understand basic GUI creation.

### For GUI Scripting
Focus on: scripted_gui.md (requires understanding of interface.md and localisation.md first).

### For Visual Artists
Key files: sprites.md, portraits.md, entities.md, particles.md, posteffects.md.

### For Audio Designers
Primary file: sound.md (relatively independent).

### For Localization Teams
Primary file: localisation.md with reference to fonts.md for character support.

## Critical Dependencies

Files that MUST be read together for complete understanding:

1. **interface.md + scripted_gui.md**: GUI structure and behavior are inseparable
2. **localisation.md + fonts.md**: Text rendering requires both systems
3. **entities.md + particles.md**: 3D models and effects integrate closely
4. **sprites.md + interface.md**: GUI elements require sprite definitions

## File Maturity

All files represent stable HOI4 systems as of version 1.14+. Version-specific features are noted in YAML frontmatter or inline text (e.g., "Version 1.5+" for scripted GUI properties).


