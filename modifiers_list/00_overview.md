---
domain: modifiers_list
concept: overview
version: 1.14+
requires: [modifiers]
relates: [ideas, dynamic_modifiers, static_modifiers]
---

# Modifiers List Overview

This domain provides complete enumeration of all available gameplay modifiers in Hearts of Iron IV 1.14+. For understanding how modifiers work, see [Modifier System](/scripting/modifiers.md).

> [!CRITICAL] Display precision shown in tables is for DISPLAY ONLY. All modifiers support up to 3 decimal places internally regardless of the displayed format. Display formatting does not limit actual precision in calculations.

## Organization

Modifiers are organized by functional domain:

**Military:**

- [Intelligence Modifiers](/modifiers_list/intelligence.md) - Intelligence agency, operatives, operations
- [Military Land Modifiers](/modifiers_list/military_land.md) - Land combat, training, special forces, unit types
- [Military Leaders Modifiers](/modifiers_list/military_leaders.md) - Land leaders, experience gain, command limits
- [Military Naval Modifiers](/modifiers_list/military_naval.md) - Naval combat, ships, leaders, production
- [Military Air Modifiers](/modifiers_list/military_air.md) - Air combat, missions, paradrops

**Political & Economic:**

- [Politics Ideology Modifiers](/modifiers_list/politics_ideology.md) - Politics, ideology, manpower, war justification
- [Economy Production Modifiers](/modifiers_list/economy_production.md) - Factories, construction, production, repair
- [Economy Resources Modifiers](/modifiers_list/economy_resources.md) - Resources, fuel, trade, lend-lease, licenses
- [Occupation Autonomy Modifiers](/modifiers_list/occupation_autonomy.md) - Occupation, resistance, autonomy, puppets

**Special Systems:**

- [State Modifiers](/modifiers_list/state_modifiers.md) - State-scoped modifiers, local effects
- [Equipment Modifiers](/modifiers_list/equipment.md) - Equipment stats, upgrades, capture, idea costs
- [Research Modifiers](/modifiers_list/research.md) - Research speed, doctrine costs
- [AI Modifiers](/modifiers_list/ai_modifiers.md) - AI behavior weights and priorities
- [Special Operations Modifiers](/modifiers_list/special_operations.md) - Strategic redeployment, exiled divisions, nuclear

## Pattern-Based Modifiers

Some categories use naming patterns to generate large modifier sets:

**Operation Modifiers** (Intelligence domain):

- Pattern: `operation_<name>_<param>`
- Parameters: `cost`, `outcome`, `risk` (all decimals: 2)
- Exception: `target_sabotage` uses `factor` instead of `outcome`
- See [Intelligence Modifiers](/modifiers_list/intelligence.md#operations)

**Mission-Specific Air Stats** (Air domain):

- Pattern: `air_<mission>_<stat>_factor`
- Missions: interception, air_superiority, close_air_support, strategic_bomber, naval_strike, paradrop
- Stats vary by mission (attack, defence, agility, detect, bombing, targetting, night_penalty)
- See [Military Air Modifiers](/modifiers_list/military_air.md#mission-specific-stats)

**Naval Ship Role Modifiers** (Naval domain):

- Pattern: `navy_<role>_<stat>_factor`
- Roles: submarine, screen, capital_ship, carrier_air
- Stats: attack, defence, detection (submarine only), targetting (carrier_air only), agility (carrier_air only)
- See [Military Naval Modifiers](/modifiers_list/military_naval.md#ship-role-modifiers)

**Unit Type Modifiers** (Land domain):

- Pattern: `<unit>_<stat>_factor`
- Generic pattern for unit-specific stat modifiers
- See [Military Land Modifiers](/modifiers_list/military_land.md#unit-type-modifiers)

**License Modifiers** (Resources domain):

- Two patterns: `license_<archetype>_purchase_cost` (broad category) and `license_<eq_type>_eq_cost_factor` (specific equipment)
- Specific overrides archetype if both present
- See [Economy Resources Modifiers](/modifiers_list/economy_resources.md#licenses)

## Version-Specific Features

**1.11+:**

- Doctrine cost modifiers: `land_doctrine_cost_factor`, `air_doctrine_cost_factor`, `naval_doctrine_cost_factor`
- These are percentual: -0.05 = 5% reduction, NOT -5

**1.13+:**

- Military Industrial Organization (MIO) modifiers
- Task capacity is FLAT (+2 means +2 slots), others are percentual

**1.15+:**

- Special project support modifiers

## Critical Scope Limitations

Different modifiers work in different scopes. Applying modifiers in wrong scopes causes silent failures.

**State-Only Modifiers:**

- All `local_*` modifiers (local_building_slots, local_factories, etc.)
- All `state_*` modifiers (state_production_speed_*, state_repair_speed_*, state_resource_*)
- Compliance and resistance modifiers
- `army_speed_factor_for_controller`, `attrition_for_controller`, `disable_strategic_redeployment_for_controller`

**Country-Only Modifiers:**

- `operative_death_on_capture_chance` (NOT operative scope)
- Most economy, politics, and research modifiers

**Unit Leader-Only Modifiers:**

- `terrain_penalty_reduction` (does NOT work in country scope despite appearing in ideas)

See individual category files for complete scope information per modifier.

## Common Patterns

**Gain vs Factor:**

- `<attribute>_gain`: Flat addition to daily/periodic change
- `<attribute>_factor`: Percentual modification to gain rate

**Own vs Enemy:**

- `own_<modifier>`: Affects YOUR units/operatives
- `enemy_<modifier>`: Affects ENEMY units/operatives

**Base vs Source-Specific:**

- `autonomy_gain`: Daily baseline autonomy progress
- `autonomy_gain_trade`, `autonomy_gain_warscore`: Source-specific additions
- `autonomy_gain_global_factor`: Multiplies ALL sources

**Experience Training vs Combat:**

- `experience_gain_<unit>_training_factor`: XP during training only
- `experience_gain_<unit>_combat_factor`: XP during combat only
- Independent multipliers, not shared pools

## Usage Notes

1. **Check scope validity** before using modifiers - wrong scope = silent failure
2. **Review edge cases** in category files for non-obvious behaviors
3. **Understand pattern-based modifiers** to avoid creating incorrect modifier names
4. **Verify version requirements** for newer modifiers (1.11+, 1.13+, 1.15+)
5. **Read behavioral documentation** in [Modifier System](/scripting/modifiers.md) for critical mechanics

## Cross-Domain References

Modifiers are referenced throughout the knowledge base:

- Military domain (MIOs): Organization modifiers, task capacity
- Equipment domain: Equipment capture modifiers
- Ideas domain: Idea slot modifiers, cost factors
- Character domain: Unit leader modifiers
- State domain: Compliance/resistance modifiers

Always verify modifier names against this list when using examples from other domains.
