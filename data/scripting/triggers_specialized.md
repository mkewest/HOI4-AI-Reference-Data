---
domain: scripting
concept: triggers_specialized
version: 1.14+
requires: [triggers_core, scopes]
relates: [peace_conferences, resistance, military, intelligence]
---

# Specialized Triggers

Domain-specific triggers for particular game systems. For core trigger logic and operators, see [Core Triggers](/scripting/triggers_core.md).

## Global Scope Triggers

Valid in any scope context:

```hoi4
always = yes/no          # Constant true/false
has_global_flag = name   # Global flag check
has_dlc = "Name"         # DLC ownership
has_start_date = date    # Campaign start date check
date > 1940.1.1          # Current game date
difficulty > 0           # Difficulty level (0-4)
threat > 0.5             # World tension (0.0-1.0)
has_game_rule = { rule = name option = value }
is_ironman = yes         # Ironman mode active
is_debug = yes           # Debug mode active
```

These triggers work regardless of the current scope type.

## Country Scope Triggers

### Existence and Identity

```hoi4
exists = yes             # Country exists in game
tag = GER                # Exact tag match (no dynamics)
original_tag = GER       # Tag match (includes dynamics)
is_ai = yes              # AI-controlled
has_country_flag = name  # Country-specific flag
```

### Military State

```hoi4
has_war = yes                        # At war with anyone
has_war_with = TAG                   # At war with specific country
has_war_with_wargoal_against = TAG   # Has wargoal against (not ally's war)
has_capitulated = yes                # Currently capitulated
days_since_capitulated > N           # Days since last capitulation
has_defensive_war = yes              # All wars are defensive
has_offensive_war = yes              # At least one offensive war
surrender_progress > 0.5             # Progress to capitulation (0.0-1.0)
has_army_manpower = { size > N }     # Deployed manpower count
has_deployed_air_force_size = { size > N }
has_navy_size = { size > N }
```

### Faction and Diplomacy

```hoi4
is_in_faction = yes                  # Member of any faction
is_faction_leader = yes              # Leader of faction
is_in_faction_with = TAG             # In same faction
is_subject = yes                     # Any subject type
is_puppet = yes                      # Puppet specifically
is_subject_of = TAG                  # Subject of specific overlord
num_subjects > N                     # Number of subjects
has_guaranteed = TAG                 # Guaranteeing independence
has_military_access_to = TAG         # Has military access
gives_military_access_to = TAG       # Giving military access
is_neighbor_of = TAG                 # Land or naval neighbors
```

### Government and Politics

```hoi4
has_government = ideology            # Current government type
has_election = yes                   # Election scheduled
has_country_leader = { name = "..." }
has_country_leader_with_trait = trait
has_stability > 0.5                  # Stability level (0.0-1.0)
has_war_support > 0.5                # War support level (0.0-1.0)
has_political_power > 100            # Political power amount
political_power_growth > 1.0         # Daily PP gain
has_idea = idea_token                # Active idea/spirit
has_idea_with_trait = trait          # Active idea with trait
has_allowed_idea_with_traits = { idea = token characters = yes }
```

### Economy and Resources

```hoi4
has_manpower > 10000                 # Manpower in reserve (in thousands)
has_equipment = { type > N }         # Stockpiled equipment
has_any_license = yes                # Holds any production license
amount_manpower_in_deployment_queue > 1000
num_of_factories > 50                # Total factories
num_of_civilian_factories > 20       # Civilian factories
num_of_military_factories > 20       # Military factories
num_of_naval_factories > 10          # Naval dockyards
has_fuel > 10000                     # Fuel reserves
fuel_ratio > 0.5                     # Fuel reserves vs capacity
```

### Technology and Research

```hoi4
has_tech = tech_id                   # Technology researched
is_researching_technology = tech_id  # Currently researching
has_trait = trait_token              # Country modifier trait
num_tech_sharing_groups > 0          # Member of tech sharing groups
```

### Territory Control

