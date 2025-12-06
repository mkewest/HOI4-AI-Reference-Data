---
domain: scripting
concept: scopes
version: 1.14+
requires: []
relates: [triggers_core, effects, on_actions_core]
---

# Scope System

Scopes are evaluation contexts that determine which game object a trigger or effect operates on. They control what data is accessible and what operations are valid at any point in script execution.

## Scope Types by Purpose

HOI4 scopes are categorized by their allowed usage contexts:

**Trigger scopes:** Only usable in trigger blocks (conditional checks). Examples: `all_country`, `any_state`

**Effect scopes:** Only usable in effect blocks (actions that modify game state). Examples: `every_country`, `random_state`

**Dual scopes:** Usable in both trigger and effect contexts, and many can serve as scope targets. Examples: `ROOT`, `PREV`, `TAG`, `owner`, `controller`

## Scope Types by Target

Scopes target specific game object types:

- **Country:** Nations, including tags and dynamic countries
- **State:** Geographic provinces with buildings and resources
- **Character:** Leaders, advisors, operatives, scientists
- **Division:** Individual military units
- **MIO:** Military industrial organizations (1.13+)
- **Contract:** Purchase contracts for equipment trading
- **Special Project:** Research projects (1.15+)

## Trigger Scope Patterns

Trigger scopes evaluate conditions across collections of objects:

**`all_<object>`:** Returns false if ANY object in the collection fails the condition. Uses short-circuit evaluation - stops at first false.

**`any_<object>`:** Returns true if ANY object in the collection meets the condition. Stops at first true. Supports optional `count = N` parameter to require at least N matches.

```hoi4
any_owned_state = {
    count = 3
    is_coastal = yes
}
```

This returns true only if the country owns at least 3 coastal states.

> [!CRITICAL] Non-dual scopes cannot select countries that do not exist. The exception is `every_possible_country`, which includes all possible tag definitions even if unspawned. Using non-existent countries in scopes like `any_country` causes silent failures.

## Effect Scope Patterns

Effect scopes execute code blocks on collections of objects:

**`every_<object>`:** Executes the effect block on each object that meets the `limit` condition. The `limit` parameter acts as an AND trigger block.

**`random_<object>`:** Executes the effect block on one randomly selected object meeting the `limit` condition.

```hoi4
random_owned_state = {
    limit = {
        is_coastal = yes
        industrial_complex > 0
    }
    add_building_construction = {
        type = naval_dockyard
        level = 1
    }
}
```

> [!CRITICAL] The `limit` parameter ONLY works in effect scopes. It does not work in trigger scopes or dual scopes. Using `limit` in a trigger context causes the entire block to fail silently.

### Scope Ordering

Effect scopes iterate in deterministic order:

- **Country scopes:** Process in tag creation order (file load order, then definition order within files)
- **State scopes:** Process in ascending state ID order

Tooltip evaluation for `every_` scopes with varying conditions only evaluates the FIRST selected scope by default. Use `display_individual_scopes = yes` to force separate tooltip evaluation for each scope.

## Scope Parameters

### limit

The `limit` parameter filters which objects are affected by effect scopes:

```hoi4
every_neighbor_country = {
    limit = {
        NOT = { has_war_with = ROOT }
        is_subject = no
    }
    add_opinion_modifier = {
        target = ROOT
        modifier = trade_agreement
    }
}
```

### random_select_amount

This parameter works ONLY with `every_` type scopes and selects up to N random objects meeting the limit:

```hoi4
every_owned_state = {
    random_select_amount = 3
    limit = { is_coastal = yes }
    add_building_construction = {
        type = bunker
        level = 2
    }
}
```

Note that this does not guarantee exactly N scopes - if fewer than N objects meet the limit, fewer will be selected.

### prioritize

This parameter works ONLY on `random_` scopes targeting states, not countries or other object types. It does not work on `random_neighbor_state`.

```hoi4
random_owned_state = {
    prioritize = { 42 116 336 }
    limit = { arms_factory > 5 }
    # effect here
}
```

States listed in `prioritize` have equal priority - the game randomly selects among qualifying priority states. If no priority states qualify, the game falls back to random selection from all qualifying states.

### include_invisible

Unit leader and MIO scopes default to visible objects only. Set `include_invisible = yes` to include invisible leaders or MIOs:

```hoi4
every_unit_leader = {
    include_invisible = yes
    # affects both visible and invisible leaders
}
```

### display_individual_scopes

