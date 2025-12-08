---
domain: defines_list
concept: NDiplomacy
version: 1.17.2
requires: [defines]
relates: [diplomacy, factions]
---

```yaml
DIPLOMACY_REQUEST_EXPIRY_DAYS:
  def: '30'
  type: int
BASE_SURRENDER_LEVEL:
  def: '1.0'
  type: float
  cmt: Surrender when level reached. valid 0-1
MAX_TRUST_VALUE:
  def: '100'
  type: int
  cmt: Max trust value cap.
MIN_TRUST_VALUE:
  def: '-100'
  type: int
  cmt: Min trust value cap.
MAX_OPINION_VALUE:
  def: '100'
  type: int
  cmt: Max opinion value cap.
MIN_OPINION_VALUE:
  def: '-100'
  type: int
  cmt: Min opinion value cap.
BASE_TRUCE_PERIOD:
  def: '180'
  type: int
  cmt: Base truce period in days.
TRUCE_PERIOD_AFTER_KICKING_FROM_FACTION:
  def: '60'
  type: int
  cmt: Truce period after kicking someone from faction in days.
NUM_DAYS_TO_ENABLE_KICKING_NEW_MEMBERS_OF_FACTION:
  def: '90'
  type: int
  cmt: Number of days before being able to kick a new member of faction
NUM_DAYS_TO_ENABLE_REINVITE_KICKED_NATIONS:
  def: '90'
  type: int
  cmt: Number of days before being able to re invite a kicked nation to your faction
BASE_NEGATIVE_OPINION_AFTER_BEING_KICKED:
  def: '20'
  type: int
  cmt: Negative opinion that will be received after kicking a nation
DECAY_RATE_OF_NEGATIVE_OPINION_AFTER_BEING_KICKED:
  def: '1'
  type: int
  cmt: Weekly decay rate of the negative opinion
TRUCE_BREAK_COST_PP:
  def: '200'
  type: int
  cmt: Base cost in PP of breaking a truce by joining a war or accepting a call to war (
    you cannot declare war yourself until the truce if up ), this is then multiplied by
    the time left on the truce ( so once half the truce is up it only cost 50% of this )
BASE_PEACE_PUPPET_FACTOR:
  def: '100'
  type: int
  cmt: Base factor for puppet in %.
BASE_PEACE_LIBERATE_FACTOR:
  def: '100'
  type: int
  cmt: Base factor for liberate in %.
BASE_PEACE_TAKE_UNCONTROLLED_STATE_FACTOR:
  def: '10.0'
  type: float
  cmt: Base factor for taking state you do not control
BASE_PEACE_TAKE_FACTION_CONTROLLED_STATE_FACTOR:
  def: '0.5'
  type: float
  cmt: Base factor for taking state you do not control, but someone in faction does
BASE_PEACE_FORCE_GOVERNMENT_COST:
  def: '100'
  type: int
  cmt: Base cost for forcing a country to change government.
PEACE_COST_FACTOR_CONTESTED_MAX:
  def: '15'
  type: int
  cmt: To prevent overflows due to the exponential increase, cap the contested factor to
    this
PEACE_COST_FACTOR_UNCONTESTED_MAX:
  def: '15'
  type: int
  cmt: To prevent overflows due to the exponential increase, cap the uncontested factor
    to this
PEACE_COST_FACTOR_CONTESTED_BID:
  def: '1.20'
  type: float
  cmt: Cost factor for each contested bid on the state.
PEACE_COST_FACTOR_UNCONTESTED_BID_MIN:
  def: '1.15'
  type: float
  cmt: Minimum cost factor for each turn a bid has been uncontested on the state.
PEACE_COST_FACTOR_UNCONTESTED_BID_MAX:
  def: '1.60'
  type: float
  cmt: Maximum cost factor for each turn a bid has been uncontested on the state.
PEACE_COST_FACTOR_UNCONTESTED_BID_STEP:
  def: '0.15'
  type: float
  cmt: Uncontested cost factor will increase by this much each turn.
PEACE_COST_FACTOR_CAPITAL_SHIP_IC:
  def: '0.005'
  type: float
  cmt: In peace conference, cost for taking one capital ship per IC
PEACE_COST_FACTOR_SCREENING_SHIP_IC:
  def: '0.005'
  type: float
  cmt: In peace conference, cost for taking a part of the screening ships per IC
PEACE_INCREASE_COST_FACTOR_PER_MISSING_PERCENT_FOR_CAPITULATION:
  def: '0.0012'
  type: float
  cmt: increase factor if loser has not capitulated, for every percent between surrender
    level and BASE_SURRENDER_LEVEL
PEACE_COST_FACTOR_COMPLIANCE_STEPS:
  def:
    - [0, 1.0]  # between 0%  and 30% compliance, factor is 1.0
    - [30, 0.9]  # between 30% and 70%
    - [70, 0.8]  # above 70%
  type: table
PEACE_COST_FACTOR_STACK_DEMILITARIZED_ZONE:
  def: '0.25'
  type: float
PEACE_COST_FACTOR_STACK_WAR_REPARATION:
  def: '0.25'
  type: float
PEACE_COST_FACTOR_STACK_RESOURCE_RIGHTS:
  def: '0.25'
  type: float
PEACE_COST_FACTOR_STACK_DISMANTLE_INDUSTRY:
  def: '0.25'
  type: float
PEACE_TIMED_EFFECT_LENGTH_DEMILITARIZED_ZONE:
  def: '1825'
  type: int
  cmt: 5 years
PEACE_TIMED_EFFECT_LENGTH_WAR_REPARATION:
  def: '1825'
  type: int
PEACE_TIMED_EFFECT_LENGTH_RESOURCE_RIGHTS:
  def: '1825'
  type: int
PEACE_TIMED_EFFECT_RATIO_CIVILIAN_FACTORY_WAR_REPARATION:
  def: '0.5'
  type: float
  cmt: ratio of civilian factories taken via stackable war reparation
INFLUENCE_NEUTRAL_DIST_CAPITAL:
  def: '30.0'
  type: float
  cmt: distance to capital that results in a cost modifier of 1.0
INFLUENCE_MAX_DIST_CAPITAL:
  def: '45.0'
  type: float
  cmt: distance to capital that results in a cost modifier of
    INFLUENCE_MAX_DIST_COST_MODIFIER
INFLUENCE_NEUTRAL_DIST_CORE:
  def: '6.0'
  type: float
  cmt: distance to nearest core state that results in a cost modifier of 1.0
INFLUENCE_MAX_DIST_CORE:
  def: '13.0'
  type: float
  cmt: distance to nearest core state that results in a cost modifier of
    INFLUENCE_MAX_DIST_COST_MODIFIER
INFLUENCE_NEUTRAL_DIST_CONTROLLED:
  def: '14.0'
  type: float
  cmt: distance to nearest controlled state that results in a cost modifier of 1.0
INFLUENCE_MAX_DIST_CONTROLLED:
  def: '20.0'
  type: float
  cmt: distance to nearest controlled state that results in a cost modifier of
    INFLUENCE_MAX_DIST_COST_MODIFIER
INFLUENCE_MIN_DIST_COST_MODIFIER:
  def: '0.70'
  type: float
  cmt: Cost modifier at min (zero) distance
INFLUENCE_MAX_DIST_COST_MODIFIER:
  def: '1.00'
  type: float
  cmt: Cost modifier at max distance
INFLUENCE_RATIO_CAPITAL:
  def: '0.05'
  type: float
  cmt: Ratio of influence based on distance to capital
INFLUENCE_RATIO_CORE:
  def: '0.45'
  type: float
  cmt: Ratio of influence based on distance to nearest core territory
INFLUENCE_RATIO_CONTROLLED:
  def: '0.5'
  type: float
  cmt: Ratio of influence based on distance to neared controlled territory (including
    uncontested peace conference bids)
INFLUENCE_DISTANCE_DIVISOR:
  def: '22.0'
  type: float
  cmt: Divide pixel distance with this when determining distance to capital / core /
    controlled states. Just an arbitrary way of scaling the distance numbers.
INFLUENCE_PER_ADJACENCY:
  def: '0.05'
  type: float
  cmt: How much influence to add per uncontested adjacent state in the PC (blob, don't
    snake)
INFLUENCE_MAJOR_FACTOR:
  def: '1.0'
  type: float
  cmt: How much influence discount an AI major will get (inverse)
INFLUENCE_MINOR_FACTOR:
  def: '1.0'
  type: float
  cmt: How much influence discount an AI minor will get (inverse)
PEACE_TRIGGER_AI_MAX_INFLUENCE_VALUE:
  def: '0.99'
  type: float
  cmt: Max influence value for pc_is_state_outside_influence_for_winner trigger
BASE_IMPROVE_RELATION_COST:
  def: '10'
  type: int
  cmt: Political power cost to initiate relation improvement
BASE_IMPROVE_RELATION_SAME_IDEOLOGY_GROUP_MAINTAIN_COST:
  def: '0.2'
  type: float
  cmt: Political power cost each update when boosting relations with nation of same
    ideology
BASE_IMPROVE_RELATION_DIFFERENT_IDEOLOGY_GROUP_MAINTAIN_COST:
  def: '0.4'
  type: float
  cmt: Political power cost each update when boosting relations with nation of different
    ideology
BASE_SEND_ATTACHE_COST:
  def: '100'
  type: int
  cmt: Political power cost to send attache
BASE_SEND_ATTACHE_CP_COST:
  def: '50.0'
  type: float
  cmt: Command Power sent attache usage cost
BASE_GENERATE_WARGOAL_DAILY_PP:
  def: '0.2'
  type: float
  cmt: Daily pp cost for generation of wargoals
WARGOAL_VERSUS_MAJOR_AT_WAR_REDUCTION:
  def: '-0.75'
  type: float
  cmt: reduction of pp cost for wargoal vs major at war.
WARGOAL_WORLD_TENSION_REDUCTION:
  def: '-0.5'
  type: float
  cmt: Reduction of pp cost for wargoal at 100% world tension, scales linearly
WARGOAL_JUSTIFY_TENSION_FROM_PRODUCTION:
  def: '30.0'
  type: float
  cmt: Base value scaled by production capacity of country compared to biggest country
MIN_WARGOAL_JUSTIFY_COST:
  def: '2.0'
  type: float
  cmt: It always takes atleast 10 days to justify a wargoal
WARGOAL_PER_JUSTIFY_AND_WAR_COST_FACTOR:
  def: '1.5'
  type: float
  cmt: Cost factor per nation at war with or justifying against
WARGOAL_THREAT_MAX_TIME_RATIO:
  def: '1.0'
  type: float
  cmt: Threat from justifying a wargoal slowly builds up, hitting 100% at this
    proportion of the way to completion
BASE_BOOST_PARTY_POPULARITY_DAILY_PP:
  def: '0.25'
  type: float
  cmt: Daily pp cost for boost party popularity
BASE_BOOST_PARTY_POPULARITY_DAILY_DRIFT:
  def: '0.1'
  type: float
  cmt: Daily amount of popularity that will be added by the activity.
BASE_STAGE_COUP_DAILY_PP:
  def: '0.5'
  type: float
  cmt: Daily pp cost for staging a coup
BASE_STAGE_COUP_TOTAL_COST:
  def: '200'
  type: int
  cmt: Equipment consume factor for stage coup.
NAP_EXPIRY_MONTHS:
  def: '48'
  type: int
  cmt: NAPs expire after this many months
NAP_UNBREAKABLE_MONTHS:
  def: '12'
  type: int
  cmt: NAPS cannot be broken for this many months
NAP_FORCE_BALANCE_RULE_MONTHS:
  def: '6'
  type: int
  cmt: The NAP border force balance rule changes with this interval
NAP_BREAK_FORCE_BALANCE_1:
  def: '2.0'
  type: float
  cmt: 2-1 brigades along the border required to break NAP
NAP_BREAK_FORCE_BALANCE_2:
  def: '1.0'
  type: float
  cmt: 1-1 brigades along the border required to break NAP
NAP_BREAK_FORCE_BALANCE_3:
  def: '0.5'
  type: float
  cmt: 1-2 brigades along the border required to break NAP
VERY_GOOD_OPINION:
  def: '50'
  type: int
  cmt: Threshold for a country that has a very good opinion of you.
VERY_BAD_OPINION:
  def: '-50'
  type: int
  cmt: Threshold for a country that has a very bad opinion of you.
DIPLOMACY_HOURS_BETWEEN_REQUESTS:
  def: '24'
  type: int
  cmt: How long a country must wait before sending a new diplomatic request.
TROOP_FEAR:
  def: '1'
  type: int
  cmt: Impact on troops on borders when deciding how willing a nation is to trade
FLEET_FEAR:
  def: '1'
  type: int
  cmt: Impact on troops on borders when deciding how willing a nation is to trade
IC_TO_EQUIPMENT_COUP_RATIO:
  def: '0.1'
  type: float
  cmt: Ratio for calculating cost of staging coup
VOLUNTEERS_PER_TARGET_PROVINCE:
  def: '0.05'
  type: float
  cmt: Each province owned by the target country contributes this amount of volunteers
    to the limit.
VOLUNTEERS_PER_COUNTRY_ARMY:
  def: '0.05'
  type: float
  cmt: Each army unit owned by the source country contributes this amount of volunteers
    to the limit.
VOLUNTEERS_RETURN_EQUIPMENT:
  def: '0.95'
  type: float
  cmt: Returning volunteers keep this much equipment
VOLUNTEERS_TRANSFER_SPEED:
  def: '14'
  type: int
  cmt: days to transfer a unit to another nation
VOLUNTEERS_DIVISIONS_REQUIRED:
  def: '30'
  type: int
  cmt: This many divisons are required for the country to be able to send volunteers.
TENSION_STATE_VALUE:
  def: '0.10'
  type: float
  cmt: Tension value gained by annexing one state (this value used to be divided by 20,
    this is no longer the case)
TENSION_CIVIL_WAR_IMPACT:
  def: '0.2'
  type: float
  cmt: civil war multiplier on tension.
TENSION_NO_CB_WAR:
  def: '14'
  type: int
  cmt: Amount of tension generated by a no-CB wargoal
TENSION_CB_WAR:
  def: '10'
  type: int
  cmt: Amount of tension generated by a war with a CB
TENSION_ANNEX_NO_CLAIM:
  def: '0.20'
  type: float
  cmt: Amount of tension generated by annexing a state you don't have claims on
TENSION_ANNEX_CLAIM:
  def: '0.10'
  type: float
  cmt: Amount of tension generated by annexing a state you DO have claims on
TENSION_ANNEX_CORE:
  def: '-0.5'
  type: float
  cmt: Amount of tension generated by annexing a state that is your core
TENSION_PUPPET:
  def: '0'
  type: int
  cmt: Amount of tension generated by puppeting (per state)
TENSION_FORCE_GOVERNMENT:
  def: '-0.5'
  type: float
  cmt: Amount of tension generated by forcing government (per state)
TENSION_VOLUNTEER_FORCE_DIVISION:
  def: '0.2'
  type: float
  cmt: Amount of tension generated for each sent division
TENSION_DECAY_DAILY:
  def: '0.005'
  type: float
  cmt: Each day tension decays this much for Threat sources which are no longer
    relevant. Replaces TENSION_DECAY as of 1.12.0
TENSION_SIZE_FACTOR:
  def: '1.0'
  type: float
  cmt: All action tension values are multiplied by this value
TENSION_TIME_SCALE_START_DATE:
  def: '1936.1.1.12'
  type: string
  cmt: Starting at this date, the tension values will be scaled down (will be equal to 1
    before that)
TENSION_TIME_SCALE_MONTHLY_FACTOR:
  def: '-0.005'
  type: float
  cmt: Timed tension scale will be modified by this amount starting with
    TENSION_TIME_SCALE_START_DATE
TENSION_TIME_SCALE_MIN:
  def: '0.25'
  type: float
  cmt: Timed tension scale won't decrease under this value
TENSION_GUARANTEE:
  def: '-5'
  type: int
TENSION_FACTION_JOIN:
  def: '4'
  type: int
TENSION_JOIN_ATTACKER:
  def: '2'
  type: int
  cmt: scale of the amount of tension added when country joins attacker side
TENSION_PEACE_FACTOR:
  def: '0.80'
  type: float
  cmt: scale of the amount of tension (from war declaration) reduced when peace is
    completed. Scaled by current world threat * TENSION_PEACE_FACTOR_THREAT_FACTOR
TENSION_PEACE_FACTOR_THREAT_FACTOR:
  def: '0.60'
  type: float
  cmt: see above
TENSION_LIBERATE:
  def: '-1'
  type: int
  cmt: Amount of tension generated by liberating a country.
TENSION_TAKE_ONE_CAPITAL_SHIP:
  def: '0'
  type: int
  cmt: Amount of tension generated by 1 take navy peace action
TENSION_DEMILITARIZE_ZONE:
  def: '-0.50'
  type: float
  cmt: Amount of tension generated by stacking demilitarize zone on 1 state, multiplied
    with the state base threat
TENSION_WAR_REPARATION:
  def: '0'
  type: int
  cmt: Amount of tension generated by stacking war reparation on 1 state, multiplied
    with the state base threat
TENSION_RESOURCE_RIGHTS:
  def: '0'
  type: int
  cmt: Amount of tension generated by stacking resource rights on 1 state, multiplied
    with the state base threat
TENSION_DISMANTLE_INDUSTRY:
  def: '0'
  type: int
  cmt: Amount of tension generated by stacking dismantle military industry on 1 state,
    multiplied with the state base threat
TENSION_CAPITULATE:
  def: '0'
  type: int
  cmt: Scale of the amount of tension created by a countries capitulation.
GUARANTEE_COST:
  def: '15'
  type: int
  cmt: Scale with the number of already guaranteed countries.
REVOKE_GUARANTEE_COST:
  def: '15'
  type: int
BASE_CONDITIONAL_PEACE_WARESCORE_RATIO:
  def: '0.5'
  type: float
  cmt: Warscore ratio needed for the losing side to able to surrender.
BASE_CONDITIONAL_PEACE_MONTHS:
  def: '3'
  type: int
  cmt: War length must be before a surrender is possible.
JOINING_NAP_WAR_PENALTY:
  def: '0.2'
  type: float
  cmt: War support penalty for breaking non-breakable NAP
BREAKING_GUARANTEE_PENALTY:
  def: '0.2'
  type: float
  cmt: War support penalty for breaking guarantee
PEACE_SCORE_TRANSFERRED_TO_FACTION_LEADER:
  def: '0.1'
  type: float
  cmt: Part of the peace score transferred from the faction members to the faction
    leader (if game rule enabled)
PEACE_SCORE_RESET_LOW_SCORE_THRESHOLD:
  def: '0.05'
  type: float
  cmt: Winners with less than this ratio of war participation will give all their score
    to other players
PEACE_SCORE_RESET_LOW_SCORE_MINIMUM_FOR_RECEIVER:
  def: '0.1'
  type: float
  cmt: Disable the previous, if no winner has at least this ratio of war participation
PEACE_SCORE_TRANSFERRED_FROM_FACTION_INFLUENCE:
  def: '0.1'
  type: float
  cmt: How much % of your war score will be given to the top
    PEACE_SCORE_TOP_FACTION_INFLUENCE_AMOUNT of your faction
PEACE_SCORE_TOP_FACTION_INFLUENCE_AMOUNT:
  def: '2'
  type: int
  cmt: The amount of highest grossing influence members from your factions that get
    additional war score
PEACE_SCORE_SCALE_FACTOR:
  def: '1.35'
  type: float
  cmt: Losers' total value times this factor becomes the default total peace conference
    score that is distributed to the winners.
PEACE_SCORE_MINOR_BOOST_FRACTION:
  def: '0.05'
  type: float
  cmt: Low-scoring winners are boosted by receiving more of their score earlier. This
    value, multiplied by the total score distributed this turn, is the minimum score
    they will receive (up until their total allocated score).
PEACE_SCORE_DISTRIBUTION:
  def:
    - [0.2, 0.2, 0.2, 0.2, 0.2]
  type: table
  cmt: How much of the total peace conference score you get during the first n turns.
PEACE_CONTEST_REFUND_FACTOR:
  def:
    - [1.0, 0.92, 0.84, 0.76]
  type: table
  cmt: How much of the spent peace conference score that gets refunded in a contest.
    First element applies for the first round of conflicts, second element for the
    second round of conflicts, etc. The final element is used for each consecutive turn,
    so setting that to e.g. 0.7 means you get 70 % of the spent score back for every
    turn thereafter.
PEACE_PLAY_SOUND_ON_NEW_TURN:
  def: 'true'
  type: bool
  cmt: Whether the 'peace_conference_new_turn' audio hook is called or not
PEACE_PLAY_NEW_TURN_SOUND_ONLY_IF_NOT_ALREADY_PLAYING:
  def: 'true'
  type: bool
  cmt: Whether the 'peace_conference_new_turn' audio hook should play only if not
    already playing (relevant if players spam-click the pass/submit button)
MAX_REMEMBERED_LEASED_IC:
  def: '1000'
  type: int
  cmt: Maximum of leased equipment value that is remembered for opinion bonus
MAX_OPINION_FOR_LEASED_IC:
  def: '30'
  type: int
  cmt: Positive opinion when remembering the MAX_REMEMBERED_LEASED_IC equipment
MONTHLY_LEASED_IC_DECAY:
  def: '35'
  type: int
  cmt: How much of leased equipment is being "forgot" each month
OPINION_PER_VOLUNTEER:
  def: '3'
  type: int
  cmt: Opinion bonus per one sent volunteer division
MAX_OPINION_FROM_VOLUNTEERS:
  def: '30'
  type: int
  cmt: Opinion bonus per one sent volunteer division
OPINION_FOR_DEMO_FROM_WT_GENERATION:
  def: '-2.0'
  type: float
  cmt: How much less do democracies like us if we generate world tension
NOT_READY_FOR_WAR_BASE:
  def: '-50'
  type: int
  cmt: AI should be unwilling to enter accept a call to war if not ready for war against
    the relevant enemies.
FRONT_IS_DANGEROUS:
  def: '-100'
  type: int
  cmt: AI should be unwilling to enter accept a call to war if front is too dangerous.
NOT_READY_FOR_WAR_VAL_PER_DAY_SINCE_CALL:
  def: '1'
  type: int
  cmt: Value modifying the not ready base over time.
PEACE_ACTION_MAX_COST:
  def: '9999'
  type: int
  cmt: Max value for a peace action cost (after all modifiers)
RESOURCE_SENT_AUTONOMY_DAILY_BASE:
  def: '0.0'
  type: float
  cmt: If puppet provides resources to its master they increasy their autonomy by at
    least this amount
RESOURCE_SENT_AUTONOMY_DAILY_FACTOR:
  def: '0.005'
  type: float
  cmt: If puppet provides resources to its master they increasy their autonomy by the
    resources factored by this
WAR_SCORE_AUTONOMY_BASE:
  def: '0.0'
  type: float
  cmt: Value added if any war score is contributed by puppet
WAR_SCORE_AUTONOMY_FACTOR:
  def: '0.6'
  type: float
  cmt: If puppet generates war score it get a boost to independence
LL_TO_OVERLORD_AUTONOMY_DAILY_BASE:
  def: '0.0'
  type: float
  cmt: If puppet lend leases equipment to overlord of at least same tech level as they
    have, they gain autonomy
LL_TO_OVERLORD_AUTONOMY_DAILY_FACTOR:
  def: '0.05'
  type: float
  cmt: If puppet lend leases equipment to overlord of at least same tech level as they
    have, they gain autonomy
LL_TO_PUPPET_AUTONOMY_DAILY_BASE:
  def: '0.0'
  type: float
  cmt: If overlord lend leases equipment to puppet of higher tech level as they have,
    puppet losses autonomy
LL_TO_PUPPET_AUTONOMY_DAILY_FACTOR:
  def: '-0.01'
  type: float
  cmt: If overlord lend leases equipment to puppet of higher tech level as they have,
    puppet losses autonomy
AUTONOMY_FREEDOM_FROM_CAPITULATE:
  def: '0.5'
  type: float
  cmt: if overlord capitulate you get this
ATTACHE_TO_SUBJECT_EFFECT:
  def: '-0.05'
  type: float
  cmt: If overlord sent attaches to the subject it losses autonomy
ATTACHE_TO_OVERLORD_EFFECT:
  def: '0.05'
  type: float
  cmt: If subject sent attaches to the overlord it gains autonomy
AUTONOMY_LEVEL_CHANGE_SANCTUARY:
  def: '30'
  type: int
  cmt: The number of days post autonomy level has changed where neither side can
    increase nor decrease the autonomy level.
AUTONOMY_LEVEL_CHANGE_PP_COST_BASE:
  def: '50.0'
  type: float
  cmt: Base cost of changing level of autonomy
AUTONOMY_LEVEL_CHANGE_PP_ANNEX:
  def: '300'
  type: int
  cmt: Annexation cost
AUTONOMY_LEVEL_CHANGE_PP_FREE:
  def: '300'
  type: int
  cmt: Break free cost
MAX_SCORE_DIFF_TO_CHANGE_AUTONOMY:
  def: '10'
  type: int
  cmt: The max diff between current freedom score and the cap for next or previous level
    allowed for changing
MASTER_BUILD_AUTONOMY_FACTOR:
  def: '-0.7'
  type: float
  cmt: scales autonomy gain from construction by this
VICTORY_POINT_WORTH_FACTOR:
  def: '10'
  type: int
  cmt: multiplier when calcualting province worth (surrender)
VICTORY_POINT_WORTH_FACTOR_WARSCORE:
  def: '0.2'
  type: float
  cmt: multiplier for each victory points when calculating province worth for warscore
PROVINCE_WORTH_FROM_STATE_VALUE_FACTOR_WARSCORE:
  def: '0.2'
  type: float
  cmt: multiplier for the average value a province received from state for warscore
CAPITAL_CAPITULATE_BONUS_SCORE:
  def: '150'
  type: int
  cmt: extra bonus when deciding who to capitulate to (applied to capital holder)
CAPITAL_CAPITULATE_BONUS_SCORE_MUL:
  def: '1.5'
  type: float
  cmt: extra bonus multiplier when deciding who to capitulate to (applied to capital
    holder)
IDEOLOGY_JOIN_FACTION_MIN_LEVEL:
  def: '0.3'
  type: float
  cmt: ideology limit required to join faction
JOIN_FACTION_LIMIT_CHANGE_AT_WAR:
  def: '0.5'
  type: float
  cmt: if in defensive war this or your modifier is counted as limit to join factions
    (so if you have 80% join limit this now means you can join at 50%)
LICENSE_ACCEPTANCE_OPINION_FACTOR:
  def: '0.4'
  type: float
  cmt: Opinion modifier for acceptance of license production requests.
LICENSE_ACCEPTANCE_PUPPET_BASE:
  def: '15'
  type: int
  cmt: Acceptance modifier for puppets requesting production licenses.
LICENSE_ACCEPTANCE_TECH_DIFFERENCE:
  def: '2'
  type: int
  cmt: Acceptance modifier for each year of technology difference.
LICENSE_ACCEPTANCE_TECH_DIFFERENCE_BASE:
  def: '10'
  type: int
  cmt: Acceptance base for tech difference
LICENSE_ACCEPTANCE_SAME_FACTION:
  def: '20'
  type: int
  cmt: Acceptance modifier for being in the same faction
WARGOAL_COST_LEND_LEASE:
  def: '-0.25'
  type: float
  cmt: cost modifier to wargoaljustification for LL
WARGOAL_COST_DOCKING_RIGHTS:
  def: '-0.2'
  type: float
  cmt: cost modifier to wargoaljustification for dockign rights
WARGOAL_COST_VOLUNTEERS:
  def: '-0.5'
  type: float
  cmt: cost modifier to wargoaljustification for volunteers
ASSUME_FACTION_LEADERSHIP_PP_COST:
  def: '200'
  type: int
  cmt: Political power cost to assume faction leadership
ASSUME_FACTION_LEADERSHIP_MIN_MANPOWER_RATIO:
  def: '2'
  type: int
  cmt: The minimum ratio of manpower that a country must have compared to the current
    leader in order to assume leadership.
ASSUME_FACTION_LEADERSHIP_MIN_FACTORY_RATIO:
  def: '1.5'
  type: float
  cmt: The minimum ratio of factories that a country must have compared to the current
    leader in order to assume leadership.
ASSUME_FACTION_LEADERSHIP_COOLDOWN_DAYS:
  def: '180'
  type: int
  cmt: Number of days after formation of faction or change in leadership before another
    country is allowed to assume leadership.
ASSUME_FACTION_SPYMASTER_COOLDOWN_DAYS:
  def: '180'
  type: int
  cmt: Number of days after change of Spy Master before another country is allowed to
    become Spy Master.
FACTION_LEADERSHIP_CHANGE_ALERT_THRESHOLD:
  def: '0.8'
  type: float
  cmt: Threshold for showing an alert when a faction member is close to being able to
    assume leadership of the faction that a player currently leads.
FACTION_LEADERSHIP_CHANGE_NOT_SUBJECT_WEIGHT:
  def: '2'
  type: int
  cmt: Importance of subject status when determining how close a faction member is to
    being able to assume leadership.
FACTION_LEADERSHIP_CHANGE_NOT_CAPITULATED_WEIGHT:
  def: '2'
  type: int
  cmt: Importance of capitulation status when determining how close a faction member is
    to being able to assume leadership.
FACTION_LEADERSHIP_CHANGE_IN_ALL_WARS_WEIGHT:
  def: '1'
  type: int
  cmt: Importance not being in all faction leader wars when determining how close a
    faction member is to being able to assume leadership.
FACTION_LEADERSHIP_CHANGE_COOLDOWN_WEIGHT:
  def: '1'
  type: int
  cmt: Importance of leadership change cooldown when determining how close a faction
    member is to being able to assume leadership.
FACTION_LEADERSHIP_CHANGE_MANPOWER_WEIGHT:
  def: '2'
  type: int
  cmt: Importance of manpower in field when determining how close a faction member is to
    being able to assume leadership.
FACTION_LEADERSHIP_CHANGE_FACTORY_WEIGHT:
  def: '2'
  type: int
  cmt: Importance of factory count when determining how close a faction member is to
    being able to assume leadership.
FACTION_POWER_RESOURCE_WEIGHT:
  def: '0.05'
  type: float
  cmt: The weight of the country resources on the faction's power projection
FACTION_POWER_INDUSTRY_WEIGHT:
  def: '0.1'
  type: float
  cmt: The weight of the industry on the faction's power projection
FACTION_POWER_ARMY_WEIGHT:
  def: '0.25'
  type: float
  cmt: The weight of the army on the faction's power projection
FACTION_POWER_AIR_BOMBER_WEIGHT:
  def: '0.25'
  type: float
  cmt: The weight of the bombers on the faction's power projection
FACTION_POWER_AIR_WEIGHT:
  def: '0.02'
  type: float
  cmt: The weight of the air equipment except bombers on the faction's power projection
FACTION_POWER_NAVAL_CAPITAL_SHIP_WEIGHT:
  def: '5'
  type: int
  cmt: The weight of the capital ships on the faction's power projection
FACTION_POWER_NAVAL_WEIGHT:
  def: '0.25'
  type: float
  cmt: The weight of the naval equipment except capital ships on the faction's power
    projection
FACTION_POWER_EFFECTS_WEIGHT:
  def: '1'
  type: int
  cmt: The weight of the faction's goal status on the faction's power projection
EMBARGO_COST:
  def: '100'
  type: int
  cmt: One-time cost
REVOKE_EMBARGO_COST:
  def: '0'
  type: int
  cmt: Cost to remove an existing embargo
EMBARGO_THREAT_THRESHOLD:
  def: '30'
  type: int
  cmt: Target-generated threat threshold to allow embargo (affected by modifiers)
EMBARGO_SAME_IDEOLOGY_AI_WEIGHT:
  def: '-20'
  type: int
  cmt: AI weight for same ideology
EMBARGO_DIFFERENT_IDEOLOGY_AI_WEIGHT:
  def: '15'
  type: int
  cmt: AI weight for different ideology
EMBARGO_DIFFERENT_IDEOLOGY_AT_OFFENSIVE_WAR_AI_WEIGHT:
  def: '10'
  type: int
  cmt: AI weight for different ideology and in offensive war (additive with above)
EMBARGO_RECIPIENT_IS_MAJOR_AI_WEIGHT:
  def: '10'
  type: int
  cmt: Ai weight for recipient being major
EMBARGO_NEIGHBOUR_AI_WEIGHT:
  def: '-10'
  type: int
  cmt: AI weight for embargoing neighbors (neighbors are big and scary, we should
    consider not doing it)
NAVAL_BLOCKADE_BASE_COST:
  def: '50'
  type: int
  cmt: Base PP cost for issuing a naval blockade
NAVAL_BLOCKADE_DAILY_COST:
  def: '0.1'
  type: float
  cmt: Daily PP cost for one naval blockade
NAVAL_BLOCKADE_THREAT_THRESHOLD:
  def: '15'
  type: int
  cmt: Target-generated threat threshold to allow naval blockade
EQUIPMENT_PURCHASE_ACCEPTANCE_OPINION:
  def: '1.1'
  type: float
  cmt: Acceptance factor for opinion
EQUIPMENT_PURCHASE_ACCEPTANCE_SAME_IDEOLOGY:
  def: '15'
  type: int
  cmt: Acceptance value added if same ideology
EQUIPMENT_PURCHASE_ACCEPTANCE_SCRIPTED_IDEOLOGY_ACCEPTANCE:
  def: '1.0'
  type: float
  cmt: Acceptance factor for scripted ideology acceptance modifier
EQUIPMENT_PURCHASE_ACCEPTANCE_TRADE_INFLUENCE:
  def: '0.70'
  type: float
  cmt: Acceptance factor for trade influence (adjusted from base value)
EQUIPMENT_PURCHASE_ACCEPTANCE_COMPETING_FACTIONS:
  def: '-30'
  type: int
  cmt: Acceptance value added if both countries are in factions, and factions are
    different
EQUIPMENT_PURCHASE_ACCEPTANCE_EMBARGO:
  def: '-200'
  type: int
  cmt: Acceptance value added if either side has embargoed the other
EQUIPMENT_PURCHASE_ACCEPTANCE_NON_AGGRESSION_PACT:
  def: '25'
  type: int
  cmt: Acceptance value added if there is a non-aggression pact between the countries
MARKET_ACCESS_ACCEPTANCE_OPINION:
  def: '1.1'
  type: float
  cmt: Acceptance factor for opinion
MARKET_ACCESS_ACCEPTANCE_SAME_IDEOLOGY:
  def: '15'
  type: int
  cmt: Acceptance value added if same ideology
MARKET_ACCESS_ACCEPTANCE_SCRIPTED_IDEOLOGY_ACCEPTANCE:
  def: '1.0'
  type: float
  cmt: Acceptance factor for scripted ideology acceptance modifier
MARKET_ACCESS_ACCEPTANCE_TRADE_INFLUENCE:
  def: '0.70'
  type: float
  cmt: Acceptance factor for trade influence (adjusted from base value)
MARKET_ACCESS_ACCEPTANCE_COMPETING_FACTIONS:
  def: '-30'
  type: int
  cmt: Acceptance value added if both countries are in factions, and factions are
    different
MARKET_ACCESS_ACCEPTANCE_EMBARGO:
  def: '-200'
  type: int
  cmt: Acceptance value added if either side has embargoed the other
MARKET_ACCESS_ACCEPTANCE_NO_TRADE_ROUTE:
  def: '-100'
  type: int
  cmt: Acceptance value added if there is no valid trade route between the countries
MARKET_ACCESS_ACCEPTANCE_NON_AGGRESSION_PACT:
  def: '25'
  type: int
  cmt: Acceptance value added if there is a non-aggression pact between the countries
```
