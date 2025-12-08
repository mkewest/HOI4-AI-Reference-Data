---
domain: defines_list
concept: NCountry
version: 1.17.2
requires: [defines]
relates: [states, country_history]
---

```yaml
EVENT_PROCESS_OFFSET:
  def: '20'
  type: int
  cmt: Events are checked every X day per country or state (1 is ideal, but CPU heavy)
BASE_RESEARCH_SLOTS:
  def: '2'
  type: int
  cmt: Base number of research slots per country.
POPULATION_YEARLY_GROWTH_BASE:
  def: '0.015'
  type: float
  cmt: basic population growth per year, used for monthly manpower gain
RESISTANCE_STRENGTH_FROM_VP:
  def: '0.001'
  type: float
  cmt: How much strength ticking speed gives each VP score.
RESISTANCE_STRENGTH_FROM_NEIGHBORS:
  def: '0.5'
  type: float
  cmt: Multiplies how much resistance can spread from one state to its neighbors, a
    state will spread whatever is highest of its victorypoints resistance increase or
    half of any of its neighbors spread, multiplied by this
RESISTANCE_DECAY_WHEN_NO_GROWTH:
  def: '0.005'
  type: float
  cmt: Resistance will fall by this much each day if there is nothing increasing it ( no
    VPs and no spread from neighbors )
REINFORCEMENT_DIVISION_PRIORITY_COUNT:
  def: '3'
  type: int
  cmt: How many priority stages we have in division template? 0)Reserves, 1)Normal,
    2)Elite.
REINFORCEMENT_DIVISION_PRIORITY_DEFAULT:
  def: '1'
  type: int
  cmt: Each template by default is 1)Normal
REINFORCEMENT_THEATER_GROUP_PRIORITY_DEFAULT:
  def: '1'
  type: int
  cmt: Each theater group by default is 1)Normal
REINFORCEMENT_THEATRE_PRIORITY_COUNT:
  def: '3'
  type: int
  cmt: Same as with divisions...
REINFORCEMENT_THEATRE_PRIORITY_DEFAULT:
  def: '1'
  type: int
REINFORCEMENT_AIRBASE_PRIORITY_COUNT:
  def: '3'
  type: int
REINFORCEMENT_AIRBASE_PRIORITY_DEFAULT:
  def: '1'
  type: int
REINFORCEMENT_DELIVERY_SPEED_MIN:
  def: '0.6'
  type: float
  cmt: The distance from the supply region to capital should affect the speed only a
    little bit. Main factor for penalty is overcrowded areas, and not the route length.
REINFORCEMENT_EQUIPMENT_DELIVERY_SPEED:
  def: '0.3'
  type: float
  cmt: Modifier for army equipment reinforcement speed
REINFORCEMENT_MANPOWER_DELIVERY_SPEED:
  def: '10.0'
  type: float
  cmt: Modifier for army manpower reinforcement delivery speed (travel time)
REINFORCEMENT_MANPOWER_CHUNK:
  def: '0.1'
  type: float
  cmt: Chunk size of manpower reinforcement delivery, in % of total manpower needed by
    the template.
EQUIPMENT_UPGRADE_CHUNK_MAX_SIZE:
  def: '10'
  type: int
  cmt: Maximum chunk size of equipment upgrade distribution per update.
COUNTRY_SCORE_MULTIPLIER:
  def: '1.0'
  type: float
  cmt: Weight of the country score.
ARMY_SCORE_MULTIPLIER:
  def: '0.15'
  type: float
  cmt: Based on number of armies.
NAVY_SCORE_MULTIPLIER:
  def: '1.0'
  type: float
  cmt: Based on number of navies.
AIR_SCORE_MULTIPLIER:
  def: '0.1'
  type: float
  cmt: Based on number of planes (which is typically a lot).
INDUSTRY_SCORE_MULTIPLIER:
  def: '1.0'
  type: float
  cmt: Based on number of factories.
PROVINCE_SCORE_MULTIPLIER:
  def: '0.1'
  type: float
  cmt: Based on number of controlled provinces.
NUCLEAR_BOMB_DROP_WAR_SUPPORT_EFFECT_MAX_INFRA:
  def: '0.2'
  type: float
  cmt: Reduce enemy national war support on nuking a province, the value scales with
    infrastructure up to this number
NUCLEAR_BOMB_DROP_WAR_SUPPORT_EFFECT_MAX_VP:
  def: '3'
  type: int
  cmt: War support will be scaled down if there's less VP than this in the province
THERMONUCLEAR_BOMB_DROP_WAR_SUPPORT_EFFECT_MAX_INFRA:
  def: '0.2'
  type: float
  cmt: Reduce enemy national war support on nuking a province, the value scales with
    infrastructure up to this number
THERMONUCLEAR_BOMB_DROP_WAR_SUPPORT_EFFECT_MAX_VP:
  def: '3'
  type: int
  cmt: War support will be scaled down if there's less VP than this in the province
WEEKLY_STABILITY_GAIN:
  def: '0.0'
  type: float
WEEKLY_WAR_SUPPORT_GAIN:
  def: '0.0'
  type: float
SUPPLY_CONVOY_FACTOR:
  def: '0.25'
  type: float
  cmt: How many convoys each supply needs
CONVOY_RANGE_FACTOR:
  def: '1'
  type: int
  cmt: How much range affects convoy need for resource trades and supply
CONVOY_LENDLEASE_RANGE_FACTOR:
  def: '1'
  type: int
  cmt: How much range affects convoy need for lend lease
CONVOY_INTERNATIONAL_MARKET_RANGE_FACTOR:
  def: '1'
  type: int
  cmt: How much range affects convoy need for international market
NAVY_USE_HOME_BASE_FOR_RANGE:
  def: 'true'
  type: bool
  cmt: If true, will calculate task force range from home base, otherwise will calculate
    from any friendly naval base
CONVOY_CONTROLLED_ROUTE_COST_REDUCTION_FACTOR:
  def: '0.25'
  type: float
  cmt: How much fewer convoys you need shipping through areas you control
LOCAL_MANPOWER_ACCESSIBLE_NON_CORE_FACTOR:
  def: '0.02'
  type: float
  cmt: accessible recruitable factor base
MAX_NON_CORE_MANPOWER_FACTOR:
  def: '1.0'
  type: float
  cmt: max clamp for recruitable local non core manpower factor for states
DEFAULT_STABILITY:
  def: '0.5'
  type: float
  cmt: Default stability if not scripted otherwise.
DEFAULT_WAR_SUPPORT:
  def: '0.5'
  type: float
  cmt: Default war support if not scripted otherwise.
BASE_STABILITY_WAR_FACTOR:
  def: '-0.2'
  type: float
  cmt: Default stability war factor
BASE_STABILITY_PARTY_POPULARITY_FACTOR:
  def: '0.15'
  type: float
  cmt: Default stability rulling party popularity factor
DEFAULT_COASTAL_PROTECTION_STABILITY:
  def: '0.1'
  type: float
  cmt: Default stability when the coastal states are fully protected
MIN_COUP_STABILITY_FACTOR:
  def: '0.0'
  type: float
  cmt: Min value of coup factor in stability
MAX_COUP_STABILITY_FACTOR:
  def: '2.0'
  type: float
  cmt: Max value of coup factor in stability
MIN_COUP_SUCCESS_STABILITY:
  def: '0.8'
  type: float
  cmt: Max stability when coup will happen
WAR_SUPPORT_OFFNSIVE_WAR:
  def: '-0.2'
  type: float
  cmt: Impact of being in offensive war
WAR_SUPPORT_DEFENSIVE_WAR:
  def: '0.2'
  type: float
  cmt: Impact of being in defensive war
WAR_SUPPORT_TENSION_IMPACT:
  def: '0.4'
  type: float
  cmt: Total impact of world tension
MIN_STABILITY:
  def: '0.0'
  type: float
MAX_STABILITY:
  def: '1.0'
  type: float
MIN_WAR_SUPPORT:
  def: '0.0'
  type: float
MAX_WAR_SUPPORT:
  def: '1.0'
  type: float
FRONT_PROVINCE_SCORE:
  def: '20'
  type: int
  cmt: Max province score of a front. Used for the hostile troop alert
MAJOR_IC_RATIO:
  def: '3'
  type: int
  cmt: difference in total factories needed to be considered major with respect to other
    nation
MAJOR_MIN_FACTORIES:
  def: '35'
  type: int
  cmt: need at least these many factories to become a major
MAX_INTELLIGENCE_DIFFERENCE:
  def: '10.0'
  type: float
  cmt: (Old Intel) Max difference in intelligence levels between countries
INTEL_FROM_ALLIANCE_FACTOR:
  def: '0.3'
  type: float
  cmt: Multiplied to the difference between a country intel and the maximum value in the
    alliance to compute the amount of intel that flows from the alliance to that
    country. 0 means no alliance contribution, 1 means a country intel's is the same as
    the max in the alliance.
MAX_INTELLIGENCE_DATA_DEVIATION:
  def: '1.0'
  type: float
  cmt: (Old Intel) Max deviation in estimating default espionage values ( 0.0 - 1.0 )
MAX_INTELLIGENCE_MILITARY_DATA_DEVIATION:
  def: '1.0'
  type: float
  cmt: (Old Intel) Max deviation in estimating enemy military units amount ( 0.0 - 1.0 )
MAX_INTELLIGENCE_NAVY_DATA_DEVIATION:
  def: '0.3'
  type: float
  cmt: (Old Intel) Max deviation in estimating enemy ships amount ( 0.0 - 1.0 )
MAX_INTELLIGENCE_AIR_DATA_DEVIATION:
  def: '1.0'
  type: float
  cmt: (Old Intel) Max deviation in estimating enemy air planes amount ( 0.0 - 1.0 )
MAX_INTELLIGENCE_CONVOY_DATA_DEVIATION:
  def: '0.3'
  type: float
  cmt: (Old Intel) Max deviation in estimating enemy convoys amount ( 0.0 - 1.0 )
MAX_INTELLIGENCE_MANPOWER_DATA_DEVIATION:
  def: '0.4'
  type: float
  cmt: (Old Intel) Max deviation in estimating enemy total manpower amount ( 0.0 - 1.0 )
MAX_INTELLIGENCE_FIELDED_MANPOWER_DATA_DEVIATION:
  def: '0.35'
  type: float
  cmt: (Old Intel) Max deviation in estimating enemy fielded manpower amount ( 0.0 - 1.0
    )
MAX_INTELLIGENCE_INDUSTRY_DATA_DEVIATION:
  def: '0,4'
  type: string
  cmt: (Old Intel) Max deviation in estimating enemy total industry
MIN_MANPOWER_RATIO:
  def: '0.15'
  type: float
  cmt: Min manpower ratio to show manpower alert
ARMY_IMPORTANCE_FACTOR:
  def: '5.0'
  type: float
  cmt: Army factor for AI and calculations
TERRAIN_IMPORTANCE_FACTOR:
  def: '5.0'
  type: float
  cmt: Terrain base factor for state strategic value
VICTORY_POINTS_IMPORTANCE_FACTOR:
  def: '5.0'
  type: float
  cmt: State victory points importance factor for AI and calculations
BUILDING_IMPORTANCE_FACTOR:
  def: '3.0'
  type: float
  cmt: State building importance factor for AI and calculations
RESOURCE_IMPORTANCE_FACTOR:
  def: '1.0'
  type: float
  cmt: State resource importance factor for AI and calculations
INTERPOLATED_FRONT_STEPS_SHORT:
  def: '2'
  type: int
  cmt: Performance optimization - The amount of steps for interpolated fronts. Non-AI
    countries got full interpolated fronts, the rest has optimized version of it.
MIN_AIR_RESERVE_RATIO:
  def: '0.33'
  type: float
  cmt: Min manpower ratio to show air reserves alert
POLITICAL_POWER_LOWER_CAP:
  def: '-500.0'
  type: float
  cmt: Min amount of political power country should have
POLITICAL_POWER_UPPER_CAP:
  def: '2000.0'
  type: float
  cmt: Max amount of political power country should have
RESISTANCE_IMPORTANT_LEVEL:
  def: '0.25'
  type: float
  cmt: Level when resistance becomes dangerous
RESISTANCE_IMPORTANT_COUNTRY_LEVEL:
  def: '0.25'
  type: float
  cmt: Level when average resistance in a country becomes dangerous
MIN_MAJOR_COUNTRIES:
  def: '7'
  type: int
  cmt: MIN_MAJOR_COUNTRIES countries with most factories will be considered as major
    countries
ADDITIONAL_MAJOR_COUNTRIES_IC_RATIO:
  def: '0.7'
  type: float
  cmt: Countries will also be considered major when having more factories that the
    average of top MIN_MAJOR_COUNTRIES countries' factories times
    ADDITIONAL_MAJOR_COUNTRIES_IC_RATIO
BASE_TENSION_MAJOR_COUNTRY_INDEX:
  def: '1'
  type: int
  cmt: Which major country should be considered the base country when scaling generated
    world tension. 0 is the country with the most factories, 1 is the second most-
    factories country etc. This number has to be lower than MIN_MAJOR_COUNTRIES
MIN_NAVAL_SUPPLY_EFFICIENCY:
  def: '0.1'
  type: float
  cmt: Min ratio when supplies will be considered delivered from the capital by naval
    path
PARADROP_AIR_SUPERIORITY_RATIO:
  def: '0.7'
  type: float
  cmt: Min ratio of air superiority for paradropping
STATE_VALUE_BASE:
  def: '10.0'
  type: float
  cmt: Base value of a state (value is used to determine costs in e.g. peace
    conferences)
STATE_VALUE_BUILDING_SLOTS_MULT:
  def: '4.0'
  type: float
  cmt: The value of each building slot in a state
STATE_VALUE_MANPOWER_FACTOR:
  def: '0.1'
  type: float
  cmt: State cost increases with this for every 10k population (so 3.1M becomes 310 and
    then multiplied by this)
INVASION_REPORT_EXPERATION_DAYS:
  def: '30'
  type: int
  cmt: Invasion experation days
MIN_FOCUSES_FOR_CONTINUOUS:
  def: '10'
  type: int
  cmt: Focuses needed to unlock continuous focuses
AUTONOMOUS_TOTAL_SCORE:
  def: '5000'
  type: int
  cmt: Total score for autonomous scale
AUTONOMOUS_SPILLOVER:
  def: '0.025'
  type: float
  cmt: Total score that can be saved to reach next level
CIVIL_WAR_INVOLVEMENT_MIN_TENSION:
  def: '0.5'
  type: float
  cmt: base value of world tension to involve other sides to the civil war
UNCAPITULATE_LEVEL:
  def: '0.1'
  type: float
  cmt: if we reclaim this much and our capital we reset capitulate status
BASE_SURRENDER_LIMIT:
  def: '0.8'
  type: float
  cmt: Base level of occupation required for country surrender
SURRENDER_LIMIT_MULT_FOR_COUNTRIES_WITH_NO_CORES:
  def: '0.7'
  type: float
  cmt: Countries with no owned cores will their surrender level multiplied by this
    amount
MIN_SURRENDER_LIMIT:
  def: '0.2'
  type: float
  cmt: Minimum non-forced surrender limit. valid 0-1
BASE_MOBILIZATION_SPEED:
  def: '0.01'
  type: float
  cmt: Base speed of manpower mobilization  #in 1/1000 of 1 %
INTERCEPTION_WAR_SUPPORT_SCALE:
  def: '0.00001'
  type: float
  cmt: Scaling of interceptions to war support impact
INTERCEPTION_BOMBING_WAR_SUPPORT_IMPACT:
  def: '0.3'
  type: float
  cmt: Max impact of interceptions on the war support
BOMBING_WAR_SUPPORT_PENALTY_SCALE:
  def: '-0.00015'
  type: float
  cmt: Scaling of bomber damage to war support impact, will be added weekly as a war
    support penalty
MAX_BOMBING_WEEKLY_WAR_SUPPORT_PENALTY:
  def: '-0.006'
  type: float
  cmt: Max penalty that will gained per week from bomber's damage
BOMBING_WEEKLY_WAR_SUPPORT_PENALTY_DECAY:
  def: '0.001'
  type: float
  cmt: Weekly decay of bomber damage war support penalty
MAX_BOMBING_WAR_SUPPORT_IMPACT:
  def: '-0.3'
  type: float
  cmt: Max total penalty from bomber's damage
HEROES_BEING_KILLED_WAR_SUPPORT_PENALTY_SCALE:
  def: '-0.03'
  type: float
  cmt: Scaling of war heroes manpower lost to war support impact, will be added weekly
    as a war support penalty
MAX_HEROES_BEING_KILLED_WEEKLY_WAR_SUPPORT_PENALTY:
  def: '-0.006'
  type: float
  cmt: Max penalty that will gained per week from war heroes manpower lost
HEROES_BEING_KILLED_WEEKLY_WAR_SUPPORT_PENALTY_DECAY:
  def: '0.001'
  type: float
  cmt: Weekly decay of war heroes manpower lost war support penalty
MAX_HEROES_BEING_KILLED_WAR_SUPPORT_IMPACT:
  def: '-0.3'
  type: float
  cmt: Max total penalty from war heroes manpower lost
WAR_SUPPORT_FROM_CASUALTIES:
  def: '0.025'
  type: float
  cmt: Base value (inverted) for calculating heroes being killed
CONVOYS_BEING_RAIDED_WAR_SUPPORT_PENALTY_SCALE:
  def: '-0.05'
  type: float
  cmt: Scaling of trade convoy raided to war support impact, will be added weekly as a
    war support penalty
MAX_CONVOYS_BEING_RAIDED_WEEKLY_WAR_SUPPORT_PENALTY:
  def: '-0.006'
  type: float
  cmt: Max penalty that will gained per week from trade convoy raided
CONVOYS_BEING_RAIDED_WEEKLY_WAR_SUPPORT_PENALTY_DECAY:
  def: '0.001'
  type: float
  cmt: Weekly decay of trade convoy raided war support penalty
MAX_CONVOYS_BEING_RAIDED_WAR_SUPPORT_IMPACT:
  def: '-0.5'
  type: float
  cmt: Max total penalty from trade convoy raided
FEMALE_UNIT_LEADER_BASE_CHANCE:
  def:
    - [0.5]  # country leaders
    - [0.5]  # army leaders
    - [0.5]  # navy leaders
    - [0.5]  # air leaders
    - [0.5]  # operatives
    - [0.5]  # scientists
  type: table
CONVOYS_SUNK_MULTIPLIER_FOR_WAR_SUPPORT:
  def: '0.2'
  type: float
  cmt: once a trade convoy ship sunk, you will get a larger negative impact on your war
    support
CONVOYS_BEING_RAIDED_DAILY_WAR_SUPPORT_IMPACT_FROM_OVERSEA_STATES:
  def: '0.2'
  type: float
  cmt: resource transfer convoys convoys from our states being raided will give a daily
    war support penalty depending on how important that resource is and how inefficent
    convoys are
CONVOYS_SUNK_MULTIPLIER_FOR_WAR_SUPPORT_FROM_OVERSEA_STATES:
  def: '0.2'
  type: float
  cmt: once a resource transfer convoys from our states ship sunk, you will get a larger
    negative impact on your war support
CONVOYS_BEING_RAIDED_DAILY_WAR_SUPPORT_IMPACT:
  def: '0.2'
  type: float
  cmt: trade convoys being raided will give a daily war support penalty depending on how
    important that resource is and how inefficent convoys are
MAX_PROPAGANDA_STABILITY_IMPACT:
  def: '-0.2'
  type: float
  cmt: Max total penalty from operative performing the propaganda mission in a country
MAX_PROPAGANDA_WAR_SUPPORT_IMPACT:
  def: '-0.2'
  type: float
  cmt: Max total penalty from operative performing the propaganda mission in a country
PROPAGANDA_STABILITY_DAILY_DECAY:
  def: '0.001'
  type: float
  cmt: Amount of stability recovered daily from propaganda effort
PROPAGANDA_WAR_SUPPORT_DAILY_DECAY:
  def: '0.001'
  type: float
  cmt: Amount of war support recovered daily from war support effort
NUM_DAYS_TO_FULLY_DELETE_STOCKPILED_EQUIPMENT:
  def: '90'
  type: int
  cmt: time in days to fully delete equipments from stockpile. when you delete an
    equipment, they go to a temporary hidden pool which still can be seized
AIR_SUPPLY_CONVERSION_SCALE:
  def: '0.01'
  type: float
  cmt: Conversion scale for planes to air supply
AIR_SUPPLY_DROP_EXPIRATION_HOURS:
  def: '168'
  type: int
  cmt: Air drop length after being dropped
STARTING_COMMAND_POWER:
  def: '0.0'
  type: float
  cmt: starting command power for every country
BASE_MAX_COMMAND_POWER:
  def: '80.0'
  type: float
  cmt: base value for maximum command power
BASE_COMMAND_POWER_GAIN:
  def: '0.4'
  type: float
  cmt: base value for daily command power gain
AIR_VOLUNTEER_PLANES_RATIO:
  def: '0.2'
  type: float
  cmt: Ratio for volunteer planes available for sending in relation to sender air force
AIR_VOLUNTEER_BASES_CAPACITY_LIMIT:
  def: '0.1'
  type: float
  cmt: Ratio for volunteer planes available for sending in relation to receiver air base
    capacity
ATTACHE_XP_SHARE:
  def: '0.15'
  type: float
  cmt: Country received xp from attaches
SPECIAL_FORCES_CAP_BASE:
  def: '0.05'
  type: float
  cmt: Max ammount of special forces battalions is total number of non-special forces
    battalions multiplied by this and modified by a country modifier
SPECIAL_FORCES_CAP_MIN:
  def: '24'
  type: int
  cmt: You can have a minimum of this many special forces battalions, regardless of the
    number of non-special forces battalions you have, this can also be modified by a
    country modifier
DAYS_OF_WAR_BEFORE_SURRENDER:
  def: '7'
  type: int
  cmt: Number of days a war has to have existed before anyone can surrender in it
FUEL_LEASE_CONVOY_RATIO:
  def: '0.0005'
  type: float
  cmt: num convoys needed per fuel land lease
STARTING_FUEL_RATIO:
  def: '0.25'
  type: float
  cmt: starting fuel ratio compared to max fuel for countries
BASE_FUEL_GAIN_PER_OIL:
  def: '2'
  type: int
  cmt: base amount of fuel gained hourly per excess oil
BASE_FUEL_GAIN:
  def: '2.0'
  type: float
  cmt: base amount of fuel gained hourly, independent of excess oil
BASE_FUEL_CAPACITY:
  def: '50000'
  type: int
  cmt: base amount of fuel capacity
SCORCHED_EARTH_STATE_COST:
  def: '5'
  type: int
  cmt: pp cost to scorch a state
COUNTRY_MANPOWER_CAPITULATED_FREE_POOL_FACTOR:
  def: '0.1'
  type: float
  cmt: Factor on amount of normal manpower left for an exiled nation with no territory.
COUNTRY_MANPOWER_CAPITULATED_CORE_GAIN_FACTOR:
  def: '0.001'
  type: float
  cmt: Factor on amount of normal manpower gained for the exile nation. From owned
    states that are controlled by an enemy. State manpower reduced by factor 1000 in
    code.
COUNTRY_MANPOWER_CAPITULATED_NON_CORE_GAIN_FACTOR:
  def: '0.001'
  type: float
  cmt: Factor on amount of normal manpower gained for the exile nation. From owned
    states that are controlled by an enemy. State manpower reduced by factor 1000 in
    code.
GIE_MAX_LEGITIMACY:
  def: '100'
  type: int
  cmt: Legitimacy max of a GiE
GIE_CAPITULATE_MAX_STOCKPILE_TRANSFER:
  def: '0.1'
  type: float
  cmt: 0-1 Transfers ratio of stockpile. from 0 to this define depending on starting
    legitimacy on capitulation.
GIE_CAPITULATE_MIN_LEGIT_FOR_TRANSFER:
  def: '5'
  type: int
  cmt: 0-100 Minimum starting legitimacy to transfer any equipment at all.
GIE_CAPITULATION_LEGITIMACY_WARSCORE_FACTOR:
  def: '0.5'
  type: float
  cmt: Multiplies war contribution percent with this factor for part of starting
    legitimacy. (0.5 would mean a 50 % war contribution gives 25 more legitimacy)
GIE_CAPITULATION_LEGITIMACY_WARLENGTH_FACTOR:
  def: '1.0'
  type: float
  cmt: Multiplies war length (nr of weeks) with this factor for part of starting
    legitimacy. (1.0 would mean a war length of 30 weeks gives 30 more legitimacy)
GIE_WARSCORE_GAIN_LEGITIMACY_FACTOR:
  def: '1'
  type: int
  cmt: Factor on how much legitimacy is gained from warscore earned by GiE units.
GIE_HOST_CIC_FROM_LEGITIMACY_MAX:
  def: '5'
  type: int
  cmt: Host will receive from 0 to this value in CIC.
GIE_HOST_MIC_FROM_LEGITIMACY_MAX:
  def: '5'
  type: int
  cmt: Host will receive from 0 to this value in MIC.
GIE_HOST_DOCKYARDS_FROM_LEGITIMACY_MAX:
  def: '0'
  type: int
  cmt: Host will receive from 0 to this value in dockyards.
GIE_VETERAN_MANPOWER_NON_CORE_GAIN_FACTOR:
  def: '0.005'
  type: float
  cmt: Factor on amount of manpower gained from owned states that are controlled by an
    enemy. State manpower reduced by factor 1000 in code.
GIE_VETERAN_MANPOWER_CORE_GAIN_FACTOR:
  def: '0.01'
  type: float
  cmt: Factor on amount of manpower gained from owned states that are controlled by an
    enemy. State manpower reduced by factor 1000 in code.
GIE_MANPOWER_TOTAL_MAX_FACTOR:
  def: '0.5'
  type: float
  cmt: Factor on max amount of exile manpower that can be gained from owned states.
    Approaching this will give diminishing returns. Reduced by factor 100 in code.
GIE_MANPOWER_RATO_OF_MAX_START_PENALTY:
  def: '0.5'
  type: float
  cmt: When this ratio of max manpower has been recruited we start applying the penalty.
GIE_MANPOWER_GAIN_PENALTY_MAX:
  def: '0.95'
  type: float
  cmt: Max penalty on exile manpower growth.
GIE_EXILE_AIR_RECRUITMENT_LEGITIMACY:
  def: '50'
  type: int
  cmt: Legitimacy required to recruit exile airwings
GIE_EXILE_AIR_START_EXPERIENCE:
  def: '3'
  type: int
  cmt: Starting experience for exile airwings
GIE_EXILE_TROOP_RECRUITMENT_LEGITIMACY:
  def: '25'
  type: int
  cmt: Legitimacy required to recruit exile troops
GIE_EXILE_TROOPS_DEPLOY_TRAINING_MAX_LEVEL:
  def: '2'
  type: int
  cmt: Max XP exile troops can receive from training
GIE_EXILE_ARMY_LEADER_LEGITIMACY_LEVELS:
  def:
    - [30]
    - [60]
    - [90]
  type: table
  cmt: Legitimacy levels where a new army leader is received.
GIE_EXILE_ARMY_LEADER_START_LEVEL:
  def: '3'
  type: int
  cmt: Starting level for exile leader
GIE_ESCAPING_DIVISIONS_TRANSFER_DAYS:
  def: '30'
  type: int
  cmt: days to transfer escaping divisions to host nation
GIE_ESCAPING_DIVISIONS_XP_BOOST:
  def: '0.4'
  type: float
  cmt: Escaping divisions gain a boost to experience. Only the toughest motherbadasses
    will band together and survive to git me one hundred Nazi scalps ... Or die
    tryin'...
GIE_DIVISION_ATTACK_BONUS_AGAINST_OCCUPIER:
  def: '0.1'
  type: float
  cmt: Attack bonus factor against whoever occupies your core territory.
GIE_DIVISION_DEFENSE_BONUS_AGAINST_OCCUPIER:
  def: '0.1'
  type: float
  cmt: Attack bonus factor against whoever occupies your core territory.
GIE_DIVISION_ATTACK_BONUS_ON_CORE:
  def: '0.1'
  type: float
  cmt: Attack bonus factor when fighting on cores.
GIE_DIVISION_DEFENSE_BONUS_ON_CORE:
  def: '0.1'
  type: float
  cmt: Defense bonus factor when fighting on cores.
GIE_ESCAPING_DIVISIONS_EQUIPMENT_RATIO:
  def: '0.2'
  type: float
  cmt: Base equipment ratio on escaped troops.
GIE_ESCAPING_DIVISIONS_AMOUNT_RATIO:
  def: '0.1'
  type: float
  cmt: Ratio on amount of divisions that escapes. Scales with starting legitimacy
GIE_LIBERATED_NATION_DAILY_LEGITIMACY_CHANGE:
  def: '-1.5'
  type: float
  cmt: An uncapitulated exile that is fully liberated will have legitimacy changed with
    this amount daily. Will be automatically reinstated when it reaches 0.
GIE_EXILE_TRANSFER_ON_LEADER_CAPITULATION_MANPOWER_FACTOR:
  def: '0.1'
  type: float
  cmt: Factor on exile manpower kept when a faction leader capitulates and the hosted
    exiles are transfered.
GIE_CONVOY_ON_CREATION:
  def: '10'
  type: int
  cmt: Number of convoy a GiE will get on creation.
SURRENDER_LIMIT_REDUCTION_PER_COLLABORATION:
  def: '0.15'
  type: float
  cmt: each percent of collaboration will lower surrender limit by this percentage
SURRENDER_RECIPIENT_SCORE_PER_COLLABORATION:
  def: '1.0'
  type: float
  cmt: countries with collaboration will get bonus while game calculates which country
    the enemy will capitulate
COMPLIANCE_PER_COLLABORATION:
  def: '1.0'
  type: float
  cmt: each percent of collaboration will be converted to this compliance at
    capitulation
WILL_LEAD_TO_WAR_FOCUS_PERSISTENCE:
  def: '60'
  type: int
  cmt: taken focuses that has lead to war will still make ai prep for war for this many
    days after being taken
WILL_LEAD_TO_WAR_DECISION_PERSISTENCE:
  def: '30'
  type: int
  cmt: the decision thats lead to war will sitll make ai prep for war for this many days
    after being taken/cooldown/timeout
ARMY_COUNT_DAILY_LERP_FOR_TRAINING_XP:
  def: '0.002'
  type: float
  cmt: number of armies that is used in training xp calculates daily lerps to actual
    number (if real number is lower)
ARMY_COUNT_DAILY_DECREASE_FOR_TRAINING_XP:
  def: '0.1'
  type: float
  cmt: number of armies that is used in training xp calculates daily linearly approaches
    this number (if real number is lower)
```
