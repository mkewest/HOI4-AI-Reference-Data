---
domain: assets
concept: portraits
version: 1.14+
requires: [sprites, characters]
relates: [countries, ideologies]
---

# Portrait System

Portraits display character images for leaders, advisors, and commanders. The system uses priority-based selection with gender and ideology fallbacks defined in `interface/*.gfx` files.

## Portrait Priority

Portrait definitions use a three-tier priority system:

1. **Tag-specific**: Country-specific portraits (e.g., USA-specific generals)
2. **Continent-based**: Regional portraits (e.g., European portraits)
3. **Default**: Universal fallback portraits

When multiple definitions match a character, tag-specific definitions override continent definitions even when both match. Continent definitions override default. Evaluation order is always: tag > continent > default.

Example priority structure:

```hoi4
spriteTypes = {
    # Default portraits - lowest priority
    portraits = {
        default = {
            male = {
                "gfx/leaders/generic_male_1.dds"
                "gfx/leaders/generic_male_2.dds"
            }
        }
    }
    
    # Continent portraits - medium priority
    portraits = {
        europe = {
            male = {
                "gfx/leaders/europe_male_1.dds"
            }
        }
    }
    
    # Tag portraits - highest priority
    portraits = {
        GER = {
            male = {
                "gfx/leaders/germany_male_1.dds"
            }
        }
    }
}
```

A German (GER) male leader uses the tag-specific portrait. A French male leader uses the Europe continent portrait. An American male leader uses the default portrait.

## Gender Fallback

Top-level `male` and `female` definitions apply to all leader types when specific gender definitions are not provided for individual leader categories. Specific type definitions take precedence over top-level when both are present.

```hoi4
portraits = {
    USA = {
        male = {
            "gfx/leaders/usa_generic_male.dds"
        }
        
        army = {
            male = {
                "gfx/leaders/usa_army_male.dds"
            }
        }
    }
}
```

In this structure, USA army leaders use the army-specific male portrait while navy and air force leaders fall back to the top-level male portrait. This enables shared generic portraits with specialized overrides for specific branches.

## Portrait Categories

Leader types with distinct portrait pools:

- `army`: Army generals and field marshals
- `navy`: Naval commanders and admirals  
- `air`: Air force commanders
- `political`: Political leaders and heads of state
- `advisor`: Political advisors and ministers
- `operative`: Intelligence operatives

Each category can have separate portrait definitions with gender sub-blocks. Categories without defined portraits fall back to top-level gender definitions, which fall back to default portraits.

## Ideology-Specific Portraits

Political portraits require ideology sub-scope within the political category:

```hoi4
portraits = {
    USA = {
        political = {
            democratic = {
                male = {
                    "gfx/leaders/usa_democratic_leader.dds"
                }
            }
            communism = {
                male = {
                    "gfx/leaders/usa_communist_leader.dds"
                }
            }
        }
    }
}
```

Political leaders display portraits matching their ideology. Cannot use generic political block without ideology specification - the game requires ideology-scoped portrait definitions for political leaders.

## Portrait Pools

Multiple portrait paths in the same definition create random selection pools:

```hoi4
portraits = {
    GER = {
        army = {
            male = {
                "gfx/leaders/ger_general_1.dds"
                "gfx/leaders/ger_general_2.dds"
                "gfx/leaders/ger_general_3.dds"
                "gfx/leaders/ger_general_4.dds"
            }
        }
    }
}
```

The game randomly selects from the pool on leader generation or replacement. Each time a new German army general is created, one of the four portraits is chosen randomly. This creates variety without requiring unique portrait assignments for every leader.

Empty path blocks indicate no portraits available for that category:

```hoi4
portraits = {
    USA = {
        operative = {
            male = {}
        }
    }
}
```

Empty blocks prevent fallback to default portraits, forcing the category to have no portraits at all.

## GFX Dependency

> [!CRITICAL] Portrait images must be declared in sprite definitions (typically `interface/*_random_portraits.gfx` files) or the game silently fails to display them. No error message appears for missing GFX definitions - portraits simply don't render in-game.

The portrait system references sprite names, not file paths directly:

```hoi4
# In interface/generic_portraits.gfx
spriteTypes = {
    spriteType = {
        name = "GFX_portrait_generic_male_1"
        texturefile = "gfx/leaders/generic_male_1.dds"
    }
}

# In portraits definition
portraits = {
    default = {
        male = {
            "GFX_portrait_generic_male_1"
        }
    }
}
```

The sprite definition connects the portrait reference to the actual texture file. Without this link, portrait paths resolve to nothing and characters appear without portraits.

## Related Systems

Portraits integrate with character definitions for leader assignments, country files for tag-specific portraits, and ideology systems for political leader images. See sprite definitions for texture loading and interface system for portrait display contexts.
