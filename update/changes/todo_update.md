# Update TODO by Scope

## Extreme scope
- None identified.

## Major scope

### ai_bonus_weights_documentation.md
- **Add new AI bonus weights page (defaults/archetype weights, error behavior, examples).**
  - Affected files: new `content/ai_bonus_weights.md` (or equivalent), `master_index.json`.

### ai_faction_theaters_documentation.md
- **Add AI faction theaters page (regions list, can_skip_first_region, preferred_countries, ai_will_do/cancel, connectivity).**
  - Affected files: new `content/ai_faction_theaters.md`, `master_index.json`.

### ai_navy_documentation.md
- **Add naval AI goals/objectives page (scoring, objective types, priority ranges, imgui show ai_navy).**
  - Affected files: new `content/ai_navy.md`, `master_index.json`.

### collections_documentation.md
- **Add scripting collections page (definition, anonymous/built-ins, collection_size, every_collection_element).**
  - Affected files: new `scripting/collections.md`, `master_index.json`.

### cost_modifiers_documentation.md
- **Add peace cost modifiers page (scope mapping, action types, categories, cost multipliers).**
  - Affected files: new `content/peace_cost_modifiers.md` (or `scripting/peace_cost_modifiers.md`), `master_index.json`.

### decisions_documentation.md
- **Add decisions page (allowed/visible/available, target_root/target/state_trigger perf notes, lifecycle).**
  - Affected files: new `content/decisions.md`, `master_index.json`.

### doctrines_documentation.md
- **Add doctrine system page (folders, grand doctrines, tracks, subdoctrines, mastery, rewards, triggers/effects/modifiers).**
  - Affected files: new `military/doctrines.md`, `master_index.json`.

### dynamic_variables_documentation.md
- **Add dynamic variables reference (global/country/state/unit_leader/MIO/special_project; AI strategy, power balance, intel).**
  - Affected files: new `scripting/dynamic_variables.md`, `master_index.json`.

### equipment_groups_documentation.md
- **Add equipment groups page (grouping types/archetypes/categories, include, description, equipment_bonus usage).**
  - Affected files: new `military/equipment_groups.md` (or `scripting/equipment_groups.md`), `master_index.json`.

### folders_documentation.md
- **Add doctrine folders page (top-level categorization, UI fields, allowed, ledger options).**
  - Affected files: new `military/doctrine_folders.md`, `master_index.json`.

### grand_doctrines_documentation.md
- **Add grand doctrines page (folder link, xp_cost/xp_type, tracks, milestones, activation effects, max_track_rows/columns).**
  - Affected files: new `military/grand_doctrines.md`, `master_index.json`.

### loc_objects_documentation.md
- **Add localization objects reference (Ace/Building/Character/Country/Faction/IndustrialOrg/Operation/Province/PurchaseContract/Scope/SpecialProject/State/Terrain/UnitLeader, properties/promotions).**
- Affected files: new `localisation/loc_objects.md`, `master_index.json`.

### operation_phases_documentation.md
- **Add operation phases page (required/optional fields, requirements, return_on_complete, equipment incl. civilian_factories, outcome vs outcome_extra, map_icon, reseeding).**
  - Affected files: new `espionage/operation_phases.md`, `master_index.json`.

### operation_tokens_documentation.md
- **Add operation tokens page (unique per country pair, targeted_modifiers, intel_source/gain rules, non-stackable).**
  - Affected files: new `espionage/operation_tokens.md`, `master_index.json`.

### operations_documentation.md
- **Add operations page (ROOT/FROM scoping, visuals, duration/danger, operatives/network_strength, phases weights, ai_will_do, allowed/available/selection_target/target_type, tokens, equipment costs, requirements, on_start, rewards, return_on_complete, seed/reseed).**
  - Affected files: new `espionage/operations.md`, `master_index.json`.

### raids_documentation.md
- **Add raids system page (categories, targeting UI, icons, command power, arrows, unit models/equipment, intel source, success levels/factors, cooldowns, allowed/visible/available/launchable/launchable_from, starting_point).**
  - Affected files: new `espionage/raids.md`, `master_index.json`.

### scientist_traits_documentation.md
- **Add scientist traits page (schema, modifiers for special projects, specialization gating, available trigger).**
  - Affected files: new `entities/scientist_traits.md` (or under characters), `master_index.json`.

### script_collection_input.md
- **Add collections input reference (game:all_countries/all_possible_countries/all_states, game:scope, named collections, constants).**
  - Affected files: new `scripting/collections_input.md`, `master_index.json`.

### script_collection_operator.md
- **Add collections operator reference (faction_members, owned_states, controlled_states, country_and_all_subjects, limit trigger, localization behavior).**
  - Affected files: new `scripting/collections_operator.md`, `master_index.json`.

### script_concept_documentation.md
- **Add script concepts page (bindable localization, formatted localization, collections structure/uniqueness/shorthand, script constants reload, contextual localization).**
  - Affected files: new `scripting/script_concepts.md`, `master_index.json`.

