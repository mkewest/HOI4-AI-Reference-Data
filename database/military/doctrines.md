---
domain: military
concept: doctrines
version: 1.14+
requires: [technologies]
relates: [military_land]
---

# Doctrine System

Doctrines define land/air/naval combat philosophies through folders, grand doctrines, tracks, and subdoctrines. This page consolidates all doctrine structures in one place.

## Folders

Folders provide top-level categorization and UI framing.

- **Fields**: `name`, `background`, `frame`, `icon`, `allowed`, `ledger`/UI options.
- **Allowed**: Gate visibility/availability (DLC, tag, triggers); evaluated in country scope.
- **Links**: Each folder references its grand doctrines and tracks; keep icons/frames consistent across the folder.

## Grand Doctrines

Grand doctrines sit at the top of a folder and anchor its tracks.

- **Fields**: `xp_cost` / `xp_type`, `tracks` list, milestones, activation effects, `max_track_rows` / `max_track_columns`.
- **Activation**: Apply effects on selection; ensure scope correctness (country/army/navy/air).
- **UI**: Uses folder visuals; keep backgrounds/icons aligned with folder styling.

## Tracks

Tracks organize progression within a grand doctrine.

- **Fields**: `name` / `background` / `frame` / `icon`, `active` trigger, mastery multipliers/contributors, linkage to grand doctrines and subdoctrines.
- **Active trigger**: Controls whether the track is available; evaluate in country or relevant force scope.
- **Mastery**: Track-level mastery can modify rewards and multipliers; keep values consistent with subdoctrine rewards.

## Subdoctrines

Subdoctrines are the selectable steps within tracks.

- **Fields**: Root per track, `xp_cost` / `xp_type`, `available` / `visible`, reward chains / mastery overrides, `reward_gfx`, activation effects.
- **Rewards**: Apply effects/modifiers; ensure scope (country/unit) matches the reward intent.
- **Ordering**: Preserve track order to avoid UI/layout breakage and mismatched mastery progress.

## Mastery and Rewards

- **Mastery**: Multipliers/contributors at track and grand-doctrine level; avoid stacking beyond intended caps.
- **Rewards**: Use clear effect blocks; keep economic/combat modifiers scoped properly; note any doctrine-specific modifiers.
- **Visuals**: `reward_gfx` should match doctrine theme; ensure assets exist.

## Hooks, Triggers, and Modifiers

- Use scripted triggers/effects to gate availability and apply rewards.
- Reference modifier tokens from `modifiers_list` when granting bonuses; keep percent vs flat semantics correct.
- For XP costs, align `xp_type` with the doctrine’s branch (e.g., land/air/naval).

## Linking and Navigation

- Link to related systems: doctrine UI, research/tech overviews, mastery/reward explanations.
- Cross-link tracks and subdoctrines within this page for quick navigation.

