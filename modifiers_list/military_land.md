---
domain: modifiers_list
concept: military_land
version: 1.14+
requires: [modifiers]
relates: [division_template, units]
---

# Military Land Modifiers

For modifier system mechanics, types, application methods, and critical behavioral edge cases, see [Modifier System](/scripting/modifiers.md).

Military land modifiers affect land combat, divisions, training, special forces, and unit-specific stats.

## Land Combat and Units

```yaml
acclimatization_cold_climate_gain_factor:
  type: num
  decimals: 1

acclimatization_hot_climate_gain_factor:
  type: num
  decimals: 1

armor_value:
  type: num
  decimals: 2
  req: eq_category

army_attack_factor:
  type: num
  decimals: 2
  desc: Division Attack

army_core_attack_factor:
  type: num
  decimals: 2
  desc: Division Attack on core

army_core_defence_factor:
  type: num
  decimals: 2
  desc: Division Defense on core

army_defence_factor:
  type: num
  decimals: 2
  desc: Division Defense

army_morale:
  type: num
  decimals: 1
  desc: Division Recovery Rate

army_morale_factor:
  type: num
  decimals: 1

army_org:
  type: num
  decimals: 1
  desc: Division Organization

army_org_factor:
  type: num
  decimals: 1

army_org_regain:
  type: num
  decimals: 2
  desc: Army Organization Regain

army_speed_factor:
  type: num
  decimals: 2
  desc: Divisions speed

army_speed_factor_for_controller:
  type: num
  decimals: 2
  desc: Divisions speed
  scope: state

attack_bonus_against:
  type: num
  decimals: 1
  desc: Attack bonus against country

attack_bonus_against_cores:
  type: num
  decimals: 1
  desc: Attack on their core territory

attrition:
  type: num
  decimals: 1
  desc: Division Attrition

attrition_for_controller:
  type: num
  decimals: 1
  scope: state

breakthrough:
  type: num
  decimals: 2
  req: land_eq_category

breakthrough_bonus_against:
  type: num
  decimals: 1

breakthrough_factor:
  type: num
  decimals: 2

combat_width_factor:
  type: num
  decimals: 1
  desc: Own Combat Width

defence:
  type: num
  decimals: 2
  desc: Defense

defense_bonus_against:
  type: num
  decimals: 1

dig_in_speed:
  type: num
  decimals: 0

dig_in_speed_factor:
  type: num
  decimals: 1

dont_lose_dig_in_on_attack:
  type: bool
  desc: No Entrenchment Lose On Attack

extra_marine_supply_grace:
  type: num
  decimals: 1

extra_paratrooper_supply_grace:
  type: num
  decimals: 1

fortification_collateral_chance:
  type: num
  decimals: 1
  desc: Fort Combat Damage Chance

fortification_damage:
  type: num
  decimals: 1
  desc: Fort Damage from Combat

heat_attrition:
  type: num
  decimals: 1

heat_attrition_factor:
  type: num
  decimals: 2

land_night_attack:
  type: num
  decimals: 1

land_reinforce_rate:
  type: num
  decimals: 1

max_dig_in:
  type: num
  decimals: 1

max_dig_in_factor:
  type: num
  decimals: 1

max_planning:
  type: num
  decimals: 1

max_planning_factor:
  type: num
  decimals: 1

max_training:
  type: num
  decimals: 2

minimum_training_level:
  type: num
  decimals: 0

no_supply_grace:
  type: num
  decimals: 1
  desc: Supply Grace

offence:
  type: num
  decimals: 2
  desc: Attack

org_loss_when_moving:
  type: num
  decimals: 1

out_of_supply_factor:
  type: num
  decimals: 1

planning_speed:
  type: num
  decimals: 1

pocket_penalty:
  type: num
  decimals: 1
  desc: Encirclement penalty

recon_factor:
  type: num
  decimals: 1
  desc: Reconnaissance

recon_factor_while_entrenched:
  type: num
  decimals: 1
  desc: Recon Bonus While Entrenched

river_crossing_factor:
  type: num
  decimals: 2
  desc: River Crossing Speed Penalty

special_forces_cap:
  type: num
  decimals: 1
  desc: Special Forces Capacity Multiplier

special_forces_min:
  type: num
  decimals: 0
  desc: Special Forces Minimum Capacity

special_forces_no_supply_grace:
  type: num
  decimals: 1

special_forces_out_of_supply_factor:
  type: num
  decimals: 2

special_forces_training_time_factor:
  type: num
  decimals: 1

supply_consumption_factor:
  type: num
  decimals: 1

terrain_penalty_reduction:
  type: num
  decimals: 1

training_time_army:
  type: num
  decimals: 1
  desc: Division training time

training_time_army_factor:
  type: num
  decimals: 1

training_time_factor:
  type: num
  decimals: 2

unit_upkeep_attrition_factor:
  type: num
  decimals: 0

winter_attrition:
  type: num
  decimals: 1

winter_attrition_factor:
  type: num
  decimals: 2

```

## Special Forces Capacity

> [!CRITICAL] `special_forces_cap` is PERCENTUAL despite affecting slot count: `0.10 = +10% to special forces cap`, NOT +10 slots.

Two modifiers control special forces capacity:

- `special_forces_min`: Sets floor (minimum) capacity regardless of division count
- `special_forces_cap`: Multiplies % of regular divisions that can be special forces

Both can be active simultaneously. Game uses higher of the two values.

Individual contribution factors also exist:

```hoi4
paratroopers_special_forces_contribution_factor = 0.50  # +50% paratrooper cap contribution
marines_special_forces_contribution_factor = 0.50       # +50% marine cap contribution
```

These scale how much each special forces battalion counts toward the cap.

## Combat Width

> [!CRITICAL] `combat_width_factor` modifies YOUR combat width calculation. Negative values reduce your width (fit more divisions in battle). Does NOT affect enemy combat width. Affects width calculation before terrain modifiers apply.

## Entrenchment

> [!CRITICAL] `dont_lose_dig_in_on_attack` is a boolean - either prevents loss or doesn't. No partial values. Any value >0 treats as true. Does not affect entrenchment gain speed, only prevents loss when attacking.

Entrenchment modifiers:

- `max_dig_in`: Maximum entrenchment level
- `max_dig_in_factor`: Percentual modification to max entrenchment
- `dig_in_speed_factor`: Speed of gaining entrenchment
- `recon_factor_while_entrenched`: Bonus recon ONLY when entrenched (stacks with base recon)

## River Crossing

> [!CRITICAL] `river_crossing_factor` modifies PENALTY, not speed directly. Negative values reduce penalty (make crossing faster). Positive values increase penalty (make crossing slower). Does not affect combat while crossing, only time to cross.

## Minimum Training Level

> [!CRITICAL] `minimum_training_level` sets floor for deploying divisions. Does NOT affect training speed, only deployment threshold. Divisions below minimum cannot be deployed even if player tries.

## Fortification Damage

> [!CRITICAL] `fortification_damage` is flat damage to forts during combat. `fortification_collateral_chance` is chance for that damage to occur. Damage only applies during active combat, not while sieging. Fort must be attacked (not just present in state) for damage to apply.

## Recon While Entrenched

> [!CRITICAL] `recon_factor_while_entrenched` is bonus recon that ONLY applies when division is entrenched. Does NOT replace base `recon_factor`, stacks with it. Requires division to be dug in. `dig_in_speed` determines how quickly it applies.

## Related Systems

For division design, see [Divisions](/military/divisions.md).

For combat mechanics, see [Land Combat](/military/land_combat.md).

For training systems, see [Training](/military/training.md).
