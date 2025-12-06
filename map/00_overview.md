---
domain: map
concept: overview
version: 1.14+
relates: [core, assets, database, military]
---

# Map Domain Structure

## Overview

The map domain contains 10 markdown files covering all geographic, terrain, and infrastructure systems in Hearts of Iron IV. Files are organized by semantic cohesion with careful attention to interdependent systems.

## File Structure

```text
/map/
├── provinces.md           - Province definitions and continental system
├── terrain.md             - Provincial and graphical terrain with atlas
├── heightmap.md           - Height mapping and visual layers
├── rivers.md              - River system and colormap indices
├── buildings.md           - Positioned map objects
├── adjacencies.md         - Province connections and rules
├── strategic_regions.md   - Regional grouping and weather
├── supply.md              - Supply nodes and railways
├── coordinates.md         - Coordinate system and conventions
└── troubleshooting.md     - Error diagnosis and tools
```

## File Descriptions

### provinces.md (~1400 tokens)

**Purpose**: Foundation of map geography  
**Covers**: provinces.bmp format, definition.csv structure, province types, continental assignment, state requirements, common errors  
**Key relationships**: Requires coordinates, relates to terrain, strategic_regions, states  
**Critical edge cases**: Province ID gaps, CRLF line endings, bitmap coastal status precedence, border limits

### terrain.md (~1800 tokens)

**Purpose**: Terrain systems for gameplay and visuals  
**Covers**: Provincial terrain (combat modifiers), graphical terrain (appearance), texture atlas system, trees, colormap preservation, nudger auto-generation  
**Key relationships**: Requires provinces, relates to heightmap and entities  
**Note**: Largest file due to dual terrain systems and their interactions

### heightmap.md (~900 tokens)

**Purpose**: Elevation and visual mapping  
**Covers**: Heightmap scale and precision, normal map channel definitions, colormap system (RGB for world color, Alpha for city lights), synchronization requirements  
**Key relationships**: Requires provinces and coordinates, relates to terrain  
**Note**: All three visual layers (heightmap, normal, colormap) must be kept synchronized

### rivers.md (~700 tokens)

**Purpose**: River mechanics and rendering  
**Covers**: River requirements (1px thick, orthogonal), colormap indices (source/flow/width categories), pathfinding impact, colormap preservation  
**Key relationships**: Requires provinces, relates to supply  
**Note**: Rivers count as level 1 railways, affecting pathfinding performance

### buildings.md (~800 tokens)

**Purpose**: Positioned structures and markers  
**Covers**: buildings.txt format, unitstacks.txt (including victory points), ambient_object.txt, rotation conventions, coordinate usage, critical crash conditions  
**Key relationships**: Requires provinces, states, and coordinates, relates to entities  
**Critical edge cases**: Empty buildings.txt crashes, missing naval_base definitions cause delayed crashes

### adjacencies.md (~1000 tokens)

**Purpose**: Special province connections  
**Covers**: adjacencies.csv format, adjacency types (sea/impassable), through province mechanics, adjacency_rules.txt (conditional logic), relation states and permissions  
**Key relationships**: Requires provinces, relates to strategic regions  
**Critical edge cases**: File terminator requirement, same-type province requirement, enemy control blocking

### strategic_regions.md (~1800 tokens)

**Purpose**: Regional organization and weather  
**Covers**: Strategic region structure, province assignment requirements, naval terrain assignment, weather system (periods, temperature, snow, weather states), weather positions, date formatting  
**Key relationships**: Requires provinces and coordinates, relates to terrain and supply  
**Critical edge cases**: Sequential ID requirement, all provinces must be assigned, weather positions need both small and large definitions  
**Note**: Second-largest file due to comprehensive weather system

### supply.md (~1000 tokens)

**Purpose**: Supply infrastructure  
**Covers**: Current system (1.11+: supply nodes and railways), legacy system (≤1.10: supply areas), rivers as railways, migration notes  
**Key relationships**: Requires provinces, conflicts with pre-1.11 supply_areas, relates to strategic regions and rivers  
**Note**: Includes deprecated content for mod compatibility

