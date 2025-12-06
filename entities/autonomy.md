---
domain: entities
concept: autonomy
version: 1.14+
requires: [country_tags, ideologies]
relates: [factions, country_history, ideologies]
---

# Autonomy System

The autonomy system governs subject relationships between overlord and puppet nations. Autonomy states define levels of independence ranging from complete integration to near-sovereign status, each with specific gameplay restrictions and bonuses.

## Autonomy State Definition

Autonomy states are defined in `common/autonomous_states/*.txt`:

```hoi4
autonomy_state = {
    id = "autonomy_puppet"
    
    default = yes
    is_puppet = yes
    
    min_freedom_level = 0.0
    manpower_influence = 0.3
    
    use_overlord_color = no
    
    rule = {
        can_not_declare_war = yes
        can_decline_call_to_war = yes
    }
    
    modifier = {
        autonomy_gain = 1.0
    }
    
    allowed = {
        has_dlc = "Together for Victory"
    }
}
```

### Core Attributes

**ID:** The `id` attribute is mandatory, unique, and used in all autonomy-related triggers and effects.

**Default:** The `default = yes` attribute marks this autonomy state as the default level for peace conference puppeting and the basic `puppet` effect. Only one autonomy state should have `default = yes`.

**Is Puppet:** The `is_puppet = yes` attribute enables the `is_puppet` trigger for countries at this autonomy level. This distinguishes true subjects from independent nations.

**Use Overlord Color:** When `use_overlord_color = yes`, the subject uses its overlord's map color instead of its own. This provides visual indication of control but can make maps harder to read when overlords have many subjects.

### Freedom Level

```hoi4
min_freedom_level = 0.4
```

> [!CRITICAL] Never use identical `min_freedom_level` values across different autonomy states. Duplicate values cause unpredictable behavior in autonomy transitions and point calculations.

Freedom levels range from 0.0 (complete integration) to 1.0 (full independence). The freedom level determines:

- When subjects can request independence
- Point thresholds for autonomy changes
- AI autonomy management behavior

**Point calculations:**

The total points required to annex from autonomy level X is `X × AUTONOMOUS_TOTAL_SCORE`, where `AUTONOMOUS_TOTAL_SCORE` is defined in `NDefines.NDiplomacy`.

The cost to transition between autonomy levels is `abs(level_diff) × AUTONOMOUS_TOTAL_SCORE`. Moving from freedom level 0.2 to 0.4 costs `0.2 × AUTONOMOUS_TOTAL_SCORE` points.

Points accumulate through lend-lease, resource sharing, and other subject contributions. The `AUTONOMOUS_SPILLOVER` define controls how many points transfer between autonomy level transitions.

### Manpower Influence

```hoi4
manpower_influence = 0.3
```

The `manpower_influence` attribute is a float between 0.0 and 1.0 that determines what percentage of the subject's manpower the overlord can access. A value of 0.3 means the overlord receives 30% of the subject's manpower for recruitment.

### Subject Rules

The `rule` block defines restrictions and permissions for subjects:

```yaml
can_not_declare_war: Subject cannot initiate wars
can_decline_call_to_war: Subject can refuse overlord's calls to arms
units_deployed_to_overlord: Subject's units deploy under overlord control
can_be_spymaster: Subject can serve as faction spymaster
contributes_operatives: Subject provides operatives to overlord
can_create_collaboration_government: Subject can create collaborations
```

Rules use boolean values (`yes`/`no`). Only specified rules need to be included; unspecified rules default to `no` (restriction not applied).

### Modifiers

The `modifier` block applies country-level modifiers to subjects at this autonomy level:

```hoi4
modifier = {
    autonomy_gain = 1.0
    autonomy_gain_global_factor = 0.5
    extra_trade_to_overlord_factor = 0.25
    overlord_trade_cost_factor = -0.9
    license_subject_master_purchase_cost = -1.0
}
```

