---
domain: content
concept: ai_strategy
version: 1.14+
requires: [triggers, modifiers, strategic_regions]
relates: [national_focus, division_template, equipment]
---

# AI Strategy System

The AI strategy system controls automated decision-making for computer-controlled countries through strategy plans, AI areas, equipment designs, division templates, and peace conference behavior.

## AI Strategy Plans

Strategy plans are defined in `common/ai_strategy_plans/*.txt` and assign strategic behaviors to countries:

```hoi4
my_strategy_plan = {
    name = "Internal reference only"
    desc = "Never needs localization"
    
    enable = {
        # Checked daily - once true, permanently assigned
    }
    
    abort_when_not_enabled = yes
    
    ai_national_focuses = {
        TAG_focus_1
        TAG_focus_2
        TAG_focus_3
    }
    
    focus_factors = {
        TAG_other_focus = 2.0
        TAG_bad_focus = 0
    }
    
    weight = {
        base = 10
        # Multiplies ALL factors in plan
    }
}
```

**enable**: Trigger checked daily. Once this evaluates true, the plan assigns permanently to the country unless an abort trigger fires. Does not auto-abort when the enable trigger becomes false unless `abort_when_not_enabled = yes` is specified.

**abort_when_not_enabled**: Boolean that causes the plan to abort when `enable` becomes false after initial assignment.

**ai_national_focuses**: Array of focus IDs the AI should prioritize in order. The AI completely ignores `ai_will_do` values on focuses until all listed focuses are taken or unavailable.

**focus_factors**: Modifiers for focus selection when `ai_national_focuses` is exhausted or empty. A factor of 0 makes a focus never picked unless it appears in `ai_national_focuses`. Factors multiply the generated random value during AI focus selection.

**weight**: MTTH block that determines plan selection when multiple plans have enable = true. Multiplies all factors in the plan.

**name** and **desc**: Internal references visible only through the `aiview` console command. Never require localization.

## AI Strategy Types

Individual strategies modify specific AI behaviors and are defined in `common/ai_strategy/*.txt`:

```hoi4
strategy_type = {
    allowed = {
        # Checked ONLY at game start
    }
    
    enable = {
        # Continuous check
    }
    
    reversed = yes  # For some strategy types
    
    value = 100
    
    # Strategy-specific attributes
}
```

**allowed**: Trigger evaluated only at game start. Use this exclusively for immutable conditions like DLC checks or permanent country attributes. Changes after game start have no effect.

**enable**: Trigger checked continuously during gameplay. Controls strategy activation.

### AI Areas

AI areas define geographic regions for strategic planning:

```hoi4
ai_area_my_region = {
    continents = { europe asia }
    strategic_regions = { 42 43 44 }
}
```

Provinces qualify for an AI area if they are in any specified continent OR any specified strategic region (OR logic, not AND). Multiple AI areas can contain the same province - they are not mutually exclusive. Debug mode hover displays all AI areas containing a province.

### Common Strategy Types

**dont_defend_ally_borders**: Strictly binary. Any positive total value means the AI never defends that ally's borders. Not graduated - even a value of 0.01 triggers the effect.

**protect**: Controls guarantee behavior. Negative total values prevent the AI from ever guaranteeing that country, regardless of other factors.

**naval_mission_threshold**: Counterintuitively, higher values make naval missions less likely. This threshold determines minimum fleet strength requirements before assigning missions.

**diplo_action_acceptance**: Modifies AI acceptance of diplomatic proposals from others. Does not make the AI propose actions, only accept them.

**diplo_action_desire**: Modifies AI desire to propose diplomatic actions. Does not affect acceptance of proposals from others.

**dont_join_wars_with**: Prevents joining wars directly with the specified country. Does not prevent joining the same war through different ally connections.

**front_control**: Modifies existing frontline behavior only. Does not create new frontlines. When multiple target types are specified (e.g., both strategic_region and country), all conditions must be met (AND logic).

