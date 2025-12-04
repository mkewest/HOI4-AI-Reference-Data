---
domain: entities
concept: factions
version: 1.14+
requires: [country_tags]
relates: [diplomacy, war_mechanics, ideologies]
---

# Faction System

Factions are military alliances between countries that fight together in wars and share resources. The modern faction system uses template-based creation with customizable rules, goals, and influence mechanics.

## Faction Creation

> [!CRITICAL] The `create_faction` effect is obsolete and should not be used. Always use `create_faction_from_template` instead. Template-based factions have different behavior and capabilities compared to legacy factions.

### Template-Based Creation

```hoi4
create_faction_from_template = {
    template = faction_template_token
    name = faction_name_loc_key
    color = { 255 0 0 }
}
```

Faction templates are defined in `common/factions/templates/*.txt` and specify the faction's structure, rules, and available features.

### Legacy Creation

```hoi4
create_faction = faction_name_loc_key
```

This effect creates a simple faction without template features. It remains for backwards compatibility but lacks the influence system, member upgrades, and advanced rules available through templates.

## Faction Structure Files

The faction system uses multiple file types in `common/factions/`:

**Templates** (`templates/*.txt`): Define faction structure and allowed features
**Rules** (`rules/*.txt`): Control faction behavior and member permissions
**Goals** (`goals/*.txt`): Define faction objectives and completion conditions
**Member Upgrades** (`member_upgrades/*.txt`): Allow member countries to gain bonuses
**Icons** (`icons/*.txt`): Specify faction UI icons and symbols

## Faction Membership

### Adding Members

```hoi4
add_to_faction = TAG
```

The `add_to_faction` effect targets a specific country and adds them to the faction of the country executing the effect. It operates in country scope.

Puppets automatically join their overlord's faction when created, but explicitly adding them via `add_to_faction` is recommended to ensure correct initialization order.

### Removing Members

```hoi4
remove_from_faction = TAG
```

The `remove_from_faction` effect can target any country in the faction and operates from country scope. It removes the specified country from the faction.

```hoi4
leave_faction = yes
```

The `leave_faction` effect must execute in the leaving country's scope and removes that country from its current faction.

## Faction Leadership

### Leadership Requirements

Two triggers determine leadership eligibility:

```hoi4
has_manpower_to_become_leader = yes
has_industry_to_become_leader = yes
```

**Manpower comparison:** The `has_manpower_to_become_leader` trigger compares the candidate country's manpower against the current faction leader and all its subjects combined. This includes puppet manpower in the calculation.

**Industry comparison:** The `has_industry_to_become_leader` trigger compares only factory counts, excluding subject factories from the calculation.

These asymmetric comparisons mean manpower-rich countries with many puppets have an advantage in maintaining leadership, while industrial powerhouses without large subject networks can challenge based on factory count alone.

### Changing Leadership

```hoi4
set_faction_leader = TAG
```

The `set_faction_leader` effect operates on the faction itself (when scoped into a faction) and changes the faction leader to the specified country. The target country must be a faction member.

```hoi4
set_faction_spymaster = TAG
```

The `set_faction_spymaster` effect designates a member as the faction's intelligence coordinator, granting them coordination bonuses for operations.

## Faction Influence System

The influence system tracks each member's contribution to the faction and determines their voice in faction decisions.

### Influence Sources

Influence comes from multiple sources with dedicated modifiers:

```yaml
faction_influence_war_score_factor: Contribution from combat and war participation
faction_influence_industrial_capacity_factor: Contribution from factory output
faction_influence_garrison_support_provider_factor: Contribution from providing garrison forces
faction_influence_garrison_support_reciver_factor: Penalty/bonus for receiving garrison support
faction_influence_expeditionary_force_provider_factor: Contribution from providing expeditionary forces
faction_influence_expeditionary_force_reciver_factor: Penalty/bonus for receiving expeditionary forces
```

These modifiers apply multiplicatively to the base contribution from each source.

### Influence Effects

```hoi4
add_faction_influence_score = 100
```

The `add_faction_influence_score` effect adds a flat amount of influence points to a country. It executes in country scope and targets the country's current faction.

```hoi4
add_faction_influence_ratio = 0.1
```

