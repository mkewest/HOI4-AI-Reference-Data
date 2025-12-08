---
domain: scripting
concept: modifiers
version: 1.14+
requires: [scopes, effects]
relates: [defines, modifiers_list, scopes, effects]
---

# Modifier System

Modifiers adjust gameplay values like combat stats, production efficiency, resource generation, and political power. They apply through ideas, character traits, dynamic modifiers, static modifiers, and targeted modifiers.

## Basic Syntax

Modifiers use simple key-value pairs:

```hoi4
modifier = {
    political_power_gain = 0.10          # +10% daily PP gain
    stability_factor = 0.05              # +5% stability
    army_org_factor = 0.10               # +10% organization
    industrial_capacity_factory = 0.15   # +15% factory output
}
```

Modifier names are fixed tokens defined by the game engine. Values are numeric (float or int depending on modifier type).

## Modifier Value Behavior

> [!CRITICAL] Any modifier with value 0 has NO EFFECT and cannot be overridden by other modifiers. A modifier set to 0 is completely ignored by the game engine.

Negative modifiers always work and produce the opposite effect:

```hoi4
stability_factor = -0.10  # -10% stability (decreases stability gain)
political_power_gain = -0.15  # -15% PP gain (reduces daily PP)
```

## Modifier Types

### Percentual Modifiers

Multiply the base value. Format: `0.5 = +50%` (50% increase)

```hoi4
political_power_gain = 0.10  # +10% to daily PP gain
army_org_factor = 0.20       # +20% to organization
production_speed_arms_factory_factor = 0.15  # +15% to military factory output
```

Most modifiers are percentual. They scale with base values.

### Flat Modifiers

Add directly to the base value:

```hoi4
political_power_cost = 50    # +50 PP cost (flat addition)
experience_gain_army = 0.05  # +0.05 experience per day (flat)
```

Flat modifiers use actual units, not percentages.

### Boolean Modifiers

Enable features - only the value 1 works:

```hoi4
can_license_air_equipment = 1      # Enables air equipment licensing
can_puppet = 1                      # Enables puppet ability
force_defend_allies_in_civil_war = 1  # Forces defending allies
```

Values other than 1 have no effect. These are binary on/off switches.

### Multiplicative Modifiers

Special modifiers that multiply instead of adding:

> [!CRITICAL] `consumer_goods_factor` and similar multiplicative modifiers use multiplication, not addition. Multiple instances compound: `0.5 + (-0.5) = (1+0.5)(1-0.5) = 0.75`, NOT `0`.

```hoi4
# Two modifiers:
consumer_goods_factor = 0.5   # +50%
consumer_goods_factor = -0.5  # -50%

# Result: (1 + 0.5) * (1 - 0.5) = 1.5 * 0.5 = 0.75
# NOT: 0.5 + (-0.5) = 0
```

This creates exponential scaling instead of linear. Commonly applies to:

- `consumer_goods_factor`
- `conscription_factor`
- Various economy-related factors

## Structure and Categories (1.14+)

- **Static vs dynamic vs targeted vs opinion**: Static apply globally; dynamic attach to scopes via add/remove; targeted attach to a source-target pair; opinion modifiers attach between countries.
- **Percent vs flat vs multiplicative**: Match semantics to the modifier token; check `modifiers_list` pages for expected units.
- **Variable-based modifiers**: Some tokens accept variable references (`var:foo`); ensure variable scope matches the target scope to avoid silent no-ops.
- **Schema references**: Use `modifiers_list/*.md` for per-category schemas and token lists; keep names synchronized to avoid ignored modifiers.
- **Integration**: Effects/triggers should use the correct block (e.g., `targeted_modifier = { }` for country-to-country, `dynamic_modifier = { }` for scoped, `opinion_modifier = { }` for bilateral).

## Dynamic modifiers

Dynamic modifiers are defined in `common/dynamic_modifiers/*.txt` and applied via effects.

