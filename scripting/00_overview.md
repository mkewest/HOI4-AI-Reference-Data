---
domain: scripting
concept: overview
version: 1.14+
relates: [core, modifiers_list, defines_list, content, military]
---

# Scripting Domain Structure

## Overview

The scripting domain contains 9 markdown files covering HOI4's core scripting systems: scopes, triggers, effects, on_actions, scripted triggers/effects/localization, defines, and modifiers. Files are organized by functional boundaries and usage patterns.

## File Structure

```
/scripting/
├── scopes.md                      - Scope system and evaluation contexts
├── triggers_core.md               - Core trigger logic and operators
├── triggers_specialized.md        - Domain-specific trigger reference
├── effects.md                     - Effect system and flow control
├── on_actions_core.md             - On_actions mechanisms and patterns
├── on_actions_reference.md        - Complete on_actions enumeration
├── scripted_triggers_effects.md   - Reusable scripting components
├── defines.md                     - Lua defines system
└── modifiers.md                   - Modifier application and types
```

## File Descriptions

### scopes.md (~4200 tokens)
**Purpose**: Complete scope system documentation  
**Covers**: Trigger/effect/dual scopes, scope patterns, parameters, scope-changing effects, invalid event targets, scope validation  
**Key concepts**: Scope types by purpose/target, effect patterns (every/random), scope parameters (limit, prioritize, random_select_amount), PREV chaining, civil war quirks  
**Unified despite size**: Splitting would destroy conceptual coherence

### triggers_core.md (~2500 tokens)
**Purpose**: Foundation trigger knowledge  
**Covers**: Comparison operators, logic operators (AND/OR/NOT/count_triggers), IF statements, tooltip control, flag values, scope validation  
**Key concepts**: Strict equality in HOI4 (= is exact, not ≥), NOT as NOR, days_since overflow, scripted triggers, meta triggers  
**Foundation for**: triggers_specialized.md and all conditional logic

### triggers_specialized.md (~2500 tokens)
**Purpose**: Domain-specific trigger lookup  
**Covers**: Global/country/state/character/mio/combat/division/contract/peace conference/intelligence triggers  
**Format**: Reference material organized by scope type  
**Key concepts**: Peace conference trigger distinctions, version-dependent behavior (pre/post-1.12), railway level constraints  
**Relationship**: Uses triggers_core.md concepts, provides specific trigger enumeration

### effects.md (~4200 tokens)
**Purpose**: Effect system and execution patterns  
**Covers**: Basic effects, flow control, looping (for/while), random selection, array scopes, common effect categories  
**Key concepts**: hidden_effect vs effect_tooltip, MAX_EFFECT_ITERATION limit (1000), loop break, scope-changing effects  
**Unified despite size**: Effect patterns and flow control are inseparable

### on_actions_core.md (~2200 tokens)
**Purpose**: On_actions mechanisms and best practices  
**Covers**: Basic structure, timing constraints, scope behavior, trigger cascades, special scope variables, performance  
**Key concepts**: on_startup has NO scope, on_daily performance issues, on_government_change cascade, capitulation sequencing, peace conference exclusivity  
**Foundation for**: on_actions_reference.md enumeration

### on_actions_reference.md (~3000 tokens)
**Purpose**: Complete on_actions enumeration  
**Covers**: All on_actions with scope mappings, triggers, and special cases  
**Format**: Organized by category (periodic, political, war, diplomatic, military, intelligence, MIO)  
**Key concepts**: Scope mapping table, FROM scope context, non-working on_actions, random_events constraints  
**Relationship**: Requires on_actions_core.md for understanding mechanisms

### scripted_triggers_effects.md (~3500 tokens)
**Purpose**: Reusable scripting system  
**Covers**: Scripted triggers, scripted effects, scripted localization, special patterns (diplomacy, resistance), meta triggers, override behavior  
**Key concepts**: Filename load order, diplomacy trigger patterns, resistance initiation control, variable-based parameterization, localization evaluation order  
**Enables**: Code abstraction and maintainability

### defines.md (~4800 tokens)
**Purpose**: Lua defines system mechanics  
**Covers**: File structure, Lua syntax, categories, loading, partial overrides, value types, common constraints, localization dependencies  
**Key concepts**: NO COMMAS (crashes), partial override support, NEVER include 00_defines.lua, MAX_EFFECT_ITERATION, GAME_SPEED_SECONDS requirements  
**Special**: Paired with the `defines_list` domain, which enumerates all `NDefines` values by category

