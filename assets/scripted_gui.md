---
domain: assets
concept: scripted_gui
version: 1.14+
requires: [interface, localisation]
relates: [effects, triggers_core, scopes]
---

# Scripted GUI System

Scripted GUI links interface elements to game logic through trigger-based visibility, effect-based interactions, and dynamic content generation. Files are defined in `common/scripted_guis/*.txt` with the folder name requiring plural form (`scripted_guis`, not `scripted_gui`).

## Window Assignment

### Container Targeting

Scripted GUI binds to interface containers through the `window_name` attribute:

```hoi4
scripted_gui = {
    example_gui = {
        window_name = "example_window"
        context_type = player_context
    }
}
```

> [!CRITICAL] Only independent `containerWindowType` elements (defined at root level in interface files) can be assigned to `window_name`. Nested containers cannot have scripted GUI directly assigned. However, scripted GUI effects and triggers propagate through the entire container tree, affecting all nested elements within the assigned parent.

The named container must exist in interface files. When a scripted GUI is assigned, it controls visibility, interactivity, and dynamic properties for all elements in that container hierarchy.

## Parent Window Integration

Scripted GUI containers can embed within base game UI using parent window references.

### Token-Based Placement

Use `parent_window_token` to attach to predefined UI locations:

```hoi4
scripted_gui = {
    topbar_element = {
        window_name = "custom_topbar_window"
        parent_window_token = top_bar
    }
}
```

Available tokens: `top_bar`, `decision_tab`, `technology_tab`, `trade_tab`, `construction_tab`, `production_tab`, `deployment_tab`, `logistics_tab`, `diplomacy_tab`, `national_focus`, `politics_tab`, `selected_country_view`, `selected_state_view`, `selected_country_view_info`, `selected_country_view_diplomacy`, `army_ledger`, `navy_ledger`, `civilian_ledger`, `air_ledger`, `tech_infantry_folder`, `tech_support_folder`, `tech_armor_folder`, `tech_artillery_folder`, `tech_land_doctrine_folder`, `tech_naval_folder`, `tech_naval_doctrine_folder`, `tech_air_techs_folder`, `tech_air_doctrine_folder`, `tech_electronics_folder`, `tech_industry_folder`.

The `top_bar` token has lower draw order than popup menus, causing GUI to render behind focus selection, politics tab, and other overlays. Creating an "anchor" container inside base game UI and using it as parent places scripted GUI between background and foreground elements. Note that `top_bar` covers the entire screen despite its name - it doesn't clip GUI to the topbar region.

### Name-Based Placement

Use `parent_window_name` to attach to specific containers by name:

```hoi4
scripted_gui = {
    nested_element = {
        window_name = "custom_nested_window"
        parent_window_name = "base_game_container_instance"
    }
}
```

Nested containers require `_instance` suffix when referenced: a nested container named `nested_container` is referenced as `nested_container_instance`. This syntax is mandatory for nested containers but does not apply to independent containers.

> [!CRITICAL] The `parent_window_name` attribute cannot be used with `gridBoxType` containers. GridBox layouts are incompatible with parent window name targeting.

## Context System

### Context Types

The `context_type` attribute determines default scope and visibility behavior:

**player_context**: Default scope is player country. GUI always visible.

**selected_country_context**: Default scope is currently selected country. GUI hidden when no country selected. AI evaluates this context for every country unless restricted with triggers, potentially impacting performance.

**selected_state_context**: Default scope is currently selected state. GUI hidden when no state selected. AI evaluates for every state unless restricted.

**decision_category**: Embeds GUI in decision category description. Temporary data structures may not work correctly in this context.

**diplomatic_action**: Links to `common/scripted_diplomatic_actions/*.txt` definitions.

**national_focus_context**: Scope is the target country owning the focus.

**country_mapicon**: Displays next to every country on the map.

**state_mapicon**: Displays next to every state on the map.

### Scope Behavior

ROOT always equals player country in all contexts, but DEFAULT scope varies by `context_type`. PREV refers to default scope when it differs from ROOT.

For example, in `selected_country_context`, ROOT is player country but the default scope is the selected country. This enables comparisons between player and selected country: `THIS` refers to selected country, `ROOT` refers to player.

## Effects and Triggers

### Click Effects

Element interactions trigger effects using `<element>_<modifiers>_click` syntax:

```hoi4
scripted_gui = {
    button_gui = {
        window_name = "button_window"
        
        example_button_click = {
            add_political_power = 10
        }
        
        example_button_shift_click = {
            add_political_power = 50
        }
        
        example_button_control_alt_click = {
            add_political_power = 100
        }
    }
}
```

Available modifiers: `right`, `alt`, `control`, `shift`. Modifiers can be combined (e.g., `control_shift_click`). Modifier order in the key name doesn't matter.

### Visibility Triggers

Control element visibility using `<element>_visible` syntax:

```hoi4
scripted_gui = {
    conditional_gui = {
        window_name = "conditional_window"
        
        warning_icon_visible = {
            has_war = yes
        }
        
        peace_text_visible = {
            has_war = no
        }
    }
}
```

Elements with visibility triggers hide when triggers evaluate false and show when true.

### Clickable Triggers

Control element interactivity using `<element>_<modifiers>_click_enabled` syntax:

```hoi4
scripted_gui = {
    enabled_gui = {
        window_name = "enabled_window"
        
        recruit_button_click_enabled = {
            has_manpower > 1000
        }
    }
}
```

