---
domain: scripting
concept: on_actions_core
version: 1.14+
requires: [effects, scopes]
relates: [events, on_actions_reference]
---

# On Actions: Core Mechanics

On actions are hooks that execute effects when specific game events occur. They enable automatic script responses to game state changes without manual triggers.

## Basic Structure

On actions are defined in `common/on_actions/*.txt` within a root `on_actions` block:

```hoi4
on_actions = {
    on_declare_war = {
        effect = {
            # Effects execute when war declared
        }
    }
}
```

Every on_action has an `effect` block (required) and optional `random_events` block.

## Effect Block

The main effect block executes whenever the on_action triggers:

```hoi4
on_capitulation = {
    effect = {
        add_war_support = -0.10
        set_country_flag = has_capitulated_once
    }
}
```

Effects run in the on_action's default scope (varies by type - see [On Actions Reference](/scripting/on_actions_reference.md)).

## Random Events

The optional `random_events` block triggers weighted random events:

```hoi4
on_war = {
    effect = {
        # Always execute
    }
    random_events = {
        100 = war_event.1
        50 = war_event.2
        0 = 0  # No-op option
    }
}
```

> [!CRITICAL] Random events require the on_action's default scope to be COUNTRY. On actions with no default scope (`on_startup`) or non-country default scope (`on_naval_invasion`, `on_paradrop`) cannot use `random_events`.

Weights are relative. The event trigger must evaluate to true using the on_action's scope mapping, or the event won't fire even if selected.

Multiple `random_events` blocks can exist in one on_action. The game picks one event from EACH block independently:

```hoi4
on_war = {
    random_events = {
        100 = domestic.1
        50 = domestic.2
    }
    random_events = {
        100 = military.1
        50 = military.2
    }
}
# Triggers one domestic event AND one military event
```

## Timing Constraints

> [!CRITICAL] All on_actions are ignored in history files and bookmark effects. They only fire during active gameplay after the game starts.

- **on_startup:** Fires ONLY on new game creation, NOT on save load
- **on_daily / on_weekly / on_monthly:** Fire during normal gameplay ticks
- **Event-driven:** Fire when the triggering event occurs

The calendar has no leap days - every year is exactly 365 days. `on_weekly` fires when `num_days % 7 == 0`.

## Scope Behavior Patterns

On actions have varying default scopes that determine context:

### Country-Scoped (Most Common)

```hoi4
on_government_change = {
    effect = {
        # ROOT/THIS = country whose government changed
    }
}
```

### No Default Scope

> [!CRITICAL] `on_startup` has NO default scope. Attempting to use country-scoped effects without explicit scoping causes errors.

```hoi4
on_startup = {
    effect = {
        # No scope - must scope manually
        every_country = {
            # Now in country scope
        }
    }
}
```

### Non-Standard Default Scope

**on_naval_invasion** and **on_paradrop:** Default scope is THIS (the invaded state), NOT ROOT:

```hoi4
on_naval_invasion = {
    effect = {
        # THIS = invaded state
        # ROOT is NOT defined
        controller = {
            # Scope into controlling country
        }
    }
}
```

**on_state_control_changed:** Scope mapping is unusual:

```hoi4
on_state_control_changed = {
    effect = {
        # FROM.FROM = the state (not FROM)
        # FROM = new controller
        # ROOT = old controller
    }
}
```

See [On Actions Reference](/scripting/on_actions_reference.md) for complete scope mappings.

## Trigger Cascades

Some on_actions automatically trigger other on_actions as side effects:

### on_government_change → on_ruling_party_change

Changing government ALWAYS triggers both:

```hoi4
set_politics = {
    ruling_party = communism
}
# Fires on_government_change, which fires on_ruling_party_change
```

### on_civil_war_end → on_annex

Civil war conclusion ALWAYS triggers both:

```hoi4
# Civil war ends
# Fires on_civil_war_end
# Then fires on_annex (loser annexed by winner)
```

### start_civil_war → on_government_change (Both Sides)

Starting a civil war triggers `on_government_change` for BOTH the original country and the rebel country:

```hoi4
start_civil_war = {
    ideology = communism
    size = 0.5
}
# Fires on_government_change for original country
# Fires on_government_change for rebel country
```

### on_peaceconference_ended → Multiple Contexts

Also triggered by:

- `white_peace` effect
- Conditional surrender (scripted peace)

Not limited to formal peace conferences.

## Special Scope Variables

