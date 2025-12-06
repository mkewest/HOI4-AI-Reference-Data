---
domain: database
concept: namelists
version: 1.14+
requires: [units, navies]
relates: [oob, localisation]
---

# Namelists System

Namelists provide naming schemes for military units, ships, and operatives. They're organized by type: divisions, ships, generic equipment, and operative codenames.

## Division Namelists

Division namelists are defined in `common/units/names_divisions/` with the filename format `TAG_names_divisions.txt`.

### Structure

```hoi4
division_names_list = {
    name = "Division Names"
    
    for_countries = { GER AUS }
    
    can_use = {
        has_dlc = "Waking the Tiger"
    }
    
    division_types = { "infantry" "motorized" }
    
    fallback_name = "%d. Infanterie-Division"
    
    link_numbering_with = { GER_INF_01 }
    
    ordered = {
        1 = { "%d. Infanterie-Division" }
        2 = { "%d. Gebirgsjäger-Division" }
        5 = { "%d. Panzergrenadier-Division" }
    }
}
```

### Core Attributes

#### name

String identifier for the namelist. Used for debugging and organization.

#### for_countries

Array of country tags that can use this namelist. When multiple countries share a namelist, they all draw from the same pool of names.

#### can_use

Optional trigger block that determines if this namelist is available. Commonly used for DLC-gating or conditional naming schemes.

#### division_types

Array of division types that use these names. Types include: `infantry`, `motorized`, `mechanized`, `armor`, `cavalry`, etc.

#### fallback_name

String template used when the ordered list runs out of names. Supports placeholder variables:

- `%d`: Decimal number (1, 2, 3, ...)
- `%s`: Roman numeral (I, II, III, ...)

Example: `"%d. Armee"` generates "1. Armee", "2. Armee", etc.

#### link_numbering_with

Array of namelist IDs to link numbering with. Linked namelists share the same counter, preventing duplicate numbers across different unit types.

Example: Infantry and cavalry divisions both start from 1 unless linked.

### ordered Block

```hoi4
ordered = {
    1 = { "1st Infantry Division" }
    2 = { "2nd Infantry Division" }
    3 = { "3rd Infantry Division" }
}
```

The `ordered` block defines specific names with priority keys:

- Keys are 1-based integers
- Keys can skip numbers (e.g., 1, 2, 5, 10)
- Names assigned sequentially based on key order
- After exhausting ordered names, fallback_name generates additional names

Names are assigned in key order, not definition order. Key 1 assigns first, then 2, then 3, etc.

### OOB Linking

Division namelists link to order of battle (OOB) files in `history/units/`:

```hoi4
# In OOB file
division = {
    name = "1st Infantry Division"
    division_name = {
        is_name_ordered = yes
        name_order = 1
    }
}
```

> [!CRITICAL] The `NAME_LIST_ID` in OOB files must match the exact string in the namelist's `name` attribute. Case-sensitive matching applies.

### File Size Limits

> [!CRITICAL] Namelist files with more than 1500 lines may cause namelists defined beyond that point to fail loading. The parser has a line limit per file, not per namelist.

**Workaround:** Split large namelists across multiple files to stay under the 1500-line threshold per file.

## Ship Namelists

Ship namelists are defined in `common/units/names_ships/` with the filename format `TAG_ship_names.txt`.

### Structure

```hoi4
ship_names = {
    name = "Royal Navy Ship Names"
    
    for_countries = { ENG }
    
    type = ship
    
    ship_types = {
        battleship carrier
        heavy_cruiser light_cruiser
        submarine destroyer
        # Must include BOTH MTG and non-MTG versions
    }
    
    prefix = "HMS "
    
    fallback_name = "Ship %d"
    
    unique = {
        "Victory" "Warspite" "Hood"
        "Nelson" "Rodney" "Renown"
    }
}
```

### Key Differences from Division Names

#### type = ship

Required attribute marking this as a ship namelist.

#### ship_types

Array of ship type IDs that use these names.

> [!CRITICAL] The `ship_types` array requires BOTH Man the Guns (MTG) DLC ship types AND base game ship types. For example, include both `battleship` (base) and `ship_hull_heavy_1` (MTG) to ensure compatibility across DLC ownership scenarios.

Omitting base game types breaks naming for players without MTG. Omitting MTG types breaks naming for players with MTG.

#### unique Block

```hoi4
unique = {
    "Bismarck" "Tirpitz" "Scharnhorst"
    "Gneisenau" "Admiral Hipper" "Prinz Eugen"
}
```

