---
domain: database
concept: resources
version: 1.14+
requires: [buildings, production]
relates: [sprites, trade, infrastructure]
---

# Resources System

Resources are strategic materials required for equipment production. They're defined in `common/resources/00_resources.txt` within a `resources = {...}` root block.

## Resource Definition

```hoi4
resources = {
    resource_id = {
        icon_frame = 1
        cic = 0.125
        convoys = 0.1
    }
}
```

## Core Attributes

### icon_frame

Integer that references a frame in the `GFX_resources_strip` spritesheet. Frame indexing starts at 1.

> [!CRITICAL] The `noOfFrames` attribute in BOTH `GFX_resources_strip` AND `GFX_missing_resources_strip` must EXACTLY match the total number of defined resources. Frame count mismatches cause display bugs or crashes.

The icon frame determines which resource icon displays in production menus and strategic resource displays.

### cic (Civilian Industrial Capacity)

Float value with a maximum of 1.0. This modifier is INVERTED: lower values mean more resources per factory.

```yaml
cic:
  type: float
  default: 0.125
  max: 1.0
  calculation: "units per factory = 1 / cic"
  examples:
    - "cic = 0.125 → 8 units per factory (1 / 0.125 = 8)"
    - "cic = 0.2 → 5 units per factory"
    - "cic = 0.5 → 2 units per factory"
```

> [!CRITICAL] The cic value is INVERTED from what you might expect. A LOWER cic value produces MORE resources per factory. Values above 1.0 are invalid and cause errors.

The default value of 0.125 results in 8 resource units per civilian factory assigned to production.

### convoys

Float value determining how many resource units a single convoy can transport. Default is 0.1, meaning 10 units per convoy.

```yaml
convoys:
  type: float
  default: 0.1
  example: "0.1 = 10 units per convoy"
```

## Graphics Configuration

Resource graphics are defined in `interface/general_stuff.gfx`:

### Required Sprites

```hoi4
spriteType = {
    name = "GFX_resources_strip"
    texturefile = "gfx/interface/resources_strip.dds"
    noOfFrames = 8
}

spriteType = {
    name = "GFX_missing_resources_strip"
    texturefile = "gfx/interface/missing_resources_strip.dds"
    noOfFrames = 8
}
```

Both sprites must have `noOfFrames` equal to the number of resources. The resources strip shows available resources, while missing_resources_strip shows deficit indicators.

### Sprite Synchronization

When adding or removing resources:

1. Update the resource definition in `00_resources.txt`
2. Add/remove frames from both texture files
3. Update `noOfFrames` in both sprite definitions
4. Ensure frame order matches resource definition order

Failing to keep these synchronized causes incorrect icons or crashes.

## UI Integration

Resource UI elements are defined in `interface/countryproductionlineview.gui` and must follow specific naming conventions:

### Element Naming

For each resource, two UI elements must exist:

- `<resource>_icon`: Displays the resource icon
- `<resource>_value`: Displays the numeric value

Example for oil resource:
```
oil_icon
oil_value
```

> [!CRITICAL] Element names are case-sensitive and must match the resource ID exactly. `Oil_icon` or `OIL_icon` will not work - it must be `oil_icon`.

Misnamed elements cause resources to not display in the production interface.

## Localisation

Localisation keys for resources:

- `PRODUCTION_MATERIALS_<RESOURCE>`: Display name (note: all caps)
- `<resource>_desc`: Resource description

Example:
```yaml
PRODUCTION_MATERIALS_OIL: "Oil"
oil_desc: "Crude oil used for fuel and refinement"
```

The `PRODUCTION_MATERIALS_` prefix is mandatory for the display name - the game won't recognize other key formats.

## Fuel System

### FUEL_RESOURCE Define

```hoi4
FUEL_RESOURCE = oil
```

Only ONE resource can be designated as fuel via the `FUEL_RESOURCE` define in `common/defines/00_defines.lua`.

> [!CRITICAL] If multiple resources are set as fuel, only the LAST defined resource wins. The game doesn't merge them - it simply overwrites previous fuel assignments.

The fuel resource has special mechanics:
- Used by vehicles, ships, and aircraft
- Consumed during movement and combat
- Stored in fuel silos
- Refined from other resources

### Multiple Fuel Resources Workaround

There is no native support for multiple fuel types. If you need multiple fuel sources, you must:

1. Use modifiers to simulate different fuel qualities
2. Use events to convert between resource types
3. Script custom fuel consumption mechanics

The engine fundamentally expects a single fuel resource.

## Infrastructure Bonus

### INFRASTRUCTURE_RESOURCE_BONUS Define

```hoi4
INFRASTRUCTURE_RESOURCE_BONUS = 0.2
```

This define applies identically to ALL resources - infrastructure provides a production bonus regardless of resource type.

The bonus is:
```
Resource production = base × (1 + infrastructure_level × INFRASTRUCTURE_RESOURCE_BONUS)
```

With default value 0.2:
- Infrastructure 0: ×1.0 (base)
- Infrastructure 5: ×2.0 (+100%)
- Infrastructure 10: ×3.0 (+200%)

There's no way to make infrastructure affect specific resources differently - the modifier is universal.

## Resource Production

Resources are produced by:

1. **State resources:** Defined in state history files
2. **Buildings:** Synthetic refineries and similar structures
3. **Modifiers:** Various modifiers can boost resource output

Production is calculated per state and aggregated nationally. Trade and convoys then distribute resources between countries.

## Resource Trade

Resources can be traded between countries through:

- **Trade deals:** Manual agreements to exchange resources
- **Convoys:** Ships that transport resources along trade routes
- **Puppets:** Subject nations automatically send resources to overlords

Insufficient convoys or naval supremacy disrupts resource flow, creating shortages even when production exists.

## Common Issues

### Missing Resource Icons

If resource icons don't display:

1. **Check icon_frame:** Must match a valid frame in the spritesheet
2. **Verify noOfFrames:** Must equal total resource count in both strips
3. **Check UI element naming:** Must be exactly `<resource>_icon` and `<resource>_value`
4. **Verify sprite files exist:** Both resources_strip and missing_resources_strip

### Incorrect Production Values

If factories produce wrong amounts:

1. **Check cic value:** Remember it's inverted (lower = more production)
2. **Verify cic ≤ 1.0:** Values above 1.0 are invalid
3. **Check for modifiers:** Infrastructure and tech can affect output

### Fuel Not Working

If fuel mechanics malfunction:

1. **Verify FUEL_RESOURCE:** Check the define points to correct resource
2. **Only one fuel:** Ensure no conflicting fuel definitions
3. **Check refineries:** Fuel storage and production buildings must exist

## Related Systems

For buildings that produce resources (refineries), see [Buildings](/database/buildings.md).

For production and factories, see the production documentation.

For trade and convoy mechanics, see the trade documentation.

For infrastructure effects on resource production, see the infrastructure documentation.
