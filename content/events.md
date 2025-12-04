---
domain: content
concept: events
version: 1.14+
requires: [triggers, effects, scopes]
relates: [localization, on_actions]
---

# Events

Events are scripted occurrences that present choices to players or execute effects automatically. HOI4 supports five event types with different scoping rules and firing mechanisms.

## Event Types

Events are defined in `events/*.txt` using UTF-8 encoding. Each event type operates in a specific scope:

**country_event**: Executes in country scope. This is the standard event type for national decisions and storylines.

**news_event**: Functionally identical to country_event with country scope. The distinction is purely semantic for organizational purposes.

**state_event**: Dual-scope event accepting effects for both country and state scopes. When an effect is valid in both scopes (such as `add_manpower`), country scope always takes priority. State events appear visually identical to country events in the UI, making them difficult to distinguish. Using event targets to explicitly pass state scope is recommended over relying on dual-scope behavior.

**unit_leader_event**: Dual-scope event for country and unit_leader scopes. Country scope has priority on overlapping effects.

**operative_leader_event**: Dual-scope event for country and operative_leader scopes. Country scope has priority on overlapping effects.

## ID System

Events use a namespaced ID system to prevent collisions between mods and content packs.

### ID Format

Event IDs follow the format `namespace.integer`, where namespace is a string token and the integer portion identifies the specific event within that namespace. The namespace declaration must appear outside any event block:

```hoi4
add_namespace = my_mod

country_event = {
    id = my_mod.1
    ...
}
```

Files load in ASCII character order of filename, which determines namespace order. The first declared namespace gets internal ID 10, incrementing by 1 for each subsequent namespace. If the `add_namespace` line is missing, the game generates a "Malformed token" error on the id line.

### Internal ID Calculation

The game converts namespaced IDs to internal integers using the formula:

```
internal_id = (namespace_order * 100000) + numeric_id
```

Where namespace_order starts at 10 for the first declared namespace. This means:
- First namespace (order 10): IDs 1000000-1099999
- Second namespace (order 11): IDs 1100000-1199999
- And so on...

> [!CRITICAL] Event IDs with numeric portions ≥100000 encroach into the next namespace's range, causing duplicate internal ID collisions. Keep numeric IDs between 0-99999.

> [!CRITICAL] Non-integer values after the last dot convert to 0. This means `my_mod.test`, `my_mod.foo`, and `my_mod.0` all become the same internal ID, creating collision risks across multiple events.

When the game reports "Duplicate internal ID error 50", the number 50 refers to the event type in the internal database (50 = country_event). Other numbers indicate different database entry types.

## Event Attributes

### Required Attributes

**id**: The namespaced identifier for the event. Format: `namespace.integer`

### Display Attributes

**title**: Localization key for the event title. Supports conditional localization to change text based on triggers.

**desc**: Localization key for the event description. Supports conditional localization.

**picture**: Event window sprite reference in format `GFX_<sprite>`. Sprites are defined in `interface/*.gfx` files.

### Trigger System

**trigger**: Trigger block that determines when auto-fire events can occur. The game checks this trigger every 20 days, not daily. Tight date bounds like `date > 1936.1.1 AND date < 1936.1.3` risk never firing if the 20-day check window skips over the valid period entirely. Single date triggers like `date > 1936.1.1` fire anywhere from the 2nd to the 21st day after the trigger becomes true, not on an exact date.

**mean_time_to_happen**: Defines the median time until the event fires after its trigger becomes true. This is not a mean or average despite the name - it represents the 50th percentile. Uses MTTH blocks with time units and modifiers:

```hoi4
mean_time_to_happen = {
    days = 30
    months = 2  # Exactly 30 days, not calendar months
    years = 1   # Exactly 365 days, no leap days
    
    modifier = {
        factor = 0.5  # Multiplies time (0.5 = twice as fast)
        has_war = yes
    }
    
    modifier = {
        add = -10  # Adds/subtracts days
        has_idea = aggressive_expansion
    }
}
```

Months convert to exactly 30 days and years to exactly 365 days regardless of actual calendar. Modifiers evaluate sequentially in definition order. Using `factor = 0` causes early termination and stops further evaluation. MTTH blocks support variables in arguments. The system only fires when the trigger is true - when the trigger becomes false, the event reverts to 20-day trigger checks without MTTH evaluation.

> [!CRITICAL] Combining `is_triggered_only = yes` with `mean_time_to_happen` creates a contradictory configuration error (manual-only vs auto-fire). Events with `is_triggered_only = no`, `fire_only_once = no`, and MTTH ≤1 day generate a "Trigger every day" warning.

**is_triggered_only**: Boolean that disables automatic firing. When true, the event can only fire through explicit effect commands.

**fire_only_once**: Boolean that prevents the event from firing more than once globally across all countries. This is checked globally, not per-country. When combined with `major = yes`, fire_only_once takes priority and the event fires for only one country total.

### Major Event Behavior

**major**: Boolean that causes the event to fire for all countries when triggered. News events are not automatically major despite the name - you must specify `major = yes` explicitly. Countries other than the original recipient ignore the event's trigger block entirely.

