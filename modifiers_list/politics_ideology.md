---
domain: modifiers_list
concept: politics_ideology
version: 1.14+
requires: [modifiers]
relates: [government, stability, war_support, ideology]
---

# Politics Ideology Modifiers

For modifier system mechanics, types, application methods, and critical behavioral edge cases, see [Modifier System](/scripting/modifiers.md).

Politics ideology modifiers affect government systems, stability, war support, ideology, diplomatic relations, manpower, and justification mechanics.

## Politics and Ideology

```yaml
acceptance:
  type: num
  decimals: 2
  desc: Acceptance of <ideology_group> Diplomacy

air_volunteer_cap:
  type: num
  decimals: 0

civil_war_involvement_tension:
  type: num
  decimals: 1

command_power_gain:
  type: num
  decimals: 2

command_power_gain_mult:
  type: num
  decimals: 0

conscription:
  type: num
  decimals: 2
  desc: Recruitable Population

conscription_factor:
  type: num
  decimals: 0
  desc: Recruitable Population Factor

defensive_war_stability_factor:
  type: num
  decimals: 2

drift:
  type: num
  decimals: 2
  desc: Daily <ideology_group> Support

drift_defence_factor:
  type: num
  decimals: 1
  desc: Ideology drift defense

enemy_declare_war_tension:
  type: num
  decimals: 1
  desc: Declare war tension on us

enemy_justify_war_goal_time:
  type: num
  decimals: 1
  desc: Justify war goal time on us

female_random_country_leader_chance:
  type: num
  decimals: 0

forced_surrender_limit:
  type: num
  decimals: 2

foreign_subversive_activities:
  type: num
  decimals: 0
  desc: Foreign subversive activities efficiency

generate_wargoal_tension:
  type: num
  decimals: 1
  desc: Generate war goal tension limit

generate_wargoal_tension_against:
  type: num
  decimals: 1

guarantee_cost:
  type: num
  decimals: 0

guarantee_tension:
  type: num
  decimals: 1
  desc: Guarantee tension limit

improve_relations_maintain_cost_factor:
  type: num
  decimals: 0

join_faction_tension:
  type: num
  decimals: 1

justify_war_goal_time:
  type: num
  decimals: 1

justify_war_goal_when_in_major_war_time:
  type: num
  decimals: 1

master_ideology_drift:
  type: num
  decimals: 2

max_command_power:
  type: num
  decimals: 0

max_command_power_mult:
  type: num
  decimals: 0

max_surrender_limit_offset:
  type: num
  decimals: 2
  desc: Minimum Surrender Limit

monthly_population:
  type: num
  decimals: 1

non_core_manpower:
  type: num
  decimals: 2

offensive_war_stability_factor:
  type: num
  decimals: 2

opinion_gain_monthly:
  type: num
  decimals: 1
  desc: Improve relations opinion

opinion_gain_monthly_factor:
  type: num
  decimals: 2

opinion_gain_monthly_same_ideology:
  type: num
  decimals: 1

opinion_gain_monthly_same_ideology_factor:
  type: num
  decimals: 2

party_popularity_stability_factor:
  type: num
  decimals: 2

political_power_cost:
  type: num
  decimals: 0
  desc: Daily Political Power Cost

political_power_factor:
  type: num
  decimals: 2

political_power_gain:
  type: num
  decimals: 2

recruitable_population:
  type: num
  decimals: 3
  desc: Additional Recruitable Population

recruitable_population_factor:
  type: num
  decimals: 2

send_volunteer_divisions_required:
  type: num
  decimals: 1
  desc: Divisions required for volunteer force

send_volunteer_factor:
  type: num
  decimals: 1

send_volunteer_size:
  type: num
  decimals: 0
  desc: Max volunteer force divisions

send_volunteers_tension:
  type: num
  decimals: 1

stability_factor:
  type: num
  decimals: 2

stability_weekly:
  type: num
  decimals: 2

stability_weekly_factor:
  type: num
  decimals: 2

subversive_activites_upkeep:
  type: num
  decimals: 0
  desc: Subversive activities cost

surrender_limit:
  type: num
  decimals: 2

war_stability_factor:
  type: num
  decimals: 2

war_support_factor:
  type: num
  decimals: 2

war_support_weekly:
  type: num
  decimals: 2

war_support_weekly_factor:
  type: num
  decimals: 2

weekly_manpower:
  type: num
  decimals: 0

```

## Ideology Drift vs Acceptance

> [!CRITICAL] `<ideology>_drift` changes daily support (affects your country's internal politics). `<ideology>_acceptance` affects diplomatic actions WITH that ideology (external relations). These are independent systems - one does not imply the other.

Examples:
```hoi4
democratic_drift = 0.10        # +10% daily democratic support gain (internal politics)
democratic_acceptance = 50     # +50 acceptance for diplomatic actions with democracies (external)
# These don't affect each other
```

## Related Systems

For government mechanics, see [Government](/systems/government.md).

For ideology systems, see [Ideologies](/systems/ideologies.md).

For diplomacy, see [Diplomacy](/diplomacy/diplomacy.md).
