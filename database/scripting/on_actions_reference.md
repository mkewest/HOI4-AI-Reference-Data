---
domain: scripting
concept: on_actions_reference
version: 1.14+
requires: [on_actions_core, scopes]
relates: [events, effects]
---

# On Actions Reference

Complete enumeration of all on_actions with scope mappings and triggering conditions. For mechanisms and best practices, see [On Actions Core](/scripting/on_actions_core.md).

> [!NOTE] Updated for 1.14+/2024-11 hooks. When adding new on_actions from patches, document scope defaults and temp variables to avoid mis-scoping in scripts.

## Periodic On Actions

Execute at regular intervals during gameplay.

### on_startup

**Trigger:** First day after country selection (new game only, not on load)  
**Default Scope:** NONE - requires manual scoping  
**Random Events:** Not supported (no country scope)

```hoi4
on_startup = {
    effect = {
        every_country = {
            # Must scope manually
        }
    }
}
```

### on_daily

**Trigger:** Every day for every country  
**Default Scope:** Country (current country)  
**Performance:** Heavy - runs ~100+ times per day  
**Random Events:** Supported

> [!CRITICAL] Scoping into other countries creates duplicate executions. When ROOT scopes into TAG, the effect runs once for ROOT viewing TAG, then again when TAG is the active country. Multiply execution count by countries interacted with.

### on_daily_TAG

**Trigger:** Every day for specific tag  
**Default Scope:** Country (the specified tag)  
**Performance:** Efficient - single execution  
**Random Events:** Supported

Example: `on_daily_GER`, `on_daily_SOV`

### on_weekly

**Trigger:** When `num_days % 7 == 0`  
**Default Scope:** Country (current country)  
**Random Events:** Supported

### on_weekly_TAG

**Trigger:** Weekly for specific tag  
**Default Scope:** Country (the specified tag)  
**Random Events:** Supported

### on_monthly

**Trigger:** Monthly for every country  
**Default Scope:** Country (current country)  
**Random Events:** Supported

### on_monthly_TAG

**Trigger:** Monthly for specific tag  
**Default Scope:** Country (the specified tag)  
**Random Events:** Supported

## Political On Actions

### on_government_change

**Trigger:** Government ideology changes  
**Default Scope:** Country (changing government)  
**Cascade:** ALWAYS triggers `on_ruling_party_change`  
**Random Events:** Supported

```hoi4
on_government_change = {
    effect = {
        # ROOT/THIS = country changing government
    }
}
```

### on_ruling_party_change

**Trigger:** Ruling party changes (also triggered by `on_government_change`)  
**Default Scope:** Country  
**Special Variable:** `old_ideology_token` contains previous ideology  
**Random Events:** Supported

```hoi4
on_ruling_party_change = {
    effect = {
        # check_variable = { old_ideology_token = token:democratic }
    }
}
```

### on_new_term_election

**Trigger:** Election completes  
**Default Scope:** Country holding election  
**Random Events:** Supported

### on_stage_coup

**Trigger:** Coup attempt initiated  
**Default Scope:** Country experiencing coup  
**Random Events:** Supported

### on_coup_succeeded

**Trigger:** Coup succeeds  
**Default Scope:** Country where coup succeeded  
**Random Events:** Supported

## War On Actions

### on_declare_war

**Trigger:** War declared  
**Default Scope:** Country declaring war  
**FROM:** Target country  
**Random Events:** Supported

```hoi4
on_declare_war = {
    effect = {
        # ROOT = declarer
        # FROM = target
    }
}
```

### on_war

**Trigger:** War begins (any involvement type)  
**Default Scope:** Country entering war  
**Random Events:** Supported

### on_peace

**Trigger:** War ends  
**Default Scope:** Country exiting war  
**Random Events:** Supported

### on_war_relation_added

**Trigger:** Country added to existing war  
**Default Scope:** Country joining war  
**Random Events:** Supported

### on_capitulation

