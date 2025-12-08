---
domain: military
concept: operations
version: 1.14+
requires: [intel_agencies]
relates: [raids, modifiers_list, scripting]
---

# Operations System

Operations are multi-phase espionage actions with tokens, phases, equipment, and rewards. This page consolidates operations, operation tokens, and operation phases.

## Operations

- **Scope**: ROOT = initiator country; FROM = target country; additional temp scopes per phase/token as defined.
- **Core fields**: visuals, duration/danger, operatives/network_strength requirements, `ai_will_do`, allowed/available/selection_target/target_type.
- **Tokens & equipment costs**: Define required tokens/equipment (civilian_factories included); keep costs consistent with phases.
- **Requirements & rewards**: `on_start`, `rewards`, `return_on_complete`, `seed/reseed` behaviors; align with phases and tokens.
- **Selection & targeting**: Use `target_type` and selection triggers; ensure network strength/operative scopes match doc expectations.

## Operation Tokens

- **Uniqueness**: Tokens are unique per country pair; non-stackable by design.
- **Fields**: `targeted_modifiers`, intel_source/gain rules; align modifiers with `modifiers_list`.
- **Usage**: Tokens gate operations/phases; ensure creation and cleanup are explicit to avoid lingering modifiers.

## Operation Phases

- **Fields**: required/optional fields, requirements, `return_on_complete`, equipment (incl. civilian_factories), `outcome` vs `outcome_extra`, `map_icon`, reseeding.
- **Weights**: Phase weights impact selection; keep balanced to avoid stalls.
- **Reseeding**: Define reseed behavior to restart phases cleanly when needed.

## AI and Balancing

- **AI**: `ai_will_do` on operations and phases; keep ranges stable and state-aware.
- **Danger/duration**: Tune to avoid trivial or impossible operations; match equipment/network requirements.

## Linking

- Cross-link with raids, intel agency upgrades, and scripting references for triggers/effects used in operations.