Elements become unclickable (grayed out) when enabled triggers evaluate false.

### Temporary Variables

Temporary variables can be set in trigger blocks and used in properties and dynamic lists. This enables complex calculations and state tracking within scripted GUI scope:

```hoi4
warning_icon_visible = {
    set_temp_variable = { threat_level = 0 }
    add_to_temp_variable = { threat_level = num_of_enemy_armies }
    check_variable = { threat_level > 50 }
}
```

Temporary variables persist throughout the trigger evaluation for that specific GUI update cycle.

## Dynamic Lists

Dynamic lists pair with `gridBoxType` interface elements to generate repeating content:

```hoi4
scripted_gui = {
    list_gui = {
        window_name = "list_window"
        
        dynamic_lists = {
            example_list = {
                array = owned_states
                entry_container = state_entry_window
                change_scope = yes
            }
        }
    }
}
```

Dynamic list attributes:

- `array`: Array variable to iterate (required)
- `entry_container`: Container template used for each entry (required)
- `value`: Variable name for current value (defaults to `v`)
- `index`: Variable name for current index (defaults to `i`)
- `change_scope`: If true, scope changes to array element for each entry

The gridBoxType in the interface must reference the same container name specified in `entry_container`. The system creates one instance of that container per array element.

## Properties

Version 1.5+ supports dynamic property assignment:

```hoi4
scripted_gui = {
    dynamic_gui = {
        window_name = "dynamic_window"
        
        properties = {
            example_icon = {
                frame = manpower_frame
                x = icon_x_position
                y = icon_y_position
                image = "[Get_Icon_Sprite]"
            }
        }
    }
}
```

Property attributes:

- `frame`: Variable determining which frame of multi-frame sprite displays
- `x`: Variable for horizontal position offset
- `y`: Variable for vertical position offset
- `image`: String (supports scripted localization) for sprite name

Variables can be set through triggers or passed from parent scopes. Image strings support scripted localization syntax for dynamic sprite selection.

## Dirty Evaluation

The `dirty` attribute controls when scripted GUI updates:

```hoi4
scripted_gui = {
    optimized_gui = {
        window_name = "optimized_window"
        dirty = variable_name
    }
}
```

**Default (no dirty attribute)**: GUI updates every tick. High CPU cost but ensures immediate reactivity.

**Optimized (with dirty attribute)**: GUI updates only when specified variable changes. Significantly reduces CPU usage for complex GUI that doesn't need constant updates.

The variable specified in `dirty` should be set or modified by effects when updates are needed. This manual control trades immediate responsiveness for performance.

## AI System

Version 1.5+ enables AI interaction with scripted GUI through evaluation and weighting systems.

### AI Enable

```hoi4
scripted_gui = {
    ai_usable_gui = {
        window_name = "ai_window"
        ai_enabled = yes
    }
}
```

The `ai_enabled` attribute is checked at initialization only. Changing it during gameplay has no effect.

### AI Testing

```hoi4
scripted_gui = {
    ai_gui = {
        window_name = "ai_window"
        ai_enabled = yes
        ai_test_interval = 24
        ai_test_variance = 0.2
        
        ai_test_scopes = {
            test_enemy_countries = yes
            test_ally_countries = yes
        }
    }
}
```

Test interval attributes:

- `ai_test_interval`: Hours between AI evaluations (defaults to 24)
- `ai_test_variance`: Random variance factor (defaults to 0.2, meaning ±20%)

Test scopes determine which entities AI evaluates:

**Country scopes**: `test_self_country`, `test_enemy_countries`, `test_ally_countries`, `test_neighbouring_countries`, `test_neighbouring_ally_countries`, `test_neighbouring_enemy_countries`

**State scopes**: `test_self_owned_states`, `test_enemy_owned_states`, `test_ally_owned_states`, `test_self_controlled_states`, `test_enemy_controlled_states`, `test_ally_controlled_states`, `test_neighbouring_states`, `test_neighbouring_enemy_states`, `test_neighbouring_ally_states`, `test_our_neighbouring_states`, `test_our_neighbouring_states_against_allies`, `test_our_neighbouring_states_against_enemies`, `test_contesded_states`

**Modifiers**: `test_if_only_major`, `test_if_only_coastal`

AI evaluates selected_country_context and selected_state_context for every applicable country or state unless restricted. This can cause significant performance impact on large numbers of AI nations.

### AI Weights

```hoi4
scripted_gui = {
    weighted_gui = {
        window_name = "weighted_window"
        
        ai_weights = {
            example_button_click = {
                ai_will_do = {
                    base = 10
                    modifier = {
                        factor = 2
                        has_war = yes
                    }
                }
            }
        }
    }
}
```

AI clicks elements when weight > 0. By default, AI selects 1 weighted option per test interval. Use `ai_max_weight_taken_per_test` to allow multiple selections per evaluation cycle.

Weight calculations use standard modifier math with base values and multiplicative/additive factors.

## Localization Commands

Scripted GUI interactions can be referenced in localization:

**Effect tooltip**: `[!<element>_<action>]` displays effect tooltip for click action
**Trigger tooltip**: `[!<element>_<action>_enabled]` displays clickable trigger tooltip

These commands generate automatic tooltip text from the defined effects and triggers without manual localization.

## Related Systems

Scripted GUI integrates with interface containers for visual structure, localization for text and icons, and game logic through effects and triggers. See [Interface System](/assets/interface.md) for container definitions and [Localization](/assets/localisation.md) for text formatting.
