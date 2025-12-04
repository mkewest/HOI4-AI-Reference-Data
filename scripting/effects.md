---
domain: scripting
concept: effects
version: 1.14+
requires: [scopes, triggers]
relates: [on_actions, events, decisions, scripted_effects]
---

# Effects System

Effects modify game state by changing variables, adding resources, triggering events, and manipulating game objects. Unlike triggers which check conditions, effects perform actions.

## Basic Structure

Effects are commands that execute sequentially:

```hoi4
add_political_power = 50
add_stability = 0.05
set_country_flag = reform_completed
```

Each effect executes in order. There is no short-circuit evaluation like triggers - all effects run unless explicitly prevented by conditional logic.

## Flow Control

### hidden_effect

Executes effects without displaying tooltips:

```hoi4
hidden_effect = {
    add_political_power = -100
    set_country_flag = secret_path
}
# These effects execute but don't show in UI
```

Use `hidden_effect` when the tooltip would be confusing or when combining with `custom_effect_tooltip` for cleaner presentation.

### effect_tooltip

Shows tooltip WITHOUT executing the effects:

```hoi4
effect_tooltip = {
    add_political_power = 50
    add_stability = 0.10
}
# Tooltip appears but nothing happens
```

Commonly paired with `hidden_effect`:

```hoi4
hidden_effect = {
    # Complex internal logic
    add_political_power = random_var
}
effect_tooltip = {
    add_political_power = 50
    # Shows simplified version to user
}
```

### custom_effect_tooltip

Replaces effect tooltip with custom localization:

```hoi4
custom_effect_tooltip = my_complex_effect_tt
add_political_power = calculate_value
```

The tooltip shows `my_complex_effect_tt` localization instead of the actual effect. The effect still executes normally.

### if / else_if / else

Conditional execution based on triggers:

```hoi4
if = {
    limit = { has_idea = great_depression }
    add_stability = 0.10
    else_if = {
        limit = { has_idea = recession }
        add_stability = 0.05
    }
    else = {
        add_stability = 0.02
    }
}
```

Only one branch executes. The first matching `limit` trigger determines which branch runs.

### random

Probabilistic execution with weighted outcomes:

```hoi4
random = {
    chance = 50
    add_stability = 0.05
    modifier = {
        factor = 2
        has_idea = lucky_nation
    }
}
```

Base chance is 50% (0-100 scale). Modifiers multiply the chance - `factor = 2` doubles it to 100%.

### random_list

Select one outcome from weighted options:

```hoi4
random_list = {
    10 = { add_stability = 0.05 }
    20 = { add_war_support = 0.05 }
    70 = { add_political_power = 50 }
}
```

Weights are relative, not percentages. Total is 100, so probabilities are 10%, 20%, and 70%.

Each entry can have its own `modifier` block:

```hoi4
random_list = {
    50 = {
        modifier = { factor = 2 has_stability < 0.3 }
        add_stability = 0.10
    }
    50 = { add_war_support = 0.10 }
}
```

## Looping Constructs

### for_loop_effect

Iterates a specific number of times:

```hoi4
set_variable = { counter = 0 }
for_loop_effect = {
    start = 0
    end = 10
    add_to_variable = { counter = 1 }
    add_political_power = 5
}
# Executes 10 times (0 through 9 inclusive)
```

> [!CRITICAL] Maximum 1000 iterations per loop. Exceeding this limit causes the loop to stop automatically without error or warning. The define `MAX_EFFECT_ITERATION` controls this.

Loop variables are not exposed directly. Use your own variables to track iteration state if needed.

### while_loop_effect

Iterates while a condition remains true:

```hoi4
set_variable = { counter = 0 }
while_loop_effect = {
    limit = { check_variable = { counter < 10 } }
    add_to_variable = { counter = 1 }
    add_political_power = 5
}
```

> [!CRITICAL] Also limited to 1000 iterations maximum. Ensure the limit condition eventually becomes false, or the loop stops at 1000 with no error.

### break

Exits a loop early:

```hoi4
for_loop_effect = {
    start = 0
    end = 100
    if = {
        limit = { check_variable = { some_var > 50 } }
        break = yes
    }
    add_political_power = 1
}
```