> [!CRITICAL] The `unique` block uses SPACE delimiters, not commas or newlines. Using commas breaks the parser and causes names to fail.

Correct:
```hoi4
unique = {
    "Name1" "Name2" "Name3"
}
```

Incorrect:
```hoi4
unique = {
    "Name1", "Name2", "Name3"  # Commas break parsing
}
```

#### No OOB Linking

Ship namelists do NOT link to OOB files. Ships are named dynamically when produced or scripted through events. There's no `name_order` system like division names have.

#### prefix

String prepended to ship names. Common examples:

- `"HMS "` - His/Her Majesty's Ship (UK)
- `"USS "` - United States Ship (USA)
- `"KMS "` - Kriegsmarine Schiff (Germany)
- `"IJN "` - Imperial Japanese Navy

The space after the prefix is intentional and must be included if desired.

## Generic Namelists

Generic namelists are defined in `common/units/names/*.txt` and serve as fallback for countries without specific namelists.

### Structure

```hoi4
generic_names = {
    name = "Generic Division Names"
    
    for_countries = { }  # Empty = applies to all
    
    division_types = { "infantry" }
    
    fallback_name = "Division %d"
    
    unique = { }  # Must be empty array for generic
}
```

### Key Requirements

#### Empty for_countries

An empty `for_countries` array means the namelist applies to all countries that don't have a specific namelist.

#### Empty unique Array

> [!CRITICAL] Generic namelists must have an empty `unique = { }` array. Providing names in the unique block for generic namelists causes conflicts when multiple countries try to use the same "unique" names simultaneously.

Generic namelists rely entirely on `fallback_name` to generate procedural names.

## Operative Codenames

Operative codenames are defined in `common/units/codenames_operatives/` and follow a different structure:

### Structure

```hoi4
operative_codenames = {
    name = "British Codenames"
    
    for_countries = { ENG }
    
    type = codename
    
    fallback_name = "Agent %d"
    
    unique = {
        "Intrepid" "Garbo" "Tricycle"
        "Cato" "Brutus" "Treasure"
    }
}
```

### type = codename

Required attribute marking this as an operative codename list.

### Assignment

> [!CRITICAL] Codenames are mutually exclusive across all active operatives for a country. Once a codename is assigned to an operative, it cannot be reused until that operative is retired or killed.

Assignment is random from the available pool. There's no OOB linking or ordered system - the game randomly selects from unused codenames.

### No OOB Linking

Like ships, operatives don't link to OOB files. Codenames are assigned dynamically when operatives are recruited.

## Placeholder Variables

Namelists support placeholder variables in fallback names:

| Placeholder | Output | Example |
|-------------|--------|---------|
| `%d` | Decimal number | 1, 2, 3, ... |
| `%s` | Roman numeral | I, II, III, IV, V, ... |

Example usage:

```hoi4
fallback_name = "%d. Armee"        # "1. Armee", "2. Armee"
fallback_name = "%s Corps"         # "I Corps", "II Corps"
fallback_name = "Division %d (%s)" # "Division 1 (I)", "Division 2 (II)"
```

Both placeholders can appear in the same string if needed.

## Common Issues

### Names Not Appearing

If custom names don't appear for units:

1. **Check for_countries:** Verify country tag is included
2. **Check division_types:** Ensure unit type matches
3. **Verify file location:** Must be in correct directory for type
4. **Check 1500-line limit:** Split large files if exceeding limit

### Duplicate Names

If divisions get duplicate numbers:

1. **Check link_numbering_with:** Link related unit types
2. **Verify ordered keys:** Ensure keys are sequential without gaps
3. **Check fallback_name:** Ensure %d/%s placeholders are present

### Ship Names Failing

If ship names break:

1. **Check unique delimiters:** Must be spaces, not commas
2. **Verify ship_types:** Include both MTG and base game types
3. **Check prefix:** Ensure prefix string is correct with trailing space

### Operative Codenames Conflicting

If operative codenames cause errors:

1. **Check uniqueness:** Ensure codenames aren't duplicated across countries
2. **Verify pool size:** Ensure enough unique names for maximum operatives
3. **Check fallback:** Ensure fallback_name exists for when unique pool exhausts

## Related Systems

For unit creation and OOB files, see the units documentation.

For ship production and naming, see the naval production documentation.

For operative recruitment, see the intelligence documentation.
