---
domain: content
concept: national_focus
version: 1.14+
requires: [triggers, effects, modifiers]
relates: [ideas_core, ai_strategy]
---

# National Focus System

National focuses represent a country's strategic priorities and long-term planning. The system consists of focus trees (containers), individual focuses (nodes), and continuous focuses (persistent modifiers).

## Focus Trees

Focus trees are defined in `common/national_focus/*.txt` using UTF-8 encoding. Each tree defines a complete focus progression for one or more countries.

### Focus Tree Attributes

**id**: String identifier for the tree, which also serves as the localization key for the tree's name.

**country**: MTTH block that determines which countries receive this focus tree. This evaluation occurs before game start and essentially never refreshes during gameplay. The only exception is dynamic countries (countries created during gameplay), which re-evaluate tree assignment upon creation. In debug mode, saving over a focus tree file forces a refresh of tree assignments.

**default**: Boolean flag. Exactly one focus tree globally must have `default = yes` to serve as the fallback for countries without specific assignments.

**reset_on_civilwar**: Boolean controlling civil war behavior. The original country always keeps its tree and all progress regardless of this value. The revolter country re-evaluates tree assignment. If the revolter gets the same tree, all completed focuses (including current progress percentage) copy to the revolter. If the revolter gets a different tree, all progress is lost. The original country never pauses or cancels its current focus during civil war.

**shared_focus**: String reference to shared focus IDs defined at root level. This includes all focuses prerequisite-connected to the specified shared focus.

**continuous_focus_position**: Coordinates in pixels for continuous focus palette placement. Defaults to `{x = 50 y = 1000}`. If specified as `{x = 0 y = 0}`, resets to the palette's default position, allowing national trees to override palette positioning.

**initial_show_position**: Defines initial camera position when opening the tree. Accepts either a focus ID or x/y coordinates.

**focus**: Focus definition blocks (see Focus Attributes section).

**shortcut**: Defines camera shortcut buttons with attributes `name`, `target`, `scroll_wheel_factor`, and `trigger`.

**inlay_window**: References an inlay window defined in `common/focus_inlay_windows/*.txt` with attributes `id` and `position`.

## Focus Attributes

Individual focuses are defined within focus_tree blocks:

### Positioning

**id**: String identifier for the focus. Convention is to prefix with country tag: `TAG_focusname`. This prevents conflicts when multiple trees use the same focus name.

> [!CRITICAL] Duplicate focus IDs across different trees break prerequisite line rendering. Lines may point to empty spaces or wrong positions, and path-generating algorithms use incorrect turn sprites. Always prefix focus IDs with country tags.

**x**: Integer defining horizontal position in 96-pixel units. Required.

**y**: Integer defining vertical position in 130-pixel units. Required.

**relative_position_id**: String reference to another focus ID. Makes this focus position relative to the referenced focus.

**offset**: Block with `x`, `y`, and optional `trigger` attributes. Evaluates on tree load to shift focus position dynamically.

### Visual Appearance

**icon**: Sprite reference in format `GFX_focus_*`. Requires a corresponding shine sprite named exactly `GFX_focus_*_shine` (regular name plus `_shine`). If the regular sprite is undefined, Goal_unknown.png displays. If the shine sprite is undefined, Goal_unknown.png displays for the shine effect as well.

> [!CRITICAL] If the texturefile path is wrong (incorrect folder or filename), the focus icon appears fully transparent. Always use forward slashes (/) in paths, not backslashes (\) - backslashes may cause the game to fail reading the folder entirely.

**text_icon**: String reference for inline text icons in focus tooltips.

**search_filters**: Array of filter tokens. Sprites must be defined as `GFX_FOCUS_FILTER_*`. Localization keys follow the same pattern: `FOCUS_FILTER_*`. Priority ordering is defined globally:

```hoi4
search_filter_prios = {
    FOCUS_FILTER_POLITICAL
    FOCUS_FILTER_RESEARCH
    FOCUS_FILTER_INDUSTRY
}
```

### Progression Control

**cost**: Float representing completion time in multiples of 7 days (default unit). For example, `cost = 10` takes 70 days.