**Trigger:** Mid-capitulation (units deleted, equipment transferred)  
**Default Scope:** Capitulating country  
**FROM:** Country that caused capitulation  
**Sequence:** Fires AFTER `on_capitulation_immediate`  
**Random Events:** Supported

### on_capitulation_immediate

**Trigger:** Start of capitulation (units/equipment still exist)  
**Default Scope:** Capitulating country  
**FROM:** Country that caused capitulation  
**Sequence:** Fires BEFORE `on_capitulation`  
**Random Events:** Supported

Use this to save unit/equipment data before it's destroyed.

### on_uncapitulation

**Trigger:** Country exits capitulation  
**Default Scope:** Un-capitulating country  
**Random Events:** Supported

### on_annex

**Trigger:** Country annexed (also triggered by `on_civil_war_end`)  
**Default Scope:** Annexed country  
**FROM:** Annexing country  
**Random Events:** Supported

### on_civil_war_end

**Trigger:** Civil war concludes  
**Default Scope:** Losing side  
**FROM:** Winning side  
**Cascade:** ALWAYS triggers `on_annex`  
**Random Events:** Supported

### on_civil_war_end_before_annexation

**Trigger:** Civil war concludes before annexation processing  
**Default Scope:** Losing side  
**FROM:** Winning side  
**Random Events:** Supported

Earlier timing than `on_civil_war_end` - use for data preservation.

## Peace Conference On Actions

> [!CRITICAL] These on_actions fire ONLY during actual peace conferences, NOT when using equivalent effects like `puppet`, `release`, or `liberate`.

### on_before_peace_conference_start

**Trigger:** Before peace conference begins  
**Default Scope:** Country on winning side  
**Random Events:** Supported

### on_peaceconference_started

**Trigger:** Peace conference begins  
**Default Scope:** Country participating  
**Random Events:** Supported

### on_peaceconference_ended

**Trigger:** Peace conference concludes OR `white_peace` effect OR conditional surrender  
**Default Scope:** Country that participated  
**Random Events:** Supported

Also fires for scripted peace, not just formal conferences.

### on_puppet

**Trigger:** Country puppeted IN PEACE CONFERENCE  
**Default Scope:** Puppeted country  
**FROM:** Puppeting country  
**Exclusivity:** Peace conference only - NOT triggered by `puppet` effect  
**Random Events:** Supported

### on_liberate

**Trigger:** Country liberated IN PEACE CONFERENCE  
**Default Scope:** Liberated country  
**FROM:** Liberating country  
**Exclusivity:** Peace conference only - NOT triggered by `liberate`/`release` effects  
**Random Events:** Supported

### on_release_as_free

**Trigger:** Country released as free nation in peace conference  
**Default Scope:** Released country  
**FROM:** Releasing country  
**Random Events:** Supported

### on_release_as_puppet

**Trigger:** Country released as puppet FROM PEACETIME OCCUPIED TERRITORIES MENU  
**Default Scope:** Released puppet  
**FROM:** Releasing country  
**Exclusivity:** Occupied territories menu only - NOT peace conferences or effects  
**Random Events:** Supported

## Diplomatic On Actions

### on_guarantee

**Trigger:** Independence guarantee given  
**Default Scope:** Guarantor country  
**FROM:** Guaranteed country  
**Random Events:** Supported

### on_military_access

**Trigger:** Military access granted to another country  
**Default Scope:** Granting country  
**FROM:** Receiving country  
**Random Events:** Supported

### on_offer_military_access

**Trigger:** Military access offered  
**Default Scope:** Offering country  
**FROM:** Target country  
**Random Events:** Supported

### on_call_allies

**Trigger:** Allies called to war  
**Default Scope:** Calling country  
**Random Events:** Supported

### on_join_allies

**Trigger:** Country joins ally's war  
**Default Scope:** Joining country  
**FROM:** Ally that called  
**Random Events:** Supported

### on_lend_lease

**Trigger:** Lend-lease agreement signed  
**Default Scope:** Sending country  
**FROM:** Receiving country  
**Random Events:** Supported

### on_create_faction

