---
domain: core
concept: console_commands
version: 1.14+
requires: [scripting_data_types]
relates: [debug_tools, effects]
---

# Console Commands

The console provides interactive access to debug commands and cheat functionality for testing and development. Understanding command behavior and limitations helps streamline the modding workflow.

## Console Access

### Opening the Console

The console is only available in non-ironman games. Multiple keyboard keys can open it depending on keyboard layout:

`^`, `°`, `~`, `Shift+2`, `§`, `\`, `` ` ``, `"`, `ALT+2+1`, `Shift+3`

Use up and down arrow keys to navigate command history.

### Command Syntax

Console documentation uses the following notation:

- `()` indicates an alias for the command
- `[]` indicates optional parameters
- `[<>]` indicates mandatory parameters

## ID Discovery

### Debug Command

The `debug` command (without arguments) toggles display of internal IDs:

- National focus IDs
- Idea IDs
- Technology IDs
- State IDs
- Province IDs
- Country tags

This visual overlay is essential for identifying targets for console commands and scripting.

### Localisation Search

When you know the display text but not the ID, search `localisation/english/` directory files for the visible text. The localisation key serves as the ID in most cases.

## Country Switching

**tag [<TAG>]:** Switch to controlling the specified country

**observe:** Enter observer mode with no controlled country

Using observer mode interferes with AI performance evaluation. The AI behaves differently when observed, so performance testing should occur without observer active.

## Resource Commands

Resource commands grant various strategic resources and currencies:

| Command | Default Amount | Cap | Notes |
|---------|----------------|-----|-------|
| `pp` | 1000 | None | Political power |
| `manpower` | 10,000,000 | None | Recruitable population |
| `fuel` | Variable | Deposits capacity | Adding far beyond capacity decreases fuel |
| `cp` | Variable | 100 | Command power |
| `st` | Variable | 100 | Stability |
| `ws` | Variable | 100 | War support |
| `xp` | Variable | None | Can only be used once per day |

> [!CRITICAL] The fuel command caps at your deposits capacity. Adding significantly more than capacity causes fuel to decrease rather than increase. Stay near your actual storage limit.

Experience (xp) grants are limited to once per 24-hour in-game period. Repeated use within the same day has no effect.

## Equipment Commands

**add_equipment (ae) [<amount>] [<equipment>]:** Add equipment of specified type

**add_latest_equipment (ale) [<amount>] [<type>]:** Add latest variant of equipment archetype

## MIO, Market, Special Projects, and Debug Expansions (1.14+)

Recent builds added many commands for Military Industrial Organisations, the International Market, and Special Projects, plus release-build gating for some debug tools. Common groups:

- **MIO funds/capacity/size**: `AddFunds`, `AddSize`, `AddTaskCapacity` (aliases: `mio.*`, `IndustrialOrganisation.*`) with optional org token and amounts.
- **Market**: `InternationalMarket.*` commands for subsidies, requests, reservations, pricing, and automation toggles.
- **Special Projects**: `sp_add_scientist`, `sp_add_scientist_level`, `sp_add_scientist_trait`, `sp_fast`, `sp_instant`, `sp_unlock_all`, etc., for scientist roles and project pacing.
- **Agency/Operations**: `Agency.Instant`, `Operation.Instant`, `operation_start`, `operation_test_phase_selection`, `endrids/prepareraids` for raids.
- **Debug/tweakables**: Many commands are unavailable in release builds; check in-game availability. Tweakable variables can be toggled/set directly (see in-game `trigger_docs`/`effect_docs`/`docs`).

> [!NOTE] Keep alias awareness (e.g., `AddFunds`, `mio.AddFunds`) and argument order. Release builds may hide certain debug commands; verify before documenting for players.

The `add_equipment` command does not support naval equipment except `convoy_1`. For equipment variants, use the exact given name as it appears in the definition file.

## Construction and Research

**instantconstruction (ic):** Toggle instant construction and unit production

This command affects AI behavior - when active, AI ships also build instantly and AI construction decisions change. The AI behavior modification can skew testing results.

**research [<technology>]:** Complete specific technology research

**research_on_icon_click (roic):** Toggle instant research on clicking tech icons. This bypasses both prerequisites and mutual exclusivity, allowing invalid tech combinations.

**reloadtechnologies:** Reload technology database from files

## Focus Commands

**Focus.AutoComplete (fa):** Bypass focus completion time

**Focus.NoChecks:** Ignore focus available conditions

**Focus.IgnorePrerequisites:** Bypass prerequisite requirements

**freefocuses (ff):** Make all focuses instantly available

These commands affect AI focus selection. When AI uses focuses instantly, their strategic behavior changes significantly.

## Decision Commands

**Decision.NoChecks:** Ignore decision available conditions

**Decision.FastRemove:** Instant decision timeout removal

**finish_decision [<decision>]:** Complete decision with specified ID

## Training Commands

**instanttraining (it):** Toggle instant division training and experience gain

## Diplomacy Commands

**allowdiplo (nocb):** Remove diplomatic action restrictions

**ai_accept:** Force AI to accept all diplomatic proposals

