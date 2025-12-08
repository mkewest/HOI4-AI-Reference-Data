---
domain: assets
concept: interface
version: 1.14+
requires: [sprites]
relates: [scripted_gui, localisation]
---

# Interface System

The interface system defines GUI layouts in `interface/*.gui` files wrapped in a root `guiTypes = { ... }` block. Elements render in definition order - later definitions appear on top of earlier ones, creating a file-based z-ordering system independent of hierarchy.

## Container System

### containerWindowType

Containers establish rendering contexts for GUI elements. Two categories exist: independent containers that require explicit activation, and nested containers that appear automatically with their parent.

```hoi4
containerWindowType = {
    name = "example_window"
    size = { width = 400 height = 300 }
    position = { x = 100 y = 50 }
    orientation = center
    origo = center
}
```

#### Container Visibility

Independent containers (defined at root level in guiTypes) do not show by default. They require function binding through scripted GUI, tech folder definitions, or music station assignments to become visible. Without such binding, the container never renders regardless of element content.

Nested containers (defined inside other containers) appear automatically when their parent container becomes visible unless overridden by scripted GUI visibility triggers. This hierarchical visibility propagates through the entire container tree.

> [!CRITICAL] Only independent containers can be assigned to scripted GUI via `window_name`. Nested containers cannot have scripted GUI directly assigned - the scripted GUI affects all elements in the container tree including nested ones through the parent assignment.

#### Container Names

Independent containers must have globally unique names. Nested containers may have name overlaps if they exist in different independent containers, though this is discouraged for parent_window_name disambiguation in scripted GUI.

Empty containers can serve as positioning anchors. When used with `parent_window_name` in scripted GUI, they enable precise positioning within base game UI without modifying existing elements.

### Container Attributes

**size**: Dimensions using pixels or percentages. Format: `{ width = <val> height = <val> }` where values accept `px` or `%` units. For independent containers, percentages are relative to screen size. For nested containers, percentages are relative to parent container. Scrollbars require pixel dimensions in scroll direction.

> [!CRITICAL] Scrollbar functionality requires `size` to use pixels (not percentages) for directions where scrolling is enabled. Mixed units work - horizontal scrollbar with `width = 400` and `height = 50%` is valid.

**position**: Pixel-based positioning. Format: `{ x = <val> y = <val> }`. Origin point determined by `origo` attribute.

**orientation**: Anchor point for positioning calculations. Valid values: `center`, `upper_left`, `upper_right`, `lower_left`, `lower_right`, `center_up`, `center_down`. Elements inherit parent container orientation unless explicitly overridden.

**origo**: Origin point for the container itself. Uses same values as orientation. Determines which point of the container aligns to the position coordinate.

**moveable**: Boolean enabling drag-to-move functionality. Only works for independent containers.

**fullScreen**: Boolean forcing container to fill entire screen regardless of size attribute.

### Background and Clipping

**background**: Defines container background using sprite reference. Format:

```hoi4
background = {
    name = "background_sprite"
    spriteType = "GFX_background"
    quadTextureSprite = "GFX_tiled_background"
}
```

The background is required for scrollbar functionality and boundary enforcement. Without a background, clipping boundaries are ignored even when `clipping = yes`.

**clipping**: Boolean controlling element cropping at container edges. Defaults to true (not false). When true, elements extending beyond container bounds are cropped. Must be true (or unset) for scrollbars to function. Setting to false allows elements to render outside container bounds.

### Container Animation

Containers support show/hide animations with customizable easing:

```hoi4
containerWindowType = {
    name = "animated_window"
    show_position = { x = 0 y = 0 }
    hide_position = { x = -500 y = 0 }
    show_animation_type = "decelerated"
    hide_animation_type = "accelerated"
    animation_time = 300
    show_sound = "ui_menu_open"
}
```

Animation attributes:

- `show_position`: Target position when container becomes visible
- `hide_position`: Target position when container hides
- `show_animation_type`: Easing function for appearance - `decelerated` or `linear`
- `hide_animation_type`: Easing function for disappearance - `accelerated` or `linear`
- `animation_type`: Alternative single attribute applying same easing to both directions
- `animation_time`: Duration in milliseconds
- `show_sound`: Sound effect identifier played on show

## Scrollbar System

### extendedScrollbarType

Scrollbars enable scrolling for containers with content exceeding visible bounds. Definition location determines behavior:

**Inside container**: Scrollbar automatically binds to that container only. Cannot be reused by other containers.

**Outside containers (independent)**: Scrollbar is not assigned by default but can be reused across multiple containers through explicit assignment.

```hoi4
containerWindowType = {
    name = "scrolling_window"
    size = { width = 400 height = 300 }
    background = { name = "bg" spriteType = "GFX_background" }
    
    extendedScrollbarType = {
        name = "scrollbar"
        slider = "GFX_scroll_dragger"
        track = "GFX_scroll_track"
        upButton = "GFX_scroll_up"
        downButton = "GFX_scroll_down"
        size = { width = 16 height = 300 }
        position = { x = 384 y = 0 }
        priority = 100
        borderSize = { x = 16 y = 16 }
        maxValue = 1000
        minValue = 0
        stepSize = 10
        startValue = 0
        horizontal = no
        lockable = yes
        autohide_scrollbar = yes
    }
}
```

> [!CRITICAL] Scrollbars have three hard requirements: (1) container must have `background` defined, (2) `clipping` must be true or unset (not false), (3) container `size` must use pixels in scroll direction. Violating any requirement causes scrollbar to fail silently.

