---
domain: modifiers_list
concept: special_operations
version: 1.14+
requires: [modifiers]
relates: [redeployment, nuclear_weapons, exiled_forces]
---

# Special Operations Modifiers

For modifier system mechanics, types, application methods, and critical behavioral edge cases, see [Modifier System](/scripting/modifiers.md).

Special operations modifiers affect strategic redeployment, exiled divisions, and nuclear weapons.

## Special Operations

| Modifier | Type | Decimals | Description |
|----------|------|----------|-------------|
| `disable_strategic_redeployment` | bool | - |  |
| `disable_strategic_redeployment_for_controller` | bool | - | (Scope: state) |
| `exiled_divisions_attack_factor` | num | 2 |  |
| `exiled_divisions_defense_factor` | num | 2 |  |
| `nuclear_production` | bool | - | Allows Nuclear Bomb |
| `nuclear_production_factor` | num | 0 |  |
| `own_exiled_divisions_attack_factor` | num | 2 |  |
| `own_exiled_divisions_defense_factor` | num | 2 |  |

## Strategic Redeployment

Strategic redeployment allows fast movement of divisions across the map. The `disable_strategic_redeployment` boolean completely disables this ability.

State-specific control uses `disable_strategic_redeployment_for_controller` which applies only to the state's controller.

## Exiled Divisions

Exiled divisions are forces from occupied countries fighting alongside their host nation. Modifiers distinguish between:
- **Your exiled divisions** (divisions you host): `own_exiled_divisions_*`
- **Allied exiled divisions** (divisions others host): `exiled_divisions_*`

## Nuclear Weapons

Nuclear modifiers affect production and deployment of nuclear weapons. These are late-game strategic systems with significant gameplay impact.

## Related Systems

For strategic redeployment mechanics, see [Redeployment](/military/redeployment.md).

For nuclear weapon systems, see [Nuclear Weapons](/systems/nuclear.md).
