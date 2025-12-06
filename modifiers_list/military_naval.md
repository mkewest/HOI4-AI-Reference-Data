---
domain: modifiers_list
concept: military_naval
version: 1.14+
requires: [modifiers]
relates: [navies]
---

# Military Naval Modifiers

For modifier system mechanics, types, application methods, and critical behavioral edge cases, see [Modifier System](/scripting/modifiers.md).

Military naval modifiers affect naval combat, ships, admirals, naval production, and amphibious invasions.

## Naval Warfare

```yaml
amphibious_invasion:
  type: num
  decimals: 1
  desc: Amphibious Invasion Speed

amphibious_invasion_defence:
  type: num
  decimals: 0

carrier_capacity_penalty_reduction:
  type: num
  decimals: 1
  desc: Carrier overcrowding

carrier_traffic:
  type: num
  decimals: 0

convoy_escort_efficiency:
  type: num
  decimals: 1

convoy_raiding_efficiency_factor:
  type: num
  decimals: 2

convoy_retreat_speed:
  type: num
  decimals: 0

critical_receive_chance:
  type: num
  decimals: 1
  desc: Chance to Receive Critical Hit

experience_gain_navy:
  type: num
  decimals: 2

experience_gain_navy_factor:
  type: num
  decimals: 1

experience_gain_navy_unit:
  type: num
  decimals: 1

experience_gain_navy_unit_factor:
  type: num
  decimals: 1
  desc: Ship Experience Gain

female_random_admiral_chance:
  type: num
  decimals: 0

fighter_sortie_efficiency:
  type: num
  decimals: 0

hull_costs:
  type: num
  decimals: 0

invasion_preparation:
  type: num
  decimals: 1
  desc: Invasion Preparation Time

mines_planting_by_fleets_factor:
  type: num
  decimals: 0

mines_sweeping_by_fleets_factor:
  type: num
  decimals: 0

naval_accidents_chance:
  type: num
  decimals: 2

naval_attrition:
  type: num
  decimals: 2
  desc: Attrition

naval_coordination:
  type: num
  decimals: 0
  desc: Fleet Coordination

naval_critical_effect_factor:
  type: num
  decimals: 2
  desc: Effects of sustained Critical Hits

naval_critical_score_chance_factor:
  type: num
  decimals: 2
  desc: Chance to score Critical Hit

naval_damage_factor:
  type: num
  decimals: 2
  desc: Damage

naval_defense_factor:
  type: num
  decimals: 2
  desc: Defense

naval_detection:
  type: num
  decimals: 0

naval_enemy_fleet_size_ratio_penalty_factor:
  type: num
  decimals: 2

naval_enemy_retreat_chance:
  type: num
  decimals: 2
  desc: Enemy retreat chance

naval_has_potf_in_combat_attack:
  type: num
  decimals: 2
  desc: Attack with Pride of the Fleet

naval_has_potf_in_combat_defense:
  type: num
  decimals: 2
  desc: Defense with Pride of the Fleet

naval_hit_chance:
  type: num
  decimals: 0

naval_invasion_capacity:
  type: num
  decimals: 0

naval_invasion_penalty:
  type: num
  decimals: 0

naval_invasion_prep_speed:
  type: num
  decimals: 1

naval_mine_hit_chance:
  type: num
  decimals: 2

naval_mines_damage_factor:
  type: num
  decimals: 0

naval_mines_effect_reduction:
  type: num
  decimals: 0
  desc: Naval mines avoidance

naval_morale:
  type: num
  decimals: 1
  desc: Ship Recovery Rate

naval_morale_factor:
  type: num
  decimals: 1

naval_retreat_chance:
  type: num
  decimals: 0
  desc: Retreat Decision Chance

naval_retreat_speed:
  type: num
  decimals: 0
  desc: Fleet speed while retreating

naval_speed_factor:
  type: num
  decimals: 0
  desc: Naval Speed

naval_strike:
  type: num
  decimals: 0

naval_torpedo_cooldown_factor:
  type: num
  decimals: 2

naval_torpedo_hit_chance_factor:
  type: num
  decimals: 2

naval_torpedo_reveal_chance_factor:
  type: num
  decimals: 2

naval_torpedo_screen_penetration_factor:
  type: num
  decimals: 2

navy_anti_air_attack:
  type: num
  decimals: 1

navy_anti_air_attack_factor:
  type: num
  decimals: 2

navy_casualty_on_hit:
  type: num
  decimals: 2
  desc: Casualties factor on hit

navy_casualty_on_sink:
  type: num
  decimals: 2
  desc: Casualties on sink

navy_fuel_consumption_factor:
  type: num
  decimals: 2

navy_leader_cost_factor:
  type: num
  decimals: 1

navy_leader_start_attack_level:
  type: num
  decimals: 0

navy_leader_start_coordination_level:
  type: num
  decimals: 0

navy_leader_start_defense_level:
  type: num
  decimals: 0

navy_leader_start_level:
  type: num
  decimals: 0

navy_leader_start_maneuvering_level:
  type: num
  decimals: 0

navy_max_range:
  type: num
  decimals: 2
  desc: Naval max range

navy_max_range_factor:
  type: num
  decimals: 2

navy_org:
  type: num
  decimals: 1
  desc: Navy Organization

navy_org_factor:
  type: num
  decimals: 1

navy_visibility:
  type: num
  decimals: 2
  desc: Visibility

port_strike:
  type: num
  decimals: 1

positioning:
  type: num
  decimals: 1

refit_ic_cost:
  type: num
  decimals: 0

refit_speed:
  type: num
  decimals: 0

repair_speed_factor:
  type: num
  decimals: 0
  desc: Ship Repair Speed

screening_efficiency:
  type: num
  decimals: 1

ship_role_modifiers:
  type: num
  decimals: 2

ships_at_battle_start:
  type: num
  decimals: 0
  desc: Number of ships in first contact

sortie_efficiency:
  type: num
  decimals: 0

spotting_chance:
  type: num
  decimals: 0
  desc: Spotting Chance

strike_force_movement_org_loss:
  type: num
  decimals: 2

sub_retreat_speed:
  type: num
  decimals: 0

submarine_attack:
  type: num
  decimals: 1

transport_capacity:
  type: num
  decimals: 2
  desc: Troop convoy requirements

```

