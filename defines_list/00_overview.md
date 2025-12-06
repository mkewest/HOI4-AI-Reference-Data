---
domain: defines_list
concept: overview
version: 1.14+
requires: [defines]
relates: []
---

# Defines List Overview

## Purpose

The `defines_list` domain provides a **complete enumeration of all HOI4 `NDefines` constants**, organized by their Lua category (e.g., `NGame`, `NMilitary`, `NGraphics`). It is the authoritative source for:

- Actual default values
- Value types and ranges
- Brief usage/context notes

For how defines work as a system (Lua syntax, loading, partial overrides, constraints), see **`/scripting/defines.md`**.

## File Structure

Each file corresponds to one `NDefines` category:

```text
/defines_list/
├── NGame.md
├── NGeography.md
├── NDiplomacy.md
├── NCountry.md
├── NResistance.md
├── NProduction.md
├── NMarket.md
├── NTechnology.md
├── NPolitics.md
├── NBuildings.md
├── NDeployment.md
├── NMilitary.md
├── NAir.md
├── NNavy.md
├── NRailwayGun.md
├── NTrade.md
├── NAI.md
├── NFocus.md
├── NOperatives.md
├── NIntel.md
├── NCharacter.md
├── NSupply.md
├── NAITheatre.md
├── NIndustrialOrganisation.md
├── NProject.md
├── NRaids.md
├── NWiki.md
├── NMapMode.md
├── NMapIcons.md
├── NAirGfx.md
├── NGraphics.md
├── NInterface.md
├── NFrontend.md
├── NSound.md
├── NFriendGUI.md
├── NCareerProfile.md
├── NCareerProfileGUI.md
└── (any future NDefines categories)
```

## Category Summary

The `Structures/defines_list_structure.md` file summarizes how many entries each category contains and their approximate size:

```yaml
NGame:
  entries: 15
  lines: 80
  depth: 2
NGeography:
  entries: 0
  lines: 1
  depth: 0
NDiplomacy:
  entries: 102
  lines: 507
  depth: 2
NCountry:
  entries: 88
  lines: 439
  depth: 2
NResistance:
  entries: 30
  lines: 148
  depth: 2
NProduction:
  entries: 30
  lines: 149
  depth: 2
NMarket:
  entries: 9
  lines: 47
  depth: 2
NTechnology:
  entries: 6
  lines: 32
  depth: 2
NPolitics:
  entries: 7
  lines: 37
  depth: 2
NBuildings:
  entries: 10
  lines: 53
  depth: 2
NDeployment:
  entries: 1
  lines: 7
  depth: 2
NMilitary:
  entries: 166
  lines: 815
  depth: 2
NAir:
  entries: 84
  lines: 407
  depth: 2
NNavy:
  entries: 170
  lines: 838
  depth: 2
NRailwayGun:
  entries: 13
  lines: 67
  depth: 2
NTrade:
  entries: 7
  lines: 36
  depth: 2
NAI:
  entries: 413
  lines: 2027
  depth: 2
NFocus:
  entries: 2
  lines: 12
  depth: 2
NOperatives:
  entries: 62
  lines: 300
  depth: 2
NIntel:
  entries: 109
  lines: 483
  depth: 2
NCharacter:
  entries: 7
  lines: 33
  depth: 2
NSupply:
  entries: 51
  lines: 246
  depth: 2
NAITheatre:
  entries: 9
  lines: 47
  depth: 2
NIndustrialOrganisation:
  entries: 9
  lines: 47
  depth: 2
NProject:
  entries: 0
  lines: 1
  depth: 0
NRaids:
  entries: 0
  lines: 1
  depth: 0
NWiki:
  entries: 1
  lines: 6
  depth: 2
NMapMode:
  entries: 40
  lines: 185
  depth: 2
NMapIcons:
  entries: 205
  lines: 825
  depth: 2
NAirGfx:
  entries: 19
  lines: 95
  depth: 2
NGraphics:
  entries: 212
  lines: 931
  depth: 2
NInterface:
  entries: 42
  lines: 207
  depth: 2
NFrontend:
  entries: 14
  lines: 62
  depth: 2
NSound:
  entries: 6
  lines: 29
  depth: 2
NFriendGUI:
  entries: 1
  lines: 7
  depth: 2
NCareerProfile:
  entries: 9
  lines: 47
  depth: 2
NCareerProfileGUI:
  entries: 3
  lines: 17
  depth: 2
```

Use this summary when you need to estimate size or choose which categories to load into context.

## Relationship to `/scripting/defines.md`

- **`/scripting/defines.md`** explains:
  - File structure and Lua syntax for defines.
  - Loading and override rules.
  - Constraints, limits, and critical edge cases (e.g., NO COMMAS rule, forbidden `00_defines.lua`, `MAX_EFFECT_ITERATION`, `GAME_SPEED_SECONDS`).
- **`/defines_list/*.md`** enumerates:
  - The actual `NDefines` entries for each category.
  - Their default values, types, and usage notes.

Recommended usage:

1. **Conceptual questions / safety** → read `/scripting/defines.md`.
2. **Find or inspect a specific define** → search in the appropriate `/defines_list/NCategory.md` file.
3. **Cross-domain references** → when other domains mention a define, verify the exact name and value in `defines_list` and the behavior constraints in `defines.md`.