The `break` effect only works inside loops. It has no effect outside looping contexts.

## Array Scopes

Array-based iteration over saved scopes:

```hoi4
add_to_temp_array = { array = targets value = GER }
add_to_temp_array = { array = targets value = ITA }

for_each_scope_loop = {
    array = targets
    add_opinion_modifier = {
        target = ROOT
        modifier = trade_agreement
    }
}
```

### random_scope_in_array

Selects one random scope from array:

```hoi4
random_scope_in_array = {
    array = potential_targets
    limit = { NOT = { has_war_with = ROOT } }
    create_wargoal = {
        type = annex_everything
        target = THIS
    }
}
```

## Scope-Changing Effects

Some effects change the active scope during execution. See [Scopes](/scripting/scopes.md) for details on `start_civil_war`, `create_dynamic_country`, and scope-changing behavior.

## Common Effect Categories

### Political Power and Stability

```hoi4
add_political_power = 50                  # Add/subtract PP
add_stability = 0.05                      # Modify stability (-1.0 to 1.0)
add_war_support = 0.05                    # Modify war support
set_stability = 0.5                       # Set exact stability
set_war_support = 0.6                     # Set exact war support
add_timed_idea = { idea = name days = N } # Temporary idea
add_ideas = idea_name                     # Permanent idea
remove_ideas = idea_name                  # Remove idea
modify_timed_idea = { idea = name days = N }  # Extend/reduce duration
swap_ideas = { remove_idea = old add_idea = new }
```

### Resources and Economy

```hoi4
add_manpower = 10000                      # Add manpower (in ones)
add_equipment_to_stockpile = { type = infantry_equipment amount = 1000 }
create_equipment_variant = { name = "..." type = base_type parent_version = 0 }
add_resource = { type = steel amount = 10 state = 42 }
add_fuel = 5000                           # Add fuel reserves
add_offsite_building = { type = industrial_complex level = 5 }
```

### Military

```hoi4
add_equipment_to_stockpile = { type = infantry_equipment amount = 1000 }
create_unit = { division = "template_name" owner = TAG }
delete_unit = { id = division_id }
white_peace = { tag = TAG }               # End war with tag
declare_war_on = { target = TAG type = annex_everything }
create_wargoal = { type = annex_everything target = TAG }
set_truce = { target = TAG days = 365 }
puppet = TAG                              # Puppet target
annex_country = { target = TAG }          # Annex target completely
```

### Territory

```hoi4
transfer_state = state_id                 # Transfer to current scope
add_state_core = state_id                 # Add core
remove_state_core = state_id              # Remove core
add_state_claim = state_id                # Add claim
remove_state_claim = state_id             # Remove claim
set_capital = { state = id }              # Change capital
set_province_controller = { id = N controller = TAG }
```

### Technology

```hoi4
add_tech_bonus = { name = bonus ahead_reduction = 1.5 uses = 1 bonus = 1.0 category = infantry_tech }
set_technology = { tech_name = 1 }        # Unlock technology
add_research_slot = 1                     # Add research slot
```

### Characters and Leaders

```hoi4
create_corps_commander = { name = "..." portrait_path = "..." traits = { ... } skill = 3 attack_skill = 2 defense_skill = 3 planning_skill = 2 logistics_skill = 2 }
create_field_marshal = { ... }
create_navy_leader = { ... }
add_unit_leader_trait = trait_token
remove_unit_leader_trait = trait_token
promote_leader = unit_leader_id
retire_character = character_token
kill_character = character_token
```

### Events and Flags

```hoi4
country_event = { id = namespace.id days = 30 }
state_event = { id = namespace.id days = 7 }
news_event = { id = namespace.id }
set_country_flag = { flag = name value = 1 days = 365 }
clr_country_flag = name                   # Clear flag
modify_country_flag = { flag = name value = 5 }
set_state_flag = name
clr_state_flag = name
set_global_flag = name
clr_global_flag = name
```

### Variables

