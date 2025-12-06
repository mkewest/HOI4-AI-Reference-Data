---
domain: content
concept: decisions
version: 1.14+
requires: [triggers, effects, modifiers]
relates: [states, events, national_focus]
---

# Decisions

Decisions represent player choices and AI actions outside the event system. They appear in the decisions menu and support three distinct types: standard decisions, targeted decisions, and missions.

## Decision Categories

Decision categories are containers defined in `common/decisions/categories/*.txt`:

```hoi4
decision_category_name = {
    icon = GFX_category_icon
    priority = 10
    
    allowed = {
        # Trigger controlling category availability
    }
    
    visible = {
        # Trigger controlling category visibility
    }
    
    picture = GFX_category_background
    
    scripted_gui = custom_gui_name
}
```

Categories organize decisions in the UI and provide shared visibility/availability context. Localization keys are `<id>` for the name and `<id>_desc` for the description.

## Standard Decisions

Standard decisions are the basic decision type, defined in `common/decisions/*.txt`:

```hoi4
my_decision = {
    icon = GFX_decision_icon
    
    allowed = {
        # One-time check at game start
    }
    
    available = {
        # Continuous availability check
    }
    
    visible = {
        # Visibility check
    }
    
    fire_only_once = yes
    
    cost = 50  # Political power
    
    days_remove = 30
    days_re_enable = 60
    
    modifier = {
        # Applied during timer
    }
    
    ai_will_do = {
        # MTTH block
    }
    
    complete_effect = {
        # Executes when selected
    }
    
    remove_effect = {
        # Executes when timer ends
    }
    
    timeout_effect = {
        # Executes on timeout
    }
}
```

### Availability and Visibility

**allowed**: Trigger checked only at game start. Use for immutable conditions like DLC requirements or permanent country restrictions.

**available**: Trigger checked continuously. Determines if the decision can be taken.

**visible**: Trigger controlling decision visibility in the UI.

**fire_only_once**: Boolean preventing the decision from appearing after first use. Can combine with `days_re_enable` to make it fire once per cooldown period.

### Cost System

**cost**: Political power cost. Standard numeric cost.

**custom_cost_trigger**: Trigger block for dynamic cost display. Does not actually cost anything - you must manually subtract resources in `complete_effect`.

**custom_cost_text**: Localization key for custom cost display. Requires three localization keys: `<key>`, `<key>_blocked`, and `<key>_tooltip`.

> [!CRITICAL] Custom cost doesn't actually cost resources automatically. You must subtract the cost manually in `complete_effect`. Custom cost is incompatible with the regular `cost` attribute. AI ignores custom cost for PP calculations unless `ai_hint_pp_cost` is set with a constant value (cannot be variable).

### Timer System

**days_remove**: Integer days until the decision completes or removes. Value of -1 creates a permanent timer that never expires.

**days_re_enable**: Integer days before the decision can be taken again after completion.

> [!CRITICAL] `complete_effect` executes when the decision is selected (starting the timer), not when it completes. `remove_effect` executes when the timer ends or when `remove_trigger` becomes true. The `visible` trigger does not cancel active timers by default - use `cancel_trigger` to stop timers based on visibility.

**cancel_trigger**: Trigger that cancels an active timer.

**cancel_if_not_visible**: Boolean that adds all `visible` triggers to `cancel_trigger` automatically.

**remove_trigger**: Trigger that causes early timer completion when true. Executes `remove_effect`.

**timeout_effect**: Effect block executed if the timer expires naturally without `remove_trigger` firing.

**modifier**: Modifier block applied while the timer is active.

### War Warnings

**war_with_on_complete**: Country tag array warning that taking this decision may cause war. Only alerts AI and doesn't actually declare war.

**war_with_on_remove**: Country tag array warning that decision removal may cause war.

> [!CRITICAL] `war_with_on_complete` and `war_with_on_remove` do not work with targeted decisions. Use `war_with_target_on_complete` and `war_with_target_on_remove` variants instead for targeted decisions.

