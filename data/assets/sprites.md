---
domain: assets
concept: sprites
version: 1.14+
requires: [interface_elements]
relates: [fonts, localisation]
---

# Sprite System

Sprites are visual assets defined in `interface/*.gfx` files that provide textures, animations, and special rendering behaviors for GUI elements. The game supports multiple sprite types optimized for different use cases, from static images to animated progress bars.

## Sprite Types

### spriteType

The standard sprite type for static or multi-frame images. Defined with required `name` and `texturefile` attributes.

```hoi4
spriteType = {
    name = "GFX_example_sprite"
    texturefile = "gfx/interface/example.dds"
    noOfFrames = 2
    effectFile = "gfx/FX/buttonstate.lua"
}
```

The `name` attribute follows the `GFX_<identifier>` format convention. Texture files use paths relative to the game root directory and typically use `.dds` format with a practical limit of approximately 16MB per file.

Multiple effect files can be specified. The `effectFile` attribute accepts pixel shader definitions from `gfx/FX/*.lua` that modify sprite rendering.

#### Sprite Overrides

The game supports tag-specific and culture-specific sprite overrides using naming conventions. Tag overrides use `GFX_<TAG>_<identifier>` format and culture overrides use `GFX_<culture>_<identifier>` format. Priority resolution follows: tag > culture > base sprite name.

#### Transparency and Loading

Three attributes control sprite transparency and loading behavior:

**alwaystransparent**: When true, disables tooltip display and click detection for the sprite region. The sprite remains visible but non-interactive.

**legacy_lazy_load**: When true, defers sprite loading until first use rather than loading at game start. Required for multi-frame icons used in localization text (see Localization Text Icons section).

**transparencecheck**: When true, uses alpha channel data to determine clickable regions. Fully transparent pixels become non-clickable even if within the sprite's bounding box.

### Animation System

spriteType supports texture animation through specialized attributes. Animations can scroll, rotate, or pulse textures over time.

```hoi4
spriteType = {
    name = "GFX_animated_texture"
    texturefile = "gfx/interface/base.dds"
    animationtexturefile = "gfx/interface/overlay.dds"
    animationrotation = -90.0
    animationlooping = yes
    animationtime = 2.0
    animationdelay = 0.5
    animationblendmode = "add"
    animationtype = "scrolling"
}
```

Animation attributes define texture overlay behavior:

- `animationtexturefile`: Overlay texture that animates over base texture
- `animationmaskfile`: Optional mask defining where animation appears
- `animationrotation`: Rotation angle in degrees, defaults to -90 (clockwise) if unspecified
- `animationtime`: Duration in seconds for one complete animation cycle
- `animationdelay`: Seconds before animation begins after sprite becomes visible
- `animationlooping`: Whether animation repeats after completing
- `animationtype`: Movement pattern - `scrolling`, `rotating`, or `pulsing`
- `animationblendmode`: How overlay combines with base - `add`, `multiply`, or `overlay`

Animations play continuously once started. The animation continues even if the sprite is not visible unless controlled by GUI visibility states.

Additional animation attributes for fine control:

- `animationrotationoffset`: Coordinate offset for rotation center point
- `animationtexturescale`: Scale factors for animation texture dimensions
- `animationframes`: Integer array defining frame sequence for multi-frame animations

### textSpriteType

Functionally identical to spriteType. This type exists for semantic clarity when defining sprites used specifically for text rendering, but accepts the same attributes and behaves identically to spriteType.

### frameAnimatedSpriteType

Specialized sprite type for frame-based animation from sprite sheets. Requires `noOfFrames` attribute.

```hoi4
frameAnimatedSpriteType = {
    name = "GFX_frame_animation"
    texturefile = "gfx/interface/spritesheet.dds"
    noOfFrames = 24
    animation_rate_fps = 12
    looping = yes
    play_on_show = yes
    pause_on_loop = 0.5
}
```

Frame animation attributes:

- `noOfFrames`: Total number of frames in sprite sheet (required)
- `animation_rate_fps`: Frames per second playback speed
- `looping`: Whether animation repeats after reaching final frame
- `play_on_show`: If true, animation starts automatically when sprite becomes visible
- `pause_on_loop`: Seconds to wait at end of loop before restarting

The sprite sheet texture must contain frames arranged horizontally. Each frame occupies `texture_width / noOfFrames` pixels.

### progressbartype

Specialized sprite for progress indicators with foreground and background textures.

```hoi4
progressbartype = {
    name = "GFX_progress_bar"
    textureFile1 = "gfx/interface/bar_fill.dds"
    textureFile2 = "gfx/interface/bar_background.dds"
    size = { x = 200 y = 20 }
    color = { 0.5 0.5 0.5 }
    colortwo = { 0.0 1.0 0.0 }
    horizontal = yes
    steps = 100
}
```

Progress bar attributes:

- `textureFile1`: Foreground texture showing progress fill
- `textureFile2`: Background texture showing unfilled portion
- `size`: Bar dimensions in pixels (required)
- `color`: RGBA color for unprogressed portion using decimal format (0.0-1.0)
- `colortwo`: RGBA color for progressed portion
- `horizontal`: Fill direction - true for left-to-right, false for bottom-to-top (defaults to true)
- `steps`: Precision of fill calculation, defaults to 100 if unspecified

The bar fills according to a value provided by the GUI element using it. Higher `steps` values provide smoother fill granularity at negligible performance cost.

### corneredTileSpriteType

Tiling texture that expands to fill the size of GUI elements using it. Useful for backgrounds and borders that scale dynamically.

```hoi4
corneredTileSpriteType = {
    name = "GFX_tiled_background"
    texturefile = "gfx/interface/tile_pattern.dds"
    size = { x = 64 y = 64 }
    borderSize = { x = 8 y = 8 }
    tilingCenter = yes
}
```

Tiling attributes:

- `size`: Dimensions of individual tile in pixels
- `borderSize`: Border region that doesn't tile (corners remain fixed)
- `tilingCenter`: Origin point for tiling - true uses center, false uses top-left
- `noOfFrames`: Optional frame count for animated tiling
- `looping`: Whether frame animation loops
- `animation_rate_spf`: Seconds per frame for animation

Tiles repeat to fill the GUI element's dimensions. The `borderSize` creates fixed corner regions that don't stretch, while the center region tiles. The `tilingCenter` attribute affects how partial tiles are cropped at edges.

### maskedShieldType

Specialized sprite for country flag shields using separate background and mask textures.

```hoi4
maskedShieldType = {
    name = "GFX_country_shield"
    textureFile1 = "gfx/interface/shield_background.dds"
    textureFile2 = "gfx/interface/shield_mask.dds"
}
```

The shield system composites the country flag (determined at runtime) with the background texture using the mask to define shield shape. The mask's alpha channel determines flag visibility - fully opaque mask regions show flag colors, transparent regions show background.

## Map Text

Animated text overlays on the strategic map use a specialized spriteType variant called `animatedmaptext`. These sprites cannot use custom names - only predefined identifiers work.

```hoi4
animatedmaptext = {
    name = "GFX_map_victory_points"
    speed = 2.0
    textblock = {
        text = "example_text"
        color = { 1.0 1.0 1.0 }
        font = "Main_14_black"
        position = { x = 100 y = 200 }
        size = { x = 200 y = 50 }
        format = center
        cull_distance = 500.0f
    }
}
```

Map text attributes:

- `speed`: Fade transition time in seconds when text appears/disappears
- `text`: Localization key or literal string to display
- `color`: RGB color in decimal format
- `font`: Font identifier from font definitions
- `position`: Map coordinate placement
- `size`: Text box dimensions
- `format`: Text alignment within box
- `cull_distance`: Distance threshold for visibility culling (append 'f' suffix)

Map text appears at fixed map coordinates and fades in/out based on zoom level and `cull_distance`. The text remains readable at various zoom levels by scaling automatically.

## Related Defines

Sprite system behavior is controlled by engine constants in defines files. Relevant defines appear in graphics-related sections.
