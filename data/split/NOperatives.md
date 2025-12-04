```yaml
AGENCY_CREATION_DAYS:
  def: '30'
  type: int
  cmt: Number of days needed to create an intelligence agency
AGENCY_CREATION_FACTORIES:
  def: '5'
  type: int
  cmt: Number of factories used to create an intelligence agency
AGENCY_AI_PER_UPGRADE_FACTORIES:
  def: '6.0'
  type: float
  cmt: 'Used by AI to pace the upgrades. Formula : if( AGENCY_AI_BASE_NUM_FACTORIES
    <= num_civ_factories - num_upgrades * AGENCY_AI_PER_UPGRADE_FACTORIES )'
MAX_OPERATIVE_SLOT_FROM_AGENCY_UPGRADES:
  def: '1'
  type: int
  cmt: max operative slots gained from upgrades
BECOME_SPYMASTER_PP_COST:
  def: '50'
  type: int
  cmt: Number of political power used to become Spy Master
BASE_COUNTER_INTELLIGENCE_RATING:
  def: '0.0'
  type: float
  cmt: Base national counter intelligence rating for all countries
INTEL_NETWORK_GAIN_RATE_ON_WRONG_CONTROLLER:
  def: '-10.0'
  type: float
  cmt: Amount of network strength lost in a state when it does not have the right
    controller anymore
INTEL_NETWORK_GAIN_FROM_ADJACENCY_FACTOR:
  def: '0.5'
  type: float
  cmt: Factor multiplied to the sum of the positive difference between a state's strength
    and its neighbors'. In other words, how strongly neighbors impact the strength
    gained in a state. Values greater or equal to 1 are discouraged.
INTEL_NETWORK_STRENGTH_TARGET_OFFSET_PER_OPERATIVE:
  def: '15.0'
  type: float
  cmt: The amount of strength each operative on build intel network mission in a sub
    network add to the base target network strength
INTEL_NETWORK_BASE_STRENGTH_TARGET_COUNTERINTELLIGENCE_FACTOR:
  def: '-10.0'
  type: float
  cmt: BaseStrengthTarget = Factor * CounterIntelligenceRating + Offset
INTEL_NETWORK_MIN_VP_TO_TARGET:
  def: '15'
  type: int
  cmt: The minimum value of the highest VP in a state to consider the state as a valid
    target to start building an intel network
INTEL_NETWORK_MIN_STRENGTH_TO_LINK_SUBNETWORKS:
  def: '0.0'
  type: float
  cmt: Where the influence of two operative meet, the two nodes on each side have
    to have strictly more than the given strength before the two operatives have a
    chance of being considered in the same network
INTEL_NETWORK_MIN_STRENGTH_FOR_STATE_TO_COUNT_TOWARD_NATIONAL_COVERAGE:
  def: '0.0'
  type: float
  cmt: Amount of strength (0, 100) in a state required for it to count toward the
    national coverage
INTEL_NETWORK_NATIONAL_COVERAGE_CORE_STATES_WEIGHT:
  def: '0.6'
  type: float
  cmt: Weight (expected [0,1]) multiplied by the number of states covered by the network
    that are core to the target over the total number of states the target has for
    core
INTEL_NETWORK_OCCUPIED_TAG_STATES_WEIGHT:
  def: '0.5'
  type: float
  cmt: Weight (expected [0,1]) multiplied to the fraction of number of state covered
    by the intel network divided by the number of states occupied by the target of
    the network, per occupied tag
INTEL_NETWORK_MIN_SUB_NETWORK_SIZE_FOR_DETECTION:
  def: '0'
  type: int
  cmt: minimum number of state of a sub-intel network before an operative on build
    intel network mission in this network can be detected
INTEL_NETWORK_MIN_SUB_NETWORK_NATIONAL_COVERAGE_FOR_DETECTION:
  def: '0.01'
  type: float
  cmt: '[0, 1] minimum national coverage of the network the operative on build intel
    network is in to have a chance to be discovered'
INTEL_NETWORK_INTELLIGENCE_AGENCY_DEFENSE_TO_DETECTION_FACTOR:
  def: '2.0'
  type: float
  cmt: multiplied to the intelligence agency defense of the target of the intel network
INTEL_NETWORK_MAX_INTELLIGENCE_AGENCY_DEFENSE_DETECTION_SCALE_FACTOR:
  def: '1.0'
  type: float
  cmt: clamp the value from the multiplication of the above factor (expect a value
    greater or equal to 1)
INTEL_NETWORK_SUB_NETWORK_STRENGTH_TO_DETECTION_CHANCE_FACTOR:
  def: '0.1'
  type: float
  cmt: multiplied to the network strength (a value in range [0, 100]
INTEL_NETWORK_DETECTION_GLOBAL_FACTOR:
  def: '0.01'
  type: float
  cmt: global factor multiplied to the detection chance before it is multiplied a
    dice roll in the range [0,1000)
QUIET_INTEL_NETWORK_DAILY_XP_GAIN:
  def: '0'
  type: int
OPERATIVE_SLOTS_FROM_FACTION_MEMBERS_FOR_SPY_MASTER:
  def: '{ 0.0, 0.0, 0.25, 10.0, 0.5, 50.0 }'
  type: array
  cmt: used for calculating how many operatives will a spy master gain from its faction
    members first number in every now is number of operatives gained second number
    is total factory needed (mil and civ) for giving previous ratio 0 operative for
    [0, 10) 0.25 operative for [10, 50) 0.5 operative for >= 50
INTEL_NETWORK_MIN_DEFAULT_FOR_SHOWING:
  def: '25'
  type: int
  cmt: default min level for networks used to filter operation requirements if not
    overriden
OPERATIVE_MAX_INTEL_NETWORK_GAIN:
  def: '-1.0'
  type: float
  cmt: Max amount of network strength gain per day provided by an operative after
    modifiers have been applied (negative value means no max)
COUNTER_INTELLIGENCE_STACKING_FACTOR:
  def: '0.5'
  type: float
  cmt: 'Multiplier applied to each operative after the first one. So if we have the
    following counter intelligence rating values [ 0.1, 0.3, 0.2 ], the factor is
    applied twice for the lowest value and once for the 2nd lowest one as such : [
    0.3, 0.2 * D, 0.1 * D * D ] and then the result is summed up to give the final
    rating value'
COUNTER_INTELLIGENCE_TO_DEFENSE_DIVISOR:
  def: '1.0'
  type: float
  cmt: see above
BOOST_IDEOLOGY_NATIONAL_COVERAGE_FACTOR:
  def: '1.0'
  type: float
  cmt: 'used to compute the drift factor as follow: BASE * SUB_NETWORK_NC * BOOST_IDEOLOGY_DEFENSE_FACTOR'
BOOST_IDEOLOGY_DRIFT_STACKING_FACTOR:
  def: '0.5'
  type: float
  cmt: 'multiplied to the drift of an operative for each operative after the first
    one, with the greatest drift. So if we have the following drift values [ 0.1,
    0.3, 0.2 ], the factor is applied twice for the lowest value and once for the
    2nd lowest one as such : [ 0.3, 0.2 * D, 0.1 * D * D ] and then the result is
    summed up to give the final drift value.'
BOOST_IDEOLOGY_DAILY_XP_GAIN:
  def: '0.274'
  type: float
OPERATIVE_BASE_BOOST_IDEOLOGY:
  def: '0.1'
  type: float
  cmt: Base amount of daily ideology drift provoked by an operative
PROPAGANDA_SUB_NETWORK_STRENGTH_FACTOR:
  def: '1.0'
  type: float
  cmt: Multiplied to the network strength before being multiplied to the Stability/WarSupport
    drift caused by an operative
PROPAGANDA_OPERATIVE_STACKING_FACTOR:
  def: '0.5'
  type: float
  cmt: Multiplied to the Stability/WarSupport drift values of each operative after
    the one with the greatest values. The process is done separatly for Stability
    and WarSupport
PROPAGANDA_DAILY_XP_GAIN:
  def: '0.350'
  type: float
ROOT_OUT_RESISTANCE_STACKING_FACTOR:
  def: '0.5'
  type: float
  cmt: Multiplied to each operative efficiency after the first one
ROOT_OUT_RESISTANCE_DAILY_XP_GAIN:
  def: '0.068'
  type: float
CONTROL_TRADE_STACKING_FACTOR:
  def: '0.5'
  type: float
  cmt: Multiplied to the drift of each operative after the first one
CONTROL_TRADE_INFLUENCE_DAILY_DECAY:
  def: '0.1'
  type: float
  cmt: The amount of trade influence lost when no operative are assigned to the mission
OPERATIVE_BASE_DIPLOMATIC_PRESSURE_AI_ACCEPTANCE_SCORE_DRIFT:
  def: '0.4'
  type: float
  cmt: The daily change in the amount of opinion requiered to join a faction
DIPLOMATIC_PRESSURE_MAX_AI_ACCEPTANCE_SCORE_INCREASE:
  def: '20.0'
  type: float
  cmt: the maximum amount of ai acceptance score from diplomatic pressure
DIPLOMATIC_PRESSURE_OPERATIVE_STACKING_FACTOR:
  def: '0.5'
  type: float
  cmt: 'The diminishing return factor to apply to operative working for the same faction
    after the first one. Operatives operating for a same faction are ranked by their
    efficiency and their opinion and tension drift are individually applyied a stacking
    factor like so: DRIFT * STACKING_FACTOR^RANK where RANK is a value from 0 to the
    number of operative -1 where the opperative with the highest drift value has rank
    0'
DIPLOMATIC_PRESSURE_TENSION_REQUIREMENTS_DECAY:
  def: '0.001'
  type: float
MIN_NATIONAL_COVERAGE_FOR_BOOST_IDEOLOGY:
  def: '0.01'
  type: float
  cmt: Minimum network coverage required to start the mission (the code ensures that
    a network exists at all)
OPERATIVE_MIN_DAYS_HARMED:
  def: '30'
  type: int
  cmt: Minimum number of days an operative can be harmed. Applied after modifiers.
    Can be zero.
OPERATIVE_MIN_DAYS_FORCED_INTO_HIDING:
  def: '7'
  type: int
  cmt: Minimum number of days an operative can be forced into hiding. Applied after
    modifiers. Can be zero.
OPERATIVE_MAX_DAYS_TO_AUTO_RESUME_MISSION:
  def: '30'
  type: int
  cmt: Maximum number of days an operative has to be disabled before its mission is
    not automatically resumed once he is available again
CRYPTO_BASE_CRYPTO_LEVEL:
  def: '12000'
  type: int
  cmt: base crypto strength for a country
CRYPTO_CRYPTO_ACTIVE_BONUS_DURATION:
  def: '30'
  type: int
  cmt: number of days the active decryption bonuses will be applied before enemy resets
    their intelligence
OPERATION_AI_MINIMUM_SCORE:
  def: '10.0'
  type: float
  cmt: Once an operation's AI weight falls below the minimum score it will be scrapped
    if it is being prepared
OPERATIVE_CAPTURE_DURATION_IN_DAYS:
  def: 9*30
  type: mixed
DEFAULT_OPERATION_TIME_MULTIPLIER:
  def: '0.0'
  type: float
BOOST_IDEOLOGY_NETWORK_MISSION_ACTIVITY_INDICATOR_FACTOR:
  def: '10'
  type: int
CONTROL_TRADE_NETWORK_MISSION_ACTIVITY_INDICATOR_FACTOR:
  def: '1'
  type: int
INTEL_NETWORK_COVERAGE_ACTIVITY_FACTOR:
  def: '100'
  type: int
  cmt: multiplied to the sum of the network coverage [0,1] all countries have over
    the target
ACTIVITY_LEVEL_PROPORTIONAL_FACTOR:
  def: '0.01'
  type: float
  cmt: Activity level PID values
ACTIVITY_LEVEL_DERIVATIVE_FACTOR:
  def: '0'
  type: int
DANGER_LEVEL_INTEGRAL_FACTOR:
  def: '0.001'
  type: float
NUM_DAYS_BEFORE_REMOVING_PREPARED_OPERATIONS:
  def: '60'
  type: int
  cmt: num days before removing prepared operations
ON_CAPTURE_COUNTERINTELLIGENCE_OPERATIVE_WEIGHT_OWN_COUNTRY_FOR_XP:
  def: '2'
  type: int
  cmt: An integer on how likely an operative operating in his own country is to get
    selected for the xp reward on enemy operative capture
RISK_LEVELS:
  def: '{ 0.1, 0.2, 0.3 }'
  type: array
  cmt: risk and outcome texts. each number array should match its labels in size,
    but its ok to have different amount of risk levels than outcomes each risk level
    comes with a label to display for operations if it goes abve that number. If below
    the first it will isntead show the good outcomes
OUTCOME_LEVELS:
  def: '{ 0.0, 0.2, 0.3 }'
  type: array
  cmt: outcome levels are shown if risk is below its first entry instead
TECH_STEAL_EQUIPMENT_FACTOR:
  def: '4'
  type: int
```
