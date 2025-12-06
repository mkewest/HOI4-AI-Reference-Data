---
domain: database
concept: ideologies
version: 1.14+
requires: [localisation]
relates: [characters, ai_strategy, factions]
---

# Ideology System

Ideologies are defined in `common/ideologies/*.txt` within an `ideologies = {...}` root block. The system uses a two-tier structure: ideology groups contain multiple subideologies (also called ideology types).

## Structure

```hoi4
ideologies = {
    ideology_group = {
        types = {
            subideology_name = {
                can_be_randomly_selected = yes
                color = { 255 0 0 }
            }
        }
        
        dynamic_faction_names = {
            "FACTION_NAME_DEMOCRATIC_1"
            "FACTION_NAME_DEMOCRATIC_2"
        }
        
        color = { 100 150 200 }
        
        rules = {
            can_create_collaboration_government = yes
            can_declare_war_on_same_ideology = no
        }
        
        modifiers = {
            generate_wargoal_tension = 0.5
            drift_defence_factor = 0.5
        }
        
        war_impact_on_world_tension = 0.5
        faction_impact_on_world_tension = 0.25
        
        can_host_government_in_exile = yes
        can_be_boosted = yes
        can_collaborate = yes
        
        faction_modifiers = {
            stability_factor = 0.1
        }
    }
}
```

## Ideology Groups vs Subideologies

The distinction between groups and subideologies is critical:

- **Ideology group:** The broad category (e.g., democratic, fascism, communism)
- **Subideology:** Specific variants within that group (e.g., marxism, stalinism, maoism under communism)

Country leaders use the **subideology name**, not the group name:

```hoi4
create_country_leader = {
    ideology = marxism  # subideology name
    # NOT ideology = communism
}
```

> [!CRITICAL] Country leaders must exist for each subideology, or the game crashes when that ideology becomes the ruling party. Always define at least one leader per subideology you intend to use.

## Subideology Attributes

### types Block

The `types = {...}` block defines all subideologies within the group:

```hoi4
types = {
    national_socialism = {
        can_be_randomly_selected = yes
        color = { 150 75 0 }
    }
    fascism_ideology = {
        can_be_randomly_selected = no
        color = { 120 60 0 }
    }
}
```

### can_be_randomly_selected

Boolean. When `yes`, AI countries can randomly adopt this subideology through drift or events. When `no`, it must be assigned explicitly.

### color

RGB color array for the subideology. This overrides the group's color for countries using this specific subideology.

## Popularity System

Ideology popularities are set via effects:

```hoi4
set_popularities = {
    democratic = 45
    fascism = 30
    communism = 20
    neutrality = 5
}
```

> [!CRITICAL] The `set_popularities` effect requires values that sum to EXACTLY 100. Any other sum causes ideologies to break entirely, preventing popularity display, drift, and related mechanics from functioning.

## Rules

The `rules` block defines what actions countries with this ideology can perform:

| Rule | Type | Description |
|------|------|-------------|
| `can_create_collaboration_government` | bool | Can create collaboration governments in occupied states |
| `can_declare_war_on_same_ideology` | bool | Can justify war goals against same ideology group |
| `can_force_government` | bool | Can force government type in peace conferences |
| `can_send_volunteers` | bool | Can send volunteer forces to other countries |
| `can_puppet` | bool | Can puppet other countries |
| `can_lower_tension` | bool | Can perform actions that reduce world tension |
| `can_only_justify_war_on_threat_country` | bool | Restricts war justification to countries that are threats |
| `can_guarantee_other_ideologies` | bool | Can guarantee countries of different ideologies |

## Modifiers

Ideology modifiers affect world tension and diplomatic costs:

### Tension Modifiers

All tension modifiers use the range [0, 1] where higher values mean more tension generated:

```yaml
generate_wargoal_tension:
  range: [0, 1]
  desc: Tension from justifying war goals

join_faction_tension:
  range: [0, 1]
  desc: Tension from joining factions

lend_lease_tension:
  range: [0, 1]
  desc: Tension from lend-lease agreements

send_volunteers_tension:
  range: [0, 1]
  desc: Tension from sending volunteers

guarantee_tension:
  range: [0, 1]
  desc: Tension from guaranteeing independence
```

### Cost Factor Modifiers

Cost factor modifiers use the range [-1, 1] where 0 is neutral:

```yaml
take_states_cost_factor:
  range: [-1, 1]
  example: 0.25 = +25% cost to take states in peace conferences

annex_cost_factor:
  range: [-1, 1]
  example: -0.5 = -50% cost to annex in peace conferences

puppet_cost_factor:
  range: [-1, 1]
  example: 0.1 = +10% cost to puppet countries

drift_defence_factor:
  range: [-1, 1]
  example: 0.5 = +50% resistance to ideology drift
```

### Justify War Goal Modifier

