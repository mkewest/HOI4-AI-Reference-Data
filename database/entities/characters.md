---
domain: entities
concept: characters
version: 1.14+
requires: [country_tags, ideologies]
relates: [portraits, country_history]
---

# Character System

Characters represent individual people in HOI4 including country leaders, military commanders, government advisors, and intelligence operatives. Characters are defined in `common/characters/*.txt` and recruited into service through country history files or scripted effects.

## Character Definition Structure

Characters are defined within a `characters = { ... }` wrapper block:

```hoi4
characters = {
    character_id = {
        name = "CHARACTER_NAME"
        portraits = { ... }
        country_leader = { ... }
        corps_commander = { ... }
        advisor = { ... }
    }
}
```

Each character has a unique identifier (`character_id`) used for recruitment and scoping.

## Core Attributes

### Name

```hoi4
name = "CHARACTER_NAME"
```

The name attribute uses a localization key that resolves to the character's display name. Literal strings can be used but localization keys are recommended for language support.

### Gender

```hoi4
gender = female
```

Valid values are `female`, `male`, or `undefined`. When undefined, the character behaves identically to male in almost all contexts. The undefined value only affects dynamic character generation with random gender assignment based on `FEMALE_UNIT_LEADER_BASE_CHANCE` defines.

### Portraits

```hoi4
portraits = {
    civilian = {
        large = "GFX_portrait_character_large"
        small = "GFX_portrait_character_small"
    }
    army = {
        large = "GFX_portrait_character_army"
        small = "GFX_portrait_character_army_small"
    }
}
```

Portrait categories are `civilian`, `army`, and `navy`. Each category supports `large` and `small` sizes. The game automatically generates `_small` variants by appending the suffix if only the base sprite is defined (e.g., `GFX_portrait` auto-creates `GFX_portrait_small`).

> [!CRITICAL] Army portraits require explicit `_small` variants for the officer corps system to function correctly. While auto-suffixing works for other contexts, officer corps specifically needs the small variant defined.

**Political portraits:** Country leader portraits must use ideology group nesting:

```hoi4
portraits = {
    civilian = {
        large = {
            "GFX_portrait_default"
            democratic = "GFX_portrait_democratic"
            communism = "GFX_portrait_communism"
        }
    }
}
```

Navy, army, and operative portraits do not use ideology group nesting.

**Random portraits:** Characters without defined portraits use random generation from the country's portrait pool. This random assignment only occurs after country selection at game start. During country selection, undefined portraits show as silhouettes.

Partial portrait definitions (e.g., defining only `large` but not `small`) prevent random generation from filling in missing variants. Either define all variants explicitly or define none to allow full random generation.

**Portrait sprite priority:** When multiple mods or files define sprites with the same name, later ASCII filenames overwrite earlier definitions. Portrait sprite evaluation follows alphabetical filename order.

## Character Roles

Characters can hold multiple roles simultaneously. Each role type has specific attributes and behavior.

### Country Leader Role

```hoi4
country_leader = {
    ideology = socialism
    expire = "1965.1.1"
    desc = "LEADER_DESC"
    traits = { trait_token }
}
```

**Ideology:** Country leaders use ideology types (sub-ideologies like `socialism` or `marxism`), not ideology groups (like `communism`). See [Ideologies](/entities/ideologies.md) for the type versus group distinction.

**Party leadership:** The first recruited character per ideology group automatically becomes that party's leader. If `set_politics` executes before character recruitment and no leader exists for the ruling party, the game generates a random character as party leader.

**Expiration:** The `expire` attribute sets a date when the leader automatically steps down. This is optional and leaders can serve indefinitely if omitted.

**Description:** The `desc` attribute is mandatory and uses a localization key for the leader's biographical description shown in the politics screen.

### Advisor Role

