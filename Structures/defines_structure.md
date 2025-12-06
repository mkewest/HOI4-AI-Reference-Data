# Defines Domain Structure

## INTEGRATION INSTRUCTIONS FOR FUTURE SELF

**IMPORTANT**: When the defines_list domain is complete, you must perform these integration tasks:

### 1. Update Cross-References in defines.md

Replace placeholder links with actual structure from defines_list:

**Current state** (defines.md):
```markdown
- `MAX_EFFECT_ITERATION`: See [NGame](/defines_list/NGame.md)
- `PROVINCE_AREA_LIMIT`: See [NGraphics](/defines_list/NGraphics.md)
```

**Action required**:
- Verify these file paths match actual defines_list structure
- Confirm define names are correct (check defines_list for exact tokens)
- Ensure all referenced defines exist in defines_list
- Add any missing cross-references discovered during defines_list creation

### 2. Create Bidirectional Linking

**defines.md explains**:
- HOW defines work (Lua syntax, loading, constraints)
- File structure and organization
- Partial override mechanics
- Common patterns and pitfalls

**defines_list/* files ARE**:
- The actual define values
- Complete enumeration by category
- Value types and ranges
- Usage contexts

**Required linking pattern**:

In defines.md:
```markdown
For complete enumeration of all defines by category, see the defines_list domain files:
- Game Constants: See [NGame](/defines_list/NGame.md)
- Military Constants: See [NMilitary](/defines_list/NMilitary.md)
```

In defines_list files (e.g., NGame.md):
```markdown
For define file structure, Lua syntax, and loading mechanics, see [Defines System](/scripting/defines.md).
```

### 3. Check Cross-Domain References

Multiple domains reference specific defines. Verify these references work post-integration:

**Known references**:
- Military domain: `MAX_EFFECT_ITERATION` (loop limits)
- Map domain: `PROVINCE_AREA_LIMIT`, `BORDER_LIMIT` (map constraints)
- Combat domain: `COMBAT_WIDTH` variations
- Supply domain: `RAILWAY_CONVERSION_RATE`, `SUPPLY_NODE_RANGE`

**Action required**:
- Search all generated .md files for defines mentions
- Verify define names match defines_list exactly
- Update cross-references if defines_list uses different names or structure
- Ensure inline values in other domains match define list values

### 4. Handle Define Value Updates

When base game updates change define values:

**In defines.md**:
- Update inline critical values (e.g., "MAX 1000 iterations")
- Update examples if they reference changed values
- Note version changes if significant

**In defines_list**:
- Update actual define values
- Add version notes if breaking changes
- Update descriptions if behavior changes

Keep both files synchronized - defines.md inline values should match defines_list enumeration.

### 5. Verify Lua Syntax Examples

Ensure Lua syntax examples in defines.md remain valid:
- Check array syntax matches actual defines (1-based indexing)
- Verify string format examples (dates, etc.)
- Confirm no-comma rule is clearly stated with correct example

### 6. Integration Testing Checklist

- [ ] All forward references in defines.md point to valid defines_list files
- [ ] Bidirectional links exist (defines.md ↔ defines_list)
- [ ] Cross-domain references work (military → defines_list, map → defines_list)
- [ ] Inline values in defines.md match defines_list values
- [ ] No duplicate information except critical values repeated inline
- [ ] Version-specific behavior noted in both places if relevant
- [ ] Examples in defines.md use actual define names from defines_list

---

## Overview (Normal Structure Document Content)

The defines domain consists of two parts:
1. **defines.md** - System mechanics (how defines work)
2. **defines_list/** - Actual values (what defines exist)

This structure separates conceptual knowledge from reference data.

## Current State

**defines.md** (~4800 tokens):
- Complete documentation of Lua defines system
- File structure, syntax, loading, and constraints
- Common patterns and value types
- Forward references to defines_list using placeholder format

**defines_list/**: Not yet created
- Will contain complete enumeration of all defines by category
- Format TBD (likely YAML blocks per Rule 3.2 for >20 items)
- Structure will follow NDefines categories

## File Relationships

```
defines.md (system mechanics)
    ↓ (references for complete values)
defines_list/NGame.md
defines_list/NMilitary.md
defines_list/NGraphics.md
defines_list/NDiplomacy.md
[... additional category files ...]
```

Relationship type: **"requires"** - understanding defines.md is required to use defines_list effectively, but defines_list is the authoritative source for actual values.

## Critical Edge Cases Integrated

All edge cases from `scripting_EdgeCases.txt` related to defines are integrated into defines.md:

- **NO COMMAS syntax rule**: Inline in File Structure section
- **Forbidden files (00_defines.lua)**: Inline in Forbidden Files section
- **GAME_SPEED_SECONDS constraints**: Inline in Value Types section
- **Graphics merge behavior**: Inline in Graphics Defines Merge section
- **SAVE_VERSION compatibility**: Inline in Save Compatibility section
- **MAX_EFFECT_ITERATION limits**: Inline in Scripting Limits section
- **Localization dependencies**: Inline in Localization Dependencies section

## Usage Pattern

**For modders changing defines**:
1. Read defines.md to understand HOW to change defines safely
2. Reference defines_list to find WHICH define to change
3. Check cross-references for defines mentioned in other domains

**For troubleshooting**:
1. Search defines_list for suspected define
2. Read defines.md for constraints and behavior
3. Verify value types and ranges

## Token Distribution

Current state:
- defines.md: ~4800 tokens (complete)
- defines_list/: TBD (depends on final structure)

Estimated defines_list total: ~15,000-20,000 tokens across all category files based on ~250-300 defines with descriptions.

## Version Notes

defines.md current for HOI4 1.14+. When game updates change define behavior or add new categories, both defines.md (if mechanics change) and defines_list (if values change) require updates.