**prerequisite**: Block defining required completed focuses. Can be repeated to create OR logic. The logic structure is OR within a single prerequisite block, AND between multiple prerequisite blocks:

```hoi4
prerequisite = { focus = A focus = B }  # A OR B
prerequisite = { focus = C }            # AND C

# This requires: (A OR B) AND C
```

> [!CRITICAL] Prerequisites must be placed above (lower Y value) the focus requiring them for correct prerequisite line rendering. 90-degree turn sprites break if the prerequisite is not above the dependent focus. The prerequisite system cannot represent complex boolean logic like `A OR (B AND C)`, negation, or other arrangements. Workaround: Use `has_completed_focus` in the `available` block with `custom_trigger_tooltip` for player clarity.

**mutually_exclusive**: Block defining focuses that cannot coexist with this focus. Can be repeated for multiple mutual exclusion sets.

**allow_branch**: Trigger block evaluated only when the focus tree first loads. If false, the focus becomes unavailable. Child focuses inherit this unavailable status. Exception: A child focus with its own `allow_branch` only checks its own condition, ignoring parent conditions. This means children with `allow_branch` must include the parent's conditions if you want them enforced.

### Availability and Bypass

**available**: Trigger block determining if the focus can be selected. Checked when attempting to select the focus.

**available_if_capitulated**: Boolean allowing focus selection while capitulated. Defaults to false.

**bypass**: Trigger block that allows skipping the focus without rewards. When true, the focus marks as complete without executing `completion_reward`. Use `bypass_effect` to provide alternate rewards for bypassed focuses.

**bypass_effect**: Effect block executed when a focus is bypassed.

**enable_automatic_bypass**: Boolean controlling automatic bypass checking. Defaults to true.

**bypass_if_unavailable**: Boolean that bypasses the focus if it becomes unavailable.

### Cancellation

**cancelable**: Boolean allowing manual cancellation. Defaults to true.

> [!CRITICAL] The `select_effect` attribute automatically makes a focus impossible to cancel manually, overriding `cancelable = yes`. Only `cancelable = no` without `select_effect` prevents manual cancellation. If a focus has `select_effect`, setting `cancelable = yes` has no effect.

**cancel**: Trigger block that forcibly cancels the focus when true.

**cancel_if_invalid**: Boolean that cancels the focus if `available` becomes false. Defaults to true.

**continue_if_invalid**: Boolean that allows the focus to continue even if `available` becomes false. Defaults to false.

If both `cancel_if_invalid` and `continue_if_invalid` are false, the focus pauses when `available` becomes false. The `gain_focus` modifier remains active, costing 1 PP/day while paused.

### Completion and Rewards

**completion_reward**: Effect block executed when the focus completes. This executes before the focus is marked complete internally.

> [!CRITICAL] During `completion_reward` execution, `has_completed_focus` returns FALSE for the currently completing focus. The focus is not marked complete until after the effect block finishes. Workarounds: (1) Use country flags set in completion_reward, (2) Fire a hidden event with no delay (executes after focus completion), or (3) Use `load_focus_tree` with `keep_completed = yes` to force completion status.

**complete_tooltip**: Effect block that overrides the tooltip for `completion_reward`. The actual effects in `completion_reward` still execute - this only changes the displayed tooltip.

**select_effect**: Effect block executed when the focus is selected (not on completion). Prevents manual cancellation regardless of `cancelable` value.

### Dynamic Content

**dynamic**: Boolean enabling dynamic localization and icons through scripted_loc and dynamic icon systems.

### AI Behavior

**ai_will_do**: MTTH block controlling AI focus selection priority. Defaults to 1. AI selection uses this only if no AI strategy plan specifies a focus order. The AI generates a random value between 0 and the `ai_will_do` value for each available focus. If a prerequisite was just completed, this value multiplies by `NAI.FOCUS_TREE_CONTINUE_FACTOR` (encouraging same-branch continuation). If an AI strategy plan has focus_factors, this value multiplies by the specified factor. The AI picks the focus with the highest generated value. Values at or below 0 cause the AI to select continuous focus or nothing.