### coordinates.md (~600 tokens)

**Purpose**: Foundational coordinate system  
**Covers**: Axis definitions (X/Y/Z), position format variations across files, rotation conventions (radians), degree-to-radian conversion, X crossing error, automatic calculation  
**Key relationships**: Relates to provinces, heightmap, buildings, and strategic regions  
**Note**: Smallest conceptual file but critically important for understanding spatial data

### troubleshooting.md (~1500 tokens)

**Purpose**: Error diagnosis and tool usage  
**Covers**: Debug mode requirement, BMP file handling (compatible editors, colormap preservation, bitdepth detection), common errors (X4008, MAP_ERROR types, no continent, bitmap coastal disagree), nudger tool (capabilities, limitations, output location), file encoding issues  
**Key relationships**: Relates to provinces, terrain, heightmap, and rivers  
**Note**: Consolidates all "fixing things" knowledge in one place

## Dependency Graph

```text
coordinates.md (foundational)
    ↓
provinces.md (geographic foundation)
    ↓
    ├→ terrain.md ←→ heightmap.md
    ├→ rivers.md → supply.md
    ├→ buildings.md
    ├→ adjacencies.md
    └→ strategic_regions.md → supply.md

troubleshooting.md (references all files)
```

## Semantic Groupings

### Geographic Foundation

- coordinates.md: Axis system
- provinces.md: Basic geography
- states (external): Province grouping

### Visual Systems

- terrain.md: Terrain appearance and gameplay
- heightmap.md: Elevation and lighting
- rivers.md: Water systems

### Infrastructure

- buildings.md: Structures and markers
- supply.md: Resource distribution
- strategic_regions.md: Regional organization

### Connectivity

- adjacencies.md: Special connections
- rivers.md: Natural pathways (level 1 railways)
- supply.md: Supply pathways

### Support Tools

- troubleshooting.md: Error diagnosis
- Debug mode: Error visibility
- Nudger: In-engine editing

## Token Distribution

| File | Token Count | Percentage |
|------|-------------|------------|
| terrain.md | ~1800 | 15.7% |
| strategic_regions.md | ~1800 | 15.7% |
| troubleshooting.md | ~1500 | 13.0% |
| provinces.md | ~1400 | 12.2% |
| adjacencies.md | ~1000 | 8.7% |
| supply.md | ~1000 | 8.7% |
| heightmap.md | ~900 | 7.8% |
| buildings.md | ~800 | 7.0% |
| rivers.md | ~700 | 6.1% |
| coordinates.md | ~600 | 5.2% |
| **Total** | **~11,500** | **100%** |

Average: ~1,150 tokens per file

## Edge Case Integration

All edge cases from `map_EdgeCases.txt` have been integrated inline at their point of relevance:

### Provinces

- BMP format requirements and editor compatibility
- Province ID gap consequences
- CRLF line ending requirement
- Border limits and disjointed provinces
- Continental boundary edge cases

### Terrain

- Colormap preservation techniques
- Indexed BMP editing workflows
- Atlas texture system requirements
- Terrain auto-generation

### Heightmap

- Height precision calculations
- Normal map channel ranges
- Colormap synchronization

### Rivers

- Source pixel requirements (exactly 1 green per river)
- Flow-in mechanics for tributaries
- Palette error safety
- Performance impact as railways

### Buildings

- Empty file crash
- Naval base crash conditions
- State ID usage for provincial buildings
- Victory point split definition

### Adjacencies

- Same-type requirement
- Through province control blocking
- File terminator requirement

### Strategic Regions

- Sequential ID requirement
- All provinces must be assigned
- Date format (zero-indexed)
- Weather state weighting vs duration
- Weather positions crash prevention
- Deprecated temperature_day_night

### Supply

- Invalid definition crashes
- Sequential ID requirement (pre-1.11)
- Very disjointed railway issues

### Coordinates

- X crossing error at map edges
- Axis convention differences
- Rotation in radians

### Troubleshooting

