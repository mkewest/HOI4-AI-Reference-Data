---
domain: content
concept: overview
version: 1.14+
relates: [scripting, database, military, assets]
---

# Content Domain Structure

## Overview

The content domain contains 6 markdown files covering all scripted game content systems in Hearts of Iron IV. Files are organized by semantic cohesion, grouping interdependent mechanics that share evaluation systems and scoping rules.

## File Structure

```text
/content/
├── events.md           - Event system and firing mechanics
├── national_focus.md   - National focus trees and progression
├── decisions.md        - Decision categories and types
├── ai_strategy.md      - AI behavior and automation
├── achievements.md     - Custom achievement system
└── bookmarks.md        - Game start scenarios and configuration
```

## File Descriptions

### events.md (~2800 tokens)

**Purpose**: Scripted occurrences with player choices  
**Covers**: Event types (country/news/state/unit_leader/operative_leader), ID system and namespacing, attributes (trigger, MTTH, major behavior), options and AI selection, firing mechanics, scope shifting, nonexistent country handling, localization requirements  
**Key relationships**: Requires triggers, effects, and scopes; relates to localisation and on_actions_core  
**Note**: Largest file due to complex scope behavior and 11 edge case sections

### national_focus.md (~2600 tokens)

**Purpose**: Long-term strategic planning system  
**Covers**: Focus trees and assignment, focus attributes (positioning, prerequisites, availability, bypass, completion), shared/joint focuses, continuous focuses, AI selection algorithm, tree refreshing, civil war behavior  
**Key relationships**: Requires triggers, effects, and modifiers; relates to ideas_core and ai_strategy  
**Note**: Second largest due to prerequisite logic complexity and 12 edge case sections

### decisions.md (~2200 tokens)

**Purpose**: Player choices outside event system  
**Covers**: Decision categories, standard decisions, targeted decisions (country/state), missions, cost systems (standard and custom), timer mechanics, war warnings, random seed control  
**Key relationships**: Requires triggers, effects, and modifiers; relates to states, events, and national_focus  
**Note**: Three distinct decision types with different evaluation rules

### ai_strategy.md (~2400 tokens)

**Purpose**: Automated decision-making for AI countries  
**Covers**: Strategy plans and assignment, AI areas (geographic), strategy types (50+ types), focus modifiers, division templates, equipment designs, peace conference AI (both 1.14+ and pre-1.12), MTTH block evaluation  
**Key relationships**: Requires triggers, modifiers, and strategic_regions; relates to national_focus, division_template, and equipment  
**Note**: Unified all AI behaviors despite spanning multiple subsystems

### achievements.md (~600 tokens)

**Purpose**: Mod-defined achievement system  
**Covers**: File structure (definitions/icons/localization), icon requirements (three variants), achievement definition, evaluation timing (possible vs happened), custom ribbons, cross-session tracking  
**Key relationships**: Requires triggers; minimal external dependencies  
**Note**: Smallest file - self-contained system added in 1.12.1

### bookmarks.md (~1200 tokens)

**Purpose**: Game start scenario configuration  
**Covers**: Bookmark structure and attributes, country entries (display and availability), date history execution, difficulty settings (slider-based), game rules, player difficulty (five presets), UI configuration  
**Key relationships**: Requires national_focus, ideologies, and country_history; relates to decisions and states  
**Note**: Multiple configuration systems unified by their shared role in game initialization

## Dependency Graph

```text
triggers, effects, scopes (external dependencies)
    ↓ (required by)
events.md
    ↓ (relates to)
national_focus.md ←→ ai_strategy.md
    ↓
decisions.md
    ↓
achievements.md

bookmarks.md → countries, focus_trees (external)
```

## Semantic Groupings

### Core Content Systems (sequential progression)

- events.md: Immediate occurrences with branching choices
- national_focus.md: Long-term strategic planning
- decisions.md: Ongoing actions and missions
- ai_strategy.md: Automated behavior for all systems above

