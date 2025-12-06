---
domain: core
concept: load_order
version: 1.14+
requires: [mod_structure]
relates: [file_syntax, duplicates]
---

# Load Order

HOI4's content loading follows a deterministic sequence that affects which files override others and how duplicate definitions are resolved. Understanding load order is critical for mod compatibility and predicting which content takes precedence.

## Load Sequence

Content loads in the following order:

1. **Base game files**
2. **DLC by internal ID** (not alphabetical)
3. **User directory files** (`<user_dir>/mod/`)
4. **Mods by descriptor filename** (ASCII alphabetical order)

Within each category, alphabetical ordering follows ASCII collation where uppercase letters sort before lowercase, and underscores/hyphens sort between letters. For example: `A_mod.mod` < `Amod.mod` < `a_mod.mod` < `amod.mod`.

### Dependency Override

The `dependencies` attribute in mod descriptors overrides alphabetical ordering. Submods always load after their dependencies regardless of filename. When multiple mods specify dependencies on each other, the game resolves them to ensure dependencies load first.

> [!CRITICAL] Dependency matching requires exact name strings including special characters. An en dash (–) is not equivalent to a hyphen (-), so "My–Mod" and "My-Mod" are treated as completely different mods for dependency resolution.

### File Override Priority

When multiple files define the same content, later-loaded files win. This means mods always override base game content, and mods loaded later (alphabetically or via dependency chain) override earlier mods.

The game only checks at file level, not line level. To add a single line to a vanilla file, you must copy the entire file and modify it. The game cannot patch individual lines - you must replace the complete file.

## Filename Dependencies

Certain files have semantically meaningful names where the filename determines behavior:

- **gfx/flags/**: Flag image files use country tag and ideology as filename (`TAG_ideology.tga`)
- **history/countries/**: Country history files must match 3-character tag pattern (`TAG - Name.txt`)
- **common/countries/colors.txt**: This exact filename is required
- **common/countries/cosmetic.txt**: This exact filename is required
- **map/**: Most map files have hardcoded expected names
- **tutorial/tutorial.txt**: This exact path is required

For most other files, the filename is irrelevant - only the content and directory location matter.

## Evaluation Order

### Sequential Execution

Effects and triggers execute sequentially in the order written. This matters for:

- **Effect blocks:** Each effect executes before the next, so order affects state
- **Trigger blocks:** Evaluation proceeds top-to-bottom
- **Temporary variables in triggers:** Variables set in earlier triggers affect later ones

Modifiers are an exception - their order is irrelevant for gameplay effect, though dynamic modifier tooltips display in code order.

### Duplicate Attribute Handling

When the same attribute appears multiple times in a definition, handling varies by context:

**National focus duplicates:** Break prerequisite line generation in the focus tree rendering.

**Event immediate blocks:** Each executes sequentially as separate effect blocks.

**Idea category ideas:** Each duplicate creates a separate idea with the same attributes.

**Scripted localisation text blocks:** First valid block is used, subsequent ones ignored.

### Database Entry Creation Order

For database entries (countries, technologies, ideas, etc.), creation order can matter. Tag definition order affects event, decision, and focus evaluation order when multiple triggers check the same conditions.

Equipment must reference existing archetypes at creation time. Defining equipment before its archetype causes a CTD even if the archetype is defined later in the same file. Place archetype definitions before derived equipment in all equipment files.

### File Load Order Within Directories

Files within a directory load alphabetically by filename. ASCII ordering applies: uppercase before lowercase, with special characters like underscore and hyphen sorting between letters.

This ordering determines:

- Which scripted triggers/effects are available for other files to reference
- Which constants are defined before use
- Tag definition sequence for database evaluation

## Tag Definition Order

Countries load in the order their tags are defined in `common/country_tags/*.txt` files. This affects:

- **AI focus evaluation:** Earlier countries evaluate focus choices first
- **AI decision evaluation:** Earlier countries evaluate decisions first  
- **Event firing order:** When events check "any_country", iteration follows tag definition order

The alphabetical order is the default but not guaranteed. If specific ordering is essential, use the `dependencies` attribute in mod descriptors to ensure correct mod load sequence, or structure file naming to achieve desired internal ordering.

## Related Systems

- Mod descriptor dependencies: See [Mod Structure](/core/mod_structure.md#descriptor-attributes)
- File override behavior: See [Mod Structure](/core/mod_structure.md#file-loading-behavior)
- Checksum determination: See [Metadata](/core/metadata.md)