```yaml
justify_war_goal_when_in_major_war_time:
  range: [0, 1]
  example: 0.5 = -50% time to justify war goals during major wars
  note: Lower values mean faster justification
```

## World Tension Impact

### war_impact_on_world_tension

Range: [-1, 1]

Modifies world tension generated when this ideology declares war. Negative values reduce tension, positive values increase it.

### faction_impact_on_world_tension

Range: [-1, 1]

Modifies world tension when this ideology creates or joins factions.

## Faction Modifiers

```hoi4
faction_modifiers = {
    stability_factor = 0.1
    political_power_gain = 0.25
}
```

Faction modifiers apply to all faction members, but only if the **faction leader** has this ideology.

> [!CRITICAL] Faction modifiers do NOT apply if a non-leader faction member has the ideology. Only the faction leader's ideology determines which faction modifiers are active for all members.

## Dynamic Faction Names

```hoi4
dynamic_faction_names = {
    "FACTION_NAME_DEMOCRATIC_1"
    "FACTION_NAME_DEMOCRATIC_2"
    "FACTION_NAME_DEMOCRATIC_3"
}
```

When a country of this ideology creates a faction, the game randomly selects one of these localisation keys for the faction name. This provides variety for player-created factions.

## Government-in-Exile and Collaboration

### can_host_government_in_exile

Boolean. When `yes`, countries of this ideology can host governments-in-exile from occupied nations.

### can_be_boosted

Boolean. When `yes`, this ideology can be boosted through espionage operations and events.

### can_collaborate

Boolean. When `yes`, collaboration governments can use this ideology.

## Localisation

Localisation files are in `localisation/english/parties_l_english.yml`:

### Standard Keys

| Key | Purpose |
|-----|---------|
| `<ideology>` | Adjective form (e.g., "democratic") |
| `<ideology>_noun` | Noun form (e.g., "democracy") |
| `<ideology>_desc` | Description for scenario selection |
| `<subideology>` | Subideology noun form |
| `<subideology>_desc` | Subideology description |

### Country-Specific Overrides

| Key | Purpose |
|-----|---------|
| `<TAG>_<ideology>` | Country name (e.g., "GER_democratic") |
| `<TAG>_<ideology>_ADJ` | Adjective form |
| `<TAG>_<ideology>_DEF` | With "the" article |
| `<TAG>_<subideology>` | Overrides ideology group name |
| `<TAG>:0` | Collaboration government name |

> [!CRITICAL] Country-specific subideology names (`TAG_<subideology>`) override ideology group names entirely. This allows fine-grained control over how different subideologies display for specific countries.

The `TAG:0` key provides the country name without ideology suffix, used specifically for collaboration governments.

### Description Length Limit

Ideology descriptions (`<ideology>_desc`) must be short - they display as only one line in the scenario selection screen. Keep them to a single sentence.

### Drift Localisation

Ideology drift modifiers use separate localisation in `modifiers_l_english.yml` with the key pattern `<ideology>_drift`.

## GFX Sprites

Ideology icons are defined in `interface/*.gfx` using a priority system:

### Sprite Priority

The game checks for sprites in this order:

1. `GFX_ideology_<TAG>_<n>` - Country + subideology specific
2. `GFX_ideology_<TAG>_<n>_group` - Country + ideology group
3. `GFX_ideology_<n>` - Generic subideology
4. `GFX_ideology_<n>_group` - Generic ideology group

Where `<n>` is the subideology or group name, and `<TAG>` is the country tag.

This allows custom icons for specific country-ideology combinations while falling back to generic icons.

## AI Peace Configuration

AI peace deal behavior is controlled by files in `common/ai_peace/*.txt`.

> [!CRITICAL] Without adjusted triggers in ai_peace files, the AI defaults to using `common/ai_peace/1_fascist.txt` regardless of what ideology it actually has. You must define or modify ai_peace files for each ideology to get correct AI behavior in peace conferences.

## History File Setup

### Setting Politics

```hoi4
set_politics = {
    ruling_party = democratic
    last_election = "1936.1.1"
    election_frequency = 48
    elections_allowed = yes
}
```

The `ruling_party` uses the ideology **group name**, not the subideology name.

### Setting Popularities

```hoi4
set_popularities = {
    democratic = 45
    fascism = 30
    communism = 20
    neutrality = 5
}
```

Must sum to exactly 100 (see Popularity System above).

### Creating Leaders

```hoi4
create_country_leader = {
    name = "Leader Name"
    ideology = national_socialism  # subideology name
    traits = { trait_id }
    picture = "GFX_portrait_name"
}
```

Use the **subideology name**, not the group name. Each subideology needs at least one leader defined to avoid crashes.

## Related Systems

For ideology drift modifiers and effects, see the static modifiers documentation.

For faction creation and management, see the factions documentation.

For government-in-exile mechanics, see the occupation documentation.
