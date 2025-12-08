# AI Instructions (post-run content sync)

Inputs:
- `update/changes/changes.md` — unified diffs per changed doc.
- `update/changes/changelog_cropped.txt` — patch notes newer than `last_patch_version` in `database/master_index.json`.
- `update/_update_log_instructions.md` Instructions for creating the `_update_log.md` file
- `update/_update_todo_instructions.md` Instructions for creating the `_update_todo.md` file

There will be three phases to each update.
Analysis
- Determine if anything needs updating, if so what, where and in what way. Write all proposed changes to `_update_todo.md`.
Discussion
- Justify proposed changes to the user, why does this need updating, why make a new file for this etc... This will be done for each proposed change or in some cases for a group of very similar changes.
Implementation
- Implement approved changes in the ways agreed upon, will also happen one item or category at a time.


## Phase 1 - Analysis:

1. Filter `update/changes/changelog_cropped.txt` for modding relevance; ignore player-facing fluff.
2. For each header called `*_documentation.md` and each modding relevant line in the changelog: 
	1. Determine if the changed information needs to be updated. Is it qualitatively different?
	2. If it is, determine if and if so where in the database this information exists.
	3. If it exists and needs to be updated, determine in what way. If it doesn't exist, determine if it should be added to an existing file or if the creation of a new file is warranted.
	4. Based on previous steps, determine what links and/or index entries need to be added/removed/edited.
	5. Create an entry in the `_update_todo.md` file following the `_update_todo_instructions.md`

Notes:
- `_update_todo.md` entries should include short description of new/changed mechanics, defines, modifiers, triggers/effects, systems.

## Phase 2 - Discussion:
1. For every type of change there will be a different justification needed. They are:
	- Creating a new file - Why do we need to create a new file? What is the closest file(s) to this domain or concept that exist and why can't this new information be added there instead? Valid reasons are for example, file size would be to big or not correlated closely enough among others. 
	- Deleting an existing file - The only real justification for this is if some system or define group gets completely removed
	- Adding data to existing file - Are you sure this information does not exist already somewhere in the database? If not is this information relevant?
	- Removing data from existing file - What made the data in the database no longer valid?
2. When the user instructs you to do something other than what you had initially planned and written in the `_update_todo.md` update that entry to align with the new plan
3. When all entries have been decided upon, go ahead and ask the user which change(s) should be implemented first and go ahead to phase 3

## Phase 3 - Implementation
1. Go through each entry in `_update_todo.md` in whatever order the user instructs.
2. When you are updating existing files or creating new one's, remember the following
	- This database is highly crosslinked and semantically chunked, make sure to add links to other pages and defines wherever one could be useful. Use existing files for reference.
	- Add version bounds inline or in frontmatter if it pertains to that whole file when behavior differs by patch.
	- Mark removed/legacy behavior clearly.
	- Keep frontmatter accurate; add/adjust relates/requires if new concepts appear.
	- Keep links accurate; add/remove/adjust links if new concepts/defines/intertangling appears.
	- If data seems missing/wrong, report the paths/files inspected.