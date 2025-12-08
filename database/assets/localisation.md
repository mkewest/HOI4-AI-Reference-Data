---
domain: assets
concept: localisation
version: 1.14+
requires: [scripted_loc]
relates: [interface, sprites, scripted_gui]
---

# Localization System

Localization files in `localisation/*.yml` provide translated text strings using a key-value syntax. The system supports color formatting, dynamic variables, nested references, and namespace-based content generation.

> [!CRITICAL] Localization files must use UTF-8 with BOM encoding (not UTF-8 without BOM). Files without BOM fail silently or cause errors. If a language database is never assigned AND the file has UTF-8-BOM AND a localization key is present, the game crashes with error 0xC0000005.

## File Structure

### Language Database Assignment

Every localization file must begin with a language database assignment as the first line:

```yaml
l_english:
 key_name:0 "Translated text"
 another_key:1 "More text"
```

The language identifier must match one of the supported language codes: `l_english`, `l_french`, `l_german`, `l_spanish`, `l_braz_por`, `l_polish`, `l_russian`, `l_japanese`, `l_simp_chinese`. The filename must contain the language ID somewhere in its name.

### Key-Value Syntax

Keys use format: `key:version "value"` where:

- **key**: Alphanumeric characters, underscores, periods, and hyphens. No spaces, diacritics, non-Latin characters, or special characters allowed.
- **version**: Optional integer suffix after colon
- **value**: Must be wrapped in double quotes. Single-line only. Use `\n` for newlines, `\"` to escape quotes within strings.

> [!CRITICAL] One syntax error breaks the entire file from that error point forward, not just the affected line. Missing closing quotes cause everything after to fail. Version numbers with non-numeric characters (like hyphens) break the rest of the file. Keys with spaces or special characters show "Expected colon(:) at line X" error without specifying which file.

When key parsing fails due to spaces or special characters, the error message indicates the line number but not the filename, making multi-file projects difficult to debug.

## Color Formatting

### Color Codes

Text colors use the `§` symbol followed by a character code. All colored text requires both opening code and closing `§!` sequence.

```yaml
colored_text:0 "§RRed text§! and §Ggreen text§!"
```

> [!CRITICAL] Missing `§!` at string end causes color to spill over into the next text element that renders. Multi-byte UTF-8 characters after `§` only read the last byte: `§Ä€` produces "character id '0'" error, `§Å` produces "character 'M'" error.

Standard color codes:

| Code | RGB Values | Usage |
|------|------------|-------|
| `C` | 35, 206, 255 | Cyan highlight |
| `L` | 195, 176, 145 | Light tan |
| `W` | 255, 255, 255 | White |
| `B` | 0, 0, 255 | Blue |
| `G` | 0, 159, 3 | Green |
| `R` | 255, 50, 50 | Red |
| `b` | 0, 0, 0 | Black |
| `g` | 176, 176, 176 | Gray |
| `Y` | 255, 189, 0 | Yellow/Gold |
| `H` | 255, 189, 0 | History (same as Y) |
| `T` | 255, 255, 255 | Title (same as W) |
| `O` | 255, 112, 25 | Orange |

Numeric codes `0` through `9` and `t` provide additional colors. Custom colors are defined in `interface/core.gfx` textcolors array.

Error messages regarding color codes show character IDs or bytes but don't specify file location, only the character position or ID. "character id '0'" means either a NULL character or `§` at string end without a following character or closing tag.

Windows Explorer cannot search `.yml` file contents - use text editor "Find in Files" functionality to locate color code errors across multiple files.

## Variable Formatting

### Dynamic Variables

Variables insert dynamic values using `[?variable_name|format_codes]` syntax:

```yaml
population_text:0 "Population: [?population|*]"
percentage_text:0 "Growth: [?growth|%+2]"
```

Format codes modify display:

| Code | Effect |
|------|--------|
| `*` or `^` | SI units with 2 decimals |
| `=` | Prefix +/- sign |
| `0-9` | Decimal places (max 3) |
| `%` | Multiply by 100, append % |
| `%%` | Append % without multiply |
| `+` | Green if positive, yellow if zero, red if negative |
| `-` | Red if positive, yellow if zero, green if negative |

Format code priority: last code wins when multiple specified. Static color codes (R/G/Y) have lower priority than dynamic color codes (+/-). `%%` overrides `%` even if `%` is specified after `%%`. For example, `[?var|+Y]` is treated as `[?var|+]` with Y ignored. Unrecognized format characters are silently ignored.

### Color Inheritance

Variables without explicit color formatting inherit from three sources in priority order:

1. Active `§` color block (if variable appears within `§code...§!`)
2. Element's `text_color_mode` attribute (if set in GUI)
3. Font default color

Static color codes (R/G/Y) have lower priority than dynamic color codes (+/-) when both are specified.

## Namespaces

### Namespace Syntax

Namespaces access dynamic content using `[Scope.Function]` or `[TAG.variable.Function]` syntax:

