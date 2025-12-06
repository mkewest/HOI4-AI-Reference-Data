---
domain: modifiers_list
concept: ai_modifiers
version: 1.14+
requires: [modifiers]
relates: [ai_strategy]
---

# AI Modifiers

For modifier system mechanics, types, application methods, and critical behavioral edge cases, see [Modifier System](/scripting/modifiers.md).

AI modifiers adjust AI behavior weights and priorities. They do not directly control AI actions but influence decision-making calculations.

> [!CRITICAL] See AI_focuses#Modding for full implementation details. AI focus modifiers don't directly change AI behavior - they adjust weights in AI decision-making. Multiple focus modifiers can stack and compete.

## AI Behavior Weights

| Modifier | Type | Decimals | Description |
|----------|------|----------|-------------|
| `ai_badass_factor` | num | 1 | Threat receptivity |
| `ai_call_ally_desire_factor` | num | 0 |  |
| `ai_desired_divisions_factor` | num | 1 | How many divisions country aims to produce |
| `ai_focus_aggressive_factor` | num | 1 | AI Focus on Offense |
| `ai_focus_aviation_factor` | num | 1 |  |
| `ai_focus_defense_factor` | num | 1 | AI Focus on Defense |
| `ai_focus_military_advancements_factor` | num | 1 |  |
| `ai_focus_military_equipment_factor` | num | 1 |  |
| `ai_focus_naval_air_factor` | num | 1 |  |
| `ai_focus_naval_factor` | num | 1 |  |
| `ai_focus_peaceful_factor` | num | 1 |  |
| `ai_focus_war_production_factor` | num | 1 |  |
| `ai_get_ally_desire_factor` | num | 0 | Desire to be in/expand faction |
| `ai_join_ally_desire_factor` | num | 0 |  |
| `ai_license_acceptance` | num | 0 | Acceptance when requesting to buy license |

## Usage Notes

AI modifiers affect the priority calculations the AI uses when making strategic decisions. Higher values make the AI more likely to pursue that strategy, but do not guarantee the behavior. The AI still considers other factors like resources, threats, and opportunities.

For example, `ai_focus_aggressive_factor = 1.0` increases the weight of offensive operations, but the AI will still defend if necessary.

## Related Systems

For AI strategy and behavior documentation, see [AI System](/systems/ai.md).
