---
domain: modifiers_list
concept: economy_resources
version: 1.14+
requires: [modifiers]
relates: [resources]
---

# Economy Resources Modifiers

For modifier system mechanics, types, application methods, and critical behavioral edge cases, see [Modifier System](/scripting/modifiers.md).

Economy resources modifiers affect resource extraction, fuel production, trade, lend-lease, and equipment licensing.

## Resources and Trade

```yaml
air_fuel_consumption_factor:
  type: num
  decimals: 2

archetype_license:
  type: num
  decimals: 0

army_fuel_capacity_factor:
  type: num
  decimals: 2

army_fuel_consumption_factor:
  type: num
  decimals: 2

autonomy_gain_trade:
  type: num
  decimals: 2
  desc: Freedom gain by trade

autonomy_gain_trade_factor:
  type: num
  decimals: 2

base_fuel_gain:
  type: num
  decimals: 2

base_fuel_gain_factor:
  type: num
  decimals: 2

country_resource:
  type: num
  decimals: 0

country_resource_cost:
  type: num
  decimals: 0
  desc: <Resource> Consumption

equipment_license:
  type: num
  decimals: 0

extra_trade_to_overlord_factor:
  type: num
  decimals: 2

extra_trade_to_target_factor:
  type: num
  decimals: 2

faction_trade_opinion_factor:
  type: num
  decimals: 2

fuel_cost:
  type: num
  decimals: 0

fuel_gain:
  type: num
  decimals: 0
  desc: Fuel Gain per Oil

fuel_gain_factor:
  type: num
  decimals: 2

fuel_gain_factor_from_states:
  type: num
  decimals: 2

fuel_gain_from_states:
  type: num
  decimals: 2
  desc: Fuel Gain from Refineries

lend_lease_tension:
  type: num
  decimals: 1

license_production_speed:
  type: num
  decimals: 0

license_purchase_cost:
  type: num
  decimals: 0

license_tech_difference_speed:
  type: num
  decimals: 0
  desc: License production speed from tech difference

max_fuel:
  type: num
  decimals: 2
  desc: Fuel Capacity (K)

max_fuel_building:
  type: num
  decimals: 2
  desc: Fuel Capacity (K)

max_fuel_factor:
  type: num
  decimals: 2

navy_fuel_consumption_factor:
  type: num
  decimals: 2

overlord_trade_cost_factor:
  type: num
  decimals: 2

production_oil_factor:
  type: num
  decimals: 0
  desc: Synthetic Oil

state_resource:
  type: num
  decimals: 0
  scope: state

state_resource_cost:
  type: num
  decimals: 0
  desc: <Resource> Consumption
  scope: state

state_resources_factor:
  type: num
  decimals: 0
  desc: Local Available Resources
  scope: state

temporary_state_resource:
  type: num
  decimals: 0
  scope: state

trade_cost_for_target_factor:
  type: num
  decimals: 2
  desc: Target country trade cost

trade_opinion_factor:
  type: num
  decimals: 2

```

## Fuel Capacity and Gain

> [!CRITICAL] `max_fuel` displays as "(K)" meaning thousands. `max_fuel_building` also displays as thousands. `base_fuel_gain` affects fuel from all sources. `fuel_gain_from_states` affects ONLY refineries, not base production.

Examples:

```hoi4
max_fuel = 50         # +50,000 fuel capacity (displayed as "50K")
base_fuel_gain = 0.10  # +10% fuel gain from all sources
fuel_gain_from_states = 0.10  # +10% fuel from refineries only
```

## Resource Modifiers

Three types control resource availability:

**state_resource_<resource>:** Adds resource to specific state (permanent)

**temporary_state_resource_<resource>:** Adds temporarily (removed when modifier expires)

**country_resource_<resource>:** Adds to national stockpile regardless of location

Resource consumption modifiers:

- `state_resource_cost_<resource>`: Changes consumption rate for state
- `country_resource_cost_<resource>`: Changes national consumption rate

## License Patterns

> [!CRITICAL] License modifiers use two patterns:
>
> - `license_<archetype>_purchase_cost`: Broad category (infantry, naval, air, armor)
> - `license_<eq_type>_eq_cost_factor`: Specific equipment type (infantry_eq, artillery_eq, etc.)
>
> Specific overrides archetype if both present. `license_tech_difference_speed` affects ALL license production, not per-type.

Examples:

```hoi4
license_infantry_purchase_cost = -0.10     # -10% all infantry equipment licenses
license_infantry_eq_cost_factor = -0.15    # -15% infantry_equipment specifically (overrides above)
license_tech_difference_speed = 0.25       # +25% production speed for all licensed equipment
```

## Autonomy Gain Sources

> [!CRITICAL] Autonomy gain uses layered system:
>
> - `autonomy_gain`: Daily baseline autonomy progress
> - `autonomy_gain_trade`, `autonomy_gain_warscore`, `autonomy_gain_ll_*`: Source-specific additions
> - `autonomy_gain_global_factor`: Multiplies ALL autonomy gain regardless of source
> - Source-specific factors (e.g., `autonomy_gain_trade_factor`) only multiply that specific source

Example calculation:

```hoi4
# Base gains
autonomy_gain = 0.5
autonomy_gain_trade = 0.2
# Modifiers
autonomy_gain_trade_factor = 0.50  # +50% to trade only
autonomy_gain_global_factor = 0.25  # +25% to everything
# Result: (0.5 + (0.2 × 1.5)) × 1.25 = 1.0 autonomy per day
```

## Related Systems

For resource mechanics, see [Resources](/economy/resources.md).

For fuel system details, see [Fuel](/military/fuel.md).

For trade and convoys, see [Trade](/economy/trade.md).
