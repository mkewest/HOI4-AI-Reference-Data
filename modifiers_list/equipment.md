---
domain: modifiers_list
concept: equipment
version: 1.14+
requires: [modifiers]
relates: [military_land, military_air, military_naval]
---

# Equipment Modifiers

For modifier system mechanics, types, application methods, and critical behavioral edge cases, see [Modifier System](/scripting/modifiers.md).

Equipment modifiers affect equipment statistics, upgrades, conversions, and idea costs.

## Equipment Stats

> [!CRITICAL] `breakthrough`, `armor_value`, and air equipment modifiers (`air_attack`, `air_defence`, `air_agility`, `maximum_speed`, `air_range`, `air_superiority`, `air_bombing`) MUST be used in their required equipment categories. `breakthrough` requires land equipment category. `armor_value` requires equipment category (not limited to land). Air modifiers require air equipment category. Equipment-specific modifiers fail silently if used outside their required category.

| Modifier | Type | Decimals | Description |
|----------|------|----------|-------------|
| `armor_value` | num | 0 | Armor value (Requires: equipment category) |
| `breakthrough` | num | 0 | Breakthrough value (Requires: land equipment category) |

## Equipment Management

| Modifier | Type | Decimals | Description |
|----------|------|----------|-------------|
| `equipment_conversion_speed` | num | 2 | Equipment conversion speed |
| `equipment_upgrade_xp_cost` | num | 2 | Equipment upgrade XP cost |

## Equipment Capture

Two types control equipment capture rates from combat:

**equipment_capture:** Flat addition to capture ratio (typically base 5%):
```hoi4
equipment_capture = 0.10  # +0.10 to capture ratio (0.05 becomes 0.15)
```

**equipment_capture_factor:** Percentual multiplication:
```hoi4
equipment_capture_factor = 0.50  # +50% to capture ratio (0.05 becomes 0.075)
```

Both can be used together: flat addition applies first, then percentual multiplication. Captured equipment respects tech level and can be used immediately.

| Modifier | Type | Decimals | Description |
|----------|------|----------|-------------|
| `equipment_capture` | num | 2 | Flat addition to equipment capture ratio |
| `equipment_capture_factor` | num | 2 | Percentual modifier to equipment capture ratio |

## Idea Costs

> [!CRITICAL] Cost modifiers require an idea or character of that category to exist in an EARLIER-EVALUATED file. Without a prerequisite idea/character, the cost modifier silently fails and does nothing. Load order determines what "earlier-evaluated" means - ensure prerequisite content loads first.

| Modifier | Type | Decimals | Description |
|----------|------|----------|-------------|
| `idea_cost_factor` | num | 2 | All idea costs modifier |
| `political_advisor_cost_factor` | num | 2 | Political advisor cost |
| `theorist_cost_factor` | num | 2 | Theorist cost |

For complete list of equipment-related modifiers including equipment-specific stats, see also [Military Land Modifiers](/modifiers_list/military_land.md), [Military Naval Modifiers](/modifiers_list/military_naval.md), and [Military Air Modifiers](/modifiers_list/military_air.md).

## Related Systems

For equipment definitions and archetypes, see [Equipment](/equipment/equipment.md).

For idea implementation, see [Ideas](/content/ideas.md).