By default, tooltip evaluation for `every_` scopes with if statements shows only the first selected scope. This parameter forces separate tooltips per scope:

```hoi4
every_owned_state = {
    display_individual_scopes = yes
    limit = { 
        if = { limit = { is_coastal = yes }
            industrial_complex < 5
        }
    }
    # effect
}
```

### tooltip

Replaces the default scope tooltip with custom localization:

```hoi4
random_owned_state = {
    tooltip = my_custom_tooltip_key
    # effect
}
```

## Dual Scopes

Dual scopes work in both trigger and effect contexts and can serve as scope targets.

### Direct Object Reference

**TAG:** References a specific country by tag. If the exact tag doesn't exist but a dynamic country derived from that tag does exist, TAG refers to the dynamic country.

**state_id:** References a state by numeric ID (e.g., `42 = { ... }`)

**character_id:** References a character by token (version 1.11+). Pre-1.12.8, this only worked if the character was already recruited. Post-1.12.8, it works for any defined character.

**mio:\<id\>:** References a military industrial organization (1.13+). Must be called from country scope.

**sp:\<id\>:** References a special project (1.15+). Must be called from country scope.

### Context Scopes

**ROOT:** The root node of the current block - the default scope. For events, this is the country receiving the event. For national focuses, this is the country taking the focus. Some blocks like `on_startup` have no ROOT scope.

**THIS:** The current scope being evaluated. In nested scopes, THIS changes to reflect the active evaluation context while ROOT remains constant.

**PREV:** The parent scope - the scope that called into the current scope. Can chain indefinitely: `PREV.PREV.PREV.PREV` traverses up four scope levels.

> [!CRITICAL] PREV chaining often causes broken tooltips where the shown scope doesn't match the execution scope. The tooltip system can't always track chained PREV references. Workaround: use `hidden_effect` for the actual execution and `custom_effect_tooltip` for the tooltip.

**FROM:** A secondary hardcoded scope with context-dependent meaning:
- Events: FROM is the country that sent the event
- Targeted decisions: FROM is the target country/state
- Diplomatic actions: FROM is the target of the action

FROM can chain like PREV: `FROM.FROM` is valid. Not all contexts define FROM - check documentation for the specific block type.

### Relationship Scopes

**overlord:** The overlord of a subject country. Only valid in subject country scope.

**faction_leader:** The leader of the faction this country belongs to. Only valid in faction member scope.

**owner:** The owning country. Valid in state, character, or combatant scope.

**controller:** The controlling country. Only valid in state scope.

**capital_scope:** The capital state. Only valid in country scope.

All relationship scopes can trigger "Invalid event target" errors if the relationship doesn't exist in context.

### Dynamic Scopes

**event_target:\<key\>:** References a saved event target created with `save_event_target_as`.

**var:\<variable\>:** References a country by the value of a variable (1.5+). The variable must contain a valid country tag.

## Invalid Event Target Error

When a scope has no valid target in the current context, the game logs "Invalid event target" but continues execution:

- **Effects:** Skipped entirely - no changes occur
- **Triggers:** Return neither true nor false - treated as non-evaluable

Common causes:
- Accessing `overlord` for independent countries
- Accessing `faction_leader` for non-faction members  
- Accessing `owner` for states with no owner

This error clutters the log if checked frequently (e.g., every tick in on_actions).

**Fix:** Always wrap scope access in conditional checks:

```hoi4
if = {
    limit = { is_subject = yes }
    overlord = {
        # safe to access overlord here
    }
}
```

## Effect-Only Scope Collections

### Country Scopes

```hoi4
every_country               # All existing countries
random_country
every_neighbor_country      # Land or naval neighbors
random_neighbor_country
every_enemy_country         # Countries at war with ROOT
random_enemy_country
every_occupied_country      # Countries with states occupied by ROOT
random_occupied_country
every_other_country         # All countries except ROOT
random_other_country
every_possible_country      # All tags (including non-existent)
```

### State Scopes

```hoi4
every_state                 # All states
random_state
every_neighbor_state        # States adjacent to current state
random_neighbor_state
every_owned_state           # States owned by current country
random_owned_state
every_core_state            # States in current country's cores
random_core_state
every_controlled_state      # States controlled by current country
random_controlled_state
random_owned_controlled_state  # States both owned and controlled
```

Note the asymmetry: `random_owned_controlled_state` exists, but `every_owned_controlled_state` does not. This is an incomplete pattern in the scope system.