```yaml
country_name:0 "Welcome to [Root.GetName]"
leader_text:0 "[This.GetLeader] leads [This.GetFactionName]"
```

Default scope is none - most contexts require explicit scoping. Characters pre-1.12.8 must scope into country first: `[USA.USA_character.GetName]`. Direct character ID access fails in older versions.

Namespaces don't work in wars, country names, and most UI elements. When used in unsupported contexts, the literal text with brackets displays instead of evaluating.

### Supported Contexts

Namespaces work in: focuses (requires `dynamic=yes`), ideas, dynamic_modifiers, decisions, events, custom_effect_tooltip, custom_trigger_tooltip, boolean_flags, operations.

Focus titles need `dynamic=yes` attribute or the namespace value freezes at game start until UI reload.

Scripted localization keys in `pdx_tooltip` GUI elements show dollar signs unless wrapped in scripted loc first. This occurs because nested loc keys in pdx_tooltip interface elements render the variable syntax literally.

### Country Functions

Available country-scope functions: `GetName`, `GetTag`, `GetLeader`, `GetManpower`, `GetFactionName`, `GetAgency`, `GetFlag`, `GetNameWithFlag`, `GetNameDef`, `GetNameDefCap`, `GetAdjective`, `GetAdjectiveCap`, `GetOldName`, `GetOldNameDef`, `GetOldNameDefCap`, `GetOldAdjective`, `GetOldAdjectiveCap`, `GetNonIdeologyName`, `GetNonIdeologyNameDef`, `GetNonIdeologyNameDefCap`, `GetNonIdeologyAdjective`, `GetNonIdeologyAdjectiveCap`, `GetPartySupport`, `GetLastElection`, `GetRulingParty`, `GetRulingPartyLong`, `GetRulingIdeology`, `GetRulingIdeologyNoun`, `GetCommunistParty`, `GetDemocraticParty`, `GetFascistParty`, `GetNeutralParty`, `GetCommunistLeader`, `GetDemocraticLeader`, `GetFascistLeader`, `GetNeutralLeader`, `GetPowerBalanceName`, `GetPowerBalanceModDesc`, `GetRightSideName`, `GetLeftSideName`, `GetActiveSideName`, `GetTrendingSideName`, `GetActiveRangeName`, `GetActiveRangeModDesc`, `GetActiveRangeRuleDesc`, `GetActiveRangeActivationEffect`, `GetActiveRangeDeactivationEffect`, `GetChangeRateDesc`, `GetBopTrendTextIcon`.

### Other Functions

General functions available across multiple scope types: `GetName`, `GetDateText`, `GetDate`, `GetMonth`, `GetYear`, `GetID`, `GetCapitalVictoryPointName`, `GetSheHe`, `GetSheHeCap`, `GetHerHim`, `GetHerHimCap`, `GetHerHis`, `GetHerHisCap`, `GetHersHis`, `GetHersHisCap`, `GetHerselfHimself`, `GetHerselfHimselfCap`, `GetIdeology`, `GetIdeologyGroup`, `GetRank`, `GetCodeName`, `GetCallsign`, `GetSurname`, `GetFullName`, `GetWing`, `GetWingShort`, `GetAceType`, `GetMissionRegion`, `GetTokenKey`, `GetTokenLocalizedKey`, `GetDateString`, `GetDateStringShortMonth`, `GetDateStringNoHour`, `GetDateStringNoHourLong`.

### Function Result Interpretation

Function results are interpreted as localization keys only when the entire string consists solely of that function. For example, `[THIS.GetTag]` returns the non-ideology name if it exists, but `"loc_key_[ALB.GetTag]"` produces literal text `"loc_key_ALB"` rather than `"loc_key_albania"`.

## Nesting and References

### Nested Localization Keys

Reference other localization keys using `$key_name$` syntax:

```yaml
base_text:0 "Basic message"
composed_text:0 "Prefix $base_text$ suffix"
```

Dollar sign literals require escaping: `$$` produces a single `$` character.

Bindable variables in scripts use `$VAR$` syntax and are replaced at runtime with provided values.

Nested loc keys in `pdx_tooltip` GUI elements show `$` signs visible to players. Bypass this by wrapping the reference in scripted localization first.

## Special Features

### Text Icons

Icons insert using `£icon_name` or `£icon_name|frame` syntax:

```yaml
icon_text:0 "Resources: £resource_icon"
multiframe_icon:0 "Frame 1: £animated_icon|1"
```

> [!CRITICAL] Multi-frame icons require `legacy_lazy_load = no` in the sprite definition or the wrong frame displays. Frame indexing starts at 1 for the first frame.

### Flags

Country flags insert using `@TAG` syntax:

```yaml
country_text:0 "Message from @USA about @GER"
```

The tag must be a valid three-letter country code. Invalid tags display as empty boxes or question marks.

## Bindable Localization

Version 1.15+ supports bindable variables in specific contexts: `custom_effect_tooltip`, `custom_trigger_tooltip`, and `bound_tooltip` in GUI elements.

