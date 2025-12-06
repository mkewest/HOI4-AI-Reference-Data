---
domain: defines_list
concept: NAI
version: 1.14+
requires: [defines]
relates: [ai_strategy, ai_modifiers]
---

```yaml
GARRISON_FRACTION:
  def: '0.0'
  type: float
  cmt: How large part of a front should always be holding the line rather than advancing
    at the enemy
DIPLOMATIC_ACTION_GOOD_BAD_RATIO_THRESHOLD:
  def: '1'
  type: int
DIPLOMATIC_ACTION_RANDOM_FACTOR:
  def: '0.5'
  type: float
  cmt: How much of the AI diplomatic action scoring is randomly determined (1.0 =
    half random, 2.0 = 2/3rd random, etc)
DILPOMATIC_ACTION_DECLARE_WAR_WARGOAL_BASE:
  def: '50'
  type: int
  cmt: Base diplomatic action score bonus to go to war per wargoal
DIPLOMACY_CREATE_FACTION_FACTOR:
  def: '0.75'
  type: float
  cmt: Factor for AI desire to create a new faction. Val < 1.0 makes it less likely
    to create than to join.
DIPLOMACY_FACTION_SAME_IDEOLOGY_MAJOR:
  def: '10'
  type: int
  cmt: AI bonus acceptance when being asked about faction is a major of the same ideology
DIPLOMACY_FACTION_GLOBAL_TENSION_FACTOR:
  def: '0.2'
  type: float
  cmt: How much the AI takes global tension into account when considering faction
    actions
DIPLOMACY_FACTION_TAKE_OVER_RELUCTANCE_VERSUS_HUMAN:
  def: '2.0'
  type: float
  cmt: Multiplier penalty for how much stronger than a human faction member an AI
    country must be to choose to assume faction leadership.
DIPLOMACY_FACTION_PLAYER_JOIN:
  def: '20'
  type: int
  cmt: Bonus for human players asking to join a faction.
DIPLOMACY_IMPROVE_RELATION_COST_FACTOR:
  def: '5.0'
  type: float
  cmt: Desire to boost relations subtracts the cost multiplied by this
DIPLOMACY_SEND_ATTACHE_COST_FACTOR:
  def: '5.0'
  type: float
  cmt: Desire to send attache substracts the cost multiplied by this
DIPLOMACY_REJECTED_WAIT_MONTHS_BASE:
  def: '4'
  type: int
  cmt: AI will not repeat offers until at least this time has passed, and at most
    the double
DIPLOMACY_CALL_ALLY_VALIDITY_DURATION:
  def: '1'
  type: int
  cmt: Overwrite above value for CallAlly and JoinAlly diplo action. This is however
    fixed, and is not subject to randomness. Also, this is the time the AI will keep
    the action in its incoming queue without declining it.
DIPLOMACY_SEND_MAX_FACTION:
  def: '0.75'
  type: float
  cmt: Country should not send away more units than this as expeditionaries
DIPLOMACY_ACCEPT_ATTACHE_BASE:
  def: '50'
  type: int
  cmt: Base value of attache acceptance (help is welcome)
DIPLOMACY_ACCEPT_ATTACHE_OPINION_PENALTY:
  def: '-100'
  type: int
  cmt: Value of acceptance penalty if the opinion too low
DIPLOMACY_FACTION_SURRENDER_LEVEL:
  def: '20'
  type: int
  cmt: How much the recipient nation losing matters for joining a faction
DIPLO_DISTANCE_BETWEEN_CAPITALS:
  def: '-340'
  type: int
  cmt: Max scaled malus from distance between capitals
DIPLO_SHOW_FACTION_JOIN_WARNING_THRESHOLD:
  def: '-20'
  type: int
  cmt: Show warning if declare-war target is this close to accepting or being sent
    a faction invitiation
RESEARCH_DAYS_BETWEEN_WEIGHT_UPDATE:
  def: '7'
  type: int
  cmt: Refreshes need scores based on country situation.
RESEARCH_LAND_DOCTRINE_NEED_GAIN_FACTOR:
  def: '0.15'
  type: float
  cmt: Multiplies value based on relative military industry size / country size.
RESEARCH_AIR_DOCTRINE_NEED_GAIN_FACTOR:
  def: '0.07'
  type: float
  cmt: Multiplies value based on relative number of air base / country size.
RESEARCH_AHEAD_BONUS_FACTOR:
  def: '4.0'
  type: float
  cmt: To which extent AI should care about ahead of time bonuses to research
RESEARCH_YEARS_BEHIND_FACTOR:
  def: '0.2'
  type: float
  cmt: To which extent AI should care about not falling behind (i.e. increase weight
    for old tech)
RESEARCH_LENGTH_FACTOR:
  def: '3'
  type: int
  cmt: To which extent AI should care about how long it takes to research something
    (it prefers short research times)
RESEARCH_AHEAD_OF_TIME_FACTOR:
  def: '4.0'
  type: float
  cmt: To which extent AI should care about ahead of time penalties to research
DECLARE_WAR_RELATIVE_FORCE_FACTOR:
  def: '0.5'
  type: float
  cmt: Weight of relative force between nations that consider going to war
MIN_DELIVERED_TRADE_FRACTION:
  def: '0.8'
  type: float
  cmt: AI will cancel trade deals that are not able to deliver more than this fraction
    of the agreed amount
MINIMUM_GOOD_TRADE_RATIO_PER_CIV:
  def: '0.005'
  type: float
  cmt: for each civ factory we have mul with this we are allowed to trade under %
    of resource on a trade
PRODUCTION_EQUIPMENT_SURPLUS_FACTOR:
  def: '0.5'
  type: float
  cmt: Base value for how much of currently used equipment the AI will at least strive
    to have in stock
AIR_SUPERIORITY_FACTOR:
  def: '2.5'
  type: float
  cmt: Factor for air superiority score
ROCKET_MIN_PRIO_ASSIGN_SCORE:
  def: '50'
  type: int
  cmt: Minimum total score for region to be considered for critical rocket air missions
MAX_VOLUNTEER_ARMY_FRACTION:
  def: '0.25'
  type: float
  cmt: Countries will not send more than their forces time this number to aid another
    country
DEPLOY_MIN_EQUIPMENT_SURRENDER_FACTOR:
  def: '0.90'
  type: float
  cmt: Required percentage of equipment (1.0 = 100%) for AI to deploy unit in wartime
    while surrender progress is higher than 0
DEPLOY_MIN_EQUIPMENT_PEACE_FACTOR:
  def: '0.98'
  type: float
  cmt: Required percentage of equipment (1.0 = 100%) for AI to deploy unit in peacetime
DEPLOY_MIN_EQUIPMENT_WAR_FACTOR:
  def: '0.95'
  type: float
  cmt: Required percentage of equipment (1.0 = 100%) for AI to deploy unit in wartime
DYNAMIC_STRATEGIES_THREAT_FACTOR:
  def: '4.0'
  type: float
  cmt: How much threat generated by other countries effects generated strategies
EQUIPMENT_MARKET_UPDATE_FREQUENCY_DAYS:
  def: '11'
  type: int
  cmt: How often the AI runs its market logic
EQUIPMENT_MARKET_BASE_MARKET_RATIO:
  def: '0.2'
  type: float
  cmt: The AI tries to keep ca this ratio of equipment surplus for sale on the market.
    Gets modified by equipment_market_for_sale_factor AI strategy.
EQUIPMENT_MARKET_NR_DELIVERIES_SOFT_MAX:
  def: '10'
  type: int
  cmt: AI tries to adjust assigned factories and amount of equipment to keep nr deliveries
    at max this
EQUIPMENT_MARKET_WANTED_CONVOY_USAGE_RATIO:
  def: '0.3'
  type: float
  cmt: If the AI's available/free/unused convoys is reduced to this ratio (0.3 = 30
    %), start buying convoys.
EQUIPMENT_MARKET_CONTRACT_EFFICIENCY_TO_CANCEL:
  def: '0.1'
  type: float
  cmt: If contract efficiency stays below this, the AI will cancel the contract
EQUIPMENT_MARKET_SHORTAGE_DAYS_TO_CANCEL:
  def: '30'
  type: int
  cmt: If equipment deficit will take more than these many days to fix, the AI will
    cancel the contract
EQUIPMENT_MARKET_MAX_CONVOY_RATIO_FOR_MARKET_WAR:
  def: '0.25'
  type: float
  cmt: Max ratio of total convoys to use for equipment trade while at war
EQUIPMENT_MARKET_SCORE_FACTOR_CIC_VALUE_NEEDED:
  def: '8.0'
  type: float
  cmt: Score coefficient for CicValueNeeded (high is prio)
EQUIPMENT_MARKET_SCORE_FACTOR_COST_PER_UNIT:
  def: '-5.0'
  type: float
  cmt: Score coefficient for SubsidizedCostPerUnit (low is good)
EQUIPMENT_MARKET_SCORE_FACTOR_DIPLO_OPINION:
  def: '1.0'
  type: float
  cmt: Score coefficient for DiploOpinion, mainly used as tie breaker (high is good)
DIPLOMACY_ACCEPT_CONDITIONAL_SURRENDER_GLOBAL_TENSION:
  def: '-10'
  type: int
  cmt: Multiplied by WT
DIPLOMACY_ACCEPT_CONDITIONAL_SURRENDER_EMBARGO:
  def: '2'
  type: int
  cmt: Multiplied by num embargo, max 5 embargo
DIPLOMACY_ACCEPT_CONDITIONAL_SURRENDER_MINOR_WAR:
  def: '10'
  type: int
  cmt: Applied if recipient is a minor nation (and therefore there are no majors in
    this war)
NUM_RESOURCES_TO_ALLOW_MINOR_EMBARGO:
  def: '69'
  type: int
  cmt: If we or any of our puppets have more total resources of a single category
    that this, we will consider embargoing countries
OPINION_CUTOFF_FOR_IMPROVE_RELATIONS:
  def: '80'
  type: int
  cmt: AI will never consider improving relations if above this opinion with target.
DEFAULT_MODULE_VARIANT_CREATION_XP_CUTOFF_NAVY:
  def: '50'
  type: int
  cmt: Same as above but for the ship designer.
DEFAULT_LEGACY_VARIANT_CREATION_XP_CUTOFF_LAND:
  def: '35'
  type: int
  cmt: Army XP needed before attempting to create a variant of a type that uses the
    legacy upgrades system. ai_strategy supports land_xp_spend_priority upgrade_xp_cutoff.
    If none is set, this define is used instead.
DEFAULT_LEGACY_VARIANT_CREATION_XP_CUTOFF_AIR:
  def: '25'
  type: int
  cmt: Same as above but for air XP and air_xp_spend_priority.
VARIANT_CREATION_XP_RESERVE_NAVY:
  def: '50'
  type: int
  cmt: Same as above but for navy XP.
LAND_DESIGN_ALTERNATIVE_ABSENT:
  def: '1000000'
  type: int
  cmt: The AI uses the below values when selecting which design to make among the
    types that use the tank designer (the tank designer DLC feature must be active).
    For each role, the highest priority AI design that can be created, if any, is
    assigned a weight. Any design with a weight of zero or a weight that falls below
    the cutoff is dropped. A random design is then picked from the remaining. Weight
    is calculated as AlternativeFactor * DemandFactor. An "alternative" is a producible
    design of the same archetype (each specialized type is its own archetype).
LAND_DESIGN_ALTERNATIVE_OF_EQUAL_TECH:
  def: '100'
  type: int
LAND_DESIGN_DEMAND_FIELD_DIVISION:
  def: '20'
  type: int
  cmt: If a template may be reinforced with the archetype it's considered to be "demanded".
    If multiple conditions are met, e.g. it's both in the field and in training, the
    largest value is used.
LAND_DESIGN_DEMAND_GARRISON_DIVISION:
  def: '10'
  type: int
LAND_DESIGN_DEMAND_ABSENT:
  def: '0'
  type: int
AIR_DESIGN_ALTERNATIVE_ABSENT:
  def: '1000000'
  type: int
  cmt: See above documentation.
AIR_DESIGN_ALTERNATIVE_OF_EQUAL_TECH:
  def: '100'
  type: int
AIR_DESIGN_DEMAND_MAX:
  def: '33'
  type: int
  cmt: The AI desires to produce equipment at a certain rate per archetype, and demand
    is determined per archetype relative to the least and most desired counts.
AIR_DESIGN_DEMAND_ABSENT:
  def: '0'
  type: int
DESIRE_USE_XP_TO_UNLOCK_LAND_DOCTRINE:
  def: '0.5'
  type: float
  cmt: The AI "desires" to spend XP on doctrines, templates, and equipment. The desire
    is built up over time and when XP is available it spends it on the action that
    has the highest accumulated desire. After spending XP the desire is reset, in
    effect balancing the desires. Below is the daily desire gain for each action.
    How quickly is desire to unlock land doctrines accumulated?
DESIRE_USE_XP_TO_UNLOCK_AIR_DOCTRINE:
  def: '0.5'
  type: float
  cmt: How quickly is desire to unlock air doctrines accumulated?
DESIRE_USE_XP_TO_UPGRADE_LAND_EQUIPMENT:
  def: '1.0'
  type: float
  cmt: How quickly is desire to update/create land equipment variants accumulated?
DESIRE_USE_XP_TO_UPGRADE_AIR_EQUIPMENT:
  def: '1.0'
  type: float
  cmt: How quickly is desire to update/create air equipment variants accumulated?
DESIRE_USE_XP_TO_UNLOCK_NAVY_SPIRIT:
  def: '0.20'
  type: float
  cmt: How quickly is desire to unlock naval spirits accumulated?
DAYS_BETWEEN_CHECK_BEST_DOCTRINE:
  def: '7'
  type: int
  cmt: Recalculate desired best doctrine to unlock with this many days inbetween.
DAYS_BETWEEN_CHECK_BEST_EQUIPMENT:
  def: '7'
  type: int
  cmt: Recalculate desired best equipment to upgrade with this many days inbetween.
UNLOCK_SPIRIT_MODIFIER_FACTOR:
  def: '0.05'
  type: float
  cmt: Factor for AI's evaluated value of the modifiers connected to the spirit
UNLOCK_SPIRIT_TRUNCATION_SELECT_THRESHOLD:
  def: '0.8'
  type: float
  cmt: Valid between [0.0, 1.0]. When unlocking spirits, select randomly from all
    spirits with AI score >= VALUE * HighestSpiritScore. To always select the best,
    set this value to 1.0. To select fully randomly, set this value to 0.0.
PLAN_VALUE_TO_EXECUTE:
  def: '-0.5'
  type: float
  cmt: AI will typically avoid carrying out a plan it below this value (0.0 is considered
    balanced).
CALL_ALLY_BASE_DESIRE:
  def: '20'
  type: int
  cmt: exactly what it says
CALL_ALLY_NEUTRAL_DESIRE:
  def: '25'
  type: int
  cmt: Desire to call ally added for neutral AI
CALL_ALLY_COMMUNIST_DESIRE:
  def: '75'
  type: int
  cmt: Desire to call ally added for communist AI
CALL_ALLY_OVERLORD_INVITE_PUPPET:
  def: '20'
  type: int
  cmt: Desire for an overlord to call its puppet into the war
CALL_ALLY_RELATIVE_ARMY_STRENGTH_THRESHOLD:
  def: '1.5'
  type: float
  cmt: If our relative army strength ratio is less than this (compared to all enemies),
    increase desire to call allies
CALL_ALLY_RELATIVE_ARMY_STRENGTH_MAX:
  def: '100.0'
  type: float
  cmt: Max desire value for relative army strength (lerping between zero and this
    based on the threshold)
CALL_ALLY_LOSING_WAR_MAX:
  def: '100.0'
  type: float
  cmt: Max desire value for losing war (lerping between zero and this based on the
    threshold)
CALL_ALLY_JOINER_HAS_ENEMY_NEIGHBOR:
  def: '100'
  type: int
  cmt: If the joining country is neighbor to at least one of the enemies, increase
    desire this much
MIN_AI_UNITS_PER_TILE_FOR_STANDARD_COHESION:
  def: '1.5'
  type: float
  cmt: How many units should we have for each tile along a front in order to switch
    to standard cohesion (less moving around)
JOIN_ALLY_BASE_DESIRE:
  def: '20'
  type: int
  cmt: exactly what it says
JOIN_ALLY_NEUTRAL_DESIRE:
  def: '25'
  type: int
  cmt: Desire to join ally added for neutral AI
JOIN_ALLY_COMMUNIST_DESIRE:
  def: '75'
  type: int
  cmt: Desire to join ally added for communist AI
LENDLEASE_FRACTION_OF_PRODUCTION:
  def: '0.5'
  type: float
  cmt: Base fraction AI would send as lendlease
MINIMUM_EQUIPMENT_TO_ASK_LEND_LEASE:
  def: '-100'
  type: int
  cmt: AI will accept to lend lease this equipment only if our stockpile is less than
    that.
MINIMUM_FUEL_DAYS_TO_ASK_LEND_LEASE:
  def: '2'
  type: int
  cmt: AI will accept to lend lease fuel only if the player have less fuel than this
    number multiply by his max daily consumption.
DEFAULT_SUPPLY_TRUCK_BUFFER_RATIO:
  def: '1.5'
  type: float
  cmt: ai will set to truck buffer ratio to this. can be modified by wanted_supply_trucks
    min_wanted_supply_trucks ai strats
POLITICAL_IDEA_MIN_SCORE:
  def: '0.1'
  type: float
  cmt: Only replace or add an idea if score is above this score.
CHIEF_ADDED_WEIGHT_FACTOR:
  def: '12.5'
  type: float
  cmt: Weight multiplier for chief roles over other advisor or idea types
GARRISON_TEMPLATE_SCORE_MANPOWER_FACTOR:
  def: '0.05'
  type: float
  cmt: formula is (template_ic * ic_factor + template_manpower * manpower_factor )
    / template_supression (lower is better)
ADVISOR_SCORE_CHEAPER_IS_BETTER_FACTOR:
  def: '0.1'
  type: float
  cmt: When scoring advisors, this define scales how much the AI prefers cheaper advisors
    over more expensive ones. 0.0 means no effect, 0.15 means a cost difference of
    100 PP modifies the score by 15 %.
EVAL_MODIFIER_NON_PERCENT_FACTOR:
  def: '0.1'
  type: float
  cmt: stuff related to how the AI evaluates/scores how useful modifiers are Multiply
    non-percent-based modifiers with this to put the values in the approximately same
    range so they can be compared. (Why we are using 0.1 and not 0.01? No idea...)
EVAL_MODIFIER_MAX_COMMAND_POWER_FACTOR:
  def: '0.01'
  type: float
  cmt: Increasing CP cap with x is maybe 100 times less useful than e.g. gaining x
    more XP per day
MIN_AI_SCORE_TO_ECONOMY_LAW_OVERRIDE_HARD_CODED_SCORE:
  def: '0.0'
  type: float
MIN_AI_SCORE_TO_ALL_LAWS_OVERRIDE_HARD_CODED_SCORE:
  def: '0.0'
  type: float
NEIGHBOUR_WAR_THREAT_FACTOR:
  def: '1.10'
  type: float
  cmt: How much increase in threat does AI feel against neighbours who are at war
POTENTIAL_FUTURE_ENEMY_FACTOR:
  def: '100'
  type: int
  cmt: How much increase in threat does AI feel against neighbours who at war with
    our allies
DIFFERENT_FACTION_THREAT:
  def: '30'
  type: int
  cmt: Threat caused by not being in the same faction
PLAN_ATTACK_MIN_ORG_FACTOR_LOW:
  def: '0.85'
  type: float
  cmt: Minimum org % for a unit to actively attack an enemy unit when executing a
    plan
PLAN_ATTACK_MIN_ORG_FACTOR_MED:
  def: '0.7'
  type: float
  cmt: (LOW,MED,HIGH) corresponds to the plan execution agressiveness level.
PLAN_ATTACK_MIN_ORG_FACTOR_HIGH:
  def: '0.45'
  type: float
PLAN_FRONTUNIT_DISTANCE_FACTOR:
  def: '10.0'
  type: float
  cmt: Factor for candidate units distance to front positions.
PLAN_STEP_COST_LIMIT:
  def: '9'
  type: int
  cmt: When stepping to draw a plan this cost makes it break if it hits hard terrain
    (multiplied by number of desired steps)
PLAN_FRONT_SECTION_MAX_LENGTH:
  def: '18'
  type: int
  cmt: When a front is longer than this it will be split in two sections for the AI
PLAN_MIN_SIZE_FOR_FALLBACK:
  def: '50'
  type: int
  cmt: A country with less provinces than this will not draw fallback plans, but rather
    station their troops along the front
SEND_VOLUNTEER_EVAL_MAJOER_POWER:
  def: '1.0'
  type: float
  cmt: How willing major powers are to send volunteers.
GIVE_STATE_CONTROL_MIN_CONTROLLED:
  def: '1'
  type: int
  cmt: AI needs to control more than this number of states before considering giving
    any away
RELATIVE_STRENGTH_TO_INVADE:
  def: '0.08'
  type: float
  cmt: Compares the estimated strength of the country/faction compared to it's enemies
    to see if it should invade or stay at home to defend.
GIVE_STATE_CONTROL_BASE_SCORE:
  def: '50'
  type: int
  cmt: Base diplo score for giving away control of states
GIVE_STATE_CONTROL_NEIGHBOR_SCORE:
  def: '20'
  type: int
  cmt: Diplo score for each neighboring state controlled by the target
GIVE_STATE_CONTROL_NEIGHBOR_OTHER_SCORE:
  def: '5'
  type: int
  cmt: Diplo score for each neighboring state controlled by someone else
GIVE_STATE_CONTROL_DIST_SCORE_MULT:
  def: '0.2'
  type: float
  cmt: Multiplier for the score gained from distance ( GIVE_STATE_CONTROL_MAX_SCORE_DIST
    - distance ) * this
GENERATE_WARGOAL_THREAT_BASELINE:
  def: '1.0'
  type: float
  cmt: Value of 200 should give 0.3% chance of Stalin going for instance crazy and
    conquering all of America The baseline for what the AI considers the world is
    getting dangerous and we want to generate wargoals with no antagonize value
RESERVE_TO_COMMITTED_BALANCE:
  def: '0.3'
  type: float
  cmt: How many reserves compared to number of committed divisions in a combat (1.0
    = as many as reserves as committed)
MAIN_ENEMY_FRONT_IMPORTANCE:
  def: '4.0'
  type: float
  cmt: How much extra focus the AI should put on who it considers to be its current
    main enemy.
AI_FRONT_MOVEMENT_FACTOR_FOR_READY:
  def: '0.25'
  type: float
  cmt: If less than this fraction of units on a front is moving, AI sees it as ready
    for action
DECLARE_WAR_MIN_FRONT_SIZE_TO_CONSIDER_FOR_NOT_READY:
  def: '0.04'
  type: float
  cmt: fronts with less armies than this ratio compared to total number of armies
    are ignored when ai checks if it is ready for war
VP_MAX_PROVINCE_WORTH:
  def: '500'
  type: int
  cmt: Max worth a province can have to a defensive order
AREA_DEFENSE_CAPITAL_PEACE_VP_WEIGHT:
  def: '{ 1.0, 1.0, 1.0 }'
  type: array
  cmt: these are all 3 numbers for min, desired, max unit need weights for area defense
AREA_DEFENSE_HOME_VP_WEIGHT:
  def: '{ 0.0, 0.5, 1.0 }'
  type: array
AREA_DEFENSE_CAPITAL_PEACE_COAST_WEIGHT:
  def: '{ 0.0, 0.0, 0.0 }'
  type: array
AREA_DEFENSE_HOME_COAST_WEIGHT:
  def: '{ 0.0, 0.1, 0.5 }'
  type: array
AREA_DEFENSE_CAPITAL_PEACE_BASE_WEIGHT:
  def: '{ 0.0, 0.0, 0.0 }'
  type: array
AREA_DEFENSE_HOME_BASE_WEIGHT:
  def: '{ 0.5, 1.0, 1.0 }'
  type: array
ESTIMATED_CONVOYS_PER_DIVISION:
  def: '6'
  type: int
  cmt: Not always correct, but mainly used to make sure AI does not go crazy
FRONT_TERRAIN_DEFENSE_FACTOR:
  def: '3.75'
  type: float
  cmt: Multiplier applied to unit defense modifier for terrain on front province multiplied
    by terrain importance
BASE_DISTANCE_TO_CARE:
  def: '600.0'
  type: float
  cmt: Countries that are too far away are less interesting in diplomacy
ORG_UNIT_STRONG:
  def: '0.75'
  type: float
  cmt: Organization % for unit to be considered strong
ORG_UNIT_WEAK:
  def: '0.25'
  type: float
  cmt: Organization % for unit to be considered weak
ORG_UNIT_NORMAL:
  def: '0.35'
  type: float
  cmt: Organization % for unit to be considered normal
PLAN_FACTION_STRONG_TO_EXECUTE:
  def: '0.50'
  type: float
  cmt: '% or more of units in an order to consider executing the plan'
PLAN_FACTION_WEAK_TO_ABORT:
  def: '0.65'
  type: float
  cmt: '% or more of units in an order to consider executing the plan'
REDEPLOY_DISTANCE_VS_ORDER_SIZE:
  def: '1.0'
  type: float
  cmt: Factor applied to the path length of a unit compared to length of an order
    to determine if it should use strategic redeployment
PLAN_VALUE_FORTIFICATION_LEVEL_MAX_PENALTY:
  def: '-0.5'
  type: float
  cmt: Max plan value penalty from fortification. This is scaled by number of provinces
    along a frontline, over the number which exceed the fort value value above
TRANSFER_DANGER_HOSTILE_SHIPS:
  def: '50'
  type: int
  cmt: max danger from complete enemy naval supriority over ai in an area
OPERATION_EQUIPMENT_NEED_PRODUCTION_MULT:
  def: '1.0'
  type: float
  cmt: equipment requests for operations will be added the equipment needs that ai
    considers while assigning factories to production
MIN_FUEL_RATIO_TO_NOT_IGNORE_INVASION_SUPPORT_COST:
  def: '0.0'
  type: float
  cmt: ai will still naval invasion support forces unless fuel ratio drops below this
    one
HOURS_BETWEEN_ENCIRCLEMENT_DISCOVERY:
  def: '72'
  type: int
  cmt: Per army, interval in hours between refresh of which provinces it considers
    make up potential encirclement points
FASCISTS_BEFRIEND_DEMOCRACIES:
  def: '-25'
  type: int
FASCISTS_ALLY_FASCISTS:
  def: '0'
  type: int
FASCISTS_ALLY_COMMUNISTS:
  def: '-100'
  type: int
FASCISTS_ANTAGONIZE_DEMOCRACIES:
  def: '100'
  type: int
DEMOCRACIES_BEFRIEND_FASCISTS:
  def: '-25'
  type: int
DEMOCRACIES_BEFRIEND_COMMUNISTS:
  def: '-25'
  type: int
DEMOCRACIES_ALLY_DEMOCRACIES:
  def: '0'
  type: int
DEMOCRACIES_ANTAGONIZE_FASCISTS:
  def: '0'
  type: int
DEMOCRACIES_ANTAGONIZE_COMMUNISTS:
  def: '0'
  type: int
COMMUNISTS_BEFRIEND_DEMOCRACIES:
  def: '-25'
  type: int
COMMUNISTS_ALLY_FASCISTS:
  def: '-100'
  type: int
COMMUNISTS_ALLY_COMMUNISTS:
  def: '0'
  type: int
COMMUNISTS_ANTAGONIZE_DEMOCRACIES:
  def: '10'
  type: int
TENSION_MIN_FOR_GUARANTEE_VS_MINOR:
  def: '10'
  type: int
  cmt: for non faction people AI will not consider you worth guaranteeing below this
DIPLOMACY_FACTION_WAR_WANTS_HELP:
  def: '50'
  type: int
  cmt: Desire to send to nations to join a faction if you are at war
FACTION_UNSTABLE_ACCEPTANCE:
  def: '-100'
  type: int
DIPLOMACY_FACTION_JOIN_COUP_INITIATOR_BONUS:
  def: '70'
  type: int
  cmt: If a country initiated coup on an another country, civil war revolter is more
    likely to join initiator's faction
NEEDED_NAVAL_FACTORIES_EXPENSIVE_SHIP_BONUS:
  def: '12'
  type: int
  cmt: Amount of naval yards you need to get a bonus to building really expensive
    ships
HEAVILY_FORTIFIED_RATIO_TO_CONSIDER_A_FRONT_FORTIFIED:
  def: '0.5'
  type: float
  cmt: ai will consider a front super fortified if this ratio of provinces has lots
    of forts
DESPERATE_AI_MIN_UNIT_ASSIGN_TO_ESCAPE:
  def: '0'
  type: int
  cmt: AI will assign at least this amount of units to break from desperate situations
DESPERATE_AI_MIN_ORG_BEFORE_ATTACK:
  def: '0.3'
  type: float
  cmt: ai will wait for this much org to attack an enemy prov in desperate situations
DESPERATE_ATTACK_WITHOUT_ORG_WHEN_NO_ORG_GAIN:
  def: '120'
  type: int
  cmt: if ai can't regain enough org to attack in this many hours, it will go truly
    desperate and attack anyway (still has to wait for move org)
CASUALTY_RATIO_TO_PULL_EXPEDITIONARIES_BACK:
  def: '0.1'
  type: float
  cmt: AI will pull expeditioniries back if its casualties is aboce this ratio compared
    to their total deployed manpower
SURRENDER_LEVEL_TO_PULL_EXPEDITIONARIES_BACK:
  def: '0.3'
  type: float
  cmt: AI will pull expeditioniries back if its surrender level is above this ratio
EXPEDITIONARY_CASUALTY_DECAY_RATIO:
  def: '0.3333'
  type: float
  cmt: expeditionary manpower lost will decay by thousands daily by this ratio (compared
    to deployed manpower)
ACCESS_SCORE_FOR_DEMOCRATIC_COUNTRIES:
  def: '500'
  type: int
  cmt: democracies gives each other access if they have a common enemy
ACCESS_SCORE_PENALTY_PER_EXISTING_ACCESS_AT_WAR:
  def: '250'
  type: int
  cmt: each access reduces the desire of next access
NAVAL_ACCESS_SCORE_PENALTY_PER_EXISTING_ACCESS_AT_WAR:
  def: '150'
  type: int
NAVAL_SUPREMACY_WEIGHT_PER_DIVISION_ON_INVASION_ORDER:
  def: '6'
  type: int
  cmt: adds to supremacy requests for regions with active or pending naval invasions
TOO_INSIGNIFICANT_MAX_PENALTY:
  def: '350'
  type: int
  cmt: max penalty that will be applied for thinking a country is too insignificant
WANTED_UNITS_THREAT_BASE:
  def: '0.7'
  type: float
  cmt: If no threat, multiply min wanted units by this
WANTED_UNITS_WAR_THREAT_FACTOR:
  def: '1.15'
  type: float
  cmt: Factor threat with this if country is at war. this value is overriden by the
    value in ideology database if that value exceedes this.
WANTED_UNITS_MANPOWER_DIVISOR:
  def: '21000'
  type: int
  cmt: Normalizing divisor for AI manpower. (for each x max available manpower, they
    want one division)
WANTED_UNITS_WEIGHT_FACTORIES:
  def: '0.45'
  type: float
  cmt: Weight of military factories when computing final nr wanted units
WANTED_UNITS_MIN_DEFENCE_FACTOR:
  def: '0.4'
  type: float
  cmt: Factor on units required for min defence
WANTED_LAND_PLANES_PER_BASE_CAPACITY_FACTOR:
  def: '1'
  type: int
  cmt: Scales how many land-based planes the AI want per air base space (excluding
    carriers).
WANTED_LAND_PLANES_TOTAL_MAX_PER_DIVISION:
  def: '100'
  type: int
  cmt: The max total number of land-based planes the AI want.
WANTED_CARRIER_PLANES_PER_CARRIER_CAPACITY_IN_PRODUCTION_FACTOR:
  def: '1'
  type: int
  cmt: Scales how many carrier planes the AI want per deck space of carriers in production.
START_TRAINING_EQUIPMENT_LEVEL:
  def: '0.95'
  type: float
  cmt: ai will not start to train if equipment drops below this level
BUILD_REFINERY_LACK_OF_RESOURCE_MODIFIER:
  def: '0.003'
  type: float
  cmt: How much lack of resources are worth when evaluating what to build.
DIVISION_DESIGN_MANPOWER_WEIGHT:
  def: '0.005'
  type: float
DIVISION_DESIGN_COMBAT_WIDTH_WEIGHT:
  def: '-1.0'
  type: float
  cmt: This score is reduced the higher width is when comparing pure changes with
    no target
DIVISION_DESIGN_MAX_FAILED_DAYS:
  def: '60'
  type: int
  cmt: max days we keep track of since failure of a template design update
EQUIPMENT_DESIGN_MAX_FAILED_DAYS:
  def: '60'
  type: int
  cmt: max days we keep track of since failure of an equipment design update
UPGRADE_PERCENTAGE_OF_FORCES:
  def: '0.03'
  type: float
  cmt: How big part of the army that should be considered for upgrading
REFIT_SHIP_PERCENTAGE_OF_FORCES:
  def: '0.1'
  type: float
  cmt: How big part of the navy that should be considered for refitting
INVASION_COASTAL_PROVS_PER_ORDER:
  def: '24'
  type: int
  cmt: AI will consider one extra invasion per number of provinces stated here (num
    orders = total coast / this)
CONVOY_NEED_SAFETY_BUFFER:
  def: '1.30'
  type: float
  cmt: AI will try and keep 15% more convoys than what it needs.
REGION_THREAT_LEVEL_TO_AVOID_REGION:
  def: 25*10
  type: mixed
  cmt: How much threat must be generated in region ( by REGION_THREAT_PER_SUNK_CONVOY
    ) so the AI will decide to mark the region as avoid
REGION_CONVOY_DANGER_DAILY_DECAY:
  def: '1'
  type: int
  cmt: When convoys are sunk it generates threat in the region which the AI uses to
    prio nalval missions
PLAN_ACTIVATION_MAJOR_WEIGHT_FACTOR:
  def: '1.5'
  type: float
  cmt: AI countries will hold on activating plans if stronger countries have plans
    in the same location. Majors count extra (value of 1 will negate this)
AREA_DEFENSE_BASE_IMPORTANCE:
  def: '30'
  type: int
  cmt: Area defense order base importance value (used for determining order of troop
    selections)
AREA_DEFENSE_IMPORTANCE_FACTOR:
  def: '1.0'
  type: float
  cmt: used to balance defensive area importance vs other fronts
MAX_DISTANCE_NAVAL_INVASION:
  def: '200.0'
  type: float
  cmt: AI is extremely unwilling to plan naval invasions above this naval distance
    limit.
MIN_SUPPLY_USE_SANITY_CAP:
  def: '100'
  type: int
  cmt: Ignore supply cap if below this value when deciding on how many divisions to
    produce.
MISSING_CONVOYS_BOOST_FACTOR:
  def: '50.0'
  type: float
  cmt: The more convoys a country is missing, the more resources it diverts to cover
    this.
MAX_MICRO_ATTACKS_PER_ORDER:
  def: '3'
  type: int
  cmt: AI goes through its orders and checks if there are situations to take advantage
    of
PRODUCTION_MAX_PROGRESS_TO_SWITCH_NAVAL:
  def: '0.1'
  type: float
  cmt: AI will not replace ships being built by newer types if progress is above this
PRODUCTION_WAIT_TO_FINISH_IF_CHEAP:
  def: '0.75'
  type: float
  cmt: If produced item is cheap (producing more than one/week), wait to finish item
    if progress is above this
FORCE_FACTOR_AGAINST_EXTRA_MINOR:
  def: '0.15'
  type: float
  cmt: AI considers generating wargoals against minors below this % of force compared
    to themselves to get at a bigger enemy.
NAVAL_MISSION_DISTANCE_BASE:
  def: '3500'
  type: int
  cmt: Base value when AI is evaluating distance score to places
NAVAL_MISSION_AGGRESSIVE_PATROL_DIVISOR:
  def: '1'
  type: int
  cmt: Divides patrol score when not defending
NAVAL_MISSION_PATROL_NEAR_OWNED:
  def: '500'
  type: int
  cmt: Extra patrol mission score near owned provinces
NAVAL_MISSION_PATROL_NEAR_CONTROLLED:
  def: '120'
  type: int
  cmt: Extra patrol mission score near controlled provinces
NAVAL_MISSION_MINES_PLANTING_NEAR_OWNED:
  def: '40000'
  type: int
NAVAL_MISSION_MINES_SWEEPING_NEAR_OWNED:
  def: '60000'
  type: int
  cmt: How likely the AI will do the sweeping missions. The value is scaled by the
    amount of mines to sweep.
NEW_LEADER_EXTRA_CP_FACTOR:
  def: '2.0'
  type: float
  cmt: Country must have at least this many times extra command power to get new admirals
    or army leaders
ATTACK_HEAVILY_DEFENDED_LIMIT:
  def: '0.5'
  type: float
  cmt: AI will not launch attacks against heavily defended fronts unless they consider
    to have this level of advantage (1.0 = 100%)
MIN_PLAN_VALUE_TO_MICRO_INACTIVE:
  def: '0.25'
  type: float
  cmt: The AI will not consider members of groups which plan is not activated AND
    evaluates lower than this.
DESIRED_UNITS_FACTOR_AREA_ORDER:
  def: '0.7'
  type: float
  cmt: Factor for desired number of units to assign to area defense orders
MAX_UNITS_FACTOR_FRONT_ORDER:
  def: '1.0'
  type: float
  cmt: Factor for max number of units to assign to area front orders
MIN_UNITS_FACTOR_FRONT_ORDER:
  def: '1.0'
  type: float
  cmt: Factor for min number of units to assign to area front orders
DESIRED_UNITS_FACTOR_INVASION_ORDER:
  def: '1.0'
  type: float
  cmt: Factor for desired number of units to assign to naval invasion orders
FRONT_UNITS_CAP_FACTOR:
  def: '15.0'
  type: float
  cmt: A factor applied to total front size and supply use. Primarily effects small
    fronts
MIN_FIELD_STRENGTH_TO_BUILD_UNITS:
  def: '0.7'
  type: float
  cmt: Cancel unit production if below this to get resources out to units in the field
AVERAGE_SUPPLY_USE_PESSIMISM:
  def: '1.5'
  type: float
  cmt: Multiplier for when AI calculates average supply use of entire army.
PROPOSE_LEND_LEASE_AIDESIRE_SAME_IDEOLOGY_CIVIL_WAR:
  def: '25'
  type: int
  cmt: Added to AI desire to propose lend lease if recipent is same ideology and they
    are currently in civil war
SEND_VOLUNTEER_AIDESIRE_SAME_IDEOLOGY_CIVIL_WAR:
  def: '25'
  type: int
  cmt: Added to AI desire to send volunteers if recipent is same ideology and they
    are currently in civil war
REQUEST_LEND_LEASE_CONTAINS_VALUE:
  def: '100'
  type: int
  cmt: Limit of contain enemy desire for boosting friendly help
FRONT_BULGE_RATIO_LOWER_CUTOFF:
  def: '0.95'
  type: float
  cmt: If local bulginess drops below this, a point of interest is found
INVASION_DISTANCE_RANDOMNESS:
  def: '300'
  type: int
  cmt: This higher the value, the more unpredictable the invasions. Compares to actual
    map distance in pixels.
DAYS_BETWEEN_AIR_PRIORITIES_UPDATE:
  def: '4'
  type: int
  cmt: Amount of days between air ai updates priorities for air wings ( from 1 to
    N )
NAVAL_SHIP_AIR_IMPORTANCE:
  def: '2.0'
  type: float
  cmt: Naval ship air importance
NAVAL_COMBAT_AIR_IMPORTANCE:
  def: '8.0'
  type: float
  cmt: Naval combat air importance
NAVAL_COMBAT_TRANSFER_AIR_IMPORTANCE:
  def: '50.0'
  type: float
  cmt: Naval combat involving enemy land units
NAVAL_COMBAT_OUR_NAVY_MULT_ON_IMPORTANCE:
  def: '0.35'
  type: float
  cmt: Naval region importance are scaled by our ships as well
NAVAL_COMBAT_MIN_OUR_NAVY_MULT_ON_IMPORTANCE:
  def: '0.5'
  type: float
  cmt: Min scale factor for naval region importance from our ships
NAVAL_RANGE_FOR_DOCKING_RIGHTS_CHECK:
  def: '240.0'
  type: float
  cmt: Naval range used to check if docking rights would allow us to reach a specific
    province
NAVAL_PATROL_PLANES_PER_SHIP_RAIDING:
  def: '10.0'
  type: float
  cmt: Amount of naval patrol planes per ship on a convoy raid mission
NAVAL_FIGHTERS_PER_PLANE:
  def: '1.0'
  type: float
  cmt: Amounts of air superiority planes requested per enemy plane
NAVAL_STRIKE_PLANES_PER_SHIP:
  def: '20'
  type: int
  cmt: Amount of bombers requested per enemy ship
MINES_SWEEPING_PLANES_PER_MAX_MINES:
  def: '150'
  type: int
  cmt: Amount of air planes request for mines sweeping when there is max amount of
    mines planted by enemy in certain region
MINES_PLANTING_DESIRE_PER_HOME_STATE:
  def: '0.4'
  type: float
  cmt: Scoring for how much do we want to plant naval mines with our air wings if
    the naval region is adjacent to a home state. Multiple adjacent states increases
    the score. Max sum of score is 1.0.
MINES_PLANTING_DESIRE_PER_NAVAL_THREAT:
  def: '250'
  type: int
  cmt: How much threat must be generated in the naval region, in order to get the
    maximum desire to plant naval mines in there.
DEMOCRATIC_AI_FACTION_KICKING_PLAYER_THREAT_DIFFERENCE:
  def: '6.0'
  type: float
  cmt: World threat generation difference needed to kick a player from a democratic
    faction
LAND_DEFENSE_AIR_SUPERIORITY_IMPORTANCE:
  def: '1.0'
  type: float
  cmt: Strategic importance of air superiority ( amount of enemy planes in area )
LAND_DEFENSE_MILITARY_FACTORY_IMPORTANCE:
  def: '70'
  type: int
  cmt: Strategic importance of military factories
LAND_DEFENSE_SUPPLY_HUB_IMPORTANCE:
  def: '4'
  type: int
  cmt: Strategic importance of supply hubs
LAND_DEFENSE_INFRA_IMPORTANCE_FACTOR:
  def: '0.5'
  type: float
  cmt: Factor of infrastructure influence on strategic importance ( 0.0 - 1.0 )
NUM_HOURS_SINCE_LAST_COMBAT_TO_SUPPORT_UNITS_VIA_AIR:
  def: '72'
  type: int
  cmt: units will be considered in combat if they are just out of their last combat
    for air supporting
LAND_DEFENSE_FIGHERS_PER_PLANE:
  def: '1.8'
  type: float
  cmt: Amount of air superiority planes requested per enemy plane
LAND_DEFENSE_INTERSEPTORS_PER_PLANE:
  def: '0.1'
  type: float
  cmt: Amount of air interceptor planes requested per enemy plane (non bomber)
LAND_COMBAT_OUR_ARMIES_AIR_IMPORTANCE:
  def: '20'
  type: int
  cmt: Strategic importance of our armies
LAND_COMBAT_FRIEND_ARMIES_AIR_IMPORTANCE:
  def: '10'
  type: int
  cmt: Strategic importance of friendly armies
LAND_COMBAT_ENEMY_ARMIES_AIR_IMPORTANCE:
  def: '12'
  type: int
  cmt: Strategic importance of our armies
LAND_COMBAT_ENEMY_COASTAL_FORTS_AIR_IMPORTANCE:
  def: '3'
  type: int
  cmt: Strategic importance of enemy coastal fronts in the region
LAND_COMBAT_FIGHTERS_PER_PLANE:
  def: '1.0'
  type: float
  cmt: Amount of air superiority planes requested per enemy plane
LAND_COMBAT_CAS_PER_ENEMY_ARMY:
  def: '30'
  type: int
  cmt: Amount of CAS planes requested per enemy division
LAND_COMBAT_CAS_PER_COMBAT:
  def: '60'
  type: int
  cmt: Amount of CAS requested per combat
LAND_COMBAT_BOMBERS_PER_COASTAL_FORT_LEVEL:
  def: '6'
  type: int
  cmt: Amount of bomber planes requested per enemy coastal fort level
LAND_COMBAT_INTERCEPT_PER_PLANE:
  def: '0.25'
  type: float
  cmt: Amount of interception planes requested per enemy plane
AIR_SUPERIORITY_FOR_FRIENDLY_CAS_RATIO:
  def: '0.75'
  type: float
  cmt: Demand at least this proportion of our cas planes as air superiority regardless
    of other needs
ENEMY_PASSING_THROUGH_PLANES_PER_BOMBER:
  def: '0.1'
  type: float
  cmt: Amount of planes we assign to intercept enemies en-route to a location
ENEMY_PASSING_THROUGH_PLANES_PER_SUPPORT:
  def: '0.1'
  type: float
  cmt: Amount of planes we assign to intercept enemies en-route to a location
MAX_AIR_REGIONS_TO_CARE_ABOUT:
  def: '6'
  type: int
  cmt: Number of regions we'll consider when trying to split planes a bit. Split is
    NOT equal, just a guide, leftovers still applied elsewhere if needed
ENEMY_PASSING_THROUGH_PLANES_PER_FIGHTER_NAVAL_REGION:
  def: '0.15'
  type: float
  cmt: Amount of planes we assign to intercept enemies en-route to a location over
    a sea region
NAVAL_DEFENSE_INTERCEPTION_IMPORTANCE_FACTOR:
  def: '30'
  type: int
  cmt: Factor on added planes passing through region to strategic importance
RESEARCH_WITH_XP_AI_WEIGHT_MULT:
  def: '1.2'
  type: float
  cmt: AI will bump score of a research with this mult if it can use XP
STR_BOMB_CIVIL_FACTORY_IMPORTANCE:
  def: '50'
  type: int
  cmt: Strategic importance of enemy civil factories
STR_BOMB_NAVAL_FACTORY_IMPORTANCE:
  def: '30'
  type: int
  cmt: Strategic importance of enemy naval factories
STR_BOMB_AA_IMPORTANCE_FACTOR:
  def: '0.5'
  type: float
  cmt: Factor of AA influence on strategic importance ( 0.0 - 1.0 )
STR_BOMB_IMPORTANCE_SCALE:
  def: '1.0'
  type: float
  cmt: str bombing total importance scale (every str bombing score get's multiplied
    by it)
STR_BOMB_FIGHTERS_PER_PLANE:
  def: '1.1'
  type: float
  cmt: Amount of air superiority planes requested per enemy plane
STR_BOMB_PLANES_PER_MIL_FACTORY:
  def: '25'
  type: int
  cmt: Amount of planes requested per enemy military factory
STR_BOMB_PLANES_PER_SUPPLY_HUB:
  def: '3'
  type: int
  cmt: Amount of planes requested per enemy supply node
RECON_PLANES_NAVAL:
  def: '50'
  type: int
  cmt: scale on recon for naval areas
RECON_PLANES_STRATEGIC:
  def: '50'
  type: int
  cmt: scale on recon for strategic areas
ASSIGN_FRONT_ARMY_HARD_ATTACK_FACTOR:
  def: '0.1'
  type: float
  cmt: Importance of unit's ARMY_HARD_ATTACK stat when assigning to a front
ASSIGN_DEFENSE_ARMY_DEFENSE_FACTOR:
  def: '3.0'
  type: float
  cmt: Importance of unit's ARMY_DEFENSE stat when assigning to an area defense order
ASSIGN_DEFENSE_TEMPLATE_CLASS_SCORE:
  def: '3.0'
  type: float
  cmt: Importance of unit's AI template class (AREA_DEFENSE, CAVALRY) when assigning
    to an area defense order
ORDER_ASSIGNMENT_DISTANCE_FACTOR:
  def: '100.0'
  type: float
  cmt: When the AI assigns units to orders, how much should distance be taken into
    account?
UNIT_ASSIGNMENT_STATS_IMPORTANCE:
  def: '3.0'
  type: float
  cmt: Stats score for units are multiplied by this when the AI is deciding which
    front they should be assigned to
ASSIGN_FRONT_TERRAIN_DEFENSE_FACTOR:
  def: '1.0'
  type: float
  cmt: Importance of unit's terrain adjusted defense stat when assigning to a front
ASSIGN_DEFENSE_TERRAIN_ATTACK_FACTOR:
  def: '0.5'
  type: float
  cmt: Importance of unit's terrain adjusted attack stat when assigning to an area
    defense order
ASSIGN_DEFENSE_TERRAIN_MOVEMENT_FACTOR:
  def: '0.5'
  type: float
  cmt: Importance of unit's terrain adjusted movement stat when assigning to an area
    defense order
ASSIGN_TANKS_TO_MOUNTAINS:
  def: '-6.0'
  type: float
  cmt: factor for assigning tank divisions to fronts with mountains (proportional
    to how much of that terrain type)
UNIT_ASSIGNMENT_TERRAIN_IMPORTANCE:
  def: '10.0'
  type: float
  cmt: Terrain score for units are multiplied by this when the AI is deciding which
    front they should be assigned to
ASSIGN_TANKS_TO_NON_WAR_FRONT:
  def: '0.4'
  type: float
  cmt: Scoring factor for assigning divisions with 'role = armor' or 'front_role_override
    = offence' to non-war fronts
REASSIGN_TO_ANOTHER_FRONT_IF_IN_COMBAT_FACTOR:
  def: '0.2'
  type: float
  cmt: Factor for reassigning to another front if in combat. 0.0  1.0 means want to.
ENEMY_FORTIFICATION_FACTOR_FOR_FRONT_REQUESTS_MAX:
  def: '0.7'
  type: float
  cmt: max factor that can be added by enemy fortification
PLAN_ACTIVATION_SUPERIORITY_AGGRO:
  def: '1.0'
  type: float
  cmt: How aggressive a country is in activating a plan based on how superiour their
    force is.
MAX_CARRIER_OVERFILL:
  def: '1.85'
  type: float
  cmt: Carriers will be overfilled to this amount if there are doctrines to justify
    it
FIELDED_MANPOWER_BUFFER_RATIO_FOR_OCCUPATION_AI:
  def: '0.3'
  type: float
  cmt: garrison ai will try to leave this ratio of buffers while assigning laws
DOCKYARDS_PER_NAVAL_DESIRE_EFFECT:
  def: '-20.0'
  type: float
  cmt: Effects how much AI wants to build dockyards based on how navally focused they
    are in general. Recommended range -100.0 to 100.0.
DESIGN_COMPANY_SCORE_MULTIPLIER:
  def: '1.25'
  type: float
  cmt: score multiplier for hiring a design company
AIR_CHIEF_SCORE_MULTIPLIER:
  def: '1.5'
  type: float
  cmt: score multiplier for hiring an air chief
POLITICAL_ADVISOR_SCORE_MULTIPLIER:
  def: '1.25'
  type: float
  cmt: score multiplier for hiring political advisors
MIN_SCALED_IDEA_WEIGHT_TO_COMPARE_WITH_DECISIONS:
  def: '100'
  type: int
  cmt: idea scores are scaled between these two values while comparing them to decisions
CRITICAL_DECISION_PRIORITY:
  def: '200'
  type: int
  cmt: critical ai score for decisions, ai will be able to pick decisions if it has
    higher prio even if it is not time to pick them (0 to disable)
MAX_PP_TO_SPEND_ON_LOWER_PRIO_TASKS:
  def: '25'
  type: int
  cmt: max pp cost for ai to allow spend pp on lower prio things while a higher prio
    things are available
LOW_PRIO_TEMPLATE_BONUS_FOR_GARRISONS:
  def: '1000'
  type: int
  cmt: bonus to make ai more likely to assign low prio units to garrisons
DEPLOYED_UNIT_MANPOWER_RATIO_TO_BUFFER_WARTIME:
  def: '0.2'
  type: float
  cmt: deployment will try to buffer a ratio of deployed manpower (for reinforcements)
    during war time
MAX_AVAILABLE_MANPOWER_RATIO_TO_BUFFER_WARTIME:
  def: '0.4'
  type: float
  cmt: deployment will try to buffer a ratio of manpower (for reinforcements) during
    war time
MANPOWER_RATIO_REQUIRED_TO_PRIO_MOBILIZATION_LAW:
  def: '0.4'
  type: float
  cmt: percentage of manpower in field is desired to be buffered for AI when it has
    upcoming wars or already at war. if it has less manpower, it will prio manpower
    laws
GIE_EXILE_AIR_MANPOWER_USAGE_RATIO:
  def: '0.2'
  type: float
  cmt: AI will not deploy new exile wings when this percentage of available exile
    manpower is already used for wing recruitment.
CAPITAL_TASKFORCE_MAX_CAPITAL_COUNT:
  def: '12'
  type: int
  cmt: optimum capital count for capital taskforces
SUB_TASKFORCE_MAX_SHIP_COUNT:
  def: '16'
  type: int
  cmt: optimum sub count for sub taskforces
CAPITALS_TO_CARRIER_RATIO:
  def: '1.5'
  type: float
  cmt: capital to carrier count in carrier taskfoces
MIN_MAIN_SHIP_RATIO:
  def: '0.3'
  type: float
  cmt: if main ship ratio is below this, steal other ships.
MIN_MAIN_SHIP_RATIO_TO_REINFORCE:
  def: '0.5'
  type: float
  cmt: the main ships will be tried to reinforce this level.
MIN_MAIN_SHIP_TO_SPARE:
  def: '0.7'
  type: float
  cmt: can only steal ships from a task force if their main ship ratio is above this.
MIN_MAIN_SHIP_RATIO_TO_MERGE:
  def: '0.7'
  type: float
  cmt: try merge task force if main ship ratio is lower than this.
MAIN_SHIP_RATIO_TO_SPLIT:
  def: '1.8'
  type: float
  cmt: if main ship ratio in a task force is larger than this, split it. (If a carrier
    TF wants 4 carriers (see defines above), but it has more than [this * 4] carriers,
    then we try to split the TF.)
MIN_NAVAL_MISSION_PRIO_TO_ASSIGN:
  def: '{ 0, 200, 200, 200, 100, 200, 100, 0, 0, 100 }'
  type: array
  cmt: priorities for regions to get assigned to a mission HOLD (consumes fuel HOLD_MISSION_MOVEMENT_COST
    fuel while moving) PATROL STRIKE FORCE CONVOY RAIDING CONVOY ESCORT MINES PLANTING
    MINES SWEEPING TRAIN RESERVE_FLEET NAVAL INVASION SUPPORT
MAX_MISSION_PER_TASKFORCE:
  def: '{ 0, 1.5, 6, 1.5, 4, 2, 2, 0, 0, 10 }'
  type: array
  cmt: max mission region/taskforce ratio HOLD (consumes fuel HOLD_MISSION_MOVEMENT_COST
    fuel while moving) PATROL STRIKE FORCE CONVOY RAIDING CONVOY ESCORT MINES PLANTING
    MINES SWEEPING TRAIN RESERVE_FLEET NAVAL INVASION SUPPORT
MAX_SCREEN_TASKFORCES_FOR_CONVOY_DEFENSE_MAX:
  def: '0.70'
  type: float
  cmt: maximum ratio of all screen-ships forces to be used in convoy defense (increases
    up to max as AI loses convoys).
MAX_SCREEN_TASKFORCES_FOR_CONVOY_DEFENSE_MAX_CONVOY_THREAT:
  def: '1500'
  type: int
  cmt: AI will increase screen assignment for escort missions as threate increases
MAX_SCREEN_TASKFORCES_FOR_MINE_SWEEPING_PRIO:
  def: '0.8'
  type: float
  cmt: if you have mines near your owned states, you will start priotize mine missions
    and will assign this ratio of screens
MAX_SCREEN_TASKFORCES_FOR_MINE_SWEEPING_PRIO_MAX_MINES:
  def: '1000'
  type: int
  cmt: highest mines for highest prio for mine missions
MAX_SCREEN_FORCES_FOR_INVASION_SUPPORT:
  def: '0.25'
  type: float
  cmt: max ratio of screens forces to be used in naval invasion missions
MAX_PATROL_TO_STRIKE_FORCE_RATIO:
  def: '3.0'
  type: float
  cmt: maximum patrol/strike force ratio
CONSTRUCTION_PRIO_CIV_FACTORY:
  def: '0.80'
  type: float
  cmt: base prio for civilian factories in the construction queue
CONSTRUCTION_PRIO_RAILWAY:
  def: '4.00'
  type: float
  cmt: base prio for railways in the construction queue
CONSTRUCTION_PRIO_UNSPECIFIED:
  def: '0.50'
  type: float
  cmt: base prio for unspecified buildings (none of the categories above) in the construction
    queue
CONSTRUCTION_PRIO_FACTOR_OWNED_NONCORE:
  def: '1.50'
  type: float
  cmt: factor prio with this if owned non-core territory
CONSTRUCTION_PRIO_FACTOR_REPAIRING:
  def: '0.30'
  type: float
  cmt: factor prio with this if building is being repaired
MAX_FACTORY_TO_SPARE_FOR_CRITICAL_MISSION_FUEL_TRADE:
  def: '0.3'
  type: float
  cmt: amount of factories to spend on oil trade in case of fuel need for prio missions
FUEL_TRADE_PRIO_FOR_CONVOY_DEFENSE:
  def: '0.3'
  type: float
  cmt: AI will be less reluctant to cancel convoy missions if it is trading for oil
MAX_FACTORY_TO_SPARE_FOR_CRITICAL_MISSION_FUEL_TRADE_IN_PEACE:
  def: '0.1'
  type: float
  cmt: amount of factories to spend on oil trade in case of fuel need for prio missions
    in peace time
FUEL_REQUEST_RATIO_FOR_COMBATS:
  def: '0.6'
  type: float
  cmt: ratio of ship combat fuel cost that is to be considered in fuel usage and request
    system
FUEL_REQUEST_RATIO_FOR_MOVEMENT:
  def: '0.4'
  type: float
  cmt: ratio of ship movement fuel cost that is to be considered in fuel usage and
    request system
NAVY_ACTUAL_FUEL_USAGE_WEIGHT_ON_OIL_REQUEST:
  def: '0.5'
  type: float
  cmt: weight of actual fuel usage of ships compared to what is being asked for missions
    while calculating oil needed for trade
MONTHS_TO_FILL_FUEL_BUFFER_WITH_OIL_REQUESTS:
  def: '6.0'
  type: float
  cmt: in war time, coutries will try to fill their buffer in this duration and trade
    for oil if necesarry
FUEL_CONSUMPTION_MULT_FOR_FUEL_SAVING_MODE:
  def: '0.25'
  type: float
  cmt: fuel consumptions will be limited by this ratio in fuel saving mode
FUEL_CONSUMPTION_MULT_AGRESSIVE_FUEL_MODE:
  def: '3.0'
  type: float
  cmt: fuel consumptions will be limited by this ratio in aggressive fuel usage mode
DAYS_FUEL_REMAINING_TO_ENTER_FUEL_SAVING_MODE_FUEL_RATIO:
  def: '0.4'
  type: float
WANTED_MAX_FUEL_BUFFER_IN_DAYS_FOR_ARMY_MAX_CONSUMPTION:
  def: '60'
  type: int
  cmt: AI will try to buffer at least this amount of days on max consumption, will
    trade if necesarry and will go into fuel saving mode/aggresive mode using this
    buffer
WANTED_MAX_FUEL_BUFFER_IN_DAYS_FOR_NAVY_MAX_CONSUMPTION:
  def: '60'
  type: int
  cmt: AI will try to buffer at least this amount of days on max consumption, will
    trade if necesarry and will go into fuel saving mode/aggresive mode using this
    buffer
GIE_LEND_LEASE_TO_PLAYER_EXILE_DESIRE_BONUS:
  def: '40'
  type: int
  cmt: AI host is more likely to accept lend lease requests from a player.
NAVAL_BASE_RATIO_ALLOCATED_FOR_REPAIRS_IN_WAR_TIME:
  def: '0.6'
  type: float
  cmt: ai will allocate at most this ratio of dockyards for repairs in war time
MAX_FUEL_CONSUMPTION_RATIO_FOR_NAVY_TRAINING:
  def: '0.20'
  type: float
  cmt: ai will use at most this ratio of affordable fuel for naval training
NUM_SILOS_PER_CIVILIAN_FACTORIES:
  def: '0.0025'
  type: float
  cmt: ai will try to build a silo per this ratio of civ factories
NUM_SILOS_PER_DOCKYARDS:
  def: '0.02'
  type: float
  cmt: ai will try to build a silo per this ratio of dockyards
SHIP_STR_RATIO_EXIT_REPAIRS:
  def: '1.00'
  type: float
  cmt: the ships will leave repairs if they are >= this ratio of total str
PLAN_VALUE_BONUS_FOR_MOVING_UNITS:
  def: '0.35'
  type: float
  cmt: AI plans gets a bonus when units are not moving and ready to fight
AGGRESSIVENESS_CHECK_BASE:
  def: '1.5'
  type: float
  cmt: front comparison where ai will consider aggressive stance, unless it is already
    then the number above is used
AGGRESSIVENESS_CHECK_CAREFUL:
  def: '0.6'
  type: float
  cmt: at what front strength balance do we go careful
AGGRESSIVENESS_CHECK_PARTLY_FORTIFIED_WEAK_POINTS:
  def: '0.75'
  type: float
  cmt: if front strength balance is at or above this value versus a party fortified
    enemy, we rush attack weak points; below this value, we are careful
AGGRESSIVENESS_CHECK_FULLY_FORTIFIED_POCKET:
  def: '6'
  type: int
  cmt: if front strength balance is at or above this value versus a fully fortified
    enemy in a pocket, we do a balanced attack instead being careful
FRONT_EVAL_UNIT_AIR_SUP_IMPACT:
  def: '1.0'
  type: float
  cmt: scale how good the AI thinks air superiority is for units
FRONT_EVAL_PERCENT_TO_ASSIST_ALLY_FRONT:
  def: '0.5'
  type: float
  cmt: percentage of how many units the AI thinks it should have compared to an ally
    before considering sending units
PRODUCTION_CARRIER_PLANE_PRODUCTION_BOOST_TO_BUFFER:
  def: '4.0'
  type: float
  cmt: production of carrier planes will go up by this ratio if we lack buffers
EXTRA_NAVY_INTEL_FOR_CONVOY_RAIDING:
  def: '0.0'
  type: float
  cmt: this amount of intel is added to navy intel while ai is assigning convoy raiding
    mission
NAVAL_CONVOY_COUNT_INTEL_DROPOFF_DUE_TO_LOW_DECYPTION:
  def: '200'
  type: int
  cmt: on lowest navy intel, ai won't be able to see enemy convoys lower than this
    ratio
AIR_AI_ENEMY_PROV_RATIO_FOR_COMBAT_REGION:
  def: '0.15'
  type: float
  cmt: if a region has more than this ratio of provinces controlled by enemy, AI will
    consider it as a combat zone while assigning planes
CONVOY_ESCORT_SCORE_FROM_CONVOYS:
  def: '15'
  type: int
  cmt: score for each convoy you have in area
CONVOY_RAID_MIN_ENEMY_THREAT:
  def: '0.05'
  type: float
RAILWAY_GUN_PRODUCTION_MIN_DIVISONS:
  def: '20'
  type: int
  cmt: Minimum required number of divisions for the AI to consider producing railway
    guns
RAILWAY_GUN_PER_ARMY_CAP:
  def: '5'
  type: int
  cmt: Maximum railway guns assigned to one army for the AI
RAILWAY_GUN_ASSIGNMENT_SCORE_HOLD:
  def: '20'
  type: int
  cmt: Score for keeping current assignment when assigning railway guns
MIN_UNIT_RATIO_FOR_INVASIONS:
  def: '0.1'
  type: float
  cmt: don't allocate more divisions than this for naval invasions
MIN_FRONT_SCORE_FOR_AFTER_INVASION_AREAS:
  def: '1500'
  type: int
  cmt: min score for army fronts that are created on recently invaded regions
MIN_CONVOY_EFFICIENCY_TO_START_TRADES:
  def: '0.6'
  type: float
  cmt: min efficiency (due to convoy raid) to start be able to trades
NAVAL_INVADED_AREA_PRIO_DURATION:
  def: '90'
  type: int
  cmt: after successful invasion, AI will prio the enemy area for this number of days
MIN_NUM_CONQUERED_PROVINCES_TO_DEPRIO_NAVAL_INVADED_FRONTS:
  def: '20'
  type: int
  cmt: if you conquer this amount of provinces after a naval invasion, it will lose
    its prio status and will act as a regular front
FAILED_INVASION_AREA_PRIO_FACTOR:
  def: '0.5'
  type: float
  cmt: for every failed invasion on an area, factor that area's invasion prio with
    this value
BUILDING_TARGETS_BUILDING_PRIORITIES:
  def: '{ "industrial_complex" }'
  type: array
  cmt: 'buildings in order of pirority when considering building targets strategies.
    First has the greatest priority, omitted has the lowest. NOTE: not all buildings
    are supported by building targets strategies.'
MIN_INVASION_ORG_FACTOR_TO_EXECUTE:
  def: '0.75'
  type: float
  cmt: ai will only activate invasions if average org factor is above this
MAX_PORT_STRIKE_HISTORY_TO_REMEMBER:
  def: '5000'
  type: int
  cmt: maximum port strike history to keep track (will be used to disable ports
PORT_STRIKE_HISTORY_DECAY_MAX:
  def: '400'
  type: int
  cmt: maximum decay for port strike history (>=37 days since last port strike)
PORT_STRIKE_HISTORY_VALUE_TO_DISABLE_REPAIRS:
  def: '200'
  type: int
  cmt: cut off for disabling ports above this threshold
CURRENT_LAW_SCORE_BONUS:
  def: '50.0'
  type: float
  cmt: current score will get an additional bonus to its ai weight
OIL_WANT_PER_POTENTIAL_NAVY_CONSUMPTION_K:
  def: '0.03'
  type: float
OIL_WANT_PER_POTENTIAL_MISC_CONSUMPTION_K:
  def: '0.1'
  type: float
OIL_WANT_AT_PEACE_PER_POTENTIAL_NAVY_CONSUMPTION_K:
  def: '0.0'
  type: float
OIL_WANT_AT_PEACE_PER_POTENTIAL_MISC_CONSUMPTION_K:
  def: '0.1'
  type: float
RESOURCE_WANT_PER_CONSUMED:
  def: '0.05'
  type: float
  cmt: if resource is being used in production, increase the desire
CRYPTO_ACTIVATE_NUM_DAYS_DROP_OFF:
  def: '0.4'
  type: float
  cmt: longer decrypted crypto waits, lower threshold it will have. threshold will
    be multiplied by this value at most
CRYPTO_ACTIVATE_NUM_ACTIVATED_DROP_OFF:
  def: '0.6'
  type: float
  cmt: having an already activated cryptos will further multiply threshold, down to
    this value
CRYPTO_ACTIVATION_SCORE_OUR_CAPITAL_BONUS:
  def: '0.2'
  type: float
  cmt: fronts of our capital get a bonus by this ratio
CRYPTO_AFTER_SCORE_INVASION_FRONT_BONUS:
  def: '1.0'
  type: float
  cmt: a front that is naval invading will increase the score by this ratio
EQUIPMENT_UPGRADE_VARIANT_MATCH_SCORE_FACTOR:
  def: '0.2'
  type: float
  cmt: the weight of equipment upgrade level when computing the match score of a variant
    to an ai equipment design.
UPDATE_SUPPLY_BOTTLENECKS_FREQUENCY_HOURS:
  def: '168'
  type: int
  cmt: Check for and try to fix supply bottlenecks this often. (168 hours = 1 week)
UPDATE_SUPPLY_MOTORIZATION_FREQUENCY_HOURS:
  def: '52'
  type: int
  cmt: Check if activating motorization would improve supply situation this often.
ARMY_LEADER_ASSIGN_FIELD_MARSHAL_TO_ARMY:
  def: '-500'
  type: int
  cmt: ' assigning leaders to armies Score for assigning a field marshal to a normal
    army (want to use them for army groups)'
ARMY_LEADER_ASSIGN_EMPTYNESS_MALUS:
  def: '0.2'
  type: float
  cmt: Factor for avoiding assigning leaders that can lead large armies to small armies
    (a value of 0.2 reduces the score by max 20 %)
ARMY_LEADER_ASSIGN_OVERALL_SKILL_FACTOR:
  def: '50'
  type: int
  cmt: This times general's overall skill is added to score
ARMY_LEADER_ASSIGN_DEFENSE_ATTACK_SKILL_FACTOR:
  def: '3'
  type: int
  cmt: If defensive army, this times general's attack skill is added to score
ARMY_LEADER_ASSIGN_DEFENSE_LOGISTICS_SKILL_FACTOR:
  def: '3'
  type: int
  cmt: If defensive army, this times general's logistics skill is added to score
ARMY_LEADER_ASSIGN_INVASION_ATTACK_SKILL_FACTOR:
  def: '10'
  type: int
  cmt: If invasion army, this times general's attack skill is added to score
ARMY_LEADER_ASSIGN_INVASION_LOGISTICS_SKILL_FACTOR:
  def: '20'
  type: int
  cmt: If invasion army, this times general's logistics skill is added to score
ARMY_LEADER_ASSIGN_ATTACK_SKILL_FACTOR:
  def: '20'
  type: int
  cmt: This times general's attack skill is added to score
ARMY_LEADER_ASSIGN_LOGISTICS_SKILL_FACTOR:
  def: '7'
  type: int
  cmt: This times general's logistics skill is added to score
ARMY_LEADER_ASSIGN_NR_TRAITS:
  def: '5'
  type: int
  cmt: This times general's nr of active traits is added to score
ARMY_LEADER_ASSIGN_EXILED_LEADS_OWN_EXILED_TROOPS:
  def: '100'
  type: int
  cmt: If exiled leader, increase chance of leading army with exiled troops from same
    country as the leader
ARMY_LEADER_ASSIGN_DEFENSE_ARMY_ARMOR_DEFENCE_FACTOR:
  def: '1.0'
  type: float
  cmt: If defensive army, importance of general's ARMY_ARMOR_DEFENCE_FACTOR modifier
    (proportional to armor ratio in the army)
ARMY_LEADER_ASSIGN_MAX_PLANNING:
  def: '0.1'
  type: float
  cmt: Importance of general's MAX_PLANNING modifier
ARMY_LEADER_ASSIGN_OUT_OF_SUPPLY_FACTOR:
  def: '1.0'
  type: float
  cmt: Importance of general's OUT_OF_SUPPLY_FACTOR modifier
ARMY_LEADER_ASSIGN_ARMY_ARMOR_SPEED_FACTOR:
  def: '20.0'
  type: float
  cmt: Importance of general's ARMY_ARMOR_SPEED_FACTOR modifier (proportional to armor
    ratio in the army)
ARMY_LEADER_ASSIGN_BOOST_ARMOR_SKILL:
  def: '20.0'
  type: float
  cmt: Importance of general's trait where armor skill is boosted, e.g. armor_officer
    which boosts panzer_leader (proportional to armor ratio in the army)
ARMY_LEADER_ASSIGN_AMPHIBIOUS_INVASION:
  def: '1.0'
  type: float
  cmt: If involved in invasion, importance of general's AMPHIBIOUS_INVASION modifier
ARMY_LEADER_ASSIGN_XP_GAIN_FACTOR:
  def: '2.0'
  type: float
  cmt: Importance of general's XP_GAIN_FACTOR modifier
ARMY_LEADER_ASSIGN_LAND_REINFORCE_RATE:
  def: '1.0'
  type: float
  cmt: Importance of general's LAND_REINFORCE_RATE modifier
ARMY_LEADER_ASSIGN_TERRAIN_FACTOR:
  def: '0.2'
  type: float
  cmt: Importance of general's terrain skills
AREA_DEFENSE_SETTING_PORTS:
  def: 'true'
  type: bool
AREA_DEFENSE_SETTING_FORTS:
  def: 'false'
  type: bool
AREA_DEFENSE_SETTING_RAILWAYS:
  def: 'false'
  type: bool
AREA_DEFENSE_MINCAP_DESIRED_CAPITAL_DEFENSE:
  def: '5'
  type: int
  cmt: DesiredUnits for capital defense is at least this.
AREA_DEFENSE_MINCAP_DESIRED_HOME_AREA:
  def: '3'
  type: int
  cmt: DesiredUnits for home area is at least this.
PEACE_BID_FOLD_TURNS_AGAINST_OTHER_AI:
  def: '2'
  type: int
  cmt: Resolve contests against other AIs after this many turns. Don't always contest
    forever, it yields the same results.
PEACE_BID_CONTEST_TIE_BREAKER_INFLUENCE_DISTANCE:
  def: '1.0'
  type: float
  cmt: When resolving contest against other AI, a tie breaker score is calculated
    and the loser folds. This is how much to weigh relative influence distance between
    the countries.
PEACE_BID_FOLD_AGAINST_PLAYER_CHANCE:
  def: '0.5'
  type: float
  cmt: Likelihood that AI will fold in a bidding contest against human player.
PEACE_AI_GROUP_PEACE_ACTIONS:
  def: 'true'
  type: bool
  cmt: Whether AI should group peace actions or greedily just select the most-desired
    peace actions
PEACE_AI_EVALUATE_FOR_ALLIES:
  def: 'true'
  type: bool
  cmt: Whether AI should include allies when evaluating giving states to other winners
    (may affect performance on new conference turn)
PEACE_AI_EVALUATE_OTHER_IF_CORE:
  def: 'true'
  type: bool
  cmt: Whether AI should evaluate giving states to other winners if state is their
    core (may affect performance on new conference turn)
PEACE_AI_EVALUATE_OTHER_ALWAYS:
  def: 'false'
  type: bool
  cmt: Whether AI should always evaluate giving states to other winners (!!! may heavily
    affect performance on new conference turn for large peace conferences !!!)
INDUSTRIAL_ORG_TRAIT_UNLOCK_RANDOMNESS:
  def: '3'
  type: int
  cmt: AI will pick a random from N top traits when choosing a trait to unlock
INDUSTRIAL_ORG_RESEARCH_ASSIGN_RANDOMNESS:
  def: '3'
  type: int
  cmt: AI will pick a random from N top MIOs when choosing an MIO to assign to a research
INDUSTRIAL_ORG_POLICY_CHANGE_SCALE:
  def: '1.0'
  type: float
  cmt: Policy change weight will be scaled by this value
INDUSTRIAL_ORG_RESEARCH_BONUS_FACTOR:
  def: '1.0'
  type: float
  cmt: Research bonus will be multiplied by this factor when evaluating design teams
AI_WANTED_CARRIER_BASED_PLANES_FACTOR:
  def: '1.0'
  type: float
  cmt: Factor applied to desire for carrier based planes (total carrier space * define)
```
