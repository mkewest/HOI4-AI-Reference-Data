---
domain: military
concept: units
version: 1.14+
requires: [equipment]
relates: [division_template, combat, terrain]
---

# Units (Battalions and Support Companies)

Units represent battalions and support companies that compose divisions. Each unit type defines combat statistics, equipment requirements, and terrain modifiers.

## Unit Definition Structure

Units are defined in `common/units/*.txt`:

```hoi4
sub_units = {
    infantry = {
        sprite = infantry
        map_icon_category = infantry
        
        priority = 600
        ai_priority = 200
        active = yes
        
        type = {
            infantry
        }
        
        group = mobile
        
        categories = {
            category_front_line
            category_light_infantry
            category_all_infantry
            category_army
        }
        
        combat_width = 2
        
        need = { infantry_equipment = 100 }
        
        manpower = 1000
        max_organisation = 60
        default_morale = 0.3
        training_time = 90
        
        # ... modifiers and equipment bonuses
    }
}
```

## Unit Groups

The `group` attribute assigns units to combat groups. Groups are created implicitly on first reference in any unit file - no explicit registration is required. Once defined anywhere, a group is immediately usable.

Common groups include:

| Group | Purpose |
|-------|---------|
| `mobile` | Infantry, motorized, mechanized |
| `armor` | Tank battalions |
| `support` | Support companies (engineer, recon, etc.) |
| `artillery` | Artillery and anti-air/anti-tank guns |
| `cavalry` | Mounted and scout units |

Groups control which units can occupy the same column in division templates. Units with different groups cannot mix within a single Y-column (see [Division Templates](/military/division_template.md#combat-battalion-groups)).

## Type and Categories

The `type` block lists equipment types this unit can use. Multiple types enable equipment substitution:

```hoi4
type = {
    infantry
    support
}
```

Categories are arbitrary tags used for triggers, effects, and AI evaluation. They have no inherent game meaning but enable scripted conditions like `has_battalion_in_template = category_all_infantry`.

## Combat Statistics

Core combat attributes define unit performance:

```hoi4
soft_attack = 1.5
hard_attack = 0.5
breakthrough = 1.0
defense = 2.0
```

These values are BASE stats. Actual combat values come from:
1. Unit base stats (these values)
2. Equipment stats (from equipped items)
3. Terrain modifiers (see below)
4. Technology bonuses
5. Commander traits and doctrines

The `combat_width` attribute determines how many battalions fit in a combat engagement. Standard infantry uses 2 width; specialized units may use 1, 3, or more.

## Equipment Requirements

The `need` block defines equipment consumption per battalion:

```hoi4
need = {
    infantry_equipment = 100
    support_equipment = 10
}
```

Equipment types must exist in game files (see [Equipment](/military/equipment.md)). The `need` block makes the unit unavailable until the nation possesses at least one unit of each required equipment type.

The `essential` block works differently - it only matters when `active = no`. Essential equipment must be unlocked via technology before the unit becomes available, even if the nation already possesses the equipment.

> [!CRITICAL] Units can be defined but remain unusable if their required equipment types don't exist in the game files. No error is generated - the unit simply never appears in the division designer.

## Unit Speed

The `maximum_speed` attribute is MULTIPLICATIVE, not additive:

```hoi4
maximum_speed = 0.5  # Results in 50% faster, not 0.5 km/h absolute
```

Actual speed is calculated as: `base_speed * (1 + maximum_speed)` km/h.

For motorized and mechanized units, transport equipment overrides the base speed calculation entirely. The unit moves at the speed of its transport equipment rather than using the `maximum_speed` multiplier.

## Supply and Organization

```hoi4
supply_consumption = 0.07
suppression = 1.5
weight = 0.5

max_organisation = 60
default_morale = 0.3
```

Supply consumption affects logistics and attrition. The `suppression` value contributes to occupation and resistance reduction. Weight affects strategic redeployment speed.

Maximum organization determines how long the unit can fight before retreating. Default morale sets initial organization percentage for newly trained units.

## Training and Manpower

```hoi4
manpower = 1000
training_time = 90
```

Manpower is the population cost per battalion. Training time is in days - standard infantry trains in 90 days, specialized units may require 120+ days.

## Equipment Bonuses

Units provide modifiers to their equipped items:

```hoi4
soft_attack = 4.5
hard_attack = 0.1

can_be_parachuted = yes
```

Positive values like `soft_attack = 4.5` ADD to equipment base stats. Negative values like `hard_attack = -0.25` REDUCE equipment stats by that percentage (not absolute subtraction).

## Terrain Modifiers

Terrain-specific modifiers REPLACE base modifiers rather than adding to them:

```hoi4
forest = {
    attack = -0.2
    movement = -0.3
}

hills = {
    attack = -0.1
    defence = 0.05
}
```

When fighting in forests, the unit uses the forest modifiers instead of base combat stats. There is no cumulative effect with the base values.

Naval units typically use ONLY `supply_consumption` and `max_organisation` - combat stats come entirely from ship equipment.

Air units typically use NO unit-level modifiers at all. Aircraft performance is determined entirely by equipment stats.

The `carrier_capable` attribute only applies to air units and is meaningless for other unit types.

## Unit Models and Visuals

Model selection follows this priority order:
1. `cosmetic_tag` (if defined)
2. Country tag
3. `graphical_culture`
4. Default model

Division map entities display based on plurality - the division shows the 3D model of whichever sub-unit type appears most frequently in the template.

### Model Cloning

Clone entities inherit all properties from their parent except explicitly overridden attributes:

```hoi4
sub_units = {
    marine = {
        type = { infantry }
        
        can_be_parachuted = no
        
        # Inherits all other properties from infantry
    }
}
```

## Unit Icons

New units without defined icons display random existing icons (often anti-air or other defaults).

> [!CRITICAL] All THREE sprite types must be defined for proper icon display: `medium`, `medium_white`, and `small`. Missing any sprite causes icon malfunction.

The `medium_white` sprite name MUST contain the word "medium" despite being used for small on-map display. This is a naming requirement, not a functional descriptor.

```hoi4
sub_units = {
    my_unit = {
        sprite = my_unit                    # Uses GFX_unit_my_unit_medium
        map_icon_category = infantry         # Uses GFX_unit_infantry_icon_medium_white
                                            # and GFX_unit_infantry_icon_small
    }
}
```

## Visibility and Availability

```hoi4
active = no
```

When `active = no`, the unit requires technology unlock before appearing in the division designer. The `essential` equipment block defines which technologies must be researched.

```hoi4
active = yes
```

With `active = yes`, the unit is immediately available if the nation possesses required equipment types (from the `need` block).

## AI Behavior

```hoi4
priority = 600
ai_priority = 200
```

Priority affects production and division template selection. Higher priority units receive equipment and production focus first. The `ai_priority` specifically controls AI template design decisions.

## Related Systems

See [Division Templates](/military/division_template.md) for how units compose divisions.  
See [Equipment](/military/equipment.md) for equipment type definitions and stats.