Syntax options:

**Inline string**: `VAR = "literal string"`
**Localization key**: `VAR = loc_key_name` (no quotes for keys)
**Recursive structure**: `VAR = { localization_key = key, DATA = value }`

Variables defined in custom tooltips are local to that tooltip scope and don't persist beyond it.

## Contextual Localization

Contextual localization accesses object properties directly using `[(Object.)+Property]` syntax:

```yaml
state_info:0 "State: [(State.GetName)], Owner: [(State.Owner.GetName)]"
```

Supported objects: Ace, Building, Character, Country, IndustrialOrg, Operation, Province, PurchaseContract, SpecialProject, State, Terrain, UnitLeader.

Conditional syntax: `[(Object ? TRUE_TEXT : FALSE_TEXT)]` evaluates object existence and displays appropriate text.

## Formatters

Formatters apply specialized formatting using `<formatter>|<token>` syntax. Available formatters: `character_name`, `country_culture`, `idea_name`, `advisor_desc`, `tech_effect`, `idea_desc`, `building_state_modifier`.

### Formatter details (1.14+)
- **advisor_desc / idea_desc / idea_name**: Expect advisor/idea tokens; pull name/description with current modifiers applied. Keep tokens valid to avoid blank strings.
- **building_state_modifier**: Formats state-scoped building modifiers; ensure state scope when calling or pass a State object via contextual loc.
- **character_name**: Resolves character display name; pairs well with loc objects (Character) for contextual loc.
- **country_culture**: Prints culture string for country; requires Country scope or Country loc object.
- **country_leader_desc**: Uses leader description; ensure ruling party leader exists in scope or provide fallback.
- **tech_effect**: Renders technology effect text; expects tech token.

> [!TIP] Cross-reference with `localisation/loc_objects.md` (once added) for supported object properties when mixing formatters and contextual localization.

## Localization Objects (Loc Objects)

Localization objects expose scoped properties and promotions for contextual localization using `[(Object.Property)]` syntax. Common objects include:
- Ace
- Building
- Character
- Country
- Faction
- IndustrialOrg
- LocalizationEnvironment
- Operation
- Province
- PurchaseContract
- Scope
- SpecialProject
- State
- Terrain
- UnitLeader

Example usage:
```yaml
state_info:0 "State: [(State.GetName)], Owner: [(State.Owner.GetName)]"
ace_call:0 "Ace [(Ace.GetCallsign)] from wing [(Ace.GetWingShort)]"
```

Object properties are evaluated in the current scope unless you qualify with an object (e.g., `State.Owner`). For each object, properties generally include:
- Names and display variants (`GetName`, `GetNameWithFlag`, etc.)
- Pronoun helpers (`GetSheHe`, `GetHerHis`, capitalized variants)
- Context-specific fields (e.g., ace wing/mission, country parties/power balance, character ideology)

> [!NOTE] Properties differ per object; consult the in-game docs or object definitions when adding new loc strings. Ensure the object exists in scope to avoid empty output.

## Scripted Localization

Scripted localization enables conditional text selection through trigger evaluation in `common/scripted_localisation/*.txt`:

```hoi4
example_scripted_loc = {
    text = {
        trigger = { has_war = yes }
        localization_key = "war_text"
    }
    text = {
        trigger = { has_war = no }
        localization_key = "peace_text"
    }
}
```

Usage in localization: `[example_scripted_loc]`

The default scope is the current scope (unlike namespaces which default to none). Temporary variables set in trigger blocks persist for localization key display, enabling math operations between variables. The first matching text block is used with top-to-bottom evaluation.

Dynamic keys support variables: `[?var]` inserts variable value before key evaluation. Recursion allows arrays or complex logic through nested structures.

## Replace Folder

The `localisation/<language>/replace/` folder overrides base game localization. Files in replace folders must still be inside the localisation directory - `replace/` at root doesn't work.

Replace folders override base game only, not other mods. Only specified keys need to be included - the rest of the file isn't necessary. This enables targeted text changes without duplicating entire localization files.

## Overlap and Priority

When multiple mods or files define the same key, priority is inconsistent and favors base game in most cases. The replace folder gets priority over base game keys. Overlap warnings appear in `logs/text.log` but don't specify which value will actually be used.

## Common Issues

### Syntax Errors

Space after `\n` in multiline text appears in-game as unwanted indentation. Avoid extra whitespace after newline escape sequences.

Version numbers with non-numeric characters break file parsing from that point forward. Use numeric-only version integers.

### Crashes and Silent Failures

> [!CRITICAL] Missing language database assignment with UTF-8-BOM encoding and existing localization keys causes crash 0xC0000005. Always include `l_<language>:` as the first line.

`§` without a following character or with a non-existent color code crashes or fails silently. Always pair color codes with closing `§!` tags.

Special characters in keys produce "Expected colon(:)" errors that don't specify the problematic file. Restrict keys to alphanumeric characters, underscores, periods, and hyphens.
