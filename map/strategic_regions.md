---
domain: map
concept: strategic_regions
version: 1.14+
requires: [provinces, coordinates]
relates: [terrain, supply]
---

# Strategic Regions

Strategic regions group provinces for weather, naval terrain assignment, and strategic-level gameplay systems. Each province must belong to exactly one strategic region.

## Region Definition

Strategic regions are defined in `map/strategicregions/*.txt` files. Multiple regions can exist in a single file, allowing logical grouping (e.g., all Mediterranean regions in one file).

### Region Structure

```hoi4
strategic_region = {
    id = 1
    name = "STRATEGICREGION_1"
    provinces = { 1 2 3 4 5 6 7 8 9 10 }
    naval_terrain = ocean
    
    weather = {
        period = {
            between = { 0.0 30.2 }
            temperature = { -5 10 }
            min_snow_level = 0.0
            
            weather_states = {
                snow = 30
                rain_light = 50
                no_phenomenon = 20
            }
        }
    }
}
```

### Region Attributes

**id:** Integer identifying the region. Must be unique.

> [!CRITICAL] Region IDs must be sequential starting from 1 with no gaps. Skipping any number causes the game to crash during region initialization.

The ID is defined within the region definition, not by filename. This means `5_region.txt` could contain region ID 12, though this is poor organization practice.

**name:** Localization key for the region name. Should be defined in localization files. Can use plain text, but localization keys are preferred for multi-language support.

**provinces:** Array of province IDs belonging to this region. All provinces in a single state must belong to the same strategic region - the game crashes if a state spans multiple regions.

> [!CRITICAL] All provinces must be assigned to exactly one strategic region. Unassigned provinces cause crashes during map loading.

Provinces should ideally be contiguous within a region, though this is not strictly enforced. Islands are typically part of sea strategic regions rather than land regions, even if they contain land provinces.

**naval_terrain:** Provincial terrain type name (defined in `common/terrain/*.txt`) assigned to all sea provinces in this region. This overrides individual province terrain for naval provinces - land provinces use definition.csv terrain, sea provinces use strategic region naval terrain.

## Weather System

Weather is defined per strategic region using nested period blocks. The weather system calculates conditions daily per province, allowing multiple weather types to occur simultaneously.

### Weather Periods

```hoi4
weather = {
    period = {
        between = { 0.0 30.2 }
        temperature = { -5 10 }
        min_snow_level = 0.0
        
        weather_states = {
            snow = 30
            rain_light = 50
            no_phenomenon = 20
        }
    }
    
    period = {
        between = { 0.3 30.5 }
        temperature = { 5 20 }
        min_snow_level = 0.0
        
        weather_states = {
            rain_light = 40
            rain_heavy = 20
            no_phenomenon = 40
        }
    }
}
```

Multiple period blocks define weather across the year. Each period covers a date range using the `between` attribute.

### Date Format

The `between` attribute uses zero-indexed day.month format:

- 0.0 = January 1st
- 30.0 = January 31st
- 0.1 = February 1st
- 30.11 = December 31st

Both boundary days are inclusive. For example, `between = { 0.0 30.2 }` includes January 1st through March 31st.

Months are zero-indexed (0=January, 11=December), but days within months are also zero-indexed (0=1st, 30=31st for months with 31 days).

### Temperature

The `temperature` attribute defines minimum and maximum temperatures in Celsius:

```hoi4
temperature = { -5 10 }  # Min: -5°C, Max: 10°C
```

Note that `temperature_day_night` was deprecated in patch 1.11. Use only `temperature` for current versions.

### Snow Level

The `min_snow_level` attribute controls permanent snow amount (0.0 to 1.0). This is distinct from weather event snow - `min_snow_level` represents permanent snow coverage like glaciers or high-altitude snowpack, while weather states like `snow` and `blizzard` represent temporary weather phenomena.

### Weather States

The `weather_states` block uses weighted random selection. Values are relative weights, not percentages or durations:

```hoi4
weather_states = {
    snow = 30
    rain_light = 50
    no_phenomenon = 20
}
```

A state with weight 50 is twice as likely to occur as weight 25. The game normalizes these weights to probabilities when selecting weather daily.

### Available Weather States

Weather states are defined in `common/weather.txt`:

- no_phenomenon
- rain_light
- rain_heavy
- snow
- blizzard
- mud
- sandstorm

Each state provides gameplay modifiers for combat, movement, and visibility.

## Weather Positions

The `map/weatherpositions.txt` file defines where weather visuals appear on the map. Format:

```csv
RegionID;X;Y;Z;size
```

**RegionID:** Strategic region ID where this weather position appears.

**X, Y, Z:** World coordinates for the weather effect.

**size:** Either `small` or `large`, controlling the scale of the weather visual effect.

> [!CRITICAL] The file needs at least one small AND one large definition to avoid crashes. Having only small or only large weather positions causes the game to crash during weather initialization.

## Design Patterns

Strategic regions typically follow geographic or strategic groupings:

- Naval regions encompass sea areas with similar weather (North Atlantic, Mediterranean)
- Land regions group provinces by climate zones or strategic importance
- Island provinces usually belong to the surrounding sea region's strategic region

The Ural Mountains and Caucasus Mountains create natural boundaries between European, Asian, and Middle Eastern strategic regions in the base game.

## Related Defines

Weather-related defines are in the NWeather category of the defines files.
