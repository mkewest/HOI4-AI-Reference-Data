---
domain: defines_list
concept: NAI
version: 1.17.2
requires: [defines]
relates: [ai_strategy, ai_modifiers]
---

```yaml
PEACE_TIME_NAVY_FUEL_FACTOR:
  def: '0.2'
  type: float
  cmt: Percentage of fuel available to navy that is allowed to use for missiosn during
    peace time
PEACE_TIME_NAVY_FUEL_LIMIT:
  def: '0.5'
  type: float
  cmt: The maximum fuel percentage to use for navy at peace from available fuel scaled
    with world tension
GARRISON_FRACTION:
  def: '0.0'
  type: float
  cmt: How large part of a front should always be holding the line rather than advancing
    at the enemy
THEORIST_SCALING_WEIGHT_FACTOR_PER_NON_POLITICAL_ADVISORS:
  def: '0.15'
  type: float
  cmt: Scale theorist weight by this * num non political advisors
DIPLOMATIC_ACTION_GOOD_BAD_RATIO_THRESHOLD:
  def: '1'
  type: int
BASE_RELUCTANCE:
  def: '20'
  type: int
  cmt: Base reluctance applied to all diplomatic offers
DIPLOMATIC_ACTION_RANDOM_FACTOR:
  def: '0.5'
  type: float
  cmt: How much of the AI diplomatic action scoring is randomly determined (1.0 = half
    random, 2.0 = 2/3rd random, etc)
DIPLOMATIC_ACTION_PROPOSE_SCORE:
  def: '50'
  type: int
  cmt: AI must score a diplomatic action at least this highly to propose it themselves
DILPOMATIC_ACTION_DECLARE_WAR_WARGOAL_BASE:
  def: '50'
  type: int
  cmt: Base diplomatic action score bonus to go to war per wargoal
DIPLOMATIC_ACTION_BREAK_SCORE:
  def: '-10'
  type: int
  cmt: AI must score a diplomatic action less than this to break it off
DIPLOMATIC_ACTION_NAVAL_BLOCKADE_BASE_SCORE:
  def: '-700'
  type: int
  cmt: The conditions need to make the base score beat DIPLOMATIC_ACTION_PROPOSE_SCORE
    before a blockade is considered
DIPLOMATIC_ACTION_NAVAL_BLOCKADE_DECREMENT_SCORE_PER_EXISTING_BLOCKADE:
  def: '100'
  type: int
  cmt: AI will decrease the desire by this amount following each existing blockade
DIPLOMATIC_ACTION_NAVAL_BLOCKADE_OPINION_SCALING:
  def: '-2'
  type: int
  cmt: AI will increase the desire by this amount times the opinion of the target, note
    that this must be a negative value to increase desire
DIPLOMATIC_ACTION_NAVAL_BLOCKADE_TENSION_FACTOR:
  def: '8'
  type: int
  cmt: Generated Threat x TENSION_FACTOR
DIPLOMATIC_ACTION_NAVAL_BLOCKADE_DECREMENT_SAME_IDEOLOGY:
  def: '2000'
  type: int
  cmt: AI will decrease the desire by this amount if the target is of the same ideology
DIPLOMATIC_ACTION_NAVAL_BLOCKADE_FLEET_SIZE_THRESHOLD:
  def: '100'
  type: int
  cmt: AI will increase/decrease the naval blockade desire if the fleet size difference
    above/below this threshold
DIPLOMATIC_ACTION_NAVAL_BLOCKADE_FLEET_SIZE_SCALING:
  def: '4'
  type: int
  cmt: AI will increase/decrease the naval blockade desire by this times if the fleet
    size difference above/below the threshold
DIPLOMACY_CREATE_FACTION_FACTOR:
  def: '0.75'
  type: float
  cmt: Factor for AI desire to create a new faction. Val < 1.0 makes it less likely to
    create than to join.
DIPLOMACY_FACTION_WRONG_IDEOLOGY_PENALTY:
  def: '60'
  type: int
  cmt: AI penalty for diplomatic faction acitons between nations of different ideologies
DIPLOMACY_FACTION_SAME_IDEOLOGY_MAJOR:
  def: '10'
  type: int
  cmt: AI bonus acceptance when being asked about faction is a major of the same
    ideology
DIPLOMACY_FACTION_NEUTRALITY_PENALTY:
  def: '50'
  type: int
  cmt: Neutral nations have a separate penalty, not wanting to get involved at all,
    rather than caring much about the difference in ideology
DIPLOMACY_FACTION_GLOBAL_TENSION_FACTOR:
  def: '0.2'
  type: float
  cmt: How much the AI takes global tension into account when considering faction
    actions
DIPLOMACY_FACTION_WAR_RELUCTANCE:
  def: '-50'
  type: int
  cmt: Penalty to desire to enter a faction with a country that we are not fighting wars
    together with.
DIPLOMACY_FACTION_TAKE_OVER_RELUCTANCE_VERSUS_HUMAN:
  def: '2.0'
  type: float
  cmt: Multiplier penalty for how much stronger than a human faction member an AI
    country must be to choose to assume faction leadership.
DIPLOMACY_SCARED_MINOR_EXTRA_RELUCTANCE:
  def: '-50'
  type: int
  cmt: extra reluctance to join stuff as scared minor
DIPLOMACY_FACTION_PLAYER_JOIN:
  def: '20'
  type: int
  cmt: Bonus for human players asking to join a faction.
DIPLOMACY_BOOST_PARTY_COST_FACTOR:
  def: '100.0'
  type: float
  cmt: Desire to boost party popularity subtracts the daily cost multiplied by this
DIPLOMACY_IMPROVE_RELATION_COST_FACTOR:
  def: '5.0'
  type: float
  cmt: Desire to boost relations subtracts the cost multiplied by this
DIPLOMACY_IMPROVE_RELATION_PP_FACTOR:
  def: '0.1'
  type: float
  cmt: Desire to boost relations adds total PP multiplied by this
DIPLOMACY_SEND_ATTACHE_COST_FACTOR:
  def: '5.0'
  type: float
  cmt: Desire to send attache substracts the cost multiplied by this
DIPLOMACY_SEND_ATTACHE_PP_FACTOR:
  def: '0.1'
  type: float
  cmt: Desire to send attache adds total PP multiplied by this
DIPLOMACY_REJECTED_WAIT_MONTHS_BASE:
  def: '4'
  type: int
  cmt: AI will not repeat offers until at least this time has passed, and at most the
    double
DIPLOMACY_LEND_LEASE_MONTHS_TO_CANCEL:
  def: '1'
  type: int
  cmt: AI will not cancel a lend lease offer until this time has passed
DIPLOMACY_CALL_ALLY_VALIDITY_DURATION:
  def: '1'
  type: int
  cmt: Overwrite above value for CallAlly and JoinAlly diplo action. This is however
    fixed, and is not subject to randomness. Also, this is the time the AI will keep the
    action in its incoming queue without declining it.
DIPLOMACY_PURCHASE_EQUIPMENT_MONTHS:
  def: '2'
  type: int
  cmt: AI will not ask to purchase equipment more often than this
DIPLOMACY_SEND_MAX_FACTION:
  def: '0.75'
  type: float
  cmt: Country should not send away more units than this as expeditionaries
DIPLOMACY_ACCEPT_VOLUNTEERS_BASE:
  def: '50'
  type: int
  cmt: Base value of volunteer acceptance (help is welcome)
DIPLOMACY_ACCEPT_ATTACHE_BASE:
  def: '50'
  type: int
  cmt: Base value of attache acceptance (help is welcome)
DIPLOMACY_ACCEPT_ATTACHE_OPINION_TRASHHOLD:
  def: '20'
  type: int
  cmt: Value of opinion that will remove accepting penalty for receiveing the attache
DIPLOMACY_ACCEPT_ATTACHE_OPINION_PENALTY:
  def: '-100'
  type: int
  cmt: Value of acceptance penalty if the opinion too low
DIPLOMACY_FACTION_MAJOR_AT_WAR:
  def: '1000.0'
  type: float
  cmt: Factor that will be multiplied with the surrender level in the desire to offer to
    the other ai to join a faction
DIPLOMACY_FACTION_SURRENDER_LEVEL:
  def: '20'
  type: int
  cmt: How much the recipient nation losing matters for joining a faction
DIPLO_PREFER_OTHER_FACTION:
  def: '-200'
  type: int
  cmt: The country has yet to ask some other faction it would prefer to be a part of.
DIPLO_DISTANCE_BETWEEN_CAPITALS:
  def: '-340'
  type: int
  cmt: Max scaled malus from distance between capitals
DIPLO_ACCEPTABLE_DISTANCE_BETWEEN_CAPITALS:
  def: '1000.0'
  type: float
  cmt: When scaled distance malus begins to kick in. At double this value, max penalty
    (above) is achieved
DIPLO_SHOW_FACTION_JOIN_WARNING_THRESHOLD:
  def: '-20'
  type: int
  cmt: Show warning if declare-war target is this close to accepting or being sent a
    faction invitiation
DIPLO_MAX_CONTAINMENT_ACCEPTANCE:
  def: '100'
  type: int
  cmt: Max value for 'wants to contain' diplo acceptance
AI_GUARANTEE_DESIRE_WITH_PRESSURE_MODIFIER:
  def: '15'
  type: int
  cmt: If we have an 'ideology drfit from guarantees' modifier, how much more likely
    will we be to guarantee nations?
RESEARCH_DAYS_BETWEEN_WEIGHT_UPDATE:
  def: '7'
  type: int
  cmt: Refreshes need scores based on country situation.
RESEARCH_WEIGHT_TRUNCATION_THRESHOLD:
  def: '0.75'
  type: float
  cmt: When choosing a tech to research, use this truncation selection threshold. (for
    example, if the top score is 10, a threshold of 0.75 will pick randomly from
    anything above 7.5 score)
RESEARCH_LAND_DOCTRINE_NEED_GAIN_FACTOR:
  def: '0.15'
  type: float
  cmt: Multiplies value based on relative military industry size / country size.
RESEARCH_NAVAL_DOCTRINE_NEED_GAIN_FACTOR:
  def: '0.05'
  type: float
  cmt: Multiplies value based on relative naval industry size / country size.
RESEARCH_AIR_DOCTRINE_NEED_GAIN_FACTOR:
  def: '0.07'
  type: float
  cmt: Multiplies value based on relative number of air base / country size.
RESEARCH_NEW_DOCTRINE_RANDOM_FACTOR:
  def: '0.05'
  type: float
  cmt: How much randomness is allowed to contribute to do new research expressed as a
    factor of total tech weights. Higher means more random exploration.
RESEARCH_AHEAD_BONUS_FACTOR:
  def: '4.0'
  type: float
  cmt: To which extent AI should care about ahead of time bonuses to research
RESEARCH_BONUS_FACTOR:
  def: '5.0'
  type: float
  cmt: To which extent AI should care about research speed bonuses
RESEARCH_YEARS_BEHIND_FACTOR:
  def: '0.2'
  type: float
  cmt: To which extent AI should care about not falling behind (i.e. increase weight for
    old tech)
RESEARCH_NEEDS_FACTOR:
  def: '0.01'
  type: float
  cmt: To which extent AI should care about its research needs (research needs are
    matched against the tech category)
RESEARCH_LENGTH_FACTOR:
  def: '3'
  type: int
  cmt: To which extent AI should care about how long it takes to research something (it
    prefers short research times)
MAX_AHEAD_RESEARCH_PENALTY:
  def: '3'
  type: int
  cmt: Max ahead of time penalty AI will ever consider (this also includes
    BASE_YEAR_AHEAD_PENALTY_FACTOR, so not the raw time)
RESEARCH_AHEAD_OF_TIME_FACTOR:
  def: '4.0'
  type: float
  cmt: To which extent AI should care about ahead of time penalties to research
RESEARCH_BASE_DAYS:
  def: '60'
  type: int
  cmt: AI adds a base number of days when weighting completion time for techs to ensure
    it doesn't only research quick techs
DECLARE_WAR_RELATIVE_FORCE_FACTOR:
  def: '0.5'
  type: float
  cmt: Weight of relative force between nations that consider going to war
TRADEABLE_FACTORIES_FRACTION:
  def: '0.8'
  type: float
  cmt: Will at most trade away this fraction of factories.
MIN_DELIVERED_TRADE_FRACTION:
  def: '0.8'
  type: float
  cmt: AI will cancel trade deals that are not able to deliver more than this fraction
    of the agreed amount
SEA_PATH_LENGTH_SCORE_BASE:
  def: '-30'
  type: int
  cmt: scoring reduction from naval paths for AI when picking trade partners
MINIMUM_GOOD_TRADE_RATIO_PER_CIV:
  def: '0.005'
  type: float
  cmt: for each civ factory we have mul with this we are allowed to trade under % of
    resource on a trade
NAVAL_DOCKYARDS_SHIP_FACTOR:
  def: '1.5'
  type: float
  cmt: The extent to which number of dockyards play into amount of sips a nation wants
PRODUCTION_EQUIPMENT_SURPLUS_FACTOR:
  def: '0.8'
  type: float
  cmt: Base value for how much of currently used equipment the AI will at least strive
    to have in stock
PRODUCTION_EQUIPMENT_SURPLUS_FACTOR_GARRISON:
  def: '0.3'
  type: float
  cmt: Base value for how much of currently used equipment the AI will at least strive
    to have in stock for garrison forces
AIR_SUPERIORITY_FACTOR:
  def: '2.5'
  type: float
  cmt: Factor for air superiority score
ROCKET_MIN_ASSIGN_SCORE:
  def: '10'
  type: int
  cmt: Minimum total score for region to be considered for rocket air missions
ROCKET_MIN_PRIO_ASSIGN_SCORE:
  def: '50'
  type: int
  cmt: Minimum total score for region to be considered for critical rocket air missions
ROCKET_PRIORITIZE_BARRAGE:
  def: 'false'
  type: bool
  cmt: Prioritize rocket barrage or strategic bombing mission. false = prioritize
    strategic bombing, true = prioritize barrage
ROCKET_ASSIGN_SCORE_REDUCTION_PER_ASSIGNMENT:
  def: '0.5'
  type: float
  cmt: each assigned rocket reduces the score of a region by this amount
GUN_EMPLACEMENT_MIN_ASSIGN_SCORE:
  def: '1'
  type: int
  cmt: Minimum total score for region to be considered for gun emplacement air missions
GUN_EMPLACEMENT_MIN_PRIO_ASSIGN_SCORE:
  def: '50'
  type: int
  cmt: Minimum total score for region to be considered for critical gun emplacement air
    missions
GUN_EMPLACEMENT_ASSIGN_SCORE_REDUCTION_PER_ASSIGNMENT:
  def: '0.5'
  type: float
  cmt: each assigned gun emplacement reduces the score of a region by this amount
MAX_VOLUNTEER_ARMY_FRACTION:
  def: '0.25'
  type: float
  cmt: Countries will not send more than their forces time this number to aid another
    country
DEPLOY_MIN_TRAINING_SURRENDER_FACTOR:
  def: '0.5'
  type: float
  cmt: Required percentage of training (1.0 = 100%) for AI to deploy unit in wartime
    while surrender progress is higher than 0
DEPLOY_MIN_EQUIPMENT_SURRENDER_FACTOR:
  def: '0.90'
  type: float
  cmt: Required percentage of equipment (1.0 = 100%) for AI to deploy unit in wartime
    while surrender progress is higher than 0
DEPLOY_MIN_TRAINING_PEACE_FACTOR:
  def: '0.98'
  type: float
  cmt: Required percentage of training (1.0 = 100%) for AI to deploy unit in peacetime
DEPLOY_MIN_EQUIPMENT_PEACE_FACTOR:
  def: '0.98'
  type: float
  cmt: Required percentage of equipment (1.0 = 100%) for AI to deploy unit in peacetime
DEPLOY_MIN_TRAINING_WAR_FACTOR:
  def: '0.95'
  type: float
  cmt: Required percentage of training (1.0 = 100%) for AI to deploy unit in wartime
DEPLOY_MIN_EQUIPMENT_WAR_FACTOR:
  def: '0.95'
  type: float
  cmt: Required percentage of equipment (1.0 = 100%) for AI to deploy unit in wartime
DEPLOY_MIN_EQUIPMENT_CAP_DEPLOY_FACTOR:
  def: '0.85'
  type: float
  cmt: If training is capped by equipment deficit and we have reached that cap, deploy
    unit anyway if percentage is above this (reinforce in field instead).
DYNAMIC_STRATEGIES_THREAT_FACTOR:
  def: '4.0'
  type: float
  cmt: How much threat generated by other countries effects generated strategies
LOCATION_BALANCE_TO_ADVANCE:
  def: '0.0'
  type: float
  cmt: Limit on location strength balance between country and enemy for unit to dare to
    move forward.
EQUIPMENT_MARKET_UPDATE_FREQUENCY_DAYS:
  def: '11'
  type: int
  cmt: How often the AI runs its market logic
EQUIPMENT_MARKET_MAX_CIVS_FOR_PURCHASES_RATIO:
  def: '0.1'
  type: float
  cmt: Ratio of available civilian factories to max use for equipment purchases (0.2 =
    20 %, so 50 available civs would mean max ca 10 civs to spend on purchases at any
    one time). Gets modified by equipment_market_spend_factories AI strategy.
EQUIPMENT_MARKET_BASE_MARKET_RATIO:
  def: '0.2'
  type: float
  cmt: The AI tries to keep ca this ratio of equipment surplus for sale on the market.
    Gets modified by equipment_market_for_sale_factor AI strategy.
EQUIPMENT_MARKET_DEFAULT_CIC_CHUNK_FOR_SALE:
  def: '150.0'
  type: float
  cmt: When putting things up for sale on the market, this determines the default
    "chunk" size of equipment the AI puts up. Gets overridden by
    equipment_market_min_for_sale AI strategy. (If one equipment is worth 5 CIC, a value
    of 150 would result in chunk sizes of 150/5 = 30 units)
EQUIPMENT_MARKET_NR_DELIVERIES_SOFT_MAX:
  def: '10'
  type: int
  cmt: AI tries to adjust assigned factories and amount of equipment to keep nr
    deliveries at max this
EQUIPMENT_MARKET_EXTRA_CONVOYS_OVERRIDE:
  def: '2'
  type: int
  cmt: Makes the AI able to buy convoys even if they are lacking free convoys. 0 will
    make them stop this behavior, anything > 0 will allow overriding the perceived nr of
    free convoys. Only if convoy equipment has a non-zero weight does the actual value
    matter.
EQUIPMENT_MARKET_WANTED_CONVOY_USAGE_RATIO:
  def: '0.3'
  type: float
  cmt: If the AI's available/free/unused convoys is reduced to this ratio (0.3 = 30 %),
    start buying convoys.
EQUIPMENT_MARKET_CONTRACT_DURATION_ACCEPTANCE:
  def: '-10'
  type: int
  cmt: If expected contract duration is longer than
    EQUIPMENT_MARKET_NR_DELIVERIES_SOFT_MAX deliveries, then add this to the
    PurchaseContract AI acceptance score per nr overdue deliveries
EQUIPMENT_MARKET_CONTRACT_EFFICIENCY_TO_CANCEL:
  def: '0.1'
  type: float
  cmt: If contract efficiency stays below this, the AI will cancel the contract
EQUIPMENT_MARKET_EQUIPMENT_SUNK_TO_CANCEL:
  def: '0.5'
  type: float
  cmt: If more equipment is sunk then the given percentage, the AI will cancel the
    contract
EQUIPMENT_MARKET_SHORTAGE_DAYS_TO_CANCEL:
  def: '30'
  type: int
  cmt: If equipment deficit will take more than these many days to fix, the AI will
    cancel the contract
EQUIPMENT_MARKET_MAX_CONVOY_RATIO_FOR_MARKET_PEACE:
  def: '0.5'
  type: float
  cmt: Max ratio of total convoys to use for equipment trade while at peace
EQUIPMENT_MARKET_MAX_CONVOY_RATIO_FOR_MARKET_WAR:
  def: '0.25'
  type: float
  cmt: Max ratio of total convoys to use for equipment trade while at war
EQUIPMENT_MARKET_SCORE_FACTOR_VARIANT_SCORE:
  def: '5.0'
  type: float
  cmt: Score coefficient for VariantScore (high is good)
EQUIPMENT_MARKET_SCORE_FACTOR_CIC_VALUE_NEEDED:
  def: '8.0'
  type: float
  cmt: Score coefficient for CicValueNeeded (high is prio)
EQUIPMENT_MARKET_SCORE_FACTOR_SUBSIDY_VALUE:
  def: '2.0'
  type: float
  cmt: Score coefficient for SubsidyValue (high is good)
EQUIPMENT_MARKET_SCORE_FACTOR_COST_PER_UNIT:
  def: '-5.0'
  type: float
  cmt: Score coefficient for SubsidizedCostPerUnit (low is good)
EQUIPMENT_MARKET_SCORE_FACTOR_AI_STRAT_WEIGHT:
  def: '50.0'
  type: float
  cmt: Score coefficient for AiStratWeight (high is prio)
EQUIPMENT_MARKET_SCORE_FACTOR_DIPLO_OPINION:
  def: '1.0'
  type: float
  cmt: Score coefficient for DiploOpinion, mainly used as tie breaker (high is good)
INFRASTRUCTURE_PERCENTAGE_AT_WHICH_TO_BUILD_INFRA_CAP_BUILDING:
  def: '0.75'
  type: float
  cmt: When should we build a cap building on a state
NUM_FACTORIES_IN_STATE_TO_WANT_ENERGY_REDUCTION:
  def: '6'
  type: int
  cmt: How many mils should we want in a state before we think about building energy
    reduction cap building
TOTAL_STATE_EXTRACTED_RESOURCES_FOR_BUILDING_RESOURCE_CAP_BUILDING:
  def: '30.0'
  type: float
  cmt: How many resources required for building a resource inproving infra cap building
DIPLOMACY_ACCEPT_CONDITIONAL_SURRENDER_MANPOWER_IN_FIELD:
  def: '-20'
  type: int
  cmt: Scale multiplied by difference in manpower in field
DIPLOMACY_ACCEPT_CONDITIONAL_SURRENDER_GLOBAL_TENSION:
  def: '-10'
  type: int
  cmt: Multiplied by WT
DIPLOMACY_ACCEPT_CONDITIONAL_SURRENDER_WAR_SUPPORT:
  def: '-10'
  type: int
  cmt: Multiplied by recipient WS
DIPLOMACY_ACCEPT_CONDITIONAL_SURRENDER_EMBARGO:
  def: '2'
  type: int
  cmt: Multiplied by num embargo, max 5 embargo
DIPLOMACY_ACCEPT_CONDITIONAL_SURRENDER_OWN_SURRENDER_LIMIT:
  def: '20'
  type: int
  cmt: Multiplied by recipient nation's surrender level
DIPLOMACY_ACCEPT_CONDITIONAL_SURRENDER_MINOR_WAR:
  def: '10'
  type: int
  cmt: Applied if recipient is a minor nation (and therefore there are no majors in this
    war)
MIN_POLITICAL_POWER_MONTHLY_GAIN_FOR_IMPROVE_RELATIONS:
  def: '0.50'
  type: float
  cmt: If country makes less than this PP per month, they won't improve relations
NUM_RESOURCES_TO_ALLOW_MINOR_EMBARGO:
  def: '69'
  type: int
  cmt: If we or any of our puppets have more total resources of a single category that
    this, we will consider embargoing countries
EMBARGO_WORLD_TENSION_THREAT_DIVISOR:
  def: '2.5'
  type: float
  cmt: A divisor to generated world tension when applying how much we care about it in
    AI desire
OPINION_CUTOFF_FOR_IMPROVE_RELATIONS:
  def: '80'
  type: int
  cmt: AI will never consider improving relations if above this opinion with target.
DEFAULT_MODULE_VARIANT_CREATION_XP_CUTOFF_LAND:
  def: '35'
  type: int
  cmt: Army XP needed before attempting to create a variant of a type that uses the tank
    designer (the tank designer DLC feature must be active).
DEFAULT_MODULE_VARIANT_CREATION_XP_CUTOFF_NAVY:
  def: '50'
  type: int
  cmt: Same as above but for the ship designer.
DEFAULT_MODULE_VARIANT_CREATION_XP_CUTOFF_AIR:
  def: '25'
  type: int
  cmt: Same as above but for the plane designer.
DEFAULT_LEGACY_VARIANT_CREATION_XP_CUTOFF_LAND:
  def: '35'
  type: int
  cmt: Army XP needed before attempting to create a variant of a type that uses the
    legacy upgrades system. ai_strategy supports land_xp_spend_priority
    upgrade_xp_cutoff. If none is set, this define is used instead.
DEFAULT_LEGACY_VARIANT_CREATION_XP_CUTOFF_NAVY:
  def: '25'
  type: int
  cmt: Same as above but for navy XP and navy_xp_spend_priority.
DEFAULT_LEGACY_VARIANT_CREATION_XP_CUTOFF_AIR:
  def: '25'
  type: int
  cmt: Same as above but for air XP and air_xp_spend_priority.
VARIANT_CREATION_XP_RESERVE_LAND:
  def: '50'
  type: int
  cmt: If the AI lacks army XP to create a variant it will reserve this much XP for
    variant creation so that it will eventually be able to create a variant.
VARIANT_CREATION_XP_RESERVE_NAVY:
  def: '50'
  type: int
  cmt: Same as above but for navy XP.
VARIANT_CREATION_XP_RESERVE_AIR:
  def: '50'
  type: int
  cmt: Same as above but for air XP.
LAND_DESIGN_ALTERNATIVE_ABSENT:
  def: '30000'
  type: int
LAND_DESIGN_ALTERNATIVE_OF_LESSER_TECH:
  def: '10000'
  type: int
LAND_DESIGN_ALTERNATIVE_OF_EQUAL_TECH:
  def: '100'
  type: int
LAND_DESIGN_ALTERNATIVE_OF_GREATER_TECH:
  def: '1'
  type: int
LAND_DESIGN_DEMAND_FIELD_DIVISION:
  def: '20'
  type: int
LAND_DESIGN_DEMAND_TRAINING_DIVISION:
  def: '15'
  type: int
LAND_DESIGN_DEMAND_GARRISON_DIVISION:
  def: '10'
  type: int
LAND_DESIGN_DEMAND_UNUSED_TEMPLATE:
  def: '1'
  type: int
LAND_DESIGN_DEMAND_ABSENT:
  def: '1'
  type: int
LAND_DESIGN_CUTOFF_AS_PERCENTAGE_OF_MAX:
  def: '0.25'
  type: float
AIR_DESIGN_ALTERNATIVE_ABSENT:
  def: '1000000'
  type: int
AIR_DESIGN_ALTERNATIVE_OF_LESSER_TECH:
  def: '10000'
  type: int
AIR_DESIGN_ALTERNATIVE_OF_EQUAL_TECH:
  def: '100'
  type: int
AIR_DESIGN_ALTERNATIVE_OF_GREATER_TECH:
  def: '1'
  type: int
AIR_DESIGN_DEMAND_MAX:
  def: '33'
  type: int
AIR_DESIGN_DEMAND_MIN:
  def: '1'
  type: int
AIR_DESIGN_DEMAND_ABSENT:
  def: '0'
  type: int
AIR_DESIGN_CUTOFF_AS_PERCENTAGE_OF_MAX:
  def: '0.34'
  type: float
DESIRE_USE_XP_TO_UNLOCK_LAND_DOCTRINE:
  def: '0.5'
  type: float
  cmt: How quickly is desire to unlock land doctrines accumulated?
DESIRE_USE_XP_TO_UNLOCK_NAVAL_DOCTRINE:
  def: '0.5'
  type: float
  cmt: How quickly is desire to unlock naval doctrines accumulated?
DESIRE_USE_XP_TO_UNLOCK_AIR_DOCTRINE:
  def: '0.5'
  type: float
  cmt: How quickly is desire to unlock air doctrines accumulated?
DESIRE_USE_XP_TO_UPDATE_LAND_TEMPLATE:
  def: '2.0'
  type: float
  cmt: How quickly is desire to update/create templates accumulated?
DESIRE_USE_XP_TO_UPGRADE_LAND_EQUIPMENT:
  def: '1.0'
  type: float
  cmt: How quickly is desire to update/create land equipment variants accumulated?
DESIRE_USE_XP_TO_UPGRADE_NAVAL_EQUIPMENT:
  def: '1.0'
  type: float
  cmt: How quickly is desire to update/create naval equipment variants accumulated?
DESIRE_USE_XP_TO_UPGRADE_AIR_EQUIPMENT:
  def: '1.0'
  type: float
  cmt: How quickly is desire to update/create air equipment variants accumulated?
DESIRE_USE_XP_TO_UNLOCK_ARMY_SPIRIT:
  def: '0.35'
  type: float
  cmt: How quickly is desire to unlock army spirits accumulated?
DESIRE_USE_XP_TO_UNLOCK_NAVY_SPIRIT:
  def: '0.35'
  type: float
  cmt: How quickly is desire to unlock naval spirits accumulated?
DESIRE_USE_XP_TO_UNLOCK_AIR_SPIRIT:
  def: '0.35'
  type: float
  cmt: How quickly is desire to unlock air spirits accumulated?
DAYS_BETWEEN_CHECK_BEST_DOCTRINE:
  def: '7;'
  type: string
  cmt: Recalculate desired best doctrine to unlock with this many days inbetween.
DAYS_BETWEEN_CHECK_BEST_TEMPLATE:
  def: '7;'
  type: string
  cmt: Recalculate desired best template to upgrade with this many days inbetween.
DAYS_BETWEEN_CHECK_BEST_EQUIPMENT:
  def: '7;'
  type: string
  cmt: Recalculate desired best equipment to upgrade with this many days inbetween.
UNLOCK_SPIRIT_AI_WILL_DO_FACTOR:
  def: '20'
  type: int
  cmt: Factor for scripted ai_will_do value
UNLOCK_SPIRIT_MODIFIER_FACTOR:
  def: '0.05'
  type: float
  cmt: Factor for AI's evaluated value of the modifiers connected to the spirit
UNLOCK_SPIRIT_USE_TRUNCATION_SELECT:
  def: 'false'
  type: bool
  cmt: Whether to use truncation select or roulette-wheel select. Set threshold for
    truncation select below.
UNLOCK_SPIRIT_TRUNCATION_SELECT_THRESHOLD:
  def: '0.80'
  type: float
  cmt: Valid between [0.0, 1.0]. When unlocking spirits, select randomly from all
    spirits with AI score >= VALUE * HighestSpiritScore. To always select the best, set
    this value to 1.0. To select fully randomly, set this value to 0.0.
FOCUS_TREE_CONTINUE_FACTOR:
  def: '1.5'
  type: float
  cmt: Factor for score of how likely the AI is to keep going down a focus tree rather
    than starting a new path.
PLAN_VALUE_TO_EXECUTE:
  def: '-0.5'
  type: float
  cmt: AI will typically avoid carrying out a plan it below this value (0.0 is
    considered balanced).
DECLARE_WAR_NOT_NEIGHBOR_FACTOR:
  def: '0.25'
  type: float
  cmt: Multiplier applied before force factor if country is not neighbor with the one it
    is considering going to war
CALL_ALLY_BASE_DESIRE:
  def: '20'
  type: int
  cmt: exactly what it says
CALL_ALLY_DEMOCRATIC_DESIRE:
  def: '50'
  type: int
  cmt: Desire to call ally added for democratic AI
CALL_ALLY_NEUTRAL_DESIRE:
  def: '25'
  type: int
  cmt: Desire to call ally added for neutral AI
CALL_ALLY_FASCIST_DESIRE:
  def: '-10'
  type: int
  cmt: Desire to call ally added for fascist AI
CALL_ALLY_COMMUNIST_DESIRE:
  def: '75'
  type: int
  cmt: Desire to call ally added for communist AI
CALL_ALLY_PUPPET_INVITE_OVERLORD:
  def: '1000'
  type: int
  cmt: Desire for a puppet to call its overlord into the war
CALL_ALLY_OVERLORD_INVITE_PUPPET:
  def: '20'
  type: int
  cmt: Desire for an overlord to call its puppet into the war
CALL_ALLY_RELATIVE_INDUSTRY_STRENGTH_THRESHOLD:
  def: '1.5'
  type: float
  cmt: If our relative industry strength ratio is less than this (compared to all
    enemies), increase desire to call allies
CALL_ALLY_RELATIVE_ARMY_STRENGTH_THRESHOLD:
  def: '1.5'
  type: float
  cmt: If our relative army strength ratio is less than this (compared to all enemies),
    increase desire to call allies
CALL_ALLY_RELATIVE_INDUSTRY_STRENGTH_MAX:
  def: '50.0'
  type: float
  cmt: Max desire value for relative industry strength (lerping between zero and this
    based on the threshold)
CALL_ALLY_RELATIVE_ARMY_STRENGTH_MAX:
  def: '100.0'
  type: float
  cmt: Max desire value for relative army strength (lerping between zero and this based
    on the threshold)
CALL_ALLY_LOSING_WAR_THRESHOLD:
  def: '0.45'
  type: float
  cmt: If our war progress is less than this, increase desire to call allies (0.5 is
    stalemate)
CALL_ALLY_LOSING_WAR_MAX:
  def: '100.0'
  type: float
  cmt: Max desire value for losing war (lerping between zero and this based on the
    threshold)
CALL_ALLY_WAR_LENGTH_NR_MONTHS:
  def: '2'
  type: int
  cmt: For every month the war has gone on, increase desire this much
CALL_ALLY_JOINER_HAS_ENEMY_NEIGHBOR:
  def: '100'
  type: int
  cmt: If the joining country is neighbor to at least one of the enemies, increase
    desire this much
AI_CHAIN_CALLS_ALLIES:
  def: 'true'
  type: bool
  cmt: with this enabled the AI will automatically call AI allies when called into a war
    (which in turn generates a single popup, this circumvents some potential modfiable
    scripts with the call ally diplo action, which might be a cause to disable it in
    some mods
MIN_AI_UNITS_PER_TILE_FOR_STANDARD_COHESION:
  def: '1.5'
  type: float
  cmt: How many units should we have for each tile along a front in order to switch to
    standard cohesion (less moving around)
MIN_FRONT_SIZE_TO_CONSIDER_STANDARD_COHESION:
  def: '12'
  type: int
  cmt: How long should fronts be before we consider switching to standard cohesion
    (under this, standard cohesion fronts will switch back to relaxed)
JOIN_ALLY_BASE_DESIRE:
  def: '20'
  type: int
  cmt: exactly what it says
JOIN_ALLY_DEMOCRATIC_DESIRE:
  def: '50'
  type: int
  cmt: Desire to join ally added for democratic AI
JOIN_ALLY_NEUTRAL_DESIRE:
  def: '25'
  type: int
  cmt: Desire to join ally added for neutral AI
JOIN_ALLY_FASCIST_DESIRE:
  def: '-10'
  type: int
  cmt: Desire to join ally added for fascist AI
JOIN_ALLY_COMMUNIST_DESIRE:
  def: '75'
  type: int
  cmt: Desire to join ally added for communist AI
JOIN_FACTION_BOTH_LOSING:
  def: '-300'
  type: int
  cmt: Desire to be in a faction when both we and htey are in losing wars
LENDLEASE_FRACTION_OF_PRODUCTION:
  def: '0.5'
  type: float
  cmt: Base fraction AI would send as lendlease
LENDLEASE_FRACTION_OF_STOCKPILE:
  def: '0.25'
  type: float
  cmt: Base fraction AI would send as lendlease
MINIMUM_EQUIPMENT_TO_ASK_LEND_LEASE:
  def: '-100'
  type: int
  cmt: AI will accept to lend lease this equipment only if our stockpile is less than
    that.
MINIMUM_CONVOY_TO_ASK_LEND_LEASE:
  def: '30'
  type: int
  cmt: AI will accept to lend lease convoys only if our stockpile is less than that
    (special case because convoy stockpile can't be negative).
MINIMUM_FUEL_DAYS_TO_ASK_LEND_LEASE:
  def: '2'
  type: int
  cmt: AI will accept to lend lease fuel only if the player have less fuel than this
    number multiply by his max daily consumption.
MINIMUM_FUEL_DAYS_TO_ACCEPT_LEND_LEASE:
  def: '10'
  type: int
  cmt: AI will accept to lend lease fuel only if they have more fuel than this number
    multiply by their max daily consumption. Note that for a GiE asking to its host, we
    divide this number by 2.
DEFAULT_SUPPLY_TRUCK_BUFFER_RATIO:
  def: '1.5'
  type: float
  cmt: ai will set to truck buffer ratio to this. can be modified by
    wanted_supply_trucks min_wanted_supply_trucks ai strats
DEFAULT_SUPPLY_TRAIN_NEED_FACTOR:
  def: '1.2'
  type: float
  cmt: AI multiplies current train usage by this to determine desired nr of wanted
    trains. Can be modified by wanted_supply_train min_wanted_supply_trains ai strats.
POLITICAL_IDEA_MIN_SCORE:
  def: '0.1'
  type: float
  cmt: Only replace or add an idea if score is above this score.
HIGH_COMMAND_ADDED_WEIGHT_FACTOR:
  def: '1.10'
  type: float
  cmt: Weight multiplier for high_command advisors over other chosen advisor or idea
    types
CHIEF_ADDED_WEIGHT_FACTOR:
  def: '2.4'
  type: float
  cmt: Weight multiplier for chief roles over other advisor or idea types
GARRISON_TEMPLATE_SCORE_IC_FACTOR:
  def: '1.0'
  type: float
  cmt: ai uses these defines while calculating garrison template score of a template.
GARRISON_TEMPLATE_SCORE_MANPOWER_FACTOR:
  def: '0.05'
  type: float
  cmt: formula is (template_ic * ic_factor + template_manpower * manpower_factor ) /
    template_supression (lower is better)
ADVISOR_SCORE_TRAIT_MODIFIER_FACTOR:
  def: '0.2'
  type: float
  cmt: When scoring advisors, factor the score contribution from the advisor's trait
    modifiers by this value
ADVISOR_SCORE_CHEAPER_IS_BETTER_FACTOR:
  def: '0.1'
  type: float
  cmt: When scoring advisors, this define scales how much the AI prefers cheaper
    advisors over more expensive ones. 0.0 means no effect, 0.15 means a cost difference
    of 100 PP modifies the score by 15 %.
ADVISOR_SCORE_CHEAPER_IS_BETTER_MIN:
  def: '0.5'
  type: float
  cmt: Clamps the above scoring factor to at minimum this value
EVAL_MODIFIER_NON_PERCENT_FACTOR:
  def: '0.1'
  type: float
  cmt: Multiply non-percent-based modifiers with this to put the values in the
    approximately same range so they can be compared. (Why we are using 0.1 and not
    0.01? No idea...)
EVAL_MODIFIER_UNSPECIFIED_CATEGORY_FACTOR:
  def: '0.75'
  type: float
  cmt: Arbitrary scoring factor for modifiers the AI doesn't know how to categorize
EVAL_MODIFIER_MAX_COMMAND_POWER_FACTOR:
  def: '0.01'
  type: float
  cmt: Increasing CP cap with x is maybe 100 times less useful than e.g. gaining x more
    XP per day
MIN_AI_SCORE_TO_MOBILIZATION_LAW_OVERRIDE_HARD_CODED_SCORE:
  def: '0.0'
  type: float
MIN_AI_SCORE_TO_ECONOMY_LAW_OVERRIDE_HARD_CODED_SCORE:
  def: '0.0'
  type: float
MIN_AI_SCORE_TO_TRADE_LAW_OVERRIDE_HARD_CODED_SCORE:
  def: '1000.0'
  type: float
MIN_AI_SCORE_TO_ALL_LAWS_OVERRIDE_HARD_CODED_SCORE:
  def: '0.0'
  type: float
AT_WAR_THREAT_FACTOR:
  def: '2.0'
  type: float
  cmt: How much increase in threat does AI feel for being in war against someone
NEIGHBOUR_WAR_THREAT_FACTOR:
  def: '1.10'
  type: float
  cmt: How much increase in threat does AI feel against neighbours who are at war
POTENTIAL_ALLY_JOIN_WAR_FACTOR:
  def: '100'
  type: int
  cmt: How much increase in threat does AI feel against neighbours who are allied
    against one of our enemies
POTENTIAL_FUTURE_ENEMY_FACTOR:
  def: '100'
  type: int
  cmt: How much increase in threat does AI feel against neighbours who at war with our
    allies
NEUTRAL_THREAT_PARANOIA:
  def: '10'
  type: int
  cmt: How scared neutrals are of everyone
DIFFERENT_FACTION_THREAT:
  def: '30'
  type: int
  cmt: Threat caused by not being in the same faction
MAX_THREAT_FOR_FIRST_YEAR_CIVILIAN_MODE:
  def: '60'
  type: int
  cmt: above this threshold, ai will leave first year civilian factory mode which bumps
    it civilian factory scores while building
PLAN_ATTACK_MIN_ORG_FACTOR_LOW:
  def: '0.85'
  type: float
  cmt: Minimum org % for a unit to actively attack an enemy unit when executing a plan
PLAN_ATTACK_MIN_STRENGTH_FACTOR_LOW:
  def: '0.60'
  type: float
  cmt: Minimum strength for a unit to actively attack an enemy unit when executing a
    plan
PLAN_ATTACK_MIN_ORG_FACTOR_MED:
  def: '0.7'
  type: float
  cmt: (LOW,MED,HIGH) corresponds to the plan execution agressiveness level.
PLAN_ATTACK_MIN_STRENGTH_FACTOR_MED:
  def: '0.50'
  type: float
PLAN_ATTACK_MIN_ORG_FACTOR_HIGH:
  def: '0.45'
  type: float
PLAN_ATTACK_MIN_STRENGTH_FACTOR_HIGH:
  def: '0.30'
  type: float
PLAN_FRONTUNIT_DISTANCE_FACTOR:
  def: '10.0'
  type: float
  cmt: Factor for candidate units distance to front positions.
PLAN_ATTACK_DEPTH_FACTOR:
  def: '0.5'
  type: float
  cmt: Factor applied to size or enemy being attacked.
PLAN_STEP_COST_LIMIT:
  def: '9'
  type: int
  cmt: When stepping to draw a plan this cost makes it break if it hits hard terrain
    (multiplied by number of desired steps)
PLAN_STEP_COST_LIMIT_REDUCTION:
  def: '3'
  type: int
  cmt: Cost limit is reduced per iteration, making hard terrain less likely to be
    crossed the further into enemy territory it is
PLAN_MIN_SIZE_FOR_FALLBACK:
  def: '50'
  type: int
  cmt: A country with less provinces than this will not draw fallback plans, but rather
    station their troops along the front
SEND_VOLUNTEER_EVAL_BASE_DISTANCE:
  def: '175.0'
  type: float
  cmt: How far away it will evaluate sending volunteers if not a major power
SEND_VOLUNTEER_EVAL_MAJOER_POWER:
  def: '1.0'
  type: float
  cmt: How willing major powers are to send volunteers.
SEND_VOLUNTEER_EVAL_CONTAINMENT_FACTOR:
  def: '0.1'
  type: float
  cmt: How much AI containment factors into its evaluation of sending volunteers.
GIVE_STATE_CONTROL_MIN_CONTROLLED:
  def: '1'
  type: int
  cmt: AI needs to control more than this number of states before considering giving any
    away
GIVE_STATE_CONTROL_MIN_CONTROL_DIFF:
  def: '2'
  type: int
  cmt: The difference in number of controlled states compared to war participation needs
    to be bigger than this for the AI to consider giving a state to a country
RELATIVE_STRENGTH_TO_INVADE:
  def: '0.08'
  type: float
  cmt: Compares the estimated strength of the country/faction compared to it's enemies
    to see if it should invade or stay at home to defend.
RELATIVE_STRENGTH_TO_INVADE_DEFENSIVE:
  def: '0.4'
  type: float
  cmt: Compares the estimated strength of the country/faction compared to it's enemies
    to see if it should invade or stay at home to defend, but while being a defensive
    country.
GIVE_STATE_CONTROL_BASE_SCORE:
  def: '50'
  type: int
  cmt: Base diplo score for giving away control of states
GIVE_STATE_CONTROL_DIFF_FACTOR:
  def: '2.0'
  type: float
  cmt: Diplo score multiplier for state control compared to war participation difference
GIVE_STATE_CONTROL_NEIGHBOR_SCORE:
  def: '20'
  type: int
  cmt: Diplo score for each neighboring state controlled by the target
GIVE_STATE_CONTROL_NEIGHBOR_ACTOR_SCORE:
  def: '-5'
  type: int
  cmt: Diplo score for each neighboring state that is controlled by the sender
GIVE_STATE_CONTROL_NEIGHBOR_OTHER_SCORE:
  def: '5'
  type: int
  cmt: Diplo score for each neighboring state controlled by someone else
GIVE_STATE_CONTROL_MAX_SCORE_DIST:
  def: '600'
  type: int
  cmt: A State that is closer to the recipient capital than this gets a score bonus
    based on the below value
GIVE_STATE_CONTROL_DIST_SCORE_MULT:
  def: '0.2'
  type: float
  cmt: Multiplier for the score gained from distance ( GIVE_STATE_CONTROL_MAX_SCORE_DIST
    - distance ) * this
IRRATIONALITY_LAMBDA:
  def: '200'
  type: int
  cmt: Lambda given to Poisson Random function determining if a leader should act a bit
    irrational
GENERATE_WARGOAL_THREAT_BASELINE:
  def: '1.0'
  type: float
  cmt: The baseline for what the AI considers the world is getting dangerous and we want
    to generate wargoals with no antagonize value
GENERATE_WARGOAL_ANTAGONIZE_SCALE:
  def: '0.35'
  type: float
  cmt: works to scale the AIs antagonize value vs the threat baseline for when it should
    act on existing claims: threat used for baseline is min_threat - antagonize * scale
RESERVE_TO_COMMITTED_BALANCE:
  def: '0.3'
  type: float
  cmt: How many reserves compared to number of committed divisions in a combat (1.0 = as
    many as reserves as committed)
DIPLOMACY_COMMUNIST_NOT_NEIGHBOUR:
  def: '-10'
  type: int
  cmt: Communists want to stay consolidated with their influence
MAIN_ENEMY_FRONT_IMPORTANCE:
  def: '4.0'
  type: float
  cmt: How much extra focus the AI should put on who it considers to be its current main
    enemy.
EASY_TARGET_FRONT_IMPORTANCE:
  def: '7.5'
  type: float
  cmt: How much extra focus the AI should put on who it considers to be the easiest
    target.
AI_FRONT_MOVEMENT_FACTOR_FOR_READY:
  def: '0.25'
  type: float
  cmt: If less than this fraction of units on a front is moving, AI sees it as ready for
    action
MICRO_POCKET_SIZE:
  def: '4'
  type: int
  cmt: Pockets with a size equal to or lower than this will be mocroed by the AI, for
    efficiency.
DECLARE_WAR_MIN_FRONT_SIZE_TO_CONSIDER_FOR_NOT_READY:
  def: '0.04'
  type: float
  cmt: fronts with less armies than this ratio compared to total number of armies are
    ignored when ai checks if it is ready for war
POCKET_DISTANCE_MAX:
  def: '40000'
  type: int
  cmt: shortest square distance we bother about chasing pockets
VP_MAX_PROVINCE_WORTH:
  def: '500'
  type: int
  cmt: Max worth a province can have to a defensive order
VP_LEVEL_IMPORTANCE_MEDIUM:
  def: '10'
  type: int
  cmt: Victory points with values higher than or equal to this are considered to be of
    medium importance.
AREA_DEFENSE_CAPITAL_PEACE_VP_WEIGHT:
  def:
    - [1.0, 1.0, 1.0]
  type: table
AREA_DEFENSE_CAPITAL_VP_WEIGHT:
  def:
    - [0.0, 1.0, 2.0]
  type: table
AREA_DEFENSE_HOME_VP_WEIGHT:
  def:
    - [0.0, 0.5, 1.0]
  type: table
AREA_DEFENSE_OTHER_VP_WEIGHT:
  def:
    - [0.0, 0.0, 1.0]
  type: table
AREA_DEFENSE_CAPITAL_PEACE_COAST_WEIGHT:
  def:
    - [0.0, 0.0, 0.0]
  type: table
AREA_DEFENSE_CAPITAL_COAST_WEIGHT:
  def:
    - [0.0, 0.2, 0.7]
  type: table
AREA_DEFENSE_HOME_COAST_WEIGHT:
  def:
    - [0.0, 0.1, 0.5]
  type: table
AREA_DEFENSE_OTHER_COAST_WEIGHT:
  def:
    - [0.0, 0.0, 0.0]
  type: table
AREA_DEFENSE_CAPITAL_PEACE_BASE_WEIGHT:
  def:
    - [0.0, 0.0, 0.0]
  type: table
AREA_DEFENSE_CAPITAL_BASE_WEIGHT:
  def:
    - [0.5, 1.0, 1.5]
  type: table
AREA_DEFENSE_HOME_BASE_WEIGHT:
  def:
    - [0.5, 1.0, 1.0]
  type: table
AREA_DEFENSE_OTHER_BASE_WEIGHT:
  def:
    - [0.5, 0.5, 1.0]
  type: table
ESTIMATED_CONVOYS_PER_DIVISION:
  def: '6'
  type: int
  cmt: Not always correct, but mainly used to make sure AI does not go crazy
ENTRENCHMENT_WEIGHT:
  def: '2.0'
  type: float
  cmt: AI should favour units with less entrenchment when assigning units around.
FRONT_TERRAIN_DEFENSE_FACTOR:
  def: '3.75'
  type: float
  cmt: Multiplier applied to unit defense modifier for terrain on front province
    multiplied by terrain importance
FRONT_TERRAIN_ATTACK_FACTOR:
  def: '5.0'
  type: float
  cmt: Multiplier applied to unit attack modifier for terrain on enemy front province
    multiplied by terrain importance
BASE_DISTANCE_TO_CARE:
  def: '600.0'
  type: float
  cmt: Countries that are too far away are less interesting in diplomacy
MIN_FORCE_RATIO_TO_PROTECT:
  def: '0.5'
  type: float
  cmt: Tiny countries should not feel protective or really large ones
ORG_UNIT_STRONG:
  def: '0.75'
  type: float
  cmt: Organization % for unit to be considered strong
STR_UNIT_STRONG:
  def: '0.70'
  type: float
  cmt: Strength (equipment) % for unit to be considered strong
ORG_UNIT_WEAK:
  def: '0.25'
  type: float
  cmt: Organization % for unit to be considered weak
STR_UNIT_WEAK:
  def: '0.30'
  type: float
  cmt: Strength (equipment) % for unit to be considered weak
ORG_UNIT_NORMAL:
  def: '0.35'
  type: float
  cmt: Organization % for unit to be considered normal
STR_UNIT_NORMAL:
  def: '0.4'
  type: float
  cmt: Strength (equipment) % for unit to be considered normal
PLAN_FACTION_STRONG_TO_EXECUTE:
  def: '0.50'
  type: float
  cmt: % or more of units in an order to consider executing the plan
PLAN_FACTION_NORMAL_TO_EXECUTE:
  def: '0.65'
  type: float
  cmt: % or more of units in an order to consider executing the plan
PLAN_FACTION_WEAK_TO_ABORT:
  def: '0.65'
  type: float
  cmt: % or more of units in an order to consider executing the plan
PLAN_AVG_PREPARATION_TO_EXECUTE:
  def: '0.5'
  type: float
  cmt: % or more average plan preparation before executing
REDEPLOY_DISTANCE_VS_ORDER_SIZE:
  def: '1.0'
  type: float
  cmt: Factor applied to the path length of a unit compared to length of an order to
    determine if it should use strategic redeployment
FORT_LEVEL_TO_CONSIDER_HIGHLY_FORTIFIED:
  def: '1'
  type: int
  cmt: Provinces above this level of fortification will be considered highly fortified
    by plan evaluation
PLAN_VALUE_FORTIFICATION_LEVEL_MAX_PENALTY:
  def: '-0.5'
  type: float
  cmt: Max plan value penalty from fortification. This is scaled by number of provinces
    along a frontline, over the number which exceed the fort value value above
MAX_ALLOWED_NAVAL_DANGER:
  def: '80'
  type: int
  cmt: AI will ignore naval paths that has danger value of above this threshold while
    assigning units
TRANSFER_DANGER_HOSTILE_SHIPS:
  def: '50'
  type: int
  cmt: max danger from complete enemy naval supriority over ai in an area
EXPORT_RESOURCE_TRADE_NEED_IMPORTANCE:
  def: '0.5'
  type: float
  cmt: how important is each lost resource to overexport for trade law selection
OPERATION_EQUIPMENT_NEED_PRODUCTION_MULT:
  def: '1.0'
  type: float
  cmt: equipment requests for operations will be added the equipment needs that ai
    considers while assigning factories to production
MIN_FUEL_RATIO_TO_NOT_IGNORE_STRIKE_FORCE_COST:
  def: '0.0'
  type: float
  cmt: ai will still assign strike forces unless fuel ratio drops below this one
MIN_FUEL_RATIO_TO_NOT_IGNORE_INVASION_SUPPORT_COST:
  def: '0.0'
  type: float
  cmt: ai will still naval invasion support forces unless fuel ratio drops below this
    one
ENEMY_HOME_AREA_RATIO_TO_DISABLE_INVASIONS:
  def: '0.3'
  type: float
  cmt: if we are fighting against an enemy home area from our home area and if the enemy
    area is larger than this ratio, non strategy invasions are disabled
HOURS_BETWEEN_ENCIRCLEMENT_DISCOVERY:
  def: '72'
  type: int
  cmt: Per army, interval in hours between refresh of which provinces it considers make
    up potential encirclement points
FASCISTS_BEFRIEND_FASCISTS:
  def: '10'
  type: int
FASCISTS_BEFRIEND_DEMOCRACIES:
  def: '-25'
  type: int
FASCISTS_BEFRIEND_COMMUNISTS:
  def: '-25'
  type: int
FASCISTS_ALLY_FASCISTS:
  def: '0'
  type: int
FASCISTS_ALLY_DEMOCRACIES:
  def: '-100'
  type: int
FASCISTS_ALLY_COMMUNISTS:
  def: '-100'
  type: int
FASCISTS_ANTAGONIZE_FASCISTS:
  def: '-10'
  type: int
FASCISTS_ANTAGONIZE_DEMOCRACIES:
  def: '100'
  type: int
FASCISTS_ANTAGONIZE_COMMUNISTS:
  def: '100'
  type: int
DEMOCRACIES_BEFRIEND_FASCISTS:
  def: '-25'
  type: int
DEMOCRACIES_BEFRIEND_DEMOCRACIES:
  def: '0'
  type: int
DEMOCRACIES_BEFRIEND_COMMUNISTS:
  def: '-25'
  type: int
DEMOCRACIES_ALLY_FASCISTS:
  def: '-50'
  type: int
DEMOCRACIES_ALLY_DEMOCRACIES:
  def: '0'
  type: int
DEMOCRACIES_ALLY_COMMUNISTS:
  def: '-50'
  type: int
DEMOCRACIES_ANTAGONIZE_FASCISTS:
  def: '0'
  type: int
DEMOCRACIES_ANTAGONIZE_DEMOCRACIES:
  def: '-25'
  type: int
DEMOCRACIES_ANTAGONIZE_COMMUNISTS:
  def: '0'
  type: int
COMMUNISTS_BEFRIEND_FASCISTS:
  def: '-25'
  type: int
COMMUNISTS_BEFRIEND_DEMOCRACIES:
  def: '-25'
  type: int
COMMUNISTS_BEFRIEND_COMMUNISTS:
  def: '25'
  type: int
COMMUNISTS_ALLY_FASCISTS:
  def: '-100'
  type: int
COMMUNISTS_ALLY_DEMOCRACIES:
  def: '-50'
  type: int
COMMUNISTS_ALLY_COMMUNISTS:
  def: '0'
  type: int
COMMUNISTS_ANTAGONIZE_FASCISTS:
  def: '100'
  type: int
COMMUNISTS_ANTAGONIZE_DEMOCRACIES:
  def: '10'
  type: int
COMMUNISTS_ANTAGONIZE_COMMUNISTS:
  def: '-10'
  type: int
TENSION_MIN_FOR_GUARANTEE_VS_MINOR:
  def: '10'
  type: int
  cmt: for non faction people AI will not consider you worth guaranteeing below this
NUM_AI_MESSAGES:
  def: '10'
  type: int
  cmt: Set to whatever category has the highest number of messages
DIPLOMACY_FACTION_WAR_WANTS_HELP:
  def: '50'
  type: int
  cmt: Desire to send to nations to join a faction if you are at war
DIPLOMACY_FACTION_CIVILWAR_WANTS_HELP:
  def: '-50'
  type: int
FACTION_UNSTABLE_ACCEPTANCE:
  def: '-100'
  type: int
DIPLOMACY_AT_WAR_WITH_ALLY_RELUCTANCE:
  def: '-1000'
  type: int
DIPLOMACY_FACTION_JOIN_COUP_INITIATOR_BONUS:
  def: '70'
  type: int
  cmt: If a country initiated coup on an another country, civil war revolter is more
    likely to join initiator's faction
SHIPS_PRODUCTION_BASE_COST:
  def: '10000'
  type: int
  cmt: Used by the AI to normalize IC values when picking what ship to build.
NEEDED_NAVAL_FACTORIES_EXPENSIVE_SHIP_BONUS:
  def: '12'
  type: int
  cmt: Amount of naval yards you need to get a bonus to building really expensive ships
FORTIFIED_RATIO_TO_CONSIDER_A_FRONT_FORTIFIED:
  def: '0.5'
  type: float
  cmt: ai will consider a front fortified if this ratio of provinces has fort
HEAVILY_FORTIFIED_RATIO_TO_CONSIDER_A_FRONT_FORTIFIED:
  def: '0.5'
  type: float
  cmt: ai will consider a front super fortified if this ratio of provinces has lots of
    forts
FORTIFIED_MIN_ORG_FACTOR_TO_CONSIDER_A_FRONT_FORTIFIED:
  def: '0.2'
  type: float
  cmt: ai will treat fortified provinces as unfortified if no unit in that province has
    an organization factor at least this high
DESPERATE_AI_MIN_UNIT_ASSIGN_TO_ESCAPE:
  def: '0'
  type: int
  cmt: AI will assign at least this amount of units to break from desperate situations
DESPERATE_AI_WEAK_UNIT_STR_LIMIT:
  def: '0.35'
  type: float
  cmt: ai will increase number of units assigned to break from desperate situations when
    units are start falling lower than this str limit
DESPERATE_AI_MIN_ORG_BEFORE_ATTACK:
  def: '0.3'
  type: float
  cmt: ai will wait for this much org to attack an enemy prov in desperate situations
DESPERATE_AI_MIN_ORG_BEFORE_MOVE:
  def: '0.06'
  type: float
  cmt: ai will wait for this much org to move in desperate situations
DESPERATE_ATTACK_WITHOUT_ORG_WHEN_NO_ORG_GAIN:
  def: '120'
  type: int
  cmt: if ai can't regain enough org to attack in this many hours, it will go truly
    desperate and attack anyway (still has to wait for move org)
MAX_REQUEST_EXPEDITIONARIES_ARMY_RATIO:
  def: '0.3'
  type: float
  cmt: AI will not accept expeditionary requests if its expeditions are above this ratio
CASUALTY_RATIO_TO_PULL_EXPEDITIONARIES_BACK:
  def: '0.1'
  type: float
  cmt: AI will pull expeditioniries back if its casualties is aboce this ratio compared
    to their total deployed manpower
CASUALTY_RATIO_TO_NOT_SEND_EXPEDITIONARIES:
  def: '0.05'
  type: float
  cmt: AI will not send expeditioniries if its casualties is aboce this ratio compared
    to their total deployed manpower
SURRENDER_LEVEL_TO_PULL_EXPEDITIONARIES_BACK:
  def: '0.3'
  type: float
  cmt: AI will pull expeditioniries back if its surrender level is above this ratio
SURRENDER_LEVEL_TO_NOT_SEND_EXPEDITIONARIES:
  def: '0.15'
  type: float
  cmt: AI will not send expeditioniries if its surrender level is above this ratio
EXPEDITIONARY_CASUALTY_DECAY_RATIO:
  def: '0.3333'
  type: float
  cmt: expeditionary manpower lost will decay by thousands daily by this ratio (compared
    to deployed manpower)
NUM_DAYS_TO_PULL_EXPEDITIONARIES_BACK:
  def: '14'
  type: int
  cmt: AI will pull units back from non-ai players after waiting this days if things are
    not going well for its units
ACCESS_SCORE_FOR_DEMOCRATIC_COUNTRIES:
  def: '500'
  type: int
  cmt: democracies gives each other access if they have a common enemy
AI_AIR_MISSION_COVERAGE_TO_STAY_PUT:
  def: '0.5'
  type: float
  cmt: AI will not rebase air wings on missions if their new mission target exceeds this
    percentage of region coverage
ACCESS_SCORE_PENALTY_PER_EXISTING_ACCESS_AT_WAR:
  def: '250'
  type: int
  cmt: each access reduces the desire of next access
ACCESS_SCORE_PENALTY_PER_EXISTING_ACCESS:
  def: '500'
  type: int
  cmt: each access reduces the desire of next access
NAVAL_ACCESS_SCORE_PENALTY_PER_EXISTING_ACCESS_AT_WAR:
  def: '150'
  type: int
NAVAL_ACCESS_SCORE_PENALTY_PER_EXISTING_ACCESS:
  def: '250'
  type: int
AIR_BASE_ACCESS_SCORE_PENALTY_PER_EXISTING_ACCESS_AT_WAR:
  def: '150'
  type: int
AIR_BASE_ACCESS_SCORE_PENALTY_PER_EXISTING_ACCESS:
  def: '250'
  type: int
TOO_INSIGNIFICANT_ARMY_RATIO_BEGIN:
  def: '0.75'
  type: float
  cmt: if army ratio is of a country is larger than this threshold, it will be less
    reluctant to accept certain diplo actions
TOO_INSIGNIFICANT_MAX_PENALTY:
  def: '350'
  type: int
  cmt: max penalty that will be applied for thinking a country is too insignificant
WANTED_UNITS_INDUSTRY_FACTOR:
  def: '1.60'
  type: float
  cmt: How many units a country wants is partially based on how much military industry
    that is available
WANTED_UNITS_THREAT_BASE:
  def: '0.7'
  type: float
  cmt: If no threat, multiply min wanted units by this
WANTED_UNITS_THREAT_MAX:
  def: '6.0'
  type: float
  cmt: Normalized threat is clamped to this
WANTED_UNITS_WAR_THREAT_FACTOR:
  def: '1.15'
  type: float
  cmt: Factor threat with this if country is at war. this value is overriden by the
    value in ideology database if that value exceedes this.
WANTED_UNITS_DANGEROUS_NEIGHBOR_FACTOR:
  def: '1.15'
  type: float
  cmt: Factor if has dangerous neighbor
WANTED_UNITS_MANPOWER_DIVISOR:
  def: '21000'
  type: int
  cmt: Normalizing divisor for AI manpower. (for each x max available manpower, they
    want one division)
WANTED_UNITS_WEIGHT_FRONTS_WANT:
  def: '0.35'
  type: float
  cmt: Weight of front needs when computing final nr wanted units
WANTED_UNITS_WEIGHT_FACTORIES:
  def: '0.45'
  type: float
  cmt: Weight of military factories when computing final nr wanted units
WANTED_UNITS_WEIGHT_MANPOWER:
  def: '0.3'
  type: float
  cmt: Weight of manpower availability when computing final nr wanted units
WANTED_UNITS_MIN_DEFENCE_FACTOR:
  def: '0.4'
  type: float
  cmt: Factor on units required for min defence
WANTED_UNITS_MAX_WANTED_CAP:
  def: '500'
  type: int
  cmt: Maximum wanted divisions for a country. This can be exceeded by certain hardcoded
    multipliers, but not by base calculation logic.
WANTED_LAND_PLANES_PER_BASE_CAPACITY_FACTOR:
  def: '1'
  type: int
  cmt: Scales how many land-based planes the AI want per air base space (excluding
    carriers).
WANTED_LAND_PLANES_PER_DIVISION:
  def: '20'
  type: int
  cmt: How many land-based planes the AI want for each division it wants.
WANTED_LAND_PLANES_TOTAL_MAX_PER_DIVISION:
  def: '100'
  type: int
  cmt: The max total number of land-based planes the AI want.
WANTED_CARRIER_PLANES_PER_CARRIER_CAPACITY_FACTOR:
  def: '1.5'
  type: float
  cmt: Scales how many carrier planes the AI want per carrier deck space.
WANTED_CARRIER_PLANES_PER_CARRIER_CAPACITY_IN_PRODUCTION_FACTOR:
  def: '1'
  type: int
  cmt: Scales how many carrier planes the AI want per deck space of carriers in
    production.
CARRIER_CAPACITY_IN_PRODUCTION_MAX_DAYS_LEFT_TO_INCLUDE_FACTOR:
  def: '365'
  type: int
  cmt: Carriers in production that will take more days to complete than this value will
    be ignored when calculating the above.
START_TRAINING_EQUIPMENT_LEVEL:
  def: '0.40'
  type: float
  cmt: ai will not start to train if equipment drops below this level
STOP_TRAINING_EQUIPMENT_LEVEL:
  def: '0.30'
  type: float
  cmt: ai will not train if equipment drops below this level
START_TRAINING_SUPPLY_LEVEL:
  def: '0.40'
  type: float
  cmt: ai will not start to train if supply ratio drops below this level
STOP_TRAINING_SUPPLY_LEVEL:
  def: '0.30'
  type: float
  cmt: ai will not train if supply ratio drops below this level
STOP_TRAINING_FULLY_TRAINED_FACTOR:
  def: '0.95'
  type: float
  cmt: ai will not train if at least this ratio of divisions in the army are fully
    trained
BUILD_REFINERY_LACK_OF_RESOURCE_MODIFIER:
  def: '0.003'
  type: float
  cmt: How much lack of resources are worth when evaluating what to build.
DIVISION_DESIGN_MAX_FAILED_DAYS:
  def: '60'
  type: int
  cmt: max days we keep track of since failure of a template design update
DIVISION_MATCH_ROLE_BOOST_FACTOR:
  def: '1.2'
  type: float
  cmt: When finding closest matching existing template to a target template, boost the
    score by this much if the template also has the correct role
EQUIPMENT_DESIGN_MAX_FAILED_DAYS:
  def: '60'
  type: int
  cmt: max days we keep track of since failure of an equipment design update
UPGRADE_DIVISION_RELUCTANCE:
  def: '7'
  type: int
  cmt: How often to consider upgrading to new templates for units in the field
UPGRADE_PERCENTAGE_OF_FORCES:
  def: '0.03'
  type: float
  cmt: How big part of the army that should be considered for upgrading
REMOVE_OBSOLETE_TEMPLATE_DAYS:
  def: '180'
  type: int
  cmt: Remove obsolete and unused templates if they have been marked as obsolete for x
    days. Non-positive value means "never remove".
REFIT_SHIP_RELUCTANCE:
  def: '28'
  type: int
  cmt: How often to consider refitting to new equipment variants for ships in the field
REFIT_SHIP_PERCENTAGE_OF_FORCES:
  def: '0.1'
  type: float
  cmt: How big part of the navy that should be considered for refitting
NAVY_PREFERED_MAX_SIZE:
  def: '25'
  type: int
  cmt: AI will generally attempt to merge fleets into this size, but as a soft limit.
INVASION_COASTAL_PROVS_PER_ORDER:
  def: '24'
  type: int
  cmt: AI will consider one extra invasion per number of provinces stated here (num
    orders = total coast / this)
MIN_INVASION_AREA_SIZE_FOR_FLOATING_HARBORS:
  def: '15'
  type: int
  cmt: AI will consider using floating harbors for naval invasion if invasion area is
    larger than this many provinces
CONVOY_NEED_SAFETY_BUFFER:
  def: '1.30'
  type: float
  cmt: AI will try and keep 15% more convoys than what it needs.
REGION_THREAT_PER_SUNK_CONVOY:
  def: '25'
  type: int
  cmt: Threat value per convoy sunk in a region. Decays over time.
REGION_THREAT_LEVEL_TO_AVOID_REGION:
  def: '25 * 10'
  type: string
  cmt: How much threat must be generated in region ( by REGION_THREAT_PER_SUNK_CONVOY )
    so the AI will decide to mark the region as avoid
REGION_THREAT_LEVEL_TO_BLOCK_REGION:
  def: '25 * 100'
  type: string
  cmt: How much threat must be generated in region ( by REGION_THREAT_PER_SUNK_CONVOY )
    so the AI will decide to mark the region as avoid
REGION_CONVOY_DANGER_DAILY_DECAY:
  def: '1'
  type: int
  cmt: When convoys are sunk it generates threat in the region which the AI uses to prio
    nalval missions
PRODUCTION_LINE_SWITCH_SURPLUS_NEEDED_MODIFIER:
  def: '0.2'
  type: float
  cmt: Is modified by efficency modifiers.
PLAN_ACTIVATION_MAJOR_WEIGHT_FACTOR:
  def: '1.5'
  type: float
  cmt: AI countries will hold on activating plans if stronger countries have plans in
    the same location. Majors count extra (value of 1 will negate this)
PLAN_ACTIVATION_PLAYER_WEIGHT_FACTOR:
  def: '50.0'
  type: float
  cmt: AI countries will hold on activating plans if player controlled countries have
    plans in the same location.
AREA_DEFENSE_BASE_IMPORTANCE:
  def: '30'
  type: int
  cmt: Area defense order base importance value (used for determining order of troop
    selections)
AREA_DEFENSE_CIVIL_WAR_IMPORTANCE:
  def: '30'
  type: int
  cmt: Area defense order importance value when a country is in a civil war as target or
    revolter.
AREA_DEFENSE_IMPORTANCE_FACTOR:
  def: '1.0'
  type: float
  cmt: used to balance defensive area importance vs other fronts
MAX_DISTANCE_NAVAL_INVASION:
  def: '200.0'
  type: float
  cmt: AI is extremely unwilling to plan naval invasions above this naval distance
    limit.
ENEMY_NAVY_STRENGTH_DONT_BOTHER:
  def: '2.5'
  type: float
  cmt: If the enemy has a navy at least these many times stronger that the own, don't
    bother invading
MIN_SUPPLY_USE_SANITY_CAP:
  def: '100'
  type: int
  cmt: Ignore supply cap if below this value when deciding on how many divisions to
    produce.
MAX_SUPPLY_DIVISOR:
  def: '1.75'
  type: float
  cmt: To make sure the AI does not overdeploy divisions. Higher number means more
    supply per unit.
MISSING_CONVOYS_BOOST_FACTOR:
  def: '50.0'
  type: float
  cmt: The more convoys a country is missing, the more resources it diverts to cover
    this.
TRANSPORTS_PER_PARATROOPER:
  def: '20'
  type: int
  cmt: Currently unused.
MAX_MICRO_ATTACKS_PER_ORDER:
  def: '3'
  type: int
  cmt: AI goes through its orders and checks if there are situations to take advantage
    of
FALLBACK_LOSING_FACTOR:
  def: '1.0'
  type: float
  cmt: The lower this number, the longer the AI will hold the line before sending them
    to the fallback line
PRODUCTION_MAX_PROGRESS_TO_SWITCH_NAVAL:
  def: '0.1'
  type: float
  cmt: AI will not replace ships being built by newer types if progress is above this
PRODUCTION_WAIT_TO_FINISH_IF_EXPENSIVE:
  def: '0.1'
  type: float
  cmt: If produced item is expensive (producing less than one/week), wait to finish item
    if progress is above this
PRODUCTION_WAIT_TO_FINISH_IF_CHEAP:
  def: '0.75'
  type: float
  cmt: If produced item is cheap (producing more than one/week), wait to finish item if
    progress is above this
STATE_CONTROL_FOR_AREA_DEFENSE:
  def: '0.4'
  type: float
  cmt: To avoid AI sending area defense to area with very little foothold
FORCE_FACTOR_AGAINST_EXTRA_MINOR:
  def: '0.15'
  type: float
  cmt: AI considers generating wargoals against minors below this % of force compared to
    themselves to get at a bigger enemy.
MAX_EXTRA_WARGOAL_GENERATION:
  def: '2'
  type: int
  cmt: AI may want to generate wargoals against weak minors to get at larger enemy, but
    never more that this at any given time.
NAVAL_MISSION_DISTANCE_BASE:
  def: '3500'
  type: int
  cmt: Base value when AI is evaluating distance score to places
NAVAL_MISSION_INVASION_BASE:
  def: '1000'
  type: int
  cmt: Base score for region with naval invasion (modified dynamically by prioritizing
    orders)
NAVAL_MISSION_AGGRESSIVE_PATROL_DIVISOR:
  def: '1'
  type: int
  cmt: Divides patrol score when not defending
NAVAL_MISSION_AGGRESSIVE_ESCORT_DIVISOR:
  def: '2'
  type: int
  cmt: Divides escort score when not defending
NAVAL_MISSION_PATROL_NEAR_OWNED:
  def: '500'
  type: int
  cmt: Extra patrol mission score near owned provinces
NAVAL_MISSION_ESCORT_NEAR_OWNED:
  def: '300'
  type: int
  cmt: Extra escort mission score near owned provinces
NAVAL_MISSION_PATROL_NEAR_CONTROLLED:
  def: '140'
  type: int
  cmt: Extra patrol mission score near controlled provinces
NAVAL_MISSION_ESCORT_NEAR_CONTROLLED:
  def: '200'
  type: int
  cmt: Extra escort mission score near controlled provinces
NAVAL_MISSION_MINES_PLANTING_NEAR_OWNED:
  def: '40000'
  type: int
NAVAL_MISSION_MINES_PLANTING_NEAR_CONTROLLED:
  def: '30000'
  type: int
NAVAL_MISSION_MINES_SWEEPING_NEAR_OWNED:
  def: '60000'
  type: int
  cmt: How likely the AI will do the sweeping missions. The value is scaled by the
    amount of mines to sweep.
NAVAL_MISSION_MINES_SWEEPING_NEAR_CONTROLLED:
  def: '50000'
  type: int
  cmt: Same as above, but nearby the controlled territory.
NEW_LEADER_EXTRA_CP_FACTOR:
  def: '2.0'
  type: float
  cmt: Country must have at least this many times extra command power to get new
    admirals or army leaders
SCARY_LEVEL_AVERAGE_DEFENSE:
  def: '-0.7'
  type: float
  cmt: average front defense modifier to make it consider it as a PITA to go for
ATTACK_HEAVILY_DEFENDED_LIMIT:
  def: '0.5'
  type: float
  cmt: AI will not launch attacks against heavily defended fronts unless they consider
    to have this level of advantage (1.0 = 100%)
CANCEL_COMBAT_DISADVANTAGE_RATIO:
  def: '1.5'
  type: float
  cmt: If the enemy's advantage ratio over us during (normal) combat is more than
    <value>, allow canceling the attack
CANCEL_COMBAT_MIN_DURATION_HOURS:
  def: '48'
  type: int
  cmt: Only allow cancelling (normal) combat if at least <value> hours have passed
CANCEL_INVASION_COMBAT_DISADVANTAGE_RATIO:
  def: '3.5'
  type: float
  cmt: If the enemy's advantage ratio over us during invasion combat is more than
    <value>, allow canceling the attack
CANCEL_INVASION_COMBAT_MIN_DURATION_HOURS:
  def: '720'
  type: int
  cmt: Only allow cancelling invasion combat if at least <value> hours have passed
MIN_PLAN_VALUE_TO_MICRO_INACTIVE:
  def: '0.25'
  type: float
  cmt: The AI will not consider members of groups which plan is not activated AND
    evaluates lower than this.
MAX_UNITS_FACTOR_AREA_ORDER:
  def: '0.75'
  type: float
  cmt: Factor for max number of units to assign to area defense orders
DESIRED_UNITS_FACTOR_AREA_ORDER:
  def: '0.7'
  type: float
  cmt: Factor for desired number of units to assign to area defense orders
MIN_UNITS_FACTOR_AREA_ORDER:
  def: '1.0'
  type: float
  cmt: Factor for min number of units to assign to area defense orders
MAX_UNITS_FACTOR_FRONT_ORDER:
  def: '1.0'
  type: float
  cmt: Factor for max number of units to assign to area front orders
DESIRED_UNITS_FACTOR_FRONT_ORDER:
  def: '1.1'
  type: float
  cmt: Factor for desired number of units to assign to area front orders
MIN_UNITS_FACTOR_FRONT_ORDER:
  def: '1.0'
  type: float
  cmt: Factor for min number of units to assign to area front orders
MAX_UNITS_FACTOR_INVASION_ORDER:
  def: '1.0'
  type: float
  cmt: Factor for max number of units to assign to naval invasion orders
DESIRED_UNITS_FACTOR_INVASION_ORDER:
  def: '1.0'
  type: float
  cmt: Factor for desired number of units to assign to naval invasion orders
MIN_UNITS_FACTOR_INVASION_ORDER:
  def: '1.0'
  type: float
  cmt: Factor for min number of units to assign to naval invasion orders
FRONT_UNITS_CAP_FACTOR:
  def: '15.0'
  type: float
  cmt: A factor applied to total front size and supply use. Primarily effects small
    fronts
MAX_DIST_PORT_RUSH:
  def: '20.0'
  type: float
  cmt: If a unit is in enemy territory with no supply it will consider nearby ports
    within this distance.
MIN_FIELD_STRENGTH_TO_BUILD_UNITS:
  def: '0.7'
  type: float
  cmt: Cancel unit production if below this to get resources out to units in the field
MIN_MANPOWER_TO_BUILD_UNITS:
  def: '0.7'
  type: float
  cmt: Cancel unit production if below this to get resources out to units in the field
AVERAGE_SUPPLY_USE_PESSIMISM:
  def: '1.5'
  type: float
  cmt: Multiplier for when AI calculates average supply use of entire army.
PROPOSE_LEND_LEASE_AIDESIRE_SAME_IDEOLOGY:
  def: '40'
  type: int
  cmt: Added to AI desire to propose lend lease if recipent is same ideology (and AI
    can't declare war on recipient)
PROPOSE_LEND_LEASE_AIDESIRE_SAME_IDEOLOGY_CIVIL_WAR:
  def: '25'
  type: int
  cmt: Added to AI desire to propose lend lease if recipent is same ideology and they
    are currently in civil war
SEND_VOLUNTEER_AIDESIRE_SAME_IDEOLOGY:
  def: '40'
  type: int
  cmt: Added to AI desire to send volunteers if recipent is same ideology (and AI can't
    declare war on recipient)
SEND_VOLUNTEER_AIDESIRE_SAME_IDEOLOGY_CIVIL_WAR:
  def: '25'
  type: int
  cmt: Added to AI desire to send volunteers if recipent is same ideology and they are
    currently in civil war
REQUEST_LEND_LEASE_PROTECT_VALUE:
  def: '75'
  type: int
  cmt: Limit for protect enemy desire for reducing lend lease desire
REQUEST_LEND_LEASE_CONTAINS_VALUE:
  def: '100'
  type: int
  cmt: Limit of contain enemy desire for boosting friendly help
FRONT_BULGE_RATIO_UPPER_CUTOFF:
  def: '1.5'
  type: float
  cmt: If total bulginess is lower than this, the front is ignored.
FRONT_BULGE_RATIO_LOWER_CUTOFF:
  def: '0.95'
  type: float
  cmt: If local bulginess drops below this, a point of interest is found
FRONT_CUTOFF_MIN_EDGE_PROXIMITY:
  def: '2'
  type: int
  cmt: Minimum number of provinces to the front edge to determine for cutoff oportunity.
AIR_SCORE_DISTANCE_IMPACT:
  def: '0.3'
  type: float
  cmt: Effect of distance applied to the score calculations
DAYS_BETWEEN_AIR_PRIORITIES_UPDATE:
  def: '4'
  type: int
  cmt: Amount of days between air ai updates priorities for air wings ( from 1 to N )
NAVAL_AIR_SUPERIORITY_IMPORTANCE:
  def: '0.10'
  type: float
  cmt: Strategic importance of air superiority ( amount of enemy planes in area )
NAVAL_SHIP_AIR_IMPORTANCE:
  def: '2.0'
  type: float
  cmt: Naval ship air importance
NAVAL_SHIP_IN_PORT_AIR_IMPORTANCE:
  def: '6.0'
  type: float
  cmt: Naval ship in the port air importance
NAVAL_COMBAT_AIR_IMPORTANCE:
  def: '8.0'
  type: float
  cmt: Naval combat air importance
NAVAL_TRANSFER_AIR_IMPORTANCE:
  def: '0.0'
  type: float
  cmt: Naval transfer air importance
NAVAL_COMBAT_TRANSFER_AIR_IMPORTANCE:
  def: '50.0'
  type: float
  cmt: Naval combat involving enemy land units
NAVAL_IMPORTANCE_SCALE:
  def: '0.65'
  type: float
  cmt: Naval total importance scale (every naval score get's multiplied by it)
NAVAL_COMBAT_OUR_NAVY_MULT_ON_IMPORTANCE:
  def: '0.35'
  type: float
  cmt: Naval region importance are scaled by our ships as well
NAVAL_COMBAT_ALLY_NAVY_MULT_ON_IMPORTANCE:
  def: '0.15'
  type: float
  cmt: Naval region importance are scaled by our ships as well
NAVAL_COMBAT_MIN_OUR_NAVY_MULT_ON_IMPORTANCE:
  def: '0.5'
  type: float
  cmt: Min scale factor for naval region importance from our ships
NAVAL_COMBAT_MAX_OUR_NAVY_MULT_ON_IMPORTANCE:
  def: '1.0'
  type: float
  cmt: Max scale factor for naval region importance from our ships
NAVAL_RANGE_FOR_DOCKING_RIGHTS_CHECK:
  def: '240.0'
  type: float
  cmt: Naval range used to check if docking rights would allow us to reach a specific
    province
NAVAL_PATROL_PLANES_PER_SHIP_PATROLLING:
  def: '10.0'
  type: float
  cmt: Amount of naval patrol planes per ship on a patrol mission
NAVAL_PATROL_PLANES_PER_SHIP_RAIDING:
  def: '10.0'
  type: float
  cmt: Amount of naval patrol planes per ship on a convoy raid mission
NAVAL_PATROL_PLANES_PER_SHIP_ESCORTING:
  def: '10.0'
  type: float
  cmt: Amount of naval patrol planes per ship on a convoy escort mission
NAVAL_FIGHTERS_PER_PLANE:
  def: '1.0'
  type: float
  cmt: Amounts of air superiority planes requested per enemy plane
NAVAL_STRIKE_PLANES_PER_ARMY:
  def: '0'
  type: int
  cmt: Amount of planes requested per enemy army
NAVAL_STRIKE_PLANES_PER_SHIP:
  def: '20'
  type: int
  cmt: Amount of bombers requested per enemy ship
PORT_STRIKE_PLANES_PER_SHIP:
  def: '10'
  type: int
  cmt: Amount of bombers request per enemy ship in the port
MINES_SWEEPING_PLANES_PER_MAX_MINES:
  def: '150'
  type: int
  cmt: Amount of air planes request for mines sweeping when there is max amount of mines
    planted by enemy in certain region
MINES_PLANTING_PLANES_PER_MAX_DESIRE:
  def: '100'
  type: int
  cmt: Amount of air planes request for mines planting when there is max desire for it.
MINES_PLANTING_DESIRE_PER_HOME_STATE:
  def: '0.4'
  type: float
  cmt: Scoring for how much do we want to plant naval mines with our air wings if the
    naval region is adjacent to a home state. Multiple adjacent states increases the
    score. Max sum of score is 1.0.
MINES_PLANTING_DESIRE_PER_ENEMY_STATE:
  def: '0.1'
  type: float
  cmt: Scoring for how much do we want to plant naval mines with our air wings if the
    naval region is adjacent to the enemy state. Multiple adjacent states increases the
    score. Max sum of score is 1.0.
MINES_PLANTING_DESIRE_PER_NAVAL_THREAT:
  def: '250'
  type: int
  cmt: How much threat must be generated in the naval region, in order to get the
    maximum desire to plant naval mines in there.
NAVAL_MIN_EXCORT_PLANES:
  def: '0'
  type: int
  cmt: Min amount of planes requested to excort operations
DEMOCRATIC_AI_FACTION_KICKING_PLAYER_THREAT_DIFFERENCE:
  def: '6.0'
  type: float
  cmt: World threat generation difference needed to kick a player from a democratic
    faction
BEFRIEND_FACTOR_FOR_KICKING_COUNTRIES:
  def: '7.5'
  type: float
  cmt: World threat difference addition per 100 befriend against a country, democratic
    leaders will forgive allies if they are befriending them
LAND_DEFENSE_AIR_SUPERIORITY_IMPORTANCE:
  def: '1.0'
  type: float
  cmt: Strategic importance of air superiority ( amount of enemy planes in area )
LAND_DEFENSE_CIVIL_FACTORY_IMPORTANCE:
  def: '50'
  type: int
  cmt: Strategic importance of civil factories
LAND_DEFENSE_MILITARY_FACTORY_IMPORTANCE:
  def: '70'
  type: int
  cmt: Strategic importance of military factories
LAND_DEFENSE_NAVAL_FACTORY_IMPORTANCE:
  def: '30'
  type: int
  cmt: Strategic importance of naval factories
LAND_DEFENSE_SUPPLY_HUB_IMPORTANCE:
  def: '4'
  type: int
  cmt: Strategic importance of supply hubs
LAND_DEFENSE_AA_IMPORTANCE_FACTOR:
  def: '1.0'
  type: float
  cmt: Factor of AA influence on strategic importance ( 0.0 - 1.0 )
LAND_DEFENSE_INFRA_IMPORTANCE_FACTOR:
  def: '0.5'
  type: float
  cmt: Factor of infrastructure influence on strategic importance ( 0.0 - 1.0 )
LAND_DEFENSE_IMPORTANCE_SCALE:
  def: '3.0'
  type: float
  cmt: Lend defence total importance scale (every land defence score get's multiplied by
    it)
NUM_HOURS_SINCE_LAST_COMBAT_TO_SUPPORT_UNITS_VIA_AIR:
  def: '72'
  type: int
  cmt: units will be considered in combat if they are just out of their last combat for
    air supporting
LAND_DEFENSE_MIN_FACTORIES_FOR_AIR_IMPORTANCE:
  def: '5'
  type: int
  cmt: If amount of factories is less importance of factories won't apply
LAND_DEFENSE_RAID_IMPORTANCE:
  def: '500'
  type: int
  cmt: Strategic importance of detected raids targetting us
LAND_DEFENSE_FIGHERS_PER_RAID:
  def: '100'
  type: int
  cmt: Amount of air superiority planes requested per detected raid targetting us
LAND_DEFENSE_INTERCEPTORS_PER_RAID:
  def: '100'
  type: int
  cmt: Amount of interceptor planes requested per detected raid targetting us
LAND_DEFENSE_FIGHERS_PER_PLANE:
  def: '1.8'
  type: float
  cmt: Amount of air superiority planes requested per enemy plane
LAND_DEFENSE_INTERCEPTORS_PER_BOMBERS:
  def: '0.8'
  type: float
  cmt: Amount of interceptor planes requested per enemy bomber
LAND_DEFENSE_INTERCEPTORS_PER_PLANE:
  def: '0.1'
  type: float
  cmt: Amount of interceptor planes requested per enemy plane (non bomber)
LAND_DEFENSE_SAM_MISSILE_IMPORTANCE_FACTOR:
  def: '0.2'
  type: float
  cmt: Importance factor of using sam missiles for regions strategic importance. Higher
    value will increase the usage
LAND_COMBAT_MISSILE_IMPORTANCE_FACTOR:
  def: '1.5'
  type: float
  cmt: Importance factor of using missiles for regions strategic importance. Higher
    value will increase the usage
LAND_COMBAT_AIR_SUPERIORITY_IMPORTANCE:
  def: '0.40'
  type: float
  cmt: Strategic importance of air superiority ( amount of enemy planes in area )
LAND_COMBAT_OUR_ARMIES_AIR_IMPORTANCE:
  def: '20'
  type: int
  cmt: Strategic importance of our armies
LAND_COMBAT_OUR_COMBATS_AIR_IMPORTANCE:
  def: '155'
  type: int
  cmt: Strategic importance of our armies in the combats
LAND_COMBAT_FRIEND_ARMIES_AIR_IMPORTANCE:
  def: '10'
  type: int
  cmt: Strategic importance of friendly armies
LAND_COMBAT_FRIEND_COMBATS_AIR_IMPORTANCE:
  def: '8'
  type: int
  cmt: Strategic importance of friendly armies in the combat
LAND_COMBAT_ENEMY_ARMIES_AIR_IMPORTANCE:
  def: '12'
  type: int
  cmt: Strategic importance of our armies
LAND_COMBAT_ENEMY_LAND_FORTS_AIR_IMPORTANCE:
  def: '5'
  type: int
  cmt: Strategic importance of enemy land forts in the region
LAND_COMBAT_ENEMY_COASTAL_FORTS_AIR_IMPORTANCE:
  def: '3'
  type: int
  cmt: Strategic importance of enemy coastal fronts in the region
LAND_COMBAT_IMPORTANCE_SCALE:
  def: '5.0'
  type: float
  cmt: Lend combat total importance scale (every land combat score get's multiplied by
    it)
LAND_COMBAT_FIGHTERS_PER_PLANE:
  def: '1.0'
  type: float
  cmt: Amount of air superiority planes requested per enemy plane
LAND_COMBAT_CAS_PLANES_PER_ENEMY_ARMY_LIMIT:
  def: '200'
  type: int
  cmt: Limit of CAS planes requested by enemy armies
LAND_COMBAT_CAS_PER_ENEMY_ARMY:
  def: '30'
  type: int
  cmt: Amount of CAS planes requested per enemy division
LAND_COMBAT_ANTI_LOGISTICS_PER_ENEMY_ARMY:
  def: '0.1'
  type: float
  cmt: Amount of CAS planes requested per enemy army for anti-logistics
LAND_COMBAT_CAS_PER_COMBAT:
  def: '60'
  type: int
  cmt: Amount of CAS requested per combat
LAND_COMBAT_BOMBERS_PER_LAND_FORT_LEVEL:
  def: '6'
  type: int
  cmt: Amount of bomber planes requested per enemy land fort level
LAND_COMBAT_BOMBERS_PER_COASTAL_FORT_LEVEL:
  def: '6'
  type: int
  cmt: Amount of bomber planes requested per enemy coastal fort level
LAND_COMBAT_MIN_EXCORT_PLANES:
  def: '80'
  type: int
  cmt: Min amount of planes requested to excort operations
LAND_COMBAT_INTERCEPT_PER_PLANE:
  def: '0.25'
  type: float
  cmt: Amount of interception planes requested per enemy plane
MIN_ALLIED_DEFENSE_FACTOR_AIRWING_REQUESTS:
  def: '0.07'
  type: float
  cmt: Airwing requests will be factored by a minimum of this when comparing own vs
    friendly troops in area
AIR_SUPERIORITY_FOR_FRIENDLY_CAS_RATIO:
  def: '0.75'
  type: float
  cmt: Demand at least this proportion of our cas planes as air superiority regardless
    of other needs
LAND_COMBAT_GUIDE_DISTANCE:
  def: '290.0'
  type: float
  cmt: Distance within whch we'll care a bit more about sending planes regardless of
    whether our boiz are dying
ENEMY_PASSING_THROUGH_PLANES_PER_BOMBER:
  def: '0.1'
  type: float
  cmt: Amount of planes we assign to intercept enemies en-route to a location
ENEMY_PASSING_THROUGH_PLANES_PER_FIGHTER:
  def: '0.1'
  type: float
  cmt: Amount of planes we assign to intercept enemies en-route to a location
ENEMY_PASSING_THROUGH_PLANES_PER_SUPPORT:
  def: '0.1'
  type: float
  cmt: Amount of planes we assign to intercept enemies en-route to a location
AI_FRACTION_OF_FIGHTERS_RESERVED_FOR_INTERCEPTION:
  def: '0.25'
  type: float
  cmt: Percentage of fighters we reserve for interception vs AS
MAX_AIR_REGIONS_TO_CARE_ABOUT:
  def: '6'
  type: int
  cmt: Number of regions we'll consider when trying to split planes a bit. Split is NOT
    equal, just a guide, leftovers still applied elsewhere if needed
ENEMY_PASSING_THROUGH_PLANES_PER_BOMBER_NAVAL_REGION:
  def: '0.15'
  type: float
  cmt: Amount of planes we assign to intercept enemies en-route to a location over a sea
    region
ENEMY_PASSING_THROUGH_PLANES_PER_FIGHTER_NAVAL_REGION:
  def: '0.15'
  type: float
  cmt: Amount of planes we assign to intercept enemies en-route to a location over a sea
    region
ENEMY_PASSING_THROUGH_PLANES_PER_SUPPORT_NAVAL_REGION:
  def: '0.15'
  type: float
  cmt: Amount of planes we assign to intercept enemies en-route to a location over a sea
    region
NAVAL_DEFENSE_INTERCEPTION_IMPORTANCE_FACTOR:
  def: '30'
  type: int
  cmt: Factor on added planes passing through region to strategic importance
XP_RATIO_REQUIRED_TO_RESEARCH_WITH_XP:
  def: '2.0'
  type: float
  cmt: AI will at least need this amount of xp compared to cost of a tech to reserch it
    with XP
RESEARCH_WITH_XP_AI_WEIGHT_MULT:
  def: '1.2'
  type: float
  cmt: AI will bump score of a research with this mult if it can use XP
STR_BOMB_AIR_SUPERIORITY_IMPORTANCE:
  def: '0.10'
  type: float
  cmt: Strategic importance of air superiority ( amount of enemy planes in area )
STR_BOMB_CIVIL_FACTORY_IMPORTANCE:
  def: '50'
  type: int
  cmt: Strategic importance of enemy civil factories
STR_BOMB_MILITARY_FACTORY_IMPORTANCE:
  def: '70'
  type: int
  cmt: Strategic importance of enemy military factories
STR_BOMB_NAVAL_FACTORY_IMPORTANCE:
  def: '30'
  type: int
  cmt: Strategic importance of enemy naval factories
STR_BOMB_SUPPLY_HUB_IMPORTANCE:
  def: '1'
  type: int
  cmt: Strategic importance of enemy supply hubs
STR_BOMB_AA_IMPORTANCE_FACTOR:
  def: '0.5'
  type: float
  cmt: Factor of AA influence on strategic importance ( 0.0 - 1.0 )
STR_BOMB_INFRA_IMPORTANCE_FACTOR:
  def: '0.25'
  type: float
  cmt: Factor of infrastructure influence on strategic importance ( 0.0 - 1.0 )
STR_BOMB_IMPORTANCE_SCALE:
  def: '1.0'
  type: float
  cmt: str bombing total importance scale (every str bombing score get's multiplied by
    it)
STR_BOMB_MIN_ENEMY_FIGHTERS_IN_AREA:
  def: '2000'
  type: int
  cmt: If amount of enemy fighters is higher than this mission won't perform
STR_BOMB_FIGHTERS_PER_PLANE:
  def: '1.1'
  type: float
  cmt: Amount of air superiority planes requested per enemy plane
STR_BOMB_PLANES_PER_CIV_FACTORY:
  def: '20'
  type: int
  cmt: Amount of planes requested per enemy civ factory
STR_BOMB_PLANES_PER_MIL_FACTORY:
  def: '25'
  type: int
  cmt: Amount of planes requested per enemy military factory
STR_BOMB_PLANES_PER_NAV_FACTORY:
  def: '15'
  type: int
  cmt: Amount of planes requested per enemy naval factory
STR_BOMB_PLANES_PER_SUPPLY_HUB:
  def: '3'
  type: int
  cmt: Amount of planes requested per enemy supply node
STR_BOMB_MIN_EXCORT_PLANES:
  def: '200'
  type: int
  cmt: Min amount of planes requested to excort operations
RECON_PLANES_NAVAL:
  def: '50'
  type: int
  cmt: scale on recon for naval areas
RECON_PLANES_LAND_COMBAT:
  def: '25'
  type: int
  cmt: scale on recon for land combat areas
RECON_PLANES_STRATEGIC:
  def: '50'
  type: int
  cmt: scale on recon for strategic areas
ASSIGN_FRONT_ARMY_SOFT_ATTACK_FACTOR:
  def: '0.1'
  type: float
  cmt: Importance of unit's ARMY_SOFT_ATTACK stat when assigning to a front
ASSIGN_FRONT_ARMY_HARD_ATTACK_FACTOR:
  def: '0.1'
  type: float
  cmt: Importance of unit's ARMY_HARD_ATTACK stat when assigning to a front
ASSIGN_FRONT_ARMY_BREAKTHROUGH_FACTOR:
  def: '0.2'
  type: float
  cmt: Importance of unit's ARMY_BREAKTHROUGH stat when assigning to a front
ASSIGN_DEFENSE_ARMY_DEFENSE_FACTOR:
  def: '3.0'
  type: float
  cmt: Importance of unit's ARMY_DEFENSE stat when assigning to an area defense order
ASSIGN_DEFENSE_ARMY_ENTRENCHMENT_FACTOR:
  def: '2.0'
  type: float
  cmt: Importance of unit's ARMY_ENTRENCHMENT stat when assigning to an area defense
    order
ASSIGN_DEFENSE_TEMPLATE_CLASS_SCORE:
  def: '3.0'
  type: float
  cmt: Importance of unit's AI template class (AREA_DEFENSE, CAVALRY) when assigning to
    an area defense order
ASSIGN_INVASION_AMPHIBIOUS_ATTACK_FACTOR:
  def: '50.0'
  type: float
  cmt: Importance of unit's amphibious attack adjuster when assigning to an invasion
    order
ORDER_ASSIGNMENT_DISTANCE_FACTOR:
  def: '100.0'
  type: float
  cmt: When the AI assigns units to orders, how much should distance be taken into
    account?
REVISITED_PROV_BOOST_FACTOR:
  def: '4'
  type: int
  cmt: When the AI picks units for a front, it prioritises units already nearby.
UNIT_ASSIGNMENT_STATS_IMPORTANCE:
  def: '3.0'
  type: float
  cmt: Stats score for units are multiplied by this when the AI is deciding which front
    they should be assigned to
ASSIGN_FRONT_TERRAIN_ATTACK_FACTOR:
  def: '3.0'
  type: float
  cmt: Importance of unit's terrain adjusted attack stat when assigning to a front
ASSIGN_FRONT_TERRAIN_DEFENSE_FACTOR:
  def: '1.0'
  type: float
  cmt: Importance of unit's terrain adjusted defense stat when assigning to a front
ASSIGN_FRONT_TERRAIN_MOVEMENT_FACTOR:
  def: '2.0'
  type: float
  cmt: Importance of unit's terrain adjusted movement stat when assigning to a front
ASSIGN_DEFENSE_TERRAIN_ATTACK_FACTOR:
  def: '0.5'
  type: float
  cmt: Importance of unit's terrain adjusted attack stat when assigning to an area
    defense order
ASSIGN_DEFENSE_TERRAIN_DEFENSE_FACTOR:
  def: '4.0'
  type: float
  cmt: Importance of unit's terrain adjusted defense stat when assigning to an area
    defense order
ASSIGN_DEFENSE_TERRAIN_MOVEMENT_FACTOR:
  def: '0.5'
  type: float
  cmt: Importance of unit's terrain adjusted movement stat when assigning to an area
    defense order
ASSIGN_MOUNTAINEERS_TO_MOUNTAINS:
  def: '10.0'
  type: float
  cmt: factor for assigning mountaineer divisions to fronts with mountains (proportional
    to how much of that terrain type)
ASSIGN_TANKS_TO_MOUNTAINS:
  def: '-6.0'
  type: float
  cmt: factor for assigning tank divisions to fronts with mountains (proportional to how
    much of that terrain type)
ASSIGN_TANKS_TO_JUNGLE:
  def: '-6.0'
  type: float
  cmt: factor for assigning tank divisions to fronts with jungle (proportional to how
    much of that terrain type)
UNIT_ASSIGNMENT_TERRAIN_IMPORTANCE:
  def: '10.0'
  type: float
  cmt: Terrain score for units are multiplied by this when the AI is deciding which
    front they should be assigned to
ASSIGN_TANKS_TO_WAR_FRONT:
  def: '6.0'
  type: float
  cmt: Scoring factor for assigning divisions with 'role = armor' or
    'front_role_override = offence' to active war fronts
ASSIGN_TANKS_TO_NON_WAR_FRONT:
  def: '0.4'
  type: float
  cmt: Scoring factor for assigning divisions with 'role = armor' or
    'front_role_override = offence' to non-war fronts
REASSIGN_TO_ANOTHER_FRONT_FACTOR:
  def: '0.5'
  type: float
  cmt: Factor for reassigning to another front. 0.0 < X < 1.0 means reluctant, X > 1.0
    means want to.
REASSIGN_TO_ANOTHER_FRONT_IF_IN_COMBAT_FACTOR:
  def: '0.2'
  type: float
  cmt: Factor for reassigning to another front if in combat. 0.0 < X < 1.0 means
    reluctant, X > 1.0 means want to.
ENEMY_FORTIFICATION_FACTOR_FOR_FRONT_REQUESTS:
  def: '2.0'
  type: float
  cmt: front unit request factor at max enemy fortification
ENEMY_FORTIFICATION_FACTOR_FOR_FRONT_REQUESTS_MAX:
  def: '0.7'
  type: float
  cmt: max factor that can be added by enemy fortification
MANPOWER_RATIO_CAREFULNESS_THRESHOLD:
  def: '0.05'
  type: float
  cmt: if manpower ratio (available/used-by-army) is less than this, start being more
    careful with plan execution (i.e. don't throw your men into the meat grinder if
    you're running out of manpower)
PLAN_ACTIVATION_SUPERIORITY_AGGRO:
  def: '1.0'
  type: float
  cmt: How aggressive a country is in activating a plan based on how superiour their
    force is.
WAIT_YEARS_BEFORE_FREER_BUILDING:
  def: '3'
  type: int
  cmt: The AI will skip considering certain buildings during the buildup phase, after
    htese many years it starts building them regardless of threat.
MAX_CARRIER_OVERFILL:
  def: '1.85'
  type: float
  cmt: Carriers will be overfilled to this amount if there are doctrines to justify it
FIELDED_EQUIPMENT_BUFFER_RATIO_FOR_OCCUPATION_AI:
  def: '0.5'
  type: float
  cmt: garrison ai will try to leave this ratio of buffers while assigning laws
FIELDED_MANPOWER_BUFFER_RATIO_FOR_OCCUPATION_AI:
  def: '0.3'
  type: float
  cmt: garrison ai will try to leave this ratio of buffers while assigning laws
IMPORTANT_VICTORY_POINT:
  def: '15'
  type: int
  cmt: during occupation ai will only care so much to ask for extra garrisons if VP
    amount is at least this
DOCKYARDS_PER_NAVAL_DESIRE_EFFECT:
  def: '-20.0'
  type: float
  cmt: Effects how much AI wants to build dockyards based on how navally focused they
    are in general. Recommended range -100.0 to 100.0.
DECISION_PRIORITY_RANDOMIZER:
  def: '0.1'
  type: float
  cmt: random factor that is used while picking decisions. ai is able to pick a lower
    priority decision earler than a higher one if it is within this threshold
DESIGN_COMPANY_SCORE_MULTIPLIER:
  def: '1.25'
  type: float
  cmt: score multiplier for hiring a design company
ARMY_CHIEF_SCORE_MULTIPLIER:
  def: '1.0'
  type: float
  cmt: score multiplier for hiring an army chief
AIR_CHIEF_SCORE_MULTIPLIER:
  def: '1.0'
  type: float
  cmt: score multiplier for hiring an air chief
NAVY_CHIEF_SCORE_MULTIPLIER:
  def: '1.0'
  type: float
  cmt: score multiplier for hiring an navy chief
POLITICAL_ADVISOR_SCORE_MULTIPLIER:
  def: '1.25'
  type: float
  cmt: score multiplier for hiring political advisors
THEORIST_ACCEPTANCE_MULTIPLIER:
  def: '0.7'
  type: float
  cmt: scale the acceptance of hiring a theorist by this number times the amount of non-
    theorists we have, capped at one.
MIN_SCALED_IDEA_WEIGHT_TO_COMPARE_WITH_DECISIONS:
  def: '100'
  type: int
  cmt: idea scores are scaled between these two values while comparing them to decisions
MAX_SCALED_IDEA_WEIGHT_TO_COMPARE_WITH_DECISIONS:
  def: '200'
  type: int
  cmt: idea scores are scaled between these two values while comparing them to decisions
CRITICAL_DECISION_PRIORITY:
  def: '200'
  type: int
  cmt: critical ai score for decisions, ai will be able to pick decisions if it has
    higher prio even if it is not time to pick them (0 to disable)
CRITICAL_IDEA_PRIORITY:
  def: '400'
  type: int
  cmt: critical ai score for ideas, ai will be able to pick ideas if it has higher prio
    even if it is not time to pick them (0 to disable)
MAX_PP_TO_SPEND_ON_LOWER_PRIO_TASKS:
  def: '25'
  type: int
  cmt: max pp cost for ai to allow spend pp on lower prio things while a higher prio
    things are available
MIN_SCORE_FOR_LOWER_PRIO_TASKS:
  def: '100'
  type: int
  cmt: this is a threshold for low prio tasks that will be considered critical
LOW_PRIO_TEMPLATE_BONUS_FOR_GARRISONS:
  def: '1000'
  type: int
  cmt: bonus to make ai more likely to assign low prio units to garrisons
LOW_PRIO_TEMPLATE_PENALTY_FOR_FRONTS:
  def: '500'
  type: int
  cmt: penalty to make ai less likely to assign low prio units to fronts
DEPLOYED_UNIT_MANPOWER_RATIO_TO_BUFFER_WARTIME:
  def: '0.2'
  type: float
  cmt: deployment will try to buffer a ratio of deployed manpower (for reinforcements)
    during war time
DEPLOYED_UNIT_MANPOWER_RATIO_TO_BUFFER_PEACETIME:
  def: '0.1'
  type: float
  cmt: deployment will try to buffer a ratio of deployed manpower (for reinforcements)
    during peace time
MAX_AVAILABLE_MANPOWER_RATIO_TO_BUFFER_WARTIME:
  def: '0.4'
  type: float
  cmt: deployment will try to buffer a ratio of manpower (for reinforcements) during war
    time
MAX_AVAILABLE_MANPOWER_RATIO_TO_BUFFER_PEACETIME:
  def: '0.2'
  type: float
  cmt: deployment will try to buffer a ratio of manpower (for reinforcements) during
    peace time
MANPOWER_RATIO_REQUIRED_TO_PRIO_MOBILIZATION_LAW:
  def: '0.4'
  type: float
  cmt: percentage of manpower in field is desired to be buffered for AI when it has
    upcoming wars or already at war. if it has less manpower, it will prio manpower laws
UPGRADES_DEFICIT_LIMIT_DAYS:
  def: '7'
  type: int
  cmt: Ai will avoid upgrading units in the field to new templates if it takes longer
    than this to fullfill their equipment need
GIE_EXILE_AIR_MANPOWER_USAGE_RATIO:
  def: '0.2'
  type: float
  cmt: AI will not deploy new exile wings when this percentage of available exile
    manpower is already used for wing recruitment.
CARRIER_TASKFORCE_MAX_CARRIER_COUNT:
  def: '4'
  type: int
  cmt: optimum carrier count for carrier taskforces
CAPITAL_TASKFORCE_MAX_CAPITAL_COUNT:
  def: '12'
  type: int
  cmt: optimum capital count for capital taskforces
SCREEN_TASKFORCE_MAX_SHIP_COUNT:
  def: '12'
  type: int
  cmt: optimum screen count for screen taskforces
SUB_TASKFORCE_MAX_SHIP_COUNT:
  def: '16'
  type: int
  cmt: optimum sub count for sub taskforces
MIN_CAPITALS_FOR_CARRIER_TASKFORCE:
  def: '6'
  type: int
  cmt: carrier fleets will at least have this amount of capitals
CAPITALS_TO_CARRIER_RATIO:
  def: '1.5'
  type: float
  cmt: capital to carrier count in carrier taskfoces
SCREENS_TO_CAPITAL_RATIO:
  def: '4.0'
  type: float
  cmt: screens to capital/carrier count in carrier & capital taskforces
MIN_MAIN_SHIP_RATIO:
  def: '0.3'
  type: float
  cmt: if main ship ratio is below this, steal other ships.
MIN_SUPPORT_SHIP_RATIO:
  def: '0.7'
  type: float
  cmt: if support ship ratio is below this, steal other ships.
MIN_MAIN_SHIP_RATIO_TO_REINFORCE:
  def: '0.5'
  type: float
  cmt: the main ships will be tried to reinforce this level.
MIN_SUPPORT_SHIP_RATIO_TO_REINFORCE:
  def: '0.9'
  type: float
  cmt: the support ships will be tried to reinforce this level.
MIN_MAIN_SHIP_TO_SPARE:
  def: '0.7'
  type: float
  cmt: can only steal ships from a task force if their main ship ratio is above this.
MIN_SUPPORT_SHIP_TO_SPARE:
  def: '1.0'
  type: float
  cmt: can only steal ships from a task force if their support ship ratio is above this.
MIN_MAIN_SHIP_RATIO_TO_MERGE:
  def: '0.7'
  type: float
  cmt: try merge task force if main ship ratio is lower than this.
MAX_MAIN_SHIP_RATIO_TO_MERGE:
  def: '1.001'
  type: float
  cmt: if resulting main ship ratio would be at most this, allow merging into this task
    force.
MAIN_SHIP_RATIO_TO_SPLIT:
  def: '1.8'
  type: float
  cmt: if main ship ratio in a task force is larger than this, split it. (If a carrier
    TF wants 4 carriers (see defines above), but it has more than [this * 4] carriers,
    then we try to split the TF.)
MISSION_FLEET_ICONS:
  def:
    - [4]  # HOLD
    - [29]  # PATROL
    - [21]  # STRIKE FORCE
    - [15]  # CONVOY RAIDING
    - [23]  # CONVOY ESCORT
    - [24]  # MINES PLANTING
    - [5]  # MINES SWEEPING
    - [4]  # TRAIN
    - [4]  # RESERVE_FLEET
    - [9]  # NAVAL INVASION SUPPORT
  type: table
MIN_NAVAL_MISSION_PRIO_TO_ASSIGN:
  def:
    - [0]  # HOLD (consumes fuel HOLD_MISSION_MOVEMENT_COST fuel while moving)
    - [200]  # PATROL
    - [200]  # STRIKE FORCE
    - [200]  # CONVOY RAIDING
    - [100]  # CONVOY ESCORT
    - [200]  # MINES PLANTING
    - [100]  # MINES SWEEPING
    - [0]  # TRAIN
    - [0]  # RESERVE_FLEET
    - [100]  # NAVAL INVASION SUPPORT
  type: table
  cmt: priorities for regions to get assigned to a mission
HIGH_PRIO_NAVAL_MISSION_SCORES:
  def:
    - [0]  # HOLD (consumes fuel HOLD_MISSION_MOVEMENT_COST fuel while moving)
    - [100000]  # PATROL
    - [1000]  # STRIKE FORCE
    - [1500]  # CONVOY RAIDING
    - [1000]  # CONVOY ESCORT
    - [-1]  # MINES PLANTING
    - [300]  # MINES SWEEPING
    - [0]  # TRAIN
    - [0]  # RESERVE_FLEET
    - [1000]  # NAVAL INVASION SUPPORT
  type: table
  cmt: priorities for regions to get assigned to a mission
MAX_MISSION_PER_TASKFORCE:
  def:
    - [0]  # HOLD (consumes fuel HOLD_MISSION_MOVEMENT_COST fuel while moving)
    - [1]  # PATROL
    - [4]  # STRIKE FORCE
    - [1.5]  # CONVOY RAIDING
    - [4]  # CONVOY ESCORT
    - [2]  # MINES PLANTING
    - [2]  # MINES SWEEPING
    - [0]  # TRAIN
    - [0]  # RESERVE_FLEET
    - [10]  # NAVAL INVASION SUPPORT
  type: table
  cmt: max mission region/taskforce ratio
MAX_SCREEN_TASKFORCES_FOR_CONVOY_DEFENSE_MIN:
  def: '0.20'
  type: float
  cmt: maximum ratio of all screen-ships forces to be used in convoy defense (increases
    up to max as AI loses convoys).
MAX_SCREEN_TASKFORCES_FOR_CONVOY_DEFENSE_MAX:
  def: '0.70'
  type: float
  cmt: maximum ratio of all screen-ships forces to be used in convoy defense (increases
    up to max as AI loses convoys).
MAX_SCREEN_TASKFORCES_FOR_CONVOY_DEFENSE_MIN_CONVOY_THREAT:
  def: '100'
  type: int
  cmt: AI will increase screen assignment for escort missions as threate increases
MAX_SCREEN_TASKFORCES_FOR_CONVOY_DEFENSE_MAX_CONVOY_THREAT:
  def: '1500'
  type: int
  cmt: AI will increase screen assignment for escort missions as threate increases
MAX_SCREEN_TASKFORCES_FOR_MINE_SWEEPING:
  def: '0.10'
  type: float
  cmt: maximum ratio of screens forces to be used in mine sweeping
MAX_SCREEN_TASKFORCES_FOR_MINE_SWEEPING_PRIO:
  def: '0.8'
  type: float
  cmt: if you have mines near your owned states, you will start priotize mine missions
    and will assign this ratio of screens
MAX_SCREEN_TASKFORCES_FOR_MINE_SWEEPING_PRIO_MIN_MINES:
  def: '10'
  type: int
  cmt: if there are at least this many mines near our owned states, we will prioritize
    mine sweeping
MAX_SCREEN_TASKFORCES_FOR_MINE_SWEEPING_PRIO_MAX_MINES:
  def: '1000'
  type: int
  cmt: if there are this many mines near our owned states, mine sweeping reaches max
    prio
MAX_SCREEN_TASKFORCES_FOR_MINE_LAYING:
  def: '0.10'
  type: float
  cmt: maximum ratio of screens forces to be used in mine laying
MAX_SCREEN_FORCES_FOR_INVASION_SUPPORT:
  def: '0'
  type: int
  cmt: max ratio of screens forces to be used in naval invasion missions
MAX_CAPITAL_FORCES_FOR_INVASION_SUPPORT:
  def: '0'
  type: int
  cmt: max ratio of capital forces to be used in naval invasion missions
MAX_PATROL_TO_STRIKE_FORCE_RATIO:
  def: '4.0'
  type: float
  cmt: maximum patrol/strike force ratio
CONSTRUCTION_PRIO_INFRASTRUCTURE:
  def: '0.20'
  type: float
  cmt: base prio for infrastructure in the construction queue
CONSTRUCTION_PRIO_CIV_FACTORY:
  def: '0.80'
  type: float
  cmt: base prio for civilian factories in the construction queue
CONSTRUCTION_PRIO_MIL_FACTORY:
  def: '0.70'
  type: float
  cmt: base prio for military factories in the construction queue
CONSTRUCTION_PRIO_SUPPLY_BUILDING:
  def: '1.10'
  type: float
  cmt: base prio for supply buildings (supply hubs, ports) in the construction queue
CONSTRUCTION_PRIO_RAILWAY:
  def: '4.00'
  type: float
  cmt: base prio for railways in the construction queue
CONSTRUCTION_PRIO_RAILWAY_GUN_REPAIR:
  def: '15.00'
  type: float
  cmt: base prio for railway gun repairs in the construction queue
CONSTRUCTION_PRIO_UNSPECIFIED:
  def: '0.50'
  type: float
  cmt: base prio for unspecified buildings (none of the categories above) in the
    construction queue
CONSTRUCTION_PRIO_FACTOR_OCCUPIED_TERRITORY:
  def: '1.00'
  type: float
  cmt: factor prio with this if occupied territory
CONSTRUCTION_PRIO_FACTOR_OWNED_NONCORE:
  def: '1.50'
  type: float
  cmt: factor prio with this if owned non-core territory
CONSTRUCTION_PRIO_FACTOR_OWNED_CORE:
  def: '2.00'
  type: float
  cmt: factor prio with this if owned core territory
CONSTRUCTION_PRIO_FACTOR_REPAIRING:
  def: '0.30'
  type: float
  cmt: factor prio with this if building is being repaired
MAX_FACTORY_TO_SPARE_FOR_MISSION_FUEL_TRADE:
  def: '0.12'
  type: float
  cmt: amount of factories to spend on oil trade in case of fuel need for missions
MAX_FACTORY_TO_SPARE_FOR_CRITICAL_MISSION_FUEL_TRADE:
  def: '0.3'
  type: float
  cmt: amount of factories to spend on oil trade in case of fuel need for prio missions
MAX_FACTORY_TO_TRADE_FOR_FUEL:
  def: '0.5'
  type: float
FUEL_TRADE_PRIO_FOR_CONVOY_DEFENSE:
  def: '0.3'
  type: float
  cmt: AI will be less reluctant to cancel convoy missions if it is trading for oil
MAX_FACTORY_TO_SPARE_FOR_MISSION_FUEL_TRADE_IN_PEACE:
  def: '0.03'
  type: float
  cmt: amount of factories to spend on oil trade in case of fuel need for missions in
    peace time
MAX_FACTORY_TO_SPARE_FOR_CRITICAL_MISSION_FUEL_TRADE_IN_PEACE:
  def: '0.1'
  type: float
  cmt: amount of factories to spend on oil trade in case of fuel need for prio missions
    in peace time
MAX_FACTORY_TO_TRADE_FOR_FUEL_IN_PEACE:
  def: '0.15'
  type: float
FUEL_REQUEST_RATIO_FOR_COMBATS:
  def: '0.6'
  type: float
  cmt: ratio of ship combat fuel cost that is to be considered in fuel usage and request
    system
PRIO_FUEL_REQUEST_RATIO_FOR_COMBATS:
  def: '0.8'
  type: float
  cmt: ratio of ship combat fuel cost that is to be considered in prio fuel usage and
    request system
FUEL_REQUEST_RATIO_FOR_MOVEMENT:
  def: '0.4'
  type: float
  cmt: ratio of ship movement fuel cost that is to be considered in fuel usage and
    request system
PRIO_FUEL_REQUEST_RATIO_FOR_MOVEMENT:
  def: '0.2'
  type: float
  cmt: ratio of ship movement fuel cost that is to be considered in prio fuel usage and
    request system
NAVY_ACTUAL_FUEL_USAGE_WEIGHT_ON_OIL_REQUEST:
  def: '0.5'
  type: float
  cmt: weight of actual fuel usage of ships compared to what is being asked for missions
    while calculating oil needed for trade
AIR_ACTUAL_FUEL_USAGE_WEIGHT_ON_OIL_REQUEST:
  def: '0.5'
  type: float
  cmt: weight of actual fuel usage of planes compared to what is being asked for
    missions while calculating oil needed for trade
MONTHS_TO_FILL_FUEL_BUFFER_WITH_OIL_REQUESTS:
  def: '6.0'
  type: float
  cmt: in war time, coutries will try to fill their buffer in this duration and trade
    for oil if necesarry
MONTHS_TO_FILL_FUEL_BUFFER_WITH_OIL_REQUESTS_IN_PEACE_TIME:
  def: '10.0'
  type: float
  cmt: in peace time, coutries will try to fill their buffer in this duration and trade
    for oil if necesarry
FUEL_CONSUMPTION_MULT_FOR_FUEL_SAVING_MODE:
  def: '0.25'
  type: float
  cmt: fuel consumptions will be limited by this ratio in fuel saving mode
FUEL_CONSUMPTION_MULT_REGULAR_FUEL_MODE:
  def: '1.0'
  type: float
  cmt: fuel consumptions will be limited by this ratio in regular fuel mode
FUEL_CONSUMPTION_MULT_AGRESSIVE_FUEL_MODE:
  def: '3.0'
  type: float
  cmt: fuel consumptions will be limited by this ratio in aggressive fuel usage mode
DAYS_FUEL_REMAINING_TO_ENTER_FUEL_SAVING_MODE:
  def: '30'
  type: int
  cmt: countries will enter fuel saving mode if they will be out of fuel in this number
    of days and their fuel ratio is below next define
DAYS_FUEL_REMAINING_TO_ENTER_FUEL_SAVING_MODE_FUEL_RATIO:
  def: '0.4'
  type: float
FUEL_RATIO_TO_EXIST_FUEL_SAVING_MODE:
  def: '0.60'
  type: float
  cmt: countries will exit fuel saving mode if they have more fuel ratio than this
WANTED_MAX_FUEL_BUFFER_IN_DAYS_FOR_ARMY_MAX_CONSUMPTION:
  def: '60'
  type: int
  cmt: AI will try to buffer at least this amount of days on max consumption, will trade
    if necesarry and will go into fuel saving mode/aggresive mode using this buffer
WANTED_MAX_FUEL_BUFFER_IN_DAYS_FOR_AIR_MAX_CONSUMPTION:
  def: '60'
  type: int
  cmt: AI will try to buffer at least this amount of days on max consumption, will trade
    if necesarry and will go into fuel saving mode/aggresive mode using this buffer
WANTED_MAX_FUEL_BUFFER_IN_DAYS_FOR_NAVY_MAX_CONSUMPTION:
  def: '60'
  type: int
  cmt: AI will try to buffer at least this amount of days on max consumption, will trade
    if necesarry and will go into fuel saving mode/aggresive mode using this buffer
MIN_WANTED_MAX_FUEL:
  def: '50'
  type: int
  cmt: minimum value for wanted fuel buffers for AI (in thousands)
GIE_LEND_LEASE_TO_PLAYER_EXILE_DESIRE_BONUS:
  def: '40'
  type: int
  cmt: AI host is more likely to accept lend lease requests from a player.
NAVAL_BASE_RATIO_ALLOCATED_FOR_REPAIRS:
  def: '0.25'
  type: float
  cmt: ai will allocate at most this ratio of dockyards for repairs in peace time
NAVAL_BASE_RATIO_ALLOCATED_FOR_REPAIRS_IN_WAR_TIME:
  def: '0.6'
  type: float
  cmt: ai will allocate at most this ratio of dockyards for repairs in war time
MAX_FUEL_CONSUMPTION_RATIO_FOR_AIR_TRAINING:
  def: '0.20'
  type: float
  cmt: ai will use at most this ratio of affordable fuel for air training
MAX_FUEL_CONSUMPTION_RATIO_FOR_NAVY_TRAINING:
  def: '0.20'
  type: float
  cmt: ai will use at most this ratio of affordable fuel for naval training
MAX_FULLY_TRAINED_SHIP_RATIO_FOR_TRAINING:
  def: '0.7'
  type: float
  cmt: ai will not train a taskforce if fully trained ships are above this ratio
NUM_SILOS_PER_CIVILIAN_FACTORIES:
  def: '0.0025'
  type: float
  cmt: ai will try to build a silo per this ratio of civ factories
NUM_SILOS_PER_MILITARY_FACTORIES:
  def: '0.012'
  type: float
  cmt: ai will try to build a silo per this ratio of mil factories
NUM_SILOS_PER_DOCKYARDS:
  def: '0.02'
  type: float
  cmt: ai will try to build a silo per this ratio of dockyards
SHIP_STR_RATIO_PUT_ON_REPAIRS:
  def: '0.8'
  type: float
  cmt: if ships are damaged below this ratio, they are put for repairs
SHIP_STR_RATIO_EXIT_REPAIRS:
  def: '1.00'
  type: float
  cmt: the ships will leave repairs if they are >= this ratio of total str
REPAIR_TASKFORCE_SIZE:
  def: '4'
  type: int
  cmt: repair taskforce sizes are limited to this many ships
PLAN_VALUE_BONUS_FOR_MOVING_UNITS:
  def: '0.35'
  type: float
  cmt: AI plans gets a bonus when units are not moving and ready to fight
AGGRESSIVENESS_BONUS_FOR_FRONTS_THAT_ARE_ON_HIGH_AGGRESSIVENESS:
  def: '-0.4'
  type: float
  cmt: AI gets a bonus to aggresiveness if it is already executing an aggressive plan
    (lower is more aggressive)
AGGRESSIVENESS_CHECK_BASE:
  def: '1.5'
  type: float
  cmt: front comparison where ai will consider aggressive stance, unless it is already
    then the number above is used
AGGRESSIVENESS_CHECK_EASY_TARGET:
  def: '-0.3'
  type: float
  cmt: if target nation is flagged as easy target we also adjust down the front
    comparison needed
AGGRESSIVENESS_CHECK_CAREFUL:
  def: '0.6'
  type: float
  cmt: at what front strength balance do we go careful
AGGRESSIVENESS_CHECK_PARTLY_FORTIFIED:
  def: '2.0'
  type: float
  cmt: if front strength balance is at or above this value versus a party fortified
    enemy, we do a balanced attack
AGGRESSIVENESS_CHECK_PARTLY_FORTIFIED_WEAK_POINTS:
  def: '0.75'
  type: float
  cmt: if front strength balance is at or above this value versus a party fortified
    enemy, we rush attack weak points; below this value, we are careful
AGGRESSIVENESS_CHECK_FULLY_FORTIFIED:
  def: '10'
  type: int
  cmt: if front strength balance is at or above this value versus a fully fortified
    enemy with no weak points, we do a balanced attack instead being careful
AGGRESSIVENESS_CHECK_FULLY_FORTIFIED_POCKET:
  def: '6'
  type: int
  cmt: if front strength balance is at or above this value versus a fully fortified
    enemy in a pocket, we do a balanced attack instead being careful
FRONT_EVAL_UNIT_ACCURACY:
  def: '1.0'
  type: float
  cmt: scale how stupid ai will act on fronts. 0 is potato
FRONT_EVAL_UNIT_AIR_SUP_IMPACT:
  def: '1.0'
  type: float
  cmt: scale how good the AI thinks air superiority is for units
FRONT_EVAL_UNIT_SUPPLY_AND_ORG_LACK_IMPACT:
  def: '1.0'
  type: float
  cmt: scale how painful the AI thinks a combined lack of supply and organization is for
    units
FRONT_EVAL_PERCENT_TO_ASSIST_ALLY_FRONT:
  def: '0.5'
  type: float
  cmt: percentage of how many units the AI thinks it should have compared to an ally
    before considering sending units
PRODUCTION_CARRIER_PLANE_BUFFER_RATIO:
  def: '1.5'
  type: float
  cmt: in addition to total deck size of carriers, we want at least this ratio to buffer
    it
PRODUCTION_CARRIER_PLANE_PRODUCTION_BOOST_TO_BUFFER:
  def: '4.0'
  type: float
  cmt: production of carrier planes will go up by this ratio if we lack buffers
NAVAL_MAX_CONVOY_TO_INTEL_FOR_CONVOY_RAIDS:
  def: '200'
  type: int
  cmt: number of convoys in region will be clamped to this max, anything more will be
    ignored while assigning raids
EXTRA_NAVY_INTEL_FOR_CONVOY_RAIDING:
  def: '0.0'
  type: float
  cmt: this amount of intel is added to navy intel while ai is assigning convoy raiding
    mission
INTEL_NEEDED_TO_NEGATVE_CONVOY_COUNT_REDUCTION:
  def: '80.0'
  type: float
  cmt: navy intel is divided by this ratio to negate
    NAVAL_CONVOY_COUNT_INTEL_DROPOFF_DUE_TO_LOW_DECYPTION
NAVAL_CONVOY_COUNT_INTEL_DROPOFF_DUE_TO_LOW_DECYPTION:
  def: '200'
  type: int
  cmt: on lowest navy intel, ai won't be able to see enemy convoys lower than this ratio
CONVOY_RAID_SCORE_FROM_CONVOY_INTELLIGENCE:
  def: '2.5'
  type: float
  cmt: each convoy intelligenge will incease raid score by this
AIR_AI_ENEMY_PROV_RATIO_FOR_COMBAT_REGION:
  def: '0.15'
  type: float
  cmt: if a region has more than this ratio of provinces controlled by enemy, AI will
    consider it as a combat zone while assigning planes
RESEARCH_MULTI_DOCTRINE_SCORE:
  def: '0.3'
  type: float
  cmt: score penalty to researchign multiple doctrines at once for AI
CONVOY_ESCORT_SCORE_FROM_CONVOYS:
  def: '15'
  type: int
  cmt: score for each convoy you have in area
CONVOY_ESCORT_MUL_FROM_NO_CONVOYS:
  def: '0.02'
  type: float
  cmt: score multiplier when no convoys are around
CONVOY_RAID_MIN_ENEMY_THREAT:
  def: '0.05'
  type: float
RAILWAY_GUN_PRODUCTION_BASE_DIVISIONS_RATIO_PERCENT:
  def: '0'
  type: int
  cmt: Base ratio of desired railway guns to divisions for AI (5 means 5%). Can be
    modified by railway_guns_divisions_ratio AI strategy value
RAILWAY_GUN_PRODUCTION_MIN_DIVISONS:
  def: '20'
  type: int
  cmt: Minimum required number of divisions for the AI to consider producing railway
    guns
RAILWAY_GUN_PRODUCTION_MIN_FACTORIES:
  def: '10'
  type: int
  cmt: Minimum required number of military factories for the AI to consider producing
    railway guns
RAILWAY_GUN_PER_ARMY_CAP:
  def: '5'
  type: int
  cmt: Maximum railway guns assigned to one army for the AI
RAILWAY_GUN_ASSIGNMENT_SCORE_UNITCOUNT_MULTIPLIER:
  def: '10.0'
  type: float
  cmt: Score multiplier for favoring orders groups with more units when assigning
    railway guns
RAILWAY_GUN_ASSIGNMENT_SCORE_HOLD:
  def: '20'
  type: int
  cmt: Score for keeping current assignment when assigning railway guns
MAX_UNIT_RATIO_FOR_INVASIONS:
  def: '0.4'
  type: float
  cmt: countries won't use armies more than this ratio of total units for invasions
MIN_UNIT_RATIO_FOR_INVASIONS:
  def: '0.1'
  type: float
  cmt: don't allocate more divisions than this for naval invasions
MAX_INVASION_FRONT_SCORE:
  def: '1000'
  type: int
  cmt: max score for naval invasion front scores
MIN_FRONT_SCORE_FOR_AFTER_INVASION_AREAS:
  def: '1500'
  type: int
  cmt: min score for army fronts that are created on recently invaded regions
MIN_CONVOY_EFFICIENCY_TO_CANCEL_TRADES:
  def: '0.4'
  type: float
  cmt: min efficiency (due to convoy raid) to cancel trades
MIN_CONVOY_EFFICIENCY_TO_START_TRADES:
  def: '0.6'
  type: float
  cmt: min efficiency (due to convoy raid) to start be able to trades
MIN_CONVOY_EFFICIENCY_PER_WAR_SUPPORT_HIT:
  def: '0.6'
  type: float
  cmt: percentage of warsupport hit you get is multiplied by this value and added to min
    convoy efficiencies
NAVAL_INVADED_AREA_PRIO_DURATION:
  def: '90'
  type: int
  cmt: after successful invasion, AI will prio the enemy area for this number of days
NAVAL_INVADED_AREA_PRIO_MULT:
  def: '1.2'
  type: float
  cmt: fronts that belongs to recent invasions gets more prio
MIN_NUM_CONQUERED_PROVINCES_TO_DEPRIO_NAVAL_INVADED_FRONTS:
  def: '20'
  type: int
  cmt: if you conquer this amount of provinces after a naval invasion, it will lose its
    prio status and will act as a regular front
INVASION_TARGET_DISTANCE_DENOMINATOR:
  def: '1000'
  type: int
  cmt: When selecting invasion target, divide this with (pixel) distance to get distance
    score factor. (Doesn't really affect the relative scoring, but it affects the
    linearity of the score function.)
INVASION_TARGET_NO_PORT_FACTOR:
  def: '0.3'
  type: float
  cmt: When selecting invasion target, multiply score with this if the target has no
    port
INVASION_TARGET_TRUNCATION_SELECT_THRESHOLD:
  def: '0.6'
  type: float
  cmt: When selecting invasion target, use this threshold for truncation selection. (1.0
    means select highest scored target, 0.0 means select randomly from all possible
    target, 0.5 means select randomly from all targets with more than 50 % of highest
    score)
INVASION_TARGET_PRIO_NOT_ENEMY_FACTOR:
  def: '0.17'
  type: float
  cmt: When calculating priority for an invasion, factor the score with this if the
    target is not an actual enemy.
FAILED_INVASION_AVOID_DURATION:
  def: '60'
  type: int
  cmt: after a failed invasion, AI will down-prioritize invading the same area again for
    this number of days
FAILED_INVASION_AREA_PRIO_FACTOR:
  def: '0.5'
  type: float
  cmt: for every failed invasion on an area, factor that area's invasion prio with this
    value
FAILED_INVASION_PORT_PRIO_FACTOR:
  def: '0.66'
  type: float
  cmt: for every failed invasion on a target port (province), factor the chance that we
    try to invade that same port again (relative to other ports)
BUILDING_TARGETS_BUILDING_PRIORITIES:
  def:
    - ['industrial_complex']
  type: table
  cmt: buildings in order of pirority when considering building targets strategies.
    First has the greatest priority, omitted has the lowest. NOTE: not all buildings are
    supported by building targets strategies.
MIN_INVASION_PLAN_VALUE_TO_EXECUTE:
  def: '0.3'
  type: float
  cmt: ai will only activate invasions if plan value is above this
MIN_INVASION_ORG_FACTOR_TO_EXECUTE:
  def: '0.9'
  type: float
  cmt: ai will only activate invasions if average org factor is above this
MIN_INVASION_UNITS_READY_TO_EXECUTE:
  def: '0.9'
  type: float
  cmt: ai will only activate invasions if this ratio of assigned units are ready
MAX_INVASION_SIZE:
  def: '24'
  type: int
  cmt: max invasion group size
MAX_PORT_STRIKE_HISTORY_TO_REMEMBER:
  def: '5000'
  type: int
  cmt: maximum port strike history to keep track (will be used to disable ports
PORT_STRIKE_HISTORY_DECAY_MIN:
  def: '10'
  type: int
  cmt: minimum decay for port strike history (<7 days since last port strike)
PORT_STRIKE_HISTORY_DECAY_MAX:
  def: '400'
  type: int
  cmt: maximum decay for port strike history (>=37 days since last port strike)
MAX_PORT_RATIO_TO_DISABLE:
  def: '0.8'
  type: float
  cmt: max ratio of ports to disable due to port strikes
PORT_STRIKE_HISTORY_VALUE_TO_DISABLE_REPAIRS:
  def: '200'
  type: int
  cmt: cut off for disabling ports above this threshold
PORT_STRIKE_HISTORY_VALUE_TO_REENABLE_REPAIRS:
  def: '10'
  type: int
  cmt: cut off for reenabling ports bloew this threshold
CURRENT_LAW_SCORE_BONUS:
  def: '50.0'
  type: float
  cmt: current score will get an additional bonus to its ai weight
OIL_WANT_PER_POTENTIAL_LAND_CONSUMPTION_K:
  def: '0.05'
  type: float
  cmt: how much extra oil requested on top of balance for country's potential oil
    consumptions
OIL_WANT_PER_POTENTIAL_NAVY_CONSUMPTION_K:
  def: '0.03'
  type: float
OIL_WANT_PER_POTENTIAL_AIR_CONSUMPTION_K:
  def: '0.03'
  type: float
OIL_WANT_PER_POTENTIAL_MISC_CONSUMPTION_K:
  def: '0.1'
  type: float
OIL_WANT_AT_PEACE_PER_POTENTIAL_LAND_CONSUMPTION_K:
  def: '0.02'
  type: float
OIL_WANT_AT_PEACE_PER_POTENTIAL_NAVY_CONSUMPTION_K:
  def: '0.0'
  type: float
OIL_WANT_AT_PEACE_PER_POTENTIAL_AIR_CONSUMPTION_K:
  def: '0.0'
  type: float
OIL_WANT_AT_PEACE_PER_POTENTIAL_MISC_CONSUMPTION_K:
  def: '0.1'
  type: float
RESOURCE_WANT_PER_MISSING_BALANCE:
  def: '0.2'
  type: float
  cmt: negative balance increases the desire on a resource
RESOURCE_WANT_PER_CONSUMED:
  def: '0.05'
  type: float
  cmt: if resource is being used in production, increase the desire
CRYPTO_ACTIVATION_THRESHOLD:
  def: '1.25'
  type: float
  cmt: will multiply crypto activation threshold. larger
CRYPTO_ACTIVATE_NUM_DAYS_DROP_OFF:
  def: '0.4'
  type: float
  cmt: longer decrypted crypto waits, lower threshold it will have. threshold will be
    multiplied by this value at most
CRYPTO_ACTIVATE_NUM_DAYS_DECAY:
  def: '60'
  type: int
  cmt: at this number of days, it will decay by %50 of prev define
CRYPTO_ACTIVATE_NUM_ACTIVATED_DROP_OFF:
  def: '0.6'
  type: float
  cmt: having an already activated cryptos will further multiply threshold, down to this
    value
CRYPTO_ACTIVATION_SCORE_ARMIES_IN_COMBAT_BONUS:
  def: '0.2'
  type: float
  cmt: having units in combat will increase the score by this ratio
CRYPTO_ACTIVATION_SCORE_OUR_CAPITAL_BONUS:
  def: '0.2'
  type: float
  cmt: fronts of our capital get a bonus by this ratio
CRYPTO_ACTIVATION_SCORE_ENEMY_CAPITAL_BONUS:
  def: '0.2'
  type: float
  cmt: fronts of enemy capital get a bonus by this ratio
CRYPTO_AFTER_SCORE_INVASION_FRONT_BONUS:
  def: '1.0'
  type: float
  cmt: a front that is naval invading will increase the score by this ratio
MAX_MODULAR_EQUIPMENT_EQUIPMENT_UPGRADE_COUNT_PER_PASS:
  def: '4'
  type: int
  cmt: the maximum number of level AI will try to add to an equipment upgrade of an
    equipment defined in common/ai_equipment in one pass
EQUIPMENT_UPGRADE_VARIANT_MATCH_SCORE_FACTOR:
  def: '0.2'
  type: float
  cmt: the weight of equipment upgrade level when computing the match score of a variant
    to an ai equipment design.
AI_UPDATE_ROLES_FREQUENCY_HOURS:
  def: '48;'
  type: string
  cmt: Update the roles for a country AI this often (affects performance)
UPDATE_SUPPLY_BOTTLENECKS_FREQUENCY_HOURS:
  def: '168;'
  type: string
  cmt: Check for and try to fix supply bottlenecks this often. (168 hours = 1 week)
FIX_SUPPLY_BOTTLENECK_SATURATION_THRESHOLD:
  def: '0.85;'
  type: string
  cmt: Try to fix supply bottlenecks if supply node saturation exceeds this value.
UPDATE_SUPPLY_MOTORIZATION_FREQUENCY_HOURS:
  def: '52;'
  type: string
  cmt: Check if activating motorization would improve supply situation this often.
AI_PREFERRED_TACTIC_WEEKLY_CHANGE_CHANCE:
  def: '0.05'
  type: float
  cmt: Chance for AI to select a new preferred tactic if they don't have one selected
ARMY_LEADER_ASSIGN_KEEP_CURRENT_LEADER_FACTOR:
  def: '1.2'
  type: float
  cmt: Boosts the score for keeping the current leader. Value > 1.0 favors the current
    leader.
ARMY_LEADER_ASSIGN_DONT_STEAL_OTHER_FACTOR:
  def: '0.75'
  type: float
  cmt: Reduces the score for leaders assigned elsewhere. Value < 1.0 discourages
    reassigning these leaders.
ARMY_LEADER_ASSIGN_FIELD_MARSHAL_TO_ARMY:
  def: '-500'
  type: int
  cmt: Score for assigning a field marshal to a normal army (want to use them for army
    groups)
ARMY_LEADER_ASSIGN_EMPTYNESS_MALUS:
  def: '0.2'
  type: float
  cmt: Factor for avoiding assigning leaders that can lead large armies to small armies
    (a value of 0.2 reduces the score by max 20 %)
ARMY_LEADER_ASSIGN_OVERCAPACITY:
  def: '-200'
  type: int
  cmt: Score for assigning leader to a too large army
ARMY_LEADER_ASSIGN_OVERALL_SKILL_FACTOR:
  def: '50'
  type: int
  cmt: This times general's overall skill is added to score
ARMY_LEADER_ASSIGN_DEFENSE_OVERALL_SKILL_FACTOR:
  def: '10'
  type: int
  cmt: If defensive army, this times general's overall skill is added to score
ARMY_LEADER_ASSIGN_DEFENSE_ATTACK_SKILL_FACTOR:
  def: '3'
  type: int
  cmt: If defensive army, this times general's attack skill is added to score
ARMY_LEADER_ASSIGN_DEFENSE_DEFENSE_SKILL_FACTOR:
  def: '20'
  type: int
  cmt: If defensive army, this times general's defense skill is added to score
ARMY_LEADER_ASSIGN_DEFENSE_LOGISTICS_SKILL_FACTOR:
  def: '3'
  type: int
  cmt: If defensive army, this times general's logistics skill is added to score
ARMY_LEADER_ASSIGN_DEFENSE_PLANNING_SKILL_FACTOR:
  def: '3'
  type: int
  cmt: If defensive army, this times general's planning skill is added to score
ARMY_LEADER_ASSIGN_INVASION_ATTACK_SKILL_FACTOR:
  def: '10'
  type: int
  cmt: If invasion army, this times general's attack skill is added to score
ARMY_LEADER_ASSIGN_INVASION_DEFENSE_SKILL_FACTOR:
  def: '10'
  type: int
  cmt: If invasion army, this times general's defense skill is added to score
ARMY_LEADER_ASSIGN_INVASION_LOGISTICS_SKILL_FACTOR:
  def: '20'
  type: int
  cmt: If invasion army, this times general's logistics skill is added to score
ARMY_LEADER_ASSIGN_INVASION_PLANNING_SKILL_FACTOR:
  def: '20'
  type: int
  cmt: If invasion army, this times general's planning skill is added to score
ARMY_LEADER_ASSIGN_ATTACK_SKILL_FACTOR:
  def: '20'
  type: int
  cmt: This times general's attack skill is added to score
ARMY_LEADER_ASSIGN_DEFENSE_SKILL_FACTOR:
  def: '10'
  type: int
  cmt: This times general's defense skill is added to score
ARMY_LEADER_ASSIGN_LOGISTICS_SKILL_FACTOR:
  def: '7'
  type: int
  cmt: This times general's logistics skill is added to score
ARMY_LEADER_ASSIGN_PLANNING_SKILL_FACTOR:
  def: '7'
  type: int
  cmt: This times general's planning skill is added to score
ARMY_LEADER_ASSIGN_NR_TRAITS:
  def: '5'
  type: int
  cmt: This times general's nr of active traits is added to score
ARMY_LEADER_ASSIGN_EXILED_LEADS_EXILED_TROOPS:
  def: '10'
  type: int
  cmt: If exiled leader, increase chance of leading army with exiled troops
ARMY_LEADER_ASSIGN_EXILED_LEADS_OWN_EXILED_TROOPS:
  def: '100'
  type: int
  cmt: If exiled leader, increase chance of leading army with exiled troops from same
    country as the leader
ARMY_LEADER_ASSIGN_DEFENSE_MAX_DIG_IN_FACTOR:
  def: '1.0'
  type: float
  cmt: If defensive army, importance of general's MAX_DIG_IN_FACTOR modifier
ARMY_LEADER_ASSIGN_DEFENSE_ARMY_ARMOR_DEFENCE_FACTOR:
  def: '1.0'
  type: float
  cmt: If defensive army, importance of general's ARMY_ARMOR_DEFENCE_FACTOR modifier
    (proportional to armor ratio in the army)
ARMY_LEADER_ASSIGN_PLANNING_SPEED:
  def: '0.1'
  type: float
  cmt: Importance of general's PLANNING_SPEED modifier
ARMY_LEADER_ASSIGN_MAX_PLANNING:
  def: '0.1'
  type: float
  cmt: Importance of general's MAX_PLANNING modifier
ARMY_LEADER_ASSIGN_RECON_FACTOR:
  def: '2.0'
  type: float
  cmt: Importance of general's RECON_FACTOR modifier
ARMY_LEADER_ASSIGN_OUT_OF_SUPPLY_FACTOR:
  def: '1.0'
  type: float
  cmt: Importance of general's OUT_OF_SUPPLY_FACTOR modifier
ARMY_LEADER_ASSIGN_WINTER_ATTRITION_FACTOR:
  def: '1.0'
  type: float
  cmt: Importance of general's WINTER_ATTRITION_FACTOR modifier
ARMY_LEADER_ASSIGN_ARMY_ARMOR_SPEED_FACTOR:
  def: '20.0'
  type: float
  cmt: Importance of general's ARMY_ARMOR_SPEED_FACTOR modifier (proportional to armor
    ratio in the army)
ARMY_LEADER_ASSIGN_ARMY_ARMOR_ATTACK_FACTOR:
  def: '20.0'
  type: float
  cmt: Importance of general's ARMY_ARMOR_ATTACK_FACTOR modifier (proportional to armor
    ratio in the army)
ARMY_LEADER_ASSIGN_BOOST_ARMOR_SKILL:
  def: '20.0'
  type: float
  cmt: Importance of general's trait where armor skill is boosted, e.g. armor_officer
    which boosts panzer_leader (proportional to armor ratio in the army)
ARMY_LEADER_ASSIGN_ARMOR_LEADER_IF_NO_ARMOR:
  def: '-0.5'
  type: float
  cmt: Avoid assigning a general with armor skills to an army with no armor (can be
    negative)
ARMY_LEADER_ASSIGN_AMPHIBIOUS_INVASION:
  def: '1.0'
  type: float
  cmt: If involved in invasion, importance of general's AMPHIBIOUS_INVASION modifier
ARMY_LEADER_ASSIGN_NAVAL_INVASION_PREPARATION:
  def: '1.0'
  type: float
  cmt: If involved in invasion, importance of general's NAVAL_INVASION_PREPARATION
    modifier
ARMY_LEADER_ASSIGN_XP_GAIN_FACTOR:
  def: '2.0'
  type: float
  cmt: Importance of general's XP_GAIN_FACTOR modifier
ARMY_LEADER_ASSIGN_SUPPLY_CONSUMPTION_FACTOR:
  def: '1.0'
  type: float
  cmt: Importance of general's SUPPLY_CONSUMPTION_FACTOR modifier
ARMY_LEADER_ASSIGN_LAND_REINFORCE_RATE:
  def: '1.0'
  type: float
  cmt: Importance of general's LAND_REINFORCE_RATE modifier
ARMY_LEADER_ASSIGN_ARMY_MORALE_FACTOR:
  def: '1.0'
  type: float
  cmt: Importance of general's ARMY_MORALE_FACTOR modifier
ARMY_LEADER_ASSIGN_TERRAIN_FACTOR:
  def: '0.2'
  type: float
  cmt: Importance of general's terrain skills
AREA_DEFENSE_SETTING_VP:
  def: 'false'
  type: bool
AREA_DEFENSE_SETTING_PORTS:
  def: 'true'
  type: bool
AREA_DEFENSE_SETTING_AIRBASES:
  def: 'false'
  type: bool
AREA_DEFENSE_SETTING_BORDERS:
  def: 'false'
  type: bool
AREA_DEFENSE_SETTING_FORTS:
  def: 'false'
  type: bool
AREA_DEFENSE_SETTING_COASTLINES:
  def: 'true'
  type: bool
AREA_DEFENSE_SETTING_RAILWAYS:
  def: 'false'
  type: bool
AREA_DEFENSE_SETTING_FACILITY:
  def: 'false'
  type: bool
AREA_DEFENSE_MINCAP_MAX_CAPITAL_DEFENSE:
  def: '100'
  type: int
  cmt: MaxUnits for capital defense is at least this. (basically use capital defense as
    a buffer if we have "too many units")
AREA_DEFENSE_MINCAP_DESIRED_CAPITAL_DEFENSE:
  def: '5'
  type: int
  cmt: DesiredUnits for capital defense is at least this.
AREA_DEFENSE_MINCAP_MAX_HOME_AREA:
  def: '10'
  type: int
  cmt: MaxUnits for home area is at least this.
AREA_DEFENSE_MINCAP_DESIRED_HOME_AREA:
  def: '3'
  type: int
  cmt: DesiredUnits for home area is at least this.
COMMAND_POWER_BEFORE_SPEND_ON_TRAITS:
  def: '30.0'
  type: float
PEACE_BID_FOLD_TURNS_AGAINST_OTHER_AI:
  def: '2'
  type: int
  cmt: Resolve contests against other AIs after this many turns. Don't always contest
    forever, it yields the same results.
PEACE_BID_CONTEST_TIE_BREAKER_CONFERENCE_SCORE:
  def: '1.0'
  type: float
  cmt: How much to weigh relative remaining peace conference score between the countries
PEACE_BID_CONTEST_TIE_BREAKER_INFLUENCE_DISTANCE:
  def: '1.0'
  type: float
  cmt: How much to weigh relative influence distance between the countries
PEACE_BID_CONTEST_TIE_BREAKER_COUNTRY_SCORE:
  def: '1.0'
  type: float
  cmt: How much to weigh relative country score between the countries
PEACE_BID_FOLD_AGAINST_PLAYER_CHANCE:
  def: '0.5'
  type: float
  cmt: Likelihood that AI will fold in a bidding contest against human player.
PEACE_BID_FOLD_AGAINST_LIBERATE_CONTEST:
  def: '1.0'
  type: float
  cmt: Likelihood that the AI will back down against a same-ideology country performing
    a contesting liberate bid ##Bordergore prevention therapy
PEACE_AI_GROUP_PEACE_ACTIONS:
  def: 'true'
  type: bool
  cmt: Whether AI should group peace actions or greedily just select the most-desired
    peace actions
PEACE_AI_EVALUATE_FOR_SUBJECTS:
  def: 'true'
  type: bool
  cmt: Whether AI should include subjects when evaluating giving states to other winners
    (may affect performance on new conference turn)
PEACE_AI_EVALUATE_FOR_ALLIES:
  def: 'true'
  type: bool
  cmt: Whether AI should include allies when evaluating giving states to other winners
    (may affect performance on new conference turn)
PEACE_AI_EVALUATE_FOR_NON_ALLIES:
  def: 'false'
  type: bool
  cmt: Whether AI should include non-allies (not in same faction) when evaluating giving
    states to other winners (may affect performance on new conference turn)
PEACE_AI_EVALUATE_OTHER_IF_CORE:
  def: 'true'
  type: bool
  cmt: Whether AI should evaluate giving states to other winners if state is their core
    (may affect performance on new conference turn)
PEACE_AI_EVALUATE_OTHER_IF_CLAIM:
  def: 'true'
  type: bool
  cmt: Whether AI should evaluate giving states to other winners if they have a claim on
    the state (may affect performance on new conference turn)
PEACE_AI_EVALUATE_OTHER_ALWAYS:
  def: 'false'
  type: bool
  cmt: Whether AI should always evaluate giving states to other winners (!!! may heavily
    affect performance on new conference turn for large peace conferences !!!)
DIVISION_SUPPLY_RATIO_TO_MOTORIZE:
  def: '0.80'
  type: float
  cmt: If supply ratio is less than this, consider motorizing any applicable nearby
    supply hub
INDUSTRIAL_ORG_TRAIT_UNLOCK_RANDOMNESS:
  def: '3'
  type: int
  cmt: AI will pick a random from N top traits when choosing a trait to unlock
INDUSTRIAL_ORG_POLICY_CHANGE_RANDOMNESS:
  def: '3'
  type: int
  cmt: AI will pick a random from N top policies when choosing a policy to attach to an
    MIO
INDUSTRIAL_ORG_RESEARCH_ASSIGN_RANDOMNESS:
  def: '3'
  type: int
  cmt: AI will pick a random from N top MIOs when choosing an MIO to assign to a
    research
INDUSTRIAL_ORG_PRODUCTION_ASSIGN_RANDOMNESS:
  def: '3'
  type: int
  cmt: AI will pick a random from N top MIOs when choosing an MIO to assign to a
    production line
INDUSTRIAL_ORG_POLICY_CHANGE_SCALE:
  def: '1.0'
  type: float
  cmt: Policy change weight will be scaled by this value
INDUSTRIAL_ORG_TRAIT_RANK_FACTOR:
  def: '0.80'
  type: float
  cmt: When precomputing weights, traits will affect the final score less the further
    down the tree they are, by this factor
INDUSTRIAL_ORG_RESEARCH_BONUS_FACTOR:
  def: '10.0'
  type: float
  cmt: Research bonus will be multiplied by this factor when evaluating design teams
AI_WANTED_LAND_BASED_PLANES_FACTOR:
  def: '0.50'
  type: float
  cmt: Factor applied to desire for land based planes (total airbase space * define)
AI_WANTED_CARRIER_BASED_PLANES_FACTOR:
  def: '1.0'
  type: float
  cmt: Factor applied to desire for carrier based planes (total carrier space * define)
AIFC_UPDATE_FREQUENCY_DAYS:
  def: '5'
  type: int
  cmt: How often will AI run its AI force concentration logic. Lowering this number may
    decrease performance.
AIFC_FRESHNESS_BASE_VALUE:
  def: '45.0'
  type: float
  cmt: AIFC fronts have a "freshness value" which decreases if no progress is made. When
    it reaches zero, it will give up on the current target and try another.
AIFC_REFRESH_NEED_PER_DAY:
  def: '1.0'
  type: float
  cmt: Decrease freshness value with this every day.
AIFC_REFRESH_NEED_SUPPLY_FACTOR_PER_DAY:
  def: '0.8'
  type: float
  cmt: Decrease freshness value with this multiplied by average supply ratio every day.
AIFC_FRESHNESS_ADD_ON_PROGRESS:
  def: '25.0'
  type: float
  cmt: Increase freshness value with this when we advance a province along the target
    path.
AIFC_UNIT_RATIO_BASE:
  def: '0.15'
  type: float
  cmt: After fulfilling minimum front unit needs, this ratio of the "extra"/desired
    units can be allocated to AI force concentration duty
AIFC_MAX_NR_FRONTS:
  def: '4'
  type: int
  cmt: The X (this) fronts with highest AIFC score are considered for AI force
    concentration
AIFC_CA_DIVISIONS_PER_PROVINCE:
  def: '3'
  type: int
  cmt: AI will use this as a baseline of how many divisions to have per province
AIFC_ACTIVATE_AVG_ORG_RATIO_THRESHOLD:
  def: '0.2'
  type: float
  cmt: Only activate the offensive order if average organisation is above this.
AIFC_ACTIVATE_IN_POSITION_RATIO_THRESHOLD:
  def: '0.3'
  type: float
  cmt: Only activate the offensive order if divisions in position is more than this
    ratio.
AIFC_OFFENSIVE_DEACTIVATION_DAYS_THRESHOLD:
  def: '5'
  type: int
  cmt: Deactivate the offensive order only if the conditions have been unfulfilled for
    this many days.
AIFC_UNIT_NUDGE_FREQUENCY_DAYS:
  def: '15'
  type: int
  cmt: On average every X day (randomly), check if another division (within same front)
    is better for AIFC based on score factors below.
AIFC_UNIT_OFFENSIVE_SCORE_FACTOR_BREAKTHROUGH:
  def: '11.0'
  type: float
AIFC_UNIT_OFFENSIVE_SCORE_FACTOR_SOFT_ATTACK:
  def: '6.0'
  type: float
AIFC_UNIT_OFFENSIVE_SCORE_FACTOR_HARD_ATTACK:
  def: '8.0'
  type: float
AIFC_UNIT_OFFENSIVE_SCORE_FACTOR_ARMOR:
  def: '30.0'
  type: float
AIFC_UNIT_OFFENSIVE_SCORE_FACTOR_PIERCING:
  def: '4.0'
  type: float
AIFC_UNIT_OFFENSIVE_SCORE_FACTOR_HARDNESS:
  def: '300.0'
  type: float
AIFC_UNIT_OFFENSIVE_SCORE_FACTOR_SPEED:
  def: '15.0'
  type: float
AIFC_UNIT_OFFENSIVE_SCORE_FACTOR_INITIATIVE:
  def: '5.0'
  type: float
AIFC_UNIT_OFFENSIVE_SCORE_FACTOR_ORGANISATION:
  def: '0.3'
  type: float
AIFC_UNIT_OFFENSIVE_SCORE_FACTOR_HITPOINTS:
  def: '0.3'
  type: float
AIFC_UNIT_OFFENSIVE_SCORE_FACTOR_DEFENSE:
  def: '-0.2'
  type: float
AIFC_UNIT_OFFENSIVE_SCORE_FACTOR_ENTRENCHMENT:
  def: '-0.5'
  type: float
AIFC_UNIT_OFFENSIVE_SCORE_FACTOR_EXPERIENCE:
  def: '300.0'
  type: float
AIFC_TARGET_IGNORE_VP_THRESHOLD:
  def: '10'
  type: int
  cmt: VP target needs at leas this many victory points to be considered a target
AIFC_TARGET_SUPPLY_HUB_BASE_SCORE:
  def: '20.0'
  type: float
  cmt: Base score for supply hubs
AIFC_TARGET_NAVAL_BASE_BASE_SCORE:
  def: '10.0'
  type: float
  cmt: Base score for naval bases
AIFC_TARGET_NAVAL_BASE_SCORE_PER_LEVEL:
  def: '1.0'
  type: float
  cmt: Score for naval bases increases by this for each level
AIFC_TARGET_VP_SCORE_FACTOR:
  def: '1.0'
  type: float
  cmt: Score for VPs increases by this for every victory point
AIFC_TARGET_CAPITAL_SCORE_EXTRA:
  def: '5.0'
  type: float
  cmt: Extra score for Capitals (in addition to VP score)
AIFC_TARGET_SHORT_PATH_PENALTY_FACTOR:
  def: '0.1'
  type: float
  cmt: Penalty factor for short AIFC paths (path <= 3 (including own start province))
AIFC_TARGET_PERSISTED_FACTOR:
  def: '30.0'
  type: float
  cmt: Bonus factor for persisted targets (used to incentivize AI to select target again
    after e.g. front lines have reformed or save file is loaded)
AIFC_PATH_MAX_COST:
  def: '7.0'
  type: float
  cmt: Only allow paths with total cost <= this. WARNING: increasing this value may
    cause stuttering and other performance issues (since AIFC will evaluate larger
    areas)
AIFC_PATH_COST_ADJ_NORMAL:
  def: '1.0'
  type: float
AIFC_PATH_COST_ADJ_STRAIT:
  def: '4.0'
  type: float
AIFC_PATH_COST_ADJ_RIVER:
  def: '2.0'
  type: float
AIFC_PATH_COST_ADJ_RIVER_LARGE:
  def: '3.0'
  type: float
AIFC_PATH_COST_TRN_MOUNTAINS:
  def: '2.0'
  type: float
AIFC_PATH_COST_TRN_FOREST:
  def: '1.5'
  type: float
AIFC_PATH_COST_TRN_DESERT:
  def: '1.5'
  type: float
AIFC_PATH_COST_TRN_HILLS:
  def: '1.2'
  type: float
AIFC_PATH_COST_TRN_JUNGLE:
  def: '3.0'
  type: float
AIFC_PATH_COST_TRN_PLAINS:
  def: '0.8'
  type: float
AIFC_PATH_COST_TRN_URBAN:
  def: '1.0'
  type: float
AIFC_PATH_COST_TRN_MARSH:
  def: '3.0'
  type: float
AIFC_PATH_COST_PER_FORT_LEVEL:
  def: '0.3'
  type: float
  cmt: This multiplier is calculated as: 1.0 + <define>*fort_level    (only for fort
    levels > 0)
AIFC_PATH_COST_HAS_SUPPLY_HUB:
  def: '0.5'
  type: float
  cmt: If the province we're entering has a supply hub
AIFC_PATH_COST_HAS_NAVAL_BASE:
  def: '0.5'
  type: float
  cmt: If the province we're entering has a naval base
AIFC_PATH_COST_RAILWAY_CONNECTION:
  def: '0.75'
  type: float
  cmt: If the provinces are connected by a railway with level > 0
RAIDS_ENABLE_AI:
  def: 'true'
  type: bool
  cmt: Whether AI should use the raid system
RAIDS_CREATE_FREQUENCY_DAYS:
  def: '7'
  type: int
  cmt: How often will AI run its raid creation logic. Lowering this number may decrease
    performance.
RAIDS_SCORE_DIFF_TO_CANCEL:
  def: '0.3'
  type: float
  cmt: If already-created low-scoring raids are blocking higher-scoring ones from being
    created due to command power, this allows the AI to cancel the lower-scoring raids.
    If `lowerScore < <value>*higherScore`, then the lower-scoring one may be cancelled.
    A value of 0.0 means it will never allow cancelling lower-scoring raids, while a
    value of 1.0 means it will always allow cancelling lower-scoring raids.
RAIDS_COMMAND_POWER_CAP_TO_CREATE:
  def: '60.0'
  type: float
  cmt: The AI will only try to create new raids if the command power cap is at least
    this.
RAIDS_MIN_SUCCESS_FOR_LAUNCH:
  def: '0.65'
  type: float
  cmt: The AI will not launch a raid if the chance of success is lower than this.
RAIDS_CANCEL_AFTER_DAYS_LAUNCHABLE:
  def: '60'
  type: int
  cmt: If a raid has been launchable for more than <this> days but not been launched
    (e.g. due to bad success chance), the AI will cancel the raid.
RAIDS_NUKE_TARGET_CUT_OFF:
  def: '10'
  type: int
  cmt: When AI selects targets for nukes, only pick from the <x> highest-scoring
    targets.
RAIDS_UNIT_SCORE_SUCCESS_CHANCE_FACTOR:
  def: '500.0'
  type: float
  cmt: When AI selects which units to use for raids, multiply the unit success chance
    modifier with this.
RAIDS_UNIT_SCORE_DISTANCE_KM_FACTOR:
  def: '0.1'
  type: float
  cmt: When AI selects which units to use for raids, multiply the km distance with this.
RAIDS_AVOID_SAME_TARGET_DURATION_DAYS:
  def: '180'
  type: int
  cmt: After a raid is finished/canceled, AI is less likely to raid the same target for
    this time.
RAIDS_AVOID_SAME_TARGET_FACTOR:
  def: '0.4'
  type: float
  cmt: If AI has already raided (or tried to raid) a target, score of new raids against
    same target is factored by this
PATROL_FLEETS_PER_INVASION_REGION_ON_PATH:
  def: '2'
  type: int
  cmt: How many STL patrol fleet templates should the AI try to use when generating
    dominance
AI_MIN_DOMINANCE_MARGIN:
  def: '200'
  type: int
  cmt: When trying to get control of a region, AI will try to exceed the required
    dominance by at least this amount
CONVOY_DANGER_FOR_MAX_IMPORTANCE:
  def: '50'
  type: int
  cmt: When deciding whether to protect a convoy route, the importance will scale with
    convoy danger up to this value
NUM_CONVOYS_FOR_MAX_PROTECTION:
  def: '50'
  type: int
  cmt: When deciding whether to protect a convoy route, the importance will scale with
    the number of convoys up to this value
CONVOY_RAIDING_TARGET_RECALC_DAYS:
  def: '3'
  type: int
  cmt: Each X days, the AI will reevaluate which regions to convoy raid (because enemy
    convoy usage or trade routes might change)
AI_OBJECTIVE_DEFAULT_TARGET_RECALC_DAYS:
  def: '0'
  type: int
  cmt: Each X days, the AI will reevaluate which regions to target for naval missions
    (this is the default value, but can be overriden by specific objectives, see
    CONVOY_RAIDING_TARGET_RECALC_DAYS)
DANGEROUS_ENEMY_ARMY_SIZE:
  def: '100'
  type: int
  cmt: If the size of the enemy's army of the attacking country is more than this value,
    the AI will add naval invasion defense importance
DANGEROUS_DISTANCE_TO_CAPITAL:
  def: '1000.0'
  type: float
  cmt: Distance in pixels from the target province to capital location where the AI will
    add the naval invasion defense importance
MIN_FACTORIES_TO_WANT_TO_IMPORT:
  def:
    - [0]  # oil
    - [0]  # aluminium
    - [0]  # rubber
    - [0]  # tungsten
    - [0]  # steel
    - [0]  # chromium
    - [10]  # coal
  type: table
  cmt: minimum number of civilian factories the AI must have to consider importing a
    resource - per strategic resource. Default 0, array -should- be updated with new
    resources, or if the order changes.
SUGGESTED_NUM_MAX_CARRIERS:
  def: '4'
  type: int
  cmt: We don't know exactly how many planes we should use when evaluating AI build so
    we need a suggested number to start things off. ALso used for task force suggestions
    list.
```