These four files represent the hierarchy of player/AI interaction with scripted content.

### Initialization Systems

- bookmarks.md: Game start configuration
- achievements.md: Meta-progression tracking

These handle game setup and meta-level progression outside normal gameplay.

## Token Distribution

| File | Token Count | Percentage |
|------|-------------|------------|
| events.md | ~2800 | 23.7% |
| national_focus.md | ~2600 | 22.0% |
| ai_strategy.md | ~2400 | 20.3% |
| decisions.md | ~2200 | 18.6% |
| bookmarks.md | ~1200 | 10.2% |
| achievements.md | ~600 | 5.1% |
| **Total** | **~11,800** | **100%** |

Average: ~1,967 tokens per file  
All files remain well under the 4000 token threshold for optimal RAG chunking.

## Edge Case Integration

All 46 edge case sections from `content_EdgeCases.txt` have been integrated inline at their point of relevance:

### Events (11 sections)

- **Scope behavior**: Dual-scope priority, ROOT/FROM shifting integrated into scoping section
- **ID system**: Namespace calculation, non-integer conversion integrated into ID system section
- **Auto-trigger timing**: 20-day checks, date windows integrated into trigger section
- **Major behavior**: fire_only_once priority, show_major filtering integrated into major events section
- **Nonexistent country**: Backlog system, timer freezing integrated into dedicated section
- **AI options**: Zero handling, deterministic selection integrated into options section
- **MTTH**: Contradictory configs, sequential evaluation integrated into MTTH section
- **Timing**: Execution order, cumulative delays integrated into timing section
- **Hidden events**: Auto-pick behavior, use cases integrated into hidden attribute section
- **Localization**: UTF-8-BOM requirement, conditional limitations integrated into dedicated section
- **Country tag**: Taglist ordering integrated into dedicated section

### National Focus (12 sections)

- **Evaluation**: MTTH timing, dynamic country exceptions integrated into tree attributes
- **Civil war**: Progress copying, tree reassignment integrated into reset_on_civilwar section
- **Completion state**: has_completed_focus timing, workarounds integrated into completion_reward section
- **Prerequisite lines**: Duplicate ID breakage, positioning requirements integrated into prerequisite section
- **Tree refreshing**: mark_focus_tree_layout_dirty timing integrated into dedicated section
- **AI selection**: Random roll algorithm, continue factor integrated into ai_will_do section
- **Visibility**: allow_branch inheritance, child exceptions integrated into allow_branch section
- **Shared focus crashes**: Reference errors, minimum requirements integrated into shared focus section
- **Sprites**: Shine naming, path errors integrated into icon section
- **Continuous position**: Tree override behavior integrated into continuous_focus_position section
- **Cancellation**: select_effect override, pause behavior integrated into cancellation section
- **Boolean logic**: System limitations, workarounds integrated into prerequisite section

### Decisions (6 sections)

- **Mission activation**: visible ineffectiveness, activation timing integrated into missions section
- **Custom cost**: Manual subtraction requirement, AI hints integrated into cost system section
- **Timer**: Execution timing, visible behavior integrated into timer system section
- **War warnings**: Targeted decision variants integrated into war warnings section
- **State targeted**: Continent values, target compatibility integrated into targeted decisions section
- **Random seed**: Fixed vs variable outcomes integrated into dedicated section

### AI Strategy (9 sections)

- **MTTH blocks**: Evaluation order, temp variables integrated into dedicated section
- **Strategies**: Binary behaviors, counterintuitive thresholds integrated into strategy types section
- **Areas**: OR logic, non-exclusivity integrated into AI areas section
- **Peace (1.14+)**: Controller vs owner, FROM non-existence integrated into peace section
- **Peace (pre-1.12)**: File loading order, temp variable persistence integrated into legacy peace section
- **Strategy plans**: Focus ignoring, permanent assignment integrated into strategy plans section
- **Templates**: Copy behavior, match scoring integrated into templates section
- **Equipment**: Role multiplicity, module comparisons integrated into equipment section
- **Focuses calculation**: Peace multipliers, fascist defaults integrated into focus modifiers section