### Character Scopes

```hoi4
every_unit_leader           # All unit leaders (visible by default)
random_unit_leader
every_army_leader           # Army and field marshals only
random_army_leader
global_every_army_leader    # All army leaders globally (not per-country)
every_navy_leader           # Admirals only
random_navy_leader
every_operative             # Intelligence operatives
random_operative
every_character             # All characters (leaders, advisors, etc.)
random_character
every_scientist             # Scientists in research teams
random_scientist
party_leader                # Leader of specific ideology party
```

> [!CRITICAL] The `party_leader` effect requires `has_ideology` in its limit block, and it must check the specific ideology type (not the ideology group). Without this, the effect silently fails.

```hoi4
party_leader = {
    limit = { has_ideology = socialism }  # Specific type required
    add_timed_idea = {
        idea = popular_leader
        days = 365
    }
}
```

### Division Scopes

```hoi4
every_country_division      # All divisions of current country
random_country_division
every_state_division        # All divisions in current state
random_state_division
```

### MIO and Contract Scopes

```hoi4
every_military_industrial_organization    # All MIOs (1.13+)
random_military_industrial_organization
every_purchase_contract                   # All purchase contracts
random_purchase_contract
```

## Array-Based Scopes

These scopes operate on arrays created with `add_to_array` or `add_to_temp_array`:

**any_of_scopes / all_of_scopes:** Trigger-type array iteration with standard AND/OR logic.

**for_each_scope_loop:** Effect-type array iteration. Supports optional `break` parameter to exit early.

**random_scope_in_array:** Selects one random scope from array. Supports `limit` and `break` parameters.

```hoi4
add_to_temp_array = {
    array = potential_targets
    value = GER
}
add_to_temp_array = {
    array = potential_targets
    value = ITA
}

any_of_scopes = {
    array = potential_targets
    has_war_with = ROOT
}
```

## Scope-Changing Effects

Some effects change the execution scope during their operation:

### start_civil_war

Initiates a civil war and changes scope to the rebelling dynamic country:

```hoi4
start_civil_war = {
    ideology = communism
    ruling_party = fascism
    size = 0.3
    capital = 42
    states = { 1 2 3 }
}
# Scope is now the rebel country
```

> [!CRITICAL] If the capital is included in the revolt states, the civil war will not fire at all. Workaround: use `set_capital` to move the capital before calling `start_civil_war`, then restore it in `on_civil_war_end`.

Parameters:
- `ideology`: Ideology of rebels
- `ruling_party`: Ruling party of rebels
- `size`: Percentage of states to revolt (0.0-1.0)
- `army_ratio` / `navy_ratio` / `air_ratio`: Equipment split
- `capital`: Capital state for rebel country
- `states`: Explicit state list for revolt
- `states_filter`: Trigger to select revolt states
- `keep_unit_leaders` / `keep_unit_leaders_trigger`: Leader handling
- `keep_political_leader` / `keep_political_party_members`: Character handling

### create_dynamic_country

Creates a new dynamic country and changes scope to it (1.9+):

```hoi4
create_dynamic_country = {
    original_tag = POL
    copy_tag = SOV
}
# Scope is now the new dynamic country
```

## States Without Owner/Controller

States that have neither an owner nor a controller are unstable and cause crashes in specific contexts:

- **AI air missions:** Game crashes when AI tries to plan missions over ownerless states
- **Most effects:** Effects targeting states without owners cause undefined behavior

Always ensure states have valid owners or controllers, or use conditional checks before operating on states.

## Scope Validation in Triggers

Triggers fail silently when used in the wrong scope type. A country-scoped trigger used in state scope returns false without error:

```hoi4
42 = {
    has_government = democratic  # Country trigger in state scope - returns false
}
```

This silent failure makes debugging difficult. Always verify trigger scope requirements against the current evaluation context.

### Tag References

`original_tag` includes dynamic countries in its matching, while `tag` does not:

```hoi4
original_tag = GER  # Matches GER and all GER dynamics (D01, D02, etc.)
tag = GER           # Matches only the base GER tag
```

### Variable Scope References

When referencing variables across scopes, the variable must reference its creation scope:

```hoi4
every_country = {
    set_variable = { target_country = THIS }
}

# Later, in different scope:
var:target_country = {
    # This works - variable references the country that created it
}
```

## Related Defines

- `MAX_EFFECT_ITERATION`: See [NGame](/defines_list/NGame.md)