Modifiers control autonomy point accumulation, trade costs, and economic relationships between subject and overlord.

## Autonomy State Icons

Icons are defined in interface `.gfx` files using the format `GFX_<id>_icon`:

```hoi4
spriteType = {
    name = "GFX_autonomy_puppet_icon"
    texturefile = "gfx/interface/autonomy/autonomy_puppet_icon.dds"
}
```

The icon sprite name must match the autonomy state's `id` with `_icon` suffix.

## Autonomy Localization

Localization keys follow three priority levels:

1. `<OVERLORD>_<SUBJECT>_<id>`: Most specific (e.g., `GER_FRA_autonomy_puppet`)
2. `<SUBJECT>_<id>`: Country-specific (e.g., `FRA_autonomy_puppet`)
3. `<id>`: Generic (e.g., `autonomy_puppet`)

The game selects the most specific available key. This allows customized subject names for specific overlord-subject pairs while falling back to generic names otherwise.

## Setting Autonomy

### Basic Effect

```hoi4
set_autonomy = {
    target = TAG
    autonomy_state = autonomy_integrated_puppet
    freedom_level = 0.2
}
```

The `set_autonomy` effect establishes a subject relationship. The executing country becomes the overlord, and the target becomes the subject.

**Freedom level:** The `freedom_level` parameter is optional. If omitted, the subject starts at the autonomy state's `min_freedom_level`. Specifying a value overrides this default.

### Autonomy and Politics

> [!CRITICAL] Setting autonomy resets the subject's party popularity and ruling party to match the overlord's ideology. Always place `set_autonomy` before `set_popularities` and `set_politics` in history files, or the political settings will be overwritten.

**Example - incorrect order:**

```hoi4
set_popularities = {
    democratic = 100
}
set_politics = {
    ruling_party = democratic
}
set_autonomy = {
    target = TAG
    autonomy_state = autonomy_puppet
}
# Result: Politics reset, settings lost
```

**Example - correct order:**

```hoi4
set_autonomy = {
    target = TAG
    autonomy_state = autonomy_puppet
}
set_popularities = {
    democratic = 100
}
set_politics = {
    ruling_party = democratic
}
# Result: Politics preserved
```

### History File Placement

> [!CRITICAL] When setting autonomy in history files, load order matters. Placing autonomy in the overlord's history file can cause the autonomy to apply before the subject's other history settings load, overwriting party configurations.

**Recommended approach:** Place autonomy effects in the subject's history file, not the overlord's:

```hoi4
# In history/countries/SUB - Subject.txt
set_autonomy = {
    target = SUB
    overlord = OVR
    autonomy_state = autonomy_puppet
}
```

This ensures the autonomy applies after the subject's own initialization.

**Alternative workaround:** Scope into the overlord's tag before setting autonomy in the subject's file:

```hoi4
# In history/countries/SUB - Subject.txt
OVR = {
    set_autonomy = {
        target = SUB
        autonomy_state = autonomy_puppet
    }
}

# Subject's own political setup follows
set_popularities = { ... }
```

**Tag order modification:** Adjust tag definition order in `common/country_tags/*.txt` so the subject's tag appears after its overlord's tag. This ensures the overlord's history fully executes before the subject's history begins.

### Faction Membership

Puppets automatically join their overlord's faction when autonomy is set. While automatic joining occurs, explicitly adding the subject via `add_to_faction` is recommended:

```hoi4
set_autonomy = {
    target = TAG
    autonomy_state = autonomy_puppet
}
add_to_faction = TAG
```

Explicit faction addition makes the relationship clear in scripting and ensures correct initialization order.

## Autonomy State Restrictions

### Manual-Only Autonomy States

To create an autonomy state that can only be assigned via `set_autonomy` (not through natural progression):

```hoi4
allowed = {
    OR = {
        is_subject = no
        has_autonomy_state = manual_only_autonomy
    }
}
```

