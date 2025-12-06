---
domain: core
concept: overview
version: 1.14+
relates: [scripting, map, military, database, assets]
---

# Core Domain Structure

## Overview

The core domain contains 9 markdown files covering fundamental modding concepts, file systems, scripting data structures, debugging tools, and troubleshooting workflows in Hearts of Iron IV. Files are organized by semantic cohesion rather than strict technical boundaries.

## File Structure

```
/core/
├── mod_structure.md         - Mod paths, descriptors, and loading
├── load_order.md            - File loading and evaluation sequence
├── file_syntax.md           - Script syntax and encoding rules
├── scripting_data_types.md  - Variables, flags, arrays, and game data
├── console_commands.md      - Debug console and cheat commands
├── debug_tools.md           - Debug mode, logs, and crash analysis
├── nudger.md                - Map editing tool and output behavior
├── troubleshooting.md       - Crash diagnosis and debugging strategies
└── metadata.md              - Checksums and special files
```

## File Descriptions

### mod_structure.md (~1500 tokens)
**Purpose**: Mod installation, descriptors, and file organization
**Covers**: User directory paths, dual descriptor system, descriptor attributes, encoding requirements, replace_path mechanism, thumbnail system, file loading behavior
**Key relationships**: Requires file_syntax and encoding_rules, relates to load_order and file_structure

### load_order.md (~930 tokens)
**Purpose**: Content loading priority and evaluation sequence
**Covers**: Load sequence (base game → DLC → user dir → mods), dependency override, filename dependencies, evaluation order, duplicate attribute handling, tag definition order
**Key relationships**: Requires mod_structure, relates to file_syntax and duplicates

### file_syntax.md (~1134 tokens)
**Purpose**: Core scripting language rules
**Covers**: Basic syntax (attribute = value), string handling, block structure, encoding standards (UTF-8 vs UTF-8-BOM), directory structure, localisation format, sprite system, constants
**Key relationships**: Foundation file with no requirements, relates to mod_structure and assets

### scripting_data_types.md (~2027 tokens)
**Purpose**: Dynamic data structures for game logic
**Covers**: Constants, flags, variables (with scoping and operators), arrays, event targets, token values, country tag aliases, scorers, MTTH variables, game variables, game arrays
**Key relationships**: Requires file_syntax, relates to scripting_effects and console_commands
**Note**: Largest file due to comprehensive coverage of all scripting data structures and their interactions

### console_commands.md (~1670 tokens)
**Purpose**: Interactive debugging and testing commands
**Covers**: Console access, ID discovery, country switching, resources, equipment, construction, research, focus, decision, training, diplomacy, intel, territory, variables, flags, scripting, AI, debug, reload, camera, special projects, deprecated/broken commands
**Key relationships**: Requires scripting_data_types, relates to debug_tools and scripting_effects

### debug_tools.md (~1210 tokens)
**Purpose**: Development and troubleshooting features
**Covers**: Debug mode (-debug flag), auto-reload limitations, crash data log (-crash_data_log flag), log files (error.log, game.log, setup.log, memory.log, etc.), debugging effects (log, print_variables), console variable commands
**Key relationships**: Requires file_syntax and mod_structure, relates to console_commands and troubleshooting

### nudger.md (~1646 tokens)
**Purpose**: Map editing interface and output management
**Covers**: Nudger access methods, output location warnings, states section, strategic regions section, database section, weather section, buildings section, supply section, removed supply areas
**Key relationships**: Requires debug_tools and map_structure, relates to states, strategic_regions, and supply

### troubleshooting.md (~1658 tokens)
**Purpose**: Crash diagnosis and resolution workflows
**Covers**: Crash types (fatal vs non-fatal), loading phase crashes, country selection crashes, mid-game crashes, specialized crash patterns (ownerless states, AI templates, naval bases, countries limit, bitmap constraints), debugging strategies (binary search, log cleaning), crash data log analysis
**Key relationships**: Requires mod_structure and file_syntax, relates to debug_tools, map_structure, and military

### metadata.md (~636 tokens)
**Purpose**: Game integrity and compatibility systems
**Covers**: Checksum system (calculation, multiplayer compatibility, achievements), order matters rules (order-sensitive vs order-irrelevant content), special files (settings.txt, dlc_load.json, launcher-v2.sqlite)
**Key relationships**: Requires mod_structure, relates to multiplayer and achievements
**Note**: Smallest file - focused on specific metadata concepts

## Dependency Graph

```
                    file_syntax.md (foundation)
                         ↓
        ┌────────────────┼────────────────┐
        ↓                ↓                ↓
mod_structure.md  scripting_data_types.md  (relates to assets)
        ↓                ↓
    load_order.md   console_commands.md
        ↓                ↓
    metadata.md      debug_tools.md ←→ troubleshooting.md
                         ↓
                     nudger.md
```