```hoi4
advisor = {
    slot = political_advisor
    idea_token = advisor_unique_token
    traits = { trait_token }
    cost = 150
    can_be_fired = yes
    
    allowed = {
        original_tag = GER
    }
    
    available = {
        NOT = { has_country_flag = advisor_unavailable }
    }
    
    on_add = {
        # Character scope, not country scope
        owner = {
            # Country scope
            add_political_power = 50
        }
    }
    
    visible = {
        has_government = fascism
    }
}
```

> [!CRITICAL] The `idea_token` attribute is mandatory for advisors. Missing or null idea tokens cause all tokenless advisors to disappear from the country. Each advisor must have a unique idea token.

**Idea token usage:** Triggers and effects reference advisors using their `idea_token`, not their `character_id`. For example, `activate_advisor = idea_token`, not `activate_advisor = character_id`.

**Available slots:** Political advisors use `political_advisor`, while high command and military staff use: `army_chief`, `navy_chief`, `air_chief`, `high_command`, `theorist`.

**Scripted attributes:** Advisors support `allowed`, `available`, `visible`, and `on_add`/`on_remove` effects. The `add_advisor_role` effect cannot include these scripted attributes - they must be in the original character definition.

**Scope in callbacks:** The `on_add` and `on_remove` blocks execute in character scope, not country scope. Use `owner = { ... }` to access the recruiting country's scope.

> [!CRITICAL] `remove_advisor_role` permanently deletes all scripted attributes (`visible`, `available`, `on_add`, etc.). These cannot be restored by re-adding the role. Use `visible = { ... }` with country flags instead of dynamically removing and re-adding advisor roles.

**Dynamic availability:** Use the `visible` trigger to conditionally show/hide advisors rather than removing and re-adding roles. This preserves all scripted attributes and avoids the permanent data loss from `remove_advisor_role`.

### Unit Leader Roles

Unit leaders include corps commanders, field marshals, and naval commanders.

```hoi4
corps_commander = {
    skill = 3
    attack_skill = 4
    defense_skill = 3
    planning_skill = 2
    logistics_skill = 3
    
    traits = { trait_token }
    
    allowed = {
        original_tag = GER
    }
}

field_marshal = {
    skill = 4
    attack_skill = 5
    defense_skill = 4
    planning_skill = 3
    logistics_skill = 2
    
    traits = { trait_token }
}

navy_leader = {
    skill = 2
    attack_skill = 3
    defense_skill = 2
    maneuvering_skill = 4
    coordination_skill = 3
    
    traits = { trait_token }
}
```

**Skill effects:**

For army leaders, the base `skill` attribute has no direct gameplay effect beyond being a prerequisite for certain traits.

For naval leaders, each point of `skill` provides +5% hit chance and +2% coordination. Coordination bonuses scale non-linearly: the 1st point grants +1%, while the 6th point grants +3%.

**Army skills:** `attack_skill` provides +2.5% offense per point, `defense_skill` provides +2.5% defense per point. `planning_skill` and `logistics_skill` only apply to army leaders.

**Navy skills:** `attack_skill` provides +5% damage per point, `defense_skill` provides +5% defense per point. `maneuvering_skill` and `coordination_skill` only apply to navy leaders.

**Field marshal mechanics:** When a field marshal directly commands divisions (not through subordinate generals), the `corps_commander_modifier` from their traits applies, not the `field_marshal_modifier`. When leading other generals, the `field_marshal_modifier` applies instead.

**Allowed trigger:** The `allowed` trigger checks in unit leader scope with `FROM` as the recruiting country. This enables conditional availability based on DLC, country tag, or other recruitment context.

## Character Recruitment

Characters are recruited in country history files or through scripted effects:

```hoi4
recruit_character = character_id
```

> [!CRITICAL] The `recruit_character` command must not be the last line in a file. At least one line (even a blank line or comment) must follow it, or recruitment silently fails.

Recruitment timing matters for country leadership. Always recruit characters before `set_politics` to ensure recruited leaders become party leaders rather than randomly generated characters.

## Character Management Effects

### Role Addition

