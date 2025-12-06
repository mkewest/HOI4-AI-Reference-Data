---
domain: military
concept: mios
version: 1.14+
requires: [equipment]
relates: [equipment]
---

# Military-Industrial Organizations (MIOs)

Military-Industrial Organizations (MIOs) represent industrial entities that provide equipment production bonuses and unlock specialized modifications. Introduced in the No Step Back (NSB) DLC, MIOs offer persistent bonuses tied to specific equipment categories and allow nations to develop specialized industrial capabilities.

## MIO Definition Structure

MIOs are defined in `common/military_industrial_organization/organizations/*.txt`:

```hoi4
GER_mauser_organization = {
    include = generic_infantry_equipment_organization
    icon = GFX_idea_mauser
    allowed = {
        tag = GER
    }
    
    initial_trait = {
        organization_modifier = {
            military_industrial_organization_research_bonus = 0.05
        }
        
        equipment_bonus = {
            build_cost_ic = -0.05
            reliability = 0.05
        }
    }
    
    trait = { ... }
    trait = { ... }
}
```

## Loading and Timing

> [!CRITICAL] MIOs and policies load ONLY when creating a new game. They cannot be injected into ongoing games through OOB files, effects, or any other mechanism.

Trait modifications (bonuses, icons, localization) can be changed in mod files without starting a new game. However:
- Adding new traits works mid-game
- Removing existing traits causes errors mid-game

When validating MIO files, check `error.log` TWICE:
1. Immediately after game start
2. After browsing MIO menus in-game (visibility filters fire on menu access, potentially revealing errors not present at load time)

## Allowed Condition

The `allowed` block is evaluated at GAME START in country scope ONLY:

```hoi4
allowed = {
    tag = GER
    has_dlc = "No Step Back"
}
```

