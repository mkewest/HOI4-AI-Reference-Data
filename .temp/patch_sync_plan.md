## Patch Sync Plan (Post-1.13 Behavior)

This document defines a **deferred synchronization pass** to align the knowledge base with game behavior in patches released after a chosen baseline version (roughly HOI4 **1.13+**). The sync will run after the master index and all domains are stable.

---

## 1. Scope

We will compare:

- **Source side**:
  - A detailed, external **patch changelog document** (covering all patches since 1.0).
  - Official HOI4 patch notes and verified behavior for patches ≥ 1.13 (or another baseline the user chooses).
- **Target side**:
  - All `.md` files in this repository, with particular focus on:
    - Systems that have changed significantly in recent patches (e.g., peace AI, supply, MIOs, special projects).
    - Files that already have version notes (frontmatter or inline) that may now be outdated.

The aim is to ensure that for the **current target version** of the database (currently 1.14+), all documented behaviors match modern HOI4, and any older behaviors are clearly marked as legacy.

---

## 2. Goals

For each relevant patch (starting from the chosen baseline, e.g. **1.13**):

1. **Behavioral accuracy**
   - Confirm that any **mechanic changes** mentioned in the patch notes are correctly reflected in the relevant `.md` files.
   - Update or add:
     - New mechanics (new defines, modifiers, triggers/effects, systems).
     - Changed mechanics (e.g., AI behavior, cost formulas, limits).
     - Deprecated/removed mechanics (mark as legacy, with version boundaries).
2. **Version labelling**
   - Maintain clear version ranges in:
     - YAML frontmatter (`version:`) where it describes the coverage of the file as a whole.
     - Inline notes for specific features (e.g., “1.13+: X behavior; pre-1.13: Y behavior”).
3. **Avoid regressions**
   - Preserve important historical/legacy notes where they help modders targeting older versions, but ensure they are:
     - Clearly marked as **pre-X.Y** or **legacy**.
     - Not misleading for users targeting current versions.

---

## 3. Procedure (Per Patch)

For each patch ≥ baseline (e.g., 1.13, 1.14, 1.15, …):

1. **Review patch summary**
   - From the patch changelog document, extract:
     - Changed systems (e.g., supply, peace conference AI, on_actions, modifiers).
     - New systems (e.g., special projects, new MIO behavior).
     - Removed/deprecated systems.
2. **Map changes to domains/files**
   - For each change, map it to the affected domain and file(s) in this repo:
     - E.g., “peace AI rewritten” → `/content/ai_strategy.md`, `/scripting/triggers_specialized.md` (peace triggers).
     - “New modifiers added” → `/modifiers_list/*.md`, `/scripting/modifiers.md`.
     - “Supply system rework” → `/map/supply.md`, `/core/file_syntax.md` (if syntax changed).
3. **Check current documentation**
   - Confirm if the current `.md` file:
     - Already documents the new behavior correctly.
     - Still describes only the old behavior, or mixes versions ambiguously.
4. **Update documentation**
   - If updates are needed:
     - Adjust explanations, examples, and edge-case notes to match current patch behavior.
     - Add or update version notes (e.g., “Pre-1.13 behavior (legacy) …”, “1.13+ behavior …”).
     - Add any new entities (defines, modifiers, triggers, effects) introduced in that patch to the appropriate lists.
5. **Log significant changes**
   - For major rewrites (e.g., peace AI, supply, special projects), record a short summary in `index_progress_log.md` mentioning:
     - Which patch version prompted the change.
     - Which files were updated.

---

## 4. Execution Strategy

After the master index and all domains are in place:

1. **Choose the baseline version explicitly**
   - E.g., “Treat **1.13** as the baseline; ensure everything is correct for **current version** (e.g. 1.14/1.15).”
2. **Run through patches in order (newest → oldest or vice versa)**
   - Recommended: newest → older within the ≥baseline range (so the latest behavior is always in mind).
3. **Priority systems**
   - Higher priority for systems known to have changed:
     - Scripting and AI: `/scripting/*.md`, `/content/ai_strategy.md`.
     - Supply, map, and logistics: `/map/supply.md`, `/map/strategic_regions.md`.
     - Modifiers and defines: `/scripting/modifiers.md`, `/modifiers_list/*`, `/scripting/defines.md`, `/defines_list/*`.
     - Special DLC systems: MIOs, special projects, etc.
4. **Stabilize on one “current” version**
   - Once sync is done, ensure that:
     - The repo has a clearly stated “current game version” (in `README.md` or a dedicated note).
     - Any older behavior is consistently tagged and does not override up-to-date explanations.

---

## 5. Interaction with Other Plans

- **Crosslink audit** (`crosslink_audit_plan.md`):
  - Patch sync may add new references (e.g., new defines/modifiers). These should be validated during the crosslink audit.
- **In-game documentation audit** (`game_docs_audit_plan.md`):
  - Some recent behaviors may only be described in patch notes or in-game docs; patch sync and game-doc sync can share findings.

Both audits (in-game docs and patch sync) are **deliberately scheduled after** the main index and domain normalization work so that structural changes don’t invalidate their results.
