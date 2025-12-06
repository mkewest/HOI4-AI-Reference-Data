---
domain: assets
concept: entities
version: 1.14+
requires: [particles]
relates: [units, buildings, particles]
---

# Entity System

Entities define 3D models and their animation behavior in `gfx/entities/*.asset` files. The system uses state machines to control model appearance, animations, and particle effects based on gameplay context.

## Entity States

### State Availability

Available states depend on entity usage context. Units receive combat-related states (idle, moving, attacking), buildings receive construction states, and props receive environmental states. The `idle` state is universally available for all entities regardless of context.

Context-specific states are not documented in entity definition files - they're determined by where and how the entity is used in gameplay. For example, infantry entities automatically receive combat states when assigned to division templates, while building entities receive construction progress states when used in state definitions.

### State Selection

Multiple state entries can share the same `name` attribute. When multiple states have identical names, the `chance` attribute determines weighted random selection:

```hoi4
entity = {
    name = "infantry_entity"
    
    state = {
        name = "idle"
        chance = 70
        animation = "idle_relaxed"
    }
    
    state = {
        name = "idle"
        chance = 30
        animation = "idle_alert"
    }
}
```

When the entity enters idle state, it randomly selects between relaxed and alert animations using 70/30 weighting. This creates variation without requiring different state names.

### State Inheritance

Child entities can inherit parent state using `get_state_from_parent` attribute:

```hoi4
entity = {
    name = "soldier_with_rifle"
    
    attach = {
        weapon_attach_point = "rifle_entity"
    }
}

entity = {
    name = "rifle_entity"
    
    state = {
        name = "idle"
        get_state_from_parent = yes
    }
}
```

When `get_state_from_parent = yes`, the child entity (rifle) transitions to match the parent entity's (soldier) current state. State propagation is one-way - parent to child only. Children don't affect parent state.

This enables complex hierarchical animations where weapon states automatically sync with character animations without duplicating state logic.

## Animation System

### Animation References

The animation system uses a three-level reference chain:

1. `.asset` animation files define animation `name`
2. `.gfx` mesh files reference animation `name` as animation `type`
3. `.gfx` mesh files define animation `id`
4. Entity state `animation` attribute references mesh animation `id`

Chain structure:

```text
.asset: animation { name = "walk_cycle" }
    ↓
.gfx mesh: animation { type = "walk_cycle" id = "anim_walk" }
    ↓
entity state: animation = "anim_walk"
```

This indirection allows multiple meshes to share animation definitions while using different local identifiers.

### State Animation

State blocks define which animation plays:

```hoi4
state = {
    name = "moving"
    animation = "anim_walk"
    animation_blend_time = 0.3
    animation_speed = 1.0
}
```

State animation attributes:

- `animation`: References animation `id` from mesh definition
- `animation_blend_time`: Seconds to blend from previous animation
- `animation_speed`: Playback speed multiplier

Blend time creates smooth transitions between states. Setting blend time to 0 causes instant animation switching which can appear jarring.

## Entity Attachments

### Attach Syntax

Entity attachments use dynamic key syntax where the skeleton node name is the key itself:

```hoi4
entity = {
    name = "character_entity"
    
    attach = {
        head_attach_point = "helmet_entity"
        weapon_attach_point = "rifle_entity"
        backpack_attach_point = "equipment_entity"
    }
}
```

The keys (`head_attach_point`, `weapon_attach_point`, etc.) must match node names in the parent entity's skeleton. The system locates the named node and attaches the specified entity to that position.

Attach points are defined in the 3D model's skeleton hierarchy. If an attachment references a non-existent node name, the attachment silently fails without error message.

## Entity Events

### Event Timing

Events trigger actions at specific times within state animations:

```hoi4
state = {
    name = "attacking"
    animation = "anim_attack"
    
    event = {
        time = 0.3
        trigger_once = yes
        particle = "muzzle_flash"
        sound = "rifle_shot"
    }
}
```

Event attributes:

- `time`: Seconds from state start when event triggers
- `trigger_once`: If true, event fires once per state entry; if false, can repeat
- `particle`: Particle effect name to spawn
- `sound`: Sound effect to play
- `keep_particle`: If true, particle persists beyond event time but within state lifecycle

Event `time` is relative to state start, not absolute game time. When an entity enters a state, the timer begins from 0. An event with `time = 0.3` fires 0.3 seconds after state activation.

The `trigger_once` attribute applies per state entry, not globally. If an entity exits and re-enters the state, `trigger_once` events can fire again. This is per-entry behavior, not per-session.

### Particle Persistence

The `keep_particle` attribute controls particle lifecycle. When true, particles spawned by the event continue beyond the event's trigger time but still terminate when the entity exits the state. When false (default), particles terminate immediately at the event's natural end time.

This enables effects that persist through an animation - a smoke trail that continues after the projectile launch event, for example - while still being cleaned up on state changes.

## Common Patterns

### Weapon Synchronization

Weapons attached to characters typically use `get_state_from_parent = yes` to sync animation states:

```hoi4
entity = {
    name = "soldier"
    
    state = { name = "idle" animation = "idle_stand" }
    state = { name = "moving" animation = "walk" }
    state = { name = "attacking" animation = "fire_rifle" }
    
    attach = {
        right_hand = "rifle_entity"
    }
}

entity = {
    name = "rifle_entity"
    
    state = {
        name = "idle"
        get_state_from_parent = yes
    }
    
    state = {
        name = "moving"
        get_state_from_parent = yes
    }
    
    state = {
        name = "attacking"
        animation = "rifle_fire_anim"
        event = {
            time = 0.1
            particle = "muzzle_flash"
            sound = "rifle_shot"
        }
    }
}
```

The rifle inherits parent state for idle and moving but defines specific animation and effects for attacking.

### Combat Effects

Combat entities use events to synchronize visual and audio effects with animation keyframes:

```hoi4
state = {
    name = "firing"
    animation = "cannon_fire"
    
    event = {
        time = 0.2
        particle = "cannon_muzzle_flash"
    }
    
    event = {
        time = 0.25
        sound = "cannon_boom"
    }
    
    event = {
        time = 0.3
        particle = "shell_eject"
    }
}
```

Multiple events at different times create complex synchronized sequences. The timing aligns with animation keyframes to match visual motion with effects.

## Related Systems

Entities integrate with animation definitions for movement, particle systems for visual effects, and sound definitions for audio. Unit and building definitions reference entities to define their 3D appearance. See [Particles](/assets/particles.md) for effect creation and animation asset files for motion data.