Some on_actions create temporary variables:

### on_ruling_party_change

Creates `old_ideology_token` variable containing the previous ruling party ideology:

```hoi4
on_ruling_party_change = {
    effect = {
        # var:old_ideology_token contains previous ideology
        if = {
            limit = {
                check_variable = { old_ideology_token = token:democratic }
            }
            # React to loss of democracy
        }
    }
}
```

### on_unit_leader_promote_from_ranks

Scope mapping is non-standard:

```hoi4
on_unit_leader_promote_from_ranks = {
    effect = {
        # FROM = promoted unit (division)
        # FROM.OWNER = country (not FROM directly)
    }
}
```

### on_operative_detected_during_operation

`FROM.FROM` is the state ONLY if the operation has `selection_target` set:

```hoi4
on_operative_detected_during_operation = {
    effect = {
        # FROM = operation
        # FROM.FROM = state (only if operation used selection_target)
    }
}
```

## Performance Considerations

### Heavy On Actions

**on_daily:** Executes for EVERY country every day (~100-200 executions per day):

```hoi4
on_daily = {
    effect = {
        # Runs 100+ times per day
        # Avoid expensive operations
    }
}
```

> [!CRITICAL] Scoping into another country inside `on_daily` causes duplicate executions - the effect runs once for each country, then again when that country is the active scope. This multiplies execution count significantly.

**on_army_leader_daily:** Runs for every army leader every day (hundreds of executions).

### Optimization Strategy

Use tag-specific variants when possible:

```hoi4
on_daily_GER = {
    effect = {
        # Runs only for Germany - 1 execution per day
    }
}

on_weekly_SOV = {
    effect = {
        # Runs only for Soviet Union weekly
    }
}
```

Tag-specific variants eliminate redundant execution for countries that don't need the logic.

## Non-Working On Actions

These on_actions are defined but non-functional:

- `on_recall_volunteers`: Listed but does nothing
- `on_mio_tech_research_cancelled`: Non-functional (1.13+)
- `on_mio_tech_research_completed`: Non-functional (1.13+)

Do not rely on these for scripting - they will never fire.

## Capitulation Sequencing

Two on_actions fire during capitulation with different timing:

**on_capitulation_immediate:** Fires at the START of capitulation:

- Units still exist
- Equipment not yet transferred
- Territory not yet transferred

**on_capitulation:** Fires MID-PROCESS:

- Units deleted
- Equipment transferred to captors
- Territory being processed

Use `on_capitulation_immediate` to save data before it's destroyed. Use `on_capitulation` to react to the completed state change.

## Peace Conference Exclusivity

Some on_actions fire ONLY in specific contexts:

**on_puppet:** ONLY during peace conferences, NOT when using the `puppet` effect directly.

**on_liberate:** ONLY during peace conferences, NOT when using `release` or `liberate` effects.

**on_release_as_puppet:** ONLY from the peacetime "Occupied Territories" menu, NOT from peace conferences or effects.

This exclusivity means you cannot trigger these on_actions through scripting - they require player/AI interaction with the appropriate game interface.

## Conditional Execution Patterns

### Existence Checks

```hoi4
on_daily = {
    effect = {
        if = {
            limit = { country_exists = GER }
            GER = { 
                # Safe to interact with Germany
            }
        }
    }
}
```

Always check country existence in on_actions that run for all countries, especially when targeting specific tags.

### DLC Gating

```hoi4
on_startup = {
    effect = {
        every_country = {
            if = {
                limit = { has_dlc = "La Resistance" }
                # DLC-specific setup
            }
        }
    }
}
```

### Flag-Based State Tracking

```hoi4
on_war = {
    effect = {
        if = {
            limit = { NOT = { has_country_flag = first_war_processed } }
            set_country_flag = first_war_processed
            # First war logic
        }
    }
}
```

## Best Practices

1. **Minimize on_daily usage:** Prefer event-driven or tag-specific on_actions
2. **Check existence before targeting:** Countries can be annexed/deleted
3. **Avoid scope chaining in on_daily:** Prevents duplicate executions
4. **Use flags for one-time logic:** Prevent repeated execution of same code
5. **Validate scope assumptions:** Not all on_actions have country scope

## Related On Actions

For complete enumeration of all on_actions with scope mappings, see [On Actions Reference](/scripting/on_actions_reference.md).

For effect and scope mechanics, see [Effects](/scripting/effects.md) and [Scopes](/scripting/scopes.md).
