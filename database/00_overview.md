---
domain: database
concept: overview
version: 1.14+
relates: [content, military, map, modifiers_list, defines_list]
---

# Database Domain Structure

## Overview

The database domain contains 10 markdown files covering all core game data systems in Hearts of Iron IV. Files are organized by semantic cohesion and functional relationships rather than strict file structure boundaries.

## File Structure

```
/database/
├── ideas_core.md           - National idea mechanics and modifiers
├── ideas_categories.md     - Idea slot system and GUI
├── ideologies.md           - Political ideology system
├── technologies_core.md    - Research mechanics and tech trees
├── technologies_gui.md     - Tech tree display and positioning
├── equipment.md            - Military equipment definitions
├── buildings.md            - Constructible structures
├── resources.md            - Strategic resource system
├── balance_of_power.md     - Dynamic relationship sliders
└── namelists.md            - Unit and ship naming
```

## File Descriptions

### ideas_core.md (~2000 tokens)
**Purpose**: Core national idea mechanics and effect systems  
**Covers**: Idea structure, picture system, five modifier types (standard/research/equipment/targeted/rules), effect blocks (on_add/on_remove), triggers (allowed/visible/available/cancel), selectable ideas, cost system, idea modification via swap_ideas  
**Key relationships**: Requires localisation, relates to characters, modifiers_list, ideas_categories  
**Critical edge cases**: GFX_idea_ prefix auto-insertion, on_add doesn't execute in history files, allowed_civil_war defaults false, modifier separation

### ideas_categories.md (~1200 tokens)
**Purpose**: Idea slot organization and GUI configuration  
**Covers**: Category definitions, slot attributes (cost/removal_cost/ledger), slot_ledgers system, special flags (designer/law/use_list_view), GUI gridbox limits, category icon frames, cost modifiers, load order issues  
**Key relationships**: Requires ideas_core, relates to interface, sprites, characters  
**Critical edge cases**: 7-slot gridbox limit causes silent failures, character slot cost modifiers fail due to load order, generic advisors need zzz_ prefix, noOfFrames must match category count

### ideologies.md (~1800 tokens)
**Purpose**: Political ideology groups and government systems  
**Covers**: Ideology structure (groups vs subideologies), subideology attributes, popularity system, rules block, modifiers (tension/cost factors), world tension impact, faction modifiers, dynamic faction names, localisation overrides, GFX sprite priority, AI peace configuration, history setup  
**Key relationships**: Requires localisation, relates to characters, ai_strategy, factions  
**Critical edge cases**: Leaders use subideology names not groups, set_popularities must sum to exactly 100, faction modifiers only apply to faction leader, country-specific subideology names override groups, AI defaults to fascist peace without custom files

### technologies_core.md (~1800 tokens)
**Purpose**: Research system mechanics and tech unlocking  
**Covers**: Tech structure, visibility system (hidden by default), allow vs allow_branch, research cost (base/start_year penalty/path modification), pathing (path OR logic, dependencies AND logic, XOR mutual exclusion), sub-technologies, enabling objects (equipment/subunits/modules/buildings/tactics), unit-specific modifiers, on_research_complete effects, AI research, categories, experience system, tech sharing  
**Key relationships**: Requires equipment, buildings, units, relates to technologies_gui, modifiers_list  
**Critical edge cases**: Hidden by default, allow blocks GUI not effects, buildings level is absolute not cumulative, on_research_complete doesn't run in history, AI requires categories in ai_focuses, XOR must be in all mutual techs, unresearch doesn't work properly, special terrain types (amphibious/river)

### technologies_gui.md (~1000 tokens)
**Purpose**: Technology tree display and positioning  
**Covers**: GUI files (standard vs doctrine), gridbox requirements, secondary paths (ignore_for_layout), folder positioning, coordinate systems (LEFT vs UP format), visibility requirements, doctrine system, tech icons (standard/country-specific/equipment fallback), sub-tech display  
**Key relationships**: Requires technologies_core, relates to interface, sprites  
**Critical edge cases**: Techs without path AND gridbox never appear, secondary paths need ignore_for_layout, start_year doesn't affect folder display, doctrine needs both tech flag and GUI folder marking

