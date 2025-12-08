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