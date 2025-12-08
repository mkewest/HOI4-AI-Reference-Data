---
domain: defines_list
concept: NFactions
version: 1.17.2
requires: [defines]
relates: [factions]
---

```yaml
FACTION_INITIATIVE_CHANGE_RULE_COST:
  def: '1'
  type: int
  cmt: Cost of changing a faction rule (FI points)
FACTION_DOCTRINE_SHARING_UNLOCK_COST:
  def: '1'
  type: int
  cmt: Cost of unlocking doctrine sharing for one folder
DOCTRINE_SHARING_BASE_MASTERY_GAIN_MONTHLY:
  def: '10'
  type: int
  cmt: When doctrine sharing is enabled, this is the base amount of mastery gained
    monthly
DOCTRINE_SHARING_MONTHLY_MASTERY_GAIN_PER_COMMANDER:
  def: '2'
  type: int
  cmt: When doctrine sharing is enabled, each theater commander increases the montly
    mastery gain by this much
AI_FACTION_POWER_PROJECTION_TRESHOLD:
  def: '1000'
  type: int
  cmt: AI score is negative if faction's Power Projection value is below the treshold
AI_FACTION_POWER_PROJECTION_VALUE:
  def: '0.01'
  type: float
  cmt: AI score per Power Projection point
AI_MIN_POWER_PROJECTION_SCORE:
  def: '-100'
  type: int
  cmt: Min AI score for Power Projection
AI_MAX_POWER_PROJECTION_SCORE:
  def: '100'
  type: int
  cmt: Max AI score for Power Projection
FACTION_INFLUENCE_LEND_LEASE_FACTOR:
  def: '0.01'
  type: float
  cmt: how much the country's contribution in the faction affects its influence
FACTION_INFLUENCE_WAR_SCORE_FACTOR:
  def: '0.1'
  type: float
  cmt: how much the country's war score affects its influence
FACTION_INFLUENCE_EFFECTS_FACTOR:
  def: '1'
  type: int
  cmt: how much the effects affects its influence
FACTION_INFLUENCE_INDUSTRIAL_CAPACITY_FACTOR:
  def: '5'
  type: int
  cmt: how much the country's industry affects its influence
FACTION_INFLUENCE_GARRISON_SUPPORT_PROVIDER_FACTOR:
  def: '0.001'
  type: float
  cmt: how much the country's provided garrison support affects its influence
FACTION_INFLUENCE_GARRISON_SUPPORT_RECIEVER_FACTOR:
  def: '-0.001'
  type: float
  cmt: how much the country's received garrison support affects its influence
FACTION_INFLUENCE_EXPEDITIONARY_FORCE_PROVIDER_FACTOR:
  def: '0.01'
  type: float
  cmt: how much the country's provided expeditionary forces affects its influence
FACTION_CONTRIBUTION_SETTING_INCREASE:
  def: '0.01'
  type: float
  cmt: How big the steps are for increasing/decreasing contribution settings
FACTION_CONTRIBUTION_DEBT_LIMIT:
  def: '250'
  type: int
  cmt: How much you are allowed to be in debt from spending contribution
FACTION_INFLUENCE_EXPEDITIONARY_FORCE_RECIEVER_FACTOR:
  def: '-0.02'
  type: float
  cmt: how much the country's provided expeditionary forces affects its influence
FACTION_MANPOWER_GIVE_CONTRIBUTION_SCALAR:
  def: '0.1'
  type: float
  cmt: a scalar of how much contribution you get for giving a singular recruitable
    population to your faction
FACTION_MANPOWER_RECIEVE_CONTRIBUTION_SCALAR:
  def: '0.1'
  type: float
  cmt: a scalar for how much contribution it takes to get a singular recruitable
    population
FACTION_SCIENTIST_CONTRIBUTION_VALUE:
  def: '3'
  type: int
  cmt: how much contribution one scientists gives to you if it is working for somebody
    else.
ASSIGN_FACILITY_TO_FACTION_INITIATIVE_COST:
  def: '1'
  type: int
  cmt: The initiative cost of assigning a facility to a faction
FACTION_ASSIGN_SCIENTIST_COST:
  def: '25'
  type: int
  cmt: how much political power it costs to assign a supportive scientist
FACTION_UNLOCK_COMMANDER_COST:
  def: '1'
  type: int
  cmt: how much initiative it costs to create a new faction theater
FACTION_REPLACE_COMMANDER_COST:
  def: '1'
  type: int
  cmt: how much FI it costs to replace someone else's theater commander
FACTION_SUPREME_COMMANDER_EFFECTIVENESS:
  def: '0.2'
  type: float
  cmt: percentage value for how effective supreme commanders are compared to their
    regular position as FM/admiral.
FACTION_THEATER_COMMANDER_COUNTRY_LIMIT_BASE:
  def: '3'
  type: int
  cmt: base value for how many countries a theater commander can lead
FACTION_THEATER_COMMANDER_COUNTRY_LIMIT_SKILL_FACTOR:
  def: '1'
  type: int
  cmt: how much each skill level adds to the country limit
FACTION_THEATER_COMMANDER_REGION_LIMIT_BASE:
  def: '3'
  type: int
  cmt: Base value of the commander region limit
FACTION_THEATER_COMMANDER_REGION_LIMIT_SKILL_FACTOR:
  def: '1'
  type: int
  cmt: An increase to the region limit per commander skill level
FACTION_THEATER_COMMANDER_LAND_SUPPLY_USAGE_MODIFIER_BASE:
  def: '0'
  type: int
  cmt: Base value (percentage, negative = good)
FACTION_THEATER_COMMANDER_LAND_SUPPLY_USAGE_MODIFIER_SKILL_FACTOR:
  def: '-0.01'
  type: float
  cmt: Value per skill level (percentage, negative = good)
FACTION_THEATER_COMMANDER_NAVY_SUPPLY_USAGE_MODIFIER_BASE:
  def: '0'
  type: int
  cmt: Base value (percentage, negative = good)
FACTION_THEATER_COMMANDER_NAVY_SUPPLY_USAGE_MODIFIER_SKILL_FACTOR:
  def: '-0.01'
  type: float
  cmt: Value per skill level (percentage, negative = good)
FACTION_THEATER_COMMANDER_SECONDARY_BONUS:
  def: '0.5'
  type: float
  cmt: A value that scales the supply usage modifiers if a Land commander is giving the
    supply bonus to Navy and vice versa
THEATER_COMMANDER_LAND_EXPERIENCE_SCALE:
  def: '0.1'
  type: float
  cmt: How much experience the theater commander will gain from land combats (FM)
THEATER_COMMANDER_NAVY_EXPERIENCE_SCALE:
  def: '0.1'
  type: float
  cmt: How much experience the theater commander will gain from naval combats (Admiral)
BECOME_FACTION_LEADER_INFLUENCE_THRESHOLD:
  def: '0.4'
  type: float
  cmt: The min influence percentage for a country to be able to take over leadership in
    the faction
MAX_PROJECT_COUNT:
  def: '3'
  type: int
  cmt: The maximum number of projects a faction can have
AI_THEATER_CREATION_PENALTY:
  def: '2.5'
  type: float
  cmt: Penalty defines how much each theater reduces the chance linearly. (The higher,
    the worse the penalty is)
BECOME_FACTION_LEADER_INFLUENCE_WEIGHT:
  def: '1'
  type: int
  cmt: Importance of faction influence when determining how close a faction member is to
    being able to assume leadership.
FACTION_INFLUENCE_LEADER_BONUS:
  def: '200'
  type: int
  cmt: How much influence we are giving a faction member for being the leader
FACTION_TAKE_OVER_RELUCTANCE_VERSUS_HUMAN_INFLUENCE:
  def: '1.5'
  type: float
  cmt: Multiplier penalty for how much more influence is required an AI country compared
    to a human To assume leadership of faction.
AI_PICK_FROM_TOP_AMOUNT:
  def: '3'
  type: int
  cmt: AI Will spend choose from the top X to decide what to spent their initiative on,
    based on a weighted random
AI_PING_AREA_PRIORITY:
  def: '100'
  type: int
  cmt: added AI strategy value for pinged regions
AI_PING_FRONT_UNIT_REQUEST:
  def: '100'
  type: int
  cmt: added AI strategy value for pinged regions
AI_PING_FORCE_CONCENTRATION_FRONT_FACTOR:
  def: '100'
  type: int
  cmt: added AI strategy value for pinged regions
AI_PING_FORCE_CONCENTRATION_TARGET_WEIGHT:
  def: '100'
  type: int
  cmt: added AI strategy value for pinged regions
AI_PING_INVASION_UNIT_REQUEST:
  def: '100'
  type: int
  cmt: added AI strategy value for pinged regions
AI_PING_NAVAL_DOMINANCE:
  def: '100'
  type: int
  cmt: added AI strategy value for pinged regions
AI_PING_FORCE_CONCENTRATION_CAREFUL_FACTOR:
  def: '0.5'
  type: float
  cmt: AI strategy factor for FC in careful order execution mode
AI_PING_FORCE_CONCENTRATION_AGGRESSIVE_FACTOR:
  def: '1.2'
  type: float
  cmt: AI strategy factor for FC in aggressive order execution mode
RANK_FOR_SHINY_FLAG:
  def: '1'
  type: int
  cmt: Top N factions get a shiny flag on the factions screen. All that death was worth
    it.
PEACE_CONFERENCE_MINIMAL_REQUIREMENT:
  def: '0.5'
  type: float
  cmt: How much more faction power projection you need to have compared to the second
    biggest contesting faction / country to start recieving the
    PEACE_CONFERENCE_MAX_DISCOUNT e.g. 0.5 means you need to be 50% bigger
PEACE_CONFERENCE_MAX_DISCOUNT:
  def: '0.25'
  type: float
  cmt: How much % disount you get for being the bigger faction. Scales between the
    PEACE_CONFERENCE_MINIMAL_REQUIREMENT and 100% where at
    PEACE_CONFERENCE_MINIMAL_REQUIREMENT you get 0% and at 100% you will get
    PEACE_CONFERENCE_MAX_DISCOUNT
MAX_NUM_SHORT_TERM_GOALS:
  def: '1'
  type: int
  cmt: Maximum number of short term goals a faction can have at any one time
MAX_NUM_MEDIUM_TERM_GOALS:
  def: '1'
  type: int
  cmt: Maximum number of medium term goals a faction can have at any one time
MAX_NUM_LONG_TERM_GOALS:
  def: '1'
  type: int
  cmt: Maximum number of long term goals a faction can have at any one time
REPLACING_UNFINISHED_FACTION_GOAL_COST:
  def: '1'
  type: int
  cmt: The cost of replacing a goal if it is not finished
PASSIVE_INITIATIVE_GENERATION:
  def: '0.01'
  type: float
  cmt: How much initiative we are generating per day, scaled by manifest progress and
    influence%
MAX_FACTION_THEATERS:
  def: '4'
  type: int
  cmt: The maximum number of faction theaters that can be created
AI_FACTION_THEATER_TEMPLATE_SELECTION_RANDOMNESS:
  def: '1'
  type: int
  cmt: AI will pick a weighted random template from the top of the list
AI_FACTION_THEATER_COMMANDER_SELECTION_RANDOMNESS:
  def: '1'
  type: int
  cmt: AI will pick a weighted random template from the top of the list
FACTION_INTELLIGENCE_ALLOWED_ADVISOR_TRAIT:
  def:
    - ["head_of_intelligence"]
    - ["mastermind_code_cracker"]
    - ["expert_code_cracker"]
    - ["spymaster"]
    - ["spymaster_no_lar"]
    - ["commander_of_the_fetno_derash"]
    - ["commander_of_the_fetno_derash_no_lar"]
    - ["SWI_soviet_spy"]
    - ["SWI_intelligence_officer"]
    - ["special_envoy"]
    - ["BRA_soviet_spy"]
    - ["HUN_military_intelligence_officer"]
    - ["AUS_secretive_priest"]
    - ["AUS_veteran_head_of_agency"]
    - ["BEL_illusive_mastermind"]
    - ["GER_intelligence_coordinator"]
    - ["GER_secretary_of_state_security"]
    - ["GER_reich_security_main_office_director_lar"]
    - ["GER_reich_security_main_office_director_no_lar"]
    - ["head_of_the_abwehr"]
    - ["head_of_the_abwehr_improved"]
    - ["intelligence_service_deputy"]
    - ["PRC_multi_talented_diplomat_lar"]
    - ["PRC_multi_talented_diplomat_no_lar"]
    - ["PRC_trained_by_the_nkvd"]
    - ["PRC_spymaster"]
    - ["PHI_intelligence_bureau_chief"]
    - ["HUN_stalinist_agent"]
    - ["JAP_tokko_chief"]
    - ["CHI_spymaster"]
  type: table
FACTION_INTELLIGENCE_UNLOCK_COST:
  def: '1'
  type: int
FACTION_INTELLIGENCE_SHARING_BONUS:
  def: '0.05'
  type: float
  cmt: How much intelligence sharing one
FACTION_INTELLIGENCE_SHARING_SPY_SLOT_GAIN:
  def: '1'
  type: int
  cmt: How many operative slots an advisor position unlocks, excludes the spymaster
FACTION_INTELLIGENCE_HEAD_OF_CRYPTOLOGY_BONUS_COUNTRY:
  def: '0.1'
  type: float
  cmt: How much bonus the Head of Operations give to the country that holds that
    position
FACTION_INTELLIGENCE_HEAD_OF_CRYPTOLOGY_BONUS_OTHERS:
  def: '0.05'
  type: float
  cmt: How much bonus the Head of Operations give to the countries that dont hold that
    position
FACTION_INTELLIGENCE_HEAD_OF_OPERATIONS_BONUS_COUNTRY:
  def: '0.1'
  type: float
  cmt: How much bonus the Head of Operations give to the country that holds that
    position
FACTION_INTELLIGENCE_HEAD_OF_OPERATIONS_BONUS_OTHERS:
  def: '0.05'
  type: float
  cmt: How much bonus the Head of Operations give to the countries that dont hold that
    position
FACTION_INTELLIGENCE_HEAD_OF_COUNTER_INTEL_BONUS_COUNTRY:
  def: '0.1'
  type: float
  cmt: How much bonus the Head of Operations give to the country that holds that
    position
FACTION_INTELLIGENCE_HEAD_OF_COUNTER_INTEL_BONUS_OTHERS:
  def: '0.05'
  type: float
  cmt: How much bonus the Head of Operations give to the countries that dont hold that
    position
FACTION_DEFAULT_ICON:
  def: 'GFX_faction_logo_generic'
  type: string
  cmt: Faction icon when creating a generic faction in game that does not have an icon
    setup
FACTION_DEFAULT_TEMPLATE:
  def: 'faction_template_generic'
  type: string
  cmt: Default template that gets used if no template template is specified when playing
    with NCNS
AI_DAYS_TO_SELECT_GOAL:
  def: '14'
  type: int
```
