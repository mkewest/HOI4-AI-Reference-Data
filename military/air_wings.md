---
domain: military
concept: air_wings
version: 1.14+
requires: [equipment, states]
relates: [airbases, air_combat]
---

# Air Wings

Air wings represent groups of aircraft stationed at airbases. They are instantiated through OOB files or scripted effects.

## Air Wing Structure

Air wings are defined in the `air_wings` block within OOB files:

```hoi4
air_wings = {
    123 = {  # State ID where airbase is located
        fighter_equipment_1 = {
            owner = "GER"
            amount = 50
            
            force_equipment_variants = {
                fighter_equipment_1 = {
                    owner = "GER"
                    creator = "GER"
                    version_name = "Bf 109 E"
                }
            }
        }
        
        tac_bomber_equipment_1 = {
            owner = "GER"
            amount = 24
        }
    }
}
```

Each top-level key under `air_wings` is a state ID. Air wings spawn in that state's airbase.

## Location Requirements

> [!CRITICAL] Air wings spawn in the state's airbase. The state MUST have an existing airbase or the wing will display an error state and be non-functional.

There is no validation on airbase capacity versus wing size. The game allows spawning 1000 planes in a size-1 airbase, though this creates overstacking penalties and may prevent takeoff.

## Equipment Assignment

Air wings use the same equipment variant system as divisions:

```hoi4
force_equipment_variants = {
    fighter_equipment_1 = {
        owner = "GER"
        creator = "GER"
        version_name = "Bf 109 E"
    }
}
```

### BBA Variant Requirement

With the **By Blood Alone (BBA)** DLC, airplane equipment REQUIRES `version_name`. Aircraft cannot spawn without a valid variant registered in country history.

Without BBA, `version_name` is optional - the game uses base aircraft archetypes if unspecified.

## Amount and Strength

The `amount` field specifies the number of aircraft in the wing. This represents the wing's current strength, not its maximum capacity.

Wings can be created at partial strength:

```hoi4
fighter_equipment_1 = {
    owner = "GER"
    amount = 30  # Creates 30-plane wing
}
```

The wing will automatically request reinforcements up to the air doctrine's wing size limits.

## Experience

Air wings can spawn with experience:

```hoi4
fighter_equipment_1 = {
    owner = "GER"
    amount = 50
    start_experience_factor = 0.3
}
```

The `start_experience_factor` uses float values 0.0-1.0, with boundaries defined in `UNIT_EXP_LEVELS` defines. A factor of 0.0 corresponds to "Green" experience level, not zero experience (minimum level always exists).

## Multiple Wings per State

A single state can host multiple wings of different types:

```hoi4
air_wings = {
    123 = {
        fighter_equipment_1 = { amount = 50 }
        tac_bomber_equipment_1 = { amount = 24 }
        cas_equipment_1 = { amount = 36 }
    }
}
```

Wings of the same type in the same state merge into a single wing unless they have different equipment variants.

## Ownership and Creator

The `owner` field must match the country receiving the OOB file. The `creator` field can differ, allowing gifted or lend-leased aircraft:

```hoi4
fighter_equipment_1 = {
    owner = "POL"      # Poland receives the aircraft
    creator = "GER"    # Germany manufactured them
}
```

If the owner lacks required technology but the creator has it, the aircraft use the creator's technology level.

## Air Wing Effects

Air wings can also be created via scripted effects:

```hoi4
create_air_wing = {
    state = 123
    equipment_type = fighter_equipment_1
    amount = 50
    version_name = "Bf 109 E"
}
```

This provides runtime air wing creation for events, decisions, and other scripted content.

## Related Systems

See [Equipment](/military/equipment.md) for aircraft equipment definitions and variant requirements.  
See [OOB Files](/military/oob.md) for initial military force setup including air wings.
