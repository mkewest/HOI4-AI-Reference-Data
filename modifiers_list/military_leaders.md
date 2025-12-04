---
domain: modifiers_list
concept: military_leaders
version: 1.14+
requires: [modifiers]
relates: [leaders, traits, command, experience]
---

# Military Leaders Modifiers

For modifier system mechanics, types, application methods, and critical behavioral edge cases, see [Modifier System](/scripting/modifiers.md).

Military leaders modifiers affect land-based commanders and field marshals, including generation, promotion, skills, and experience.

## Land Leaders and Experience

```yaml
army_leader_cost_factor:
  type: num
  decimals: 1

army_leader_start_attack_level:
  type: num
  decimals: 0

army_leader_start_defense_level:
  type: num
  decimals: 0

army_leader_start_level:
  type: num
  decimals: 0

army_leader_start_logistics_level:
  type: num
  decimals: 0

army_leader_start_planning_level:
  type: num
  decimals: 0

cannot_use_abilities:
  type: bool
  desc: Cannot Use Combat Abilities

experience_gain_army:
  type: num
  decimals: 2

experience_gain_army_factor:
  type: num
  decimals: 1

experience_gain_army_unit:
  type: num
  decimals: 1
  desc: Division Experience Gain

experience_gain_army_unit_factor:
  type: num
  decimals: 1

experience_gain_factor:
  type: num
  decimals: 1
  desc: Leader Experience Gain

experience_loss_factor:
  type: num
  decimals: 1
  desc: Experienced soldier losses

female_random_army_leader_chance:
  type: num
  decimals: 0

max_commander_army_group_size:
  type: num
  decimals: 0

max_commander_army_size:
  type: num
  decimals: 0
  desc: General Max Army Size

max_marshal_army_group_size:
  type: num
  decimals: 0

max_marshal_army_size:
  type: num
  decimals: 0
  desc: Field Marshal Max Army Size

military_leader_cost_factor:
  type: num
  decimals: 1

promote_cost_factor:
  type: num
  decimals: 1

reassignment_duration_factor:
  type: num
  decimals: 1

sickness_chance:
  type: num
  decimals: 2

skill_bonus_factor:
  type: num
  decimals: 1
  desc: Leader Skill Bonuses

wounded_chance_factor:
  type: num
  decimals: 2

```

## Leader Start Levels

> [!CRITICAL] When both `army_leader_start_level` (total skill) and specific skill modifiers (`army_leader_start_attack_level`, etc.) are used, specific skills are set first, then remaining points distributed. Total level from specific skills can exceed start_level (specific takes priority).

For example:
```hoi4
army_leader_start_level = 3
army_leader_start_attack_level = 2
army_leader_start_defense_level = 2
# Result: Leader has attack=2, defense=2, remaining skills distributed to reach level 3 total
# If specific skills exceed 3, they take priority
```

## Experience Gain Patterns

Experience gain modifiers distinguish between training and combat:

> [!CRITICAL] `experience_gain_<unit>_training_factor` affects XP during training ONLY. `experience_gain_<unit>_combat_factor` affects XP during combat ONLY. These are independent multipliers, not shared pools.

Examples:
```hoi4
experience_gain_army_unit_factor = 0.25        # +25% to division XP gain (both training and combat)
experience_gain_army_training_factor = 0.50    # +50% to XP during training only
experience_gain_army_combat_factor = 0.50      # +50% to XP during combat only
```

## Health and Casualties

Two independent systems affect leader health:

**wounded_chance_factor:** Applies only during combat when taking casualties. Roll occurs when units under command take losses.

**sickness_chance:** Applies continuously over time regardless of combat. Passive roll that can occur even during peace.

These are independent rolls - both can occur simultaneously.

## Related Systems

For unit leader trait definitions, see [Traits](/characters/traits.md).

For experience mechanics, see [Experience System](/military/experience.md).
