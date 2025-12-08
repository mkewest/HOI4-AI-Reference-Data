---
domain: military
concept: raids
version: 1.14+
requires: [defines]
relates: [operations, intel_agencies]
---

# Raids System

Raids are espionage-style actions with their own UI, targeting, and resolution rules.

## Core Structure

- **Categories & targeting**: Raids are grouped by category and target selection rules (country/region/asset). Ensure category tokens match UI definitions.
- **UI & icons**: Each raid uses defined icons/command power visuals; keep icons and map arrows aligned with category.
- **Command power & costs**: Costs scale per category; include cooldowns and prerequisites.

## Targeting & Execution

- **allowed / visible / available / launchable / launchable_from**: Gate selection, visibility, and origin; evaluate in country scope with target in FROM where applicable.
- **starting_point**: Define origin point if required; ensure it matches map/owner logic.
- **Unit models/equipment**: Specify participating units and equipment expectations; avoid empty equipment tokens.

## Outcomes & Intel

- **Success levels**: `failure`, `limitedsuccess`, `success`, `criticalsuccess` with factors per category.
- **Cooldowns**: Set per-raid cooldowns; avoid 0 to prevent spam.
- **Intel source**: Define intel gain/source tokens; align with operations/intel systems.

## Debug/Defines

- Uses raid-related defines (see `defines_list` where applicable).
- Test with debug tools to confirm targeting, cooldown, and outcome weighting.

