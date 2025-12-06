---
domain: military
concept: navies
version: 1.14+
requires: [equipment]
relates: [oob]
---

# Navies

Navies define the organization of naval forces into fleets, task forces, and individual ships. The system differs significantly between MTG (Man the Guns) and non-MTG configurations.

## Fleet Structure

Navies are defined in the `units` block of OOB files using a hierarchical structure:

```hoi4
units = {
    fleet = {
        name = "High Seas Fleet"
        naval_base = 3458  # Province ID
        
        task_force = {
            name = "1st Battle Squadron"
            location = 3458
            
            ship = { name = "Bismarck" definition = battleship equipment = { ship_hull_heavy_1 = { amount = 1 owner = "GER" } } }
            ship = { name = "Tirpitz" definition = battleship }
        }
        
        task_force = {
            name = "Destroyer Flotilla"
            location = 3458
            
            ship = { name = "Z1" definition = destroyer }
            ship = { name = "Z2" definition = destroyer }
        }
    }
}
```

Fleets contain task forces, and task forces contain ships. The three-level hierarchy enables tactical organization and command structures.

## MTG vs Non-MTG Equipment

### Man the Guns (MTG)

With MTG, ships use modular hull-based equipment:

```hoi4
ship = {
    name = "Bismarck"
    definition = battleship
    equipment = {
        ship_hull_heavy_1 = {
            amount = 1
            owner = "GER"
            version_name = "Bismarck Class"
        }
    }
    start_experience_factor = 0.5
}
```

> [!CRITICAL] MTG ships REQUIRE `version_name`. Ships cannot spawn without a valid variant registered in country history. Missing variants cause the ship to fail spawning entirely.

### Non-MTG (Legacy)

Without MTG, ships use direct equipment types:

```hoi4
ship = {
    name = "Bismarck"
    definition = battleship
    equipment = {
        battleship_1 = {
            amount = 1
            owner = "GER"
        }
    }
}
```

Non-MTG equipment does not require `version_name` - the game uses base archetypes if unspecified.

> [!CRITICAL] MTG and non-MTG equipment types are mutually exclusive. Mixing `ship_hull_heavy_1` with `battleship_1` causes load failure. Equipment type must match the country's DLC status - MTG equipment on a non-MTG country causes crash.

## Ship Definition

The `definition` attribute references ship types defined in `common/units/equipment/ships.txt`:

```hoi4
ship = {
    name = "Bismarck"
    definition = battleship
}
```

Common definitions include:

- `battleship` - Capital ships
- `battle_cruiser` - Fast battleships
- `heavy_cruiser` - Heavy cruisers
- `light_cruiser` - Light cruisers
- `destroyer` - Destroyers
- `submarine` - Submarines
- `carrier` - Aircraft carriers

Each definition determines the ship's role, stats, and available modules (MTG only).

## Pride of the Fleet

Ships can be designated as Pride of the Fleet:

```hoi4
ship = {
    name = "Bismarck"
    definition = battleship
    pride_of_the_fleet = yes
}
```

> [!CRITICAL] Pride of the Fleet is limited to ONE ship per fleet globally, not per task force or per fleet. Designating a second ship with `pride_of_the_fleet = yes` causes the first ship to lose Pride status (last-write-wins behavior).

Pride status is per-fleet, meaning you can have multiple Pride ships across different fleets, but only one Pride ship within any single fleet.

Pride ships receive combat bonuses and special national spirit effects when sunk.

## Location and Naval Base

Fleets spawn at a `naval_base` province ID:

```hoi4
fleet = {
    name = "High Seas Fleet"
    naval_base = 3458  # Province ID with naval base
}
```

Task forces within the fleet have a `location` attribute that should match or be near the fleet's naval base. Ships spawn at the task force location.

If the specified province lacks a naval base, the fleet spawns but cannot deploy or move.

## Ship Experience

Ships can spawn with experience:

```hoi4
ship = {
    name = "Bismarck"
    definition = battleship
    start_experience_factor = 0.5
}
```

The `start_experience_factor` uses float values 0.0-1.0, corresponding to experience level boundaries defined in `UNIT_EXP_LEVELS`. Factor 0.0 gives "Green" experience (minimum level), not zero experience.

## Equipment Variants and Creator

Ships support the same variant system as other equipment:

```hoi4
equipment = {
    ship_hull_heavy_1 = {
        amount = 1
        owner = "GER"
        creator = "GER"
        version_name = "Bismarck Class"
    }
}
```

If the owner lacks ship technology but the creator has it, the ship uses the creator's technology level BUT the owner receives and can deploy the ship. This enables gifting advanced ships to less developed nations.

## Production Efficiency

Ships do NOT have `production_efficiency_cap_factor` or `production_efficiency_gain_factor` effects. These production bonuses, which work for land equipment and aircraft, have no effect on naval equipment.

Attempting to modify ship production efficiency through these factors does nothing - the game ignores them for naval equipment types.

## Start Equipment Factor

When spawning ships through OOB files:

```hoi4
ship = {
    name = "Bismarck"
    definition = battleship
    start_equipment_factor = 0.8
}
```

The `start_equipment_factor` does NOT subtract from country reserves. Ships spawn with equipment "out of thin air" at the specified percentage. This is consistent with other military units but particularly relevant for expensive naval equipment.

## Task Force Organization

Task forces can be organized by role:

```hoi4
task_force = {
    name = "1st Battle Squadron"
    location = 3458
    
    # Capital ships
    ship = { name = "Bismarck" definition = battleship }
    ship = { name = "Tirpitz" definition = battleship }
}

task_force = {
    name = "Destroyer Screen"
    location = 3458
    
    # Screening ships
    ship = { name = "Z1" definition = destroyer }
    ship = { name = "Z2" definition = destroyer }
    ship = { name = "Z3" definition = destroyer }
}
```

Task force composition affects combat performance and AI behavior. Properly organized fleets with screens and capital ships perform better than mixed compositions.

## Related Systems

See [Equipment](/military/equipment.md) for ship equipment definitions and variant requirements.  
See [OOB Files](/military/oob.md) for initial fleet setup and loading mechanics.
