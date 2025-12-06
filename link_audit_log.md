## Link Audit Log

- Scope: tracks crosslink/frontmatter/link consistency changes per domain.
- Convention: root-relative paths for all internal links and master_index targets.
- Update after completing each domain pass.

### Core (completed)
- Standardized master_index core targets to `core/*`.
- Frontmatter fixes:
  - `core/mod_structure.md`: requires `[file_syntax]`; relates `[load_order]` (removed non-existent `encoding_rules`/`file_structure`).
  - `core/troubleshooting.md`: relates `[debug_tools, provinces, states, military]`; link to `entities/states.md`.
  - `core/scripting_data_types.md`: relates `[effects, console_commands]`.
  - `core/console_commands.md`: relates `[debug_tools, effects]`.
  - `core/nudger.md`: requires `[debug_tools, provinces]`; relates `[states, strategic_regions, supply, buildings]`; links to `entities/states.md`, `map/buildings.md`.
  - `core/metadata.md`: relates `[load_order, achievements]`; link to `core/load_order.md`.
  - `core/00_overview.md`: relationship descriptions aligned to existing concepts (removed `encoding_rules`, `map_structure`, `duplicates`, `scripting_effects`).

### master_index.json (completed)
- All primary/secondary targets now root-relative (`domain/file.md`), eliminating mixed formats across domains.

### Scripting (completed)
- Frontmatter cleanup to real concepts and dependencies:
  - `scripting/scopes.md`: foundation; requires `[]`; relates `[triggers_core, effects, on_actions_core]`.
  - `scripting/triggers_core.md`: relates `[effects, scripted_triggers_effects, on_actions_core]`.
  - `scripting/triggers_specialized.md`: relates `[effects, on_actions_core, scopes]` (removed nonexistent peace_conferences/resistance concepts).
  - `scripting/effects.md`: requires `[scopes, triggers_core]`; relates `[on_actions_core, scripted_triggers_effects, events, decisions]`.
  - `scripting/defines.md`: requires `[file_syntax]`; relates `[effects, triggers_core, modifiers]`.
  - `scripting/modifiers.md`: relates `[defines, modifiers_list, scopes, effects]`.
- No content link changes needed beyond frontmatter; all links remain root-relative.

### Database (completed)
- Frontmatter aligned to existing concepts:
  - `database/ideologies.md`: requires `[localisation]`; relates `[characters, ai_strategy, factions]`.
  - `database/ideas_core.md`: requires `[localisation]`; relates `[characters, modifiers_list, ideas_categories]`.
  - `database/ideas_categories.md`: relates `[interface, sprites, characters]`.
  - `database/balance_of_power.md`: relates `[modifiers, decisions]` (keeps requires `[modifiers_list, decisions]`).
  - `database/equipment.md`: relates `[units, resources, modifiers_list]`.
  - `database/resources.md`: requires `[buildings]`; relates `[sprites, trade, infrastructure]`.
  - `database/buildings.md`: relates `[supply, infrastructure, technologies_core]`.
  - `database/technologies_core.md`: relates `[technologies_gui, modifiers_list, equipment]`.
  - `database/technologies_gui.md`: relates `[interface, sprites]`.
  - `database/namelists.md`: requires `[units, navies]`; relates `[oob, localisation]`.
- `database/00_overview.md` relationship summaries updated to match the above.

### Assets (completed)
- Frontmatter cleaned to real concepts:
  - `assets/sprites.md`: requires `[]`; relates `[interface, localisation, fonts]`.
  - `assets/interface.md`: requires `[sprites]`; relates `[scripted_gui, localisation]`.
  - `assets/localisation.md`: requires `[scripted_loc]`; relates `[interface, sprites, scripted_gui]`.
  - `assets/scripted_gui.md`: requires `[interface, localisation]`; relates `[effects, triggers_core, scopes]`.
  - `assets/fonts.md`: requires `[localisation]`; relates `[sprites, interface]`.
  - `assets/sound.md`: relates `[interface]`.
  - `assets/portraits.md`: requires `[sprites, characters]`; relates `[ideologies, entities]`.
  - `assets/entities.md`: requires `[particles]`; relates `[units, buildings, particles]`.
  - `assets/particles.md`: requires `[]`; relates `[entities]`.
  - `assets/posteffects.md`: requires `[]`; relates `[map]`.
- `assets/00_overview.md` relationship descriptions aligned with the above.

### Map (completed)
- Frontmatter tweaks:
  - `map/terrain.md`: relates `[heightmap, entities]` (removed non-existent colormap).
  - `map/supply.md`: relates `[strategic_regions, rivers]` (railways not a domain file).
  - `map/00_overview.md`: relationship summaries updated to match current frontmatter.
  - Other map files reviewed; no path fixes needed.
- Lint cleanup: `map/00_overview.md` fully formatted (blank lines, code fence language tags); all map files lint-clean.
