---
domain: database
concept: technologies_gui
version: 1.14+
requires: [technologies_core]
relates: [interface, sprites]
---

# Technology GUI System

Technology display in the research tree is controlled by GUI files in `interface/` and positioning within technology definitions.

## GUI Files

Two separate GUI systems exist:

- **Standard techs:** `interface/countrytechtreeview.gui`
- **Doctrine techs:** `interface/countrydoctrinetreeview.gui`

Graphics definitions are in `interface/countrytechtreeview.gfx`.

## Gridbox and Positioning

### Gridbox Requirements

> [!CRITICAL] Technologies without a `path` AND without a separate `gridboxType` definition never appear in the GUI. Even if a tech has coordinates in its `folder` attribute, it needs either a `path` parent or explicit gridbox assignment to display.

A technology becomes visible when it has:

1. At least one `path` parent (which assigns it to a gridbox), OR
2. A separate `gridboxType` defined in the GUI file

### Secondary Paths

When a technology has multiple paths to different parents, secondary paths need special handling:

```hoi4
path = {
    leads_to_tech = primary_parent
}

path = {
    leads_to_tech = secondary_parent
    ignore_for_layout = yes
}
```

Without `ignore_for_layout = yes` on secondary paths, the game generates a "Found multiple potential grid boxes" error.

## Folder Positioning

```hoi4
folder = {
    name = infantry_folder
    position = { x = 2 y = 4 }
}
```

The `folder` attribute assigns the technology to a specific GUI folder and position.

### Coordinate Systems

Two coordinate formats exist, defined per-folder in the GUI file:

**format="LEFT"** (horizontal layout):

- x = up-to-down position
- y = left-to-right position

**format="UP"** (vertical layout):

- x = left-to-right position  
- y = up-to-down position

The coordinate offset is per-folder, NOT consistent like national focus trees. Each folder can use its own origin point.

### Start Year Display

The `start_year` attribute in a technology definition does NOT affect which GUI folder displays the tech. Folder assignment is purely based on the `folder = { name = ... }` attribute.

Start year only affects ahead-of-time research penalties, not GUI organization.

## Visibility System

Technologies are hidden by default. Visibility requires both tech configuration and GUI code.

### Making Technologies Visible

To make a tech visible, you must:

1. Define the technology in `common/technologies/*.txt`
2. Add a `folder` attribute with position coordinates
3. Ensure the folder exists in the GUI file
4. Add the tech to a gridbox (via `path` or explicit GUI definition)

The AI can research hidden technologies - visibility only affects the GUI, not research eligibility.

### allow vs Visibility

```hoi4
allow = {
    always = no
}
```

Setting `allow = { always = no }` blocks AI research but keeps the tech visible in the GUI (displayed as locked). To completely hide a tech, use `allow_branch` or don't define GUI positioning.

## Doctrine System

Doctrine technologies require special handling:

```hoi4
doctrine = yes
```

When `doctrine = yes` is set:

1. The technology uses `interface/countrydoctrinetreeview.gui`
2. The folder must be marked as a doctrine folder in the GUI file
3. Display layout differs from standard tech trees

Both the tech definition AND the GUI folder configuration must specify doctrine status.

## Technology Icons

### Standard Icons

Technology icons use the sprite pattern `GFX_<tech_id>_medium`:

```text
GFX_infantry_weapons_medium
GFX_basic_light_tank_medium
```

### Country-Specific Icons

Country-specific tech icons override the generic versions:

```text
GFX_GER_infantry_weapons_medium  # Germany's infantry weapons icon
GFX_SOV_tank_tech_medium         # Soviet tank tech icon
```

The game checks for country-specific icons first, then falls back to generic icons.

### Equipment Icon Fallback

If equipment unlocked by a technology doesn't have its own icon defined (`GFX_<equipment>_medium`), the equipment automatically copies the technology's icon.

This allows technologies that unlock single equipment items to define one icon that serves both purposes.

## Sub-Technology Display

```hoi4
tech_id = {
    sub_technologies = {
        sub_tech_1
        sub_tech_2
        sub_tech_3
    }
}
```

Sub-technologies automatically display stacked under their parent in the GUI. They don't require separate `folder` definitions - the parent's folder and position apply to all sub-techs.

The default maximum is 3 sub-techs displayed per parent, though this can be overridden with `sub_tech_index` for non-sequential arrangement.

## Folder Organization

Folders organize technologies by theme or type:

- Infantry technologies typically use `infantry_folder`
- Armor technologies use `armour_folder`  
- Naval technologies use `naval_folder`
- Air technologies use `air_folder`
- Doctrine folders are separate: `land_doctrine`, `air_doctrine`, `naval_doctrine`

Folder names must match definitions in the GUI file's `technology_folders` section.

## Common Display Issues

### Tech Not Appearing

If a technology doesn't appear in the research GUI:

1. **Check for `path` or gridbox:** Tech needs at least one parent path or explicit gridbox definition
2. **Verify folder name:** Folder must exist in GUI file
3. **Check coordinates:** Position values must be valid for the folder's coordinate system
4. **Confirm `allow_branch`:** A parent tech's `allow_branch` can hide connected techs

### Multiple Grid Boxes Error

```text
Found multiple potential grid boxes for technology <tech_id>
```

This occurs when a technology has multiple `path` blocks pointing to parents in different gridboxes, without `ignore_for_layout = yes` on secondary paths.

**Fix:** Add `ignore_for_layout = yes` to all but one `path` block:

```hoi4
path = {
    leads_to_tech = primary_parent
}

path = {
    leads_to_tech = secondary_parent
    ignore_for_layout = yes
}
```

### Tech Hidden Despite Definition

If a tech is defined with proper positioning but still hidden:

1. **Check `allow_branch` in parent techs:** This hides all connected techs
2. **Verify GUI folder exists:** Referencing non-existent folders hides techs
3. **Check for missing `path`:** Without a path, techs need explicit gridbox definitions

## Doctrine GUI Differences

Doctrine trees use a different layout system:

- **File:** `interface/countrydoctrinetreeview.gui`
- **Layout:** Usually horizontal/linear instead of grid-based
- **Mutual exclusivity:** More common in doctrine trees (XOR relationships)
- **Folder marking:** Both tech and GUI must specify doctrine status

When creating doctrine technologies:

1. Set `doctrine = yes` in tech definition
2. Mark folder as doctrine folder in GUI file
3. Use appropriate doctrine folder names (`land_doctrine`, etc.)
4. Ensure `countrydoctrinetreeview.gui` exists and is configured

## Related Systems

For core technology mechanics, pathing, cost, and enabling objects, see [Technologies Core](/database/technologies_core.md).

For sprite definitions, see the interface graphics documentation.

For gridbox and container configuration, see the GUI system documentation.
