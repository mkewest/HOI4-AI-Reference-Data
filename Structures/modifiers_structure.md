# Modifiers Domain Structure

## Overview

The modifiers domain is split into two complementary parts:
1. **modifiers.md** (scripting domain) - System mechanics and behavioral documentation
2. **modifiers_list/** (modifiers_list domain) - Complete enumeration of all available modifiers

This separation maintains clear distinction between "how modifiers work" vs "what modifiers exist."

## File Organization

### Scripting Domain: modifiers.md

**Location:** `/scripting/modifiers.md`  
**Token count:** ~6500 tokens  
**Purpose:** Explains modifier system mechanics, types, application methods, and critical edge cases

**Content:**
- Modifier types (percentual, flat, boolean, multiplicative)
- Application methods (ideas, traits, dynamic, static, targeted, opinion)
- Dynamic modifier evaluation mechanics and timing
- Zero-value behavior and multiplicative compounding
- Scope contexts and requirements
- Broken modifiers (cavalry_speed_factor, attack_bonus_against, defense_bonus_against)
- Variable-based modifier system
- Opinion modifiers distinction
- Terrain and special forces scope limitations
- MIO and operative modifiers
- Best practices and related systems

**Critical edge cases integrated:**
- Zero-value behavior (completely ignored by engine)
- Multiplicative modifier compounding
- Dynamic modifier evaluation order (call order, not definition order)
- State variable scoping (must be FOR THE STATE)
- Tooltip limitations (variables don't show)
- Targeted modifier block requirement
- Broken modifiers
- Idea cost modifier prerequisites
- Terrain_penalty_reduction scope limitation (unit_leader only)
- Operative_death_on_capture_chance scope limitation (country only)

### Modifiers_List Domain

**Location:** `/modifiers_list/`  
**Total files:** 15 markdown files  
**Total modifiers:** 455+ modifiers  
**Total tokens:** ~24,000 tokens  
**Purpose:** Complete enumeration of available modifiers by functional category

#### File Structure

```
/modifiers_list/
├── 00_overview.md           (~800 tokens)  - Navigation, pattern explanations, relationships
├── intelligence.md          (~1800 tokens) - Intelligence agency, operatives, operations
├── military_land.md         (~3400 tokens) - Land combat, training, special forces, unit types
├── military_leaders.md      (~1900 tokens) - Land leaders, experience, command limits
├── military_naval.md        (~3000 tokens) - Naval combat, ships, leaders, production, invasion
├── military_air.md          (~2400 tokens) - Air combat, missions, paradrops
├── politics_ideology.md     (~2600 tokens) - Politics, ideology, manpower, justification, volunteers
├── economy_production.md    (~2000 tokens) - Economy, production, construction, repair
├── economy_resources.md     (~2200 tokens) - Resources, fuel, trade, lend-lease, licenses
├── occupation_autonomy.md   (~2100 tokens) - Occupation, resistance, autonomy, puppets
├── state_modifiers.md       (~1400 tokens) - State-scoped modifiers, local effects
├── equipment.md             (~800 tokens)  - Equipment stats, upgrades, capture, idea costs
├── research.md              (~700 tokens)  - Research speed, doctrine costs
├── ai_modifiers.md          (~1000 tokens) - AI behavior weights and priorities
└── special_operations.md    (~900 tokens)  - Strategic redeployment, exiled divisions, nuclear
```

## Semantic Groupings

### Military Domain (6 files, ~15,200 tokens)
- **intelligence.md**: Intelligence systems separate from combat
- **military_land.md**: Ground warfare (63 modifiers) - largest military file
- **military_leaders.md**: Leader-specific modifiers and experience systems
- **military_naval.md**: Complete naval warfare stack (77 modifiers) - largest file overall
- **military_air.md**: Air warfare and air-land interaction (51 modifiers)

**Rationale:** Military split by warfare domain (land/naval/air) rather than by modifier type. Leaders separated as they apply across all domains. Intelligence isolated due to distinct mechanics.

### Political & Economic Domain (5 files, ~9,200 tokens)
- **politics_ideology.md**: Government, ideology, diplomacy (54 modifiers)
- **economy_production.md**: Factories, construction, output
- **economy_resources.md**: Resources, fuel, trade, licensing
- **occupation_autonomy.md**: Occupation and puppet mechanics
- **state_modifiers.md**: State-scoped local effects

**Rationale:** Politics and economy split by functional area. State modifiers separated due to scope distinction (state vs country).

### Support Systems (4 files, ~3,800 tokens)
- **equipment.md**: Equipment stats and idea costs
- **research.md**: Research and doctrine
- **ai_modifiers.md**: AI behavior weights
- **special_operations.md**: Low-frequency military mechanics

**Rationale:** Smaller, specialized systems that don't fit main categories. Equipment kept minimal as most equipment modifiers are in military files.

## Edge Case Integration

All 47 edge cases from `modifiers_list_EdgeCases.txt` have been integrated inline at their point of relevance:

### Critical Edge Cases by File

**00_overview.md:**
- Display precision (applies to all modifiers)
- Pattern-based modifier explanations
- Version-specific features (1.11+, 1.13+, 1.15+)

**intelligence.md:**
- AI focus modifiers behavior
- Operation cost/outcome/risk pattern
- Target_sabotage naming inconsistency
- Decryption bonus requirements
- Operative_death_on_capture_chance scope

**military_land.md:**
- Special forces capacity (percentual despite affecting slots)
- Combat width mechanics
- Entrenchment loss behavior (boolean)
- River crossing (modifies penalty, not speed)
- Minimum training level (deployment threshold)
- Fortification damage (combat only)
- Recon while entrenched (stacking behavior)

**military_leaders.md:**
- Leader start levels (specific skills vs total)
- Experience gain patterns (training vs combat)
- Wounded vs sickness (independent systems)

**military_naval.md:**
- Naval role patterns (ship-type specific)
- Critical hits (three independent systems)
- Retreat chances (own vs enemy)
- Carrier overcrowding (penalty reduction, not capacity)
- Pride of the Fleet (doesn't apply to PotF itself)

**military_air.md:**
- Mission-specific air stats (only during mission)
- Paradrop agility quirk (doesn't work)
- Shore bombardment (amphibious only)

**politics_ideology.md:**
- Ideology drift vs acceptance (internal vs external)

**economy_production.md:**
- Production efficiency (four independent modifiers)
- Consumer goods factor (multiplicative)
- Conversion costs (asymmetric)

**economy_resources.md:**
- Fuel capacity (displays as thousands)
- Resource modifiers (state/temporary/country types)
- License purchase patterns (archetype vs specific)
- Autonomy gain sources (layered system)

**occupation_autonomy.md:**
- Occupied state modifiers (directional)
- Compliance vs resistance (opposing forces)

**state_modifiers.md:**
- State scope requirements (critical)
- Local vs global modifiers
- Controller-specific modifiers

**equipment.md:**
- Equipment category requirements (breakthrough, armor_value, air stats)
- Equipment capture (flat + factor)
- Idea cost prerequisites

**research.md:**
- Doctrine cost version (1.11+)
- Doctrine cost is percentual
- Doctrine prefix requirement (cat_)

**special_operations.md:**
- Exiled divisions (own vs allied distinction)

## Cross-Referencing Strategy

### From modifiers.md to modifiers_list:
```markdown
For complete modifier enumeration by category, see [Modifiers List](/modifiers_list/00_overview.md).

For specific modifier categories:
- Intelligence and operations: See [Intelligence Modifiers](/modifiers_list/intelligence.md)
- Land combat and units: See [Military Land Modifiers](/modifiers_list/military_land.md)
[... all 14 category links ...]
```

### From modifiers_list files to modifiers.md:
Every modifiers_list file begins with:
```markdown
For modifier system mechanics, types, application methods, and critical behavioral edge cases, see [Modifier System](/scripting/modifiers.md).
```

### Cross-Domain References:
Multiple domains reference specific modifiers:
- Military domain (MIOs) → modifiers_list
- Equipment domain → modifiers_list
- Ideas domain → modifiers_list
- Character domain → modifiers_list
- State domain → modifiers_list

All cross-references validated during integration.

## Token Distribution

| Component | Token Count | Percentage |
|-----------|-------------|------------|
| modifiers.md | ~6,500 | 21.3% |
| modifiers_list (15 files) | ~24,000 | 78.7% |
| **Total Domain** | **~30,500** | **100%** |

### modifiers_list Breakdown:

| File | Modifiers | Tokens | % of List |
|------|-----------|--------|-----------|
| military_naval.md | 77 | ~3,000 | 12.5% |
| military_land.md | 63 | ~3,400 | 14.2% |
| politics_ideology.md | 54 | ~2,600 | 10.8% |
| military_air.md | 51 | ~2,400 | 10.0% |
| occupation_autonomy.md | 39 | ~2,100 | 8.8% |
| economy_resources.md | 35 | ~2,200 | 9.2% |
| economy_production.md | 28 | ~2,000 | 8.3% |
| military_leaders.md | 24 | ~1,900 | 7.9% |
| ai_modifiers.md | 15 | ~1,000 | 4.2% |
| state_modifiers.md | 15 | ~1,400 | 5.8% |
| special_operations.md | 8 | ~900 | 3.8% |
| research.md | 8 | ~700 | 2.9% |
| equipment.md | 7 | ~800 | 3.3% |
| intelligence.md | 31 | ~1,800 | 7.5% |
| 00_overview.md | - | ~800 | 3.3% |

Average: ~1,600 tokens per file

## Dependency Graph

```
modifiers.md (system mechanics)
    ↓ (referenced by all)
modifiers_list/00_overview.md (navigation)
    ↓ (links to all)
[All 14 category files]
    ↓ (referenced by)
[External domains: military, equipment, ideas, characters, states]
```

**Typed Relationships:**

- **modifiers_list files** `requires: [modifiers]` - Must understand system mechanics first
- **modifiers.md** `relates: [ideas, dynamic_modifiers, static_modifiers, defines]` - Related scripting systems
- **Individual category files** have domain-specific `relates:` links

Examples:
```yaml
# intelligence.md
requires: [modifiers]
relates: [operatives, operations, intelligence_agency]

# military_land.md  
requires: [modifiers]
relates: [divisions, combat, units, training]

# economy_production.md
requires: [modifiers]
relates: [factories, construction, output, economy]
```

## Usage Patterns

### For New Modders
1. Read **modifiers.md** to understand how modifiers work
2. Browse **00_overview.md** for available categories
3. Reference specific category files as needed

### For Experienced Modders
- Use **00_overview.md** as quick reference for patterns
- Jump directly to category files for specific modifiers
- Reference **modifiers.md** for edge cases and broken modifiers

### For AI Systems (RAG)
- **Vector similarity**: Works well for finding specific modifiers by name or description
- **Graph traversal**: Follow `requires` relationship from category files back to modifiers.md for behavioral context
- **Multi-hop reasoning**: Category file → modifiers.md → related systems (ideas, effects, scopes)

## Pattern-Based Modifiers

Several categories use naming patterns to generate large modifier sets efficiently:

### Operations (intelligence.md)
- Pattern: `operation_<n>_<param>`
- Parameters: cost, outcome, risk
- Exception: target_sabotage uses "factor" instead of "outcome"
- 24 operations × 3 parameters = ~72 modifiers

### Mission-Specific Air Stats (military_air.md)
- Pattern: `air_<mission>_<stat>_factor`
- Missions: 6 types (interception, air_superiority, CAS, strategic_bomber, naval_strike, paradrop)
- Stats: 4-5 per mission type
- ~30 modifiers

### Naval Ship Roles (military_naval.md)
- Pattern: `navy_<role>_<stat>_factor`
- Roles: submarine, screen, capital_ship, carrier_air
- Stats: attack, defence, detection, targetting, agility (role-dependent)
- ~12 modifiers

### License Modifiers (economy_resources.md)
- Two patterns: `license_<archetype>_purchase_cost` and `license_<eq_type>_eq_cost_factor`
- Archetypes: infantry, naval, air, armor
- Specific equipment types: numerous

These patterns are documented in 00_overview.md and their respective category files.

## Version-Specific Features

**1.11+:**
- Doctrine cost modifiers (land/air/naval_doctrine_cost_factor)
- Percentual format: -0.05 = 5% reduction

**1.13+:**
- Military Industrial Organization (MIO) modifiers
- Task capacity is FLAT, others percentual

**1.15+:**
- Special project support modifiers

Version requirements noted in file frontmatter and inline where relevant.

## Critical Behaviors Preserved

These non-obvious behaviors MUST be maintained across any future refactoring:

1. **Zero-value modifiers** are completely ignored by engine
2. **Multiplicative modifiers** (consumer_goods_factor) compound, not add
3. **Dynamic modifiers** evaluate in call order, not definition order
4. **State dynamic modifiers** require variables in state scope
5. **Targeted modifiers** must be in targeted_modifier block
6. **attack_bonus_against** doesn't work when defending (and vice versa)
7. **cavalry_speed_factor** is broken
8. **terrain_penalty_reduction** only works in unit_leader scope
9. **operative_death_on_capture_chance** only works in country scope
10. **air_paradrop_agility_factor** doesn't actually work
11. **Idea cost modifiers** require prerequisite ideas in earlier-loaded files

These are documented in modifiers.md and repeated in relevant category files where users encounter them.

## File Maturity

All files represent HOI4 1.14+ systems with version-specific features noted. Modifier enumeration is complete as of version 1.14. Future game updates may add new modifiers which should be added to appropriate category files.

## Related Domains

Modifiers are referenced throughout the knowledge base:

- **Military domain:** MIOs reference organization and task capacity modifiers
- **Equipment domain:** Equipment definitions reference stat modifiers
- **Ideas domain:** Idea implementations use modifier blocks extensively
- **Character domain:** Leader traits use modifier blocks
- **State domain:** State modifiers and compliance/resistance systems
- **Effects domain:** Effects apply modifiers via various methods
- **Scopes domain:** Scope validity determines where modifiers work

Cross-references maintained bidirectionally in all cases.

## Master Index Integration

For master index generation:

**Domain entries:**
```json
{
  "scripting": {
    "concepts": ["modifiers", ...],
    "path": "/scripting/"
  },
  "modifiers_list": {
    "concepts": [
      "overview",
      "intelligence",
      "military_land",
      "military_leaders",
      "military_naval",
      "military_air",
      "politics_ideology",
      "economy_production",
      "economy_resources",
      "occupation_autonomy",
      "state_modifiers",
      "equipment",
      "research",
      "ai_modifiers",
      "special_operations"
    ],
    "path": "/modifiers_list/"
  }
}
```

**Graph relationships:**
- modifiers_list/* → requires → modifiers
- modifiers → relates → [ideas, dynamic_modifiers, static_modifiers, defines]
- Individual category files have domain-specific relates links

**Usage recommendation:**
- Route "how do modifiers work" queries → modifiers.md
- Route "what modifiers exist for X" queries → modifiers_list/category.md
- Route "find modifier named Y" queries → modifiers_list/* (vector search)
- Route error diagnosis → modifiers.md edge cases + category-specific modifiers

This structure optimizes for both human navigation (clear separation of mechanics vs enumeration) and AI retrieval (precise scoping, comprehensive edge cases, bidirectional linking).
