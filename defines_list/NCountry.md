```yaml
EVENT_PROCESS_OFFSET:
  def: '20'
  type: int
  cmt: Events are checked every X day per country or state (1 is ideal, but CPU heavy)
POPULATION_YEARLY_GROWTH_BASE:
  def: '0.015'
  type: float
  cmt: basic population growth per year, used for monthly manpower gain
RESISTANCE_STRENGTH_FROM_NEIGHBORS:
  def: '0.5'
  type: float
  cmt: Multiplies how much resistance can spread from one state to its neighbors,
    a state will spread whatever is highest of its victorypoints resistance increase
    or half of any of its neighbors spread, multiplied by this
REINFORCEMENT_DIVISION_PRIORITY_COUNT:
  def: '3'
  type: int
  cmt: How many priority stages we have in division template? 0)Reserves, 1)Normal,
    2)Elite.
REINFORCEMENT_THEATER_GROUP_PRIORITY_DEFAULT:
  def: '1'
  type: int
  cmt: Each theater group by default is 1)Normal
REINFORCEMENT_THEATRE_PRIORITY_DEFAULT:
  def: '1'
  type: int
REINFORCEMENT_AIRBASE_PRIORITY_DEFAULT:
  def: '1'
  type: int
REINFORCEMENT_EQUIPMENT_DELIVERY_SPEED:
  def: '0.3'
  type: float
  cmt: Modifier for army equipment reinforcement speed
REINFORCEMENT_MANPOWER_CHUNK:
  def: '0.1'
  type: float
  cmt: Chunk size of manpower reinforcement delivery, in % of total manpower needed
    by the template.
COUNTRY_SCORE_MULTIPLIER:
  def: '1.0'
  type: float
  cmt: Weight of the country score.
NAVY_SCORE_MULTIPLIER:
  def: '1.0'
  type: float
  cmt: Based on number of navies.
INDUSTRY_SCORE_MULTIPLIER:
  def: '1.0'
  type: float
  cmt: Based on number of factories.
NUCLEAR_BOMB_DROP_WAR_SUPPORT_EFFECT_MAX_INFRA:
  def: '0.2'
  type: float
  cmt: Reduce enemy national war support on nuking a province, the value scales with
    infrastructure up to this number
WEEKLY_STABILITY_GAIN:
  def: '0.0'
  type: float
SUPPLY_CONVOY_FACTOR:
  def: '0.25'
  type: float
  cmt: How many convoys each supply needs
CONVOY_LENDLEASE_RANGE_FACTOR:
  def: '1'
  type: int
  cmt: How much range affects convoy need for lend lease
LOCAL_MANPOWER_ACCESSIBLE_NON_CORE_FACTOR:
  def: '0.02'
  type: float
  cmt: accessible recruitable factor base
DEFAULT_STABILITY:
  def: '0.5'
  type: float
  cmt: Default stability if not scripted otherwise.
  use: Also used for calculating the modifiers applied to the country with the stability_good_modifier
    and stability_bad_modifier [[static modifiers]], multiplying the relevant modifiers
    by \frac{|\text{Current Stability} - \text{DEFAULT STABILITY}|}{\text{DEFAULT
    STABILITY}}. Highly unstable on the low values and completely disables the modifier
    if set to 0.
DEFAULT_WAR_SUPPORT:
  def: '0.5'
  type: float
  cmt: Default war support if not scripted otherwise.
  use: Also used for calculating the modifiers applied to the country with the war_support_good_modifier
    and war_support_bad_modifier [[static modifiers]], multiplying the relevant modifiers
    by \frac{|\text{Current War Support} - \text{DEFAULT WAR SUPPORT}|}{\text{DEFAULT
    WAR SUPPORT} }. Highly unstable on the low values and completely disables the
    modifier if set to 0.
BASE_STABILITY_WAR_FACTOR:
  def: '-0.2'
  type: float
  cmt: Default stability war factor
MIN_COUP_STABILITY_FACTOR:
  def: '0.0'
  type: float
  cmt: Min value of coup factor in stability
MIN_COUP_SUCCESS_STABILITY:
  def: '0.8'
  type: float
  cmt: Max stability when coup will happen
WAR_SUPPORT_DEFENSIVE_WAR:
  def: '0.2'
  type: float
  cmt: Impact of being in defensive war
MIN_STABILITY:
  def: '0.0'
  type: float
MIN_WAR_SUPPORT:
  def: '0.0'
  type: float
FRONT_PROVINCE_SCORE:
  def: '20'
  type: int
  cmt: Max province score of a front. Used for the hostile troop alert
MAJOR_MIN_FACTORIES:
  def: '35'
  type: int
  cmt: need at least these many factories to become a major
INTEL_FROM_ALLIANCE_FACTOR:
  def: '0.3'
  type: float
  cmt: Multiplied to the difference between a country intel and the maximum value
    in the alliance to compute the amount of intel that flows from the alliance to
    that country. 0 means no alliance contribution, 1 means a country intel's is the
    same as the max in the alliance.
MAX_INTELLIGENCE_MILITARY_DATA_DEVIATION:
  def: '1.0'
  type: float
  cmt: (Old Intel) Max deviation in estimating enemy military units amount ( 0.0 -
    1.0 )
MAX_INTELLIGENCE_AIR_DATA_DEVIATION:
  def: '1.0'
  type: float
  cmt: (Old Intel) Max deviation in estimating enemy air planes amount ( 0.0 - 1.0
    )
MAX_INTELLIGENCE_MANPOWER_DATA_DEVIATION:
  def: '0.4'
  type: float
  cmt: (Old Intel) Max deviation in estimating enemy total manpower amount ( 0.0 -
    1.0 )
MAX_INTELLIGENCE_INDUSTRY_DATA_DEVIATION:
  def: '0.4'
  type: float
  cmt: (Old Intel) Max deviation in estimating enemy total industry
ARMY_IMPORTANCE_FACTOR:
  def: '5.0'
  type: float
  cmt: Army factor for AI and calculations
VICTORY_POINTS_IMPORTANCE_FACTOR:
  def: '5.0'
  type: float
  cmt: State victory points importance factor for AI and calculations
RESOURCE_IMPORTANCE_FACTOR:
  def: '1.0'
  type: float
  cmt: State resource importance factor for AI and calculations
MIN_AIR_RESERVE_RATIO:
  def: '0.33'
  type: float
  cmt: Min manpower ratio to show air reserves alert
POLITICAL_POWER_UPPER_CAP:
  def: '2000.0'
  type: float
  cmt: Max amount of political power country should have
RESISTANCE_IMPORTANT_COUNTRY_LEVEL:
  def: '0.25'
  type: float
  cmt: Level when average resistance in a country becomes dangerous
ADDITIONAL_MAJOR_COUNTRIES_IC_RATIO:
  def: '0.7'
  type: float
  cmt: Countries will also be considered major when having more factories that the
    average of top MIN_MAJOR_COUNTRIES countries' factories times ADDITIONAL_MAJOR_COUNTRIES_IC_RATIO
MIN_NAVAL_SUPPLY_EFFICIENCY:
  def: '0.1'
  type: float
  cmt: Min ratio when supplies will be considered delivered from the capital by naval
    path
STATE_VALUE_BASE:
  def: '10.0'
  type: float
  cmt: Base value of a state (value is used to determine costs in e.g. peace conferences)
STATE_VALUE_MANPOWER_FACTOR:
  def: '0.1'
  type: float
  cmt: State cost increases with this for every 10k population (so 3.1M becomes 310
    and then multiplied by this)
MIN_FOCUSES_FOR_CONTINUOUS:
  def: '10'
  type: int
  cmt: Focuses needed to unlock continuous focuses
AUTONOMOUS_SPILLOVER:
  def: '0.025'
  type: float
  cmt: Total score that can be saved to reach next level
UNCAPITULATE_LEVEL:
  def: '0.1'
  type: float
  cmt: if we reclaim this much and our capital we reset capitulate status
SURRENDER_LIMIT_MULT_FOR_COUNTRIES_WITH_NO_CORES:
  def: '0.7'
  type: float
  cmt: Countries with no owned cores will their surrender level multiplied by this
    amount
BASE_MOBILIZATION_SPEED:
  def: '0.01'
  type: float
  cmt: 'Base speed of manpower mobilization  #in 1/1000 of 1 %'
INTERCEPTION_BOMBING_WAR_SUPPORT_IMPACT:
  def: '0.3'
  type: float
  cmt: Max impact of interceptions on the war support
MAX_BOMBING_WEEKLY_WAR_SUPPORT_PENALTY:
  def: '-0.006'
  type: float
  cmt: Max penalty that will gained per week from bomber's damage
MAX_BOMBING_WAR_SUPPORT_IMPACT:
  def: '-0.3'
  type: float
  cmt: Max total penalty from bomber's damage
MAX_HEROES_BEING_KILLED_WEEKLY_WAR_SUPPORT_PENALTY:
  def: '-0.006'
  type: float
  cmt: Max penalty that will gained per week from war heroes manpower lost
MAX_HEROES_BEING_KILLED_WAR_SUPPORT_IMPACT:
  def: '-0.3'
  type: float
  cmt: Max total penalty from war heroes manpower lost
CONVOYS_BEING_RAIDED_WAR_SUPPORT_PENALTY_SCALE:
  def: '-0.05'
  type: float
  cmt: Scaling of trade convoy raided to war support impact, will be added weekly
    as a war support penalty
CONVOYS_BEING_RAIDED_WEEKLY_WAR_SUPPORT_PENALTY_DECAY:
  def: '0.001'
  type: float
  cmt: Weekly decay of trade convoy raided war support penalty
FEMALE_UNIT_LEADER_BASE_CHANCE:
  def: '{ 0.5, 0.5, 0.5, 0.5, 0.5 }'
  type: array
  cmt: applies as a factor to female unit leader randomization the values needs to
    be zero if you don't actually have random portraits country leaders army leaders
    navy leaders air leaders operatives
CONVOYS_BEING_RAIDED_DAILY_WAR_SUPPORT_IMPACT_FROM_OVERSEA_STATES:
  def: '0.2'
  type: float
  cmt: resource transfer convoys convoys from our states being raided will give a
    daily war support penalty depending on how important that resource is and how
    inefficent convoys are
CONVOYS_BEING_RAIDED_DAILY_WAR_SUPPORT_IMPACT:
  def: '0.2'
  type: float
  cmt: trade convoys being raided will give a daily war support penalty depending
    on how important that resource is and how inefficent convoys are
MAX_PROPAGANDA_WAR_SUPPORT_IMPACT:
  def: '-0.2'
  type: float
  cmt: Max total penalty from operative performing the propaganda mission in a country
PROPAGANDA_WAR_SUPPORT_DAILY_DECAY:
  def: '0.001'
  type: float
  cmt: Amount of war support recovered daily from war support effort
AIR_SUPPLY_CONVERSION_SCALE:
  def: '0.01'
  type: float
  cmt: Conversion scale for planes to air supply
STARTING_COMMAND_POWER:
  def: '0.0'
  type: float
  cmt: starting command power for every country
BASE_COMMAND_POWER_GAIN:
  def: '0.4'
  type: float
  cmt: base value for daily command power gain
AIR_VOLUNTEER_BASES_CAPACITY_LIMIT:
  def: '0.1'
  type: float
  cmt: Ratio for volunteer planes available for sending in relation to receiver air
    base capacity
SPECIAL_FORCES_CAP_BASE:
  def: '0.05'
  type: float
  cmt: Max ammount of special forces battalions is total number of non-special forces
    battalions multiplied by this and modified by a country modifier
DAYS_OF_WAR_BEFORE_SURRENDER:
  def: '7'
  type: int
  cmt: Number of days a war has to have existed before anyone can surrender in it
STARTING_FUEL_RATIO:
  def: '0.25'
  type: float
  cmt: starting fuel ratio compared to max fuel for countries
BASE_FUEL_GAIN:
  def: '2.0'
  type: float
  cmt: base amount of fuel gained hourly, independent of excess oil
SCORCHED_EARTH_STATE_COST:
  def: '5'
  type: int
  cmt: pp cost to scorch a state
COUNTRY_MANPOWER_CAPITULATED_CORE_GAIN_FACTOR:
  def: '0.001'
  type: float
  cmt: Factor on amount of normal manpower gained for the exile nation. From owned
    states that are controlled by an enemy. State manpower reduced by factor 1000
    in code.
GIE_MAX_LEGITIMACY:
  def: '100'
  type: int
  cmt: Legitimacy max of a GiE
GIE_CAPITULATE_MIN_LEGIT_FOR_TRANSFER:
  def: '5'
  type: int
  cmt: 0-100 Minimum starting legitimacy to transfer any equipment at all.
GIE_CAPITULATION_LEGITIMACY_WARLENGTH_FACTOR:
  def: '1.0'
  type: float
  cmt: Multiplies war length (nr of weeks) with this factor for part of starting legitimacy.
    (1.0 would mean a war length of 30 weeks gives 30 more legitimacy)
GIE_HOST_CIC_FROM_LEGITIMACY_MAX:
  def: '5'
  type: int
  cmt: Host will receive from 0 to this value in CIC.
GIE_HOST_DOCKYARDS_FROM_LEGITIMACY_MAX:
  def: '0'
  type: int
  cmt: Host will receive from 0 to this value in dockyards.
GIE_VETERAN_MANPOWER_CORE_GAIN_FACTOR:
  def: '0.01'
  type: float
  cmt: Factor on amount of manpower gained from owned states that are controlled by
    an enemy. State manpower reduced by factor 1000 in code.
GIE_MANPOWER_RATO_OF_MAX_START_PENALTY:
  def: '0.5'
  type: float
  cmt: When this ratio of max manpower has been recruited we start applying the penalty.
GIE_EXILE_AIR_RECRUITMENT_LEGITIMACY:
  def: '50'
  type: int
  cmt: Legitimacy required to recruit exile airwings
GIE_EXILE_TROOP_RECRUITMENT_LEGITIMACY:
  def: '25'
  type: int
  cmt: Legitimacy required to recruit exile troops
GIE_EXILE_ARMY_LEADER_LEGITIMACY_LEVELS:
  def: '{ 30, 60, 90 }'
  type: array
  cmt: Legitimacy levels where a new army leader is received.
GIE_ESCAPING_DIVISIONS_TRANSFER_DAYS:
  def: '30'
  type: int
  cmt: days to transfer escaping divisions to host nation
GIE_DIVISION_ATTACK_BONUS_AGAINST_OCCUPIER:
  def: '0.1'
  type: float
  cmt: Attack bonus factor against whoever occupies your core territory.
GIE_DIVISION_ATTACK_BONUS_ON_CORE:
  def: '0.1'
  type: float
  cmt: Attack bonus factor when fighting on cores.
GIE_ESCAPING_DIVISIONS_EQUIPMENT_RATIO:
  def: '0.2'
  type: float
  cmt: Base equipment ratio on escaped troops.
GIE_LIBERATED_NATION_DAILY_LEGITIMACY_CHANGE:
  def: '-1.5'
  type: float
  cmt: An uncapitulated exile that is fully liberated will have legitimacy changed
    with this amount daily. Will be automatically reinstated when it reaches 0.
GIE_CONVOY_ON_CREATION:
  def: '10'
  type: int
  cmt: Number of convoy a GiE will get on creation.
SURRENDER_RECIPIENT_SCORE_PER_COLLABORATION:
  def: '1.0'
  type: float
  cmt: countries with collaboration will get bonus while game calculates which country
    the enemy will capitulate
WILL_LEAD_TO_WAR_FOCUS_PERSISTENCE:
  def: '60'
  type: int
  cmt: taken focuses that has lead to war will still make ai prep for war for this
    many days after being taken
ARMY_COUNT_DAILY_LERP_FOR_TRAINING_XP:
  def: '0.002'
  type: float
  cmt: number of armies that is used in training xp calculates daily lerps to actual
    number (if real number is lower)
```
