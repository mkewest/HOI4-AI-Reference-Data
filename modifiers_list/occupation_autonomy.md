---
domain: modifiers_list
concept: occupation_autonomy
version: 1.14+
requires: [modifiers]
relates: [autonomy, states]
---

# Occupation Autonomy Modifiers

For modifier system mechanics, types, application methods, and critical behavioral edge cases, see [Modifier System](/scripting/modifiers.md).

Occupation autonomy modifiers affect occupied territories, resistance, compliance, puppet relationships, and exile governments.

## Occupation and Autonomy

```yaml
annex_cost_factor:
  type: num
  decimals: 1

autonomy_gain:
  type: num
  decimals: 1
  desc: Daily autonomy progress gain

autonomy_gain_global_factor:
  type: num
  decimals: 1
  desc: All autonomy gain

autonomy_gain_ll_to_overlord:
  type: num
  decimals: 2
  desc: Freedom gain by LL to overlord

autonomy_gain_ll_to_overlord_factor:
  type: num
  decimals: 2

autonomy_gain_ll_to_subject:
  type: num
  decimals: 2
  desc: Subject freedom from LL from overlord

autonomy_gain_ll_to_subject_factor:
  type: num
  decimals: 2

autonomy_gain_warscore:
  type: num
  decimals: 2
  desc: Freedom gain by war score

autonomy_manpower_share:
  type: num
  decimals: 2
  desc: Subject manpower requirement

can_master_build_for_us:
  type: bool

cic_to_overlord_factor:
  type: num
  decimals: 2
  desc: Civilian industry to overlord

cic_to_target_factor:
  type: num
  decimals: 2
  desc: Civilian industry to target

compliance_gain:
  type: num
  decimals: 3
  desc: Daily Compliance Gain
  scope: state

compliance_growth:
  type: num
  decimals: 0
  scope: state

compliance_growth_on_our_occupied_states:
  type: num
  decimals: 0
  desc: In our states occupied by enemy
  scope: state

exile_manpower_factor:
  type: num
  decimals: 2
  desc: Daily Exile Manpower

legitimacy_daily:
  type: num
  decimals: 2

legitimacy_gain_factor:
  type: num
  decimals: 0

license_subject_master_purchase_cost:
  type: num
  decimals: 2

master_build_autonomy_factor:
  type: bool
  desc: Autonomy from building

mic_to_overlord_factor:
  type: num
  decimals: 2
  desc: Military industry to overlord

mic_to_target_factor:
  type: num
  decimals: 2
  desc: Military industry to target

no_compliance_gain:
  type: bool

occupation_cost:
  type: num
  decimals: 2

puppet_cost_factor:
  type: num
  decimals: 1

required_garrison_factor:
  type: num
  decimals: 0
  desc: Required Garrisons
  scope: state

resistance_activity:
  type: num
  decimals: 1
  desc: Resistance Activity Chance
  scope: state

resistance_damage_to_garrison:
  type: num
  decimals: 2
  scope: state

resistance_damage_to_garrison_on_our_occupied_states:
  type: num
  decimals: 2
  scope: state

resistance_decay:
  type: num
  decimals: 0
  scope: state

resistance_decay_on_our_occupied_states:
  type: num
  decimals: 0
  scope: state

resistance_garrison_penetration_chance:
  type: num
  decimals: 2
  scope: state

resistance_growth:
  type: num
  decimals: 0
  scope: state

resistance_growth_on_our_occupied_states:
  type: num
  decimals: 0
  scope: state

resistance_target:
  type: num
  decimals: 0
  scope: state

resistance_target_on_our_occupied_states:
  type: num
  decimals: 0
  scope: state

starting_compliance:
  type: num
  decimals: 0

subjects_autonomy_gain:
  type: num
  decimals: 1
  desc: Master impact

targeted_legitimacy_daily:
  type: num
  decimals: 1

```

## Occupied State Modifiers

> [!CRITICAL] `*_on_our_occupied_states` modifiers only affect YOUR states when occupied by enemy. They do NOT affect enemy states you occupy. For bidirectional effects, use separate modifiers with different naming.

Examples:
```hoi4
compliance_growth_on_our_occupied_states = 0.15  # +15% compliance growth when ENEMY occupies YOUR states
# Does NOT affect states you occupy

required_garrison_factor = -0.10  # -10% garrison needed in states YOU control
# Applied to YOUR occupied territories
```

## Compliance vs Resistance

Compliance and resistance operate on opposing scales (0-100):

> [!CRITICAL] Compliance and resistance are opposing forces on the same scale. Higher compliance reduces resistance cap. `resistance_target` sets where resistance naturally trends toward. Garrison reduces resistance growth but doesn't directly increase compliance.

Key modifiers:
- `compliance_gain`: Rate of compliance increase
- `compliance_growth`: Multiplier for compliance gain rate
- `resistance_*`: Various resistance mechanics
- `required_garrison_factor`: Garrison force needed to suppress resistance

## Related Systems

For occupation mechanics, see [Occupation](/systems/occupation.md).

For autonomy and puppet systems, see [Autonomy](/diplomacy/autonomy.md).

For resistance mechanics, see [Resistance](/systems/resistance.md).