Definition fields:
- `icon` (optional): Shown in GUIs if provided.
- `enable` (optional): Gate; modifier does not apply when false.
- `remove_trigger` (optional): Removes the modifier when true.
- `attacker_modifier = yes` (optional): Also read in combat for attackers even if not in the state.
- Standard modifier list inside the definition; supports variable-based values (e.g., `max_fuel = var_max_fuel`).

Application:
```hoi4
add_dynamic_modifier = {
    modifier = example_dynamic_modifier
    scope = GER    # optional; overrides ROOT
    days = 14      # optional; auto-removal after N days
}
```
- Scopes: country, state, unit_leader, special_project.
- Evaluated daily; force refresh with `force_update_dynamic_modifier`.
- Removal: via `remove_trigger`, `remove_dynamic_modifier`, or `days` expiry.

Guidelines:
- Keep `remove_trigger` lightweight when applied broadly.
- Use `scope` to target specific entities; omit for ROOT.
- Provide `icon` when player-visible; omit for hidden/internal modifiers.

## Application Methods

### Ideas and National Spirits

Applied via `common/ideas/*.txt`:

```hoi4
ideas = {
    country = {
        great_depression = {
            modifier = {
                political_power_gain = -0.50
                consumer_goods_factor = 0.30
                industrial_capacity_factory = -0.30
            }
        }
    }
}
```

Ideas apply to the country scope. They persist until removed via `remove_ideas` effect.

### Country Leader Traits

Applied via country leader definitions:

```hoi4
create_country_leader = {
    name = "Leader Name"
    traits = { dictator }
}
```

Trait modifiers are defined in `common/country_leader/*.txt`:

```hoi4
dictator = {
    political_power_gain = 0.10
    stability_factor = -0.10
}
```

### Unit Leader Traits

Applied to corps commanders, field marshals, and admirals:

```hoi4
traits = {
    panzer_leader = {
        type = corps_commander
        modifier = {
            army_armor_speed_factor = 0.05
            army_armor_attack_factor = 0.10
        }
    }
}
```

Unit leader modifiers apply to units under that leader's command.

### Dynamic Modifiers

Defined in `common/dynamic_modifiers/*.txt` with variable-based values:

```hoi4
dynamic_war_economy = {
    icon = 1
    enable = { has_war = yes }
    remove_trigger = { has_war = no }
    
    war_support_factor = var:war_support_bonus
    industrial_capacity_factory = var:factory_bonus
}
```

Applied via effect:

```hoi4
set_variable = { war_support_bonus = 0.15 }
set_variable = { factory_bonus = 0.10 }
add_dynamic_modifier = {
    modifier = dynamic_war_economy
    days = 365
}
```

> [!CRITICAL] Dynamic modifiers cannot be reloaded in debug mode - they require a full game restart to reflect changes. Variable values reset to 0 at the start of each day BEFORE modifier evaluation occurs.

#### Evaluation Order

Dynamic modifiers evaluate in the order `add_dynamic_modifier` was called, NOT definition file order:

```hoi4
# First applied - evaluates first
add_dynamic_modifier = { modifier = economy_bonus }

# Second applied - evaluates second
add_dynamic_modifier = { modifier = military_bonus }
```

If modifier B depends on variables set by modifier A, apply A first.

#### Tooltip Limitations

> [!CRITICAL] Tooltips do NOT show variable-based modifier values. Use `custom_effect_tooltip` to display dynamic values:

```hoi4
custom_effect_tooltip = economy_modifier_tt
add_dynamic_modifier = {
    modifier = dynamic_economy
}
```

Localization:

```yaml
economy_modifier_tt:0 "Grants +[?factory_bonus|%0]% factory output"
```

#### State Dynamic Modifiers

For state-targeted dynamic modifiers, variables must be defined FOR THE STATE, not the owner:

```hoi4
# WRONG - variable in country scope
set_variable = { factory_bonus = 0.10 }
42 = {
    add_dynamic_modifier = { modifier = state_economy }
    # Reads state's factory_bonus (doesn't exist)
}

# CORRECT - variable in state scope
42 = {
    set_variable = { factory_bonus = 0.10 }
    add_dynamic_modifier = { modifier = state_economy }
}
```

