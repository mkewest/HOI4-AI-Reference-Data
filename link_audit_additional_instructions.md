## Link Audit Additional Instructions (handoff notes)

This file captures working practices and recent state, beyond what’s already in README and the existing plan, so the next agent can continue consistently.

### Overall conventions used
- All route targets and inline links should be root-relative paths (`domain/file.md`), consistent with the master_index work already done.
- YAML frontmatter alignment:
  - `requires` / `relates` / `conflicts` must reference real concepts or files; remove non-existent placeholders.
  - Keep `requires` empty (`[]`) when nothing is required, rather than using invented tokens.
- Linting: resolve markdownlint basics (blank lines around headings/lists, code fence language tags). Expect to fix MD022/MD032/MD040/MD012 when they appear.
- Do not revert user changes; only adjust for consistency and lint fixes related to this audit.

### Domains completed so far
- **Core**: Frontmatter cleaned; links updated to root-relative; `map_structure/encoding_rules/etc` placeholders removed; crosslinks updated to `entities/states.md` where applicable; metadata duplicate link removed.
- **Scripting**: Frontmatter aligned (`effects`, `triggers_core`, etc.); `defines.md` lints fixed; all links root-relative.
- **Database**: Frontmatter aligned to real concepts; overview updated; links remain root-relative; lints clean.
- **Assets**: Frontmatter aligned; overview updated; lints clean.
- **Map**: Frontmatter aligned (`terrain` relates heightmap/entities; `supply` relates strategic_regions/rivers); `map/00_overview.md` fully reformatted and lint-clean; other map files reviewed—no path/link changes needed.
- `link_audit_log.md` tracks per-domain changes (Core, Scripting, Database, Assets, Map marked completed).

### Outstanding / Next domains
- Remaining domains: Military, Content, Entities (if any lingering), Modifiers_list, Defines_list, plus any others not yet audited (check master_index.json domain list).
- Continue the same pattern: audit frontmatter, links, master_index consistency (if applicable), lint fixes.

### Known patterns to maintain
- When adding/removing relationships, keep them semantically real (e.g., use `interface`, `localisation`, `effects`, `triggers_core`, `states`, `provinces`, `strategic_regions`, etc.; avoid non-existent `map_structure`, `colormap`, `encoding_rules`, `file_structure`, `gui_system`, `peace_conferences` unless real files exist).
- Supply/railways: `railways` is not a domain file; use `rivers`/`strategic_regions` as relates, unless a file exists.
- Cross-domain references should use the correct domain prefix (e.g., `entities/states.md`, `map/provinces.md`, `core/debug_tools.md`).

### Master index status
- Already standardized to root-relative paths across all domains (core, scripting, database, assets, modifiers_list, defines_list, map, etc.). Maintain this convention for any future changes.

### Lint expectations
- If lint issues arise, fix them inline (add blank lines around headings/lists; add language tags to fenced code blocks like ```text or ```hoi4; remove multiple consecutive blank lines).

### Misc
- Do not undo accepted changes; build on the current state.
- If ambiguity about a relationship target arises, prefer leaving as-is or note for follow-up rather than guessing new, non-existent concepts.

