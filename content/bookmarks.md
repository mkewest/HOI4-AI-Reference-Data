---
domain: content
concept: bookmarks
version: 1.14+
requires: [national_focus, ideologies, country_history]
relates: [decisions, states]
---

# Bookmarks

Bookmarks define game start scenarios with specific dates, available countries, and initial conditions. They appear in the scenario selection screen before country selection.

## Bookmark Structure

Bookmarks are defined in `common/bookmarks/*.txt`:

```hoi4
bookmarks = {
    bookmark = {
        name = "SCENARIO_1936_NAME"
        desc = "SCENARIO_1936_DESC"
        date = 1936.1.1.12
        picture = GFX_select_date_1936
        default = yes
        default_country = GER
        
        effect = {
            # Executes after history, before country select
            randomize_weather = 22222
        }
        
        GER = {
            history = "SCENARIO_GER_HISTORY"
            ideology = fascism
            ideas = { autarky militarism }
            focuses = { GER_rhineland GER_anschluss GER_sudetenland }
        }
        
        --- = {
            # Other countries menu entry
            history = "SCENARIO_OTHER_NATIONS"
        }
    }
}
```

### Bookmark Attributes

**name**: Localization key for the scenario name displayed in the UI.

**desc**: Localization key for the scenario description.

**date**: Start date in format `YYYY.MM.DD.HH`. Minimum supported date is 2.1.1.1 (year 2, January 1st, hour 1). Earlier dates require defines overrides for `NGame.START_DATE`, `NGame.END_DATE`, and `NDiplomacy.TENSION_TIME_SCALE_START_DATE`.

**picture**: Sprite reference for the scenario image, typically 180×104 pixels.

**default**: Boolean flag. Exactly one bookmark must have `default = yes` to serve as the initially selected scenario.

**default_country**: Country tag that is pre-selected when entering country selection. The country must have `minor = no` or have a non-default focus tree (see Country Entry section).

**effect**: Effect block executed after history files process but before country selection screen appears. Use `randomize_weather` with a seed value to properly initialize weather systems. Without this, weather may behave incorrectly.

### Single Bookmark Behavior

> [!CRITICAL] If only one bookmark is defined, the game skips bookmark selection entirely and goes straight to country selection. From country selection with a single bookmark, players cannot return to the main menu - they must quit the game. Workaround: Define a second bookmark but hide it through UI modifications.

## Country Entries

Country entries define which nations appear in the scenario and their displayed information:

```hoi4
GER = {
    history = "SCENARIO_GER_HISTORY"
    ideology = fascism
    minor = no
    
    available = {
        # Trigger controlling country availability
        has_dlc = "Required DLC"
    }
    
    ideas = { idea_1 idea_2 idea_3 }
    focuses = { focus_1 focus_2 focus_3 }
}
```

**history**: Localization key for the country's historical background text.

**ideology**: Ideology group identifier (fascism, communism, democratic, neutrality). This is purely cosmetic and affects display of leader portrait, country name, flag, and faction icon. It does not verify against actual history files or modify the game state.

**minor**: Boolean controlling whether the country appears in the main selection or "other countries" menu.

> [!CRITICAL] Countries with `minor = yes` also require a non-default focus tree to appear in country selection. A minor country using the default focus tree will not display at all. Use `minor = no` or assign a custom focus tree.

**available**: Trigger block determining if the country can be selected. Use for DLC requirements or scenario-specific restrictions.

**ideas**: Array of up to 3 idea identifiers. Purely cosmetic display in the UI - does not actually add ideas to the country.

**focuses**: Array of up to 3 focus identifiers. Purely cosmetic display showing example focuses - does not modify actual focus tree or add completion status.

### Multiple Country Definitions

The same country tag can have multiple definitions within one bookmark for DLC variants:

```hoi4
USA = {
    history = "SCENARIO_USA_BASE"
    ideology = democratic
    available = { NOT = { has_dlc = "Man the Guns" } }
}

USA = {
    history = "SCENARIO_USA_MTG"
    ideology = democratic
    available = { has_dlc = "Man the Guns" }
}
```

### Other Countries Entry

The special `---` entry creates a menu item for countries not explicitly listed:

```hoi4
--- = {
    history = "SCENARIO_OTHER_NATIONS"
}
```

## Date History Execution

Date blocks in history files interact with bookmark dates in specific ways:

> [!CRITICAL] Date blocks in history files execute only if the bookmark start date is strictly later than the block's date. A bookmark dated `1937.1.1` will not execute a history block dated `1937.1.1` - only dates strictly after (like `1937.1.2`) trigger execution. For same-date differences, use the bookmark's `effect` attribute instead.

Example:

```hoi4
# In history file:
1937.1.1 = {
    owner = DEF
}

# Bookmark dated 1937.1.1: Block does NOT execute
# Bookmark dated 1937.1.2: Block executes
```

## Difficulty Settings

Difficulty settings are defined in `common/difficulty_settings/*.txt` and provide slider-based modifiers for specific countries:

```hoi4
difficulty_setting_name = {
    key = "DIFFICULTY_SETTING_NAME"
    
    modifier = static_modifier_name
    
    countries = { GER ITA JAP }
    
    multiplier = {
        position_1 = 0.5
        position_2 = 0.75
        position_3 = 1.0
        position_4 = 1.25
        position_5 = 1.5
    }
}
```

**key**: Localization key for the setting name.

**modifier**: Reference to a static modifier that scales by the multiplier value.

**countries**: Array of country tags affected by this setting.

**multiplier**: Five positions defining scaling values for the slider. Position 3 (1.0) is typically the baseline.

> [!CRITICAL] If `difficulty_settings/*.txt` contains no valid entries, the game rules menu cannot open. At least one valid difficulty setting must exist.

This system is independent from player difficulty (Very Easy through Very Hard), despite similar naming. Player difficulty applies `diff_*_player` and `diff_*_ai` static modifiers to all countries simultaneously.

## Game Rules

Game rules are defined in `common/game_rules/*.txt` and provide toggleable gameplay modifications:

```hoi4
rule_name = {
    name = "RULE_NAME_LOC"
    group = "RULE_GROUP"
    icon = GFX_rule_icon
    
    required_dlc = "DLC Name"
    exclude_dlc = "Other DLC Name"
    
    default = {
        name = default_option
        text = "OPTION_DEFAULT"
        desc = "OPTION_DEFAULT_DESC"
    }
    
    option = {
        name = alternative_option
        text = "OPTION_ALT"
        desc = "OPTION_ALT_DESC"
        allow_achievements = no
    }
}
```

**name**: Localization key for the rule name.

**group**: Category identifier for organizing rules in the UI.

**icon**: Sprite reference for the rule icon.

**required_dlc**: If specified DLC is not enabled, the rule is not created (not just hidden).

**exclude_dlc**: If specified DLC is enabled, the rule is not created.

**default**: Option block that serves as the default selection. Required.

**option**: Additional option blocks. Repeatable.

### Option Attributes

**name**: Internal identifier for the option.

**text**: Localization key for the option name displayed in UI.

**desc**: Localization key for the option description.

**allow_achievements**: Boolean controlling achievement eligibility. In mods, this is ineffective due to checksum mismatch regardless of value.

> [!CRITICAL] If `game_rules/*.txt` contains no valid entries, the game rules menu cannot open. At least one valid game rule must exist. Mod-created rules with `allow_achievements = yes` have no effect on achievement eligibility due to automatic checksum mismatch.

### Game Rule Trigger

The `has_game_rule` trigger checks active game rule selections:

```hoi4
has_game_rule = {
    rule = rule_name
    option = alternative_option
}
```

## Player Difficulty

Player difficulty provides five preset difficulty levels that apply static modifiers to all countries:

**Player modifiers**: `diff_very_easy_player`, `diff_easy_player`, `diff_normal_player`, `diff_hard_player`, `diff_very_hard_player`

**AI modifiers**: `diff_very_easy_ai`, `diff_easy_ai`, `diff_normal_ai`, `diff_hard_ai`, `diff_very_hard_ai`

These modifiers are defined in `common/modifiers/*.txt` and apply globally based on the player's difficulty selection.

## UI Configuration

The bookmark UI is defined in `interface/frontendgamesetupview.gui` using two primary grids:

**bookmarks_grid**: Displays available scenarios
**countries_grid**: Displays selectable countries

Custom UI modifications can alter bookmark and country display without changing the underlying bookmark definitions.

## Related Defines

- `NGame.START_DATE`: Minimum allowed game start date
- `NGame.END_DATE`: Maximum allowed game end date  
- `NDiplomacy.TENSION_TIME_SCALE_START_DATE`: Date when tension calculations begin

These defines must be overridden when using dates before year 2.
