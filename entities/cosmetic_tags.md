---
domain: entities
concept: cosmetic_tags
version: 1.14+
requires: [country_tags]
relates: [localisation, autonomy, country_history]
---

# Cosmetic Tag System

Cosmetic tags allow countries to change their display name, flag, map color, character portraits, and unit entities without affecting game mechanics. Countries can only have one cosmetic tag active at a time.

## Scope of Changes

Cosmetic tags modify:

- Country flag sprites
- Country display name
- Map color (political and UI modes)
- Random character names (for generated characters)
- Random character portraits (for generated characters)
- Unit entity models (visual appearance of units)

Cosmetic tags do not affect:

- Game mechanics or scripting logic
- National focus trees
- Event scripting and triggers
- Decision availability
- Country tags in triggers (still use base tag)

## Cosmetic Tag Effects

```hoi4
set_cosmetic_tag = COSMETICTAG

drop_cosmetic_tag = yes
```

The `set_cosmetic_tag` effect activates a cosmetic tag for the country. The `drop_cosmetic_tag` effect removes the active cosmetic tag and reverts to the base country appearance.

Only one cosmetic tag can be active per country. Setting a new cosmetic tag automatically drops any previous cosmetic tag.

## Flag System

Cosmetic flags follow a specific priority when rendering:

### Flag Priority Order

1. Base country ideology flag: `TAG_ideology.tga`
2. Cosmetic fallback flag: `COSMETICTAG.tga`
3. Cosmetic ideology flag: `COSMETICTAG_ideology.tga`

> [!CRITICAL] The fallback cosmetic flag (`COSMETICTAG.tga`) does not override ideology-specific base flags (`TAG_ideology.tga`). If the base country has ideology-specific flags defined, you must provide matching cosmetic ideology flags, or the base ideology flags will display instead of the cosmetic fallback.

**Example:** Germany has `GER_democratic.tga`, `GER_communism.tga`, and `GER_fascism.tga` flags. If a cosmetic tag `WEIMAR` only provides `WEIMAR.tga`, the game still renders `GER_democratic.tga` when Germany is democratic because the ideology-specific base flag takes priority over the cosmetic fallback.

**Solution:** Provide all ideology-specific variants:

```text
WEIMAR.tga
WEIMAR_democratic.tga
WEIMAR_communism.tga
WEIMAR_fascism.tga
WEIMAR_neutrality.tga
```

### Flag Format

Cosmetic flags use the same format as base country flags: 32-bit ARGB uncompressed TGA files with bottom-left origin. See [Country Tags](/entities/country_tags.md) for detailed flag format requirements.

## Map Colors

Map colors are defined in `common/countries/cosmetic.txt`:

```hoi4
COSMETICTAG = {
    color = rgb { 255 100 50 }
    color_ui = rgb { 200 80 40 }
}
```

The `color` attribute controls political map mode (F1), while `color_ui` controls the intelligence map (F10), history viewer, and division backgrounds.

Colors follow the same modifier system as base country colors: saturation multiplied by 0.6 and value multiplied by 0.8. Use values greater than 1.0 to achieve high saturation or value in the rendered result.

## Localization

Cosmetic tag localization uses the same key structure as base country tags:

```yaml
COSMETICTAG_ideology: "Cosmetic Country Name"
COSMETICTAG_ideology_ADJ: "Cosmetic Adjective"
COSMETICTAG_ideology_DEF: "the Cosmetic Country"
```

### Localization Priority

> [!CRITICAL] Cosmetic localization overrides base country localization even when the base localization is more specific. A generic cosmetic key (`COSMETICTAG`) takes priority over specific base keys (`TAG_autonomy_state_OVERLORD`).

This means cosmetic tags can inadvertently break subject naming or autonomy-specific names if not carefully implemented with full localization coverage.

**Automatic variations:** All automatic localization variations work with cosmetic tags:

- Subject names (`COSMETICTAG_subject`, `COSMETICTAG_OVERLORD_subject`)
- Autonomy names (`COSMETICTAG_autonomy_state`)
- Ideology subtypes (`COSMETICTAG_ideology_type`)

### Missing Localization Behavior

When the `_DEF` localization key is missing, the tooltip shows the country name unchanged but the cosmetic tag still applies for other purposes. Use `hidden_effect` around `set_cosmetic_tag` to suppress confusing tooltips when the visible name shouldn't change:

```hoi4
hidden_effect = {
    set_cosmetic_tag = COSMETICTAG
}
```

