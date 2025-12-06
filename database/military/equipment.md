---
domain: military
concept: equipment
version: 1.14+
requires: [units]
relates: [units, oob, mios]
---

# Equipment System

Equipment represents weapons, vehicles, and gear used by military units. The system uses an archetype hierarchy where specific equipment types inherit from base archetypes, with variants allowing customization per nation.

## Archetype Hierarchy

Equipment is organized in parent-child relationships:

```hoi4
equipments = {
    infantry_equipment = {
        is_archetype = yes
        is_buildable = no
        type = infantry
        group_by = archetype
        
        interface_category = interface_category_land
        
        # Base stats all infantry equipment shares
        reliability = 0.8
    }
    
    infantry_equipment_1 = {
        archetype = infantry_equipment
        parent = infantry_equipment_0
        is_buildable = yes
        
        priority = 10
        
        # Specific stats for this tech level
        defense = 10
        breakthrough = 2
        
        build_cost_ic = 0.5
        resources = {
            steel = 1
        }
    }
}
```

Archetypes marked `is_archetype = yes` serve as templates and cannot be built. Buildable equipment inherits from archetypes and defines actual production items.

## Parent Relationships

The `parent` attribute creates upgrade paths:

```hoi4
infantry_equipment_1 = {
    archetype = infantry_equipment
    parent = infantry_equipment_0
}

infantry_equipment_2 = {
    archetype = infantry_equipment
    parent = infantry_equipment_1
}
```

This creates the chain: `infantry_equipment_0` → `infantry_equipment_1` → `infantry_equipment_2`

Parent relationships enable:

- Upgrade buttons in production screen
- Technology unlock progression
- Equipment conversion mechanics

## Equipment Stats

Common equipment attributes:

```hoi4
build_cost_ic = 10.5
manpower = 2
fuel_consumption = 1.2

reliability = 0.9
maximum_speed = 5.0

soft_attack = 15
hard_attack = 8
air_attack = 4
defense = 6
breakthrough = 10
armor_value = 20
piercing = 12

resources = {
    steel = 2
    tungsten = 1
}
```

Stats are combined with unit base stats (see [Units](/military/units.md)) to determine final combat values. Equipment stats typically dominate for specialized units (tanks, ships, aircraft) while unit stats dominate for infantry.

## Equipment Variants

Variants allow nations to customize equipment with upgrades:

```hoi4
create_equipment_variant = {
    name = "Panzer IV Ausf. G"
    type = medium_tank_equipment_2
    parent_version = 0
    
    upgrades = {
        tank_gun_upgrade = 3
        tank_armor_upgrade = 2
        tank_engine_upgrade = 1
    }
    
    obsolete = no
    model = "GER_medium_tank_2_entity"
}
```

### Variant Requirements by DLC

Equipment variants have mandatory `version_name` (the variant name) requirements depending on DLC:

**NSB (No Step Back):** Tank equipment REQUIRES `version_name` or the equipment definition name when spawning units. Missing this causes crash or failure to spawn divisions.

**MTG (Man the Guns):** Ship equipment REQUIRES `version_name`. Ships cannot spawn without a valid variant registered in country history.

**BBA (By Blood Alone):** Airplane equipment REQUIRES `version_name`.

**Non-DLC equipment:** `version_name` is OPTIONAL. If unspecified, the game uses the base archetype.

> [!CRITICAL] When DLC equipment lacks a variant name during unit spawning (in OOB files), the game will crash or fail to create the unit. Always define variants in country history before referencing them in OOB files.

## Upgrade Modules

Upgrades modify equipment stats:

```hoi4
upgrades = {
    tank_gun_upgrade = {
        soft_attack = 1
        hard_attack = 2
        piercing = 3
        
        build_cost_ic = 0.5
        resources = {
            tungsten = 1
        }
    }
}
```

Each upgrade level applies its bonuses cumulatively. Level 3 tank_gun_upgrade applies the bonuses three times.

## Production System

Equipment production is initiated via effects or OOB files:

```hoi4
add_equipment_production = {
    equipment = {
        type = infantry_equipment_1
        creator = "GER"
        version_name = "Kar98k"
    }
    requested_factories = 5
    progress = 0.85
    efficiency = 50
}
```

### Production Efficiency

Efficiency is specified as **0-100 (percent)**, NOT 0.0-1.0.

> [!CRITICAL] Using `efficiency = 0.5` sets 0.5% efficiency, not 50%. Always use whole number percentages: `efficiency = 50` for 50%.

The `progress` attribute represents completion toward a SINGLE unit, not the entire production run. A value of `progress = 2.3` means 2 completed units have been produced, plus 0.3 progress toward the third unit.

Ships do NOT have `production_efficiency_cap_factor` or `production_efficiency_gain_factor`. These production bonuses have no effect on naval equipment - attempting to modify ship production efficiency through these factors does nothing.

## Equipment Behavior in OOB Files

When spawning units through OOB files:

```hoi4
division = {
    start_equipment_factor = 0.8
    force_equipment_variants = {
        infantry_equipment = {
            owner = "GER"
            creator = "GER" 
            version_name = "Kar98k"
        }
    }
}
```

The `start_equipment_factor` does NOT subtract from country reserves. Units spawn with equipment "out of thin air" at the specified percentage of their maximum capacity.

> [!CRITICAL] When using `force_equipment_variants` with partial amounts, remaining equipment slots stay EMPTY rather than auto-filling. A division with 100 equipment need and `start_equipment_factor = 0.5` forcing only 30 specific variants will have 30 of the variant and 20 empty slots, not 50 filled slots.

## Factory Assignment

The `requested_factories` parameter in production effects queues the request if insufficient factories are available. It does NOT error or clamp to current capacity - the game will assign factories as they become available.

## Equipment Categories

Equipment uses the `type` field to match with unit `need` and `type` blocks:

```hoi4
# In equipment definition
type = infantry

# In unit definition
type = {
    infantry
    support
}
```

Units can use equipment matching any of their listed types. This enables equipment substitution (e.g., support equipment filling infantry equipment roles).

## Lend-Lease and Gifting

Equipment can be transferred between nations:

```hoi4
# Creator field determines technology level
infantry_equipment_1 = {
    owner = "POL"
    creator = "GER"
    version_name = "Kar98k"
}
```

If the owner lacks the required technology but the creator has it, the equipment uses the creator's technology level. This allows gifting advanced equipment to less developed nations.

For ships specifically, if the owner lacks ship technology but the creator has it, the ship uses creator's tech level BUT the owner receives and can deploy the ship normally.

## Interface Categories

```hoi4
interface_category = interface_category_land
```

Interface categories group equipment in production menus:

- `interface_category_land` - Ground equipment
- `interface_category_air` - Aircraft  
- `interface_category_naval` - Ships
- `interface_category_armor` - Tanks (NSB only)

## Related Systems

See [Units](/military/units.md) for equipment need blocks and type matching.  
See [OOB Files](/military/oob.md) for equipment assignment in starting forces.  
See [MIOs](/military/mios.md) for equipment production bonuses from military-industrial organizations.