### modifiers.md (~6500 tokens)
**Purpose**: Modifier application and behavior  
**Covers**: Modifier types (percentual/flat/boolean/multiplicative), application methods (ideas/traits/dynamic/static/targeted), dynamic modifier evaluation, opinion modifiers, custom modifiers  
**Key concepts**: Zero-value behavior, multiplicative compounding, dynamic modifier evaluation order, state variable scoping, targeted modifier blocks, broken modifiers  
**Special**: Paired with the `modifiers_list` domain, which provides complete enumeration of individual modifiers by category

## Dependency Graph

```
scopes.md ←──┐
             ├─→ triggers_core.md → triggers_specialized.md
             │
             ├─→ effects.md
             │       ↓
             └─→ on_actions_core.md → on_actions_reference.md
                     ↓
             scripted_triggers_effects.md
                     ↓
             ┌───────┴───────┐
        defines.md      modifiers.md
```

**Foundation layer**: scopes.md (everything requires understanding scopes)  
**Logic layer**: triggers_core.md and effects.md (conditional and execution logic)  
**Automation layer**: on_actions_core.md and scripted_triggers_effects.md (event-driven and reusable code)  
**Special systems**: defines.md and modifiers.md (game constants and value modification)

## Semantic Groupings

### Core Execution Systems (tightly coupled)
- scopes.md: Evaluation contexts
- triggers_core.md: Conditional logic
- effects.md: State modification
- on_actions_core.md: Event-driven execution

These four files form the foundation of all HOI4 scripting.

### Reference Material (lookup-focused)
- triggers_specialized.md: Trigger enumeration
- on_actions_reference.md: On_actions enumeration

Split from core files to separate mechanisms from complete listings.

### Reusable Components
- scripted_triggers_effects.md: Code abstraction and reuse

Enables maintainable mod development and vanilla content organization.

### Configuration Systems
- defines.md: Read-only game constants
- modifiers.md: Value modification system

Both affect how other systems behave but operate independently.

## Token Distribution

| File | Token Count | Percentage |
|------|-------------|------------|
| modifiers.md | ~6500 | 22.8% |
| defines.md | ~4800 | 16.8% |
| scopes.md | ~4200 | 14.7% |
| effects.md | ~4200 | 14.7% |
| scripted_triggers_effects.md | ~3500 | 12.3% |
| on_actions_reference.md | ~3000 | 10.5% |
| triggers_core.md | ~2500 | 8.8% |
| triggers_specialized.md | ~2500 | 8.8% |
| on_actions_core.md | ~2200 | 7.7% |
| **Total** | **~28,500** | **100%** |

Average: ~3,167 tokens per file

Two files exceed 4000 tokens (scopes.md, effects.md) but remain unified because splitting would destroy conceptual coherence. The Rule 1 threshold is a guideline, not a hard limit - semantic completeness takes priority.

## Edge Case Integration

All 62 edge case categories from `scripting_EdgeCases.txt` have been integrated inline at their point of relevance:

**scopes.md (10 categories):**
- SCOPE EXISTENCE & SELECTION
- INVALID EVENT TARGET ERROR  
- SCOPE ORDERING
- LIMIT RESTRICTIONS
- PRIORITIZE BEHAVIOR
- VISIBILITY FILTERING
- PREV CHAINING
- CIVIL WAR QUIRKS
- CHARACTER SCOPE
- RANDOM_SELECT_AMOUNT

**triggers_core.md (7 categories):**
- TRIGGER OPERATORS
- TRIGGER LOGIC
- SCOPE VALIDATION
- FLAG VALUES
- DAYS_SINCE TRIGGERS
- META TRIGGERS/EFFECTS
- ZERO VALUES

**triggers_specialized.md (7 categories):**
- EQUIPMENT TRIGGERS
- STRENGTH RATIO
- WAR TRIGGERS
- ADVISOR TRIGGERS
- TEMPLATE TRIGGERS
- RAILWAY TRIGGERS
- RESISTANCE TRIGGERS
- OCCUPATION LAW TRIGGERS
- PEACE CONFERENCE TRIGGERS

**effects.md (5 categories):**
- LOOP LIMITS
- FROM SCOPE
- ROOT VS THIS
- EVALUATION TIMING
- TOOLTIP BEHAVIOR

