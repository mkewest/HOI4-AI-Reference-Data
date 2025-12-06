---
domain: database
concept: technologies_core
version: 1.14+
requires: [equipment, buildings, units]
relates: [technologies_gui, modifiers_list, equipment]
---

# Technology System

Technologies are defined in `common/technologies/*.txt` within a `technologies = {...}` root block. Categories are defined in `common/technology_tags/*.txt`.

## Basic Structure

```hoi4
technologies = {
    tech_id = {
        enable_equipments = { equipment_id }
        
        path = {
            leads_to_tech = next_tech_id
            research_cost_coeff = 1.0
        }
        
        research_cost = 1.5
        start_year = 1936
        
        folder = {
            name = infantry_folder
            position = { x = 2 y = 4 }
        }
        
        categories = { infantry_tech }
        
        ai_will_do = {
            factor = 10
        }
    }
}
```

## Visibility and Allow System

Technologies are **hidden by default** - they require GUI code to be visible, but the AI can research hidden techs.

### allow Trigger

```hoi4
allow = {
    has_government = democratic
}
```

The `allow` trigger is checked continuously. When false, it blocks tech selection in the GUI and prevents AI research, but technologies can still be researched via effects regardless of the allow status.

### allow_branch Trigger

```hoi4
allow_branch = {
    has_dlc = "Together for Victory"
}
```

The `allow_branch` trigger hides the technology AND all technologies connected to it via `path` relationships. It also blocks AI research. This is useful for DLC-gated tech trees.

## Research Cost

### Base Cost

```hoi4
research_cost = 1.5
```

Research cost is measured in units where 1.0 = 100 days of base research. A cost of 1.5 = 150 days.

### Start Year Penalty

```hoi4
start_year = 1939
```

The `start_year` attribute applies an ahead-of-time penalty of +200% per year when researching before that year. However, this does NOT affect which GUI folder displays the tech - folder display is purely based on the `folder` attribute.

The penalty applies smoothly based on days, not discrete years. Researching 6 months early incurs a 100% penalty, not the full 200%.

### Path Cost Modification

```hoi4
path = {
    leads_to_tech = next_tech_id
    research_cost_coeff = 0.5
}
```

The `research_cost_coeff` attribute in a `path` block multiplies the child technology's cost. A value of 0.5 reduces the child's cost by 50%.

## Technology Pathing

### path (OR Logic)

```hoi4
path = {
    leads_to_tech = tech_a
    research_cost_coeff = 1.0
}

path = {
    leads_to_tech = tech_b
    research_cost_coeff = 1.0
}
```

Multiple `path` blocks create OR logic: researching **any** parent satisfies the requirement. The `path` also assigns the technology to a gridbox for GUI display.

### dependencies (AND Logic)

```hoi4
dependencies = {
    tech_a = 1
    tech_b = 1
}
```

The `dependencies` block creates AND logic: **all** dependencies must be researched before this tech becomes available. Unlike `path`, dependencies do NOT assign gridbox positions.

### XOR (Mutual Exclusion)

```hoi4
# In tech_a:
xor = { tech_b }

# In tech_b:
xor = { tech_a }
```

> [!CRITICAL] XOR declarations must exist in ALL mutually exclusive technologies. Defining XOR in only one tech does nothing - both techs must declare the XOR relationship.

XOR techs block each other: researching one prevents researching the other.

## Sub-Technologies

```hoi4
tech_id = {
    sub_technologies = {
        sub_tech_1
        sub_tech_2
        sub_tech_3
    }
}
```

Sub-technologies don't need their own `folder` argument or separate gridbox. They automatically display stacked under their parent. The default maximum is 3 sub-techs per parent.

### Sub-Tech Indexing

```hoi4
sub_tech_id = {
    sub_tech_index = 1
}
```

The `sub_tech_index` attribute can override automatic indexing if you need non-sequential sub-tech arrangement.

## Enabling Objects

Technologies unlock database objects through several mechanisms:

### Equipment

```hoi4
enable_equipments = {
    equipment_archetype_1
    equipment_archetype_2
}
```

Unlocks equipment for production. Equipment already produced remains usable even if you somehow "unresearch" the tech.

### Subunits

```hoi4
enable_subunits = {
    infantry
    cavalry
}
```

Unlocks military subunits (battalions/regiments) for division templates.

### Modules

```hoi4
enable_equipment_modules = {
    ship_module_1
    tank_module_2
}
```

Unlocks equipment modules for customization systems (ships, tanks).

### Buildings

```hoi4
enable_building = {
    building = synthetic_refinery
    level = 3
}
```

Unlocks buildings up to the specified level. This unlocks UP TO that level, not ADDS levels.

> [!CRITICAL] If a building already has level 2, and a tech enables `level = 5`, the maximum becomes 5, not 7. The level is absolute, not cumulative.

Buildings can be constructed via effects BEFORE technologies unlock them - the tech requirement only blocks manual construction through the GUI.

### Tactics

```hoi4
enable_tactic = tactic_id
```

Unlocks combat tactics for the land combat system.

## Modifiers

Technologies apply country-scoped modifiers:

```hoi4
modifier = {
    stability_factor = 0.05
    army_org_factor = 0.10
}
```

### Unit-Specific Modifiers