### Static Modifiers

Defined in `common/modifiers/*.txt`:

```hoi4
my_static_modifier = {
    stability_factor = 0.10
    war_support_factor = 0.05
}
```

Applied via effects:

- Country modifiers: Apply directly in modifier blocks
- Province modifiers: `add_province_modifier` / `remove_province_modifier`
- Relation modifiers: `add_relation_modifier` / `remove_relation_modifier`

#### Global Static Modifiers

Special hardcoded modifiers where WHEN they apply is fixed, but WHAT they do is editable:

```hoi4
# common/modifiers/00_static_modifiers.txt
at_peace = {
    consumer_goods_factor = -0.10  # What the modifier does (editable)
}
# When it applies: country not at war (hardcoded)
```

Common global modifiers:

- `at_peace` / `at_war`
- `low_stability` / `high_stability`
- `embargo` / `has_embargo`
- `civilian_economy` / `war_economy` / `tot_economy`

#### Difficulty Modifiers

Defined in `common/difficulty_settings/*.txt`:

```hoi4
difficulty_settings = {
    # 5 levels: 0, 1, 2, 3, 4
    # Multipliers: 0.0, 0.25, 0.5, 0.75, 1.0
    
    player_bonuses = {
        army_attack_factor = 0.10  # At max difficulty: 0.10 * 1.0 = +10%
    }
}
```

The five difficulty levels scale from 0% (easiest) to 100% (hardest) of the defined values.

#### Province Modifiers

Apply to specific provinces (rarely used, most state modifiers work instead):

```hoi4
add_province_modifier = {
    modifier = terrain_penalty
    province = 1234
}
```

Many state modifiers function on provinces despite being undocumented. Test before using.

### Balance of Power Modifiers

Applied via `add_power_balance_modifier` effect:

```hoi4
balance_of_power_modifier = {
    range = -1 to 1  # Left side (-1) to right side (+1)
    modifier = {
        stability_factor = 0.05
    }
}
```

BOP modifiers scale based on power balance position.

### Targeted Modifiers

Apply modifiers against specific countries:

```hoi4
targeted_modifier = {
    tag = GER
    attack_bonus_against = 0.10
    defense_bonus_against = 0.10
}
```

> [!CRITICAL] Targeted modifiers MUST be inside a `targeted_modifier = {...}` block, NOT inside a regular `modifier = {...}` block. Placing them in regular modifier blocks causes them to fail silently.

Can use variables for dynamic targets:

```hoi4
set_variable = { my_target = GER }
targeted_modifier = {
    tag = var:my_target
    attack_bonus_against = 0.15
}
```

#### Targeted Modifier Bugs

> [!CRITICAL] `attack_bonus_against` doesn't work when your unit is defending. `defense_bonus_against` doesn't work when your unit is attacking. These modifiers only apply in their respective combat roles.

This limits their usefulness for balanced combat bonuses. Use general combat modifiers or separate offensive/defensive spirits for consistent effects.

### Opinion Modifiers

Defined in `common/opinion_modifiers/*.txt`:

```hoi4
trade_agreement = {
    value = 20           # Opinion value (±100 cap)
    trade = yes          # Affects trade acceptance
    decay = -1           # Monthly decay (trends to 0, not original)
    duration = 365       # Days before removal
    min_trust = 10       # Minimum trust level
    max_trust = 50       # Maximum trust level
}
```

> [!CRITICAL] Opinion modifiers are NOT actual gameplay modifiers - they only affect diplomacy and trade relations. They cannot be used in regular modifier blocks.

Applied via:

- `add_opinion_modifier` effect
- `remove_opinion_modifier` effect

File encoding MUST be UTF-8-BOM (not plain UTF-8). Incorrect encoding causes display issues.