### scripted_guis_documentation.md
- **Add scripted GUIs page (context_type options, parent window tokens, visibility/triggers, effects binding, properties, dynamic_lists, dirty flag, AI fields/testing scopes/weights).**
  - Affected files: new `interface/scripted_guis.md`, `master_index.json`.

### subdoctrines_documentation.md
- **Add subdoctrines page (root per track, xp_cost/xp_type, available/visible, reward chains/mastery overrides, reward_gfx, activation effects).**
  - Affected files: new `military/subdoctrines.md`, `master_index.json`.

### taskforce_documentation.md
- **Add taskforce composition page (allowed trigger, ai_will_do, mission list, min vs optimal composition semantics).**
  - Affected files: new `military/taskforces.md`, `master_index.json`.

### tracks_documentation.md
- **Add doctrine tracks page (name/background/frame/icon, active trigger, mastery multipliers/contributors, linkage to grand doctrines and subdoctrines).**
  - Affected files: new `military/doctrine_tracks.md`, `master_index.json`.

## Average scope

### ai_equipment_documentation.md
- **Update AI equipment section to new spec (priority blocks, target_variant/modules, requirements, allowed_modules, enable/blocked/available, new tokens).**
  - Affected files: `content/ai_strategy.md`.

### ai_peace_documentation.md
- **Refresh AI peace to new peace_ai_desires structure, scopes, action types, summing/zero-disable, triggers.**
  - Affected files: `content/ai_strategy.md`.

### ai_strategy_documentation.md
- **Expand to 2024-11 tokens (equipment market, raid targets, naval dominance/convoy raiding, research weighting, production minimums, new unit_ratio behavior).**
  - Affected files: `content/ai_strategy.md`.

### ai_templates_documentation.md
- **Align AI templates with new examples (role-level entries, upgrade_prio/enable/replace_with, target_template, match scores, field upgrades, imgui debug).**
  - Affected files: `content/ai_strategy.md`.

### characters_documentation.md
- **Add scientist role section (desc, traits, skills, visible trigger, defaults).**
  - Affected files: `entities/characters.md`.

### console_commands_documentation.md
- **Expand command list (MIO/market/special projects/debug/tweakables, aliases, args, release-build notes).**
  - Affected files: `core/console_commands.md`.

### effects_documentation.md
- **Expand effects reference to full current set (categories, params, nuances, new effects).**
  - Affected files: `scripting/effects.md`.

### equipment_documentation.md
- **Expand equipment coverage (ai_type, module slots/count limits, default_modules, resources/stats, production limits).**
  - Affected files: `military/equipment.md`.

### factions_documentation.md
- **Add detailed goal/rule/template/range/progress/AI spending content.**
  - Affected files: `entities/factions.md`.

### intelligence_agency_upgrades_documentation.md
- **Verify/expand upgrades schema (picture/frame/sound, ai_will_do, modifiers_during_progress, multi-level modifiers/effects).**
  - Affected files: `military/intel_agencies.md`.

### loc_formatter_documentation.md
- **Add full parameters/examples for advisor_desc, building_state_modifier, character_name, country_culture, country_leader_desc, idea_desc/name, tech_effect.**
  - Affected files: `assets/localisation.md`.

### modifiers_documentation.md
- **Integrate/expand modifiers structure with categories, schema examples, percent/flat/multiplicative, dynamic/static/targeted/opinion, variable-based modifiers; keep modifiers_list links.**
  - Affected files: `scripting/modifiers.md`, `modifiers_list/*.md`.

### on_actions_documentation.md
- **Refresh to full 2024-11 enumeration and scope notes (new entries, deprecated notes).**
  - Affected files: `scripting/on_actions_core.md`, `scripting/on_actions_reference.md`.

### organizations_documentation.md
- **Fill MIO schema gaps (name/icon/background resolution, allowed/visible/available timing, equipment_type/research_categories, on_* hooks, ai_will_do, tree_flavor_text, initial_trait, parents/exclusivity, positioning/relative_position_id, equipment/production/organization bonuses, task_capacity, funds, size-up).**
  - Affected files: `military/mios.md`.

### policies_documentation.md
- **Ensure MIO policies match new doc (cost/cooldown, allowed/visible/available, equipment_bonus/production_bonus keyed by groups/categories/archetypes with same_as_mio, organization_modifier, on_add/on_remove, ai_will_do).**
  - Affected files: `military/mios.md`.

### triggers_documentation.md
- **Expand to full 2024-11 set (new scopes: industrial_org, raid_instance, special_project, purchase_contract, operation; new triggers) and update scope tables.**
  - Affected files: `scripting/triggers_core.md`, `scripting/triggers_specialized.md`.

## Minor scope

### resources_documentation.md
- **Add note on `NAI::MIN_FACTORIES_TO_WANT_TO_IMPORT` and import-desire gating.**
  - Affected files: `database/resources.md`.

