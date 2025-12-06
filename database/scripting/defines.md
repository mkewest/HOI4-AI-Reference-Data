---
domain: scripting
concept: defines
version: 1.14+
requires: [file_syntax]
relates: [effects, triggers_core, modifiers]
---

# Defines System

Defines are read-only game constants that control core gameplay mechanics, balance, and engine limits. They are written in Lua, not PDXscript, and stored in `common/defines/*.lua`.

## File Structure and Syntax

Defines use Lua syntax with a specific structure:

```lua
NDefines.NGame.START_DATE = "1936.1.1.12"
NDefines.NGame.END_DATE = "1949.1.1.1"
NDefines.NDiplomacy.BASE_SURRENDER_LEVEL = 0.2
```

> [!CRITICAL] NO COMMAS between statements. Adding commas causes immediate game crash on launch:

```lua
-- WRONG - crashes
NDefines.NGame.START_DATE = "1936.1.1.12",
NDefines.NGame.END_DATE = "1949.1.1.1"

-- CORRECT
NDefines.NGame.START_DATE = "1936.1.1.12"
NDefines.NGame.END_DATE = "1949.1.1.1"
```

This is standard Lua syntax, but easy to forget coming from PDXscript.

## Define Categories

Defines are organized into categories by domain:

**Core Game:**

- `NDefines.NGame` - Start/end dates, game speed, iterations
- `NDefines.NGeography` - Map and terrain constants
- `NDefines.NGr aphics` - Visual and rendering limits

**Military:**

- `NDefines.NMilitary` - Combat mechanics, organization
- `NDefines.NAir` - Air combat and missions
- `NDefines.NNavy` - Naval combat and convoy
- `NDefines.NUnit` - Unit stats and behavior

**Economy and Production:**

- `NDefines.NProduction` - Factory efficiency, construction
- `NDefines.NTrade` - Trade and resources
- `NDefines.NBuildings` - Building costs and effects
- `NDefines.NSupply` - Supply system constants

**Politics and Diplomacy:**

- `NDefines.NDiplomacy` - Diplomatic actions, wargoals
- `NDefines.NPolitics` - Stability, war support, government
- `NDefines.NCountry` - Country-level constants

**Technology and Research:**

- `NDefines.NTechnology` - Research speed, ahead-of-time
- `NDefines.NFocus` - National focus mechanics

**Intelligence:**

- `NDefines.NIntel` - Intelligence agency mechanics
- `NDefines.NOperatives` - Operative stats and operations
- `NDefines.NResistance` - Resistance and compliance

**UI and Interface:**

- `NDefines.NInterface` - UI behavior and limits
- `NDefines.NSound` - Audio settings

**AI:**

- `NDefines.NAI` - AI behavior weights and thresholds

## File Loading

Files in `common/defines/` load in **ASCII character ID order**:

```text
00_defines.lua      # Loads first
01_custom.lua       # Loads second
zzz_overrides.lua   # Loads last
```

Numbers sort before letters. Use filename prefixes to control load order.

## Partial Overrides

Defines support partial overrides - you don't need to copy entire files:

```lua
-- In your mod's 01_my_changes.lua
NDefines.NGame.START_DATE = "1933.1.1.12"
NDefines.NDiplomacy.BASE_SURRENDER_LEVEL = 0.15

-- Only these two values change; all other defines remain default
```

This enables clean modding without copying hundreds of unchanged values.

## Forbidden Files

> [!CRITICAL] NEVER include 00_defines.lua or 00_graphics.lua in mods. These files change with every game update and including them prevents your mod from receiving balance patches and engine fixes.

Always create new files with different names:

- `01_my_mod.lua` ✓
- `custom_defines.lua` ✓  
- `00_defines.lua` ✗ Forbidden

## Graphics Defines Merge

`NDefines_Graphics` is a separate table that merges into `NDefines` using **pointer references**:

```lua
-- In NDefines_Graphics
NDefines_Graphics.NGraphics.CITY_LEVEL_FOR_BORDER = 2

-- Accessible as
NDefines.NGraphics.CITY_LEVEL_FOR_BORDER
```

Changes to `NDefines_Graphics` update the main `NDefines` table. This is an engine-level merge, not a script operation.

## Value Types and Constraints

### Numeric Types

```lua
NDefines.NGame.MAX_EFFECT_ITERATION = 1000  -- Integer
NDefines.NDiplomacy.BASE_SURRENDER_LEVEL = 0.2  -- Float
```

Integers and floats follow standard Lua typing. Some defines have specific range constraints.

### String Types

```lua
NDefines.NGame.START_DATE = "1936.1.1.12"  -- Date string format
NDefines.NProduction.FUEL_RESOURCE = "oil"  -- Resource token
```

Date format: `YYYY.M.D.H` (year.month.day.hour)

### Array Types

```lua
NDefines.NGame.GAME_SPEED_SECONDS = {2.0, 1.0, 0.5, 0.2, 0.0}
```

> [!CRITICAL] `GAME_SPEED_SECONDS` must have exactly 5 entries, and the last entry MUST be 0. Other array sizes crash the game.

Arrays use 1-based indexing (Lua standard). Access as `NDefines.NGame.GAME_SPEED_SECONDS[1]`.

### Color Arrays

```lua
NDefines.NGraphics.COUNTRY_COLOR_SATURATION_MODIFIER = {0.6, 0.65, 0.5, 1.0}
```

Format: `[r, g, b, a]` with values 0.0-1.0. Some accept RGB only (3 values), others require RGBA (4 values).

## Common Define Constraints

### Range-Limited Values

