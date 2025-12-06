---
domain: assets
concept: posteffects
version: 1.14+
requires: []
relates: [map]
---

# Posteffect System

Posteffect volumes apply visual filters and color grading to map regions. Defined in `map/posteffect_volumes.txt`, they create environmental atmosphere through fog, color tinting, and lighting adjustments.

## Posteffect Values

### Basic Structure

```hoi4
posteffect = {
    posteffect_values_day = {
        saturation = 1.0
        contrast = 1.0
        brightness = 1.0
        fog_color = { 0.5 0.5 0.6 }
        fog_distance = 100.0
    }
    
    posteffect_values_night = {
        saturation = 0.8
        contrast = 1.1
        brightness = 0.7
        fog_color = { 0.2 0.2 0.3 }
        fog_distance = 80.0
    }
}
```

Each posteffect requires day and night value sets. The system interpolates between day and night based on game time.

### Seasonal Variants

Winter posteffect variants are optional:

```hoi4
posteffect = {
    posteffect_values_day = { ... }
    posteffect_values_night = { ... }
    
    posteffect_values_day_winter = {
        saturation = 0.9
        fog_color = { 0.7 0.7 0.8 }
    }
    
    posteffect_values_night_winter = {
        saturation = 0.7
        fog_color = { 0.3 0.3 0.4 }
    }
}
```

If winter variants are not specified, the system uses standard day/night values during winter months. No error is thrown when winter variants are missing - the system silently falls back to non-winter values.

This enables partial seasonal variation - only regions requiring distinct winter atmosphere need winter definitions.

## Posteffect Inheritance

The `inherit` attribute copies all values from a specified posteffect_values block:

```hoi4
posteffect = {
    posteffect_values_base = {
        saturation = 1.0
        contrast = 1.0
        brightness = 1.0
    }
    
    posteffect_values_day = {
        inherit = posteffect_values_base
        fog_color = { 0.5 0.5 0.6 }
    }
    
    posteffect_values_night = {
        inherit = posteffect_values_base
        brightness = 0.7
        fog_color = { 0.2 0.2 0.3 }
    }
}
```

Inherited values are copied first, then explicitly defined values override inherited ones. This enables shared base parameters with per-variant adjustments.

> [!CRITICAL] No circular inheritance validation exists. Circular references (A inherits from B, B inherits from A) may crash the game or cause infinite loops. Always ensure inheritance forms a directed acyclic graph.

## Position Volumes

Position volumes define 3D regions where posteffects apply:

```hoi4
posteffect_volume = {
    posteffect = "desert_effect"
    
    position = {
        position = { 2000 50 1500 }
        size = { 500 200 500 }
        fade_distance = 100
    }
}
```

Position attributes:

- `position`: XYZ coordinates in map coordinate space (not screen/world space)
- `size`: Box dimensions from center point, not corner-to-corner
- `fade_distance`: Linear blend zone width at volume boundaries

The z-axis in position vector affects height positioning. Volumes operate in 3D space enabling stratified effects - high-altitude fog layers above low-altitude clear zones, for example.

The `size` dimensions define the box extending from the center point. A size of `{ 500 200 500 }` creates a box 1000 units wide (500 in each direction from center), 400 units tall, and 1000 units deep.

### Fade Distance

`fade_distance` creates linear blend zones at volume boundaries. At the boundary, the posteffect fades from full strength to zero over the specified distance. A `fade_distance = 100` creates a 100-unit transition zone.

Setting `fade_distance = 0` creates hard transitions with no blending. The posteffect snaps on/off at the exact boundary. Negative fade_distance behavior is undefined - avoid negative values.

## Height Volumes

Height volumes apply posteffects based on vertical position:

```hoi4
posteffect_volume = {
    posteffect = "altitude_haze"
    
    height = {
        min_height = 0
        max_height = 500
        fade_distance = 50
    }
}
```

Height volumes apply independently of position volumes. An entity can be affected by both a position volume and a height volume simultaneously.

Height attributes:

- `min_height`: Lower boundary for effect
- `max_height`: Upper boundary for effect
- `fade_distance`: Blend zone at both boundaries

Height volumes enable altitude-based effects - fog in valleys, clear air on mountains - without requiring separate position volumes for every elevation change.

## Volume Overlap

Multiple position volumes can overlap the same map coordinates. When multiple volumes overlap, the behavior is undefined - the system may blend effects, prioritize one volume, or produce unexpected results. Height volumes apply independently of position volumes, creating another dimension of potential overlap.

Design patterns for handling overlap:

1. Use fade distances to create smooth transitions between adjacent volumes rather than overlapping volumes
2. Test overlap behavior in-game before deploying complex overlapping configurations
3. Document intentional overlaps with expected behavior for troubleshooting

## Console Commands

Debug commands for posteffect development:

**PostEffectVolumes.Enabled**: Toggles posteffect volume rendering. Requires developer mode (`-developer` launch flag).

**PostEffectVolumes.Draw**: Visualizes volume boundaries and blend zones. Requires developer mode.

**reload posteffectvolumes**: Reloads posteffect definitions from files. Works in standard console without developer mode. Preserves game state but updates visual effects immediately, enabling iterative tuning without restart.

The reload command is essential for workflow - adjust values, reload, observe changes, repeat. This is significantly faster than restarting the game for each adjustment.

## Coordinate System

Posteffect coordinates use map coordinate space matching the coordinate system used for province positions and state locations. This is not screen space (pixels) or world space (3D engine units) but the game's internal map coordinate system.

To determine coordinates for positioning:

1. Enable console (`~` key)
2. Hover over desired map location
3. Note coordinates displayed in debug information
4. Use those coordinates in position volume definitions

The coordinate system origin and scale match province definition coordinates, enabling precise positioning of effects relative to map features.

## Related Systems

Posteffects integrate with map rendering for visual atmosphere and graphics settings for effect quality levels. Seasonal weather systems can trigger winter posteffect variants. See map coordinate systems for position volume placement.