## Semantic Groupings

### Foundational Systems (prerequisite knowledge)
- file_syntax.md: Language rules
- mod_structure.md: File organization
- load_order.md: Loading sequence

These three files define how mods are structured and loaded.

### Scripting Infrastructure
- scripting_data_types.md: Data structures
- console_commands.md: Interactive testing

Understanding data types is essential for using console commands effectively.

### Development Tools
- debug_tools.md: Debugging features
- nudger.md: Map editing
- troubleshooting.md: Crash diagnosis

These form the complete debugging workflow from setup through diagnosis.

### Metadata
- metadata.md: Standalone reference for checksums and special files

## Token Distribution

| File | Token Count | Percentage |
|------|-------------|------------|
| scripting_data_types.md | ~2027 | 16.5% |
| console_commands.md | ~1670 | 13.6% |
| troubleshooting.md | ~1658 | 13.5% |
| nudger.md | ~1646 | 13.4% |
| mod_structure.md | ~1503 | 12.2% |
| debug_tools.md | ~1210 | 9.9% |
| file_syntax.md | ~1134 | 9.2% |
| load_order.md | ~930 | 7.6% |
| metadata.md | ~636 | 5.2% |
| **Total** | **~12,314** | **100%** |

Average: ~1,368 tokens per file

## Edge Case Integration

All edge cases from `core_EdgeCases.txt` have been integrated inline at their point of relevance:

- **Loading & file handling quirks**: Integrated into mod_structure.md and load_order.md
- **Encoding mismatches**: Integrated into file_syntax.md and mod_structure.md
- **Replace_path limitations**: Integrated into mod_structure.md
- **Evaluation order issues**: Integrated into load_order.md
- **Descriptor & launcher edge cases**: Integrated into mod_structure.md
- **Sprite rendering errors**: Integrated into file_syntax.md
- **Localisation syntax**: Integrated into file_syntax.md
- **Constants limitations**: Integrated into file_syntax.md
- **Defines override warnings**: Integrated into file_syntax.md (referenced in scripting context)
- **Flag behavior quirks**: Integrated into scripting_data_types.md
- **Variable overflow and scoping**: Integrated into scripting_data_types.md
- **Array iteration warnings**: Integrated into scripting_data_types.md
- **Event target persistence**: Integrated into scripting_data_types.md
- **Console command behavior**: Integrated into console_commands.md
- **Nudger output location warnings**: Integrated into nudger.md
- **Nudger subsystem crashes**: Integrated into nudger.md
- **Crash data log interpretation**: Integrated into debug_tools.md and troubleshooting.md
- **Crash cascade patterns**: Integrated into troubleshooting.md
- **State without owner crashes**: Integrated into troubleshooting.md
- **AI template crashes**: Integrated into troubleshooting.md
- **Naval base building crashes**: Integrated into troubleshooting.md
- **Bitmap constraint crashes**: Integrated into troubleshooting.md

No separate edge case files exist - all warnings and gotchas appear in context where users encounter them.

## Usage Patterns

### For New Modders
Start with: file_syntax.md → mod_structure.md → load_order.md sequence to understand basic modding infrastructure.

### For Scripters
Focus on: scripting_data_types.md (requires understanding of file_syntax.md first), then console_commands.md for testing.

### For Debugging
Key files: debug_tools.md → troubleshooting.md → nudger.md (for map issues).

### For Multiplayer Modding
Primary file: metadata.md for checksum implications.

### For Map Creators
Primary files: nudger.md with frequent reference to troubleshooting.md for crash patterns.

## Critical Dependencies

Files that MUST be read together for complete understanding:

1. **file_syntax.md + mod_structure.md**: Syntax rules and file organization are inseparable
2. **debug_tools.md + troubleshooting.md**: Debugging features and crash diagnosis form complete workflow
3. **scripting_data_types.md + console_commands.md**: Data structures and console testing integrate closely
4. **mod_structure.md + load_order.md**: File organization and loading sequence determine override behavior

## File Maturity

All files represent stable HOI4 systems as of version 1.14+. Version-specific features are noted in YAML frontmatter or inline text where relevant. Deprecated systems (e.g., supply areas pre-1.11, Workshop .zip archives pre-1.9) are documented with clear version markers.

## Relationship to Other Domains

### Core → Map
- nudger.md extensively references map systems (states, provinces, strategic regions, supply)
- troubleshooting.md covers map-specific crashes (bitmap constraints, province definitions)

### Core → Military
- troubleshooting.md covers AI template crashes
- console_commands.md includes equipment and unit commands

### Core → Scripting
- scripting_data_types.md provides foundation for all scripting domains
- console_commands.md enables testing of scripted content

### Core → Assets
- file_syntax.md covers sprite and localisation basics
- mod_structure.md explains directory structure including gfx/ and interface/

The core domain serves as the foundational layer that all other domains depend on.