```hoi4
add_country_leader_role = {
    country_leader = {
        ideology = fascism
        expire = "1965.1.1"
    }
}

add_corps_commander_role = {
    traits = { trait_token }
    skill = 3
    attack_skill = 4
    defense_skill = 3
}

add_field_marshal_role = { ... }
add_naval_commander_role = { ... }

add_advisor_role = {
    advisor = {
        slot = political_advisor
        idea_token = token
        cost = 150
    }
}
```

Role addition effects allow dynamically granting new roles to characters. Note that `add_advisor_role` cannot include scripted attributes like `visible`, `available`, or `on_add` - these must exist in the original character definition.

### Character Promotion

```hoi4
promote_character = character_id
```

The `promote_character` effect can execute in either character scope or country scope. It promotes the character to party leader for their ideology group, replacing the current leader.

Use `promote_character` between scenario start dates to ensure new leaders take over when transitioning from earlier bookmarks.

### Character Retirement

```hoi4
retire_character = yes
```

Character retirement removes the character from active service but does not delete them. Retired characters remain in the same country for scoping purposes and can be brought back via `set_nationality`.

The legacy effects `retire_country_leader` and `retire_ideology_leader` only remove characters from leadership succession but do not remove the character entirely. These effects are deprecated in favor of `retire_character`.

Similarly, `kill_country_leader` and `kill_ideology_leader` behave as retirement rather than permanent deletion and are reversible via `set_nationality`.

### Advisor Activation

```hoi4
activate_advisor = idea_token
```

The `activate_advisor` effect uses the advisor's `idea_token`, not their `character_id`. This distinction is critical for scripting.

### Portrait Changes

```hoi4
set_portraits = {
    civilian = {
        large = "GFX_new_portrait"
    }
}
```

The `set_portraits` effect can execute in character scope or country scope (affecting the country leader). It dynamically changes portrait sprites for specific categories.

## Character Instances

Character instances enable conditional character definitions based on DLC or other factors:

```hoi4
character_id = {
    name = "CHARACTER_NAME"
    
    instance = {
        allowed = {
            has_dlc = "La Resistance"
        }
        
        advisor = {
            slot = political_advisor
            idea_token = token_with_dlc
        }
    }
    
    instance = {
        allowed = {
            NOT = { has_dlc = "La Resistance" }
        }
        
        advisor = {
            slot = political_advisor
            idea_token = token_without_dlc
        }
    }
}
```

> [!CRITICAL] The `allowed` trigger in instances only checks at game start, not dynamically. If a single instance exists without an `allowed` trigger, it is useless because the character will never take it (always preferring instances with `allowed = { ... }`).

Characters automatically take all instances where `allowed = { always = yes }`. Multiple instances can be active simultaneously if their `allowed` conditions are all true.

## Generated Characters

The `generate_character` effect creates characters dynamically from templates:

```hoi4
generate_character = {
    token_base = generated_character
    name = random
    portraits = {
        army = {
            large = "GFX_generic_portrait"
        }
    }
    
    advisor = {
        slot = political_advisor
        idea_token = custom_token  # Final token: generated_character_custom_token
    }
}
```

> [!CRITICAL] The character template referenced by `token_base` must exist in country history files before the `generate_character` effect can be used in mid-game events or decisions. The game requires the template definition at initialization.

**Idea token assembly:** If `idea_token` is specified in the generated advisor role, the full token becomes `token_base + "_" + idea_token`. If `idea_token` is omitted, it defaults to the slot name (e.g., `generated_character_political_advisor`).

**Name generation:** When `name = random`, the game selects from the country's random name pool. Explicit localization keys can be provided instead.

**Bypassing recruitment:** Wrap the character definition in `always = no` triggers in history files to define templates without recruiting them:

```hoi4
if = {
    limit = { always = no }
    
    recruit_character = template_character
}
```

## Trait System

Character traits are defined separately in `common/country_leader/*.txt` and `common/unit_leader/*.txt`.