**add_opinion [<source>] [<target>] [<amount>]:** Modify opinion between countries. The amount parameter is ignored - the command always grants exactly 100 opinion with the modifier "cheat_opinion_modified_good".

**whitepeace (wp) [<TAG>] [<TAG>]:** Create peace between two countries

**annex [<TAG>]:** Annex target country to current player

**puppet [<TAG>]:** Make target country a puppet of current player

## Intelligence Commands

**Agency.Instant:** Toggle instant agency upgrades

**Operation.instant:** Toggle instant operation completion

**prevent_operative_detection:** Prevent operative capture

## Territory Commands

**setowner [<state_id>] [<TAG>]:** Transfer state ownership. You must click the state first - direct state ID input no longer works.

**setcontroller [<state_id>] [<TAG>]:** Transfer state control

**occupationpaint (op) [<TAG>]:** Occupy all owned land provinces of specified country. Note this occupies owned provinces, not controlled ones - it won't occupy territory the country controls but doesn't own.

**add_core [<state_id>] [<TAG>]:** Add core to state

The `remove_core` command is broken and does not function.

## Variable and Flag Commands

**set_var [<variable>] [<value>]:** Set variable in current scope

**get_var [<variable>]:** Display variable value

**list_vars:** List all variables in current scope (context-sensitive based on selection)

**set_country_flag [<flag>]:** Set country flag in current scope. This does not work with another nation's tag parameter even if the console confirms success - it only affects the currently selected country.

**set_global_flag [<flag>]:** Set global flag

**list_flags:** List flags based on current selection - nothing selected shows global flags, country selected shows country flags, state selected shows state flags.

## Scripting Commands

**event [<event_id>]:** Fire event in current scope. Shows which triggers were met and unmet if the event has a trigger block, useful for debugging event conditions.

**trigger [<trigger>]:** Evaluate trigger expression

**eval_trigger [<trigger>]:** Evaluate trigger in currently selected scope

**effect (e) [<effect>]:** Execute effect

**eval_effect [<effect>]:** Execute effect in currently selected scope

The `eval_trigger` and `eval_effect` commands execute within the currently selected scope - use country selection, state selection, or unit selection to change context.

## AI Commands

**ai [<TAG>]:** Without parameters, toggles AI for all countries. With parameters, creates exceptions - the specified countries maintain AI while others don't.

**aiview:** Toggle AI strategic planning overlay

**human_ai [<TAG>]:** Make AI play with human-accessible mechanics. Creates logs at `logs/scripted_ai.log`.

**ai_invasion [<TAG>]:** Toggle AI naval invasions for specified country

## Debug Commands

**tdebug:** Toggle debug information display

**error:** Toggle extended error logging

**fow:** Toggle fog of war

**collision:** Toggle collision boxes display

## Reload Commands

**reload [<file>]:** Reload database files. Also accepts individual `interface/*.gui` files for targeted interface reloading.

**reloadoob:** Reload order of battle files

**reloadinterface:** Reload all interface files

**update_loc:** Reload localisation files

**updateequipments:** Reload equipment definitions

**updatesubunits:** Reload unit definitions

**reloadfx:** Reload particle effects

## Camera Commands

**goto_province [<id>]:** Move camera to province

**goto_state [<id>]:** Move camera to state

## Special Projects Commands

**sp_instant:** Instant special project research

**sp_fast:** Fast special project research

**sp_available:** Make special project available

**sp_breakthrough:** Complete special project breakthrough

**sp_add_scientist:** Add scientist to facility

**sp_set_selected_scientist_level [<level>]:** Set scientist level. The facility GUI with assigned scientist must be open for this to work.

## Special Command Behaviors

**threat 999999999:** Resets world tension to 0 rather than setting it to maximum

**acclimization [<type>] [<value>]:** Setting one climate type resets the opposite climate to 0%

**random_seed [<value>]:** The AI uses this seed for all focus and decision choices. Changing the seed rerolls AI strategic behavior, allowing repeated testing of different AI decision paths.

**gain_xp [<trait>]:** Only gainable traits work - not all traits are assignable through experience gain

**ai_front_dump:** Requires a unit to be selected or the command fails

**instant_prepare:** Only functions in debug mode

## Deprecated and Broken Commands

The following commands have been removed or don't function:

**winwars:** Removed as of patch 1.9.1

**debug_nuking:** Removed as of patch 1.15.1

**remove_core:** Broken - does not work

## Command Defaults

When commands accept optional amount parameters, defaults are:

- **manpower:** 10,000,000
- **pp:** 1,000
- **addTaskCapacity:** 1
- **addSize:** 1
- **add_cic_bank:** 1

## DLC Dependencies

Some commands may not work depending on which DLC is installed. The game doesn't document these dependencies, so test commands with your target DLC configuration active.

## Related Systems

- Variable system details: See [Scripting Data Types](/core/scripting_data_types.md#variables)
- Debug mode features: See [Debug Tools](/core/debug_tools.md)
- Console debugging output: See [Debug Tools](/core/debug_tools.md#debugging-effects)
