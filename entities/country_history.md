---
domain: entities
concept: country_history
version: 1.14+
requires: [country_tags, ideologies, states]
relates: [characters, autonomy, factions]
---

# Country History System

Country history files define the starting state of nations including political setup, technology, military forces, and diplomatic relationships. These files execute as effect blocks when a scenario starts.

## File Structure

History files are located in `history/countries/` and must begin with the country's three-character tag. The remainder of the filename is cosmetic:

```text
history/countries/TAG - Any Description.txt
```

For example, `SCO - Bahrain.txt` is valid for Scotland because only the first three characters (`SCO`) are parsed.

### Multiple Files Per Country

A single country can have multiple history files which all load and merge together. Content is combined rather than overwritten when multiple files exist for the same tag.

### Execution Order

History files execute in the order tags appear in the `common/country_tags/*.txt` file. This order matters for operations that reset state, such as puppeting (which resets party popularity to the overlord's ideology).

> [!CRITICAL] Any unnecessary closing bracket `}` in a history file stops execution prematurely at that point. All content after the unexpected bracket is silently ignored, causing incomplete initialization without error messages.

## Core History Attributes

### Capital Assignment

```hoi4
capital = 123  # State ID
```

The province with the highest victory points in the specified state becomes the capital city. If multiple provinces have equal victory points, the selection is deterministic but based on internal ordering.

### Research and Stability

```hoi4
set_research_slots = 4
set_stability = 0.7
set_war_support = 0.5
```

Research slots default to 2 if not specified. Stability and war support are float values between 0.0 and 1.0.

### National Ideas

```hoi4
add_ideas = {
    idea_token_1
    idea_token_2
}
```

Ideas include national spirits, design companies, and laws. The `add_ideas` effect accepts multiple idea tokens in a single block.

### Technology

```hoi4
set_technology = {
    tech_token_1 = 1
    tech_token_2 = 1
}
```

Technology tokens reference definitions in `common/technologies/`. The value `1` indicates the technology is researched; only this value is valid in history files.

## Order of Battle System

> [!CRITICAL] Countries without any order of battle file suffer broken building construction. The `add_building_construction` effect fails silently until the country experiences a consumer goods change or the player reloads the game. Always assign an OOB file, even if empty.

### OOB Assignment Methods

Three methods exist for assigning order of battle files, with different timing and scoping behavior:

**`oob` (argument syntax):**

```hoi4
oob = "TAG_1936"
```

This is an argument, not an effect. It cannot be used inside `if` statements or conditional blocks. The OOB file loads during country initialization.

**`set_oob` (effect syntax):**

```hoi4
set_oob = "TAG_1936"
```

This is an effect that can be used in `if` statements and conditional logic. The OOB loads during country initialization.

**`load_oob` (immediate effect):**

```hoi4
load_oob = "TAG_1936"
```

This effect loads the OOB file immediately when the effect executes. It is not recommended because if the OOB contains divisions, the game crashes. If it contains equipment or units that require technologies not yet researched, errors occur. Use `set_oob` instead for standard initialization.

### Naval and Air OOB Overwriting

```hoi4
set_naval_oob = "TAG_navy"
set_air_oob = "TAG_air"
```

Unlike the standard OOB effects which might merge in some contexts, naval and air OOB assignments completely overwrite any previous definitions. Each country can have only one active naval OOB and one active air OOB.

### OOB and Focus Completion

National focus trees can be initialized as completed in OOB files using `instant_effect` blocks. However, focuses that should be marked as already completed at game start must be defined in the country history file itself, not in the OOB file. The OOB system only handles focuses that complete during the initialization process.

## Political System

### Party Popularity

```hoi4
set_popularities = {
    democratic = 30
    communism = 20
    fascism = 40
    neutrality = 10
}
```

Popularity percentages must sum to exactly 100. These values represent public support for each ideology group, not the power of the ruling party.

### Ruling Party

```hoi4
set_politics = {
    ruling_party = democratic
    last_election = "1936.1.1"
    election_frequency = 48
    elections_allowed = yes
}
```

The `ruling_party` attribute uses ideology groups (e.g., `democratic`, `communism`), not ideology types (e.g., `liberalism`, `marxism`). See [Ideologies](/entities/ideologies.md) for the distinction.

> [!CRITICAL] `set_politics` should always be placed after `recruit_character` commands. If `set_politics` executes first and no country leader exists for the ruling party's ideology group, the game creates a random character automatically. This random character becomes the party leader, preventing any subsequently recruited character from becoming leader.

## Character Recruitment

```hoi4
recruit_character = character_id
```

Character recruitment brings characters defined in `common/characters/*.txt` into active service for the country.

> [!CRITICAL] The `recruit_character` command must have at least one line after it in the file (even a blank line or comment). If it is the last line with no content after, the recruitment silently fails and the character does not join the country.

### Recruitment Timing

Always recruit characters before calling `set_politics`. The first recruited character per ideology group becomes that party's leader. Country leaders recruited after `set_politics` has executed do not become party leaders, as the leadership is already determined.

When multiple leaders exist for the same ideology group, the first recruited character becomes the party leader. Use `promote_character` to change leadership between scenario start dates.

## Diplomatic Relationships

### Subject Status

```hoi4
set_autonomy = {
    target = TAG
    autonomy_state = autonomy_integrated_puppet
    freedom_level = 0.4
}
```

> [!CRITICAL] `set_autonomy` must be placed before `set_popularities` and `set_politics`. The puppeting process resets party popularity and ruling party to match the overlord's ideology, overwriting any values set before the autonomy change.

It is recommended to place autonomy settings in the subject's history file rather than the overlord's history file. This avoids file load order issues that can cause the autonomy to apply at the wrong time relative to other initialization.

### Faction Membership

```hoi4
create_faction = faction_localization_key

add_to_faction = TAG
```

Puppets automatically join their overlord's faction when created, but it is recommended to include explicit `add_to_faction` commands to ensure correct initialization order and make the faction structure clear in the history file.

The `create_faction` effect uses a localization key, not a literal string. See [Factions](/entities/factions.md) for faction system details.

## Date-Dependent History

History files support date blocks that execute conditionally based on the scenario start date:

```hoi4
1939.1.1 = {
    # Effects here only apply when starting on dates STRICTLY LATER than 1939.1.1
    set_technology = {
        advanced_infantry_weapons = 1
    }
}
```

Date blocks use the format `YYYY.MM.DD = { ... }` and only execute when the scenario start date is strictly later than the specified date. Starting exactly on `1939.1.1` does not trigger a `1939.1.1` date block.

### Date Block Behavior

Date blocks have special handling for certain effects:

**OOB replacement:** An `oob` or `set_oob` command inside a date block completely replaces the previous OOB, it does not merge with it.

**Technology addition:** Technology definitions in date blocks add to existing technologies rather than replacing them.

**Ideas merging:** Ideas from date blocks merge with previous idea assignments.

### Conditional Logic in History

History files support `if` statements with triggers, but the `else` clause only works in nested form:

```hoi4
if = {
    limit = { has_dlc = "Together for Victory" }
    # Effects
    else = {
        # This works
    }
}

# Standalone else outside if block does NOT work
```

## Equipment Variants

```hoi4
create_equipment_variant = {
    name = "Panzer III Ausf. E"
    type = medium_tank_chassis_0
    parent_version = 0
    modules = {
        main_armament_slot = tank_small_cannon
        turret_type_slot = tank_light_one_man_tank_turret
    }
    icon = "GFX_GER_basic_medium_tank_medium"
    obsolete = no
}
```

Equipment variants are DLC-dependent features. The `create_equipment_variant` effect in history files allows countries to start with pre-configured equipment designs that match their historical vehicle variants.

## Related Systems

For character recruitment details and role assignment, see [Characters](/entities/characters.md).

For ideology type versus ideology group distinction, see [Ideologies](/entities/ideologies.md).

For autonomy state configuration and subject mechanics, see [Autonomy](/entities/autonomy.md).
