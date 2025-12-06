---
domain: entities
concept: ideologies
version: 1.14+
requires: [country_tags]
relates: [characters, country_history, localisation]
---

# Ideology System

HOI4 uses a two-tier ideology system: ideology groups (broad political alignments) and ideology types (specific sub-ideologies within groups). Understanding the distinction between these tiers is essential for correctly configuring countries, characters, and political mechanics.

## Ideology Groups vs Ideology Types

**Ideology groups** are the top-level political categories displayed prominently in the game interface:
- `democratic`
- `communism`
- `fascism`
- `neutrality`

**Ideology types** are specific sub-ideologies within each group:
- Democratic group: `liberalism`, `conservatism`, `socialism`
- Communist group: `marxism`, `leninism`, `stalinism`, `maoism`
- Fascist group: `nazism`, `fascism_ideology`, `falangism`, `rexism`
- Neutrality group: `despotism`, `oligarchism`, `moderatism`, `centrism`

## Usage Contexts

The distinction between groups and types matters in different scripting contexts:

**Country leader ideology:** Country leaders use ideology types (sub-ideologies):

```hoi4
country_leader = {
    ideology = socialism  # Ideology type, not group
    traits = { trait_token }
}
```

**Ruling party:** The `set_politics` effect uses ideology groups:

```hoi4
set_politics = {
    ruling_party = communism  # Ideology group, not type
    elections_allowed = yes
}
```

**Localization keys:** Country names use different keys for groups versus types:

- `TAG_ideology` uses the ideology group (e.g., `GER_communism`)
- `TAG_ideology_type` uses the ideology type (e.g., `GER_marxism`)

Both keys support the standard `_DEF` and `_ADJ` variants for definition and adjective forms.

## Party Leadership

> [!CRITICAL] The first recruited character per ideology group becomes that party's leader. If `set_politics` is called before character recruitment and no leader exists for the ruling party's ideology group, the game automatically creates a random character as party leader.

This automatic character generation prevents subsequently recruited characters from becoming party leader, as leadership is already assigned. Always recruit characters before calling `set_politics` in country history files.

### Multiple Leaders

When multiple country leaders exist for the same ideology group, the first recruited character becomes the party leader by default. Use `promote_character` to change party leadership:

```hoi4
promote_character = character_id
```

This effect promotes the specified character to party leader for their ideology group, replacing the current leader.

## Political System Integration

### Party Popularity

Party popularity represents public support for ideology groups, not specific ideology types:

```hoi4
set_popularities = {
    democratic = 30
    communism = 20
    fascism = 40
    neutrality = 10
}
```

Values must sum to exactly 100. These percentages affect drift toward and away from ideologies, civil war triggers, and public opinion events.

### Government Changes

When changing governments via coup, civil war, or political events, the ruling party switches at the ideology group level. The specific ideology type of the new government is determined by the party leader's defined ideology type.

## Localization Priority

Localization for country names follows a priority system when multiple keys are defined:

1. `TAG_autonomy_state_OVERLORD` (most specific)
2. `TAG_autonomy_state`
3. `TAG_OVERLORD_subject`
4. `TAG_subject`
5. `TAG_ideology_type` (specific sub-ideology)
6. `TAG_ideology` (group)
7. `TAG` (base name)

Ideology-based localization applies when the country has a ruling party matching the ideology group or type specified in the key.

## Ideology Definition

Ideology groups and types are defined in `common/ideologies/*.txt`:

```hoi4
ideologies = {
    fascism = {  # Ideology group
        types = {
            nazism = {  # Ideology type
                # Type-specific attributes
            }
            
            fascism_ideology = {
                # Type-specific attributes
            }
        }
        
        # Group-level attributes
        dynamic_faction_names = { ... }
        color = { 150 50 50 }
    }
}
```

Group-level attributes apply to all types within the group, while type-specific attributes override or extend group defaults.

## Dynamic Faction Names

Ideology groups can define dynamic faction names that change based on the faction leader's ideology:

```hoi4
dynamic_faction_names = {
    "FACTION_NAME_DEMOCRATIC_1"
    "FACTION_NAME_DEMOCRATIC_2"
    "FACTION_NAME_DEMOCRATIC_3"
}
```

The game randomly selects from available names when creating a faction. This provides variety without requiring unique names for each country.

## Ideology Triggers and Effects

Common triggers and effects that interact with the ideology system:

**Triggers:**
- `has_government = ideology_group` (checks ruling party)
- `has_idea_with_trait = ideology_group` (checks country leader traits)
- `has_country_leader = { character = character_id }` (checks active leader)

**Effects:**
- `set_politics = { ruling_party = ideology_group }` (changes government)
- `add_popularity = { ideology = ideology_group value = 0.1 }` (modifies support)
- `set_party_name = { ideology = ideology_group name = "loc_key" }` (renames party)

## Ideology and Country Leaders

Country leaders are tied to their ideology type permanently. Changing a character's ideology requires:

1. Removing their current country leader role
2. Adding a new country leader role with the desired ideology type

Leaders cannot dynamically switch ideology types while maintaining their role. This design ensures ideological consistency and prevents nonsensical political shifts.

## Related Systems

For character recruitment timing and party leadership selection, see [Characters](/entities/characters.md).

For country history political setup, see [Country History](/entities/country_history.md).

For localization priority and naming conventions, see [Country Tags](/entities/country_tags.md).