```hoi4
set_variable = { var = name value = 100 }
set_variable = { var = name value = TAG }  # Store scope reference
add_to_variable = { var = name value = 10 }
subtract_from_variable = { var = name value = 5 }
multiply_variable = { var = name value = 2 }
divide_variable = { var = name value = 2 }
modulo_variable = { var = name value = 3 }
clamp_variable = { var = name min = 0 max = 100 }
round_variable = name                      # Round to integer
clear_variable = name                      # Delete variable
```

### Diplomatic Relations

```hoi4
add_opinion_modifier = { target = TAG modifier = name }
reverse_add_opinion_modifier = { target = TAG modifier = name }
remove_opinion_modifier = { target = TAG modifier = name }
add_relation_modifier = { target = TAG modifier = name }
remove_relation_modifier = { target = TAG modifier = name }
add_ai_strategy = { type = strategy_type id = TAG value = 100 }
create_faction = name
add_to_faction = TAG
remove_from_faction = TAG
leave_faction = yes
dismantle_faction = yes
set_faction_leader = yes
```

### Occupation and Resistance

```hoi4
set_occupation_law = law_token
set_occupation_law_where_available = law_token
add_resistance = 10                        # Add resistance level
add_compliance = 10                        # Add compliance level
force_enable_resistance = TAG              # Enable resistance in occupied
add_resistance_target = { state = id amount = 50 occupier = TAG days = 365 }
```

### Modifiers

```hoi4
add_dynamic_modifier = { modifier = name scope = TAG days = 365 }
remove_dynamic_modifier = { modifier = name }
force_update_dynamic_modifier = yes
add_province_modifier = { modifier = name province = id }
remove_province_modifier = { modifier = name province = id }
```

## Tooltip Management

Single-scope tooltips only show the FIRST scope when multiple are evaluated:

```hoi4
every_neighbor_country = {
    limit = {
        if = { limit = { is_major = yes }
            has_army_size = { size > 50 }
        }
    }
    # Tooltip shows only first neighbor
}
```

Use `display_individual_scopes = yes` to force separate tooltips per scope:

```hoi4
every_neighbor_country = {
    display_individual_scopes = yes
    limit = { ... }
    # Shows separate tooltip for each neighbor
}
```

## Meta Effects

Meta effects support dynamic text replacement using square brackets:

```hoi4
log = "[THIS.GetName] has [?manpower] manpower"
# Evaluates and substitutes bracketed expressions
```

Add `debug = yes` to log output to game.log for debugging.

## Scripted Effects

Defined in `common/scripted_effects/*.txt`:

```hoi4
my_effect_name = {
    add_political_power = 50
    add_stability = 0.05
}
```

Usage:
```hoi4
my_effect_name = yes
```

Multiple definitions: last evaluated file wins (ASCII filename order).

## Zero-Value Modifiers

> [!CRITICAL] Any modifier with value 0 has NO EFFECT and cannot be overridden by other modifiers. A modifier set to 0 is completely ignored by the game engine.

Negative modifiers always work and have the opposite effect of positive modifiers. For example, `stability_factor = -0.10` reduces stability gain.

## Common Patterns

### Safe Event Triggers

```hoi4
if = {
    limit = { country_exists = GER }
    GER = { country_event = namespace.1 }
}
```

Always check existence before targeting specific countries, especially in on_actions that fire for all countries.

### Progressive Effects

```hoi4
if = {
    limit = { has_stability > 0.7 }
    add_political_power = 100
    else_if = {
        limit = { has_stability > 0.5 }
        add_political_power = 50
    }
    else = {
        add_political_power = 25
    }
}
```

### Array Building and Iteration

```hoi4
# Build array
every_neighbor_country = {
    limit = { NOT = { has_war_with = ROOT } }
    add_to_temp_array = { array = potential_allies value = THIS }
}

# Iterate array
for_each_scope_loop = {
    array = potential_allies
    # Effects on each scope
}
```

## Related Defines

- `MAX_EFFECT_ITERATION`: Maximum loop iterations - See [NGame](/defines_list/NGame.md)

## Documentation

Complete effects documentation: `documentation/effects_documentation.html` (in game installation directory)
