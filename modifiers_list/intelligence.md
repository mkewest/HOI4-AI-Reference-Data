---
domain: modifiers_list
concept: intelligence
version: 1.14+
requires: [modifiers]
relates: [intel_agencies, special_operations]
---

# Intelligence Modifiers

For modifier system mechanics, types, application methods, and critical behavioral edge cases, see [Modifier System](/scripting/modifiers.md).

Intelligence modifiers affect the intelligence agency, operatives, operations, and cryptology systems.

## Agency Basics

| Modifier | Type | Decimals | Description |
|----------|------|----------|-------------|
| `agency_upgrade_time` | num | 2 | Intelligence agency upgrade time |
| `civilian_intel_factor` | num | 2 | Civilian Intelligence |
| `army_intel_factor` | num | 2 | Army Intelligence |
| `navy_intel_factor` | num | 2 | Navy Intelligence |
| `airforce_intel_factor` | num | 2 | Air Intelligence |
| `crypto_department_enabled` | bool | - | Enables cryptology department |
| `crypto_strength` | num | 0 | Cryptology Level |
| `decryption_power` | num | 0 | Decryption power |
| `decryption_power_factor` | num | 2 | Decryption power modifier |

## Decryption Bonuses

> [!CRITICAL] Decryption bonuses only apply when you've successfully decrypted that branch's ciphers. Decryption power determines success chance, bonus determines benefit if successful. Each branch (civilian/army/navy/airforce) is independent.

| Modifier | Type | Decimals | Description |
|----------|------|----------|-------------|
| `civilian_intel_decryption_bonus` | num | 0 | Decrypted Civilian Cipher Bonus |
| `army_intel_decryption_bonus` | num | 0 | Army cipher decryption bonus |
| `navy_intel_decryption_bonus` | num | 0 | Navy cipher decryption bonus |
| `airforce_intel_decryption_bonus` | num | 0 | Airforce cipher decryption bonus |

## Operatives

> [!CRITICAL] `operative_death_on_capture_chance` only works in country scope, NOT operative scope. Applying it in operative scope has no effect.

| Modifier | Type | Decimals | Description |
|----------|------|----------|-------------|
| `operative_slot` | num | 0 | Operative slots |
| `new_operative_slot_bonus` | num | 0 | Operative recruitment choices |
| `female_random_operative_chance` | num | 0 | Added Female Operative Chance |
| `commando_trait_chance_factor` | num | 0 | Chance of recruiting Commando trait |
| `enemy_operative_recruitment_chance` | num | 2 | Enemy operative recruitment chance |
| `occupied_operative_recruitment_chance` | num | 2 | Occupied territory operative recruitment |
| `operative_death_on_capture_chance` | num | 2 | Operative death chance on capture (country scope only) |

## Intel Network

| Modifier | Type | Decimals | Description |
|----------|------|----------|-------------|
| `intel_network_gain` | num | 2 | Intel network gain rate |
| `intel_network_gain_factor` | num | 2 | Intel network gain modifier |
| `intel_from_operatives_factor` | num | 2 | Intelligence from Operatives and Infiltrated Assets |
| `intelligence_agency_defense` | num | 2 | Counter intelligence |
| `defense_impact_on_blueprint_stealing` | num | 1 | Enemy Counter Intel impact on Steal Blueprints |

## Missions

> [!CRITICAL] See AI_focuses#Modding for AI focus modifier implementation details. AI focus modifiers don't directly change AI behavior - they adjust weights in AI decision-making. Multiple focus modifiers can stack and compete.

| Modifier | Type | Decimals | Description |
|----------|------|----------|-------------|
| `boost_ideology_mission_factor` | num | 2 | Boost ideology mission effectiveness |
| `control_trade_mission_factor` | num | 2 | Control trade mission effectiveness |
| `propaganda_mission_factor` | num | 2 | Propaganda mission effectiveness |
| `diplomatic_pressure_mission_factor` | num | 2 | Diplomatic pressure effectiveness |
| `boost_resistance_factor` | num | 2 | Strengthen Resistance efficiency |
| `root_out_resistance_effectiveness_factor` | num | 2 | Root out resistance effectiveness |

## Operations

Operations use the pattern `operation_<n>_<param>` where parameters are `cost`, `outcome`, and `risk` (all decimals: 2).

> [!CRITICAL] The `target_sabotage` operation uses `factor` instead of `outcome` in the middle parameter (inconsistent naming). All operations take decimals: 2 format.

Available operations for pattern generation:

- `operation` (generic)
- `fake_intel`
- `rescue_operative`
- `make_resistance_contacts`
- `boost_resistance`
- `collaboration_government`
- `coup_government`
- `capture_cipher`
- `coordinated_strike`
- `infiltrate` (plus branch-specific: `_armed_forces_army`, `_armed_forces_navy`, `_armed_forces_airforce`, `_civilian`)
- `steal_tech` (plus branch-specific: `_army`, `_navy`, `_airforce`, `_civilian`)
- `target_sabotage` (uses `_factor` not `_outcome`)
- `targeted_sabotage_industry`
- `targeted_sabotage_infrastructure`
- `targeted_sabotage_resources`

Example modifiers:

```hoi4
operation_infiltrate_cost = -0.15        # -15% infiltrate operation cost
operation_steal_tech_outcome = 0.20      # +20% steal tech effectiveness
operation_coup_government_risk = -0.10   # -10% coup risk
operation_target_sabotage_factor = 0.25  # NOTE: uses 'factor' not 'outcome'
```

## Related Systems

For operative mechanics and operations details, see [Intelligence Agency](/systems/intelligence_agency.md).

For dynamic modifiers using variable-based operation costs, see [Modifier System](/scripting/modifiers.md#dynamic-modifiers).
