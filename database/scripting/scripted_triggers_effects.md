---
domain: scripting
concept: scripted_triggers_effects
version: 1.14+
requires: [triggers_core, effects, scopes]
relates: [localisation, events, decisions]
---

# Scripted Triggers, Effects, and Localization

Reusable script components that enable code abstraction, maintainability, and dynamic content generation.

## Scripted Triggers

Reusable trigger definitions in `common/scripted_triggers/*.txt`:

```hoi4
is_major_european_power = {
    is_major = yes
    OR = {
        tag = GER
        tag = FRA
        tag = ENG
        tag = ITA
        tag = SOV
    }
    capital_scope = {
        is_on_continent = europe
    }
}
```

### Usage

```hoi4
if = {
    limit = { is_major_european_power = yes }
    # Trigger evaluates to true/false
}

# Inverted check
if = {
    limit = { is_major_european_power = no }
    # Checks if trigger is false
}
```

### Override Behavior

When multiple files define the same scripted trigger name, the last evaluated file wins. Files load in ASCII filename order:

```text
00_scripted_triggers.txt    # Loads first
zz_scripted_triggers.txt    # Loads last - overrides earlier definitions
```

Use filename prefixes to control load order and intentional overrides.

## Special Scripted Trigger Patterns

### Diplomacy Triggers

Special naming pattern modifies diplomatic action availability:

```hoi4
DIPLOMACY_<ACTION>_ENABLE_TRIGGER = {
    # Custom conditions
    has_war = no
    is_subject = no
}
```

Example actions:

- `DIPLOMACY_BOOST_PARTY_ENABLE_TRIGGER`
- `DIPLOMACY_GUARANTEE_ENABLE_TRIGGER`  
- `DIPLOMACY_MILITARY_ACCESS_ENABLE_TRIGGER`

These triggers directly control whether diplomatic options appear as available in the UI.

### Resistance Triggers

Control resistance initiation in occupied states:

**Global setting:**

```hoi4
should_initiate_resistance = {
    # Conditions for any state
    always = yes
}
```

**State-specific override:**

```hoi4
should_initiate_resistance_42_116 = {
    # Specific rule for states 42-116
    compliance < 50
}
```

> [!CRITICAL] Resistance never auto-initiates unless a `should_initiate_resistance` trigger returns true. Without any such trigger, occupied states never generate resistance. State-specific triggers override the global setting.

Format: `should_initiate_resistance_<start_id>_<end_id>` for state ranges, or `should_initiate_resistance_<id>` for single states.

## Scripted Effects

Reusable effect definitions in `common/scripted_effects/*.txt`:

```hoi4
promote_random_general = {
    random_unit_leader = {
        limit = {
            is_field_marshal = no
            skill > 3
        }
        promote_leader = yes
    }
}
```

### Usage

```hoi4
promote_random_general = yes
```

Simply reference the name followed by `= yes`. The effect block executes in the current scope.

### Parameterization via Variables

Scripted effects can read variables from the calling scope for parameterization:

```hoi4
# Definition
add_scaled_political_power = {
    add_political_power = var:pp_amount
}

# Usage
set_variable = { pp_amount = 100 }
add_scaled_political_power = yes
```

The effect reads `pp_amount` from the calling scope's variables. This enables pseudo-parameters without formal parameter syntax.

### Override Behavior

Same as scripted triggers - last evaluated file wins based on ASCII load order.

## Scripted Localization

Dynamic localization selection based on game state. Defined in `common/scripted_localisation/*.txt`:

```hoi4
defined_text = {
    name = get_country_status
    
    text = {
        trigger = {
            has_war = yes
            has_capitulated = yes
        }
        localization_key = "STATUS_CAPITULATED"
    }
    
    text = {
        trigger = {
            has_war = yes
        }
        localization_key = "STATUS_AT_WAR"
    }
    
    text = {
        trigger = {
            always = yes
        }
        localization_key = "STATUS_PEACE"
    }
}
```

### Usage in Localization Files

```yaml
event_text:0 "The situation in [ROOT.get_country_status]..."
```

At runtime, the game evaluates each `trigger` block in order and uses the first matching `localization_key`.

### Multiple Text Blocks

The first text block with a true trigger is selected. Order matters - place more specific conditions before general ones:

```hoi4
defined_text = {
    name = get_leader_title
    
    text = {
        trigger = { has_government = fascism }
        localization_key = "TITLE_FUHRER"
    }
    text = {
        trigger = { has_government = communism }
        localization_key = "TITLE_GENERAL_SECRETARY"
    }
    text = {
        trigger = { always = yes }  # Fallback
        localization_key = "TITLE_LEADER"
    }
}
```

### Scope Context

Scripted localization evaluates in the scope of the bracketed reference:

```yaml
# In country scope
text:0 "[ROOT.get_country_status]"  # Evaluates in ROOT country scope

# In state scope  
text:0 "[owner.get_country_status]"  # Evaluates in owner country scope
```

## Meta Triggers and Effects

Dynamic text replacement for trigger and effect tooltips:

```hoi4
text = {
    has_equipment = {
        [EQUIPMENT] > 100
    }
}
```

