---
domain: scripting
concept: script_concepts
version: 1.14+
requires: [scopes, triggers_core, effects]
relates: [scripted_triggers_effects, localisation, collections]
---

# Script Concepts

Foundational scripting patterns that support reusable, maintainable content.

## Bindable and Formatted Localization

- Bindable loc: Attach localization to scripted contexts; pass scopes/variables explicitly.
- Formatted loc: Use formatters (`<formatter>|<token>`) and contextual loc objects; keep tokens valid and scoped.

## Collections Structure and Shorthand

- Collections are iterable sets (countries, states, etc.) used in triggers/effects and loc.
- Use named collections for reuse; keep scope consistency; avoid implicit ordering assumptions.
- Shorthand and structure: Prefer a single `collections.md` reference for inputs/operators; document any mod-added collections.

## Script Constants Reload

- Constants can be reloaded; guard against mid-session changes if gameplay depends on fixed values.
- Keep constants in well-documented files to prevent accidental overrides.

## Contextual Localization

- Use loc objects (`[(Object.Property)]`) with correct scope.
- Provide fallbacks for missing objects; avoid spillover by validating scope before rendering.

