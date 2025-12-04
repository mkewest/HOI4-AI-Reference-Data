---
domain: scripting
concept: triggers_core
version: 1.14+
requires: [scopes]
relates: [effects, scripted_triggers, on_actions]
---

# Core Trigger System

Triggers check game state without modifying it. They return boolean values and control conditional logic throughout HOI4's scripting system.

## Fundamental Behavior

Triggers evaluate game conditions and return true or false. They never modify game state - that's the role of effects. The default logic is AND with short-circuit evaluation: execution stops at the first false trigger.

```hoi4
# All must be true
has_political_power > 100
has_manpower > 10000
has_war = no
```

If `has_political_power` returns false, the remaining triggers are never evaluated.

## Comparison Operators

### Equality Operator (=)

The equality operator has two distinct behaviors in HOI4:

**Strict equality comparison:**
```hoi4
has_political_power = 100  # True only at exactly 100 PP
```

> [!CRITICAL] Unlike older Paradox games where `=` meant "≥", HOI4 uses strict equality. `has_political_power = 100` is FALSE if you have 101 political power.

**Trigger block introduction:**
```hoi4
has_opinion = {
    target = GRE
    value < -10
}
```

When `=` is followed by a block `{ ... }`, it introduces a scoped trigger with additional parameters.

### Greater Than (>)

Strict greater than - false at the exact value:

```hoi4
has_political_power > 100  # False at exactly 100 PP, true at 101+
```

### Less Than (<)

Strict less than - false at the exact value:

```hoi4
has_stability < 0.5  # False at exactly 0.5, true below
```

## Logic Operators

### AND (Implicit)

Default behavior - all sub-triggers must be true. Uses short-circuit evaluation:

```hoi4
has_war = yes
has_capitulated = no
has_stability > 0.3
# Stops at first false
```

### OR

True if ANY sub-trigger is true. Also uses short-circuit evaluation - stops at first true:

```hoi4
OR = {
    has_idea = anti_communist_raids
    has_idea = trotskyite_plot
    has_government = fascism
}
```

### NOT

> [!CRITICAL] NOT is implemented as NOR, not NAND. It returns false if ANY sub-trigger is true, not if ALL are false.

```hoi4
NOT = {
    has_war_with = GER
    has_war_with = SOV
}
# False if at war with GER OR SOV (or both)
# True only if at war with neither
```

This is counterintuitive but critical for proper logic construction. To check "not all true", use:

```hoi4
OR = {
    NOT = { has_war_with = GER }
    NOT = { has_war_with = SOV }
}
```

### count_triggers

Returns true if at least N sub-triggers evaluate to true:

```hoi4
count_triggers = {
    amount = 2
    has_tech = infantry_weapons1
    has_tech = infantry_weapons2
    has_tech = infantry_weapons3
    has_tech = support_weapons1
}
# True if at least 2 of these techs are researched
```

Each sub-trigger contributes 1 to the count if true. The `amount` parameter sets the threshold.

### IF Statements

Conditional evaluation with optional branches:

```hoi4
if = {
    limit = { has_dlc = "La Resistance" }
    compliance > 50
    else_if = {
        limit = { has_dlc = "Together for Victory" }
        autonomy_level > autonomy_free
    }
    else = {
        is_subject = no
    }
}
```

If no branch matches, the if statement returns TRUE by default. This means:

```hoi4
if = {
    limit = { has_dlc = "Nonexistent" }
    always = no
}
# Returns TRUE (no branch matched)
```

## Tooltip Control

### hidden_trigger

Hides triggers from tooltip evaluation without affecting their execution:

```hoi4
hidden_trigger = {
    has_country_flag = secret_path_unlocked
    has_completed_focus = hidden_focus
}
is_ai = no  # Only this appears in tooltip
```

### custom_trigger_tooltip

Replaces trigger tooltip with custom localization:

```hoi4
custom_trigger_tooltip = {
    tooltip = my_complex_condition_tt
    has_country_flag = flag_a
    has_country_flag = flag_b
    has_country_flag = flag_c
}
```

The system automatically generates a negative variant by appending `_NOT` to the localization key. To prevent this or provide a custom negative:

```hoi4
custom_trigger_tooltip = {
    tooltip = my_condition_tt
    not_tooltip = my_condition_failed_tt
    # triggers
}
```

### custom_override_tooltip

Works in BOTH triggers and effects. Overrides the entire tooltip for the contained block:

```hoi4
custom_override_tooltip = {
    tooltip = custom_tt_key
    add_political_power = 50
    add_stability = 0.05
}
# Tooltip shows custom_tt_key instead of PP and stability changes
```

## Flag Value Checks

Flags support numeric values with comparisons:

```hoi4
has_country_flag = my_flag  # Default: checks if value > 0
has_country_flag = { flag = my_flag value > 5 }
has_country_flag = { flag = my_flag value = 0 }  # Checks exact zero
```

> [!CRITICAL] Flag values are stored as signed 16-bit integers, limited to the range -32768 to 32767. Exceeding this range causes integer overflow with undefined behavior.

The default comparison for bare flag checks is `> 0`, not boolean existence. A flag set to 0 exists but fails the default check. Use `value = 0` to check for explicit zero values.

## Scope Validation

Triggers automatically validate against the current scope type but fail silently in wrong scopes:

```hoi4
# In state scope:
has_government = democratic  # Country trigger - returns FALSE, no error
```

This silent failure makes debugging difficult. Always verify trigger scope requirements match the execution context.