Some conditions are meaningless at game start (e.g., `is_ai` - the player hasn't taken control yet). The allowed condition determines which countries can see and use the MIO.

AI requires BOTH `visible = yes` AND `available = yes` to actually use an MIO. Setting only one prevents AI utilization.

## Initial Trait

The initial trait provides starting bonuses and has special properties:

```hoi4
initial_trait = {
    organization_modifier = {
        military_industrial_organization_research_bonus = 0.05
    }
    
    limit_to_equipment_type = {
        infantry_equipment
    }
    
    equipment_bonus = {
        build_cost_ic = -0.05
        reliability = 0.05
    }
    
    production_bonus = {
        production_efficiency_gain_factor = 0.02
    }
}
```

Initial traits have NO position on the trait grid, NO icon, and NO player decision point. Only these attributes are meaningful:
- `name` (for localization)
- `limit_to_equipment_type`
- `equipment_bonus`
- `production_bonus`
- `organization_modifier`

## Trait System

Traits are arranged on a 10×5 grid (scrollable below y=4) and provide specialized bonuses:

```hoi4
trait = {
    token = mauser_improved_quality
    name = mauser_improved_quality
    icon = GFX_generic_mio_trait_icon_production_efficiency
    
    position = { x = 0 y = 0 }
    
    visible = {
        FROM = { has_tech = infantry_weapons1 }
    }
    
    available = {
        FROM = { has_completed_focus = GER_prepare_for_war }
    }
    
    limit_to_equipment_type = {
        infantry_equipment
    }
    
    equipment_bonus = {
        soft_attack = 0.05
        reliability = 0.03
    }
    
    production_bonus = {
        production_efficiency_cap_factor = 0.05
    }
}
```

### Trait Grid Coordinates

The trait grid is 10 wide (x: 0-9) and 5 high (y: 0-4). Additional rows below y=4 are scrollable but not recommended for usability.

Coordinates follow the same system as division templates: origin (0,0) is TOP-LEFT, Y increases DOWNWARD. Maximum indices are `(MAX_VALUE - 1)`, not `MAX_VALUE`.

> [!CRITICAL] Out-of-bounds coordinates fail silently. A trait at x=10 when maximum is 9 simply does not appear, with no error message.

### Relative Positioning

Traits can use relative positioning:

```hoi4
trait = {
    position = { x = 0 y = 1 }
    relative_position_id = parent_trait_token
}
```

When `relative_position_id` is set, coordinates become relative to the specified trait. For example, `x = 0 y = 1` with `relative_position_id = parent` places the trait directly beneath the parent trait.

## Visibility and Availability

Trait visibility and availability are evaluated in MIO scope with the country in FROM scope:

```hoi4
visible = {
    FROM = { has_tech = advanced_infantry_weapons }
}

available = {
    FROM = { 
        has_completed_focus = GER_industrial_expansion
        num_of_factories > 50
    }
}
```

`visible` controls whether the trait appears in the selection interface. `available` controls whether it can be selected (grayed out if unavailable).

This enables civil war mechanics where different traits appear based on faction:

```hoi4
trait = {
    token = nationalist_path
    visible = { FROM = { has_government = fascism } }
}

trait = {
    token = republican_path
    position = { x = 0 y = 0 }  # Same coordinates
    visible = { FROM = { has_government = democratic } }
}
```

Multiple traits at the same coordinates switch via `visible` conditions, useful for TAG-specific variations without creating separate MIOs (alternative to Delta MIOs).

## Equipment Bonuses

### Trait Equipment Bonuses

Trait equipment bonuses apply to ALL equipment types produced by the MIO unless constrained by `limit_to_equipment_type`:

```hoi4
trait = {
    equipment_bonus = {
        build_cost_ic = -0.10
        soft_attack = 0.05
    }
    # Applies to all MIO equipment types
}

trait = {
    limit_to_equipment_type = { infantry_equipment }
    equipment_bonus = {
        reliability = 0.05
    }
    # Only applies to infantry equipment
}
```

### Policy Equipment Bonuses

Policy equipment bonuses REQUIRE equipment group/category/archetype/type specification:

```hoi4
policy = {
    equipment_bonus = {
        infantry_equipment = {
            build_cost_ic = -0.05
        }
    }
}
```

> [!CRITICAL] Unlike trait bonuses, policy equipment bonuses do NOT work without explicit equipment type specification. Omitting the equipment type causes the bonus to have no effect.

### Organization Bonuses

Organization modifiers are GLOBAL to the MIO and cannot be constrained by `limit_to_equipment_type`:

```hoi4
trait = {
    organization_modifier = {
        military_industrial_organization_research_bonus = 0.10
    }
    # Affects ALL research by this MIO, cannot be limited to specific equipment
}
```

The `military_industrial_organization_research_bonus` modifier is ADDITIVE, not multiplicative:

```hoi4
# Base research bonus: 20%
# Modifier: 0.1
# Result: 30% (not 22%)
```

A base 20% research bonus plus a 0.1 modifier results in 30% total bonus, not 20% × 1.1 = 22%.

## Production Bonuses

Production bonuses affect factories assigned to MIO equipment:

```hoi4
production_bonus = {
    production_efficiency_cap_factor = 0.05
    production_efficiency_gain_factor = 0.02
    production_capacity_factor = 0.10
}
```

These modifiers only apply to equipment types within the MIO's scope (as defined by `limit_to_equipment_type` in traits or equipment type in policies).

## Mutual Exclusion

Traits can be mutually exclusive:

```hoi4
trait = {
    token = quality_focus
    mutually_exclusive = { token = quantity_focus }
}

trait = {
    token = quantity_focus
    mutually_exclusive = { token = quality_focus }
}
```

> [!CRITICAL] Mutual exclusion must be defined in ALL traits in the exclusion set. If only one trait has it, players can pick the non-exclusive trait first, then bypass the exclusion by selecting the exclusive trait afterward.

## Policy System

Policies are temporary modifiers activated through decisions:

```hoi4
policy = {
    token = emergency_production
    name = emergency_production_policy
    icon = GFX_generic_mio_policy_icon
    
    visible = {
        FROM = { has_war = yes }
    }
    
    available = {
        FROM = { has_manpower > 100000 }
    }
    
    cost = 150
    timeout = 365
    
    equipment_bonus = {
        infantry_equipment = {
            build_cost_ic = -0.15
        }
    }
    
    on_timeout_effect = {
        FROM = {
            add_stability = -0.05
        }
    }
}
```

Policy visibility and availability are evaluated during policy screen display in MIO scope with country in FROM scope.

Policies have costs (political power) and durations. They can trigger effects on activation, timeout, or cancellation.

## Name Resolution

MIO and trait names use fallback localization chains:

**MIO name:** Tries `<tag>_<name>`, then `<name>`
- `GER_mauser_organization` → tries `GER_mauser_organization`, then `mauser_organization`

**Trait name:** Tries `<tag>_<trait_name>`, then `<mio_name>_<trait_token>`
- Trait in `GER_mauser_organization` with token `improved_quality` tries:
  1. `GER_improved_quality`
  2. `mauser_organization_improved_quality`

**Initial trait default:** `<mio_name>_initial_trait`
- `mauser_organization_initial_trait`

**Policy name:** Uses scripted localization in country scope, allowing dynamic text based on conditions.

## Include System

MIOs can include templates:

```hoi4
GER_mauser_organization = {
    include = generic_infantry_equipment_organization
    # Override specific attributes
}
```

The `include` attribute imports another MIO definition as a base, allowing inheritance of common traits and structure while overriding specific attributes like `allowed`, `icon`, or individual traits.

## Related Systems

See [Equipment](/military/equipment.md) for equipment type definitions that MIO bonuses apply to.  
See [OOB Files](/military/oob.md) for initial force setup (note: MIOs cannot be loaded mid-game through OOB).