### Nested Strings

Nested localization strings (`$NONIDEOLOGY$`, `$OVERLORD$`, `$OVERLORDADJ$`) only work in subject names. These variables do not function in independent country names:

```yaml
# Works for subjects
COSMETICTAG_subject: "$NONIDEOLOGY$ Client State"

# Does NOT work for independent countries
COSMETICTAG: "$NONIDEOLOGY$ Republic"
```

## Random Character Names

Random character names for generated characters use files in `common/names/COSMETICTAG.txt`. These files follow the same format as base country name files:

```hoi4
COSMETICTAG = {
    male = {
        names = { "Name1" "Name2" "Name3" }
    }
    female = {
        names = { "Name1" "Name2" "Name3" }
    }
    surnames = { "Surname1" "Surname2" "Surname3" }
}
```

When a cosmetic tag is active, the game uses the cosmetic name file for generating random characters.

## Random Character Portraits

Random character portraits use the `portraits/` path structure. When a cosmetic tag is active, the game searches for portraits in cosmetic-specific directories before falling back to base country portraits.

Portrait assignment only occurs after country selection at game start. During country selection, characters without portraits show as silhouettes. The cosmetic tag affects which portrait pool is used for random generation.

## Unit Entities

Cosmetic tags can define custom unit entity models in `gfx/entities/*.asset`:

```hoi4
entity = {
    name = "COSMETICTAG_infantry_entity"
    clone = "GER_infantry_entity"
}
```

Entity names must follow the format `COSMETICTAG_<unit_type>_entity`. Entities can clone from any valid source including other countries' cosmetic entities.

> [!CRITICAL] There is no automatic fallback for missing entities. If a cosmetic tag is active but the required entity is undefined, the game uses the default engine entity, which may not match the intended visual style.

Define all necessary entities for each unit type when creating cosmetic tags:

```text
COSMETICTAG_infantry_entity
COSMETICTAG_armor_entity
COSMETICTAG_artillery_entity
# ... etc for all unit types
```

## On_Actions and Puppeting

The `on_ruling_party_change` on_action only fires after game start, not during initial scenario load. This limits its usefulness for automatically applying cosmetic tags at game start.

### Puppeting Detection

Cosmetic tags have limited automatic application for puppeting. The system only detects puppeting through:

- Peace conference puppeting
- The `release_country` effect

Manual `puppet` or `set_autonomy` effects do not trigger automatic cosmetic tag application.

**Workaround:** Include `set_cosmetic_tag` in the same effect block as the puppeting effect:

```hoi4
puppet = {
    target = TAG
    end_wars = no
}
set_cosmetic_tag = TAG_PUPPET
```

This ensures the cosmetic tag applies immediately alongside the puppeting effect rather than waiting for an on_action that may never fire.

### Subject History Files

When setting autonomy in history files, include cosmetic tags explicitly:

```hoi4
# In subject's history file
set_autonomy = {
    target = TAG
    autonomy_state = autonomy_puppet
}

set_cosmetic_tag = TAG_PUPPET
```

Place cosmetic tag effects after autonomy effects to ensure they apply in the correct order. See [Autonomy](/entities/autonomy.md) for autonomy system details.

## Common Patterns

### Exile Governments

Cosmetic tags are commonly used for exile governments:

```hoi4
FRA = {
    if = {
        limit = {
            has_government = democratic
            NOT = { controls_state = 16 }  # Île-de-France
        }
        set_cosmetic_tag = FRA_EXILE
    }
}
```

The cosmetic tag changes the flag and name to reflect the government-in-exile status while maintaining all of France's focuses, events, and mechanics.

### Civil Wars

Civil war factions often use cosmetic tags to differentiate sides while sharing the same base country scripting:

```hoi4
# Nationalist Spain
set_cosmetic_tag = SPA_NATIONALIST

# Republican Spain (base tag)
# No cosmetic tag, uses base SPA
```

### Puppet States

Subject nations frequently use cosmetic tags to reflect their subordinate status:

```hoi4
set_autonomy = {
    target = FRA
    autonomy_state = autonomy_puppet
    freedom_level = 0.3
}
set_cosmetic_tag = FRA_VICHY
```

## Related Systems

For base flag format requirements and color modifiers, see [Country Tags](/entities/country_tags.md).

For autonomy state setup and subject mechanics, see [Autonomy](/entities/autonomy.md).

For character portrait systems and random generation, see [Characters](/entities/characters.md).
