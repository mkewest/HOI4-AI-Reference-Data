---
domain: modifiers_list
concept: state_modifiers
version: 1.14+
requires: [modifiers]
relates: [states]
---

# State Modifiers

For modifier system mechanics, types, application methods, and critical behavioral edge cases, see [Modifier System](/scripting/modifiers.md).

State modifiers apply only to specific states, providing localized effects. These are distinct from country-scoped modifiers.

> [!CRITICAL] State modifiers can ONLY be applied to states. Using state modifiers at country scope has no effect. Similarly, using country modifiers at state scope fails silently.

## State-Only Modifiers

All `local_*` and `state_*` prefixed modifiers are state-scoped. Additionally:
- `army_speed_factor_for_controller`
- `attrition_for_controller`
- `disable_strategic_redeployment_for_controller`
- `required_garrison_factor`
- All compliance and resistance modifiers

## State-Scoped Modifiers

| Modifier | Type | Decimals | Description |
|----------|------|----------|-------------|
| `local_building_slots` | num | 0 | Max Factories in State (Scope: state) |
| `local_building_slots_factor` | num | 0 | (Scope: state) |
| `local_factories` | num | 0 | (Scope: state) |
| `local_factory_sabotage` | num | 0 | Chance to Sabotage Constructions (Scope: state) |
| `local_intel_to_enemies` | num | 0 | (Scope: state) |
| `local_manpower` | num | 0 | (Scope: state) |
| `local_non_core_manpower` | num | 2 | (Scope: state) |
| `local_org_regain` | num | 2 | (Scope: state) |
| `local_resources` | num | 0 | (Scope: state) |
| `local_resources_factor` | num | 2 | Resource Gain Efficiency |
| `local_supplies` | num | 0 | (Scope: state) |
| `local_supplies_for_controller` | num | 0 | (Scope: state) |
| `state_building_construction` | num | 2 | (Scope: state) |
| `state_building_repair` | num | 2 | (Scope: state) |
| `state_production_speed_buildings_factor` | num | 0 | Local Construction Speed (Scope: state) |

## Local vs Global

State modifiers use "local_" prefix to distinguish from country-wide equivalents:

- `global_building_slots`: Flat addition to max factories per state (country-wide)
- `global_building_slots_factor`: Percentage modification (country-wide)
- `local_building_slots`: Flat addition (state-specific)
- `local_building_slots_factor`: Percentage (state-specific)

Local modifiers override global for that specific state (not additive).

## Controller-Specific Modifiers

Modifiers ending in `_for_controller` affect the state's controller specifically:
- `army_speed_factor_for_controller`: Movement speed bonus/penalty in this state
- `attrition_for_controller`: Attrition rate for controlling nation's forces
- `disable_strategic_redeployment_for_controller`: Blocks redeployment for controller

These are useful for representing difficult terrain or occupation costs that affect the occupier specifically.

## Related Systems

For state definitions and mechanics, see [States](/map/states.md).

For building construction in states, see [Construction](/economy/construction.md).

For occupation and compliance systems, see [Occupation Autonomy Modifiers](/modifiers_list/occupation_autonomy.md).
