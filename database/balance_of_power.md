---
domain: database
concept: balance_of_power
version: 1.13+
requires: [modifiers_list, decisions]
relates: [modifiers, decisions]
---

# Balance of Power System

Balance of Power (BoP) is a slider mechanic introduced in version 1.13 that tracks dynamic relationships between two opposing sides. BoPs are defined in `common/bop/*.txt`.

## Core Structure

```hoi4
bop_id = {
    id = bop_id
    
    initial_value = 0
    
    left_side = {
        id = left_side_id
        icon = GFX_left_icon
    }
    
    right_side = {
        id = right_side_id
        icon = GFX_right_icon
    }
    
    range = {
        id = range_id
        min = -0.5
        max = 0
        
        modifier = {
            stability_factor = 0.1
        }
        
        on_activate = {
            # effects when entering range
        }
        
        on_deactivate = {
            # effects when leaving range
        }
    }
}
```

## Value System

Balance of Power uses a float value in the range [-1, 1] with 3 decimal places of precision:

```yaml
value_range: [-1.0, 1.0]
precision: 3
examples:
  - -1.000 (maximum left)
  - -0.500 (moderate left)
  - 0.000 (center)
  - 0.500 (moderate right)
  - 1.000 (maximum right)
```

The value represents the current position on the slider between the two sides.

## Side Definitions

### Left and Right Sides

```hoi4
left_side = {
    id = monarchists
    icon = GFX_bop_monarchists
}

right_side = {
    id = republicans
    icon = GFX_bop_republicans
}
```

Each side requires:

- `id`: Unique identifier for the side
- `icon`: Sprite reference for UI display

> [!CRITICAL] Side assignment only controls VISIBILITY and display, not the logic of how ranges work. A left side can have ranges in the right half of the slider (positive values), and vice versa. The balance visual is independent of which side's range is currently active.

## Range System

Ranges define zones on the slider that activate modifiers and effects:

```hoi4
range = {
    id = moderate_left
    min = -0.5
    max = 0
    
    modifier = {
        political_power_gain = 0.1
        stability_factor = 0.05
    }
    
    rule = {
        can_create_factions = yes
    }
    
    on_activate = {
        add_political_power = 50
    }
    
    on_deactivate = {
        add_political_power = -50
    }
}
```

### Range Boundaries

- `min`: Inclusive lower boundary (value ≥ min)
- `max`: Upper boundary (value < max), EXCEPT when max = 1

> [!CRITICAL] The `max` boundary is EXCLUSIVE in all cases except when `max = 1`. For example, `max = 0.5` means values up to 0.499... activate this range, but 0.5 itself does not. Only `max = 1` is inclusive, allowing the value 1.0 to activate the range.

This exception exists to ensure the maximum slider value (1.0) can activate a range.

### Duplicate Range IDs

> [!CRITICAL] When multiple ranges share the same ID, the game displays ALL non-disabled ranges with that ID simultaneously. However, the trigger `is_power_balance_in_range` recognizes only the LEFTMOST duplicate (first defined range with that ID).

This creates inconsistent behavior where:

- Visual display shows all duplicates as active
- Trigger checks only recognize the first occurrence
- Modifiers from all duplicates stack

Avoid duplicate range IDs to prevent confusion.

## Modifiers and Rules

### Modifiers

```hoi4
modifier = {
    stability_factor = 0.1
    war_support_factor = 0.05
    political_power_gain = 0.25
}
```

Modifiers use standard country-scoped modifier syntax. They apply to every country that has this BoP initialized.

> [!CRITICAL] BoP modifiers are CLONED to each country with the BoP. If multiple countries share the same BoP ID, they each receive independent copies of the modifiers. Changing the BoP's modifiers doesn't retroactively update existing country modifiers.

### Rules

```hoi4
rule = {
    can_create_factions = yes
    can_declare_war_on_same_ideology = no
}
```

Rules modify game rules for countries within this range. They use standard rule modifier syntax.

## Effects

### on_activate

```hoi4
on_activate = {
    country_event = my_event.1
    add_stability = 0.05
}
```

Executes when the BoP value enters this range. Fires once per range entry.

### on_deactivate

```hoi4
on_deactivate = {
    country_event = my_event.2
    add_stability = -0.05
}
```

Executes when the BoP value leaves this range. Fires once per range exit.

## Global Tracking

> [!CRITICAL] The BoP value is SHARED across all countries that have the same BoP ID assigned. When multiple countries have modifiers that affect the same BoP, their effects STACK.

This creates interesting dynamics:

- Multiple countries can collaboratively push the same BoP
- Modifiers from different countries combine
- The BoP represents a global relationship, not per-country state

Example: If Germany and Italy both have `spanish_civil_war_bop` and both apply modifiers, the modifiers stack to move the slider faster.

## Decision Category Integration

```hoi4
decision_category = bop_decisions
```

The `decision_category` attribute moves a decision category exclusively to the BoP interface view.

> [!CRITICAL] Decisions in a BoP-linked category become impossible to access outside the BoP interface. This is a one-way binding - once a decision category is assigned to a BoP, it can only be accessed through that BoP's UI.

Use this to create BoP-specific actions that directly manipulate the slider or respond to its state.

## Static Modifiers

BoP modifiers are defined as static modifiers in `common/modifiers/*.txt`:

### Special Modifier Types

```hoi4
power_balance_daily = {
    # modifiers that apply daily
}

power_balance_weekly = {
    # modifiers that apply weekly
}
```

These special modifier categories control the rate at which BoP values change. Daily modifiers apply every day, weekly modifiers apply every 7 days.

## Effects and Triggers

### set_power_balance

```hoi4
set_power_balance = {
    id = bop_id
    left_side = left_side_id
    right_side = right_side_id
    set_value = 0.5
}
```

Initializes or modifies a BoP. Attributes:

- `id`: BoP to modify
- `left_side`: Left side ID (optional if already set)
- `right_side`: Right side ID (optional if already set)
- `set_value`: New value to set
- `set_default`: Boolean, resets to initial configuration

> [!CRITICAL] When `set_default = yes`, the effect resets to `initial_value`, `left_side`, and `right_side` from the definition, overriding all other parameters in the same effect call.

### add_power_balance_modifier

```hoi4
add_power_balance_modifier = {
    id = bop_id
    modifier = daily_shift_left
}
```

Adds a static modifier that continuously affects the BoP value. The modifier must be defined in `common/modifiers/*.txt`.

### remove_power_balance_modifier

```hoi4
remove_power_balance_modifier = {
    id = bop_id
    modifier = daily_shift_left
}
```

Removes a previously applied BoP modifier.

### remove_all_power_balance_modifiers

```hoi4
remove_all_power_balance_modifiers = {
    id = bop_id
}
```

Removes all modifiers from the specified BoP, resetting it to only its base drift.

## Triggers

### has_power_balance

```hoi4
has_power_balance = {
    id = bop_id
}
```

Checks if the country has the specified BoP initialized.

### is_power_balance_in_range

```hoi4
is_power_balance_in_range = {
    id = bop_id
    range = range_id
}
```

Checks if the BoP's current value falls within the specified range. Remember that duplicate range IDs only check the first occurrence.

### is_power_balance_side_active

```hoi4
is_power_balance_side_active = {
    id = bop_id
    side = left_side_id
}
```

Checks if the specified side is currently "winning" (value is on that side's half of the slider).

### power_balance_value

```hoi4
power_balance_value = {
    id = bop_id
    value > 0.5
}
```

Compares the BoP's current value using standard comparison operators: `>`, `<`, `=`, `>=`, `<=`.

### power_balance_daily_change

```hoi4
power_balance_daily_change = {
    id = bop_id
    value > 0.01
}
```

Checks the daily rate of change for the BoP value.

### power_balance_weekly_change

```hoi4
power_balance_weekly_change = {
    id = bop_id
    value < -0.05
}
```

Checks the weekly rate of change for the BoP value.

## Common Usage Patterns

### Civil War Dynamics

```hoi4
spanish_civil_war = {
    id = spanish_civil_war
    initial_value = 0
    
    left_side = {
        id = nationalists
        icon = GFX_nationalist_spain
    }
    
    right_side = {
        id = republicans
        icon = GFX_republican_spain
    }
    
    range = {
        id = nationalist_victory
        min = 0.7
        max = 1
        
        on_activate = {
            country_event = spanish_civil_war.10
        }
    }
}
```

### Diplomatic Influence

```hoi4
turkish_foreign_policy = {
    id = turkish_alignment
    initial_value = 0
    
    left_side = {
        id = axis_influence
        icon = GFX_axis_icon
    }
    
    right_side = {
        id = allied_influence
        icon = GFX_allied_icon
    }
    
    range = {
        id = axis_leaning
        min = -1
        max = -0.3
        
        modifier = {
            justify_war_goal_time = -0.15
        }
    }
}
```

## Related Systems

For static modifier definitions, see the static modifiers documentation.

For decision integration, see [Decisions](/decisions.md).

For effect and trigger syntax, see the scripting reference documentation.