Opinion decay trends toward zero, not the original value. A +50 opinion with -5 decay becomes +45, +40, ..., 0 (stops at zero, doesn't go negative).

## Modifier Definitions (Custom Modifiers)

Create custom modifiers in `common/modifier_definitions/*.txt`:

```hoi4
my_custom_modifier = {
    color_type = good        # Tooltip color (good/bad/neutral)
    value_type = percentage  # Display format (percentage/number)
    precision = 2            # Decimal places
    postfix = "%"            # Display suffix
    category = country       # Category for organization
}
```

Custom modifiers act as variables that can be read via `modifier@token_name`:

```hoi4
# Definition
custom_factory_bonus = {
    color_type = good
    value_type = percentage
    precision = 1
}

# Usage in dynamic modifier
production_bonus = {
    industrial_capacity_factory = modifier@custom_factory_bonus
}
```

## Idea Cost Modifiers

Modifiers affecting idea/advisor costs:

```hoi4
idea_cost_factor = -0.10              # -10% cost for all ideas
political_advisor_cost_factor = -0.15  # -15% political advisor cost
theorist_cost_factor = -0.20          # -20% theorist cost
```

> [!CRITICAL] Cost modifiers require an idea or character of that category to exist in an EARLIER-EVALUATED file. Without a prerequisite idea/character, the cost modifier silently fails and does nothing.

Load order determines what "earlier-evaluated" means. If your cost modifier is in `00_ideas.txt` but no advisor exists until `99_advisors.txt`, the cost modifier won't work. Ensure prerequisite content loads first.

## Equipment and Doctrine Modifiers

### Equipment Capture

Two types control equipment capture rates:

**equipment_capture:** Flat addition to capture ratio:

```hoi4
equipment_capture = 0.10  # +0.10 to capture ratio (e.g., 0.05 becomes 0.15)
```

**equipment_capture_factor:** Percentual multiplication:

```hoi4
equipment_capture_factor = 0.50  # +50% to capture ratio (e.g., 0.05 becomes 0.075)
```

Both can be used together: flat addition applies first, then percentual multiplication.

### Doctrine Costs

Doctrine cost modifiers require the "cat_" prefix for specific doctrines:

```hoi4
# Specific doctrine line
cat_mobile_warfare_cost_factor = -0.10  # -10% to Mobile Warfare

# Branch-wide (no prefix needed)
land_doctrine_cost_factor = -0.15       # -15% to all land doctrines
air_doctrine_cost_factor = -0.10        # -10% to all air doctrines
naval_doctrine_cost_factor = -0.10      # -10% to all naval doctrines
```

The prefix distinction is inconsistent but mandatory for specific doctrine lines.

### Broken Modifiers

> [!CRITICAL] `cavalry_speed_factor` is broken and not recognized by the game engine. Use `cavalry_attack_factor` or other cavalry modifiers instead.

## Terrain Modifiers

> [!CRITICAL] `terrain_penalty_reduction` only works in unit_leader scope despite appearing in country-scoped national spirits. Using it in country scope has no effect.

```hoi4
# WRONG - doesn't work
ideas = {
    country = {
        my_idea = {
            modifier = {
                terrain_penalty_reduction = 0.10  # No effect in country scope
            }
        }
    }
}

# CORRECT - works
traits = {
    terrain_specialist = {
        type = corps_commander
        modifier = {
            terrain_penalty_reduction = 0.10  # Works in unit leader scope
        }
    }
}
```

## Special Forces Modifiers

> [!CRITICAL] `special_forces_cap` is PERCENTUAL despite affecting slot count:

```hoi4
special_forces_cap = 0.10  # +10% to special forces cap, NOT +10 slots
```

Individual contribution factors also exist:

```hoi4
paratroopers_special_forces_contribution_factor = 0.50  # +50% paratrooper cap contribution
marines_special_forces_contribution_factor = 0.50       # +50% marine cap contribution
```

These scale how much each special forces battalion counts toward the cap.

## MIO Modifiers

Military Industrial Organization modifiers (1.13+):

```hoi4
military_industrial_organization_task_capacity = 2  # Flat count, not percentual
military_industrial_organization_design_team_change_cost_factor = -0.25
military_industrial_organization_design_team_assign_cost_factor = -0.30
military_industrial_organization_industrial_manufacturer_cost_factor = -0.20
```

`task_capacity` is a FLAT count modifier (+2 means +2 task slots), while others are percentual.

MIO policy cooldown uses days, not hours like most timers:

```hoi4
military_industrial_organization_policy_cost_factor = -0.15
military_industrial_organization_policy_cooldown_factor = -0.20  # Days, not hours
```

## Operative Modifiers

Intelligence operative modifiers:

```hoi4
own_operative_forced_into_hiding_time_factor = -0.25      # Affects YOUR operatives
enemy_operative_forced_into_hiding_time_factor = 0.50     # Affects ENEMY operatives

own_operative_capture_chance_factor = -0.30               # YOUR operative capture chance
enemy_operative_capture_chance_factor = 0.30              # ENEMY operative capture chance
```

"own" affects YOUR operatives, "enemy" affects enemy operatives. The distinction is critical for proper effect direction.

> [!CRITICAL] `operative_death_on_capture_chance` only works in country scope, NOT operative scope. Applying it in operative scope has no effect.

## Variable-Based Modifiers

Dynamic and custom modifiers can read variables:

```hoi4
# Set variables
set_variable = { attack_bonus = 0.15 }
set_variable = { defense_bonus = 0.10 }

# Use in dynamic modifier
add_dynamic_modifier = {
    modifier = combat_bonus  # Reads var:attack_bonus and var:defense_bonus
}
```

Variables must be defined in the appropriate scope (country for country modifiers, state for state modifiers, etc.).

## Modifier Scope Contexts

Different application methods apply to different scopes:

| Application Method | Valid Scopes |
|-------------------|--------------|
| Ideas | Country |
| Country Leader Traits | Country |
| Unit Leader Traits | Unit Leader, Units |
| Dynamic Modifiers | Country, State, Unit Leader |
| Static Modifiers | Country, State, Province |
| Targeted Modifiers | Country |
| Opinion Modifiers | Country (diplomatic) |

Applying modifiers in wrong scopes causes silent failures - no errors, but no effect.

## Best Practices

1. **Test multiplicative modifiers:** Verify they compound correctly
2. **Scope validation:** Ensure modifiers work in intended scope
3. **Variable hygiene:** Use unique variable names for dynamic modifiers
4. **Tooltip clarity:** Use `custom_effect_tooltip` for variable-based modifiers
5. **Load order awareness:** Place prerequisite content before cost modifiers
6. **Debug mode limitation:** Restart game after changing dynamic modifiers
7. **Zero avoidance:** Never set modifiers to exactly 0 if you want override capability

## Related Systems

For complete modifier enumeration by category, see [Modifiers List](/modifiers_list/00_overview.md).

For specific modifier categories:

- Intelligence and operations: See [Intelligence Modifiers](/modifiers_list/intelligence.md)
- Land combat and units: See [Military Land Modifiers](/modifiers_list/military_land.md)
- Leaders and experience: See [Military Leaders Modifiers](/modifiers_list/military_leaders.md)
- Naval warfare: See [Military Naval Modifiers](/modifiers_list/military_naval.md)
- Air warfare: See [Military Air Modifiers](/modifiers_list/military_air.md)
- Politics and ideology: See [Politics Ideology Modifiers](/modifiers_list/politics_ideology.md)
- Economy and production: See [Economy Production Modifiers](/modifiers_list/economy_production.md)
- Resources and trade: See [Economy Resources Modifiers](/modifiers_list/economy_resources.md)
- Occupation and puppets: See [Occupation Autonomy Modifiers](/modifiers_list/occupation_autonomy.md)
- State-scoped modifiers: See [State Modifiers](/modifiers_list/state_modifiers.md)
- Equipment and idea costs: See [Equipment Modifiers](/modifiers_list/equipment.md)
- Research and doctrine: See [Research Modifiers](/modifiers_list/research.md)
- AI behavior: See [AI Modifiers](/modifiers_list/ai_modifiers.md)
- Special operations: See [Special Operations Modifiers](/modifiers_list/special_operations.md)

For defines that interact with modifiers, see [Defines](/scripting/defines.md).

For effects that apply modifiers, see [Effects](/scripting/effects.md).