## Naval Role Patterns

Ship role modifiers use pattern `navy_<role>_<stat>_factor`:

> [!CRITICAL] Naval role modifiers are ship-type specific. Carrier aircraft use `navy_carrier_air_*` not standard `air_*` modifiers. Naval detection affects both spotting AND being spotted (asymmetric).

**Available patterns:**
- Submarine: attack, defence, detection
- Screen: attack, defence  
- Capital ship: attack, defence
- Carrier air: attack, targetting, agility

Examples:
```hoi4
navy_submarine_attack_factor = 0.15       # +15% submarine attack
navy_carrier_air_targetting_factor = 0.10 # +10% carrier aircraft targeting
```

## Critical Hits

Three independent naval critical hit systems:

> [!CRITICAL] Naval critical hits use three separate systems:
> - `critical_receive_chance`: Chance to receive crits when hit
> - `naval_critical_score_chance_factor`: Chance to score crits when hitting
> - `naval_critical_effect_factor`: Damage/effects of crits already received
>
> All three are independent and multiply together for total critical hit impact.

## Retreat Chances

> [!CRITICAL] `naval_retreat_chance` is YOUR chance to retreat when conditions met. `naval_enemy_retreat_chance` is enemy's chance. These are separate systems - modifying one does not affect the other.

Retreat speed modifiers (`naval_retreat_speed`, `sub_retreat_speed`, `convoy_retreat_speed`) only apply AFTER retreat decision made. They don't affect the chance to retreat.

## Carrier Overcrowding

> [!CRITICAL] `carrier_capacity_penalty_reduction` reduces penalty from exceeding carrier capacity. Does NOT increase carrier capacity itself. Overcrowding penalties include: reduced stats, higher accident chance, slower operations.

## Pride of the Fleet

> [!CRITICAL] `naval_has_potf_in_combat_attack` and `naval_has_potf_in_combat_defense` only apply when fighting alongside ship designated as Pride of the Fleet. Does NOT apply to the PotF ship itself. Only one ship can be PotF at a time per country.

## Related Systems

For ship design, see [Ships](/equipment/ships.md).

For naval combat mechanics, see [Naval Combat](/military/naval_combat.md).

For admiral traits and skills, see [Admirals](/characters/admirals.md).

For naval invasion mechanics, see [Naval Invasions](/military/naval_invasion.md).
