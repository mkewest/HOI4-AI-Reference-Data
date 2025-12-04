---
domain: database
concept: ideas_core
version: 1.14+
requires: [localisation_system]
relates: [country_leaders, characters, modifiers_list, ideas_categories]
---

# National Ideas System

National ideas are modifiers that countries can have, ranging from national spirits to political advisors. They're defined in `common/ideas/*.txt` with category definitions in `common/idea_tags/*.txt`.

## File Structure

Ideas are defined within an `ideas = {...}` root block. Each idea belongs to one of five categories:

- **country:** General national spirits
- **hidden_ideas:** Ideas that don't appear in politics view
- **law_category:** Political laws like economy and conscription
- **designer_category:** Military designers and advisors
- **custom:** User-defined categories

Example structure:

```hoi4
ideas = {
    country = {
        idea_id = {
            picture = GFX_idea_generic_trait
            modifier = {
                stability_factor = 0.05
            }
        }
    }
}
```

## Picture System

Ideas use sprites with the `GFX_idea_` prefix. The `picture` attribute specifies which sprite to use, but the game automatically prepends `GFX_idea_` to whatever value you provide.

> [!CRITICAL] The GFX_idea_ prefix is ALWAYS inserted automatically. If you write `picture = GFX_XYZ`, the game looks for `GFX_idea_GFX_XYZ`, which won't exist. Write `picture = XYZ` to reference `GFX_idea_XYZ`.

If the texturefile path is incorrect, the idea becomes invisible in the politics view, but its modifiers still apply normally.

### Graphical Culture Support

Ideas support graphical culture variants using the suffix pattern `GFX_idea_<n>_<culture_2d>`. The game checks for culture-specific sprites after checking the base name.

The default sprite for ideas without a specified picture is `GFX_idea_<n>` where `<n>` is a frame number.

## Modifiers

Ideas can apply five distinct types of modifiers, each defined as separate attributes at the same level:

### Standard Modifiers

```hoi4
modifier = {
    stability_factor = 0.05
    war_support_factor = 0.1
}
```

Standard modifiers use any country-scoped modifier. Variables are NOT supported within modifier blocks - attempting to use them does nothing.

> [!CRITICAL] The `modifier`, `research_bonus`, `equipment_bonus`, and `rule` attributes are separate and must be defined at the same level. Defining `research_bonus = {...}` inside a `modifier = {...}` block does nothing.

### Research Bonuses

```hoi4
research_bonus = {
    infantry_weapons = 0.15
    electronics = 0.10
}
```

Research bonuses apply to technology categories defined in `common/technology_tags/*.txt`.

### Equipment Bonuses

```hoi4
equipment_bonus = {
    infantry_equipment = {
        soft_attack = 0.05
        build_cost_ic = -0.10
        instant = yes
    }
}
```

Equipment bonuses modify equipment archetypes. By default, bonuses only apply after researching a new technology that unlocks equipment of that archetype. The `instant = yes` attribute makes bonuses apply immediately without requiring research.

### Targeted Modifiers

```hoi4
targeted_modifier = {
    tag = GER
    attack_bonus_against = 0.1
    defense_bonus_against = 0.1
}
```

Targeted modifiers apply TO the country that has the idea AGAINST the specified tag. The country with the idea receives the bonus when fighting against the target.

### Rules

```hoi4
rule = {
    can_create_factions = yes
    can_force_government = no
}
```

Rule modifiers only show in the tooltip if the value differs from the default. Setting a rule to its default value results in no tooltip entry.

## Effect Blocks

Ideas can execute effects when added or removed:

### on_add

```hoi4
on_add = {
    add_political_power = 50
    add_stability = 0.05
}
```

The `on_add` effect executes when the idea is added via effects like `add_ideas`. However, it does NOT execute when ideas are added through history files or bookmark effect blocks.

> [!CRITICAL] When adding ideas in history files or bookmarks, you must manually replicate any `on_add` effects in the same effect block. The `on_add` block will not run automatically in these contexts.

### on_remove

```hoi4
on_remove = {
    add_political_power = -50
}
```

The `on_remove` effect executes when the idea is removed via `remove_ideas` or when it auto-cancels via its `cancel` trigger. Unlike `on_add`, this DOES trigger for automatic cancellation.

## Triggers

Ideas support several trigger types with different evaluation frequencies:

### allowed