```hoi4
controls_state = id                  # Controls specific state
owns_state = id                      # Owns specific state
has_full_control_of_state = id       # Owns and controls
controls_province = id               # Controls specific province
any_owned_state = { ... }            # Trigger scope for owned states
any_controlled_state = { ... }       # Trigger scope for controlled
num_of_owned_states > N              # Count of owned states
num_of_controlled_states > N         # Count of controlled states
core_compliance > 50                 # Average compliance in cores
core_resistance > 30                 # Average resistance in cores
```

## State Scope Triggers

### Ownership and Control

```hoi4
is_controlled_by = TAG               # Controlled by specific country
is_owned_by = TAG                    # Owned by specific country
is_owned_and_controlled_by = TAG     # Both owned and controlled
controller = { ... }                 # Trigger scope for controller
owner = { ... }                      # Trigger scope for owner
```

### Territory Properties

```hoi4
is_core_of = TAG                     # Is core of specific country
is_claimed_by = TAG                  # Is claimed by (not necessarily core)
has_state_flag = name                # State-specific flag
is_coastal = yes                     # Has coastal provinces
is_island_state = yes                # All provinces on island(s)
is_capital = yes                     # Is capital state
state_population > 1000000           # Population (in ones, not thousands)
state_and_terrain_strategic_value > 50
impassable = yes                     # All provinces impassable
```

### Buildings and Infrastructure

```hoi4
building_level = { building = type level > N }
free_building_slots = { building = type size > N }
has_damaged_buildings = yes          # Any damaged buildings
infrastructure > 5                   # Infrastructure level (0-10)
arms_factory > 10                    # Military factory count
industrial_complex > 10              # Civilian factory count
air_base > 5                         # Air base level
anti_air_building > 3                # Anti-air building level
radar_station > 1                    # Radar station level
rocket_site > 1                      # Rocket site level
nuclear_reactor > 0                  # Nuclear reactor level
```

### Resources and Industry

```hoi4
has_resources_amount = { resource = type amount > N }
resource_count = { resource = type count > N }
free_resource = { resource = type amount > N }
has_mined_resources_rights_of = TAG  # Resource rights held by
```

### Occupation and Resistance

```hoi4
compliance > 50                      # Compliance level (0-100)
resistance > 30                      # Resistance level (0-100)
resistance_speed > 0.5               # Resistance growth rate
compliance_speed > 0.5               # Compliance growth rate
has_resistance = yes                 # Resistance active
has_occupation_modifier = modifier   # Occupation modifier active
has_active_resistance = yes          # Active resistance operations
garrison_manpower_need > 1000        # Required garrison strength
```

### State Modifiers

```hoi4
has_dynamic_modifier = { modifier = name }
has_modifier = modifier_token
state_strategic_value > 50           # Strategic AI value
```

## Character Scope Triggers

```hoi4
has_character_flag = name            # Character-specific flag
has_trait = trait_token              # Character trait
has_ideology = ideology_type         # Specific ideology (not group)
is_hired_as_advisor = yes            # Hired in any advisor slot
has_advisor_role = role              # Has specific advisor role
is_corps_commander = yes             # Is corps commander
is_field_marshal = yes               # Is field marshal
skill > 3                            # Overall skill level
attack_skill_level > 2               # Attack skill
defense_skill_level > 3              # Defense skill
logistics_skill_level > 2            # Logistics skill
planning_skill_level > 3             # Planning skill
is_exiled_leader_from = TAG          # Exiled leader from country
has_nationality = TAG                # Character nationality
can_be_fired = yes                   # Can be removed/fired
```

### Version-Dependent Behavior

Pre-1.12:
```hoi4
is_air_chief = yes      # True if ever had role
is_army_chief = yes
is_navy_chief = yes
```

Post-1.12:
```hoi4
is_air_chief = yes      # True if currently in role
is_army_chief = yes
is_navy_chief = yes
```

## Combat Scope Triggers

Used in combat evaluation contexts:

```hoi4
is_attacker = yes                    # Current side is attacker
is_defender = yes                    # Current side is defender
is_winning = yes                     # Current side winning
hardness > 0.5                       # Unit hardness value
armor > 50                           # Armor value
dig_in > 2                           # Entrenchment level
temperature > 0                      # Temperature at location
night = yes                          # Night time
```

## Division Scope Triggers

```hoi4
division_has_majority_template = template_name
division_has_battalion_in_template = battalion_type
unit_strength > 0.8                  # Division strength (0.0-1.0)
unit_organization > 0.5              # Division organization (0.0-1.0)
has_unit_leader = yes                # Division has assigned leader
```

## MIO Scope Triggers

Military Industrial Organization triggers (1.13+):

```hoi4
is_military_industrial_organization = yes
is_mio_visible = yes                 # Visible in UI
is_mio_available = yes               # Can be assigned
has_mio_policy_active = policy       # Policy currently active
has_mio_policy_available = policy    # Policy can be activated
has_mio_size > 3                     # Size/tier level
has_mio_trait = trait                # Has specific trait
is_mio_trait_available = trait       # Trait can be unlocked
is_mio_trait_completed = trait       # Trait fully upgraded
has_mio_flag = name                  # MIO-specific flag
mio_number_of_completed_traits > 5   # Count completed traits
mio_policy_cost_offset > -50         # Policy cost modifier
```

## Contract Scope Triggers

Purchase contract triggers:

```hoi4
contract_contains_equipment = type   # Contract includes equipment type
deal_completion > 0.5                # Contract progress (0.0-1.0)
seller = { ... }                     # Trigger scope for seller country
buyer = { ... }                      # Trigger scope for buyer country
```

## Peace Conference Triggers

Active only during peace conferences:

```hoi4
pc_is_winner = yes                           # On winning side
pc_is_loser = yes                            # On losing side
pc_is_liberated = yes                        # Being liberated
pc_is_puppeted = yes                         # Being puppeted
pc_is_winner_but_no_control = yes            # Won but no control
pc_is_untouched_winner = yes                 # Won without territory loss
pc_current_score > 100                       # Current available score
pc_total_score > 500                         # Total score gained (winners only)
pc_turn_number > 5                           # Conference turn count
pc_is_on_same_side_as = TAG                  # On same side
pc_is_on_winning_side = TAG                  # Country on winning side
```

### State Claims

```hoi4
pc_is_state_claimed = yes                    # Someone claimed state
pc_is_state_claimed_by = TAG                 # Specific country claimed
pc_is_state_claimed_and_taken_by = TAG       # "Take State" action
```

> [!CRITICAL] `pc_is_state_claimed_by` includes force government, puppet, and liberate actions. `pc_is_state_claimed_and_taken_by` checks ONLY the "Take State" action specifically. These are not interchangeable.

### Conference Actions

```hoi4
pc_does_state_stack_demilitarize = yes       # State being demilitarized
pc_does_state_stack_dismantled = yes         # State being dismantled
pc_is_forced_government = yes                # Government being forced
pc_is_forced_government_by = TAG             # By specific country
```

## Intelligence and Operatives

```hoi4
has_intelligence_agency = yes                # Agency unlocked
decryption_progress = { target = TAG progress > 0.5 }
intel_level_over = { target = TAG category = type value > 1 }
has_captured_operative = TAG                 # Holding operative from
network_strength = { target = TAG value > 50 }
num_fake_intel_divisions > 10                # Fake army size
```

### Operative Scope

```hoi4
is_operative_captured = yes                  # Currently captured
operative_leader_mission = mission_type      # On specific mission type
operative_leader_operation = operation_type  # In specific operation
```

## Special Project Triggers

Special project triggers (1.15+):

```hoi4
has_special_project = project_id
special_project_completed = project_id
special_project_progress = { project = id progress > 0.5 }
```

## Related Systems

For scripted trigger definitions and meta triggers, see [Core Triggers](/scripting/triggers_core.md).

For trigger usage in on_actions, see [On Actions Core](/scripting/on_actions_core.md).

## Documentation

Complete trigger documentation: `documentation/triggers_documentation.html`
