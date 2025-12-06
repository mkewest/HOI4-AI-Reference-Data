---
domain: modifiers_list
concept: military_air
version: 1.14+
requires: [modifiers]
relates: [air_wings]
---

# Military Air Modifiers

For modifier system mechanics, types, application methods, and critical behavioral edge cases, see [Modifier System](/scripting/modifiers.md).

Military air modifiers affect aircraft stats, air missions, paradrops, and air-land interaction.

## Air Warfare

```yaml
air_accidents:
  type: num
  decimals: 1

air_accidents_factor:
  type: num
  decimals: 2

air_ace_generation_chance_factor:
  type: num
  decimals: 2

air_agility:
  type: num
  decimals: 0
  req: air_eq_category

air_agility_factor:
  type: num
  decimals: 2

air_attack:
  type: num
  decimals: 0
  req: air_eq_category

air_attack_factor:
  type: num
  decimals: 2

air_bombing:
  type: num
  decimals: 1
  desc: Ground Bombing
  req: air_eq_category

air_bombing_targetting:
  type: num
  decimals: 1

air_cas_efficiency:
  type: num
  decimals: 2
  desc: Air Support Mission Efficiency

air_cas_present_factor:
  type: num
  decimals: 2
  desc: Ground support

air_defence:
  type: num
  decimals: 0
  req: air_eq_category

air_defence_factor:
  type: num
  decimals: 2

air_detection:
  type: num
  decimals: 2

air_escort_efficiency:
  type: num
  decimals: 2

air_fuel_consumption_factor:
  type: num
  decimals: 2

air_intercept_efficiency:
  type: num
  decimals: 2

air_maximum_speed_factor:
  type: num
  decimals: 2

air_mission_efficiency:
  type: num
  decimals: 1

air_mission_xp_gain_factor:
  type: num
  decimals: 0

air_nav_efficiency:
  type: num
  decimals: 2
  desc: Naval Mission Efficiency

air_night_penalty:
  type: num
  decimals: 2
  desc: Night Operations Penalty

air_range:
  type: num
  decimals: 0
  req: air_eq_category

air_range_factor:
  type: num
  decimals: 2

air_superiority:
  type: num
  decimals: 1
  req: air_eq_category

air_superiority_bonus_in_combat:
  type: num
  decimals: 1

air_superiority_efficiency:
  type: num
  decimals: 2

air_training_xp_gain_factor:
  type: num
  decimals: 0

air_weather_penalty:
  type: num
  decimals: 2
  desc: Bad Weather Penalty

air_wing_xp_loss_when_killed_factor:
  type: num
  decimals: 0

army_bonus_air_superiority_factor:
  type: num
  decimals: 2
  desc: Air Superiority

cas_damage_reduction:
  type: num
  decimals: 1
  desc: Damage Reduction Against CAS

enemy_army_bonus_air_superiority_factor:
  type: num
  decimals: 2
  desc: Enemy Air Support

experience_gain_air:
  type: num
  decimals: 2

experience_gain_air_factor:
  type: num
  decimals: 1

ground_attack:
  type: num
  decimals: 2

ground_attack_factor:
  type: num
  decimals: 2

maximum_speed:
  type: num
  decimals: 0
  desc: Max Air Speed
  req: air_eq_category

mines_planting_by_air_factor:
  type: num
  decimals: 0

mines_sweeping_by_air_factor:
  type: num
  decimals: 0

mission_specific_stats:
  type: num
  decimals: 2

modifier_enemy_port_superiority_limit:
  type: num
  decimals: 0
  desc: Port strike enemy superiority limit

naval_strike_agility_factor:
  type: num
  decimals: 0
  desc: Naval Agility

naval_strike_attack_factor:
  type: num
  decimals: 0
  desc: Naval Bombing

naval_strike_targetting_factor:
  type: num
  decimals: 0
  desc: Naval Targeting

paradrop_organization_factor:
  type: num
  decimals: 1

paratrooper_aa_defense:
  type: num
  decimals: 1

paratrooper_count_per_plane:
  type: num
  decimals: 1

rocket_attack_factor:
  type: num
  decimals: 1
  desc: Rocket Damage

shore_bombardment_bonus:
  type: num
  decimals: 1

strategic_bomb_visibility:
  type: num
  decimals: 2

```

## Mission-Specific Air Stats

Air missions use pattern `air_<mission>_<stat>_factor` for mission-specific bonuses:

> [!CRITICAL] Mission-specific stats (e.g., `air_interception_attack_factor`) only apply during that specific mission type. Mission efficiency modifiers (e.g., `air_superiority_efficiency`) multiply with mission-specific stats for multiplicative benefit, not additive.

**Available patterns:**
- Interception: attack, defence, agility, detect
- Air superiority: attack, defence, agility, detect
- Close air support: attack, defence, agility
- Strategic bomber: attack, defence, agility, bombing, night_penalty
- Naval strike: attack, targetting, agility
- Paradrop: attack, defence, agility

**Paradrop Quirk:**
> [!CRITICAL] `air_paradrop_agility_factor` exists in localization and is recognized by the game, but does NOT actually do anything in game code. Only `air_paradrop_attack_factor` and `air_paradrop_defence_factor` are functional.

Examples:
```hoi4
air_interception_attack_factor = 0.15    # +15% attack during interception missions only
air_intercept_efficiency = 0.10          # +10% overall interception effectiveness
# These multiply together for total effect
```

## Shore Bombardment

> [!CRITICAL] `shore_bombardment_bonus` only applies during amphibious invasions. Requires naval units in sea zone with shore bombardment capability. Does NOT apply to regular land combat even with naval units present.

## Related Systems

For aircraft definitions, see [Aircraft](/equipment/aircraft.md).

For air mission mechanics, see [Air Missions](/military/air_missions.md).

For paradrop mechanics, see [Paradrops](/military/paradrops.md).
