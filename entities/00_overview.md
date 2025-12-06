---
domain: entities
concept: overview
version: 1.14+
relates: [content, database, military, map, assets]
---

# Entities Domain Structure

## Overview

The entities domain contains 8 markdown files covering core world entities in HOI4: countries, states, factions, characters, autonomy relationships, and visual/cosmetic country variants. These files bridge low-level data (tags, states) with higher-level content systems (focuses, events, decisions, AI).

## File Structure

```
/entities/
├── country_tags.md     - Country tag definitions and country files
├── country_history.md  - Country history setup and recruitment
├── states.md           - State grouping and state history
├── autonomy.md         - Subject/autonomy relationships
├── factions.md         - Faction creation and behavior
├── characters.md       - Characters, leaders, advisors, and commanders
├── cosmetic_tags.md    - Cosmetic country tags (names/flags/colors)
└── ideologies.md       - Country ideology setup and interactions
```

## File Descriptions

### country_tags.md
**Purpose**: Country tag system and visual country definition  
**Covers**: Tag definition in `common/country_tags/*.txt`, dynamic tags, reserved tags, country file references (`common/countries/*.txt`), graphical culture, color systems (RGB/HSV), and hidden saturation/value modifiers  
**Key relationships**: Requires basic file structure knowledge, relates to country_history, flags, colors, and localisation

### country_history.md
**Purpose**: Country startup configuration  
**Covers**: Country history files in `history/countries/*.txt`, government setup, starting territories and cores, OOB references, starting ideas and laws, advisors, leaders, and scripted setup events  
**Key relationships**: Requires country_tags and states, relates to characters, ideas, autonomy, and factions

### states.md
**Purpose**: State system and state history  
**Covers**: State definitions in `history/states/*.txt`, mandatory attributes (id, name, manpower, category, provinces), history block (owner/controller, buildings, victory points), state categories, and state-specific edge cases  
**Key relationships**: Requires provinces and strategic_regions (map domain), relates to buildings, victory points, manpower, and state_categories

### autonomy.md
**Purpose**: Subject/autonomy mechanics  
**Covers**: Autonomy state definitions in `common/autonomous_states/*.txt`, freedom levels, default puppet levels, point calculations, manpower influence, rule and modifier blocks, DLC requirements, and interaction with defines  
**Key relationships**: Requires country_tags and ideologies, conflicts with older independence mechanics, relates to factions, diplomacy, subjects, and country_history

### factions.md
**Purpose**: Faction creation and membership rules  
**Covers**: Faction templates, scripted faction creation, joining and leaving factions, rules and modifiers affecting faction behavior, and AI interaction with factions  
**Key relationships**: Relates to autonomy, diplomacy, country_history, and ideologies

### characters.md
**Purpose**: Character system for leaders, advisors, and commanders  
**Covers**: Character definitions in `common/characters/*.txt`, character IDs, name and gender, portraits and ideology-specific portraits, roles (country_leader, advisor, corps_commander, field_marshal, operative), recruitment methods, traits, and interactions with other systems  
**Key relationships**: Requires country_tags and ideologies, relates to portraits, traits, advisors, unit_leaders, and country_history

### cosmetic_tags.md
**Purpose**: Cosmetic country tags for alternate names and flags  
**Covers**: Cosmetic tag definitions, linking cosmetics to base tags, conditions for switching cosmetics (ideology, focus, autonomy), name and flag overrides, and usage patterns  
**Key relationships**: Requires country_tags and ideologies, relates to autonomy, factions, and localisation

### ideologies.md
**Purpose**: Country-level ideology setup and links to ideology system  
**Covers**: Assigning starting ideologies and popularity in history files, dynamic ideology changes, interaction with national spirits and parties, and linkage to the global ideology definitions  
**Key relationships**: Requires global ideology system (database/ideologies.md), relates to country_history, autonomy, and factions

## Semantic Groupings

### Country Identity and Visuals
- country_tags.md: Tags, country files, graphical culture, colors
- cosmetic_tags.md: Cosmetic variants for names/flags/colors

These files define how countries are identified and presented visually.

### Territorial and Structural Entities
- states.md: State grouping of provinces and state history
- country_history.md: Country setup, ownership, and starting conditions

Together they control how the world map is partitioned and who owns what at game start.

### Political and Relationship Systems
- autonomy.md: Subject relationships and autonomy levels
- factions.md: Alliances and faction membership
- ideologies.md: Country ideology setup (ties into global ideology system)

These govern how countries relate to each other politically.

### People and Leadership
- characters.md: Leaders, advisors, and commanders

This links countries to individual personas that participate in politics, military, and intelligence.

## Usage Patterns

### For New Country Modders
1. Define tags and country files in **country_tags.md** (see referenced structure).
2. Create starting setup in **country_history.md** (government, OOB, ideas).
3. Define states in **states.md** (IDs, provinces, buildings, VPs).

### For Subject and Faction Mechanics
- Use **autonomy.md** to design subject levels and transitions.
- Use **factions.md** to script faction creation and join rules.

### For Character and Cosmetic Work
- Use **characters.md** for all character definitions and recruitment.
- Use **cosmetic_tags.md** for alternate country names/flags keyed to conditions.

## Critical Dependencies

Files that MUST be read together for complete understanding:

1. **country_tags.md + country_history.md**: Tags are meaningless without corresponding history setup.
2. **states.md + provinces.md (map)**: States reference province IDs and depend on valid map definitions.
3. **autonomy.md + country_tags.md + ideologies.md**: Autonomy levels rely on correct country and ideology setups.
4. **characters.md + portraits.md (assets)**: Character definitions require correct portrait sprites and categories.


