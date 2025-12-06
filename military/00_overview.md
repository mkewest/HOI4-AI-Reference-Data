---
domain: military
concept: overview
version: 1.14+
relates: [core, scripting, database, modifiers_list]
---

# Military Domain Structure

## Overview

The military domain contains 8 markdown files covering all aspects of military force organization, equipment systems, and industrial capabilities in Hearts of Iron IV. Files are organized by functional subsystem rather than strict technical hierarchy.

## File Structure

```text
/military/
├── oob.md                  - Organization of Battle loading system
├── division_template.md    - Division composition and naming
├── units.md                - Battalion and support company definitions
├── equipment.md            - Equipment archetypes and variants
├── air_wings.md            - Air force instantiation
├── navies.md               - Naval fleet organization
├── mios.md                 - Military-Industrial Organizations (NSB DLC)
└── intel_agencies.md       - Intelligence services (LaR DLC)
```

## File Descriptions

### oob.md (~900 tokens)

**Purpose**: Military force loading and initialization system  
**Covers**: File structure, loading mechanics, DLC handling, division instantiation, equipment assignment, production setup, load timing  
**Key relationships**: Entry point for military system - requires division_template, units, and equipment concepts  
**Critical edge cases**: Additive loading behavior (not replacement), explicit loading requirement (no auto-load), DLC conditional branching, equipment spawn behavior (not from reserves)

### division_template.md (~1400 tokens)

**Purpose**: Division composition and organization  
**Covers**: Template structure, regiment coordinate system, combat battalion groups, division naming (direct and ordered), template locking, combat width calculation, priority and obsolescence  
**Key relationships**: Requires units for battalion types; relates to oob and equipment  
**Critical edge cases**: Inverted Y-axis (0,0 at top-left), out-of-bounds coordinates fail silently, group mixing restrictions in columns, mutual exclusion of naming methods

### units.md (~2200 tokens)

**Purpose**: Battalion and support company definitions  
**Covers**: Unit definition structure, groups (implicit creation), type and categories, combat statistics, equipment requirements, unit speed (multiplicative), supply and organization, training and manpower, equipment bonuses, terrain modifiers, unit models and visuals, icons, availability  
**Key relationships**: Core concept required by division_template and equipment; relates to terrain systems  
**Critical edge cases**: Speed multiplier behavior, terrain modifiers REPLACE base stats, negative attack values as percentages, icon sprite requirements (all three types), group creation on first reference, equipment need blocks affecting availability

### equipment.md (~1300 tokens)

**Purpose**: Equipment archetype hierarchy and variant system  
**Covers**: Archetype hierarchy (inheritance), parent relationships (upgrade paths), equipment stats, variants, variant requirements by DLC, upgrade modules, production system, production efficiency, equipment behavior in OOB, factory assignment, categories, lend-lease and gifting  
**Key relationships**: Requires units for type matching; relates to units, oob, and mios  
**Critical edge cases**: Efficiency as 0-100 not 0.0-1.0, progress as single unit completion, variant name requirements by DLC (NSB/MTG/BBA mandatory), start_equipment_factor spawning from nothing, force_equipment_variants leaving empty slots, ship production efficiency factors having no effect

### air_wings.md (~500 tokens)

**Purpose**: Air force instantiation and organization  
**Covers**: Air wing structure, location requirements, equipment assignment, BBA variant requirement, amount and strength, experience, multiple wings per state, ownership and creator, air wing effects  
**Key relationships**: Requires equipment variants and states (for airbases); relates to oob  
**Critical edge cases**: State must have airbase or wing shows error, no validation on capacity vs wing size, BBA requires version_name for aircraft  
**Note**: Smallest file - focused concept with minimal complexity

### navies.md (~1200 tokens)

**Purpose**: Naval fleet organization and ship management  
**Covers**: Fleet structure (fleet/task force/ship hierarchy), MTG vs non-MTG equipment, ship definition, pride of the fleet, location and naval base, ship experience, equipment variants and creator, production efficiency (lack of), start equipment factor, task force organization  
**Key relationships**: Requires equipment variants; relates to oob  
**Critical edge cases**: MTG/non-MTG mutual exclusivity (mixing causes crash), MTG ships require version_name, pride of fleet limited to ONE per fleet globally (last-write-wins), ship production efficiency factors have no effect, equipment spawns from nothing

