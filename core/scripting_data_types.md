---
domain: core
concept: scripting_data_types
version: 1.14+
requires: [file_syntax]
relates: [scripting_effects, console_commands]
---

# Scripting Data Types

HOI4 provides several data structures for storing and manipulating state during gameplay. These types form the foundation of dynamic scripting and enable complex logic flows.

## Constants

Constants define reusable values using the `@` prefix:

```hoi4
@PP_COST = 150
@TAG_NAME = GER

idea = {
    cost = @PP_COST
    available = { tag = @TAG_NAME }
}
```

Constants are file-local in scope and can be defined anywhere in the file. Both numeric and string types are supported.

> [!CRITICAL] String constants only work in triggers and element attributes, never in effects. Using string constants in effect blocks causes "invalid database object" errors. This makes them primarily useful for conditions and GUI element configuration.

## Flags

Flags are binary state indicators that persist until explicitly cleared.

### Flag Scoping

```hoi4
set_country_flag = my_flag
set_global_flag = world_state
set_state_flag = local_condition
```

Flags scope to specific entities (country, state, unit leader, etc.) or globally. Each scope maintains its own namespace.

### Flag Behavior

Flag values persist when set, even if the value is 0. Use `clr_flag` to truly remove a flag from memory. The `modify_<scope>_flag` effects do nothing if the flag was never set - they don't initialize to 0 automatically.

The `has_flag` trigger's "days" parameter checks days since the flag was set, not days remaining. This is useful for tracking how long a condition has existed.

### Targeted Flags

Flags support targeting with the `@TAG` suffix:

```hoi4
set_country_flag = alliance_@GER
has_country_flag = alliance_@GER
```

This is pure string concatenation - `alliance_@GER` becomes `alliance_GER`. Each flag can only have one `@` target. Complex targeting like `@PREV.PREV` does not work.

Unit leader flags are deprecated and will be removed in future versions. Avoid using them in new content.

### Performance Considerations

Flags are more optimized than variables for boolean values in both memory usage and execution speed. When you only need true/false state without numeric values, prefer flags.

## Variables

Variables store numeric values with scoped persistence.

### Variable Declaration

```hoi4
set_variable = { var = my_var value = 100 }
set_variable = { global.world_var = 50 }
```

Variables use dotted notation for scoping. The `global.` prefix is mandatory for global variables, unlike other scopes where the default is the current scope.

### Variable Access

```hoi4
THIS.var_name        # Current scope
ROOT.var_name        # Root scope in effect chain
ABC.capital:var_name # Chained scope with colon for variables
```

Variable chaining uses different separators: dot (`.`) for static scope navigation and colon (`:`) for variable access after scope changes. The syntax `ABC.capital:var_name` reads as "ABC's capital's variable."

The `var:` prefix is optional in some contexts but causes errors in others. For consistency and safety, always include it when referencing variables in checks.

### Variable Operators

Variables support arithmetic operations:

- **set, set_random, clear:** Assignment and removal
- **add, subtract, multiply, divide, modulo:** Arithmetic
- **round, clamp:** Value manipulation

Comparison operators for triggers:

- **equals, not_equals:** Equality checks
- **less_than, less_than_or_equals:** Magnitude comparisons
- **greater_than, greater_than_or_equals:** Magnitude comparisons

### Variable Edge Cases

Unset variables default to 0 in checks rather than causing errors. This can mask logic bugs where you expect an unset variable to be distinguishable from zero.

> [!CRITICAL] Variables overflow at ±2,147,483.648. Adding beyond this limit wraps to the opposite extreme, creating severe bugs in accumulation logic.

The `round_variable` effect rounds 0.5 to the larger absolute value: -1.5 rounds to -2, while 1.5 rounds to 2. The `clamp_variable` effect only affects the current value - variables can exceed limits in subsequent operations.

Temporary variables may not persist through scripted effects and triggers. Their behavior is inconsistent, so use regular scoped variables when persistence across effect boundaries is required.

### Null Coalescing

The null coalesce operator `?` provides default values for unset variables:

```hoi4
var?100  # Returns 100 if unset, 0 if set to 0
```

This distinguishes between unset variables and variables explicitly set to zero.

### Variable Targeting

Variables support targeting similar to flags:

```hoi4
set_variable = { var = score_@GER value = 50 }
```

Using variables with token pasting is far more optimized than meta-effect token concatenation. Prefer `var_name_@TAG` over meta-effects for dynamic variable names.

Note that multiple target specifiers like `@TAG1_@TAG2` exhibit extremely inconsistent behavior and should be avoided entirely.

## Arrays

Arrays store ordered collections of elements with zero-based indexing.

### Array Types

**Regular arrays:** Scoped and permanent, surviving between effect blocks

**Temp arrays:** Unscoped and temporary, only existing within the current block

```hoi4
add_to_array = { array_name = value }
array_name^0  # Access first element
array_name^num  # Get array size
```

### Array Operations

Available operations:

- **add_to_array, remove_from_array:** Element manipulation
- **clear_array, resize_array:** Size management
- **find_highest, find_lowest:** Value searches

Array triggers:

- **is_in_array:** Element existence check
- **any_of, all_of:** Iteration with value checks
- **any_of_scopes, all_of_scopes:** Iteration with scope checks

Loops:

- **for_each_loop, for_each_scope_loop:** Iteration
- **random_scope_in_array:** Random selection
- **while_loop_effect, for_loop_effect:** Conditional iteration

### Array Behavior

> [!CRITICAL] Never remove elements during `for_each_loop` iteration. This causes undefined behavior as the iterator becomes invalid. Collect elements to remove in a separate array and process after iteration completes.

Empty trigger blocks in `any_of` and `all_of` scopes always return true. For `any_of`, this causes immediate exit since the first element satisfies the condition.

Trigger scopes short-circuit evaluation: `all_<>` stops at the first false, while `any_<>` stops at the first true.

Loop iterations are limited to 1000 by default via `NDefines.NGame.MAX_EFFECT_ITERATION`. Exceeding this limit terminates the loop early.

Array elements are treated as variables - they must exist before modification operations. Attempting to modify a nonexistent element causes errors.

The `for_loop_effect` default comparison is `less_than`, meaning the end value is never actually processed. Use `less_than_or_equals` if you need inclusive ranges.

When using temporary variables in loop triggers, prefer if-blocks over direct limit checks due to scope evaluation inconsistencies.

## Event Targets

Event targets save scope references for later use.

### Target Types

**Regular event targets:** Persist through the effect block and all events fired within that block

```hoi4
save_event_target_as = my_target
event_target:my_target = { ... }
```

**Global event targets:** Persist permanently until manually cleared

```hoi4
save_global_event_target_as = persistent_target
clear_global_event_target = persistent_target
```

### Target Behavior

Event targets can be set to non-existing countries, allowing preparation for dynamic country creation. Setting an existing event target overwrites it with the new scope.

Some effect blocks prohibit event target creation, particularly scripted diplomatic actions. Plan target creation to occur before entering restricted contexts.

In localisation, event targets don't require the `event_target:` prefix - use `[my_target.GetName]` instead of `[event_target:my_target.GetName]`.

The `has_event_target` trigger checks target existence without referencing its scope.

## Token Values

Token values reference database entries dynamically.

```hoi4
set_variable = { var = my_idea value = token:generic_idea }
```

Token types include:

- **ideas, ideologies, technologies, equipment:** Game content
- **operations, characters, decisions, buildings:** Gameplay systems
- **script_enums:** Custom enumerations

Localisation functions `GetTokenKey` and `GetTokenLocalizedKey` retrieve token identifiers and display names respectively.

Character tokens change value when the character is promoted to unit leader, potentially breaking references that rely on stable token values.

## Country Tag Aliases

Tag aliases provide dynamic country references defined in `common/country_tag_aliases/*.txt`:

```hoi4
alias_name = {
    variable = my_var
    event_target = my_target
    global_event_target = global_target
    original_tag = GER
    targets = { TAG1 TAG2 }
    target_array = my_array
    country_score = scorer_name
    fallback = USA
}
```

Aliases can point to non-existing countries, making them useful for dynamic country systems. The `original_tag` scope prevents certain logged errors during evaluation.

Dynamic countries require a flag to be set in the `start_civil_war` effect for tag aliases to recognize them correctly.

Aliases are evaluated dynamically each time used rather than cached, ensuring they always reflect current game state.

## Scorers

Scorers evaluate countries numerically, defined in `common/scorers/country/*.txt`:

```hoi4
get_highest_scored_country = { scorer = my_scorer }
get_sorted_scored_countries = { scorer = my_scorer array = result_array }
```

Scorers support hot-reloading but behave unreliably. For consistent results, quit to menu and reload when modifying scorer definitions.

## MTTH Variables

Mean Time To Happen variables are defined in `common/mtth/*.txt` and accessed via:

```hoi4
set_variable = { var = result value = mtth:event_likelihood }
```

These provide probability calculations for event firing and decision weighting.

## Game Variables

Game variables provide read-only access to internal state:

```hoi4
global.countries  # Array of all countries
ROOT.num_divisions  # Division count
```

Documentation exists at `documentation/dynamic_variables_documentation` in the game files. Global game variables require the `global.` prefix (mandatory, unlike user-defined globals where it's just recommended).

See the scripting.json reference for complete listings of available game variables.

## Game Arrays

The game provides built-in arrays:

### Global Arrays

```yaml
countries: All country tags
majors: Major powers
states: All state IDs
ideology_groups: Available ideologies
operations: Intelligence operations
province_controllers: Province ownership
technology: Available technologies
```

### Country-Scoped Arrays

```yaml
allies: Allied countries
army_leaders: Military commanders
enemies: At-war countries
faction_members: Faction members
occupied_countries: Occupied territories
subjects: Puppet states
owned_states: Owned states
controlled_states: Controlled states
core_states: Core states
neighbors: Adjacent countries
researched_techs: Completed research
navy_leaders: Naval commanders
operatives: Intelligence operatives
exiles: Exiled governments
```

### State-Scoped Arrays

```yaml
core_countries: Countries with cores on this state
```

These arrays are populated automatically by the game and update dynamically as the game state changes.

## Related Systems

- File syntax and encoding: See [File Syntax](/core/file_syntax.md)
- Console variable commands: See [Console Commands](/core/console_commands.md#variables)
- Debugging variable output: See [Debug Tools](/core/debug_tools.md#debugging-effects)
