---
domain: military
concept: oob
version: 1.14+
requires: [division_template, units, equipment]
relates: [country_history, effects]
---

# Organization of Battle (OOB) Files

OOB files define a country's starting military forces including division templates, deployed units, air wings, and naval fleets. They are loaded through country history files or scripted effects.

## File Structure

OOB files are located in `history/units/*.txt` and use standard HOI4 scripting syntax. Each file contains multiple top-level blocks defining different aspects of military organization:

```hoi4
division_template = { ... }
units = { ... }
air_wings = { ... }
instant_effect = { ... }
```

## Loading Mechanism

OOB files execute as **additive operations**. Loading an OOB file mid-game adds to existing military state rather than replacing it. This allows multiple OOB files to be layered or scenarios to build upon base game forces.

Each OOB must be explicitly loaded via country history or scripted effects:

```hoi4
# In country history file
1936.1.1 = {
    oob = "ENG_1936"
}

# Via scripted effect
load_oob = GER_1939_tanks
```

> [!CRITICAL] OOB files do NOT auto-load by filename. A file named `TAG_1936.txt` will not load unless explicitly referenced in country history or called via `load_oob` effect.

## DLC-Specific Content Handling

When OOB files contain DLC-specific content (NSB tank equipment, MTG ship hulls), use conditional branching in the country history file:

```hoi4
if = {
    limit = { has_dlc = "No Step Back" }
    oob = "SOV_1936_NSB"
}
else = {
    oob = "SOV_1936_legacy"
}
```

The `if`/`else` structure ensures appropriate OOB loads based on player's DLC ownership. OOB files themselves do not check DLC status.

> [!CRITICAL] Missing the `else` clause causes NO OOB to load for non-DLC users. Always include both branches when DLC content is involved.

DLC splits are required for ANY reference to DLC-specific equipment types, not just divisions using them. A single tank equipment variant in the file requires the entire OOB to be in the conditional branch.

## Division Instantiation

The `units` block within OOB files instantiates divisions from templates:

```hoi4
units = {
    division = {
        name = "1st Infantry Division"
        division_name = { is_name_ordered = yes name_order = 1 }
        location = 3456
        division_template = "Infantry Division"
        start_experience_factor = 0.3
        start_equipment_factor = 0.8
    }
}
```

Multiple divisions can reference the same template. Division names can be set directly via `name` or through the `division_name` block for ordered naming systems.

## Equipment Assignment

Equipment variants can be forced on divisions or production lines:

```hoi4
division = {
    division_template = "Panzer Division"
    force_equipment_variants = {
        medium_tank_equipment = { 
            owner = "GER"
            creator = "GER"
            version_name = "Panzer IV Ausf. G"
        }
    }
}
```

The `start_equipment_factor` attribute controls initial equipment levels as a percentage (0.0-1.0). This does NOT subtract from country reserves - units spawn with equipment "out of thin air."

In contrast, `start_manpower_factor` DOES subtract from reserves if unset, auto-filling divisions to maximum possible manpower from available pools.

> [!CRITICAL] When using `force_equipment_variants` with partial amounts, remaining equipment slots stay EMPTY rather than auto-filling with other variants or base types.

## Variant Requirements by DLC

Equipment variants have mandatory `version_name` requirements depending on DLC:

- **NSB (No Step Back):** Tank equipment REQUIRES `version_name` - missing causes crash or failure to spawn
- **MTG (Man the Guns):** Ship equipment REQUIRES `version_name` - cannot spawn without valid variant in country history
- **BBA (By Blood Alone):** Airplane equipment REQUIRES `version_name`
- **Non-DLC equipment:** `version_name` is OPTIONAL - uses base archetype if unspecified

For ships, if the owner lacks required technology but the `creator` has it, the ship uses creator's technology level BUT the owner receives the ship. This allows gifting advanced ships to less developed nations.

## Production Setup

The `instant_effect` block can initialize production lines:

```hoi4
instant_effect = {
    add_equipment_production = {
        equipment = {
            type = infantry_equipment_1
            creator = "GER"
        }
        requested_factories = 5
        progress = 0.85
        efficiency = 50
    }
}
```

Production efficiency is specified as 0-100 (percent), NOT 0.0-1.0. Using `efficiency = 0.5` sets 0.5% efficiency, not 50%.

The `progress` attribute represents completion toward a SINGLE unit, not the entire production run. A value of `progress = 2.3` means 2 completed units plus 0.3 progress toward the third unit.

The `requested_factories` parameter queues the request if insufficient factories are available - it does NOT error or clamp to available capacity.

## Load Timing and Validation

MIOs (Military-Industrial Organizations) and policies load ONLY when creating a new game. They cannot be injected into ongoing games through OOB files or effects.

Trait modifications (bonuses, icons, localization) can be changed without starting a new game, but adding new traits works mid-game while removing existing traits causes errors.

> [!CRITICAL] Check `error.log` TWICE when validating OOB files: (1) immediately after game start, and (2) after browsing MIO menus in-game. Visibility filters fire on menu access, potentially revealing errors not present at load time.

## Related Systems

See [Division Templates](/military/division_template.md) for template definition syntax.  
See [Equipment](/military/equipment.md) for variant creation and archetype hierarchy.  
See [Air Wings](/military/air_wings.md) and [Navies](/military/navies.md) for force-specific instantiation details.
