---
domain: database
concept: equipment
version: 1.14+
requires: [technologies_core]
relates: [units, production, resources, modifiers_list]
---

# Equipment System

Equipment represents producible military hardware in HOI4. Equipment is defined in `common/units/equipment/*.txt` using a two-tier system: archetypes define base stats, and specific equipment variants inherit from archetypes.

## Structure

```hoi4
equipments = {
    archetype_id = {
        is_archetype = yes
        type = infantry
        group_by = archetype
        
        interface_category = interface_category_land
        
        lend_lease_cost = 1
        build_cost_ic = 10
        manpower = 100
        
        maximum_speed = 4
        reliability = 0.8
        
        soft_attack = 25
        hard_attack = 5
        defense = 30
    }
    
    specific_equipment = {
        archetype = archetype_id
        parent = previous_equipment_version
        
        build_cost_ic = 12
        soft_attack = 30
    }
}
```

## Archetypes vs Specific Equipment

### Archetypes

Archetypes define the base template for a category of equipment:

```hoi4
infantry_equipment = {
    is_archetype = yes
    type = infantry
    # ... base stats
}
```

- `is_archetype = yes` marks this as a base template
- `type` determines which unit types can use this equipment
- All stats defined here serve as defaults

### Specific Equipment

Specific equipment inherits from archetypes:

```hoi4
infantry_equipment_1 = {
    archetype = infantry_equipment
    parent = infantry_equipment_0
    
    soft_attack = 30  # Overrides archetype value
    # All other stats inherited from archetype
}
```

> [!CRITICAL] Regular equipment inherits ALL modifiers from its archetype unless explicitly overridden. If the archetype has `maximum_speed = 4` and the specific equipment doesn't override it, the specific equipment also has `maximum_speed = 4`.

### is_buildable

```hoi4
is_buildable = no
```

Setting `is_buildable = no` prevents the equipment from being directly produced in factories. It can still be used by units if acquired through other means (lend-lease, captured equipment, etc.).

This is commonly used for obsolete equipment variants that should only exist from historical conversion.

## Equipment Modifiers

Equipment modifiers are grouped by type and purpose.

### Universal Modifiers

All equipment types support these modifiers:

```yaml
lend_lease_cost:
  desc: Cost factor for lend-lease agreements

build_cost_ic:
  desc: Industrial capacity cost to produce one unit

manpower:
  desc: Manpower required to field one unit

can_license:
  desc: Boolean - can be licensed to other countries

is_convertable:
  desc: Boolean - can be converted to other equipment types
```

### Land Equipment Base Stats

All land equipment uses these modifiers:

```yaml
reliability:
  range: [0, 1]
  desc: Affects equipment losses from attrition and combat

maximum_speed:
  default: 4
  desc: Base movement speed modifier
  note: Defaults to 4 if not specified
```

The `maximum_speed` modifier defaults to 4 for all land equipment when not explicitly defined.

### Land Offensive Stats

```yaml
soft_attack:
  desc: Damage against low-hardness targets (infantry, artillery)

hard_attack:
  desc: Damage against high-hardness targets (tanks, bunkers)

air_attack:
  desc: Damage against air units

ap_attack:
  desc: Armor-piercing attack value

breakthrough:
  desc: Attack modifier when on the offensive
```

### Land Defensive Stats

```yaml
defense:
  desc: Defense value when holding position

max_strength:
  desc: Maximum organization/strength

armor_value:
  desc: Armor protection level

hardness:
  desc: Damage reduction against soft attack (0-1)

entrenchment:
  desc: Bonus when entrenched
```

### Naval Equipment Stats

```yaml
naval_speed:
  desc: Base movement speed for naval units

lg_armor_piercing:
  desc: Light gun armor penetration

lg_attack:
  desc: Light gun attack value

hg_armor_piercing:
  desc: Heavy gun armor penetration

hg_attack:
  desc: Heavy gun attack value

torpedo_attack:
  desc: Torpedo damage

anti_air_attack:
  desc: Anti-aircraft attack value

sub_attack:
  desc: Attack bonus against submarines

sub_detection:
  desc: Submarine detection capability

surface_visibility:
  desc: How easily this ship is detected (LOWER = harder to detect)

sub_visibility:
  desc: Submarine detection difficulty (LOWER = harder to detect)

naval_range:
  desc: Maximum operational range

port_capacity_usage:
  desc: Port capacity consumed when docked
```