**Trigger:** Faction created  
**Default Scope:** Faction leader  
**Random Events:** Supported

### on_join_faction

**Trigger:** Country joins faction  
**Default Scope:** Joining country  
**FROM:** Faction leader  
**Random Events:** Supported

### on_leave_faction

**Trigger:** Country leaves faction  
**Default Scope:** Leaving country  
**FROM:** Faction leader  
**Random Events:** Supported

## State On Actions

### on_state_control_changed

**Trigger:** State controller changes  
**Default Scope:** ROOT = old controller, FROM = new controller  
**Special Scope:** FROM.FROM = the state  
**Random Events:** Supported

> [!CRITICAL] Scope mapping is unusual - the state is accessed via `FROM.FROM`, not `FROM` or a direct scope.

```hoi4
on_state_control_changed = {
    effect = {
        # ROOT = old controller
        # FROM = new controller
        # FROM.FROM = the state
        FROM.FROM = {
            # State effects here
        }
    }
}
```

## Wargoal On Actions

### on_generate_wargoal

**Trigger:** Wargoal generated  
**Default Scope:** Country generating wargoal  
**FROM:** Target country  
**Random Events:** Supported

### on_justifying_wargoal_pulse

**Trigger:** During wargoal justification (periodic)  
**Default Scope:** Justifying country  
**FROM:** Target country  
**Random Events:** Supported

### on_wargoal_expire

**Trigger:** Wargoal expires unused  
**Default Scope:** Country with expired wargoal  
**FROM:** Target country  
**Random Events:** Supported

## Unit Leader On Actions

### on_unit_leader_created

**Trigger:** Unit leader created  
**Default Scope:** Character  
**FROM:** Owner country  
**Random Events:** Not supported (character scope)

### on_army_leader_daily

**Trigger:** Every day for every army leader  
**Default Scope:** Character (the leader)  
**Performance:** Heavy - runs for every leader daily  
**Random Events:** Not supported (character scope)

### on_army_leader_won_combat

**Trigger:** Army leader wins combat  
**Default Scope:** Character (the leader)  
**FROM:** Enemy division  
**Random Events:** Not supported (character scope)

### on_army_leader_lost_combat

**Trigger:** Army leader loses combat  
**Default Scope:** Character (the leader)  
**FROM:** Enemy division  
**Random Events:** Not supported (character scope)

### on_unit_leader_level_up

**Trigger:** Unit leader gains level  
**Default Scope:** Character (the leader)  
**Random Events:** Not supported (character scope)

### on_army_leader_promoted

**Trigger:** Unit leader promoted  
**Default Scope:** Character (the leader)  
**Random Events:** Not supported (character scope)

### on_unit_leader_promote_from_ranks

**Trigger:** Leader promoted from division ranks  
**Default Scope:** Character (the leader)  
**FROM:** Division unit  
**Special Scope:** FROM.OWNER = country (not FROM directly)  
**Random Events:** Not supported (character scope)

## Military On Actions

### on_nuke_drop

**Trigger:** Nuclear bomb dropped  
**Default Scope:** Bomber country  
**FROM:** Bombed state  
**Random Events:** Supported

### on_naval_invasion

**Trigger:** Naval invasion occurs  
**Default Scope:** THIS = invaded state (NOT ROOT)  
**Scope Note:** ROOT is not defined  
**Random Events:** Not supported (state scope)

```hoi4
on_naval_invasion = {
    effect = {
        # THIS = invaded state
        controller = {
            # Scope into controller country
        }
    }
}
```

### on_paradrop

**Trigger:** Paradrop occurs  
**Default Scope:** THIS = invaded state (NOT ROOT)  
**Scope Note:** ROOT is not defined  
**Random Events:** Not supported (state scope)

### on_pride_of_the_fleet_sunk

**Trigger:** Pride of the Fleet ship sunk  
**Default Scope:** Owning country  
**Random Events:** Supported

## Ace On Actions

### on_ace_promoted

