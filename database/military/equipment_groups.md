---
domain: military
concept: equipment_groups
version: 1.14+
requires: [equipment]
relates: [mios, modifiers_list]
---

# Equipment Groups

Equipment groups are content groupings (types/archetypes/categories) used to scope bonuses, policies, and modifiers—commonly in MIO policies/traits and related systems.

## Defining Groups

Groups live in equipment definitions or group files and can reference:
- **Types**: Broad categories (e.g., `ship`, `tank`, `plane`).
- **Archetypes**: Specific base items (e.g., `ship_hull_heavy`, `ship_hull_cruiser`, `ship_hull_submarine`).
- **Categories/Subcategories**: Finer filters used by policies/bonuses.
- **Nested groups**: Groups can include other groups; keep inclusion DAG acyclic.

Keep names consistent and documented; avoid overlapping tokens that blur intent.

## Using Groups in Bonuses/Policies

- **MIO policies/traits**: `equipment_bonus = { group_token = { ... } }` or `production_bonus` keyed by group/category/archetype; `same_as_mio` can mirror org scope.
- **Modifiers/effects**: When modifiers accept equipment filters, align group tokens with definitions to avoid no-ops.
- **AI filters**: If used for AI production/role scoping, ensure group coverage matches AI expectations to prevent empty matches.

Guidelines:
- Prefer group tokens over long include lists for maintainability.
- Document intended coverage per group; keep naval/air/land separated unless intentionally mixed.
- Validate group references in logs to catch typos or missing definitions.

## Maintenance Tips

- When adding new equipment, update relevant groups (and any nested group membership).
- Avoid circular group inclusion.
- Keep group scope narrow enough to be meaningful but broad enough to reduce duplication.

