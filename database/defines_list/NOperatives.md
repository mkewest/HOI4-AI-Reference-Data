---
domain: defines_list
concept: NOperatives
version: 1.17.2
requires: [defines]
relates: [operatives, intelligence]
---

```yaml
AGENCY_CREATION_DAYS:
  def: '30'
  type: int
  cmt: Number of days needed to create an intelligence agency
AGENCY_UPGRADE_DAYS:
  def: '30'
  type: int
  cmt: Number of days needed to upgrade an intelligence agency
AGENCY_CREATION_FACTORIES:
  def: '5'
  type: int
  cmt: Number of factories used to create an intelligence agency
AGENCY_AI_BASE_NUM_FACTORIES:
  def: '25.0'
  type: float
  cmt: Used by AI to pace the upgrades. Formula : if( AGENCY_AI_BASE_NUM_FACTORIES <=
    num_civ_factories - num_upgrades * AGENCY_AI_PER_UPGRADE_FACTORIES )
AGENCY_AI_PER_UPGRADE_FACTORIES:
  def: '6.0'
  type: float
  cmt: Used by AI to pace the upgrades. Formula : if( AGENCY_AI_BASE_NUM_FACTORIES <=
    num_civ_factories - num_upgrades * AGENCY_AI_PER_UPGRADE_FACTORIES )
AGENCY_UPGRADE_PER_OPERATIVE_SLOT:
  def: '5'
  type: int
  cmt: Number of upgrade needed to unlock an additional operative slot
MAX_OPERATIVE_SLOT_FROM_AGENCY_UPGRADES:
  def: '1'
  type: int
  cmt: max operative slots gained from upgrades
AGENCY_OPERATIVE_RECRUITMENT_TIME:
  def: '30'
  type: int
  cmt: Number of days to wait to have operative to recruit when an operative slot first
    becomes available
BECOME_SPYMASTER_PP_COST:
  def: '50'
  type: int
  cmt: Number of political power used to become Spy Master (only without faction dlc)
BECOME_SPYMASTER_FI_COST:
  def: '1'
  type: int
  cmt: Faction initiative used to become Spy Master (only with faction dlc)
BECOME_SPYMASTER_MIN_UPGRADES:
  def: '3'
  type: int
  cmt: Number of agency upgrades you need before becoming Spy Master
BASE_COUNTER_INTELLIGENCE_RATING:
  def: '0.0'
  type: float
  cmt: Base national counter intelligence rating for all countries
AGENCY_DEFENSE_EFFECT_ON_HOSTILE_ACTION_COST:
  def: '0.2'
  type: float
  cmt: Defense factor that is responsible for multiplying the cost hostile actions
    against our country by its level and this value
INTEL_NETWORK_GAIN_RATE_ON_WRONG_CONTROLLER:
  def: '-10.0'
  type: float
  cmt: Amount of network strength lost in a state when it does not have the right
    controller anymore
INTEL_NETWORK_GAIN_RATE_ON_OUT_OF_RANGE:
  def: '-1.75'
  type: float
  cmt: Amount of network strength lost in a state that has the right controller but is
    out of range of any operative
INTEL_NETWORK_GAIN_FROM_ADJACENCY_FACTOR:
  def: '0.5'
  type: float
  cmt: Factor multiplied to the sum of the positive difference between a state's
    strength and its neighbors'. In other words, how strongly neighbors impact the
    strength gained in a state. Values greater or equal to 1 are discouraged.
INTEL_NETWORK_GAIN_DECAY_PER_STEP_FACTOR:
  def: '0.5'
  type: float
  cmt: Factor multiplied to the gain of the previous node in the netowrk initially
    contributed by the agent. In other words, before adjacency, the strength gain in a
    state would be GainFromOperative * ( INTEL_NETWORK_GAIN_DECAY_PER_STEP_FACTOR ^
    NodeDepth ) where NodeDepth is the distance between the state and the operative's
    location.
INTEL_NETWORK_STRENGTH_TARGET_OFFSET_PER_OPERATIVE:
  def: '15.0'
  type: float
  cmt: The amount of strength each operative on build intel network mission in a sub
    network add to the base target network strength
INTEL_NETWORK_STRENGTH_DECAY_WHEN_ABOVE_TARGET:
  def: '-2.5'
  type: float
  cmt: The amount of strength removed each tick from a state that has more strength than
    the target
INTEL_NETWORK_BASE_STRENGTH_TARGET_COUNTERINTELLIGENCE_FACTOR:
  def: '-10.0'
  type: float
  cmt: BaseStrengthTarget = Factor * CounterIntelligenceRating + Offset
INTEL_NETWORK_BASE_STRENGTH_TARGET_COUNTERINTELLIGENCE_OFFSET:
  def: '90'
  type: int
  cmt: Offset mentioned above
INTEL_NETWORK_MIN_VP_TO_TARGET:
  def: '15'
  type: int
  cmt: The minimum value of the highest VP in a state to consider the state as a valid
    target to start building an intel network
INTEL_NETWORK_MIN_STRENGTH_TO_TARGET:
  def: '101.0'
  type: float
  cmt: The minimum value of the intel network in a state to consider it a valid target
    to deploy an operative in
INTEL_NETWORK_MIN_STRENGTH_TO_LINK_SUBNETWORKS:
  def: '0.0'
  type: float
  cmt: Where the influence of two operative meet, the two nodes on each side have to
    have strictly more than the given strength before the two operatives have a chance
    of being considered in the same network
INTEL_NETWORK_OPERATIVE_GAIN_STACKING_FACTOR:
  def: '0.5'
  type: float
  cmt: When multiple operative are present in the same location, this factor is applied
    for each operative with a lower gain than the max. So if operatives have the gain [
    3, 1, 2 ] in the same location, it is sorted to [ 1, 2, 3 ] then converted to [
    1*D^2, 2*D^1, 3 ], with D being this define, so if D=0.5 we have [ 0.25, 1, 3 ] and
    the final gain from operative at this location will be 4.25. Putting this define to
    0 is equivalent to considering the maximum value only.
INTEL_NETWORK_MIN_STRENGTH_FOR_STATE_TO_COUNT_TOWARD_NATIONAL_COVERAGE:
  def: '0.0'
  type: float
  cmt: Amount of strength (0, 100) in a state required for it to count toward the
    national coverage
INTEL_NETWORK_NATIONAL_COVERAGE_CONTROLLED_STATES_WEIGHT:
  def: '0.2'
  type: float
  cmt: Weight (expected [0,1]) multiplied by the number of states covered by the network
    that are controlled by the target over the total number of states the target
    controls
INTEL_NETWORK_NATIONAL_COVERAGE_CORE_STATES_WEIGHT:
  def: '0.6'
  type: float
  cmt: Weight (expected [0,1]) multiplied by the number of states covered by the network
    that are core to the target over the total number of states the target has for core
INTEL_NETWORK_NATIONAL_COVERAGE_OWNED_WORTH_WEIGHT:
  def: '0.2'
  type: float
  cmt: Weight (expected [0,1]) multiplied by the value of victory points covered by the
    network over the total value of victory points controlled by the targets
INTEL_NETWORK_OCCUPIED_TAG_STATES_WEIGHT:
  def: '0.5'
  type: float
  cmt: Weight (expected [0,1]) multiplied to the fraction of number of state covered by
    the intel network divided by the number of states occupied by the target of the
    network, per occupied tag
INTEL_NETWORK_OCCUPIED_TAG_WORTH_WEIGHT:
  def: '0.5'
  type: float
  cmt: Weight (expected [0,1]) multiplied to the fraction of victory points worth of
    states covered by the intel network divided by the worth of states occupied by the
    target of the network, per occupied tag
INTEL_NETWORK_MIN_SUB_NETWORK_SIZE_FOR_DETECTION:
  def: '0'
  type: int
  cmt: minimum number of state of a sub-intel network before an operative on build intel
    network mission in this network can be detected
INTEL_NETWORK_MIN_NATIONAL_COVERAGE_FOR_DETECTION:
  def: '0.02'
  type: float
  cmt: [0, 1] minimum national coverage required for an operative on build intel network
    to have a chance to be discovered
INTEL_NETWORK_MIN_SUB_NETWORK_NATIONAL_COVERAGE_FOR_DETECTION:
  def: '0.01'
  type: float
  cmt: [0, 1] minimum national coverage of the network the operative on build intel
    network is in to have a chance to be discovered
INTEL_NETWORK_MIN_SUB_NETWORK_STRENGTH_FOR_DETECTION:
  def: '10.0'
  type: float
  cmt: [0, 100] minimum network strength of the network the operative on build intel
    network mission is in to have a chance to be discovered
INTEL_NETWORK_INTELLIGENCE_AGENCY_DEFENSE_TO_DETECTION_FACTOR:
  def: '2.0'
  type: float
  cmt: multiplied to the intelligence agency defense of the target of the intel network
INTEL_NETWORK_INTELLIGENCE_AGENCY_DEFENSE_DETECTION_SCALE_FACTOR:
  def: '0.0'
  type: float
  cmt: factor multiplied to the intelligence agency defense of the target of the intel
    network before being factored to the detection chance
INTEL_NETWORK_MAX_INTELLIGENCE_AGENCY_DEFENSE_DETECTION_SCALE_FACTOR:
  def: '1.0'
  type: float
  cmt: clamp the value from the multiplication of the above factor (expect a value
    greater or equal to 1)
INTEL_NETWORK_NATIONAL_COVERAGE_TO_DETECTION_CHANCE_FACTOR:
  def: '1.0'
  type: float
  cmt: multiplied to the national coverage (a value in range [0, 1]
INTEL_NETWORK_SUB_NETWORK_STRENGTH_TO_DETECTION_CHANCE_FACTOR:
  def: '0.1'
  type: float
  cmt: multiplied to the network strength (a value in range [0, 100]
INTEL_NETWORK_SUB_NETWORK_NATIONAL_COVERAGE_TO_DETECTION_CHANCE_FACTOR:
  def: '3.0'
  type: float
  cmt: multiplied to the contribution to the national coverage of the sub network (a
    value in range [0, 1])
INTEL_NETWORK_DETECTION_GLOBAL_FACTOR:
  def: '0.01'
  type: float
  cmt: global factor multiplied to the detection chance before it is multiplied a dice
    roll in the range [0,1000)
BUILD_INTEL_NETWORK_DAILY_XP_GAIN:
  def: '1'
  type: int
QUIET_INTEL_NETWORK_DAILY_XP_GAIN:
  def: '0'
  type: int
OPERATIVE_MISSION_DETECTION_CHANCE_FACTOR:
  def:
    - [0.0]  # NoMission
    - [1.0]  # BuildIntelNetwork
    - [1.0]  # QuietIntelNetwork
    - [1.0]  # CounterIntelligence
    - [0.0]  # RootOutResistance
    - [3.0]  # BoostIdeology
    - [0.1]  # ControlTrade
    - [0.1]  # DiplomaticPressure
    - [3.0]  # Propaganda
  type: table
OPERATIVE_SLOTS_FROM_FACTION_MEMBERS_FOR_SPY_MASTER:
  def:
    - [0.0, 0.0]  # 0 operative for [0, 10)
    - [0.25, 10.0]  # 0.25 operative for [10, 50)
    - [0.5, 50.0]  # 0.5 operative for >= 50
  type: table
INTEL_NETWORK_STATE_MODIFIER_STRENGTH_THRESHOLD:
  def: '10'
  type: int
  cmt: Minimum amount of strength required in a state for the intel network related
    modifiers to start being applied
INTEL_NETWORK_MIN_DEFAULT_FOR_SHOWING:
  def: '25'
  type: int
  cmt: default min level for networks used to filter operation requirements if not
    overriden
OPERATIVE_BASE_INTEL_NETWORK_GAIN:
  def: '0.4'
  type: float
  cmt: Base amount of network strength gain per day provided by an operative
OPERATIVE_MAX_INTEL_NETWORK_GAIN:
  def: '-1.0'
  type: float
  cmt: Max amount of network strength gain per day provided by an operative after
    modifiers have been applied (negative value means no max)
COUNTER_INTELLIGENCE_FOREIGN_AGENT_FACTOR:
  def: '0.0'
  type: float
  cmt: Multiplier to the counter intelligence provided by foreign (ally) operatives
COUNTER_INTELLIGENCE_STACKING_FACTOR:
  def: '0.5'
  type: float
  cmt: Multiplier applied to each operative after the first one. So if we have the
    following counter intelligence rating values [ 0.1, 0.3, 0.2 ], the factor is
    applied twice for the lowest value and once for the 2nd lowest one as such : [ 0.3,
    0.2 * D, 0.1 * D * D ] and then the result is summed up to give the final rating
    value
COUNTER_INTELLIGENCE_TO_DEFENSE_LOG_FACTOR:
  def: '0.0'
  type: float
  cmt: Defense = LogFactor * log( 1 + CounterIntelligence ) + CounterIntelligence /
    Divisor
COUNTER_INTELLIGENCE_TO_DEFENSE_DIVISOR:
  def: '1.0'
  type: float
  cmt: see above
COUNTER_INTELLIGENCE_DAILY_XP_GAIN:
  def: '0.112'
  type: float
BOOST_IDEOLOGY_NATIONAL_COVERAGE_FACTOR:
  def: '1.0'
  type: float
  cmt: used to compute the drift factor as follow: BASE * SUB_NETWORK_NC *
    BOOST_IDEOLOGY_DEFENSE_FACTOR
BOOST_IDEOLOGY_MAX_DRIFT_BY_OPERATIVE:
  def: '0.25'
  type: float
  cmt: the maximum drift an operative can cause, a negative value means no maximum
BOOST_IDEOLOGY_DRIFT_STACKING_FACTOR:
  def: '0.5'
  type: float
  cmt: multiplied to the drift of an operative for each operative after the first one,
    with the greatest drift. So if we have the following drift values [ 0.1, 0.3, 0.2 ],
    the factor is applied twice for the lowest value and once for the 2nd lowest one as
    such : [ 0.3, 0.2 * D, 0.1 * D * D ] and then the result is summed up to give the
    final drift value.
BOOST_IDEOLOGY_DEFENSE_FACTOR:
  def: '0.2'
  type: float
  cmt: multiplied to the target's defense to get the amount of drift to remove from each
    operative's drift
BOOST_IDEOLOGY_DAILY_XP_GAIN:
  def: '0.274'
  type: float
OPERATIVE_BASE_INTEL_AGENCY_DEFENSE:
  def: '1.0'
  type: float
  cmt: Base amount of intel agency defense contributed by an operative on
    counter_intelligence mission
OPERATIVE_BASE_BOOST_IDEOLOGY:
  def: '0.1'
  type: float
  cmt: Base amount of daily ideology drift provoked by an operative
OPERATIVE_BASE_PROPAGANDA_POWER:
  def: '0.0005'
  type: float
  cmt: Base amount of daily war support and stability change when an operative is
    assigned to propaganda
PROPAGANDA_SUB_NETWORK_STRENGTH_FACTOR:
  def: '1.0'
  type: float
  cmt: Multiplied to the network strength before being multiplied to the
    Stability/WarSupport drift caused by an operative
PROPAGANDA_DEFENSE_FACTOR:
  def: '0.01'
  type: float
  cmt: Multiplied to the target's defense before being subtracted from the
    Stability/WarSupport drift caused by an operative
PROPAGANDA_OPERATIVE_STACKING_FACTOR:
  def: '0.5'
  type: float
  cmt: Multiplied to the Stability/WarSupport drift values of each operative after the
    one with the greatest values. The process is done separatly for Stability and
    WarSupport
PROPAGANDA_COUNTRY_STACKING_FACTOR:
  def: '0.5'
  type: float
  cmt: Multiplied to the Stability/WarSupport drift values of each country after the one
    with the greatest values. The process is done separatly for Stability and WarSupport
PROPAGANDA_DAILY_XP_GAIN:
  def: '0.350'
  type: float
OPERATIVE_BASE_ROOT_OUT_RESISTANCE_EFFICIENCY:
  def: '1.0'
  type: float
  cmt: The base efficiency of an operative at the RootOutResistance mission (this is a
    percentage, 1.0 == 100%)
ROOT_OUT_RESISTANCE_STACKING_FACTOR:
  def: '0.5'
  type: float
  cmt: Multiplied to each operative efficiency after the first one
ROOT_OUT_RESISTANCE_RANGE_STEP_FACTOR:
  def: '0.5'
  type: float
  cmt: Multiplied to the summed up efficiency from all operative operating in a same
    state to determine the efficiency in neighboring states
ROOT_OUT_RESISTANCE_DAILY_XP_GAIN:
  def: '0.068'
  type: float
OPERATIVE_BASE_CONTROL_TRADE_DRIFT:
  def: '0.5'
  type: float
  cmt: The base daily drift in trade influence caused by an operative
CONTROL_TRADE_STACKING_FACTOR:
  def: '0.5'
  type: float
  cmt: Multiplied to the drift of each operative after the first one
CONTROL_TRADE_MAX_INFLUENCE:
  def: '50.0'
  type: float
  cmt: The maximum amount of trade influence that can be gained through the control
    trade mission
CONTROL_TRADE_INFLUENCE_DAILY_DECAY:
  def: '0.1'
  type: float
  cmt: The amount of trade influence lost when no operative are assigned to the mission
CONTROL_TRADE_DAILY_XP_GAIN:
  def: '0.137'
  type: float
OPERATIVE_BASE_DIPLOMATIC_PRESSURE_AI_ACCEPTANCE_SCORE_DRIFT:
  def: '0.4'
  type: float
  cmt: The daily change in the amount of opinion requiered to join a faction
OPERATIVE_BASE_DIPLOMATIC_PRESSURE_TENSION_REQUIREMENTS_DRIFT:
  def: '0.001'
  type: float
  cmt: The daily change in world tension requiered to join a faction
DIPLOMATIC_PRESSURE_MAX_AI_ACCEPTANCE_SCORE_INCREASE:
  def: '20.0'
  type: float
  cmt: the maximum amount of ai acceptance score from diplomatic pressure
DIPLOMATIC_PRESSURE_MAX_TENSION_REQUIREMENTS_DECREASE:
  def: '0.20'
  type: float
  cmt: amount of tension (tensions is in range [0,1]) that can be removed from the
    requirements imposed by the modifier join_faction_tension_limit
DIPLOMATIC_PRESSURE_OPERATIVE_STACKING_FACTOR:
  def: '0.5'
  type: float
  cmt: The diminishing return factor to apply to operative working for the same faction
    after the first one. Operatives operating for a same faction are ranked by their
    efficiency and their opinion and tension drift are individually applyied a stacking
    factor like so: DRIFT * STACKING_FACTOR^RANK where RANK is a value from 0 to the
    number of operative -1 where the opperative with the highest drift value has rank 0
DIPLOMATIC_PRESSURE_AI_ACCEPTANCE_SCORE_DECAY:
  def: '0.4'
  type: float
  cmt: daily decay when the mission is not active
DIPLOMATIC_PRESSURE_TENSION_REQUIREMENTS_DECAY:
  def: '0.001'
  type: float
DIPLOMATIC_PRESSURE_DAILY_XP_GAIN:
  def: '0.137'
  type: float
MIN_NATIONAL_COVERAGE_FOR_BOOST_IDEOLOGY:
  def: '0.01'
  type: float
  cmt: Minimum network coverage required to start the mission (the code ensures that a
    network exists at all)
MIN_NATIONAL_COVERAGE_FOR_PROPAGANDA:
  def: '0.01'
  type: float
  cmt: Minimum network coverage required to start the mission (the code ensures that a
    network exists at all)
OPERATIVE_MIN_DAYS_HARMED:
  def: '30'
  type: int
  cmt: Minimum number of days an operative can be harmed. Applied after modifiers. Can
    be zero.
OPERATIVE_MAX_DAYS_HARMED:
  def: '120'
  type: int
  cmt: Maximum number of days an operative can be harmed. Applied after modifiers. Is
    ignored if negative
OPERATIVE_MIN_DAYS_FORCED_INTO_HIDING:
  def: '7'
  type: int
  cmt: Minimum number of days an operative can be forced into hiding. Applied after
    modifiers. Can be zero.
OPERATIVE_MAX_DAYS_FORCED_INTO_HIDING:
  def: '120'
  type: int
  cmt: Maximum number of days an operative can be forced into hiding. Applied after
    modifiers. Is ignored if negative
OPERATIVE_MAX_DAYS_TO_AUTO_RESUME_MISSION:
  def: '30'
  type: int
  cmt: Maximum number of days an operative has to be disabled before its mission is not
    automatically resumed once he is available again
MAX_RECRUITED_OPERATIVES:
  def: '10'
  type: int
CRYPTO_BASE_CRYPTO_LEVEL:
  def: '12000'
  type: int
  cmt: base crypto strength for a country
CRYPTO_CRYPTO_LEVEL_PER_CRYPTO_UPGRADE:
  def: '4250'
  type: int
  cmt: crypto strength per crypto upgrade
CRYPTO_CRYPTO_ACTIVE_BONUS_DURATION:
  def: '30'
  type: int
  cmt: number of days the active decryption bonuses will be applied before enemy resets
    their intelligence
CYRPTO_ACTIVE_BONUS_ACTIVATION_PROGRESS_RATIO:
  def: '0.5'
  type: float
  cmt: once bonus is activated, decryption progress will be reduced to this ratio
OPERATION_AI_MINIMUM_SCORE:
  def: '10.0'
  type: float
  cmt: Once an operation's AI weight falls below the minimum score it will be scrapped
    if it is being prepared
OPERATION_COMPLETION_XP:
  def: '18'
  type: int
OPERATIVE_CAPTURE_DURATION_IN_DAYS:
  def: '9*30'
  type: string
DEFAULT_OPERATION_COST_MULTIPLIER:
  def: '0.15'
  type: float
DEFAULT_OPERATION_TIME_MULTIPLIER:
  def: '0.0'
  type: float
BUILD_INTEL_NETWORK_MISSION_ACTIVITY_INDICATOR_FACTOR:
  def: '10'
  type: int
BOOST_IDEOLOGY_NETWORK_MISSION_ACTIVITY_INDICATOR_FACTOR:
  def: '10'
  type: int
PROPAGANDA_NETWORK_MISSION_ACTIVITY_INDICATOR_FACTOR:
  def: '10'
  type: int
CONTROL_TRADE_NETWORK_MISSION_ACTIVITY_INDICATOR_FACTOR:
  def: '1'
  type: int
DIPLOMATIC_PRESSURE_NETWORK_MISSION_ACTIVITY_INDICATOR_FACTOR:
  def: '1'
  type: int
INTEL_NETWORK_COVERAGE_ACTIVITY_FACTOR:
  def: '100'
  type: int
INTEL_NETWORK_STRENGTH_DANGER_FACTOR:
  def: '1'
  type: int
ACTIVITY_LEVEL_PROPORTIONAL_FACTOR:
  def: '0.01'
  type: float
ACTIVITY_LEVEL_INTEGRAL_FACTOR:
  def: '0.001'
  type: float
ACTIVITY_LEVEL_DERIVATIVE_FACTOR:
  def: '0'
  type: int
DANGER_LEVEL_PROPORTIONAL_FACTOR:
  def: '0.01'
  type: float
DANGER_LEVEL_INTEGRAL_FACTOR:
  def: '0.001'
  type: float
DANGER_LEVEL_DERIVATIVE_FACTOR:
  def: '0'
  type: int
NUM_DAYS_BEFORE_REMOVING_PREPARED_OPERATIONS:
  def: '60'
  type: int
  cmt: num days before removing prepared operations
ON_CAPTURE_COUNTERINTELLIGENCE_OPERATIVE_XP_GAIN:
  def: '100'
  type: int
  cmt: Xp gain when an enemy operative is captured in the country the operative is
    assigned to counter intelligence to. Apply to a single randomly selected operative
ON_CAPTURE_COUNTERINTELLIGENCE_OPERATIVE_WEIGHT_OWN_COUNTRY_FOR_XP:
  def: '2'
  type: int
  cmt: An integer on how likely an operative operating in his own country is to get
    selected for the xp reward on enemy operative capture
ON_CAPTURE_COUNTERINTELLIGENCE_OPERATIVE_WEIGHT_DIFFERENT_COUNTRY_FOR_XP:
  def: '1'
  type: int
  cmt: same for an operative assigned to counter intelligence in a different country
    than his own
RISK_LEVELS:
  def:
    - [0.1, 0.2, 0.3]
  type: table
  cmt: each risk level comes with a label to display for operations if it goes abve that
    number. If below the first it will isntead show the good outcomes
RISK_LEVELS_LABELS:
  def:
    - ["RISK_LOW", "RISK_MID", "RISK_HIGH"]
  type: table
OUTCOME_LEVELS:
  def:
    - [0.0, 0.2, 0.3]
  type: table
  cmt: outcome levels are shown if risk is below its first entry instead
OUTCOME_LEVELS_LABELS:
  def:
    - ["OUTCOME_BASE", "OUTCOME_GOOD", "OUTCOME_VGOOD"]
  type: table
TECH_STEAL_EQUIPMENT_FACTOR:
  def: '4'
  type: int
TECH_STEAL_YEAR_FACTOR:
  def: '4'
  type: int
```
