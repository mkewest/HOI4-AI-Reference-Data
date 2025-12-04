---
domain: military
concept: intel_agencies
version: 1.14+
requires: [LaR_DLC]
relates: [espionage, operatives]
---

# Intelligence Agencies

Intelligence agencies are special organizations introduced in the La Résistance DLC that provide espionage capabilities and operative bonuses. Each nation can create one intelligence agency with a unique identity and upgrade path.

## Agency Definition Structure

Intelligence agencies are defined in `common/intelligence_agencies/*.txt`:

```hoi4
generic_intelligence_agency = {
    picture = GFX_intelligence_agency_logo_generic
    
    names = {
        GER = {
            "Abwehr"
            "Geheime Staatspolizei"
        }
        
        ENG = {
            "Secret Intelligence Service"
            "Special Operations Executive"
        }
        
        generic = {
            "Intelligence Service"
            "Secret Service"
        }
    }
    
    available = {
        has_war = yes
    }
    
    upgrade = { ... }
    upgrade = { ... }
}
```

## Icon System

Agency icons use a special two-frame sprite system:

```hoi4
picture = GFX_intelligence_agency_logo_generic
```

The sprite must be 234×119 pixels split into two frames:

| Frame | X Range | Purpose |
|-------|---------|---------|
| 1 | 0-116px | Unselected state |
| 2 | 117-233px | Selected state |

> [!CRITICAL] The frame split occurs at exactly 117px on the X-axis. The sprite definition must include `noOfFrames = 2` or the icon selection visual breaks.

Missing the `noOfFrames = 2` attribute causes the selection highlight to malfunction - the icon may appear stuck in selected or unselected state.

## Agency Names

The `names` block provides randomized agency names per country:

```hoi4
names = {
    GER = {
        "Abwehr"
        "Geheime Staatspolizei"
        "Sicherheitsdienst"
    }
    
    generic = {
        "Intelligence Service"
        "Secret Service"
    }
}
```

Names are organized by country tag with a `generic` fallback. The game randomly selects from the list when creating an agency.

### Name Selection Behavior

The names list is only used if the `create_intelligence_agency` effect doesn't specify a `name` parameter:

```hoi4
# Uses random name from definition
create_intelligence_agency = yes

# Uses specified name
create_intelligence_agency = {
    name = "Custom Agency Name"
}
```

When a name is explicitly provided in the effect, the `names` list is ignored entirely.

> [!CRITICAL] Icon-only definitions (agencies without upgrades or special mechanics) still require at least one name entry or the definition is invalid. Even if names are never used, the block must exist with at least one entry.

## Availability Trigger

The `available` block controls icon selection in the UI:

```hoi4
available = {
    has_war = yes
    has_government = fascism
}
```

This trigger affects ONLY which agency icon can be selected, NOT which names appear in the names list. The availability condition is checked when the player opens the agency creation interface.

If multiple agencies exist with different `available` conditions, the UI shows only those agencies currently available based on the country's state.

## Upgrade System

Agencies can define upgrade paths:

```hoi4
upgrade = {
    token = upgrade_form_department
    name = upgrade_form_department
    icon = GFX_intelligence_agency_upgrade_form_department
    
    cost = 50
    
    visible = {
        always = yes
    }
    
    available = {
        num_of_operatives > 2
    }
    
    modifier = {
        operative_slot = 1
        crypto_strength = 0.05
    }
    
    ai_will_do = {
        factor = 1
    }
}
```

Upgrades provide permanent modifiers to agency capabilities and are purchased with political power. Each upgrade can have visibility and availability conditions to gate progression.

## Multiple Default Names

When multiple country entries exist without TAG-specific identifiers:

```hoi4
names = {
    generic = {
        "Service A"
        "Service B"
        "Service C"
    }
    generic = {
        "Agency X"
        "Agency Y"
    }
}
```

Multiple `generic` blocks or duplicate TAG entries create a random selection queue. The game treats each block as a separate pool and randomly chooses which pool to use, then randomly selects a name from that pool.

This allows defining themed name sets where the game picks a theme and then a name within that theme.

## Selection Effect

Intelligence agencies require manual integration with the agency creation system:

```hoi4
# In a decision or focus
create_intelligence_agency = {
    picture = GFX_intelligence_agency_logo_generic
}
```

> [!CRITICAL] The selection effect is NOT automatically generated. You must manually create decision or focus effects for both the agency creation and the two-frame icon states (selected/unselected).

Without proper effect integration, the agency definition exists but cannot be selected or created by players.

## AI Behavior

The `ai_will_do` block in upgrades controls AI upgrade prioritization:

```hoi4
upgrade = {
    ai_will_do = {
        factor = 2
        
        modifier = {
            factor = 0.5
            num_of_operatives < 3
        }
    }
}
```

Higher factors make the AI prioritize that upgrade. Modifiers allow conditional weighting based on game state.

## Related Systems

See [Operatives](/espionage/operatives.md) for operative mechanics and upgrades enabled by agencies.  
See [Espionage](/espionage/operations.md) for intelligence operations and mission types.