Low `ai_will_do` values are less likely than intuition suggests due to this random roll algorithm.

**historical_ai**: Trigger block for historical AI behavior. If false, historical AI won't select this focus.

**will_lead_to_war_with**: Country tag that this focus may cause war with. Informs AI decision-making but doesn't automatically declare war.

## Shared Focuses

Shared focuses are defined at root level (outside focus_tree blocks) and included in multiple trees:

```hoi4
shared_focus = {
    id = shared_research_bonus
    x = 5
    y = 0
    cost = 5
    # ... other attributes
}

focus_tree = {
    id = generic_tree
    shared_focus = shared_research_bonus
    # ... tree-specific focuses
}
```

The `shared_focus` attribute in a focus tree includes all focuses prerequisite-connected to the specified shared focus.

> [!CRITICAL] Referencing a non-existing shared focus crashes the game on main menu load. Having only shared focuses with no tree-specific focuses also crashes. Every tree must have at least one non-shared focus.

## Joint Focuses

Joint focuses allow multiple countries to work on the same focus simultaneously. Defined at root level, added in version 1.13:

```hoi4
joint_focus = {
    id = joint_invasion_plan
    # ... standard focus attributes
    
    joint_trigger = {
        # Evaluated for each country
    }
    
    completion_reward = {
        # Executes for ALL joint countries
    }
    
    completion_reward_joint_originator = {
        # Executes only for completing country
    }
    
    completion_reward_joint_member = {
        # Executes only for other joint countries
    }
}
```

## Continuous Focuses

Continuous focuses are persistent modifiers defined in `common/continuous_focus/*.txt`. They unlock when a country completes a threshold number of regular focuses (defined by `NFocus.MIN_FOCUSES_FOR_CONTINUOUS`).

### Continuous Focus Palettes

Palettes contain multiple continuous focuses organized by category:

```hoi4
continuous_focus_palette = {
    id = my_palette
    country = { # MTTH block }
    default = yes
    reset_on_civilwar = yes
    
    continuous_focus = {
        id = stability_effort
        icon = GFX_continuous_stability
        
        available = {
            # Visibility trigger (checked daily)
        }
        
        enable = {
            # Selection trigger
        }
        
        modifier = {
            # Applied while active
            stability_factor = 0.1
        }
        
        idea = {
            # Idea granted while active (mutually exclusive with modifier)
        }
        
        select_effect = {
            # Executed on activation
        }
        
        cancel_effect = {
            # Executed on deactivation
        }
        
        daily_cost = 0.5  # PP per day
        
        ai_will_do = {
            # MTTH block
        }
        
        supports_ai_strategy = strategy_name
    }
}
```

The `available` trigger controls visibility and is checked daily, not every frame like UI `visible` attributes. The `enable` trigger controls whether the AI can select this continuous focus.

## Focus Tree Refreshing

Dynamic focus tree modifications require special handling:

> [!CRITICAL] Using `mark_focus_tree_layout_dirty` in `completion_reward` won't work properly because the focus is not marked complete yet. Solution: Fire a hidden event immediately (no delay) with `mark_focus_tree_layout_dirty` in the event effect, or use `load_focus_tree` with `keep_completed = yes` first to force completion status before calling the layout refresh.

## Titlebar Styles

Custom titlebar styles are defined in focus tree files:

```hoi4
titlebar_style = {
    name = my_custom_style
    default = GFX_default_sprite
    unavailable = GFX_unavailable_sprite
    completed = GFX_completed_sprite
    available = GFX_available_sprite
    current = GFX_current_sprite
}
```

## Related Defines

- `NFocus.FOCUS_POINT_DAYS`: Days per cost point (default 7)
- `NFocus.FOCUS_PROGRESS_PEACE`: Daily progress percentage at peace
- `NFocus.FOCUS_PROGRESS_WAR`: Daily progress percentage at war
- `NFocus.MIN_FOCUSES_FOR_CONTINUOUS`: Number of regular focuses required to unlock continuous focuses
- `NAI.FOCUS_TREE_CONTINUE_FACTOR`: AI same-branch continuation bonus multiplier
