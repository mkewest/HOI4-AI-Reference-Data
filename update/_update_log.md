# Update log

Log of updates.
---
## 2025-12-07

### Edited database/database/resources.md
**Update based on:** "resources_documentation.md"

Added AI import desire note: `NAI::MIN_FACTORIES_TO_WANT_TO_IMPORT` guidance for imports when adding/reordering resources, and linked to `defines_list/NAI.md`.

### Edited database/scripting/effects.md
**Update based on:** "effects_documentation.md"

Expanded effects guidance: supply/logistics examples, notes on espionage/operations scopes, MIO effects, and localisation/UI effects, keeping scope cautions.

---
## 2025-12-08

### Edited database/content/ai_strategy.md
**Update based on:** "ai_bonus_weights_documentation.md", "ai_faction_theaters_documentation.md", "ai_navy_documentation.md", "ai_equipment_documentation.md", "ai_peace_documentation.md", "ai_strategy_documentation.md", "ai_templates_documentation.md"

Added AI bonus weights, faction theaters, naval AI objectives, updated equipment design guidance (priority blocks, modules/requirements, enables), refreshed peace_ai_desires structure with zero-disable behavior, expanded 2024-11 tokens, and enhanced AI templates notes/debug pointers.

### Edited database/entities/characters.md
**Update based on:** "characters_documentation.md"

Added scientist role schema (desc, traits, skills, visibility trigger) for Special Projects.

### Edited database/core/console_commands.md
**Update based on:** "console_commands_documentation.md"

Noted MIO/Market/Special Projects/debug command groups, aliases, and release-build availability.

### Edited database/scripting/effects.md
**Update based on:** "effects_documentation.md"

Added 1.14+/2024-11 coverage note across operations/espionage, supply/logistics, MIO/industry, localisation/UI, and specialized scopes.

### Edited database/military/equipment.md
**Update based on:** "equipment_documentation.md"

Added AI/module design notes (ai_type alignment, slot limits, default modules, resource/stats consistency, production limits, equipment group linkage).

### Edited database/entities/factions.md
**Update based on:** "factions_documentation.md"

Added goals/rules/templates summary with AI spending and scope notes.

### Edited database/military/intel_agencies.md
**Update based on:** "intelligence_agency_upgrades_documentation.md"

Documented upgrade schema notes (media fields, modifiers_during_progress, multi-level handling, ai_will_do weighting).

### Edited database/assets/localisation.md
**Update based on:** "loc_formatter_documentation.md"

Detailed formatter parameters for advisor/idea/building/character/country/tech formatters and linked to loc objects.

### Edited database/scripting/modifiers.md
**Update based on:** "modifiers_documentation.md"

Added structure/category guidance (static/dynamic/targeted/opinion, percent/flat/multiplicative, variable-based) and integration notes with modifiers_list.

### Edited database/scripting/on_actions_core.md and database/scripting/on_actions_reference.md
**Update based on:** "on_actions_documentation.md"

Added 1.14+/2024-11 coverage notes and reminders to document scopes/temp vars for new hooks.

### Edited database/military/mios.md
**Update based on:** "organizations_documentation.md", "policies_documentation.md"

Documented organization schema notes (identity, allowed/visible/available, equipment scope, hooks, ai_will_do, layout) and policy schema notes (costs/cooldowns, gating, bonuses, callbacks, ai_will_do).

### Edited database/scripting/triggers_core.md and database/scripting/triggers_specialized.md
**Update based on:** "triggers_documentation.md"

Added 1.14+/2024-11 scope additions (industrial_org, raid_instance, special_project, purchase_contract, operation) and scope-matching reminders for specialized triggers.

### Created database/military/doctrines.md
**Update based on:** "doctrines_documentation.md", "tracks_documentation.md", "subdoctrines_documentation.md", "folders_documentation.md", "grand_doctrines_documentation.md"

Added consolidated doctrine page covering folders, grand doctrines, tracks, and subdoctrines with mastery/rewards and triggers/effects/modifiers guidance.

### Created database/scripting/collections.md
**Update based on:** "script_collection_input.md", "script_collection_operator.md"

Added a single collections reference (inputs/operators, iteration patterns, scope safety, performance tips, localization behavior).

### Created database/scripting/script_concepts.md
**Update based on:** "script_concept_documentation.md"

Added scripting concepts page (bindable/formatted localization, collections structure/shorthand, script constants reload, contextual localization patterns).

### Updated database/scripting/00_overview.md
**Update based on:** new scripting files

Added collections/script_concepts to structure, descriptions, and file count.

### Updated database/master_index.json
**Update based on:** new scripting files

Added routes for collections and script concepts pointing to the new pages with relevant signals.

### Edited database/content/decisions.md
**Update based on:** "decisions_documentation.md"

Added polling cadence and performance guidance for targeted decisions (`allowed`, `visible`, `available` frame checks; `target_root_trigger`/`target_trigger` daily checks; state_target/targets filtering best practices).

### Edited database/entities/characters.md
**Update based on:** "scientist_traits_documentation.md"

Added scientist traits section: sample schema, Special Projects scope, specialization gating, availability gating, and icon/name defaults.

### Edited database/military/navies.md
**Update based on:** "taskforce_documentation.md"

Added AI task force template guidance (allowed, ai_will_do, mission list, min/optimal composition with example) into navies.md instead of a new file.

### Edited database/core/scripting_data_types.md
**Update based on:** "dynamic_variables_documentation.md"

Expanded the Variables section with dynamic variable notes: clarified read-only scope-specific dynamic variables, key global/country/state/unit_leader/MIO/special_project examples, and pointed to the in-game documentation for full lists.

### Edited database/assets/interface.md
**Update based on:** "scripted_guis_documentation.md"

Added scripted GUI integration details (contexts, parent bindings, visibility/map_mode, effects/triggers/properties, dynamic_lists, dirty updates, AI fields) into interface.md instead of a new file.

### Created database/military/equipment_groups.md
**Update based on:** "equipment_groups_documentation.md"

Added equipment groups page covering group definition (types/archetypes/categories, nested groups), usage in MIO policies/traits and modifiers, and maintenance guidelines.

### Edited database/scripting/modifiers.md
**Update based on:** "0_dynamic_modifiers.txt"

Added a dynamic modifiers section: definition fields (`icon`, `enable`, `remove_trigger`, `attacker_modifier`), application via `add_dynamic_modifier` (scope/days), supported scopes (country/state/unit_leader/special_project), daily evaluation/`force_update_dynamic_modifier`, removal paths, and usage guidelines.

### Edited database/content/peace_cost_modifiers.md
**Update based on:** "cost_modifiers_documentation.md", "00_generic_peace.txt"

Added peace cost modifier schema plus vanilla pattern examples (core/claims, occupation, ideology, defensive war, ally core, continuous political action, special cases) with typical multiplier ranges.