### Dynamic Tag Resolution

`original_tag` matches dynamic countries while `tag` does not:

```hoi4
original_tag = GER  # Matches GER, D01, D02, etc.
tag = GER           # Matches only base GER
```

Use `original_tag` when civil wars or dynamic countries are relevant.

### Variable Scoping

Variables must reference their creation scope when accessed from different contexts:

```hoi4
set_variable = { my_var = 100 }  # Created in country scope

# Later, in different scope:
ROOT = {
    check_variable = { my_var > 50 }  # Must reference ROOT's variable
}
```

## Common Trigger Patterns

### Days Since Events

Several triggers return extremely large numbers when the checked event never occurred:

```hoi4
days_since_capitulated > 30
```

> [!CRITICAL] If the country has never capitulated, `days_since_capitulated` returns an extremely large number (effectively infinity), making `> 30` evaluate to true. Always combine with existence checks:

```hoi4
has_capitulated = yes
days_since_capitulated > 30
```

This pattern applies to all `days_since_*` triggers.

### Equipment Checks

**stockpile_ratio:** Checks fielded equipment ratio (equipped vs. total available)

**Convoy equipment:** Uses direct amount, not percentage:

```hoi4
has_equipment = {
    convoy > 100  # Checks for 100+ convoys (not a ratio)
}
```

This is inconsistent with other equipment types which generally use ratios.

### Strength Ratio

The strength ratio calculation includes a hidden modifier:

```hoi4
strength_ratio = {
    tag = GER
    ratio > 1.0
}
```

Formula: `fielded_divisions(current) / fielded_divisions(target)` OR 1 if target has zero divisions.

The current scope receives a hidden +10% modifier if it has a stronger air force than the target. This is not documented in the tooltip.

### War Triggers

**has_war_with_wargoal_against:** Joining an ally's war does NOT count as having a wargoal. Only wars initiated with your own justification or focus-generated wargoals count.

**any_war_score:** Checks WAR PROGRESS (how close to victory), not WAR PARTICIPATION (contribution percentage). These are different systems.

## Character and Advisor Triggers

### Version-Dependent Behavior

Pre-1.12 vs Post-1.12 for role-checking triggers:

**Pre-1.12:**
```hoi4
is_air_chief = yes  # True if character EVER HAD the role
is_army_chief = yes
```

**Post-1.12:**
```hoi4
is_air_chief = yes  # True if character IS CURRENTLY SELECTED in role
is_army_chief = yes
```

**is_hired_as_advisor:** Checks if character is hired in ANY advisor slot, not a specific role.

### Template and Division Triggers

**has_template_majority_unit:** Division must be >50% of the specified battalion type:

```hoi4
has_template_majority_unit = infantry
# True only if >50% of combat width is infantry battalions
```

**divisions_in_state:** Counts divisions where the majority battalion type matches the filter:

```hoi4
divisions_in_state = {
    state = 42
    type = armor
    size > 5
}
```

## Railway and Infrastructure

**has_railway_level:** Level 0 does not work as a valid check - only levels 1-5 are valid:

```hoi4
has_railway_level = 0  # INVALID - always false
has_railway_level = 1  # Valid
```

Railway connection can exist via naval crossings (straits, sea zones with naval access). Check connectivity separately from rail level if naval crossings matter.

## Resistance System

Resistance never auto-initiates unless explicitly configured:

**Global setting:**
```hoi4
should_initiate_resistance = yes  # In scripted trigger
```

**State-specific:**
```hoi4
should_initiate_resistance_<state_id>_<state_id> = yes
```

State-specific triggers override the global setting. Without any `should_initiate_resistance` trigger returning yes, occupied states never generate resistance.

## Occupation Law Context

**In country scope:** Checks PREV's occupation law over the current country:

```hoi4
GER = {
    POL = {
        has_occupation_policy = brutally_oppressive
        # Checks GER's policy over POL
    }
}
```

**In state scope:** Checks the occupation law applied to that state:

```hoi4
42 = {
    has_occupation_policy = brutally_oppressive
    # Checks policy applied to state 42
}
```

## Scripted Triggers

Defined in `common/scripted_triggers/*.txt`:

```hoi4
my_trigger_name = {
    has_war = yes
    has_capitulated = no
    num_of_factories > 50
}
```

Usage:
```hoi4
my_trigger_name = yes
my_trigger_name = no  # Inverted check
```

Multiple definitions of the same trigger name: the last evaluated file wins (based on ASCII filename order).

### Diplomacy Triggers

Special pattern for modifying diplomatic action availability:

```hoi4
DIPLOMACY_<ACTION>_ENABLE_TRIGGER = {
    # Custom conditions for diplomatic action
}
```

These scripted triggers directly modify whether diplomatic actions appear as available.

## Meta Triggers

Meta triggers enable dynamic text replacement in tooltips:

```hoi4
text = {
    has_equipment = {
        [EQUIPMENT] > 100
    }
}
```

Square brackets `[EXAMPLE]` mark dynamic replacement points. The actual equipment type is substituted at evaluation time.

Add `debug = yes` to log the final output to game.log for debugging:

```hoi4
text = {
    debug = yes
    has_equipment = { [EQUIPMENT] > 100 }
}
```

## Documentation

Complete trigger documentation: `documentation/triggers_documentation.html` (in game installation directory)

## Related Defines

- `MAX_EFFECT_ITERATION`: See [NGame](/defines_list/NGame.md)
