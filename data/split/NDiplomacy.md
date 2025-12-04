```yaml
DIPLOMACY_REQUEST_EXPIRY_DAYS:
  def: '30'
  type: int
MAX_TRUST_VALUE:
  def: '100'
  type: int
  cmt: Max trust value cap.
MAX_OPINION_VALUE:
  def: '100'
  type: int
  cmt: Max opinion value cap.
BASE_TRUCE_PERIOD:
  def: '180'
  type: int
  cmt: Base truce period in days.
NUM_DAYS_TO_ENABLE_KICKING_NEW_MEMBERS_OF_FACTION:
  def: '90'
  type: int
  cmt: Number of days before being able to kick a new member of faction
BASE_NEGATIVE_OPINION_AFTER_BEING_KICKED:
  def: '20'
  type: int
  cmt: Negative opinion that will be received after kicking a nation
TRUCE_BREAK_COST_PP:
  def: '200'
  type: int
  cmt: Base cost in PP of breaking a truce by joining a war or accepting a call to
    war ( you cannot declare war yourself until the truce if up ), this is then multiplied
    by the time left on the truce ( so once half the truce is up it only cost 50%
    of this )
BASE_PEACE_LIBERATE_FACTOR:
  def: '100'
  type: int
  cmt: Base factor for liberate in %.
BASE_PEACE_TAKE_FACTION_CONTROLLED_STATE_FACTOR:
  def: '0.5'
  type: float
  cmt: Base factor for taking state you do not control, but someone in faction does
PEACE_COST_FACTOR_CONTESTED_MAX:
  def: '15'
  type: int
  cmt: In peace conference, cost is factored based on how many times the state has
    been contested and for how long it has been uncontested (for everyone else) To
    prevent overflows due to the exponential increase, cap the contested factor to
    this
PEACE_COST_FACTOR_CONTESTED_BID:
  def: '1.20'
  type: float
  cmt: Cost factor for each contested bid on the state.
PEACE_COST_FACTOR_UNCONTESTED_BID_MAX:
  def: '1.60'
  type: float
  cmt: Maximum cost factor for each turn a bid has been uncontested on the state.
PEACE_COST_FACTOR_CAPITAL_SHIP_IC:
  def: '0.005'
  type: float
  cmt: In peace conference, cost for taking one capital ship per IC
PEACE_INCREASE_COST_FACTOR_PER_MISSING_PERCENT_FOR_CAPITULATION:
  def: '0.0012'
  type: float
  cmt: increase factor if loser has not capitulated, for every percent between surrender
    level and BASE_SURRENDER_LEVEL
PEACE_COST_FACTOR_STACK_DEMILITARIZED_ZONE:
  def: '0.25'
  type: float
  cmt: In peace conference, adding a stackable to a peace action, increment the cost
    by a percentage
PEACE_COST_FACTOR_STACK_RESOURCE_RIGHTS:
  def: '0.25'
  type: float
PEACE_TIMED_EFFECT_LENGTH_DEMILITARIZED_ZONE:
  def: '1825'
  type: int
  cmt: peace conference can set timed effect, set length in days 5 years
PEACE_TIMED_EFFECT_LENGTH_RESOURCE_RIGHTS:
  def: '1825'
  type: int
INFLUENCE_NEUTRAL_DIST_CAPITAL:
  def: '30.0'
  type: float
  cmt: 'The Influence cost modifier is basically the inverse of distance. Nearby states
    are cheaper, and far-away states are more expensive. We basically do a two-segment
    lerp: if distance is between [0, NEUTRAL_DIST], we lerp the cost modifier between
    [MIN_DIST_COST_MODIFIER, 1.0] if distance is between [NEUTRAL_DIST, MAX_DIST],
    we lerp the cost modifier between [1.0, MAX_DIST_COST_MODIFIER] The below values
    represent (pixel distance / INFLUENCE_DISTANCE_DIVISOR) distance to capital that
    results in a cost modifier of 1.0'
INFLUENCE_NEUTRAL_DIST_CORE:
  def: '6.0'
  type: float
  cmt: distance to nearest core state that results in a cost modifier of 1.0
INFLUENCE_NEUTRAL_DIST_CONTROLLED:
  def: '14.0'
  type: float
  cmt: distance to nearest controlled state that results in a cost modifier of 1.0
INFLUENCE_MIN_DIST_COST_MODIFIER:
  def: '0.70'
  type: float
  cmt: Cost modifier at min (zero) distance
INFLUENCE_RATIO_CAPITAL:
  def: '0.05'
  type: float
  cmt: Ratio of influence based on distance to capital
INFLUENCE_RATIO_CONTROLLED:
  def: '0.5'
  type: float
  cmt: Ratio of influence based on distance to neared controlled territory (including
    uncontested peace conference bids)
INFLUENCE_PER_ADJACENCY:
  def: '0.05'
  type: float
  cmt: How much influence to add per uncontested adjacent state in the PC (blob, don't
    snake)
INFLUENCE_MINOR_FACTOR:
  def: '1.0'
  type: float
  cmt: How much influence discount an AI minor will get (inverse)
BASE_IMPROVE_RELATION_COST:
  def: '10'
  type: int
  cmt: Political power cost to initiate relation improvement
BASE_IMPROVE_RELATION_DIFFERENT_IDEOLOGY_GROUP_MAINTAIN_COST:
  def: '0.4'
  type: float
  cmt: Political power cost each update when boosting relations with nation of different
    ideology
BASE_SEND_ATTACHE_CP_COST:
  def: '50.0'
  type: float
  cmt: Command Power sent attache usage cost
WARGOAL_VERSUS_MAJOR_AT_WAR_REDUCTION:
  def: '-0.75'
  type: float
  cmt: reduction of pp cost for wargoal vs major at war.
WARGOAL_JUSTIFY_TENSION_FROM_PRODUCTION:
  def: '30.0'
  type: float
  cmt: Base value scaled by production capacity of country compared to biggest country
WARGOAL_PER_JUSTIFY_AND_WAR_COST_FACTOR:
  def: '1.5'
  type: float
  cmt: Cost factor per nation at war with or justifying against
BASE_BOOST_PARTY_POPULARITY_DAILY_PP:
  def: '0.25'
  type: float
  cmt: Daily pp cost for boost party popularity
BASE_STAGE_COUP_DAILY_PP:
  def: '0.5'
  type: float
  cmt: Daily pp cost for staging a coup
NAP_EXPIRY_MONTHS:
  def: '48'
  type: int
  cmt: NAPs expire after this many months
NAP_FORCE_BALANCE_RULE_MONTHS:
  def: '6'
  type: int
  cmt: The NAP border force balance rule changes with this interval
NAP_BREAK_FORCE_BALANCE_2:
  def: '1.0'
  type: float
  cmt: 1-1 brigades along the border required to break NAP
VERY_GOOD_OPINION:
  def: '50'
  type: int
  cmt: Threshold for a country that has a very good opinion of you.
DIPLOMACY_HOURS_BETWEEN_REQUESTS:
  def: '24'
  type: int
  cmt: How long a country must wait before sending a new diplomatic request.
FLEET_FEAR:
  def: '1'
  type: int
  cmt: Impact on troops on borders when deciding how willing a nation is to trade
VOLUNTEERS_PER_TARGET_PROVINCE:
  def: '0.05'
  type: float
  cmt: Each province owned by the target country contributes this amount of volunteers
    to the limit.
VOLUNTEERS_RETURN_EQUIPMENT:
  def: '0.95'
  type: float
  cmt: Returning volunteers keep this much equipment
VOLUNTEERS_DIVISIONS_REQUIRED:
  def: '30'
  type: int
  cmt: This many divisons are required for the country to be able to send volunteers.
TENSION_CIVIL_WAR_IMPACT:
  def: '0.2'
  type: float
  cmt: civil war multiplier on tension.
TENSION_CB_WAR:
  def: '7'
  type: int
  cmt: Amount of tension generated by a war with a CB
TENSION_ANNEX_CLAIM:
  def: '0.5'
  type: float
  cmt: Amount of tension generated by annexing a state you DO have claims on
TENSION_PUPPET:
  def: '1.25'
  type: float
  cmt: Amount of tension generated by puppeting (per state)
TENSION_VOLUNTEER_FORCE_DIVISION:
  def: '0.2'
  type: float
  cmt: Amount of tension generated for each sent division
TENSION_SIZE_FACTOR:
  def: '1.0'
  type: float
  cmt: All action tension values are multiplied by this value
TENSION_TIME_SCALE_MONTHLY_FACTOR:
  def: '-0.005'
  type: float
  cmt: Timed tension scale will be modified by this amount starting with TENSION_TIME_SCALE_START_DATE
TENSION_GUARANTEE:
  def: '-5'
  type: int
TENSION_JOIN_ATTACKER:
  def: '2'
  type: int
  cmt: scale of the amount of tension added when country joins attacker side
TENSION_LIBERATE:
  def: '-1'
  type: int
  cmt: Amount of tension generated by liberating a country.
TENSION_DEMILITARIZE_ZONE:
  def: '0.25'
  type: float
  cmt: Amount of tension generated by stacking demilitarize zone on 1 state, multiplied
    with the state base threat
TENSION_RESOURCE_RIGHTS:
  def: '0.25'
  type: float
  cmt: Amount of tension generated by stacking resource rights on 1 state, multiplied
    with the state base threat
TENSION_CAPITULATE:
  def: '0.40'
  type: float
  cmt: Scale of the amount of tension created by a countries capitulation.
REVOKE_GUARANTEE_COST:
  def: '25'
  type: int
BASE_CONDITIONAL_PEACE_MONTHS:
  def: '3'
  type: int
  cmt: War length must be before a surrender is possible.
BREAKING_GUARANTEE_PENALTY:
  def: '0.2'
  type: float
  cmt: War support penalty for breaking guarantee
PEACE_SCORE_RESET_LOW_SCORE_THRESHOLD:
  def: '0.05'
  type: float
  cmt: Winners with less than this ratio of war participation will give all their
    score to other players
PEACE_SCORE_SCALE_FACTOR:
  def: '1.35'
  type: float
  cmt: Losers' total value times this factor becomes the default total peace conference
    score that is distributed to the winners.
PEACE_SCORE_DISTRIBUTION:
  def: '{ 0.2, 0.2, 0.2, 0.2, 0.2 }'
  type: array
  cmt: 'Example: If 2000 score is distributed to winners this turn and this value
    is set to 0.05, each winner will receive a minimum of 100 score (clamped by the
    max score they will receive over the cource of the conference). How much of the
    total peace conference score you get during the first n turns.'
PEACE_PLAY_SOUND_ON_NEW_TURN:
  def: 'true'
  type: bool
  cmt: Whether the 'peace_conference_new_turn' audio hook is called or not
MAX_REMEMBERED_LEASED_IC:
  def: '1000'
  type: int
  cmt: Maximum of leased equipment value that is remembered for opinion bonus
MONTHLY_LEASED_IC_DECAY:
  def: '35'
  type: int
  cmt: How much of leased equipment is being "forgot" each month
MAX_OPINION_FROM_VOLUNTEERS:
  def: '30'
  type: int
  cmt: Opinion bonus per one sent volunteer division
NOT_READY_FOR_WAR_BASE:
  def: '-50'
  type: int
  cmt: AI should be unwilling to enter accept a call to war if not ready for war against
    the relevant enemies.
NOT_READY_FOR_WAR_VAL_PER_DAY_SINCE_CALL:
  def: '1'
  type: int
  cmt: Value modifying the not ready base over time.
RESOURCE_SENT_AUTONOMY_DAILY_BASE:
  def: '0.0'
  type: float
  cmt: If puppet provides resources to its master they increasy their autonomy by
    at least this amount
WAR_SCORE_AUTONOMY_BASE:
  def: '0.0'
  type: float
  cmt: Value added if any war score is contributed by puppet
LL_TO_OVERLORD_AUTONOMY_DAILY_BASE:
  def: '0.0'
  type: float
  cmt: If puppet lend leases equipment to overlord of at least same tech level as
    they have, they gain autonomy
LL_TO_PUPPET_AUTONOMY_DAILY_BASE:
  def: '0.0'
  type: float
  cmt: If overlord lend leases equipment to puppet of higher tech level as they have,
    puppet losses autonomy
AUTONOMY_FREEDOM_FROM_CAPITULATE:
  def: '0.5'
  type: float
  cmt: if overlord capitulate you get this
ATTACHE_TO_OVERLORD_EFFECT:
  def: '0.05'
  type: float
  cmt: If subject sent attaches to the overlord it gains autonomy
AUTONOMY_LEVEL_CHANGE_PP_COST_BASE:
  def: '50.0'
  type: float
  cmt: Base cost of changing level of autonomy
AUTONOMY_LEVEL_CHANGE_PP_FREE:
  def: '300'
  type: int
  cmt: Break free cost
MASTER_BUILD_AUTONOMY_FACTOR:
  def: '-0.7'
  type: float
  cmt: scales autonomy gain from construction by this
VICTORY_POINT_WORTH_FACTOR_WARSCORE:
  def: '0.2'
  type: float
  cmt: multiplier for each victory points when calculating province worth for warscore
CAPITAL_CAPITULATE_BONUS_SCORE:
  def: '150'
  type: int
  cmt: extra bonus when deciding who to capitulate to (applied to capital holder)
IDEOLOGY_JOIN_FACTION_MIN_LEVEL:
  def: '0.3'
  type: float
  cmt: ideology limit required to join faction
LICENSE_ACCEPTANCE_OPINION_FACTOR:
  def: '0.4'
  type: float
  cmt: Opinion modifier for acceptance of license production requests.
LICENSE_ACCEPTANCE_TECH_DIFFERENCE:
  def: '2'
  type: int
  cmt: Acceptance modifier for each year of technology difference.
LICENSE_ACCEPTANCE_SAME_FACTION:
  def: '20'
  type: int
  cmt: Acceptance modifier for being in the same faction
WARGOAL_COST_DOCKING_RIGHTS:
  def: '-0.2'
  type: float
  cmt: cost modifier to wargoaljustification for dockign rights
ASSUME_FACTION_LEADERSHIP_PP_COST:
  def: '200'
  type: int
  cmt: Political power cost to assume faction leadership
ASSUME_FACTION_LEADERSHIP_MIN_FACTORY_RATIO:
  def: '1.5'
  type: float
  cmt: The minimum ratio of factories that a country must have compared to the current
    leader in order to assume leadership.
ASSUME_FACTION_SPYMASTER_COOLDOWN_DAYS:
  def: '180'
  type: int
  cmt: Number of days after change of Spy Master before another country is allowed
    to become Spy Master.
FACTION_LEADERSHIP_CHANGE_NOT_SUBJECT_WEIGHT:
  def: '2'
  type: int
  cmt: Importance of subject status when determining how close a faction member is
    to being able to assume leadership.
FACTION_LEADERSHIP_CHANGE_IN_ALL_WARS_WEIGHT:
  def: '1'
  type: int
  cmt: Importance not being in all faction leader wars when determining how close
    a faction member is to being able to assume leadership.
FACTION_LEADERSHIP_CHANGE_MANPOWER_WEIGHT:
  def: '2'
  type: int
  cmt: Importance of manpower in field when determining how close a faction member
    is to being able to assume leadership.
EMBARGO_COST:
  def: '100'
  type: int
  cmt: One-time cost
EMBARGO_THREAT_THRESHOLD:
  def: '30'
  type: int
  cmt: Target-generated threat threshold to allow embargo (affected by modifiers)
EMBARGO_DIFFERENT_IDEOLOGY_AI_WEIGHT:
  def: '15'
  type: int
  cmt: AI weight for different ideology
EMBARGO_RECIPIENT_IS_MAJOR_AI_WEIGHT:
  def: '10'
  type: int
  cmt: Ai weight for recipient being major
EQUIPMENT_PURCHASE_ACCEPTANCE_OPINION:
  def: '1.1'
  type: float
  cmt: Acceptance factor for opinion
EQUIPMENT_PURCHASE_ACCEPTANCE_SCRIPTED_IDEOLOGY_ACCEPTANCE:
  def: '1.0'
  type: float
  cmt: Acceptance factor for scripted ideology acceptance modifier
EQUIPMENT_PURCHASE_ACCEPTANCE_COMPETING_FACTIONS:
  def: '-30'
  type: int
  cmt: Acceptance value added if both countries are in factions, and factions are
    different
EQUIPMENT_PURCHASE_ACCEPTANCE_NON_AGGRESSION_PACT:
  def: '25'
  type: int
  cmt: Acceptance value added if there is a non-aggression pact between the countries
MARKET_ACCESS_ACCEPTANCE_SAME_IDEOLOGY:
  def: '15'
  type: int
  cmt: Acceptance value added if same ideology
MARKET_ACCESS_ACCEPTANCE_TRADE_INFLUENCE:
  def: '0.70'
  type: float
  cmt: Acceptance factor for trade influence (adjusted from base value)
MARKET_ACCESS_ACCEPTANCE_EMBARGO:
  def: '-200'
  type: int
  cmt: Acceptance value added if either side has embargoed the other
MARKET_ACCESS_ACCEPTANCE_NON_AGGRESSION_PACT:
  def: '25'
  type: int
  cmt: Acceptance value added if there is a non-aggression pact between the countries
```