### equipment.md (~1400 tokens)
**Purpose**: Military hardware definitions and stats  
**Covers**: Archetype vs specific equipment structure, inheritance system, is_buildable flag, modifier types (universal/land base/land offensive/land defensive/naval/air), obsolete modifiers, naval shore bombardment, localisation, production unlocking  
**Key relationships**: Requires technologies_core, relates to units, resources, modifiers_list  
**Critical edge cases**: maximum_speed defaults to 4, surface/sub visibility is inverted (lower = harder to detect), shore_bombardment obsolete (use lg_attack + hg_attack), inheritance is complete unless overridden, equipment usable before tech unlock via effects

### buildings.md (~2200 tokens)
**Purpose**: Constructible structures and positioning  
**Covers**: Building structure, cost system (base_cost/per_level_extra_cost arithmetic progression), slot categories (shared/state/provincial), level caps (state_max/province_max), tech requirements (GUI-only), modifiers (country modifiers/enable_for_controllers), attributes (value/damage_factor/allied_build), visual display (show_on_map/meshes/destroyed), positioning (buildings.txt format/coordinates/rotation), special types (railways/supply/ports/infrastructure/production/specialized)  
**Key relationships**: Requires states, provinces, relates to supply, infrastructure, technologies_core  
**Critical edge cases**: MAX_SHARED_SLOTS is per-state total, tech bypass via effects/history, only_costal typo is correct spelling, buildings.txt must not be empty, railways/supply can't use add_building_construction, damage_factor 0 = invulnerable, y coordinate range [0, 25.5]

### resources.md (~800 tokens)
**Purpose**: Strategic material system  
**Covers**: Resource definition (icon_frame/cic/convoys), graphics configuration (GFX_resources_strip/GFX_missing_resources_strip), UI integration (element naming), localisation (PRODUCTION_MATERIALS_ prefix), fuel system (FUEL_RESOURCE define/single fuel only), infrastructure bonus (universal to all resources)  
**Key relationships**: Requires buildings, relates to sprites, trade, infrastructure  
**Critical edge cases**: noOfFrames must match resource count in both strips, cic is inverted (lower = more per factory), cic max 1.0, UI elements case-sensitive exact naming, only one fuel resource (last wins), infrastructure bonus applies equally to all

### balance_of_power.md (~1200 tokens)
**Purpose**: Dynamic relationship slider mechanics  
**Covers**: BoP structure, value system ([-1,1] range with 3 decimal precision), side definitions (left/right), range system (min/max boundaries), modifiers and rules, effects (on_activate/on_deactivate), global tracking, decision category integration, static modifiers (power_balance_daily/weekly), effects and triggers  
**Key relationships**: Requires modifiers_list, decisions, relates to modifiers  
**Critical edge cases**: Side assignment only controls visibility not logic, duplicate range IDs display all but trigger checks first only, max is exclusive except when max=1, BoP value shared across all countries with same ID, modifiers stack between countries, decision category becomes BoP-exclusive, set_default resets everything, modifiers are cloned per country

### namelists.md (~1000 tokens)
**Purpose**: Military unit and ship naming systems  
**Covers**: Division namelists (structure/ordered block/OOB linking/file size limits), ship namelists (structure/ship_types/no OOB linking/unique space delimiters), generic namelists (fallback/empty unique), operative codenames (mutually exclusive/random assignment), placeholder variables (%d/%s)  
**Key relationships**: Requires units, navies, relates to oob, localisation  
**Critical edge cases**: 1500-line file limit causes failures beyond, NAME_LIST_ID must match exactly, ship_types needs MTG + base types, unique uses spaces not commas, generic unique must be empty array, operative codenames mutually exclusive

## Dependency Graph