- Debug mode necessity
- BMP header format issues
- Nudger quote removal
- Nudger UTF-8 crash
- Replace path visibility
- File encoding requirements

No separate edge case files exist - all warnings and gotchas appear in context where users encounter them.

## Usage Patterns

### For New Map Modders

Start with this sequence:

1. **coordinates.md** - Understand the axis system
2. **provinces.md** - Learn province creation
3. **troubleshooting.md** - Set up debug mode
4. **terrain.md** - Add terrain types
5. **strategic_regions.md** - Organize regions

### For Total Conversion Mods

Critical files:

- provinces.md: Complete province redefinition
- terrain.md: Custom terrain types
- strategic_regions.md: New regional organization
- supply.md: Supply network design
- troubleshooting.md: Debug workflow

### For Visual Enhancement Mods

Key files:

- heightmap.md: Elevation and lighting
- terrain.md: Texture atlas customization
- rivers.md: Water system visuals
- troubleshooting.md: BMP editing workflow

### For Performance Optimization

Focus on:

- provinces.md: Border count management
- rivers.md: Railway-as-river performance impact
- supply.md: Railway network optimization

### For Scenario Mods

Primary files:

- buildings.md: Structure placement
- strategic_regions.md: Weather configuration
- adjacencies.md: Custom connections (canals, straits)

## Critical Dependencies

Files that MUST be read together for complete understanding:

1. **coordinates.md + provinces.md**: Coordinate system is foundational for understanding province positioning
2. **terrain.md + heightmap.md**: Visual systems are tightly coupled through colormap synchronization
3. **provinces.md + strategic_regions.md**: All provinces must be assigned to strategic regions
4. **supply.md + rivers.md**: Rivers function as level 1 railways
5. **buildings.md + coordinates.md**: Building placement requires coordinate system understanding

## File Maturity

All files represent stable HOI4 systems as of version 1.14+. Version-specific features are noted:

- **1.11+ changes**: Supply system redesign (supply_areas → supply_nodes/railways), temperature_day_night deprecation
- **1.15+ changes**: airports.txt and rocketsites.txt removal
- **Pre-1.11 content**: Preserved in supply.md with clear deprecation warnings

## Key Design Decisions

### Why separate coordinates.md?

- Foundational knowledge needed by 5+ files
- Small enough for quick reference (600 tokens)
- Conceptually distinct from any single system
- X crossing error is fundamentally a coordinate system issue

### Why combine terrain.md?

- Provincial and graphical terrain are tightly coupled
- Nudger auto-generates one from the other
- Atlas system is inseparable from graphical terrain
- Trees use the same colormap system as graphical terrain

### Why separate troubleshooting.md?

- BMP handling affects provinces, terrain, heightmap, rivers (4 files)
- Avoids 4× duplication of edge case blocks
- Users access troubleshooting in a different "mode" (when stuck)
- Consolidates tool usage (debug mode, nudger)

### Why combine heightmap systems?

- Heightmap, normal map, and colormap share coordinate system
- Synchronization requirement means they must be understood together
- All three are visual layers with no gameplay separation

### Why include deprecated supply system?

- Mod compatibility for pre-1.11 mods
- Understanding historical design decisions
- Migration guidance for modders updating old mods

## Related External Systems

Map files connect to external systems documented in other domains:

- **States** (history/states/): Province grouping, victory points, buildings
- **Defines** (common/defines/): Numeric constants referenced throughout
- **Entities** (gfx/entities/): 3D models for buildings and ambient objects
- **Localization**: Region names, terrain names, error messages
- **Weather** (common/weather.txt): Weather state definitions

## Version Compatibility Notes

The map system has been relatively stable since 1.11, with the major change being the supply system redesign. Key version breakpoints:

- **1.0-1.10**: Original supply areas system
- **1.11**: Supply nodes and railways introduced, temperature_day_night deprecated
- **1.11-1.14**: Stable period with minor refinements
- **1.15**: airports.txt and rocketsites.txt removed

Mods targeting multiple versions should include both supply systems or use version checks to load appropriate files.
