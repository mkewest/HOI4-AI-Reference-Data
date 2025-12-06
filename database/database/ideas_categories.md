---
domain: database
concept: ideas_categories
version: 1.14+
requires: [ideas_core]
relates: [interface, sprites, characters]
---

# Idea Categories System

Idea categories define slots in the politics view where ideas can be equipped. They're defined in `common/idea_tags/*.txt` within an `idea_categories = {...}` root block.

## Category Definition Structure

```hoi4
idea_categories = {
    category_id = {
        slot = slot_name
        cost = 150
        removal_cost = -1
        ledger = army
        hidden = no
        politics_tab = yes
        
        slot_ledgers = {
            character_slot_1 = navy
            character_slot_2 = air
        }
    }
}
```

## Core Attributes

### slot

The `slot` attribute defines which idea category slot this uses. Ideas in the same slot compete for space based on the `slot_ledgers` configuration or GUI gridbox limits.

### character_slot

References a character slot name, allowing characters to occupy idea slots. Characters must be defined before ideas in the load order, which creates complications with cost modifiers (see Cost Modifiers section below).

### cost

Default political power cost for ideas in this category. Individual ideas can override this with their own `cost` attribute.

### removal_cost

Default removal cost. A value of -1 makes ideas in this category non-removable by default.

### ledger

Default ledger assignment for cost display. Valid values: `army`, `air`, `navy`, `military`, `civilian`, `all`, `hidden`.

### slot_ledgers

Assigns different ledgers to specific character slots within the category:

```hoi4
slot_ledgers = {
    political_advisor = civilian
    army_chief = army
    navy_chief = navy
}
```

This allows fine-grained control over how costs appear in different ledger tabs.

### hidden

Boolean. When `yes`, the category doesn't appear in the politics view. Ideas in hidden categories still function normally.

### politics_tab

Boolean. When `no`, the category doesn't show in the politics tab interface. Default is `yes`.

## Special Flags

### designer = yes

Marks the category as containing designer ideas (tank designers, ship designers, aircraft designers). Changes UI behavior and filtering.

### law = yes

Marks the category as containing law ideas (economy laws, trade laws, conscription laws). Affects AI behavior and UI grouping.

### use_list_view = yes

Displays ideas in this category as a list instead of the default grid layout. Useful for categories with many options.

## GUI Configuration

The politics view GUI is defined in `interface/countrypoliticsview.gui`.

### Default Gridbox Limits

The standard gridbox allows 7 horizontal slots × 1 vertical slot, for a maximum of 7 visible slots per category.

> [!CRITICAL] Exceeding gridbox limits causes slots to not display. The game doesn't generate an error - ideas beyond the 7-slot limit simply become invisible. If you have more than 7 ideas in a category, you must modify the GUI file to expand the gridbox or enable scrolling.

### Category Icons

Category icons use the `GFX_idea_categories` sprite, which is a spritesheet. Frame assignment follows the order categories are defined in the idea_tags files.

The `noOfFrames` attribute in the `GFX_idea_categories` sprite definition must exactly match the number of categories you've defined. Mismatches cause incorrect icons or crashes.

### Slot Icons

Individual slot icons use the naming pattern `GFX_idea_slot_<slot>` where `<slot>` matches the `slot` attribute in the category definition.

## Cost Modifiers

Idea and character slot costs can be modified using the format `<slot>_cost_factor`:

```hoi4
modifier = {
    political_advisor_cost_factor = -0.25
    army_chief_cost_factor = 0.50
}
```

However, there's a critical load order constraint:

> [!CRITICAL] `<slot>_cost_factor` modifiers REQUIRE that ideas or characters already be defined in that slot. The game reads cost modifiers during the same load pass as idea definitions.

This creates a problem with character slots because characters are loaded AFTER ideas due to file load order.

### File Load Order

Files load in Unicode sort order: CAPITALS < underscore (_) < lowercase

This means:

- `00_IDEAS.txt` loads before `ideas.txt`
- `_ideas.txt` loads after `IDEAS.txt` but before `ideas.txt`
- Character files typically load after idea files

As a result, `character_slot_cost_factor` modifiers in ideas often fail because no characters exist in those slots when the ideas load.

**Workaround:** Place character definitions in files that load before your idea files using the Unicode sort order, or avoid using character slot cost modifiers entirely.

## Sprite Frame Indexing

The `GFX_idea_categories` sprite is a horizontal strip divided into frames. Frame indices are assigned based on the definition order of categories in `common/idea_tags/*.txt`:

1. First defined category → Frame 1
2. Second defined category → Frame 2
3. And so on...

The sprite's `noOfFrames` attribute must equal the total number of categories. If you add a new category, you must:

1. Add a new frame to the `GFX_idea_categories` texture
2. Update `noOfFrames` in the sprite definition
3. Ensure the frame order matches the definition order

Mismatches between `noOfFrames` and actual category count cause display bugs or crashes.

## Generic Political Advisors

When defining generic political advisors that should apply to all countries, place them in a file named `zzz_generic.txt`.

> [!CRITICAL] Generic advisors must be defined in files that load AFTER country-specific advisor files. Using `zzz_` as a prefix ensures Unicode sort order places it last, preventing generic advisors from being overridden by country-specific definitions.

## Category Usage Examples

### Military Advisor Category

```hoi4
idea_categories = {
    army_chief = {
        slot = army_chief
        cost = 150
        removal_cost = 10
        ledger = army
        
        designer = yes
    }
}
```

### Law Category

```hoi4
idea_categories = {
    economy = {
        slot = economy_law
        cost = 150
        removal_cost = 0
        ledger = civilian
        
        law = yes
        use_list_view = yes
    }
}
```

### Hidden Category

```hoi4
idea_categories = {
    hidden_modifiers = {
        slot = hidden_buff
        hidden = yes
        cost = 0
    }
}
```

## Related Systems

For core idea mechanics, modifiers, and effect blocks, see [Ideas Core](/database/ideas_core.md).

For character system integration with idea slots, see the characters documentation.

For GUI sprite configuration, see the interface sprite documentation.