### Random Seed

**fixed_random_seed**: Boolean controlling random outcome determinism. Defaults to true, causing `random_list` and `random_owned_controlled_state` to pick the same choice every time based on seed determined at game start. Set to `no` for different outcomes on each use.

## Targeted Decisions

Targeted decisions allow selecting a specific country or state as the target:

```hoi4
my_targeted_decision = {
    icon = GFX_decision_icon
    
    target_trigger = {
        FROM = {
            # FROM is the potential target
        }
    }
    
    target_root_trigger = {
        # ROOT scope additional filters
    }
    
    target_array = scope_name  # Alternative to target_trigger
    
    targets = { TAG1 TAG2 TAG3 }  # Alternative explicit target list
    
    state_target = yes  # Or state_target = any
    
    on_map_mode = map_only  # Or map_and_decisions_view
    
    target_non_existing = yes
    
    # ... standard decision attributes
}
```

### Target Selection

**target_trigger**: Trigger block where FROM represents potential targets. Filters which countries/states can be targeted.

**target_root_trigger**: Additional trigger in ROOT scope for filtering.

**target_array**: Scope reference (like `enemies` or `allies`) to automatically populate targets.

**targets**: Explicit array of country tags to use as targets.

**state_target**: Boolean or `any` value enabling state targeting instead of country targeting. Valid values are `yes` (owned states) or `any` (all states). When combined with explicit `targets` or `target_array`, only `state_target = yes` or `state_target = any` work.

**on_map_mode**: Controls map icon display. Values: `map_only` (icon only on map mode) or `map_and_decisions_view` (icon always visible when decision menu open).

**target_non_existing**: Boolean allowing targeting of non-existent countries.

### State Targeting

For state-targeted decisions, icons appear over states when the decision menu is open. Continent values for filtering are: `europe`, `africa`, `north_america`, `south_america`, `asia`, `oceania`, `middle_east`.

## Missions

Missions are time-limited objectives with special activation and completion mechanics. Defined with `is_good = yes`:

```hoi4
my_mission = {
    icon = GFX_mission_icon
    is_good = yes
    
    activation = {
        # Checked daily for mission appearance
    }
    
    available = {
        # Instant disappearance when false (defaults to always true)
    }
    
    visible = {
        # Has NO EFFECT in missions - use activation instead
    }
    
    days_mission_timeout = 365
    
    timeout_effect = {
        # Executes on timeout
    }
    
    complete_effect = {
        # Executes on completion
    }
    
    # ... other decision attributes
}
```

> [!CRITICAL] The `visible` attribute has no effect in missions. Use `activation` instead to control when missions appear. The `activation` trigger is checked daily, not every frame. The `available` trigger defaults to "always true" in missions, causing instant disappearance if not specified. Missions vanish immediately when `available` becomes false.

**activation**: Trigger checked daily to determine if the mission should appear. This replaces the role of `visible` for missions.

**days_mission_timeout**: Integer days until the mission expires if not completed.

**is_good**: Boolean. Must be `yes` for missions (good outcomes) or `no` for anti-missions (bad outcomes to avoid).

The `activate_mission` effect bypasses both `allowed` and `activation` checks, forcing a mission to appear immediately.

## AI Behavior

**ai_will_do**: MTTH block controlling AI likelihood of taking the decision. The base value starts at 1. Operations apply in order: base operations first, then factors, then adds.

Temp variables in MTTH blocks require the value-modifying argument to come after the variable definition for proper evaluation.

## Localization

Standard localization keys:

- `<decision_id>`: Decision name
- `<decision_id>_desc`: Decision description

For custom cost, three keys required:

- `<custom_cost_text>`: Cost display
- `<custom_cost_text>_blocked`: Blocked state text
- `<custom_cost_text>_tooltip`: Tooltip explanation
