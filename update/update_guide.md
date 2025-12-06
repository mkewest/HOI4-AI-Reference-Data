## Human User Instructions (quick runbook)

1) Open a terminal and go to the repo:
   - `cd update/update_script`
2) (Optional but recommended) create/activate a venv:
   - `python -m venv .venv`
   - Windows: `.\.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`
3) Run the update:
   - `python update.py`
   - When prompted, paste the HOI4 game folder path (must contain `hoi4.exe`).
4) Outputs:
   - `update/current_patch/` is populated during grab; emptied after pruning.
   - `update/changes/changes.md` (diff hunks) and `update/changes/changelog_cropped.txt`.
   - `update/archive/<yyyy-mm-dd>.zip` (snapshot of `database/` + `last_patch/`; keeps newest 2).
   - `update/last_patch/` is refreshed to the latest grabbed docs.
5) If no changes are detected, the script skips archive/rotation and leaves `last_patch/` intact.

---

## AI Instructions (post-run content sync)

Inputs for the AI:
- `update/changes/changes.md` — unified diffs per changed doc.
- `update/changes/changelog_cropped.txt` — patch notes newer than `last_patch_version` in `database/master_index.json`.
- `update/last_patch/` — latest vanilla docs snapshot (baseline for next run).
- `update/archive/` — zip snapshots of prior baseline + database. Never delete; newest 2 are kept automatically.

Workflow:
1) Filter for modding relevance; ignore player-facing fluff.
2) Map each change to repo domains/files via `master_index.json` intents and architecture rules.
3) Update `.md` files with new/changed mechanics, defines, modifiers, triggers/effects, systems.
   - Add version bounds inline or in frontmatter when behavior differs by patch.
   - Mark removed/legacy behavior clearly.
4) Log major edits in `index_progress_log.md` (which patch, which files touched).
5) Write a comprehensive change summary `changelog_<yyyy-mm-dd>.md` and place it in `update/archive/`. These are never deleted.
6) Update `last_patch_version` in `database/master_index.json` when content sync for the patch is complete.

Ground rules:
- Do not copy whole patch notes; only integrate modding-relevant behavior.
- Keep links and frontmatter accurate; add/adjust relates/requires if new concepts appear.
- If no answers are found or data seems missing/wrong, report the paths/files inspected.
- Preserve snapshots: archive zips and change logs stay in `update/archive/`.

---

## Patch Sync Playbook (post-1.13+ behavior)

Baseline:
- Explicitly choose/record the baseline (e.g., 1.13) in `database/master_index.json` (`last_patch_version`) before starting a patch pass.

Per patch (>= baseline):
1) Review patch notes/changelog (cropped file) and identify changed/new/removed systems.
2) Map each change to target repo files/domains using `master_index.json` intents and architecture rules.
3) Check current docs for correctness vs the patch; update behavior, formulas, edge cases.
4) Add version bounds: frontmatter `version` if file-wide; inline notes for feature-level differences; mark legacy/pre-baseline behavior clearly.
5) Add new defines/modifiers/triggers/effects/systems; mark removed ones as legacy.
6) Log major rewrites in `index_progress_log.md` (which patch, which files).
7) When the patch is fully integrated, bump `last_patch_version` in `database/master_index.json`.

Priority focus (when triaging):
- Scripting/AI (`/scripting/*`, `/content/ai_strategy.md`), supply/logistics/map, modifiers/defines, special DLC systems (MIOs, special projects).

---

## In-Game Documentation Audit (vanilla docs → repo coverage)

Scope/goal:
- Ensure concepts described only in vanilla in-game docs are present and accurate here; prefer repo prose, not verbatim copy.

Procedure (per vanilla doc section):
1) Identify the concept and map to repo domain/file(s) (e.g., supply nodes → `/map/supply.md`).
2) Search repo to confirm coverage and correctness.
3) If missing/unclear, add or extend the right file; integrate clarifying constraints/edge cases inline.
4) Respect version awareness: if vanilla doc is version-specific, reflect that with version bounds (frontmatter or inline).
5) Avoid redundant duplication; summarize rather than paste.
6) Log major additions in `index_progress_log.md`.