**Trigger:** Pilot becomes ace  
**Default Scope:** Character (the ace)  
**FROM:** Country  
**Random Events:** Not supported (character scope)

### on_ace_killed

**Trigger:** Ace killed  
**Default Scope:** Character (the ace)  
**FROM:** Owning country  
**Random Events:** Not supported (character scope)

### on_ace_killed_by_ace

**Trigger:** Ace killed by enemy ace  
**Default Scope:** Character (killed ace)  
**FROM:** Character (killer ace)  
**Random Events:** Not supported (character scope)

### on_ace_killed_other_ace

**Trigger:** Ace kills enemy ace  
**Default Scope:** Character (killer ace)  
**FROM:** Character (killed ace)  
**Random Events:** Not supported (character scope)

## Intelligence On Actions

### on_operation_completed

**Trigger:** Intelligence operation completes  
**Default Scope:** Country running operation  
**FROM:** Operation scope  
**Random Events:** Supported

### on_operative_detected_during_operation

**Trigger:** Operative detected  
**Default Scope:** Operative's country  
**FROM:** Operation scope  
**Special Scope:** FROM.FROM = state (ONLY if operation has `selection_target`)  
**Random Events:** Supported

### on_operative_captured

**Trigger:** Operative captured  
**Default Scope:** Operative's country  
**FROM:** Capturing country  
**Random Events:** Supported

### on_operative_death

**Trigger:** Operative dies  
**Default Scope:** Character (the operative)  
**FROM:** Owning country  
**Random Events:** Not supported (character scope)

### on_operative_created

**Trigger:** Operative created  
**Default Scope:** Character (the operative)  
**FROM:** Owning country  
**Random Events:** Not supported (character scope)

### on_operative_recruited

**Trigger:** Operative recruited  
**Default Scope:** Character (the operative)  
**FROM:** Owning country  
**Random Events:** Not supported (character scope)

### on_fully_decrypted_cipher

**Trigger:** Cipher fully decrypted  
**Default Scope:** Decrypting country  
**FROM:** Target country  
**Random Events:** Supported

## MIO On Actions

### on_mio_size_increased

**Trigger:** MIO increases size/tier (1.13+)  
**Default Scope:** Country owning MIO  
**FROM:** MIO scope  
**Random Events:** Supported

### on_mio_design_team_assigned_to_tech

**Trigger:** Design team assigned to technology (1.13+)  
**Default Scope:** Country  
**Random Events:** Supported

### on_mio_design_team_assigned_to_variant

**Trigger:** Design team assigned to equipment variant (1.13+)  
**Default Scope:** Country  
**Random Events:** Supported

### on_mio_industrial_manufacturer_assigned

**Trigger:** Industrial manufacturer assigned (1.13+)  
**Default Scope:** Country  
**Random Events:** Supported

### on_mio_tech_research_cancelled

**Trigger:** MIO tech research cancelled (1.13+)  
**Status:** NON-FUNCTIONAL - does not fire  
**Random Events:** N/A

### on_mio_tech_research_completed

**Trigger:** MIO tech research completed (1.13+)  
**Status:** NON-FUNCTIONAL - does not fire  
**Random Events:** N/A

## Non-Working On Actions

### on_recall_volunteers

**Status:** Listed in code but completely non-functional  
**Random Events:** N/A

Do not use these in mods - they will never execute.

## Scope Mapping Summary

| On Action | Default Scope | FROM Scope | Special Notes |
|-----------|---------------|------------|---------------|
| on_startup | NONE | N/A | Must scope manually |
| on_naval_invasion | THIS (state) | N/A | ROOT not defined |
| on_paradrop | THIS (state) | N/A | ROOT not defined |
| on_state_control_changed | ROOT (old controller) | New controller | FROM.FROM = state |
| on_unit_leader_promote_from_ranks | Character | Division | FROM.OWNER = country |
| on_operative_detected_during_operation | Country | Operation | FROM.FROM = state (if selection_target) |

All other on_actions use standard ROOT = primary scope, FROM = secondary scope pattern.
