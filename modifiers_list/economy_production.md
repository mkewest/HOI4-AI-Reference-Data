---
domain: modifiers_list
concept: economy_production
version: 1.14+
requires: [modifiers]
relates: []
---

# Economy Production Modifiers

For modifier system mechanics, types, application methods, and critical behavioral edge cases, see [Modifier System](/scripting/modifiers.md).

Economy production modifiers affect factory output, construction speed, repair rates, and consumer goods.

## Economy and Production

```yaml
building_construction:
  type: num
  decimals: 2

building_repair:
  type: num
  decimals: 2

civilian_factory_use:
  type: num
  decimals: 0

consumer_goods_factor:
  type: num
  decimals: 2
  desc: Consumer Goods Factories

conversion_cost_civ_to_mil_factor:
  type: num
  decimals: 2

conversion_cost_mil_to_civ_factor:
  type: num
  decimals: 2

dockyard_donations:
  type: num
  decimals: 0

global_building_slots:
  type: num
  decimals: 0
  desc: Max Factories in a State

global_building_slots_factor:
  type: num
  decimals: 0

industrial_capacity_dockyard:
  type: num
  decimals: 2

industrial_capacity_factory:
  type: num
  decimals: 2
  desc: Factory Output

industrial_factory_donations:
  type: num
  decimals: 0

industry_air_damage_factor:
  type: num
  decimals: 2
  desc: Factory Bomb Vulnerability

industry_free_repair_factor:
  type: num
  decimals: 2
  desc: Free repair

industry_repair_factor:
  type: num
  decimals: 2
  desc: Factory Repair Speed

line_change_production_efficiency_factor:
  type: num
  decimals: 2
  desc: Production Efficiency Retention

military_factory_donations:
  type: num
  decimals: 0

min_export:
  type: num
  decimals: 2
  desc: Resources to Market

production_factory_efficiency_gain_factor:
  type: num
  decimals: 2
  desc: Production Efficiency growth

production_factory_max_efficiency_factor:
  type: num
  decimals: 2
  desc: Production Efficiency Cap

production_factory_start_efficiency_factor:
  type: num
  decimals: 2
  desc: Production Efficiency Base

production_lack_of_resource_penalty_factor:
  type: num
  decimals: 2

production_speed_buildings_factor:
  type: num
  decimals: 2
  desc: Construction Speed

refit_ic_cost:
  type: num
  decimals: 0

refit_speed:
  type: num
  decimals: 0

static_anti_air_damage_factor:
  type: num
  decimals: 2

static_anti_air_hit_chance_factor:
  type: num
  decimals: 2

tech_air_damage_factor:
  type: num
  decimals: 2
  desc: Anti-Air Bombing Damage Reduction

```

## Production Efficiency

Four independent efficiency modifiers control different aspects:

> [!CRITICAL] Production efficiency modifiers are independent systems:
> - `production_factory_start_efficiency_factor`: Starting efficiency only (when production begins)
> - `production_factory_max_efficiency_factor`: Maximum achievable efficiency cap
> - `production_factory_efficiency_gain_factor`: Speed of gaining efficiency
> - `line_change_production_efficiency_factor`: Efficiency retained when changing production

All four can be modified separately. For example, high max efficiency with slow gain creates long ramp-up times.

## Consumer Goods

> [!CRITICAL] `consumer_goods_factor` uses MULTIPLICATION, not addition. Multiple instances compound: `0.5 + (-0.5) = (1+0.5)(1-0.5) = 0.75`, NOT `0`. This creates exponential scaling.

Example:
```hoi4
# Two ideas:
consumer_goods_factor = 0.5   # +50%
consumer_goods_factor = -0.5  # -50%
# Result: 1.5 × 0.5 = 0.75 (75% of base, not 0%)
```

## Conversion Costs

Conversion between factory types uses asymmetric modifiers:

> [!CRITICAL] `conversion_cost_civ_to_mil_factor` only affects converting civilian TO military factories. `conversion_cost_mil_to_civ_factor` only affects reverse direction. These are independent - reducing one doesn't affect the other.

Conversion preserves partial production progress differently than new construction.

## Related Systems

For factory mechanics and construction, see [Construction](/economy/construction.md).

For production lines and efficiency, see [Production](/economy/production.md).