Checked ONCE at game start or when loading a save. Determines if the idea can be selected at all. The `add_ideas` effect bypasses this check entirely, allowing you to add ideas that wouldn't normally be allowed.

### allowed_to_remove

Checked continuously. Determines if the player can manually remove the idea from the politics screen. Doesn't prevent removal via effects.

### visible

Checked per-frame. Controls whether the idea appears in the politics view. The idea's effects continue to apply even when invisible.

### available

Checked per-frame. When false, the idea appears grayed out and cannot be selected. The tooltip shows why it's unavailable.

### cancel

```hoi4
cancel = {
    has_war = yes
}
```

Checked continuously. When the trigger becomes true, the idea is automatically removed and fires its `on_remove` effect block.

### allowed_civil_war

```hoi4
allowed_civil_war = {
    always = yes
}
```

Determines which side keeps the idea when a civil war starts. The default is `always = no`, meaning national spirits disappear for both sides unless explicitly specified.

> [!CRITICAL] The `allowed_civil_war` trigger is checked per side independently during civil war initialization. An idea can transfer to one side, both sides, or neither side depending on how the trigger evaluates for each faction.

### do_effect

```hoi4
do_effect = {
    if = {
        limit = { has_stability < 0.5 }
        add_stability = 0.01
    }
}
```

Checked continuously. Effects execute only when the idea's modifiers are active, allowing for conditional passive effects based on the `limit` trigger.

## Selectable Ideas

Ideas can be configured as selectable options in the politics view:

### Cost System

```hoi4
cost = 150
removal_cost = 50
```

Costs are in political power. The default cost is 150 PP. A `removal_cost` of -1 makes the idea impossible to remove manually (must use effects or cancel trigger).

### Level System

```hoi4
idea_id = {
    level = 3
    cost = 150
    
    modifier = {
        stability_factor = 0.05
    }
}
```

Ideas can have levels, representing upgrades or different tiers. When jumping levels (e.g., level 1 → level 3), costs accumulate: you pay cost(2) + cost(3), not just cost(3).

### Ledger Assignment

```hoi4
ledger = army
```

Controls which ledger tab displays the idea's cost in the politics view. Valid values: `army`, `air`, `navy`, `military`, `civilian`, `all`, `hidden`.

### Traits Reference

```hoi4
traits = { <trait_id> }
```

References traits defined in `common/country_leader/*.txt`, allowing ideas to share trait definitions with country leaders.

## Localisation

Localisation files are located in `localisation/english/*_l_english.yml` with UTF-8-BOM encoding.

### Standard Keys

- `<id>`: The name displayed in the politics view
- `<id>_desc`: The description displayed in tooltips

### Override Syntax

```hoi4
name = custom_loc_key
```

The `name` attribute within an idea definition overrides the default localisation key, allowing multiple ideas to share the same displayed name.

### Fallback Behavior

For non-spirit ideas without explicit localisation, the game uses the country's name-list for random name generation. For national spirits without localisation, the idea ID itself displays as the name.

## Idea Modification

There is NO direct way to modify idea values after they're added. Variables do NOT work within modifier blocks.

To change idea values, you must use `swap_ideas`:

```hoi4
swap_ideas = {
    remove_idea = old_idea_id
    add_idea = new_idea_id
}
```

Both ideas can use the same localisation name (via the `name` attribute) to make the swap appear as a modification to the player.

### Dynamic Modifiers Alternative

For truly dynamic values, use dynamic modifiers instead of ideas. However, dynamic modifiers only accept standard modifiers - they cannot provide `research_bonus` or `equipment_bonus` functionality.

## Adding and Removing Ideas

### Effects

```hoi4
add_ideas = idea_id
remove_ideas = idea_id

swap_ideas = {
    remove_idea = old_id
    add_idea = new_id
}

add_timed_idea = {
    idea = idea_id
    days = 365
}
```

The `add_ideas` effect bypasses the `allowed` trigger check, enabling you to add ideas that wouldn't normally be selectable.

Timed ideas automatically remove themselves after the specified number of days, triggering the `on_remove` effect.

## Related Systems

Ideas integrate with several other systems:

- **Country Leaders:** Can reference leader traits via the `traits` attribute
- **Characters:** Can be assigned to idea slots (see ideas_categories.md)
- **Static Modifiers:** Ideas are a form of dynamic static modifier
- **Political Power:** Required for selecting and removing ideas

For category definitions, GUI configuration, and slot management, see [Ideas Categories](/database/ideas_categories.md).