**on_actions_core.md (9 categories):**
- ON_ACTION SCOPE BEHAVIOR
- ON_ACTION TRIGGER CASCADES
- RANDOM_EVENTS CONSTRAINTS
- ON_ACTION TIMING
- CAPITULATION SEQUENCING
- PEACE CONFERENCE EXCLUSIVITY
- ON_ACTION SPECIAL SCOPES
- NON-WORKING ON_ACTIONS
- ON_ACTION PERFORMANCE

**scripted_triggers_effects.md (3 categories):**
- SCRIPTED TRIGGER PRIORITY
- TOOLTIP BEHAVIOR
- EVALUATION TIMING

**defines.md (7 categories):**
- DEFINES FILE STRUCTURE
- DEFINES SYNTAX
- DEFINES VALUE CONSTRAINTS
- DEFINES LOCALIZATION
- SCRIPTING LIMITS
- DEFINES TIMING
- DEFINES COMPATIBILITY

**modifiers.md (14 categories):**
- DYNAMIC MODIFIERS
- MULTIPLICATIVE MODIFIERS
- STATIC MODIFIERS
- IDEA COST MODIFIERS
- OPINION MODIFIERS
- TARGETED MODIFIERS
- MODIFIER BUGS
- DOCTRINE COSTS
- TERRAIN MODIFIERS
- EQUIPMENT CAPTURE
- SPECIAL FORCES
- MIO MODIFIERS
- OPERATIVE MODIFIERS
- ZERO VALUES

No separate edge case files exist - all warnings and gotchas appear in context.

## Usage Patterns

### For New Modders
**Start with**: scopes.md → triggers_core.md → effects.md  
**Reason**: Foundation concepts required for any scripting

**Then**: on_actions_core.md for event-driven systems  
**Reason**: Most mods need on_actions for automatic behaviors

**Finally**: scripted_triggers_effects.md for code organization  
**Reason**: Improves maintainability as mod complexity grows

### For Experienced Modders
**Reference**: triggers_specialized.md, on_actions_reference.md  
**Reason**: Quick lookup without wading through explanations

**Deep dive**: defines.md, modifiers.md  
**Reason**: Advanced tuning and optimization

### For Troubleshooting
**Scope issues**: scopes.md (INVALID EVENT TARGET, scope ordering)  
**Logic errors**: triggers_core.md (NOT as NOR, operator strictness)  
**Performance**: on_actions_core.md (on_daily optimization, cascade awareness)  
**Modifier bugs**: modifiers.md (multiplicative behavior, broken modifiers, scope requirements)

### For Balance Modders
**Primary files**: defines.md, modifiers.md  
**Reason**: Most balance changes through defines and modifiers

**Secondary**: effects.md for scripted balance adjustments  
**Reason**: Dynamic balance via scripted effects

## Critical Dependencies

Files that MUST be read together for complete understanding:

1. **scopes.md + triggers_core.md + effects.md**: Core execution model is inseparable
2. **on_actions_core.md + on_actions_reference.md**: Mechanisms and enumeration form complete system
3. **triggers_core.md + triggers_specialized.md**: Foundation and application
4. **defines.md + modifiers.md**: Both affect game balance and interact with each other

## File Maturity

All files represent HOI4 1.14+ stable systems. Version-specific features are noted in YAML frontmatter or inline text:
- Scopes: character scope version behavior (pre/post-1.12.8)
- Triggers: advisor trigger version behavior (pre/post-1.12)
- Modifiers: MIO modifiers (1.13+), special projects (1.15+)

## Forward References

### defines.md → defines_list domain
Contains forward references to not-yet-created files:
- `MAX_EFFECT_ITERATION`: See [NGame](/defines_list/NGame.md)
- `PROVINCE_AREA_LIMIT`: See [NGraphics](/defines_list/NGraphics.md)
- And others as appropriate

Actual define values are included inline where critical (e.g., "1000 iterations maximum").

### modifiers.md → modifiers_list domain
Entire file marked for future integration. See [Modifiers Structure](/scripting/modifiers_structure.md) for integration instructions.

## Retrieval Optimization

**Simple lookups**: Start with specialized files (triggers_specialized.md, on_actions_reference.md)  
**Concept understanding**: Start with core files (scopes.md, triggers_core.md, effects.md)  
**Troubleshooting**: Use edge case integration to find relevant warnings at point of use  
**Cross-domain**: Follow typed relationships in YAML frontmatter (requires/relates/conflicts)