> [!CRITICAL] Surface and submarine visibility modifiers are INVERTED: lower values make the ship harder to detect, not easier. A ship with `surface_visibility = 1` is much easier to spot than one with `surface_visibility = 0.5`.

### Air Equipment Stats

```yaml
air_attack:
  desc: Air-to-air combat capability

air_defence:
  desc: Defense against air attacks

air_range:
  desc: Maximum operational range

air_agility:
  desc: Maneuverability in air combat

air_ground_attack:
  desc: Close air support effectiveness

air_bombing:
  desc: Strategic bombing effectiveness

air_superiority:
  desc: Air superiority mission effectiveness

naval_strike_attack:
  desc: Ship attack capability

naval_strike_targetting:
  desc: Hit chance against naval targets

carrier_size:
  desc: Deck space consumed on carriers

carrier_capable:
  desc: Boolean - can operate from carriers
```

### Obsolete Modifiers

These modifiers exist in older versions but are no longer functional:

```yaml
fire_range:
  status: obsolete
  note: No longer affects combat

shore_bombardment:
  status: obsolete
  replacement: Use lg_attack + hg_attack instead

evasion:
  status: obsolete
  replacement: Use naval_speed instead
```

Do not use these modifiers in new equipment definitions - they have no effect in current versions.

## Naval Shore Bombardment

Shore bombardment is a special naval mechanic:

```hoi4
lg_attack = 15
hg_attack = 25
```

Naval guns contribute to shore bombardment during land battles. The ship must be on a Hold mission in a sea province adjacent to the land battle.

The obsolete `shore_bombardment` modifier no longer works - use the light gun (`lg_attack`) and heavy gun (`hg_attack`) stats instead.

## Inheritance System

Equipment inheritance follows this priority:

1. **Specific equipment overrides:** Values defined in the specific equipment
2. **Archetype defaults:** Values from the archetype if not overridden
3. **Hardcoded defaults:** Engine defaults if neither specify (e.g., `maximum_speed = 4`)

Example inheritance chain:

```hoi4
# Archetype
infantry_equipment = {
    is_archetype = yes
    build_cost_ic = 10
    soft_attack = 20
    defense = 30
    maximum_speed = 4
}

# Specific equipment
infantry_equipment_2 = {
    archetype = infantry_equipment
    build_cost_ic = 12   # Overrides archetype
    soft_attack = 25     # Overrides archetype
    # defense = 30 (inherited from archetype)
    # maximum_speed = 4 (inherited from archetype)
}
```

## Localisation

Localisation files are in `localisation/english/*_l_english.yml`:

### Standard Keys

- `<equipment>`: Equipment name
- `<equipment>_desc`: Equipment description
- `<equipment>_short`: Short name for UI elements

### Country-Specific Keys

- `<TAG>_<equipment>`: Country-specific equipment name
- `<TAG>_<equipment>_desc`: Country-specific description

Country-specific localisation overrides standard localisation for that country, allowing custom naming for nation-specific equipment variants.

## Equipment Icons

Equipment icons use the naming pattern `GFX_<equipment>_medium`. If an equipment doesn't have its own icon defined, it automatically copies the icon from the technology that unlocks it.

This fallback system means you only need to define equipment icons when they differ from the unlocking technology's icon.

## Production and Unlocking

Equipment is unlocked by technologies using the `enable_equipments` block:

```hoi4
# In technology definition
enable_equipments = {
    infantry_equipment_1
    infantry_equipment_2
}
```

Once unlocked, equipment appears in the production menu and can be assigned to units.

Note that effects and history files can construct buildings and assign equipment before the relevant technologies are researched - tech requirements only block manual player actions, not scripted setup.

## Related Systems

For technology unlocking and research, see [Technologies Core](/database/technologies_core.md).

For unit templates and equipment assignment, see the units documentation.

For production and factories, see the production documentation.

For equipment conversion and upgrades, see the conversion documentation.
