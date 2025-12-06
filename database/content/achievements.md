---
domain: content
concept: achievements
version: 1.12.1+
requires: [triggers]
relates: []
---

# Custom Achievements

Custom achievements allow mods to define their own achievement system with unique icons and conditions. Added in version 1.12.1.

## File Structure

Custom achievements are organized across three directories:

**Definitions**: `common/achievements/custom_achievements_achievements.txt` - Contains achievement logic and conditions

**Icons**: `gfx/achievements/` - Stores achievement icon files

**Localization**: `localization/english/*_l_english.yml` - Defines achievement names and descriptions

## Icon Requirements

Each achievement requires three icon files in DDS format:

- `{id}.dds` - Colored icon shown when achieved
- `{id}_grey.dds` - Grayscale icon shown when locked
- `{id}_not_eligible.dds` - Icon shown when permanently impossible

Sprite definitions in `.gfx` files are not required for achievement icons. The game automatically loads icons based on the achievement ID.

## Achievement Definition

Achievements use a unique identifier system scoped at the mod level:

```hoi4
unique_id = my_mod_achievements

custom_achievement = {
    id = conquer_world
    
    possible = {
        # Evaluated only at game start
        has_dlc = "My Required DLC"
        date > 1936.1.1
    }
    
    happened = {
        # Checked continuously during gameplay
        controls_state = 1
        controls_state = 2
        # ... all states
    }
}
```

**unique_id**: String identifier scoped to the mod level. This prevents conflicts between different mods' achievement systems.

**id**: String identifier for the specific achievement. Used for icon filenames and localization keys.

### Evaluation Timing

**possible**: Trigger block evaluated only at game start, never again.

> [!CRITICAL] If the `possible` trigger evaluates false at game start, the achievement becomes permanently impossible for that entire playthrough. It will show the `_not_eligible.dds` icon and cannot be unlocked regardless of later conditions. Use this only for immutable requirements like DLC checks or start date restrictions.

**happened**: Trigger block checked continuously during gameplay. When this evaluates true, the achievement unlocks after approximately 2 in-game hours. This delay allows the game state to stabilize before marking completion.

### Cross-Session Tracking

The trigger `has_completed_custom_achievement` checks achievement completion across any previous session, not just the current playthrough:

```hoi4
has_completed_custom_achievement = {
    mod = my_mod_unique_id
    achievement = conquer_world
}
```

If the mod defining the achievement is not currently loaded, this trigger returns false.

## Custom Ribbons

Ribbons are cosmetic indicators that can represent ongoing progression or special status:

```hoi4
custom_ribbon = {
    id = master_strategist
    
    possible = {
        # Evaluated at game start
        always = yes
    }
    
    happened = {
        # Checked continuously
        num_of_military_factories > 100
        has_war = yes
    }
    
    ribbon = {
        frames = { 1 2 3 4 }  # Array of 4 frame indices
        
        colors = {
            { 255 0 0 255 }    # Red RGBA
            { 0 255 0 255 }    # Green RGBA
            { 0 0 255 255 }    # Blue RGBA
            { 255 255 0 255 }  # Yellow RGBA
        }
    }
}
```

**frames**: Array of exactly 4 integers defining frame indices for the ribbon animation or display.

**colors**: Array of exactly 4 RGBA color values. Each color is specified as an array of 4 integers (red, green, blue, alpha) with values 0-255.

Ribbons use the same `possible` and `happened` evaluation timing as achievements.

## Localization Keys

Each achievement requires two localization keys:

- `{id}_NAME`: The achievement title displayed in the UI
- `{id}_DESC`: The achievement description explaining requirements

Example:

```yaml
l_english:
 conquer_world_NAME: "Master of the World"
 conquer_world_DESC: "Control every state on the map"
```

## Ironman Requirement

Custom achievements only track in Ironman mode, matching base game achievement behavior. The `has_completed_custom_achievement` trigger always returns false in non-Ironman games.

## Mod Compatibility

Achievements persist across sessions as long as the defining mod remains loaded. If a mod is unloaded, its achievement tracking becomes unavailable but previously unlocked achievements remain in the player's profile.

When a mod updates its achievement definitions, existing progress may reset depending on the changes made to `possible` and `happened` conditions.