Square brackets `[TOKEN]` mark replacement points. The actual value substitutes at evaluation.

### Debug Mode

Add `debug = yes` to log the final substituted text to game.log:

```hoi4
text = {
    debug = yes
    trigger = {
        has_political_power > [PP_AMOUNT]
    }
    localization_key = "EVENT_TEXT"
}
```

This helps debug complex dynamic localization where the final output isn't obvious.

## Priority and Evaluation Order

### Scripted Trigger/Effect Priority

When the same name is defined multiple times:

1. Files load in ASCII character order (00_ before ZZ_)
2. Within files, last definition wins
3. The final evaluated definition is used globally

This enables:

- Base game definitions in 00_filename.txt
- Mod overrides in ZZ_filename.txt
- Conditional loading via filename manipulation

### Scripted Localization Evaluation

Text blocks evaluate in **definition order**, not trigger complexity. The first matching trigger wins:

```hoi4
defined_text = {
    name = example
    
    text = {
        trigger = { always = yes }  # Matches everything
        localization_key = "GENERIC"
    }
    
    text = {
        trigger = { has_war = yes }  # Never reached
        localization_key = "WAR"
    }
}
```

Always order from most specific to most general, with `always = yes` as the final fallback.

## Common Patterns

### Scope-Aware Scripted Triggers

```hoi4
is_eligible_for_focus = {
    is_subject = no
    has_war = no
    has_stability > 0.5
    NOT = { has_country_flag = focus_in_progress }
}
```

Use in multiple focuses without duplication:

```hoi4
available = {
    is_eligible_for_focus = yes
    has_idea = mobilization_laws
}
```

### Chained Scripted Effects

```hoi4
# Definition
stabilize_economy = {
    add_stability = 0.05
    add_political_power = 50
}

boost_war_effort = {
    stabilize_economy = yes  # Call other scripted effect
    add_war_support = 0.10
}
```

Scripted effects can call other scripted effects, enabling composition.

### Variable-Based Parameterization

```hoi4
# Effect definition
apply_scaled_modifier = {
    add_ideas = var:modifier_token
    add_timed_idea = {
        idea = var:modifier_token
        days = var:duration_days
    }
}

# Usage
set_variable = { modifier_token = token:economic_boom }
set_variable = { duration_days = 365 }
apply_scaled_modifier = yes
```

Variables provide pseudo-parameters for scripted effects.

### Dynamic Localization with State Context

```hoi4
defined_text = {
    name = get_state_situation
    
    text = {
        trigger = {
            resistance > 50
            compliance < 30
        }
        localization_key = "SITUATION_UPRISING"
    }
    text = {
        trigger = {
            compliance > 70
        }
        localization_key = "SITUATION_PACIFIED"
    }
    text = {
        trigger = { always = yes }
        localization_key = "SITUATION_NORMAL"
    }
}
```

Usage in state scope:

```yaml
state_modifier_tt:0 "The situation is [THIS.get_state_situation]"
```

## Tooltip Behavior

### Scripted Trigger Tooltips

Scripted triggers generate compound tooltips showing all sub-conditions:

```hoi4
is_valid_target = {
    is_subject = no  # Shows in tooltip
    has_war = no     # Shows in tooltip
}
```

Use `custom_trigger_tooltip` to override:

```hoi4
is_valid_target = {
    custom_trigger_tooltip = {
        tooltip = valid_target_tt
        is_subject = no
        has_war = no
    }
}
```

### Scripted Effect Tooltips

Similarly generate compound tooltips. Use `custom_effect_tooltip` or `hidden_effect` + `effect_tooltip` pattern for control.

## Best Practices

1. **Name descriptively:** `is_major_power` not `check1`
2. **Order by specificity:** Most specific triggers/text blocks first
3. **Document complex logic:** Comments in definition files
4. **Use fallbacks:** Always include `always = yes` in scripted localization
5. **Avoid circular references:** Scripted effect A calling effect B calling effect A causes crashes
6. **Scope validation:** Ensure triggers/effects work in intended scopes
7. **Variable hygiene:** Use unique variable names to avoid collisions

## Common Pitfalls

### Infinite Recursion

```hoi4
# DON'T DO THIS
effect_a = {
    effect_b = yes
}

effect_b = {
    effect_a = yes  # Circular dependency - crashes
}
```

### Scope Mismatches

```hoi4
# Definition assumes country scope
is_prepared_for_war = {
    has_army_size = { size > 50 }  # Country-scoped trigger
}

# Used in state scope - fails
42 = {
    is_prepared_for_war = yes  # Returns false (wrong scope)
}
```

Always validate scope requirements.

### Localization Fallback Omission

```hoi4
defined_text = {
    name = get_status
    text = {
        trigger = { has_war = yes }
        localization_key = "AT_WAR"
    }
    # No fallback - returns empty string in peace
}
```

Always include `always = yes` fallback to prevent empty strings.

## Related Systems

For trigger and effect mechanics, see [Core Triggers](/scripting/triggers_core.md) and [Effects](/scripting/effects.md).

For localization file format, see [Localisation](/assets/localisation.md).