**Trait sprites:** Country leader and advisor traits use `GFX_idea_traits_strip` with frame numbers. The `noOfFrames` attribute must match if the strip image is changed, otherwise frame indexing breaks.

Unit leader traits use individual sprites named `GFX_trait_<name>`. The exception is traits with names starting with `trait_` (e.g., `trait_example`), which use `GFX_trait_example` without doubling the prefix.

> [!CRITICAL] Base game `ideas.gfx` files should not exist in mods. These files break during game updates when new traits are added to the base game. Reference trait sprites through custom `.gfx` files or rely on base game definitions.

### Trait Experience

Traits can have experience requirements for selection:

```hoi4
trait_token = {
    cost = 1000
    gain_xp = {
        # Checked in combatant scope
        always = yes
    }
    gain_xp_leader = {
        # Checked in unit_leader scope
        always = yes
    }
}
```

The `gain_xp` trigger checks in combatant scope (during combat), while `gain_xp_leader` checks in unit_leader scope (applies to the leader's XP pool).

The `trait_xp_factor` modifier is multiplicative: a value of `0.1` means +10% more XP (not 10% of XP).

### Scientist Role

Scientists attach to characters to drive Special Projects.

```hoi4
my_character_token = {
    scientist = {
        desc = desc_loc_key            # optional flavor description
        traits = { trait_token }       # scientist trait DB (or country leader traits until DB exists)
        skills = { specialization = 2 }# per-specialization skill overrides (default 1)
        visible = { ... }              # optional trigger to gate visibility; ROOT = character
    }
}
```

- **desc**: Localisation key for flavor.
- **traits**: Scientist-specific or shared traits.
- **skills**: Per-specialization starting levels; unspecified default to 1.
- **visible**: Optional trigger controlling whether the scientist role is shown/usable.

### Scientist Traits

Scientist traits are defined in the scientist trait database and apply to Special Projects only.

Example:

```hoi4
my_scientist_trait_token = {
    name = name_loc_key        # optional; otherwise uses the token loc key
    icon = GFX_icon            # optional; otherwise uses GFX_<token>

    modifier = {               # applies to the special project the scientist is attached to
        special_project_prototype_speed_factor = 0.5
    }

    specialization = { specialization_land }  # optional: restrict to specializations; omit for all

    available = {              # optional availability trigger; FROM/ROOT/PREV in country scope
        has_dlc = "No Step Back"
        ROOT = { has_tech = tech_engineers }
    }
}
```

Guidelines:
- Use modifiers relevant to Special Projects.
- Gate via `available` when DLC/tech/theme restrictions apply.
- Provide icons/names or rely on token defaults (`GFX_<token>`, `<token>` loc key).

## Legacy Systems

### Legacy ID

The `legacy_id` attribute is deprecated from the pre-1.12 character system. Modern character triggers should be used instead of legacy ID-based references.

### Removal Cost

The `removal_cost = -1` pattern for unfirable advisors is deprecated. Use `can_be_fired = no` instead.

### Retirement Effects

The effects `retire_country_leader`, `retire_ideology_leader`, `kill_country_leader`, and `kill_ideology_leader` only remove characters from leadership succession rather than deleting them. These are legacy effects maintained for backwards compatibility. Use `retire_character` and `set_nationality` for modern character management.

## Character Scope Usage

Characters maintain scope relationships with their owning country:

- Advisor `on_add`/`on_remove` execute in character scope; use `owner` scope for country effects
- Unit leader `allowed` checks in unit leader scope with `FROM = recruiting_country`
- Retired characters remain in their country for scoping even after retirement
- Characters can change nationality via `set_nationality`, which moves them between countries

## Related Defines

- `FEMALE_UNIT_LEADER_BASE_CHANCE`: See [NAI](/defines_list/NAI.md)
- `ARMY_LEADER_XP_GAIN_PER_SKILL`: See [NMilitary](/defines_list/NMilitary.md)
