---
domain: military
concept: division_template
version: 1.14+
requires: [units]
relates: [oob, equipment]
---

# Division Templates

Division templates define the composition, organization, and naming of military divisions. They specify which battalions and support companies form a division and control combat width calculations.

## Template Structure

Templates are defined in OOB files or via the `division_template` effect:

```hoi4
division_template = {
    name = "Infantry Division"
    division_names_group = GER_INF_01
    
    regiments = {
        infantry = { x = 0 y = 0 }
        infantry = { x = 0 y = 1 }
        infantry = { x = 0 y = 2 }
        infantry = { x = 1 y = 0 }
        infantry = { x = 1 y = 1 }
        infantry = { x = 1 y = 2 }
    }
    
    support = {
        engineer = { x = 0 y = 0 }
        recon = { x = 0 y = 1 }
        artillery = { x = 0 y = 2 }
    }
}
```

## Regiment Coordinate System

Regiment and support company positions use a grid coordinate system. The division origin (0,0) is the TOP-LEFT corner, with the Y-axis increasing DOWNWARD (inverted from standard Cartesian coordinates).

Maximum indices are `(MAX_VALUE - 1)`, not `MAX_VALUE`. For example, if `MAX_DIVISION_BRIGADE_WIDTH = 5`, valid X coordinates are 0-4, not 0-5.

> [!CRITICAL] Out-of-bounds coordinates fail silently. A unit placed at x=10 when the maximum is 4 simply does not appear in the division, with no error message.

### Combat Battalion Groups

Combat battalions within a single Y-column CANNOT mix unit groups. If x=0 contains infantry (which has `group = mobile`), then x=0 cannot also contain artillery (which has a different group). This restriction prevents combining infantry, armor, and support-type battalions in the same column.

Support companies require their unit definition to have `group = support`. Placing non-support units in the support block causes them to fail silently - they won't appear in the division.

## Division Naming

Templates support two mutually exclusive naming methods:

### Direct Naming

```hoi4
division_template = {
    name = "1st Panzer Division"
}
```

Sets a fixed name for all divisions using this template.

### Ordered Naming

```hoi4
division_template = {
    division_names_group = GER_MOT_01
}
```

References a named group in `common/units/names_divisions/*.txt`:

```hoi4
GER_MOT_01 = {
    name = "Motorized Division"
    
    for_countries = { GER }
    can_use = { always = yes }
    
    division_types = { motorized }
    
    fallback_name = "%d. Motorized Division"
    
    ordered = {
        1 = { "%d. Motorized Division" }
        2 = { "%d. Motorized Division" }
        10 = { "%d. (mot) Division" }
    }
}
```

The `name_order` lookup checks the `ordered` array first, then uses `fallback_name` if the number is missing. There is no error if a specific number lacks an entry.

> [!CRITICAL] Using both `name = ""` and `division_names_group = {}` causes undefined behavior. Choose only one naming method per template.

### Automatic Division Names Group Selection

If `division_names_group` is unset, the game auto-selects a group based on division composition. The selection uses the FIRST subunit type in the `regiments` block, not the dominant or most numerous type.

For a template with the first entry as `cavalry = { x = 0 y = 0 }` followed by infantry, the game selects a cavalry names group even if infantry battalions outnumber cavalry 9:1.

## Template Locking

Templates can be locked to prevent player modification:

```hoi4
division_template = {
    is_locked = yes
    division_cap = 10
    force_allow_recruiting = yes
}
```

The `division_cap` attribute limits the maximum number of divisions that can use this template. However, `division_cap` requires `is_locked = yes` - the cap is ignored without the lock.

Similarly, `force_allow_recruiting = yes` has no effect without `is_locked = yes`.

Locked templates prevent player modification through the division designer but AI countries can still modify them via scripting effects.

## Combat Width Calculation

Combat width is calculated from the sum of battalion widths in the template. Each battalion type has a `width` attribute in its unit definition (see [Units](/military/units.md)).

Support companies contribute to combat width based on the `combat_support_width` value in terrain definitions, not their own width attribute.

## Priority and Obsolescence

Templates support priority ordering and obsolescence marking:

```hoi4
division_template = {
    priority = 2
    is_obsolete = yes
}
```

Priority controls production and reinforcement ordering. Higher priority templates receive equipment and manpower first. The `is_obsolete` flag marks templates for replacement and can trigger AI template updates.

## Template Modification Effects

Templates can be modified mid-game via effects:

```hoi4
division_template = {
    name = "Infantry Division"
    regiments = {
        infantry = { x = 0 y = 0 }
        infantry = { x = 0 y = 1 }
    }
}
```

When used as an effect rather than initial definition, this modifies the existing template matching the `name` field. The effect replaces the entire regiment structure with the new definition.

## Related Systems

See [Units](/military/units.md) for battalion and support company definitions.  
See [OOB Files](/military/oob.md) for initial template loading and division instantiation.
