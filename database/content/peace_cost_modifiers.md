---
domain: content
concept: peace_cost_modifiers
version: 1.14+
requires: [triggers, effects]
relates: [decisions, modifiers_list]
---

# Peace Cost Modifiers

Scripted cost modifiers for peace actions are defined under `peace_action_modifiers` and adjust costs during peace conferences.

## Scopes

- `ROOT`: Negotiator country (who is doing the negotiation)
- `FROM`: Taker country (future owner)
- `FROM.FROM`: Giver country (previous owner)
- `FROM.FROM.FROM`: State (if the action targets a state)
- Inside nested scopes you may need to hop back (e.g., `ROOT.FROM`).

## Peace Action Types

Supported `peace_action_type` values include:
- `take_states`
- `puppet`
- `force_government`
- `liberate`

Single type or array is allowed (e.g., `{ puppet liberate }`).

## Definition Schema

```hoi4
peace_action_modifiers = {
    my_cost_mod = {
        category = is_core               # groups in tooltips; default is "other" if omitted
        peace_action_type = force_government  # single or array

        enable = {                       # triggers for activation; can use peace-conference-specific triggers
            ROOT = { has_government = democratic }
            ROOT.FROM = { tag = AUS }
            ROOT.FROM.FROM.FROM = { is_core_of = AUS }
        }

        cost_multiplier = 0.65           # > 0; all active multipliers multiply together
    }
}
```

## Guidance

- All active cost modifiers multiply together; keep values near ~0.4–3.0 to avoid extreme results.
- Use peace-conference-specific triggers (`pc_*`) for conditions that only exist during the conference (ownership/relations aren’t updated mid-conference).
- Keep `enable` lightweight; avoid expensive checks across many states/targets.

## Common vanilla patterns (examples)

Vanilla uses a set of standard modifiers by category and action type. Examples include:
- **Core/claims**: Cheaper if the taker has a core or claim; slightly cheaper if the target isn’t the loser’s core; more expensive if an ally major has a core on the target.
- **Occupation**: Cheaper when the negotiator controls the state (with compliance guardrails).
- **Ideology**: Ideology-based tweaks per action (e.g., democratic more expensive to take non-core states, cheaper to liberate; fascist cheaper to take states/puppet; communist adjustments for take/liberate/puppet).
- **Defensive war**: Adjust costs when the negotiator is (or was) in a defensive war against the loser.
- **Continuous political action**: Slight discounts when the target is already being forced/puppeted by the negotiator.
- **Special cases**: “Belonged to someone else,” “war of independence” adjustments, “dormant national identity” for unlikely tags.

These patterns illustrate typical multipliers (generally modest, e.g., ~0.25–1.3) and category usage for tooltip grouping.