```
localisation_system (external)
    ↓ (required by)
ideas_core.md → ideas_categories.md
    ↓
characters (external)

localisation_system (external)
    ↓ (required by)
ideologies.md
    ↓
country_leaders, factions (external)

equipment.md, buildings.md, units (external)
    ↓ (all required by)
technologies_core.md → technologies_gui.md
    ↓
ai_focuses, tech_sharing (external)

technologies_core.md
    ↓ (required by)
equipment.md
    ↓
units, production (external)

states.md, provinces.md (external)
    ↓ (required by)
buildings.md
    ↓
supply, infrastructure (external)

buildings.md, production (external)
    ↓ (required by)
resources.md
    ↓
trade (external)

modifiers_list, decisions (external)
    ↓ (required by)
balance_of_power.md

units.md, ships.md (external)
    ↓ (required by)
namelists.md
```

## Semantic Groupings

### National Idea System (tightly coupled)
- ideas_core.md: Core mechanics
- ideas_categories.md: Slot organization and GUI

These files are split to keep token counts manageable, but form a single conceptual system.

### Technology System (tightly coupled)
- technologies_core.md: Research mechanics
- technologies_gui.md: Display system

Split by functionality (mechanics vs presentation) to maintain clarity.

### Political Systems
- ideologies.md: Government types and political rules
- balance_of_power.md: Dynamic relationship mechanics

Both handle political mechanics but at different scopes.

### Production Chain
- equipment.md: Hardware definitions
- buildings.md: Construction structures
- resources.md: Strategic materials

These three form the production pipeline from resources → buildings → equipment.

### Naming Systems
- namelists.md: Unit/ship/operative naming (standalone)

## Token Distribution

| File | Token Count | Percentage |
|------|-------------|------------|
| buildings.md | ~2200 | 17.2% |
| ideas_core.md | ~2000 | 15.6% |
| ideologies.md | ~1800 | 14.1% |
| technologies_core.md | ~1800 | 14.1% |
| equipment.md | ~1400 | 10.9% |
| ideas_categories.md | ~1200 | 9.4% |
| balance_of_power.md | ~1200 | 9.4% |
| technologies_gui.md | ~1000 | 7.8% |
| namelists.md | ~1000 | 7.8% |
| resources.md | ~800 | 6.3% |
| **Total** | **~12,800** | **100%** |

Average: ~1,280 tokens per file

## Edge Case Integration

All 45 edge case sections from `database_EdgeCases.txt` have been integrated inline at their point of relevance:

**Ideas System (15 sections)**:
- Picture/sprite prefix auto-insertion → ideas_core.md
- Effect timing in history files → ideas_core.md
- Localisation fallback behavior → ideas_core.md
- Modification via swap_ideas → ideas_core.md
- Civil war default behavior → ideas_core.md
- Cost modifier load order → ideas_categories.md
- Trigger evaluation frequency → ideas_core.md
- Equipment bonus tech requirement → ideas_core.md
- GUI gridbox limits → ideas_categories.md
- Sprite frame assignment → ideas_categories.md
- Allowed bypass via effects → ideas_core.md
- Level cost accumulation → ideas_core.md
- Modifier attribute separation → ideas_core.md
- Targeted modifier direction → ideas_core.md

**Ideologies (7 sections)**:
- Popularities sum requirement → ideologies.md
- AI peace defaults → ideologies.md
- Localisation override priority → ideologies.md
- GFX sprite priority system → ideologies.md
- Generic advisor load order → ideas_categories.md
- Leader ideology naming → ideologies.md
- Modifier ranges → ideologies.md
- Faction modifier leader-only → ideologies.md

**Technologies (14 sections)**:
- Hidden by default → technologies_core.md
- Gridbox requirements → technologies_gui.md
- Building level absolute values → technologies_core.md
- Unresearch failures → technologies_core.md
- Localisation fallback chain → technologies_core.md
- Cost calculation smoothing → technologies_core.md
- Path vs dependencies logic → technologies_core.md
- Sub-tech indexing → technologies_core.md
- Coordinate system formats → technologies_gui.md
- AI category requirements → technologies_core.md
- Effect execution contexts → technologies_core.md
- Doctrine dual requirements → technologies_gui.md
- Tech sharing restrictions → technologies_core.md
- Special terrain types → technologies_core.md