**show_major**: Trigger block that filters which additional countries receive a major event beyond the original recipient. This trigger is ignored for the original recipient - it only affects the additional recipients from major event propagation.

**fire_for_sender**: Boolean controlling whether the country executing the event effect receives the event. Defaults to true.

### Effect Timing

**immediate**: Effect block that executes before the event window appears and before AI evaluates event options. This runs before AI processes the event for other countries in major events, making it useful for setting flags that affect MTTH calculations in subsequent major event instances.

**after**: Effect block that executes after an option is selected. Added in patch 1.16.9.

Both immediate and after blocks appear in tooltips after the event description. Use `hidden_effect` to execute effects without showing them in tooltips.

**timeout_days**: Integer defining days until the first option auto-selects if the player doesn't choose. Does not apply to AI.

**hidden**: Boolean that causes the first option to auto-select immediately without displaying the event window. No title or description is required for hidden events. Hidden events are useful for delayed effect execution while preserving FROM scope, which scripted effects don't maintain.

**minor_flavor**: Boolean allowing players to disable the event popup through game settings.

## Event Options

Options define player choices within events. Each event must have at least one option:

```hoi4
option = {
    name = my_mod.1.a
    
    trigger = {
        # Visibility condition
    }
    
    ai_chance = {
        base = 50
        modifier = {
            factor = 2
            has_war = yes
        }
    }
    
    # Effects execute here
    add_political_power = 50
}
```

**name**: Localization key for the option button text. Cannot use conditional localization. Workaround: Create separate options with triggers to display different text.

**trigger**: Determines option visibility. Evaluated only when the event fires, not continuously. Invisible options remain invisible until the event refires with different conditions.

**ai_chance**: MTTH block controlling AI selection probability. Defaults to 1. The AI rolls d100 and selects options using probability-proportional-to-size sampling. This means the minimum effective probability is 1% - you cannot get more granular. If all ai_chance values are 0, the first option is chosen deterministically, not randomly. AI selection is deterministic and consistent across save/load based on seed, game time, country ID, and unit_leader ID.

**original_recipient_only**: Boolean for major events. When true, only the original recipient can see this option.

## Firing Events

Events fire through effect commands with optional parameters:

### Basic Syntax

```hoi4
country_event = my_mod.1

# Or with parameters:
country_event = {
    id = my_mod.1
    days = 5
    random_days = 3
}
```

### Delay Parameters

All delay parameters are cumulative and sum together:

- **hours**: Integer hours of delay
- **days**: Integer days of delay  
- **months**: Exactly 30 days (not calendar months)
- **random_hours**: Random value from [0, n] hours
- **random_days**: Random value from [0, n] days

Example: `days = 5`, `random_days = 3`, `hours = 12` creates a delay between 5 days 12 hours and 8 days 12 hours.

Delayed event triggers evaluate when the event would fire, not when the effect executes.

### Special Event Types

**state_event**: Requires the `trigger_for` parameter to specify scope. Valid values are TAG (specific country), `controller` (current controller), `owner` (original owner), or `occupied` (occupying country).

```hoi4
state_event = {
    id = my_mod.1
    trigger_for = controller
}
```

**operative_leader_event**: Supports scoping parameters `originator`, `recipient`, `set_root`, `set_from`, and `set_from_from` to control scope flow.

## Scope Behavior

Event scoping differs from normal effect scoping in important ways:

When an effect block fires an event, scopes shift forward:
- Effect's ROOT becomes event's FROM
- Effect's FROM becomes event's FROM.FROM  
- Effect's FROM.FROM becomes event's FROM.FROM.FROM

Event targets defined in the effect block port into the event scope normally.

On_action random_events have no automatic scope porting - they use only the on_action's scoping context.

FROM interpretation varies by context and is not always "sender". On_actions may add additional scopes, and decision targets use different FROM assignments than effect-fired events.

## Nonexistent Country Handling

When an effect fires an event for a nonexistent country, the event enters a backlog queue and all timers freeze. Timers only resume counting down after the country is created. For example, firing an event for Bahrain (BHR) with a 1-day delay when BHR doesn't exist causes the event to fire 1 day after BHR's creation, regardless of how much time passes in between. This applies to major event original recipients as well.

## Localization Requirements

Event localization files must follow strict formatting rules:

> [!CRITICAL] Localization files must end with `_l_english.yml` (lowercase L, not uppercase i) and use UTF-8-BOM encoding, not plain UTF-8. The first line must be exactly `l_english:` with no other content.

Option names cannot use conditional localization. To achieve dynamic option text, create separate options with visibility triggers.

## Event-Country Assignment

Events are not assigned to specific countries based on namespace or filename - these are purely organizational. When checking auto-fire triggers, the game evaluates all countries in taglist order. A trigger without country-specific checks fires for the first country where the trigger evaluates true, which is usually GER (Germany) due to taglist ordering.

## Related Defines

- `NFocus.FOCUS_POINT_DAYS`: Affects event timing when fired from focus completion_reward
- `NAI.FOCUS_TREE_CONTINUE_FACTOR`: Affects AI focus selection, which may trigger events
