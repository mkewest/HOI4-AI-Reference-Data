## In-Game Documentation Audit Plan

This document defines a **deferred audit** for validating that all relevant information from Paradox’s in-game documentation files is represented in the HOI4-AI-Reference-Data knowledge base.

The audit will run **after** the master index JSON and all domains are structurally complete, so we have a stable target set of `.md` files.

---

## 1. Scope

The audit compares:

- **Source side** (authoritative but often terse):
  - Documentation bundled with HOI4 itself, e.g.:
    - Any `documentation`, `readme`, or `help` files shipped with the game.
    - Commented sections in `common/`, `map/`, `events/`, etc. that contain actual explanatory text (not just labels).
    - Any “developer docs” subfolders present in the game install.
- **Target side**:
  - This repo’s `.md` files in all domains (`assets/`, `content/`, `core/`, `database/`, `defines_list/`, `entities/`, `map/`, `military/`, `modifiers_list/`, `scripting/`).

The goal is not to mirror vanilla docs verbatim, but to ensure **no important concepts** described only in the game’s own documentation are missing from this database.

---

## 2. Goals

For each relevant in-game documentation section:

1. **Coverage check**
   - Confirm that the concept is already explained in at least one `.md` file here.
   - If missing, **add or extend** the appropriate domain file to include that concept (following the existing architecture rules).
2. **Clarity and correctness**
   - Prefer the repo’s prose style (semantic, context-rich, edge-case integrated) over vanilla doc phrasing.
   - If in-game docs clarify an ambiguity or add a critical constraint, integrate that nuance **inline at the point of relevance**.
3. **Version awareness**
   - If in-game docs are version-specific, ensure our files:
     - Either already match that version, or
     - Are updated to reflect the correct version range in frontmatter or inline notes.

---

## 3. Procedure (Per In-Game Doc Section)

For each section in the vanilla documentation set:

1. **Identify the concept and domain**
   - Map the concept to one or more existing concepts/domains in this repo (e.g., “supply nodes” → `/map/supply.md`).
2. **Search the repo for coverage**
   - Use semantic/text search to locate the relevant `.md` file(s).
   - Confirm that:
     - The concept is present.
     - The explanation is at least as complete and correct as the in-game doc.
3. **Integrate missing or improved information**
   - If a concept is missing or under-documented:
     - Add a new subsection or expand an existing one in the correct file.
     - Integrate any critical constraints or edge cases found only in the in-game docs.
   - Keep formatting consistent with `architecture_rules.md` and `output_templates.md`.
4. **Avoid redundant duplication**
   - Do not copy raw in-game text wholesale when the repo already covers the concept well.
   - Prefer brief notes like “Vanilla docs also mention X; this behavior is already captured here under Y”.

---

## 4. Execution Order

After all domains and `master_index.json` are complete:

1. **Core + Scripting documentation**
   - Check that any scripting/defines/console docs in the game are represented or improved in `/core/` and `/scripting/`.
2. **Map + Military + Database**
   - Cross-check any map or unit-related vanilla docs against `/map/`, `/military/`, and `/database/`.
3. **Content + Assets + Entities**
   - Verify that any event/focus/GUI/asset notes in vanilla docs have equivalents here.
4. **Defines/Modifiers Lists**
   - Ensure any define/modifier descriptions in in-game docs are covered (or superseded) by `defines_list/` and `modifiers_list/`.

Progress and any major additions should be logged in `index_progress_log.md`.