### Achievements (1 section)

- **Evaluation**: possible timing, happened delay integrated into evaluation timing section

### Bookmarks (7 sections)

- **Single bookmark**: Skip behavior, menu lockout integrated into dedicated section
- **Interesting country**: Minor + default tree invisibility integrated into country entries section
- **Date history**: Strictly-later execution integrated into dedicated section
- **Country entry**: Multiple definitions, cosmetic attributes integrated into country entries section
- **Game rules**: Menu requirements, DLC behavior integrated into game rules section
- **Dates**: Year 2 minimum, randomize_weather integrated into date section
- **Difficulty**: Independent systems integrated into difficulty settings section

No separate edge case files exist - all warnings and gotchas appear in context where users encounter them.

## Usage Patterns

### For New Modders

Start with: events.md → decisions.md sequence to understand basic content creation. Then progress to national_focus.md for long-term systems.

### For AI Behavior

Focus on: ai_strategy.md (requires understanding of focuses, templates, and equipment from other domains).

### For Scenario Creation

Key files: bookmarks.md (requires understanding of history files and countries from other domains).

### For Meta-Systems

Primary file: achievements.md (relatively independent, requires only trigger knowledge).

### For Event Writers

Primary file: events.md with reference to scopes documentation from external domain.

## Critical Dependencies

Files that MUST be read together for complete understanding:

1. **events.md + scopes**: Scope shifting is meaningless without scope system knowledge
2. **national_focus.md + ai_strategy.md**: AI focus selection depends on both systems
3. **decisions.md + effects**: Decision mechanics require effect system knowledge
4. **ai_strategy.md + strategic_regions**: AI areas reference strategic region definitions

## System Interaction Patterns

### Event → Focus → Decision Flow

Events can fire decisions, decisions can complete focuses, focuses can fire events. This circular dependency explains why ai_strategy.md had to unify all AI behaviors.

### AI Behavior Hierarchy

Strategy plans (ai_strategy.md) control focus selection (national_focus.md), which triggers events (events.md), which may present decisions (decisions.md). All four files must be understood for comprehensive AI behavior modding.

### Initialization Chain

Bookmarks (bookmarks.md) load history, which assigns focus trees (national_focus.md), which may auto-fire events (events.md) or activate missions (decisions.md).

## File Maturity

All files represent stable HOI4 systems as of version 1.14+. Version-specific features are noted in YAML frontmatter or inline text:

- achievements.md: Version 1.12.1+ (system introduction)
- national_focus.md: Joint focuses added 1.13, continuous focus properties added 1.5
- events.md: After attribute added 1.16.9
- ai_strategy.md: Peace AI rewritten in 1.14 (legacy pre-1.12 documented separately)

## Known Interdependencies with Other Domains

### External Requirements

- **triggers**: Required by events, focuses, decisions, ai_strategy, achievements, bookmarks
- **effects**: Required by events, focuses, decisions
- **scopes**: Required by events (scope shifting), ai_strategy (peace AI)
- **modifiers**: Required by focuses (continuous), ai_strategy (all strategy types)
- **strategic_regions**: Required by ai_strategy (AI areas)
- **national_focus**: Required by bookmarks (tree assignment and display)
- **ideologies**: Required by bookmarks (country entries)
- **country_history**: Required by bookmarks (date execution)

### External Relations

- **on_actions_core**: Relates to events (firing context)
- **localisation**: Relates to events, focuses, decisions (loc keys)
- **ideas_core**: Relates to focuses (continuous focus ideas)
- **division_template**: Relates to ai_strategy (templates)
- **equipment**: Relates to ai_strategy (designs)

These relationships are documented in each file's YAML frontmatter using typed relationship keys (requires/conflicts/relates).
