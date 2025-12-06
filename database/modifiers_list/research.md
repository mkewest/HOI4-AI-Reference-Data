---
domain: modifiers_list
concept: research
version: 1.14+
requires: [modifiers]
relates: [technologies_core]
---

# Research Modifiers

For modifier system mechanics, types, application methods, and critical behavioral edge cases, see [Modifier System](/scripting/modifiers.md).

Research modifiers affect technology research speed and doctrine purchase costs.

## Research and Doctrine

| Modifier | Type | Decimals | Description |
|----------|------|----------|-------------|
| `decryption` | num | 2 |  |
| `decryption_factor` | num | 2 |  |
| `encryption` | num | 2 |  |
| `encryption_factor` | num | 2 |  |
| `mobilization_speed` | num | 2 |  |
| `research_sharing_per_country_bonus` | num | 2 | Technology sharing bonus |
| `research_sharing_per_country_bonus_factor` | num | 2 |  |
| `research_speed_factor` | num | 2 |  |

> [!CRITICAL] Doctrine cost modifiers were added in version 1.11. These are PERCENTUAL modifiers: `-0.05 = 5% reduction`, NOT `-5`. They affect doctrine purchase cost only, NOT research speed.

Doctrine cost modifiers require the "cat_" prefix for specific doctrine lines:

```hoi4
# Specific doctrine line
cat_mobile_warfare_cost_factor = -0.10  # -10% to Mobile Warfare

# Branch-wide (no prefix needed)
land_doctrine_cost_factor = -0.15       # -15% to all land doctrines
air_doctrine_cost_factor = -0.10        # -10% to all air doctrines
naval_doctrine_cost_factor = -0.10      # -10% to all naval doctrines
```

## Related Systems

For technology definitions and research mechanics, see [Technology](/systems/technology.md).

For doctrine trees and effects, see [Doctrines](/military/doctrines.md).