Scrollbar attributes:

- `maxValue`: Maximum scroll position (content height/width minus visible area)
- `stepSize`: Scroll distance per button click or wheel notch
- `horizontal`: Scroll direction - false for vertical (default), true for horizontal
- `autohide_scrollbar`: If true (default), scrollbar hides when unnecessary
- `lockable`: Enables/disables scrolling when content fits visible area

The scrollbar uses container size to determine visible bounds, not the total size of internal elements. This is a common source of confusion - adding elements doesn't automatically update scroll range; `maxValue` must be set explicitly.

### Drag Scrolling

Containers support drag-to-scroll functionality through `drag_scroll` attribute:

```hoi4
containerWindowType = {
    name = "draggable_scroll"
    drag_scroll = { left }
}
```

> [!CRITICAL] Drag scrolling only works if: (1) a scrollbar exists for the same axis, (2) the container has both `drag_scroll` attribute AND an active scrollbar. Only the `left` mouse button actually functions despite syntax allowing `middle` and `right`.

## GUI Elements

### Element Types

**buttonType**: Combines image and text functionality for interactive buttons. Most flexible element type.

**iconType**: Static image display only. Has significant functional overlap with buttonType - use iconType when no interactivity needed, buttonType when click handling required.

**instantTextBoxType**: Text display element. Some instances generate text internally (e.g., regiment_count displays) and ignore the `text` attribute. Internally-generated text cannot be edited unless exposed through localization variables.

**smoothListboxType / listboxType**: List containers that are "internally linked" with another container defining entry appearance. Entries cannot be defined directly in the listbox element itself - a separate container template is required.

**checkboxType**: Boolean toggle element. Relies on internal code for state management.

**OverlappingElementsBoxType**: Container for overlapping element layouts. Internal code manages positioning.

**editBoxType**: Text input field. Internal code handles input and validation.

**shieldtype**: Flag display element requiring internal code. Modern flag displays use different elements.

### Scripted GUI Compatibility

Only three element types work with scripted GUI effects and triggers:

1. **iconType**: Can have visibility triggers, click effects, and dynamic properties
2. **instantTextBoxType**: Can have visibility triggers and dynamic text
3. **buttonType**: Can have click effects, enabled triggers, and dynamic properties

Elements relying on internal code (smoothListboxType, listboxType, checkboxType, OverlappingElementsBoxType, editBoxType, shieldtype) can be added to GUI files but won't populate with data or respond to scripted GUI interactions. They render but remain non-functional without engine support.

### Unused Attributes

Some element attributes exist in legacy code but have no effect:

**In buttonType/checkboxType:**

- `tooltip`, `tooltipText`, `delayedTooltipText`: Never used. Use `pdx_tooltip` in localization instead.

**In smoothListboxType/listboxType:**

- `textureFile`: Never used
- `background`: Never used

### Legacy Element Types

Older interface files use deprecated type names that map to modern equivalents:

- `guiButtonType` → `buttonType`
- `textBoxType` → `instantTextBoxType`
- `eu3dialogtype` → `windowType`

The old `shieldtype` element only appears within `eu3dialogtype` containers. Modern flag displays use different elements entirely.

## Element Rendering

Elements render in file definition order creating a z-ordering system. This ordering is file-based, not hierarchy-based. An element defined later in the file appears on top regardless of nesting level.

Elements inherit container orientation unless the element specifies its own `orientation` attribute. This inheritance creates consistent positioning across nested containers but can be overridden per-element when needed.

## Scripted GUI Integration (contexts, bindings, dynamics)

Scripted GUIs attach GUI containers to game contexts:

- **context_type**: `player_context`, `selected_country_context`, `selected_state_context`, `diplomacy_target_context`, `decision_category`, `diplomatic_action`, `national_focus_context`, `country_mapicon`, `state_mapicon`.
- **window_name**: Name of the container defined in `.gui`.
- **parent binding**: `parent_window_token` (common tokens: top_bar, decision_tab, tech folders, diplomacy_tab, etc.), or `parent_window_window` (container name), or `parent_scripted_gui`.
- **visibility / map_mode**: `visible = { }` for show/hide; `map_mode` for map-icon contexts; `mapicon_targets` (targeting like decisions) for mapicon guis.

### Interactive wiring
- **effects**: Bind button clicks (supports modifiers like `_alt_right_click`).
- **triggers**: Enable/visible checks per element (`button_name_click_enabled`, `icon_name_visible`).
- **properties**: Dynamically set textures/frames/positions (`image`, `frame`, `x`, `y`).
- **dynamic_lists**: Populate entries from arrays; optional `change_scope`, `entry_container`, `ai_weights`.
- **dirty**: Optional variable name to throttle updates—GUI refreshes only when the variable changes.

### AI fields
- `ai_enabled`: One-time gate (use tag/original_tag checks here).
- `ai_test_interval` / `ai_test_variance`: Hours between AI evaluations.
- `ai_check`: Per-tick gate for AI using the GUI.
- `ai_test_scopes`: Target sets to evaluate (self/enemy/ally/neighbouring countries/states variants).
- `ai_check_scope`: Per-target gate.
- `ai_weights`: Per-action weights (`ai_will_do` style) with `ignore_lower_weights`, `weight`, and `ai_max_weight_taken_per_test` cap.

## Related Systems

Containers and elements integrate with scripted GUI for dynamic behavior, localization for text content, and sprite definitions for visual assets. See [Scripted GUI](/assets/scripted_gui.md) for event handling and dynamic element control.
