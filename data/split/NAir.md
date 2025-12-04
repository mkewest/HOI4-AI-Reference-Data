```yaml
AIR_WING_FLIGHT_SPEED_MULT:
  def: '0.02'
  type: float
  cmt: Global speed multiplier for airplanes (affects fe.transferring to another base)
AIR_WING_MAX_STATS_DEFENCE:
  def: '100'
  type: int
AIR_WING_MAX_STATS_SPEED:
  def: '800'
  type: int
AIR_WING_MAX_SIZE:
  def: '1000'
  type: int
  cmt: Max amount of airplanes in wing
AIR_WING_BOMB_DAMAGE_FACTOR:
  def: '2'
  type: int
  cmt: Used to balance the damage done while bombing.
BIGGEST_SPEED_FACTOR_DIFF:
  def: '3.5'
  type: float
  cmt: biggest factor difference in speed for doing damage (caps to this)
COMBAT_DAMAGE_STATS_MULTILPIER:
  def: '0.2'
  type: float
COMBAT_BETTER_SPEED_DAMAGE_INCREASE:
  def: '0.65'
  type: float
  cmt: How much the better Speed (than opponent's) can reduce increase our damage
    to them. Both of these defines are combined with their sister FACTOR_DIFF defines
    to create defense or offensive buffs In both cases the maximum bonus or reduction
    is (BIGGEST_X_FACTOR_DIFF - 1) * COMBAT_BETTER_X_DAMAGE_Y * Damage
COMBAT_MAX_WINGS_AT_GROUND_ATTACK:
  def: '10000'
  type: int
  cmt: we can really pounce a land strike and escalate
  use: Deprecated/Unused
COMBAT_MAX_WINGS_AT_ONCE_PORT_STRIKE:
  def: '10000'
  type: int
  cmt: we can really pounce a naval strike and escalate
  use: Deprecated/Unused
AIR_REGION_SUPERIORITY_PIXEL_SCALE:
  def: '0.04'
  type: float
  cmt: air superiority scale = superiority/(pixels*this)
COMBAT_DAMAGE_SCALE:
  def: '1'
  type: int
  cmt: Higher value = more shot down planes
DETECT_CHANCE_FROM_OCCUPATION:
  def: '0.10'
  type: float
  cmt: How much the controlled provinces in area affects the air detection base value.
DETECT_CHANCE_FROM_AIRCRAFTS_EFFECTIVE_COUNT:
  def: '3000'
  type: int
  cmt: Max amount of aircrafts in region to give full detection bonus.
DETECT_CHANCE_FROM_NIGHT:
  def: '-0.2'
  type: float
  cmt: How much the night can reduce the air detection. (see static modifiers to check
    how weather affects it too.)
DETECT_EFFICIENCY_FROM_RADAR:
  def: '0.7'
  type: float
  cmt: How much radars affect the efficiency.
DAY_NIGHT_COVERAGE_FACTOR:
  def: '0.5'
  type: float
  cmt: The max night coverage in a region that is still considered to be day-time
    when determining if day/night air missions shall run.
PORT_STRIKES_DELAY_MULTIPLIER:
  def: '2'
  type: int
  cmt: multplies HOURS_DELAY_AFTER_EACH_COMBAT if port strikes
CARRIER_SIZE_STAT_INCREMENT:
  def: '10'
  type: int
  cmt: Each Point of carrier_size state adds capacity for this many planes
NAVAL_STRIKE_DAMAGE_TO_STR:
  def: '1.0'
  type: float
  cmt: Balancing value to convert damage ( naval_strike_attack * hits ) to Strength
    reduction.
NAVAL_STRIKE_CARRIER_MULTIPLIER:
  def: '10.0'
  type: float
  cmt: damage bonus when planes are in naval combat where their carrier is present
    (and can thus sortie faster and more effectively)
FIELD_EXPERIENCE_MAX_PER_DAY:
  def: '2'
  type: int
  cmt: Most xp you can gain per day
PARADROP_EXPERIENCE_SCALE:
  def: '0.03'
  type: float
  cmt: How much the experinence gained by paradropping is scaled
EXPERIENCE_SCALE_ATTACK_LOGISTICS_NO_TRUCK_CONSUMERS:
  def: '0.0001'
  type: float
  cmt: How much country experinence gained by attacking consumers who aren't motorized
EXPERIENCE_SCALE_ATTACK_LOGISTICS_TRUCKS:
  def: '0.0002'
  type: float
  cmt: How much country experinence gained by attacking trucks
AI_ALLOWED_PLANES_KEPT_IN_RESERVE:
  def: '0.10'
  type: float
  cmt: AI allowed planes is reduced by this percentage. Overflow will be distributed
    to the next valid order. Worst case, this will result in this % of planes no being
    assigned any order.
ACCIDENT_CHANCE_CARRIER_MULT:
  def: '1.5'
  type: float
  cmt: The total accident chance is scaled up when it happens on the carrier ship.
ACCIDENT_CHANCE_RELIABILITY_MULT:
  def: '2.0'
  type: float
  cmt: Multiplier to accident chance per point of missing reliability.
ACE_DEATH_CHANCE_BASE:
  def: '0.005'
  type: float
  cmt: Base chance % for ace pilot die when an airplane is shot down in the Ace wing.
ACE_DEATH_CHANCE_PLANES_MULT:
  def: '0.001'
  type: float
  cmt: The more airplanes was lost in a single airplanes (more bloody it was) the
    higher chance of Ace to die.
ACE_EARN_CHANCE_BASE:
  def: '0.01'
  type: float
  cmt: Base chance % for ace pilot creation roll to happen. Happens only when successfully
    kill airplane/ship or damage the buildings.
AIR_DAMAGE_TO_DIVISION_LOSSES:
  def: '1.0'
  type: float
  cmt: factor for conversion air damage to division losses for details statistics
    of air wings
AIR_NAVAL_KAMIKAZE_LOSSES_MULT:
  def: '4.0'
  type: float
  cmt: Balancing value to increase usual losses if Kamikaze participating in the battle
BASE_KAMIKAZE_TARGETING:
  def: '2.0'
  type: float
  cmt: Kamikaze can't be a bad target
BASE_STRATEGIC_BOMBING_HIT_SHIP_DAMAGE_FACTOR:
  def: '50'
  type: int
BASE_STRATEGIC_BOMBING_HIT_PLANE_DAMAGE_FACTOR:
  def: '0.2'
  type: float
AGGRESSION_THRESHOLD:
  def: '{ 0.0, 0.25, 0.5 }'
  type: array
  cmt: Threshold levels for mission aggressivity for air
ACE_WING_SIZE_MAX_BONUS:
  def: '2'
  type: int
  cmt: biggest bonus we can get from having a small wing with an ace on
SUPPLY_NEED_FACTOR:
  def: '0.28'
  type: float
  cmt: multiplies supply usage
CAPACITY_PENALTY:
  def: '2'
  type: int
  cmt: scales penalty of having overcrowded bases.
AIR_COMBAT_FINAL_DAMAGE_PLANES:
  def: '50'
  type: int
  cmt: scaling/control for when only very few planes exist to stop roundoff issues
AA_INDUSTRY_AIR_DAMAGE_FACTOR:
  def: '-0.12'
  type: float
  cmt: 5x levels = 60% defense from bombing
NAVAL_RECON_DETECTION_BALANCE_FACTOR:
  def: '0.5'
  type: float
  cmt: Value used to scale the surface_visibility stats to balance the gameplay, so
    100% detection chance still won't spam spotting.
ANTI_AIR_PLANE_DAMAGE_FACTOR:
  def: '0.8'
  type: float
  cmt: Anti Air Gun Damage factor
ANTI_AIR_ATTACK_TO_DAMAGE_REDUCTION_FACTOR:
  def: '1.0'
  type: float
  cmt: Balancing value to convert equipment stat anti_air_attack to the damage reduction
    modifier apply to incoming air attacks against units with AA.
AIR_DEPLOYMENT_DAYS:
  def: '2'
  type: int
  cmt: Days to deploy one air wing
NAVAL_COMBAT_EXTERNAL_PLANES_JOIN_RATIO:
  def: '0.05'
  type: float
  cmt: Max planes that can join a combat comparing to the total strength of the ships
NAVAL_COMBAT_EXTERNAL_PLANES_MIN_CAP:
  def: '20'
  type: int
  cmt: Min cap for planes that can join naval combat
AIR_MORE_GROUND_CREWS_BOOST:
  def: '0.1'
  type: float
  cmt: Efficienct boost for more ground crews
EFFICIENCY_REGION_CHANGE_DAILY_GAIN_DEFAULT:
  def: '1'
  type: int
  cmt: Gain should be changed in increments of 0.024 due to precision. Default how
    much efficiency to regain per day. Gain applied hourly.
EFFICIENCY_REGION_CHANGE_DAILY_GAIN_NAVAL_BOMBER:
  def: '0.192'
  type: float
  cmt: How much efficiency to regain per day. Gain applied hourly.
EFFICIENCY_REGION_CHANGE_DAILY_GAIN_FIGHTER:
  def: '0.888'
  type: float
  cmt: How much efficiency to regain per day. Gain applied hourly.
EFFICIENCY_REGION_CHANGE_DAILY_GAIN_MARITIME_PATROL_PLANE:
  def: '1'
  type: int
AIR_WING_XP_LEVELS:
  def: '{ 100, 300, 700, 900 }'
  type: array
  cmt: Experience needed to progress to the next level
AIR_WING_XP_TRAINING_MAX:
  def: '300.0'
  type: float
  cmt: Max average XP achieved with training.
AIR_WING_XP_AIR_VS_AIR_COMBAT_GAIN:
  def: '0.8'
  type: float
  cmt: Wings in combat gain extra XP
AIR_WING_XP_RECON_MISSION_COMPLETED_GAIN:
  def: '0.05'
  type: float
  cmt: recon mission
AIR_WING_XP_TRAINING_MISSION_ACCIDENT_FACTOR:
  def: '0.2'
  type: float
  cmt: Training exercises cause more accidents
DISRUPTION_FACTOR:
  def: '4.0'
  type: float
  cmt: multiplier on disruption damage to scale its effects on planes
DISRUPTION_SPEED_FACTOR:
  def: '1.0'
  type: float
DISRUPTION_ATTACK_FACTOR:
  def: '0.0'
  type: float
ESCORT_FACTOR:
  def: '2.0'
  type: float
ESCORT_AGILITY_FACTOR:
  def: '1.0'
  type: float
DISRUPTION_DEFENCE_DEFENCE_FACTOR:
  def: '0.5'
  type: float
DISRUPTION_DEFENCE_ATTACK_FACTOR:
  def: '0.5'
  type: float
CAS_NIGHT_ATTACK_FACTOR:
  def: '0.1'
  type: float
  cmt: CAS damaged get multiplied by this in land combats at night
AIR_WING_ATTACK_LOGISTICS_TRUCK_DAMAGE_FACTOR:
  def: '0.27'
  type: float
AIR_WING_ATTACK_LOGISTICS_TRAIN_DAMAGE_FACTOR:
  def: '0.040'
  type: float
AIR_WING_ATTACK_LOGISTICS_TRAIN_DAMAGE_DISRUPTION_SMOOTHING:
  def: '5.0'
  type: float
AIR_WING_ATTACK_LOGISTICS_DISRUPTION_MIN_DAMAGE_FACTOR:
  def: '0.1'
  type: float
  cmt: Multiply train damage by this factor, scale from 1.0 at 0 disruption to this
    at AIR_WING_ATTACK_LOGISTICS_MAX_DISRUPTION_DAMAGE_TO_CONSIDER
AIR_WING_ATTACK_LOGISTICS_DIRECT_DISRUPTION_DAMAGE_FACTOR:
  def: '0.01'
  type: float
  cmt: Disruption damage to supply throughput done by bombing damage, not dependant
    on killing trains which also causes diruption.
SECONDARY_DAMAGE_STRAT:
  def: '0.2'
  type: float
  cmt: how much damage gets translated to railway guns for strat bombing
INTERCEPTION_DISTANCE_SCALE:
  def: '50'
  type: int
  cmt: At this many pixels of path length, full interception efficiency is applied
    to air missions. Lerp from 0.
MIN_PLANE_COUNT_PARADROP:
  def: '50'
  type: int
BASE_UNIT_WEIGHT_IN_TRANSPORT_PLANES:
  def: '45.0'
  type: float
MISSION_COMMAND_POWER_COSTS:
  def: '{ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.05, 0.0, 0.0, 0.0, 0.0,
    0.0 }'
  type: array
  cmt: command power cost per plane to create a mission AIR_SUPERIORITY CAS INTERCEPTION
    STRATEGIC_BOMBER NAVAL_BOMBER DROP_NUKE PARADROP NAVAL_KAMIKAZE PORT_STRIKE ATTACK_LOGISTICS
    AIR_SUPPLY TRAINING NAVAL_MINES_PLANTING NAVAL_MINES_SWEEPING RECON NAVAL_PATROL
MAX_FUEL_FLOW_MULT:
  def: '1.0'
  type: float
  cmt: max fuel flow ratio for planes, which will be multiplied by supply
MISSION_EFFICIENCY_MULT_AT_LACK_OF_FUEL:
  def: '0.25'
  type: float
  cmt: multiplier for mission efficiency when a base lacks fuel
BOMBING_PROV_BUILD_PRIO_SCALE:
  def: '1.5'
  type: float
  cmt: Scale of the selected priority for provincial buildings
BOMBING_INFRA_PRIO_SCALE:
  def: '0.7'
  type: float
  cmt: Scale of the selected priority for infastryctyre
NAVAL_MINES_SWEEPING_SPEED_MULT:
  def: '0.025'
  type: float
  cmt: Value used to overall balance of the speed of sweeping naval mines
RECON_LAND_SPOT_CHANCE:
  def: '0.02'
  type: float
  cmt: scale factor on spotting lan
THRUST_WEIGHT_AGILITY_FACTOR:
  def: '0.5'
  type: float
  cmt: For plane designs, additive agility bonus per point of thrust exceeding weight
USE_SINGLE_NAVAL_ARMAMENT_CATEGORY:
  def: 'true'
  type: bool
  cmt: If true, only the armament module category that inflicts the greatest damage
    to naval targets will contribute naval strike and port strike mission specific
    stats. Only modules with both naval_strike_attack and naval_strike_targetting
    are considered. This is used to prevent torpedo_mounting and bomb_locks stats
    from stacking.
```