**front_unit_request**: Similar to front_control. Multiple target types use AND logic - all conditions must be met.

**build_building**: Completely ignored if the specified building is already under construction in any province/state.

**role_ratio**: Affects both AI division templates and AI equipment (ships/planes/tanks). The same role_ratio value influences unit composition and equipment production priorities.

**research_weight_factor**: Value represents percentage modification. A value of 50 means +50% research weight, -30 means -30% weight.

### Reversed Strategies

Some strategy types support `reversed = yes`, which inverts their logic. Reversed strategies have no default scope and must specify targets explicitly.

## AI Focus Modifiers

Focus selection factors modify AI focus priorities and are defined in `common/ai_focuses/*.txt`:

```hoi4
ai_focus_<type>_factor = {
    modifier = {
        factor = 1.5
        # Conditions
    }
}
```

These modifiers apply after the game's default focus value calculations. Peace status applies a 0.75 multiplier before country-specific modifiers evaluate.

Country-specific overrides use the format `ai_focus_<type>_<TAG>` and completely replace the generic version - they do not merge or stack.

### Default Focus Calculations

Fascist countries have different default values for certain focus types:

- aggressive: 75 (vs 50 for others)
- war_production: 30 (vs 10 for others)

Focus types naval, naval_air, and aviation default to large negative values (-999) when the country lacks necessary infrastructure like dockyards or airfields.

The military_advancements focus type scales with research slots: `25 * research_slots` with a cap of 100.

## AI Templates

Division templates guide AI army composition and are defined in `common/ai_templates/*.txt`:

```hoi4
my_template_role = {
    roles = { infantry }
    
    blocked_for = { TAG1 TAG2 }
    available_for = { TAG3 TAG4 }
    
    upgrade_prio = {
        base = 5
        # Weighted-random selection at role level
    }
    
    my_specific_template = {
        reinforce_prio = 1  # 0=garrison, 1=normal, 2=elite
        
        custom_icon = 12
        
        division_names_group = my_group  # Defaults to branched template
        
        upgrade_prio = {
            base = 10
            # Deterministic selection at template level
        }
        
        enable = {
            # Trigger for template availability
        }
        
        can_upgrade_in_field = {
            # Trigger for field upgrades
        }
        
        target_template = {
            support = {
                recon = 1
                engineer = 1
            }
            regiments = {
                infantry = 9
                artillery = 1
            }
        }
        
        replace_at_match = 0.8  # Triggers at 80% match
        replace_with = better_template
        target_min_match = 0.5  # Required for replacement
    }
}
```

> [!CRITICAL] The AI never modifies templates in-place. It always creates copies when upgrading or modifying templates. This prevents unexpected changes to player-designed templates.

**upgrade_prio**: At role level, uses weighted-random selection. At template level, uses deterministic selection (highest priority wins).

**reinforce_prio**: Controls priority tiers. 0 = garrison units, 1 = normal units, 2 = elite units. Affects reinforcement and equipment allocation.

**replace_at_match**: Triggers template replacement when match score reaches this threshold (1.0 = 100% match). Replacement only occurs if `target_min_match` is also met.

**target_min_match**: Minimum match score required for replacement eligibility. Both `replace_at_match` and this threshold must be met.

**division_names_group**: Inherits from the branched-from template if unspecified, preserving naming conventions.

The same role can have multiple target templates. The highest priority template determines AI build choices.

## AI Equipment

Equipment designs guide AI variant creation for ships, planes, and tanks. Defined in `common/ai_equipment/*.txt`:

```hoi4
my_equipment_role = {
    category = naval  # naval, air, or land
    
    roles = { fleet_carrier escort_carrier }
    
    available_for = { TAG1 TAG2 }
    blocked_for = { TAG3 }
    
    priority = {
        base = 10
    }
    
    my_variant_design = {
        name = "Carrier Design Alpha"
        
        role_icon_index = 3  # Ships only
        
        priority = {
            base = 50
        }
        
        enable = {
            # Trigger for design availability
        }
        
        allowed_types = { ship_hull_carrier }
        
        target_variant = {
            match_value = 2000
            type = ship_hull_carrier
            
            modules = {
                fixed_ship_deck_slot_1 = ship_deck_space
                fixed_ship_anti_air_slot = ship_anti_air_2
                mid_1_custom_slot = ship_armor_light
                fixed_ship_engine_slot = carrier_ship_engine_2
            }
            
            upgrades = {
                ship_reliability_upgrade = 2
                carrier_armor_upgrade = {
                    base = 1
                    # Can use MTTH block
                }
            }
        }
        
        requirements = {
            module = ship_deck_space
            module = carrier_ship_engine_2
        }
        
        allowed_modules = {
            ship_anti_air_3
            ship_anti_air_2
            ship_anti_air_1
        }
    }
}
```

> [!CRITICAL] The AI creates one variant per role listed in the `roles` array. Multiple roles produce multiple variants from the same design template.

### Module Slot Syntax

**>MODULE**: Slot must contain a module newer than (by year) the specified module.

**<MODULE**: Slot must contain a module older than the specified module.

**>empty**: Slot must not be empty.

**any_of**: Array of acceptable modules for the slot (OR logic).

**upgrade = current**: Locks the slot during variant upgrades - keep current module.

**upgrade = >current**: Forces upgrade of that slot to a newer module during variant upgrades.

**requirements**: Modules that must exist somewhere in the design, not tied to specific slots. Just verifies presence.

**allowed_modules**: Ordered array determining priority. First module has highest priority during selection.

**role_icon_index**: Only functions for naval equipment. Controls ship role icon display.

## AI Peace Conference (1.14+)

Peace conference AI is defined in `common/peace_conference/ai_peace/*.txt` for version 1.14 and later:

```hoi4
my_peace_ai = {
    enable = {
        # Multiple enable blocks can be true simultaneously
    }
    
    peace_action_type = {
        # liberate, puppet, take_states, force_government, take_navy
    }
    
    ai_desire = 500  # Range: -1000 to 1000
}
```

**Scopes**:

- ROOT = winner country
- FROM = country undergoing the action (may be non-existent for liberation/puppeting)
- FROM.FROM.FROM = state being affected

> [!CRITICAL] Controller refers to the pre-conference occupier, not current owner. Owner refers to the original pre-war owner, not current controller. FROM can represent a non-existent country about to be created through liberation or puppeting.

Multiple enable blocks can evaluate true simultaneously. The AI weights all enabled options and selects based on desire values.

**take_navy** peace action has zero AI modding support - only player cost modifiers are available with the BBA DLC.

## AI Peace Conference (Pre-1.12)

Legacy peace AI system in `common/ai_peace/*.txt` for versions before 1.12:

```hoi4
my_peace_ai = {
    enable = {
        # First matching enable wins
    }
    
    # Temp variables available:
    # taken_states@TAG, taken_by@STATE, current_states@TAG
    # subject_states@TAG, subject_countries@TAG
    # subjected_by@STATE, subjected_by@TAG
    # liberate_states@TAG, liberate_countries@TAG
}
```

Files load in ASCII-sorted order. The first matching `enable` trigger wins at game start. Once assigned, that AI persists for the entire peace conference.

**Scopes**:

- ROOT = winner country
- FROM = loser country

Temp variables persist across peace actions within the same conference, allowing the AI to track decisions and states across multiple selections.

## MTTH Block Evaluation

MTTH blocks in AI systems follow specific evaluation rules:

Event options use probability-proportional-to-size sampling with d100 rolls. Operations apply in order: base operations first, then factor multiplications, then additions.

Temp variables in MTTH blocks require the value-modifying argument to come after the variable definition for proper evaluation.

All MTTH blocks start at value 1 before any modifications apply.

## Related Defines

- `NAI.FOCUS_TREE_CONTINUE_FACTOR`: AI same-branch focus continuation bonus
- `NAI.*`: Various AI behavior constants affecting strategy execution