### mios.md (~2800 tokens)

**Purpose**: Military-Industrial Organizations system (NSB DLC)  
**Covers**: MIO definition structure, loading and timing, allowed condition, initial trait (special properties), trait system, trait grid coordinates, relative positioning, visibility and availability, equipment bonuses (trait vs policy differences), organization bonuses (global and additive), production bonuses, mutual exclusion, policy system, name resolution, include system  
**Key relationships**: Requires equipment types; relates to equipment  
**Critical edge cases**: Load only on new game (not mid-game), check error.log twice (menu access fires visibility), allowed evaluated at game start only, initial trait has no grid position, grid coordinates 10×5 with inverted Y-axis, relative positioning, mutual exclusion must be in ALL traits, trait equipment bonus vs policy equipment bonus differences, organization bonuses cannot be limited by equipment type, research bonus is additive not multiplicative  
**Note**: Largest file due to complex grid system, visibility mechanics, and bonus type variations

### intel_agencies.md (~800 tokens)

**Purpose**: Intelligence agency creation and upgrades (LaR DLC)  
**Covers**: Agency definition structure, icon system (two-frame split), agency names, name selection behavior, availability trigger, upgrade system, multiple default names, selection effect, AI behavior  
**Key relationships**: Requires none beyond base scripting; standalone system  
**Critical edge cases**: Icon frame split at exactly 117px with noOfFrames=2 required, names list only used without explicit name parameter, available controls icon selection not names list, icon-only definitions still need at least one name entry, selection effect not automatically generated

## Dependency Graph

```text
equipment.md
    ↓ (required by)
units.md
    ↓ (required by)
division_template.md
    ↓ (all required by)
oob.md

equipment.md → air_wings.md
equipment.md → navies.md

equipment.md + NSB_DLC → mios.md

LaR_DLC → intel_agencies.md
```

## Semantic Groupings

### Core Military Stack (interdependent chain)

- equipment.md: Equipment definitions and variants
- units.md: Battalion/company definitions using equipment
- division_template.md: Templates composed of units
- oob.md: Loading system that instantiates templates

These four files form the complete ground forces system and must be understood in order.

### Force Instantiation

- oob.md: Generic loading system
- air_wings.md: Air force-specific instantiation
- navies.md: Naval force-specific instantiation

Each handles different force types with unique organizational requirements.

### Industrial Systems

- equipment.md: Base equipment system
- mios.md: Industrial organization bonuses (NSB)

MIOs extend the equipment system with production and research bonuses.

### Special Systems

- intel_agencies.md: Standalone espionage system (LaR)

Intelligence agencies operate independently from military force systems.

## Token Distribution

| File | Token Count | Percentage |
|------|-------------|------------|
| mios.md | ~2800 | 27.7% |
| units.md | ~2200 | 21.8% |
| division_template.md | ~1400 | 13.9% |
| equipment.md | ~1300 | 12.9% |
| navies.md | ~1200 | 11.9% |
| oob.md | ~900 | 8.9% |
| intel_agencies.md | ~800 | 7.9% |
| air_wings.md | ~500 | 5.0% |
| **Total** | **~10,100** | **100%** |

Average: ~1,263 tokens per file

## Edge Case Integration

All edge cases from `military_EdgeCases.txt` have been integrated inline at their point of relevance:

- **Loading behavior**: Integrated into oob.md (additive operations, explicit loading, DLC splits, MIO timing)
- **Coordinate systems**: Integrated into division_template.md and mios.md (inverted Y-axis, max indices, out-of-bounds failures)
- **Division naming**: Integrated into division_template.md (mutual exclusivity, auto-selection logic)
- **Equipment behavior**: Integrated into equipment.md and oob.md (start factors, variant requirements, production values)
- **Variant requirements**: Integrated into equipment.md, air_wings.md, and navies.md (DLC-specific mandates)
- **Production efficiency**: Integrated into equipment.md (0-100 range, progress meaning, ship limitations)
- **Naval systems**: Integrated into navies.md (pride of fleet, MTG exclusivity, equipment type matching)
- **Air systems**: Integrated into air_wings.md (airbase requirement, capacity validation)
- **Template locking**: Integrated into division_template.md (requires is_locked, force_allow_recruiting)
- **Experience**: Integrated into oob.md, air_wings.md, navies.md (0.0-1.0 range, minimum level)
- **Officer portraits**: Integrated into oob.md (auto-generation, small suffix)
- **DLC file splitting**: Integrated into oob.md (if/else structure, NSB tank references)
- **MIO allowed timing**: Integrated into mios.md (game start evaluation, AI requirements)
- **MIO mutual exclusion**: Integrated into mios.md (all traits must define)
- **MIO bonuses**: Integrated into mios.md (trait vs policy differences, organization scope, additivity)
- **MIO name resolution**: Integrated into mios.md (fallback chains)
- **MIO initial trait**: Integrated into mios.md (no position, limited attributes)
- **MIO civil war visibility**: Integrated into mios.md (same coordinates, visible switching)
- **Unit icons**: Integrated into units.md (three sprite requirement, medium_white naming)
- **Unit groups**: Integrated into units.md (implicit creation)
- **Unit models**: Integrated into units.md (priority order, plurality display, clone inheritance)
- **Unit speed**: Integrated into units.md (multiplicative, transport override)
- **Unit equipment**: Integrated into units.md (need blocks, essential blocks)
- **Unit modifiers**: Integrated into units.md (terrain replacement, negative values, naval/air specifics)
- **Intel agency icons**: Integrated into intel_agencies.md (frame split, noOfFrames requirement)
- **Intel agency names**: Integrated into intel_agencies.md (selection behavior, minimum entry requirement)

No separate edge case files exist - all warnings and gotchas appear in context where modders encounter them.

## Usage Patterns

### For New Modders

Start with: equipment.md → units.md → division_template.md → oob.md sequence to understand how military forces are created.

### For OOB Creation

Primary files: oob.md, division_template.md, air_wings.md, navies.md for force composition.

### For Equipment Design

Focus on: equipment.md (archetypes and variants), units.md (battalion stats), mios.md (production bonuses).

### For DLC-Specific Content

- **NSB modders**: mios.md for industrial organizations, equipment.md for tank variants
- **MTG modders**: navies.md for ship hulls and fleet structure
- **BBA modders**: air_wings.md for aircraft variants
- **LaR modders**: intel_agencies.md for espionage systems

### For Balance Work

Key files: units.md (combat stats), equipment.md (equipment stats and costs), division_template.md (combat width).

## Critical Dependencies

Files that MUST be read together for complete understanding:

1. **equipment.md + units.md**: Equipment types and unit equipment needs are inseparable
2. **units.md + division_template.md**: Unit positioning and group restrictions require both
3. **oob.md + (division_template + air_wings + navies)**: Loading system and instantiation targets
4. **equipment.md + mios.md**: Equipment bonuses require understanding base equipment system

## DLC Requirements

Files with hard DLC dependencies:

- **mios.md**: Requires No Step Back (NSB) DLC
- **intel_agencies.md**: Requires La Résistance (LaR) DLC
- **navies.md**: MTG content section requires Man the Guns (MTG) DLC
- **air_wings.md**: BBA variant requirements need By Blood Alone (BBA) DLC

Base game modding only requires: oob.md, division_template.md, units.md, equipment.md.

## Version Notes

All files represent HOI4 1.14+ systems. Version-specific features noted inline:

- NSB features (MIOs, tank variants): Version 1.11+
- MTG features (ship hulls): Version 1.6+
- BBA features (aircraft variants): Version 1.12+
- LaR features (intelligence agencies): Version 1.9+

## File Maturity

All files represent stable HOI4 systems. The military domain is foundational and changes infrequently compared to content systems (events, focuses, decisions).

Edge case density is highest in:

1. mios.md (8 major edge case categories)
2. units.md (6 major edge case categories)
3. oob.md (4 major edge case categories)

These files require careful attention when modding due to complex behavior and silent failure modes.