> [!CRITICAL] The `add_faction_influence_ratio` effect calculates based on the faction's total influence, not the individual country's influence. A ratio of 0.1 adds 10% of the entire faction's combined influence to the specified country.

This can result in massive influence gains if used with large faction totals. Design influence-granting events carefully to avoid unintended power shifts.

### Influence Queries

```hoi4
faction_influence_score > 500
faction_influence_ratio > 0.15
faction_influence_rank < 3
```

These triggers check a country's influence standing:
- `faction_influence_score`: Absolute influence points
- `faction_influence_ratio`: Percentage of total faction influence (0.0 to 1.0)
- `faction_influence_rank`: Rank position within faction (1 = highest influence)

## Faction Goals

Factions can have active goals that provide bonuses or direction:

```hoi4
add_faction_goal = {
    goal = goal_token
}

remove_faction_goal = {
    goal = goal_token
}
```

Goals are defined in `common/factions/goals/*.txt` and can have completion conditions, progress tracking, and rewards.

### Goal State Checking

```hoi4
has_faction_goal = goal_token
has_completed_faction_goal = goal_token
```

> [!CRITICAL] The `has_faction_goal` trigger returns true for both active and completed goals. Use `has_completed_faction_goal` to check specifically for completed goals only.

This distinction matters when checking whether a goal is in progress versus finished. Using `has_faction_goal` when you mean `has_completed_faction_goal` causes logic errors in completion rewards and follow-up goals.

## Faction Manifests

Manifests are the faction's primary objective, distinct from regular goals:

```hoi4
set_faction_manifest = {
    manifest = manifest_token
}
```

Manifests represent the faction's overarching purpose and typically have more significant effects than regular goals. Only one manifest can be active at a time.

```hoi4
faction_manifest_fulfillment > 0.5
```

The `faction_manifest_fulfillment` trigger checks progress toward completing the current manifest as a percentage (0.0 to 1.0).

## Faction Rules

Rules control faction behavior and member permissions:

```hoi4
set_faction_rule = {
    rule = rule_token
    enable = yes
}
```

Rules are defined in `common/factions/rules/*.txt` and can enable or restrict various actions such as:
- Declaring war without faction leader approval
- Kicking members from the faction
- Inviting new members
- Separate peace treaties
- Resource sharing

## Faction Power Projection

```hoi4
faction_power_projection > 100
```

The `faction_power_projection` trigger measures the faction's military and economic strength on a scale that combines factory output, military size, and strategic resource control.

## Faction Scoping

Most faction-related triggers operate in country scope and check the country's current faction membership:

```hoi4
# In country scope
if = {
    limit = { has_faction_goal = goal_token }
    # Checks if this country's faction has the goal
}
```

Effects that target the faction itself require explicit faction scope:

```hoi4
# Effects that operate on faction itself
set_faction_leader = TAG
set_faction_spymaster = TAG
set_faction_name = loc_key
```

The `leave_faction` effect must be called from country scope (the leaving country), while `remove_from_faction` can target any member.

## Faction Names and Colors

```hoi4
set_faction_name = "FACTION_NAME_LOC_KEY"
```

Faction names use localization keys that can include ideology-specific variants. Dynamic faction names are defined in ideology files and automatically select based on the faction leader's government.

Faction colors are set during creation with the `color` attribute in the `create_faction_from_template` effect. Colors affect map display and faction UI elements.

## Faction Dissolution

```hoi4
dismantle_faction = yes
```

The `dismantle_faction` effect dissolves the faction entirely, removing all members and destroying the faction structure. This effect executes in country scope and dismantles that country's faction.

When a faction leader leaves via `leave_faction`, the faction automatically selects a new leader from remaining members based on influence or industry. If no valid leader exists, the faction dissolves.

## Related Systems

For country tag requirements and faction membership scripting, see [Country Tags](/entities/country_tags.md).

For ideology-based dynamic faction names, see [Ideologies](/entities/ideologies.md).

For diplomatic effects and faction formation in country history, see [Country History](/entities/country_history.md).

## Related Defines

- `FACTION_INFLUENCE_DAILY_GAIN`: See [NDiplomacy](/defines_list/NDiplomacy.md)
- `FACTION_LEADER_CHANGE_INFLUENCE_THRESHOLD`: See [NDiplomacy](/defines_list/NDiplomacy.md)
