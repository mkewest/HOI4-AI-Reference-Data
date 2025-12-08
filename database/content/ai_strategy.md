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

## AI Bonus Weights

AI bonus weights live in `common/ai_bonus_weights/*.txt` and layer multiplicative or additive factors on AI choices (research, production, decisions, peace, naval priorities, etc.). Keep naming consistent with the consuming systems to avoid silent zeros.

> [!NOTE] Missing or malformed weights are treated as zero. Provide defensive defaults for DLC-gated or optional content so AI behaviors do not collapse when data is absent.

### Common fields
- **enable**: Trigger gating the weight entry.
- **weights**: Named weights used downstream (e.g., research_air, production_navy). Units should match the consumer (usually multipliers).
- **fallbacks**: Explicit neutral weights (1.0 for multipliers, 0 for additive) to prevent unintended suppression.

### Small example

```hoi4
ai_bonus_weight_example = {
    enable = { has_dlc = "By Blood Alone" }
    weights = {
        research_air = 1.25
        research_navy = 0.9
    }
}
```

### AI Areas

AI areas define geographic regions for strategic planning:

```hoi4
ai_area_my_region = {
    continents = { europe asia }
    strategic_regions = { 42 43 44 }
}
```

Provinces qualify for an AI area if they are in any specified continent OR any specified strategic region (OR logic, not AND). Multiple AI areas can contain the same province - they are not mutually exclusive. Debug mode hover displays all AI areas containing a province.

## AI Faction Theaters

Faction theaters (`common/ai_faction_theaters/*.txt`) partition strategic regions into AI-manageable buckets shared across a faction.

Key fields:
- **regions**: Strategic region list defining the theater footprint.
- **preferred_countries**: Countries the theater is optimized around to prioritize allied fronts.
- **can_skip_first_region**: Allows starting from later regions when the first is invalid or already secured.
- **ai_will_do / cancel**: MTTH-style blocks controlling adoption or abandonment.
- **connectivity**: Hints for linking adjacent theaters for fronts/naval presence.

Debugging: `imgui ai theaters` and aiview overlays surface membership and weight decisions.

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

## Naval AI Objectives

Naval AI objectives live in `common/ai_navy/*.txt` (1.14+) and drive fleet assignment and mission weighting.

Key fields:
- **enable**: Gating trigger (checked continuously).
- **objective_type**: Objective category (e.g., convoy_raiding, naval_supremacy, invasion_support).
- **priority**: MTTH block; higher values win. Keep ranges stable across objectives to avoid oscillation.
- **regions / target**: Strategic regions or scripted targets for the objective scope.
- **ai_will_do**: Additional weighting hooks for situational boosts or suppression.

Debugging:
- `imgui show ai_navy` to inspect objective scores and assignments.
- Check that naval supremacy targets align with invasion paths; mismatched regions produce idle fleets.

Links:
- Uses defines in `defines_list/NAI.md` and `defines_list/NNavy.md` for thresholds and weighting.

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

### 2024-11 template notes
- **Role-level entries first**: The AI picks a role, then a template; keep role coverage complete to avoid empty production.
- **upgrade_prio / enable / replace_with**: Use to guide field upgrades; `target_template` plus `replace_at_match`/`target_min_match` control when swaps occur.
- **Field upgrades**: `can_upgrade_in_field` gates upgrades in active divisions; avoid triggers that constantly flip states.
- **Debugging**: `imgui show ai templates` surfaces role matches and template scores; keep priorities stable to avoid churn.

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

### 2024-11 equipment notes
- **priority blocks**: Use MTTH blocks for both design-level `priority` and per-variant `priority` to create clear ordering; avoid overlapping wide ranges that cause oscillation.
- **target_variant/modules**: Prefer explicit module slots with year-based guards (`>MODULE`, `<MODULE`, `>empty`) to steer upgrades; avoid ambiguous `any_of` unless necessary.
- **requirements vs allowed_modules**: Requirements are must-have checks; allowed_modules define ordered preference. Keep them in sync to avoid generating illegal designs.
- **enable / available_for / blocked_for**: Gate designs and variants cleanly; DLC-gated modules should be paired with enable triggers to prevent null designs.
- **New tokens**: `allowed_modules` plus `requirements` should reflect current module sets (including post-1.14 modules). Use `upgrade = current` / `>current` to lock or force upgrades during iterative variant improvements.
- **Debugging**: `imgui show ai equipment` to inspect role matches, selected modules, and priority scores; ensure categories match `ai_type` expectations.

## AI Peace Conference (1.14+)

Peace conference AI lives in `common/peace_conference/ai_peace/*.txt` (1.14+). Entries use `peace_ai_desires` with action-level weights.

```hoi4
my_peace_ai = {
    enable = { }  # multiple enables can be true
    
    peace_action_type = {
        action = take_states
        desire = 500        # -1000..1000
        zero_disables = yes # if desire sums to 0, disable the action
    }
}
```

Action types: `liberate`, `puppet`, `take_states`, `force_government`, `take_navy` (no AI modding support), and others introduced post-1.14 as applicable.

Scopes:
- ROOT = winner country
- FROM = country undergoing the action (can be non-existent for liberation/puppeting)
- FROM.FROM.FROM = state being affected

Behavior:
- Multiple `peace_action_type` blocks can be active; desires are summed. Use `zero_disables` to explicitly disable an action when total desire is 0.
- Keep desires comparable across actions; wide ranges cause unstable selection.
- Controller refers to pre-conference occupier; owner is the original pre-war owner.

Debug/links:
- Uses defines in `defines_list/NAI.md` for base weights; reference peace cost modifiers where applicable.
* `take_navy` still lacks AI hooks; only player cost modifiers apply (BBA).

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

## AI Strategy Tokens (2024-11)

Recent tokens (1.14+/2024-11) expand AI knobs:
- **Equipment market / raid targets**: New strategy tokens for buying/selling and selecting raid targets; align with raid/market systems and ensure region/target scopes are valid.
- **Naval dominance / convoy raiding**: Separate weights for dominance vs raiding; keep consistent with naval objective priorities.
- **Research weighting**: Finer-grained category weights; ensure category names match tech folders to avoid zeroed research.
- **Production minimums**: Tokens enforcing floor production for critical roles; set conservative minimums to avoid starving niche equipment.
- **unit_ratio updates**: Behavior now influences both templates and equipment; keep ratios aligned so production matches desired force mix.

> [!TIP] When adding new tokens, keep default values neutral and gate with enable triggers to avoid sudden AI swings in mods without supporting data.

## Related Defines

- `NAI.FOCUS_TREE_CONTINUE_FACTOR`: AI same-branch focus continuation bonus
- `NAI.*`: Various AI behavior constants affecting strategy execution