**Equipment (5 sections)**:
- Maximum speed defaults → equipment.md
- Obsolete modifiers → equipment.md
- Complete inheritance → equipment.md
- Naval visibility inversion → equipment.md
- Country-specific localisation → equipment.md

**Buildings (11 sections)**:
- Arithmetic cost progression → buildings.md
- Shared slot totals → buildings.md
- Tech requirement bypass → buildings.md
- Controller modifier scoping → buildings.md
- Coordinate y-range limits → buildings.md
- Railway construction crashes → buildings.md
- Infrastructure bonus calculation → buildings.md
- Icon frame indexing → buildings.md
- Entity mesh naming → buildings.md
- Coastal typo spelling → buildings.md
- Damage factor invulnerability → buildings.md
- Allied build scope → buildings.md
- DMZ dual blocking → buildings.md

**Resources (4 sections)**:
- Sprite frame synchronization → resources.md
- CIC inversion → resources.md
- UI element naming → resources.md
- Single fuel resource → resources.md
- Universal infrastructure bonus → resources.md

**Balance of Power (6 sections)**:
- Global value sharing → balance_of_power.md
- Range assignment visibility → balance_of_power.md
- Duplicate range ID behavior → balance_of_power.md
- Max boundary inclusivity → balance_of_power.md
- Decision category exclusivity → balance_of_power.md
- Modifier cloning → balance_of_power.md
- Set_default override → balance_of_power.md

**Namelists (4 sections)**:
- File line limits → namelists.md
- Ship type dual requirements → namelists.md
- Generic empty unique → namelists.md
- Operative codename exclusivity → namelists.md

No separate edge case files exist - all warnings and gotchas appear in context where users encounter them.

## Usage Patterns

### For New Modders
Start with: ideologies.md → ideas_core.md → technologies_core.md sequence to understand core game systems.

### For Gameplay Designers
Focus on: ideas_core.md, ideologies.md, balance_of_power.md for political mechanics and national spirits.

### For Military Designers
Key files: technologies_core.md, equipment.md, namelists.md for research trees and military hardware.

### For Economic Modders
Primary files: buildings.md, resources.md, equipment.md for production chains.

### For GUI Designers
Reference: ideas_categories.md, technologies_gui.md for interface integration.

## Critical Dependencies

Files that MUST be read together for complete understanding:

1. **ideas_core.md + ideas_categories.md**: Core mechanics and GUI system are split but inseparable
2. **technologies_core.md + technologies_gui.md**: Research mechanics and display system form one complete system
3. **equipment.md + technologies_core.md**: Equipment definitions depend on tech unlocking mechanics
4. **buildings.md + resources.md**: Buildings produce resources, forming production pipeline
5. **ideologies.md + ideas_core.md**: National spirits often reference ideology-specific mechanics

## File Maturity

All files represent stable HOI4 systems as of version 1.14+ (except balance_of_power.md which is 1.13+). Version-specific features are noted in YAML frontmatter or inline text where relevant.

## System Interdependencies

### Political Layer
ideologies.md → ideas_core.md → balance_of_power.md  
Forms complete political system from government types through national spirits to dynamic relationships.

### Military Layer
technologies_core.md → equipment.md → namelists.md  
Forms complete military system from research through production to unit naming.

### Economic Layer
resources.md → buildings.md → equipment.md  
Forms complete economic system from strategic materials through construction to military production.

### Interface Layer
ideas_categories.md + technologies_gui.md  
Both connect game systems to GUI presentation.

## Critical Warning Density

Files with highest concentration of critical edge cases:

1. **technologies_core.md**: 8 critical warnings (hidden by default, building levels, unresearch, AI categories, etc.)
2. **ideas_core.md**: 6 critical warnings (GFX prefix, history effects, civil war, modifiers, etc.)
3. **buildings.md**: 5 critical warnings (slots, railways, buildings.txt empty, spelling typo, etc.)
4. **balance_of_power.md**: 5 critical warnings (global sharing, duplicates, max boundary, decision category, etc.)
5. **ideologies.md**: 4 critical warnings (popularities sum, leaders, faction modifiers, AI peace)

These files require careful attention due to non-obvious behaviors that cause silent failures or crashes.