```hoi4
modifier = {
    infantry = {
        soft_attack = 0.1
        defense = 0.15
    }
    
    armor = {
        breakthrough = 0.2
    }
}
```

Unit-specific modifiers target subunit types or unit categories. They can include terrain-specific nested modifiers:

```hoi4
modifier = {
    infantry = {
        defense = 0.1
        
        forest = {
            movement = 0.05
        }
    }
}
```

Special terrain types exist for "amphibious" (naval invasions) and "river" (river crossings). These don't exist in `common/terrain/*.txt` but are valid in technology modifiers.

### show_effect_as_desc

```hoi4
show_effect_as_desc = yes

modifier = {
    stability_factor = 0.05
}
```

When `yes`, the modifier tooltips display as the technology's description. This affects both standard modifiers and effects.

## Effects

### on_research_complete

```hoi4
on_research_complete = {
    add_political_power = 50
    add_stability = 0.05
}
```

Executes when the technology finishes research. Scope is the researcher country.

> [!CRITICAL] `on_research_complete` does NOT run when technologies are unlocked via history files. It only triggers for actual research completion during gameplay.

### on_research_complete_limit

```hoi4
on_research_complete_limit = {
    has_dlc = "Together for Victory"
}
```

A trigger that gates the entire `on_research_complete` effect block. If the limit is false, the effects don't execute.

This should be set if parts of the effect block might be invisible or invalid for some countries, preventing error log spam.

## AI Research

### ai_will_do

```hoi4
ai_will_do = {
    factor = 10
    
    modifier = {
        factor = 2
        has_war = yes
    }
}
```

The AI evaluates `ai_will_do` every 7 days to determine research priorities. Higher values increase priority.

> [!CRITICAL] The AI requires at least ONE category defined in `common/ai_focuses/` or it ignores ALL technologies. If you create custom categories, you must add them to ai_focuses files or the AI will never research techs using those categories.

## Categories

```hoi4
categories = {
    infantry_weapons
    infantry_tech
}
```

Categories serve multiple purposes:

- **AI focus files:** Direct AI research priorities
- **Research bonuses:** Ideas and modifiers can boost category research speed
- **Tech sharing:** Determines which techs can be shared between countries
- **add_tech_bonus effects:** Allow temporary research bonuses to categories

Categories are defined in `common/technology_tags/*.txt`.

## Experience System

### Research Type

```hoi4
xp_research_type = army
```

Valid values: `army`, `navy`, `air`

Determines which experience pool can be spent to boost this technology's research.

### XP Boost

```hoi4
xp_boost_cost = 50
xp_research_bonus = 1.5
```

- `xp_boost_cost`: Experience points required to boost
- `xp_research_bonus`: Speed multiplier when boosted (1.5 = +50% speed)

### XP Unlock

```hoi4
xp_unlock_cost = 100
```

Experience points required to unlock the technology for research without meeting normal prerequisites.

## Technology Sharing

```hoi4
add_to_tech_sharing_group = tech_sharing_group_id
```

This is the ONLY way to join a tech sharing group. Countries cannot join via other effects.

### available Trigger for Sharing

```hoi4
available = {
    is_in_faction_with = FROM
}
```

The `available` trigger for the tech sharing group automatically kicks countries out if it becomes false. This allows dynamic sharing groups based on faction membership or other conditions.

### is_faction_sharing

```hoi4
is_faction_sharing = yes
```

When enabled, both the giver and receiver must be in the same faction for sharing to work.

## Unresearching Technologies

```hoi4
set_technology = {
    tech_id = 0
}
```

> [!CRITICAL] Using `set_technology` with value 0 to unresearch technologies does NOT work properly. It fails for mutually exclusive (XOR) technologies, and database objects (equipment, buildings, subunits) remain usable until game restart. Treat enabled objects as permanent grants - there's no reliable way to revoke them.

## Doctrine Technologies

```hoi4
doctrine = yes
```

Technologies with `doctrine = yes` are doctrine techs, but the folder must ALSO be marked as a doctrine folder in the GUI file. Doctrine techs use a different GUI: `interface/countrydoctrinetreeview.gui` instead of `countrytechtreeview.gui`.

## Localisation

### Standard Keys

- `<tech_id>`: Technology name
- `<tech_id>_desc`: Technology description

### Country-Specific

- `<TAG>_<tech_id>`: Country-specific tech name
- `<TAG>_<equipment_id>`: If tech unlocks equipment

### Fallback Behavior

Technologies without explicit localisation borrow names from the equipment they unlock. The priority is:

1. `<TAG>_<tech_id>`
2. `<tech_id>`
3. `<TAG>_<equipment_id>`
4. `<equipment_id>`

## Icon System

Technology icons use the pattern `GFX_<tech_id>_medium`. Country-specific overrides use `GFX_<TAG>_<tech_id>_medium`.

If equipment unlocked by the tech doesn't have a `GFX_<equipment>_medium` icon, it copies the tech's icon automatically.

## Related Systems

For GUI configuration, visibility, positioning, and doctrine display, see [Technologies GUI](/database/technologies_gui.md).

For equipment unlocking and production, see [Equipment](/database/equipment.md).

For building unlocking, see [Buildings](/database/buildings.md).