**BASE_SURRENDER_LEVEL:** Valid range 0.0-1.0 only. Values outside cause undefined behavior.

**Opinion/Trust Values:** Capped at ±100. Values beyond range are clamped at runtime.

### Required Formats

**Date Strings:** Must use `YYYY.M.D.H` format exactly. Invalid formats crash the game or cause incorrect date parsing.

### Timing Multipliers

Many timing defines use implicit multipliers:

```lua
NDefines.NDiplomacy.TRUCE_BREAK_COST_PP = 50  -- Multiplied by fraction remaining
```

Breaking a truce with 0.5 (50%) remaining costs: `50 * 0.5 = 25 PP`

**DECAY_RATE_OF_NEGATIVE_OPINION_AFTER_BEING_KICKED:** Applied WEEKLY, not daily. Value of 0.1 means -0.1 per week, not per day.

## Localization Dependencies

Changing resource-related defines requires updating localization:

```lua
NDefines.NProduction.FUEL_RESOURCE = "crude_oil"  -- Changed from "oil"
```

Must update:

- `FUEL_DAILY_GAIN_FROM_OIL:0` localization key
- `FUEL_DAILY_GAIN_OIL_ONLY:0` localization key
- Resource icon references

Without localization updates, the UI shows broken icons and text.

## Scripting Limits

### MAX_EFFECT_ITERATION

Maximum iterations for `for_loop_effect` and `while_loop_effect`: 1000 by default.

Exceeding this limit causes the loop to stop automatically without error or warning. The script continues execution after the loop.

```lua
NDefines.NGame.MAX_EFFECT_ITERATION = 1000  -- Default
```

To extend for complex mods:

```lua
NDefines.NGame.MAX_EFFECT_ITERATION = 5000  -- Increased limit
```

### MAX_SCRIPTED_LOC_RECURSION

Maximum recursion depth for scripted localization: default varies by version.

> [!CRITICAL] Exceeding this limit causes a game crash. This occurs when scripted localization references itself or creates circular reference chains.

Example crash scenario:

```hoi4
defined_text = {
    name = recursive_text
    text = {
        localization_key = "TEXT_WITH_[ROOT.recursive_text]"  # Self-reference
    }
}
```

## Save Compatibility

### SAVE_VERSION

Ties to game version - changing this breaks save compatibility:

```lua
NDefines.NGame.SAVE_VERSION = 11400  -- Version 1.14.0
```

Mods should never change this define. Save version mismatches prevent save loading.

### CHECKSUM_SALT

Changes game checksum when binaries change:

```lua
NDefines.NGame.CHECKSUM_SALT = "ABCD"
```

Modifying this causes checksum mismatches in multiplayer. Only change if intentionally forcing incompatibility.

## Common Define Patterns

### Cost Multipliers

```lua
NDefines.NDiplomacy.GUARANTEE_COST = 25  -- Base PP cost
NDefines.NProduction.BASE_FACTORY_COST_IC = 10800  -- Factory IC cost
```

Most costs are base values multiplied by situation-specific factors.

### Ratio Values

```lua
NDefines.NMilitary.COMBAT_VALUE_ORG_IMPORTANCE = 1.0  # 0.0-1.0 range
NDefines.NProduction.MIN_POSSIBLE_TRAINING_MANPOWER = 0.3  # Percentage
```

Ratio defines typically use 0.0-1.0 range where 1.0 = 100%.

### Timeout Values

```lua
NDefines.NDiplomacy.VOLUNTEERS_RETURN_DAYS = 7  -- Days
NDefines.NIntel.INTEL_NETWORK_MIN_OPERATIVES = 1  -- Count
```

Timing defines usually express duration in days. Some use hours or months - check context.

## Key Defines by Domain

### Game Flow

- `START_DATE` / `END_DATE`: Campaign date boundaries
- `GAME_SPEED_SECONDS`: Speed settings (5 entries required)

### Map Limits

- `PROVINCE_AREA_LIMIT`: Maximum map area (13,238,272 px default)
- `BORDER_LIMIT`: Maximum province borders (65,536 default)
- `MINIMUM_PROVINCE_SIZE_IN_PIXELS`: Minimum province size (2 px default)

### Scripting

- `MAX_EFFECT_ITERATION`: Loop iteration limit (1000 default)
- `MAX_SCRIPTED_LOC_RECURSION`: Localization recursion depth

### Combat

- `COMBAT_VALUE_ORG_IMPORTANCE`: Organization vs HP weighting
- `BASE_COMBAT_WIDTH`: Default combat width
- `RIVER_CROSSING_PENALTY`: Combat penalty for river crossings

### Economy

- `BASE_FACTORY_COST_IC`: Factory construction cost
- `FUEL_RESOURCE`: Fuel resource token name
- `BASE_FUEL_CAPACITY`: Base fuel storage

### Diplomacy

- `BASE_SURRENDER_LEVEL`: Capitulation threshold (0.0-1.0)
- `TRUCE_BREAK_COST_PP`: PP cost for breaking truce
- `GUARANTEE_COST`: PP cost for guarantee

## Related Systems

For complete enumeration of all defines by category, see the defines_list domain files:

- Game Constants: See [NGame](/defines_list/NGame.md)
- Military Constants: See [NMilitary](/defines_list/NMilitary.md)
- Diplomacy Constants: See [NDiplomacy](/defines_list/NDiplomacy.md)
- Graphics Constants: See [NGraphics](/defines_list/NGraphics.md)

For modifier mechanics that interact with defines, see [Modifiers](/scripting/modifiers.md).

For effects that reference define values, see [Effects](/scripting/effects.md).