This `allowed` trigger prevents transitions to this autonomy state from other states (since `allowed = no` when the country is a subject at a different autonomy level). The state can only be reached through explicit `set_autonomy` effects.

> [!CRITICAL] The target country must be independent at the time `set_autonomy` executes when creating a subject with a manual-only autonomy state. If the target is already a subject of another overlord, the `allowed` trigger fails and the autonomy change doesn't apply.

### DLC-Gated Autonomy

Autonomy states can require specific DLC:

```hoi4
allowed = {
    has_dlc = "Together for Victory"
}
```

When an autonomy state has DLC requirements:

- Subjects remain at that autonomy level if the DLC is disabled later
- New autonomy assignments to that state are blocked without the DLC
- Autonomy transitions skip that state when the DLC is not present

## Autonomy Triggers

Common triggers for checking autonomy status:

```hoi4
is_subject = yes
is_subject_of = TAG
has_autonomy_state = autonomy_puppet
has_autonomy = {
    target = TAG
    autonomy_state = autonomy_integrated_puppet
}
```

The `is_puppet` trigger specifically checks if the subject's autonomy state has `is_puppet = yes` defined.

## AI Autonomy Behavior

### AI Decision Blocks

```hoi4
ai_subject_wants_higher = {
    factor = 100
    
    modifier = {
        factor = 0
        has_government = fascism
        overlord = { has_government = fascism }
    }
}

ai_overlord_wants_lower = {
    factor = 100
    
    modifier = {
        factor = 2
        overlord = { is_in_faction_with = ROOT }
    }
}
```

These MTTH blocks control AI desire to change autonomy levels:

- `ai_subject_wants_higher`: Subject's desire to gain more freedom
- `ai_overlord_wants_lower`: Overlord's desire to tighten control

Lower MTTH values mean stronger desire. Use modifiers to adjust behavior based on ideology, war status, and relationship factors.

### Garrison Desires

```hoi4
ai_overlord_wants_garrison = {
    always = yes
}
```

This trigger determines whether the overlord wants the subject to provide garrison forces. The trigger checks in overlord scope and affects AI garrison division transfers.

## Autonomy Progression

### Level Transitions

```hoi4
can_take_level = {
    # Trigger block
}

can_lose_level = {
    # Trigger block
}
```

These triggers control whether autonomy level can increase or decrease. They enable conditional autonomy progression based on war status, ideology, or other factors.

### Peace Conference Behavior

```hoi4
use_for_peace_conference_weight = {
    factor = 100
    
    # ROOT = subject
    # FROM = overlord
    
    modifier = {
        factor = 0.5
        FROM = { is_major = no }
    }
}
```

This MTTH block determines how likely this autonomy level is to be assigned during peace conferences. The weight compares against other autonomy states when the AI decides puppet levels.

### Initial Freedom

```hoi4
peace_conference_initial_freedom = 0.5
```

The `peace_conference_initial_freedom` attribute sets the starting freedom level when this autonomy state is assigned during peace conferences. It defaults to 0.5 if not specified.

### Allowed Levels Filter

```hoi4
allowed_levels_filter = { 1 3 5 }
```

The `allowed_levels_filter` array specifies which autonomy progression levels this state can transition to. This creates custom autonomy paths that skip certain intermediate states.

## Related Defines

- `AUTONOMOUS_TOTAL_SCORE`: See [NDiplomacy](/defines_list/NDiplomacy.md)
- `AUTONOMOUS_SPILLOVER`: See [NDiplomacy](/defines_list/NDiplomacy.md)
- `AUTONOMY_LEVEL_CHANGE_PP_COST`: See [NDiplomacy](/defines_list/NDiplomacy.md)

## Related Systems

For subject naming and cosmetic tags, see [Cosmetic Tags](/entities/cosmetic_tags.md).

For autonomy effects in country history files, see [Country History](/entities/country_history.md).

For faction membership and subject relationships, see [Factions](/entities/factions.md).
