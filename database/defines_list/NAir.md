---
domain: defines_list
concept: NAir
version: 1.17.2
requires: [defines]
relates: [air_wings]
---

```yaml
AIR_INVASION_PREPARE_DAYS:
  def: '7'
  type: int
  cmt: base days needed to prepare an airborne invasion
AIR_INVASION_PLAN_CAP:
  def: '1000'
  type: int
  cmt: base cap of airborne invasions can be planned at the same time
AIR_WING_FLIGHT_SPEED_MULT:
  def: '0.02'
  type: float
  cmt: Global speed multiplier for airplanes (affects fe.transferring to another base)
AIR_WING_MAX_STATS_ATTACK:
  def: '100'
  type: int
  cmt: Max stats
AIR_WING_MAX_STATS_DEFENCE:
  def: '100'
  type: int
AIR_WING_MAX_STATS_AGILITY:
  def: '100'
  type: int
AIR_WING_MAX_STATS_SPEED:
  def: '800'
  type: int
AIR_WING_MAX_STATS_BOMBING:
  def: '100'
  type: int
AIR_WING_MAX_SIZE:
  def: '1000'
  type: int
  cmt: Max amount of airplanes in wing
AIR_WING_AVERAGE_SIZE:
  def: '100'
  type: int
  cmt: Eyeballed average amount of airplanes in wing. Used when calculating air
    volunteer.
AIR_WING_BOMB_DAMAGE_FACTOR:
  def: '2'
  type: int
  cmt: Used to balance the damage done while bombing.
BASE_AIR_INVASION_DIVISION_CAP:
  def: '1000'
  type: int
  cmt: base cap of divisions that can be assigned in a airborne invasion
BIGGEST_AGILITY_FACTOR_DIFF:
  def: '4.0'
  type: float
  cmt: biggest factor difference in agility for doing damage (caps to this)
BIGGEST_SPEED_FACTOR_DIFF:
  def: '3.5'
  type: float
  cmt: biggest factor difference in speed for doing damage (caps to this)
TOP_SPEED_DAMAGE_BONUS_FACTOR:
  def: '0.025'
  type: float
  cmt: A factor for scaling the top speed of a plane into damage buff. If an attacking
    wing has a speed advantage of any form their speed value will be converted into a
    percentage bonus with this modifier
COMBAT_DAMAGE_STATS_MULTILPIER:
  def: '0.2'
  type: float
CARRIER_COMBAT_DAMAGE_STATS_MULTIPLIER:
  def: '0.35'
  type: float
COMBAT_BETTER_AGILITY_DAMAGE_REDUCTION:
  def: '0.45'
  type: float
  cmt: How much the better agility (than opponent's) can reduce their damage to us.
COMBAT_BETTER_SPEED_DAMAGE_INCREASE:
  def: '0.65'
  type: float
  cmt: How much the better Speed (than opponent's) can reduce increase our damage to
    them.
COMBAT_MAX_WINGS_AT_ONCE:
  def: '10000'
  type: int
  cmt: Max amount of air wings in one combat simulation. The higher value, the quicker
    countries may loose their wings. It's a gameplay balance value.
COMBAT_MAX_WINGS_AT_GROUND_ATTACK:
  def: '10000'
  type: int
  cmt: we can really pounce a land strike and escalate
COMBAT_MAX_WINGS_AT_ONCE_PORT_STRIKE:
  def: '10000'
  type: int
  cmt: we can really pounce a naval strike and escalate
AIR_REGION_SUPERIORITY_PIXEL_SCALE:
  def: '0.04'
  type: float
  cmt: air superiority scale = superiority/(pixels*this)
COMBAT_MULTIPLANE_CAP:
  def: '3.0'
  type: float
  cmt: How many planes can shoot at each plane on other side ( if there are 100 planes
    we are atttacking COMBAT_MULTIPLANE_CAP * 100 of our planes can shoot )
COMBAT_DAMAGE_SCALE:
  def: '1'
  type: int
  cmt: Higher value = more shot down planes
COMBAT_DAMAGE_SCALE_CARRIER:
  def: '5'
  type: int
  cmt: same as above but used inside naval combat for carrier battles
CARRIER_PERCENTAGE_DEFEND:
  def: '0.35'
  type: float
  cmt: Percentage of planes able to defend a carrier from air attacks (historically 15%
    - 35%)
DETECT_CHANCE_FROM_OCCUPATION:
  def: '0.10'
  type: float
  cmt: How much the controlled provinces in area affects the air detection base value.
DETECT_CHANCE_FROM_RADARS:
  def: '0.5'
  type: float
  cmt: How much the radars in area affects detection chance.
DETECT_CHANCE_FROM_AIRCRAFTS_EFFECTIVE_COUNT:
  def: '3000'
  type: int
  cmt: Max amount of aircrafts in region to give full detection bonus.
DETECT_CHANCE_FROM_AIRCRAFTS:
  def: '0.8'
  type: float
  cmt: How much aircrafts in region improves air detection (up to effective count).
DETECT_CHANCE_FROM_NIGHT:
  def: '-0.2'
  type: float
  cmt: How much the night can reduce the air detection. (see static modifiers to check
    how weather affects it too.)
DETECT_EFFICIENCY_BASE:
  def: '0.1'
  type: float
  cmt: Base value for detection efficiency (once something detected, efficiency says how
    many airplanes was detected).
DETECT_EFFICIENCY_FROM_RADAR:
  def: '0.7'
  type: float
  cmt: How much radars affect the efficiency.
DETECT_EFFICIENCY_RANDOM_FACTOR:
  def: '0.1'
  type: float
  cmt: How much randomness is in amount of detected aircrafts.
DAY_NIGHT_COVERAGE_FACTOR:
  def: '0.5'
  type: float
  cmt: The max night coverage in a region that is still considered to be day-time when
    determining if day/night air missions shall run.
HOURS_DELAY_AFTER_EACH_COMBAT:
  def: '4'
  type: int
  cmt: How many hours needs the wing to be ready for the next combat. Use for tweaking
    if combats happens too often. (generally used as double because of roundtrip)
PORT_STRIKES_DELAY_MULTIPLIER:
  def: '2'
  type: int
  cmt: multplies HOURS_DELAY_AFTER_EACH_COMBAT if port strikes
CARRIER_HOURS_DELAY_AFTER_EACH_COMBAT:
  def: '3'
  type: int
  cmt: how often carrier planes do battle inside naval combat
CARRIER_SIZE_STAT_INCREMENT:
  def: '10'
  type: int
  cmt: Each Point of carrier_size state adds capacity for this many planes
SUBMARINE_CARRIER_SIZE_STAT_INCREMENT:
  def: '3'
  type: int
  cmt: Each Point of carrier_size state adds capacity for this many planes for
    submarines
MISSILE_LAUNCHER_CAPACITY:
  def: '10'
  type: int
  cmt: The number of missiles per slot
MISSILE_LAUNCHER_SLOTS:
  def: '1'
  type: int
  cmt: The number of missile slots a missile launcher unit can have
NAVAL_STRIKE_TARGETTING_TO_AMOUNT:
  def: '0.3'
  type: float
  cmt: Balancing value to convert the naval_strike_targetting equipment stats to chances
    of how many airplanes managed to do successfull strike.
NAVAL_STRIKE_DAMAGE_TO_STR:
  def: '1.0'
  type: float
  cmt: Balancing value to convert damage ( naval_strike_attack * hits ) to Strength
    reduction.
NAVAL_STRIKE_DAMAGE_TO_ORG:
  def: '1.5'
  type: float
  cmt: Balancing value to convert damage ( naval_strike_attack * hits ) to Organisation
    reduction.
NAVAL_STRIKE_CARRIER_MULTIPLIER:
  def: '10.0'
  type: float
  cmt: damage bonus when planes are in naval combat where their carrier is present (and
    can thus sortie faster and more effectively)
FIELD_EXPERIENCE_SCALE:
  def: '0.0004'
  type: float
FIELD_EXPERIENCE_MAX_PER_DAY:
  def: '2'
  type: int
  cmt: Most xp you can gain per day
CLOSE_AIR_SUPPORT_EXPERIENCE_SCALE:
  def: '0.0005'
  type: float
  cmt: How much the experinence gained by CAS is scaled
PARADROP_EXPERIENCE_SCALE:
  def: '0.03'
  type: float
  cmt: How much the experinence gained by paradropping is scaled
BOMBING_DAMAGE_EXPERIENCE_SCALE:
  def: '0.0002'
  type: float
  cmt: How much the experinence gained by bombing is scaled
EXPERIENCE_SCALE_ATTACK_LOGISTICS_NO_TRUCK_CONSUMERS:
  def: '0.0001'
  type: float
  cmt: How much country experinence gained by attacking consumers who aren't motorized
EXPERIENCE_SCALE_ATTACK_LOGISTICS_NODE_AND_TRAINS:
  def: '0.0002'
  type: float
  cmt: How much country experinence gained by attacking node/trains
EXPERIENCE_SCALE_ATTACK_LOGISTICS_TRUCKS:
  def: '0.0002'
  type: float
  cmt: How much country experinence gained by attacking trucks
FIELD_EXPERIENCE_FACTOR:
  def: '0.7'
  type: float
  cmt: Factor all air experience gain from missions by this
AI_ALLOWED_PLANES_KEPT_IN_RESERVE:
  def: '0.10'
  type: float
  cmt: AI allowed planes is reduced by this percentage. Overflow will be distributed to
    the next valid order. Worst case, this will result in this % of planes no being
    assigned any order.
ACCIDENT_CHANCE_BASE:
  def: '0.1'
  type: float
  cmt: Base chance % (0 - 100) for accident to happen. Reduced with higher reliability
    stat.
ACCIDENT_CHANCE_CARRIER_MULT:
  def: '1.5'
  type: float
  cmt: The total accident chance is scaled up when it happens on the carrier ship.
ACCIDENT_CHANCE_BALANCE_MULT:
  def: '0.10'
  type: float
  cmt: Multiplier for balancing how often the air accident really happens. The higher
    mult, the more often.
ACCIDENT_CHANCE_RELIABILITY_MULT:
  def: '2.0'
  type: float
  cmt: Multiplier to accident chance per point of missing reliability.
ACCIDENT_EFFECT_MULT:
  def: '0.007'
  type: float
  cmt: Multiplier for balancing the effect of accidents
ACE_DEATH_CHANCE_BASE:
  def: '0.005'
  type: float
  cmt: Base chance % for ace pilot die when an airplane is shot down in the Ace wing.
ACE_DEATH_BY_OTHER_ACE_CHANCE:
  def: '1.0'
  type: float
  cmt: chance to an ace dying by another ace if it was hit by ace in combat
ACE_DEATH_CHANCE_PLANES_MULT:
  def: '0.001'
  type: float
  cmt: The more airplanes was lost in a single airplanes (more bloody it was) the higher
    chance of Ace to die.
AIR_AGILITY_TO_NAVAL_STRIKE_AGILITY:
  def: '0.02'
  type: float
  cmt: conversion factor to bring agility in line with ship AA
ACE_EARN_CHANCE_BASE:
  def: '0.01'
  type: float
  cmt: Base chance % for ace pilot creation roll to happen. Happens only when
    successfully kill airplane/ship or damage the buildings.
ACE_EARN_CHANCE_PLANES_MULT:
  def: '0.005'
  type: float
  cmt: Ace generation chance per aircraft. Chance is rolled twice because decimal
    numbers can't be small enough
AIR_DAMAGE_TO_DIVISION_LOSSES:
  def: '1.0'
  type: float
  cmt: factor for conversion air damage to division losses for details statistics of air
    wings
AIR_NAVAL_KAMIKAZE_DAMAGE_MULT:
  def: '20.0'
  type: float
  cmt: Balancing value to increase usual damage to Strength for Kamikaze
AIR_NAVAL_KAMIKAZE_LOSSES_MULT:
  def: '4.0'
  type: float
  cmt: Balancing value to increase usual losses if Kamikaze participating in the battle
BASE_KAMIKAZE_DAMAGE:
  def: '2.0'
  type: float
  cmt: Base Kamikaze death rate
BASE_KAMIKAZE_TARGETING:
  def: '2.0'
  type: float
  cmt: Kamikaze can't be a bad target
BASE_STRATEGIC_BOMBING_HIT_SHIP_CHANCE:
  def: '0.01'
  type: float
  cmt: Chance to hit a ship in port when it is bombed.
BASE_STRATEGIC_BOMBING_HIT_SHIP_DAMAGE_FACTOR:
  def: '50'
  type: int
BASE_STRATEGIC_BOMBING_HIT_PLANE_CHANCE:
  def: '0.5'
  type: float
  cmt: Chance to hit a plane in airbase when it is bombed.
BASE_STRATEGIC_BOMBING_HIT_PLANE_DAMAGE_FACTOR:
  def: '0.2'
  type: float
AGGRESSION_THRESHOLD:
  def:
    - [0.0, 0.25, 0.5]
  type: table
  cmt: Threshold levels for mission aggressivity for air
ACE_WING_SIZE:
  def: '100'
  type: int
  cmt: size of wing ace bonuses are set up for. if lower more bonus, if higher less
    bonus
ACE_WING_SIZE_MAX_BONUS:
  def: '2'
  type: int
  cmt: biggest bonus we can get from having a small wing with an ace on
NO_SEARCH_MISSION_DETECT_FACTOR:
  def: '-0.5'
  type: float
  cmt: value of planes not on active search missions for detection
SUPPLY_NEED_FACTOR:
  def: '0.28'
  type: float
  cmt: multiplies supply usage
SUPPLY_PRIO_FACTOR:
  def: '100.0'
  type: float
  cmt: Effect of supply need per unit for target province picking for air supply
CAPACITY_PENALTY:
  def: '2'
  type: int
  cmt: scales penalty of having overcrowded bases.
AIR_COMBAT_FINAL_DAMAGE_SCALE:
  def: '0.015'
  type: float
  cmt: % how many max disrupted only planes are alloed to die in a single combat
AIR_COMBAT_FINAL_DAMAGE_PLANES:
  def: '50'
  type: int
  cmt: scaling/control for when only very few planes exist to stop roundoff issues
AIR_COMBAT_FINAL_DAMAGE_PLANES_FACTOR:
  def: '0.1'
  type: float
AA_INDUSTRY_AIR_DAMAGE_FACTOR:
  def: '-0.12'
  type: float
  cmt: 5x levels = 60% defense from bombing
NAVAL_STRIKE_DETECTION_BALANCE_FACTOR:
  def: '0.5'
  type: float
  cmt: Value used to scale the surface_visibility stats to balance the gameplay, so 100%
    detection chance still won't spam the strikes.
NAVAL_RECON_DETECTION_BALANCE_FACTOR:
  def: '0.5'
  type: float
  cmt: Value used to scale the surface_visibility stats to balance the gameplay, so 100%
    detection chance still won't spam spotting.
LEND_LEASED_EQUIPMENT_EXPERIENCE_GAIN:
  def: '0.5'
  type: float
  cmt: Value used for equipment
ANTI_AIR_PLANE_DAMAGE_FACTOR:
  def: '0.8'
  type: float
  cmt: Anti Air Gun Damage factor
ANTI_AIR_PLANE_DAMAGE_CHANCE:
  def: '0.1'
  type: float
  cmt: Anti Air Gun hit chance
ANTI_AIR_ATTACK_TO_DAMAGE_REDUCTION_FACTOR:
  def: '1.0'
  type: float
  cmt: Balancing value to convert equipment stat anti_air_attack to the damage reduction
    modifier apply to incoming air attacks against units with AA.
ANTI_AIR_MAXIMUM_DAMAGE_REDUCTION_FACTOR:
  def: '0.75'
  type: float
  cmt: Maximum damage reduction factor applied to incoming air attacks against units
    with AA.
AIR_DEPLOYMENT_DAYS:
  def: '2'
  type: int
  cmt: Days to deploy one air wing
NAVAL_STRIKE_BASE_STR_TO_PLANES_RATIO:
  def: '0.03'
  type: float
  cmt: Max airbombers to do port strike comparing to strength
NAVAL_COMBAT_EXTERNAL_PLANES_JOIN_RATIO:
  def: '0.05'
  type: float
  cmt: Max planes that can join a combat comparing to the total strength of the ships
NAVAL_COMBAT_EXTERNAL_PLANES_JOIN_RATIO_PER_DAY:
  def: '0.2'
  type: float
  cmt: max extra plane % that can join every day
NAVAL_COMBAT_EXTERNAL_PLANES_MIN_CAP:
  def: '20'
  type: int
  cmt: Min cap for planes that can join naval combat
AIR_MORE_GROUND_CREWS_COST:
  def: '20.0'
  type: float
  cmt: CP cost to maintain more ground crews
AIR_MORE_GROUND_CREWS_BOOST:
  def: '0.1'
  type: float
  cmt: Efficienct boost for more ground crews
EFFICIENCY_REGION_CHANGE_PENALTY_FACTOR:
  def: '0.9'
  type: float
  cmt: Penalty applied for changing region
EFFICIENCY_REGION_CHANGE_DAILY_GAIN_DEFAULT:
  def: '1'
  type: int
  cmt: Default how much efficiency to regain per day. Gain applied hourly.
EFFICIENCY_REGION_CHANGE_DAILY_GAIN_CAS:
  def: '0.888'
  type: float
  cmt: How much efficiency to regain per day. Gain applied hourly.
EFFICIENCY_REGION_CHANGE_DAILY_GAIN_NAVAL_BOMBER:
  def: '0.192'
  type: float
  cmt: How much efficiency to regain per day. Gain applied hourly.
EFFICIENCY_REGION_CHANGE_DAILY_GAIN_TACTICAL_BOMBER:
  def: '0.192'
  type: float
  cmt: How much efficiency to regain per day. Gain applied hourly.
EFFICIENCY_REGION_CHANGE_DAILY_GAIN_FIGHTER:
  def: '0.888'
  type: float
  cmt: How much efficiency to regain per day. Gain applied hourly.
EFFICIENCY_REGION_CHANGE_DAILY_GAIN_STRATEGIC_BOMBER:
  def: '0.072'
  type: float
  cmt: How much efficiency to regain per day. Gain applied hourly.
EFFICIENCY_REGION_CHANGE_DAILY_GAIN_MARITIME_PATROL_PLANE:
  def: '1'
  type: int
AIR_WING_XP_MAX:
  def: '1000.0'
  type: float
  cmt: Per plane XP.
AIR_WING_XP_LEVELS:
  def:
    - [100, 300, 700, 900]
  type: table
  cmt: Experience needed to progress to the next level
AIR_WING_XP_LOSS_WHEN_KILLED:
  def: '300'
  type: int
  cmt: if a plane dies, the game assumes that a pilot with this amount of xp died and
    recalcs average.
AIR_WING_XP_TRAINING_MAX:
  def: '300.0'
  type: float
  cmt: Max average XP achieved with training.
AIR_WING_XP_TRAINING_MISSION_GAIN_DAILY:
  def: '7.0'
  type: float
  cmt: Daily gain when running training exercise mission
AIR_WING_XP_AIR_VS_AIR_COMBAT_GAIN:
  def: '0.8'
  type: float
  cmt: Wings in combat gain extra XP
AIR_WING_XP_GROUND_MISSION_COMPLETED_GAIN:
  def: '0.28'
  type: float
  cmt: Bombers bombing, CAS cassing, NBs nbing, kamikazees kamikazeeing, etc.
AIR_WING_XP_RECON_MISSION_COMPLETED_GAIN:
  def: '0.05'
  type: float
  cmt: recon mission
AIR_WING_COUNTRY_XP_FROM_TRAINING_FACTOR:
  def: '0.003'
  type: float
  cmt: Factor on country Air XP gained from wing training
AIR_WING_XP_TRAINING_MISSION_ACCIDENT_FACTOR:
  def: '0.2'
  type: float
  cmt: Training exercises cause more accidents
AIR_WING_XP_LOSS_REDUCTION_OVER_FRIENDLY_TERRITORY_FACTOR:
  def: '0.3'
  type: float
  cmt: Reduction on XP loss over friendly territory
DISRUPTION_FACTOR:
  def: '4.0'
  type: float
  cmt: multiplier on disruption damage to scale its effects on planes
DISRUPTION_FACTOR_CARRIER:
  def: '6.0'
  type: float
  cmt: multiplier on disruption damage to scale its effects on carrier vs carrier planes
DISRUPTION_SPEED_FACTOR:
  def: '1.0'
  type: float
DISRUPTION_AGILITY_FACTOR:
  def: '0.0'
  type: float
DISRUPTION_ATTACK_FACTOR:
  def: '0.0'
  type: float
DISRUPTION_DETECTION_FACTOR:
  def: '1.0'
  type: float
ESCORT_FACTOR:
  def: '2.0'
  type: float
ESCORT_SPEED_FACTOR:
  def: '1.0'
  type: float
ESCORT_AGILITY_FACTOR:
  def: '1.0'
  type: float
ESCORT_ATTACK_FACTOR:
  def: '1.0'
  type: float
DISRUPTION_DEFENCE_DEFENCE_FACTOR:
  def: '0.5'
  type: float
DISRUPTION_DEFENCE_SPEED_FACTOR:
  def: '1.0'
  type: float
DISRUPTION_DEFENCE_ATTACK_FACTOR:
  def: '0.5'
  type: float
CARRIER_PLANES_AMOUNT_FOR_POSITIONING:
  def: '50'
  type: int
  cmt: below this amount of planes on a carrier we no longer get max benefit on enemy
    positioning
CAS_NIGHT_ATTACK_FACTOR:
  def: '0.1'
  type: float
  cmt: CAS damaged get multiplied by this in land combats at night
AIR_WING_ATTACK_LOGISTICS_NO_TRUCK_DISRUPTION_FACTOR:
  def: '0.02'
  type: float
  cmt: If a unit isn't motorized, still disrupt its supply by damage * this
AIR_WING_ATTACK_LOGISTICS_TRUCK_DAMAGE_FACTOR:
  def: '0.27'
  type: float
AIR_WING_ATTACK_LOGISTICS_INFRA_DAMAGE_SPILL_FACTOR:
  def: '0.0016'
  type: float
  cmt: Portion of truck damage to additionally deal to infrastructure
AIR_WING_ATTACK_LOGISTICS_TRAIN_DAMAGE_FACTOR:
  def: '0.040'
  type: float
AIR_WING_ATTACK_LOGISTICS_TRAIN_DAMAGE_DISRUPTION_MITIGATION:
  def: '6.0'
  type: float
  cmt: Multiply Train Damage by (Smooth / (Smooth + (Disruption * Mitigation)))
AIR_WING_ATTACK_LOGISTICS_TRAIN_DAMAGE_DISRUPTION_SMOOTHING:
  def: '5.0'
  type: float
AIR_WING_ATTACK_LOGISTICS_RAILWAY_DAMAGE_SPILL_FACTOR:
  def: '0.006'
  type: float
  cmt: Portion of train damage to additionally deal to railways
AIR_WING_ATTACK_LOGISTICS_DISRUPTION_MIN_DAMAGE_FACTOR:
  def: '0.1'
  type: float
  cmt: Multiply train damage by this factor, scale from 1.0 at 0 disruption to this at
    AIR_WING_ATTACK_LOGISTICS_MAX_DISRUPTION_DAMAGE_TO_CONSIDER
AIR_WING_ATTACK_LOGISTICS_MAX_DISRUPTION_DAMAGE_TO_CONSIDER:
  def: '15.0'
  type: float
  cmt: see above
AIR_WING_ATTACK_LOGISTICS_DIRECT_DISRUPTION_DAMAGE_FACTOR:
  def: '0.01'
  type: float
  cmt: Disruption damage to supply throughput done by bombing damage, not dependant on
    killing trains which also causes diruption.
AIR_WING_ATTACK_LOGISTICS_TRUCK_MAX_FACTOR:
  def: '0.3'
  type: float
  cmt: max trucks we can destroy in one instance of a logistics strike
SECONDARY_DAMAGE_STRAT:
  def: '0.2'
  type: float
  cmt: how much damage gets translated to railway guns for strat bombing
SECONDARY_DAMAGE_LOGISTICS:
  def: '1.0'
  type: float
  cmt: how much damage gets translated to railway guns for logistic strike
INTERCEPTION_DISTANCE_SCALE:
  def: '50'
  type: int
  cmt: At this many pixels of path length, full interception efficiency is applied to
    air missions. Lerp from 0.
INTERCEPTION_DAMAGE_SCALE:
  def: '0.3'
  type: float
  cmt: Multiply the interception damage with this value. Works as a cap when
    interception distance is at maximum.
MIN_PLANE_COUNT_PARADROP:
  def: '50'
  type: int
MIN_PLANE_COUNT_AIR_SUPPLY:
  def: '1'
  type: int
BASE_UNIT_WEIGHT_IN_TRANSPORT_PLANES:
  def: '45.0'
  type: float
MANPOWER_LOSS_RATIO_PLANE_SHOT:
  def: '0.10'
  type: float
  cmt: The loss ratio of manpower for a shot plane.
MISSION_COMMAND_POWER_COSTS:
  def:
    - [0.0]  # AIR_SUPERIORITY
    - [0.0]  # CAS
    - [0.0]  # INTERCEPTION
    - [0.0]  # STRATEGIC_BOMBER
    - [0.0]  # NAVAL_BOMBER
    - [0.0]  # DROP_NUKE
    - [0.0]  # PARADROP
    - [0.0]  # NAVAL_KAMIKAZE
    - [0.0]  # PORT_STRIKE
    - [0.0]  # ATTACK_LOGISTICS
    - [0.05]  # AIR_SUPPLY
    - [0.0]  # TRAINING
    - [0.0]  # NAVAL_MINES_PLANTING
    - [0.0]  # NAVAL_MINES_SWEEPING
    - [0.0]  # RECON
    - [0.0]  # NAVAL_PATROL
    - [0, 0]  # BARRAGE
    - [0, 0]  # SAM
  type: table
  cmt: command power cost per plane to create a mission
MISSION_FUEL_COSTS:
  def:
    - [1.0]  # AIR_SUPERIORITY
    - [1.0]  # CAS
    - [0.2]  # INTERCEPTION
    - [1.0]  # STRATEGIC_BOMBER
    - [1.0]  # NAVAL_BOMBER
    - [1.0]  # DROP_NUKE
    - [1.0]  # PARADROP
    - [0.75]  # NAVAL_KAMIKAZE
    - [1.2]  # PORT_STRIKE
    - [1.2]  # ATTACK_LOGISTICS
    - [1.0]  # AIR_SUPPLY
    - [0.6]  # TRAINING
    - [1.0]  # NAVAL_MINES_PLANTING
    - [1.0]  # NAVAL_MINES_SWEEPING
    - [1.0]  # RECON
    - [1.0]  # NAVAL_PATROL
    - [0.0]  # BARRAGE
    - [0, 0]  # NUCLEAR
    - [0, 0]  # SAM
  type: table
  cmt: fuel cost per plane for each mission
MAX_FUEL_FLOW_MULT:
  def: '1.0'
  type: float
  cmt: max fuel flow ratio for planes, which will be multiplied by supply
FUEL_COST_MULT:
  def: '0.35'
  type: float
  cmt: fuel multiplier for all air missions
MISSION_EFFICIENCY_MULT_AT_LACK_OF_FUEL:
  def: '0.25'
  type: float
  cmt: multiplier for mission efficiency when a base lacks fuel
STRATEGIC_BOMBING_PROV_BUILD_PRIO_SCALE:
  def: '1.5'
  type: float
  cmt: Scale of the selected priority for provincial buildings
STRATEGIC_BOMBING_STATE_BUILD_PRIO_SCALE:
  def: '1.5'
  type: float
  cmt: Scale of the selected priority for state buildings
STRATEGIC_BOMBING_INFRA_PRIO_SCALE:
  def: '0.7'
  type: float
  cmt: Scale of the selected priority for infrastructure
STRATEGIC_BOMBING_RAILWAY_PRIORITY_SCALE:
  def: '0.2'
  type: float
  cmt: The scale of extra priority assigned to railway for strategic bombing
STRATEGIC_BOMBING_STATE_BUILDING_SCALE:
  def: '1.0'
  type: float
  cmt: The scale of state building priority for strategic bombing
NAVAL_MINES_PLANTING_SPEED_MULT:
  def: '0.025'
  type: float
  cmt: Value used to overall balance of the speed of planting naval mines
NAVAL_MINES_PLANTING_SPEED_LOWER_BOUND:
  def: '0.001'
  type: float
  cmt: Speed of planting naval mines can not be lower than this
NAVAL_MINES_SWEEPING_SPEED_MULT:
  def: '0.025'
  type: float
  cmt: Value used to overall balance of the speed of sweeping naval mines
NAVAL_MINES_SWEEPING_SPEED_LOWER_BOUND:
  def: '0.001'
  type: float
  cmt: Speed of sweeping naval mines can not be lower than this
NON_CORE_STRATEGIC_IMPACT:
  def: '0.5'
  type: float
  cmt: multiplier for strategic impact of non-core bombing
RECON_LAND_SPOT_CHANCE:
  def: '0.02'
  type: float
  cmt: scale factor on spotting lan
REINFORCEMENT_DISABLING_DURATION_IN_LAND_CARRIER_TRANSFER:
  def: '48'
  type: int
  cmt: The reinforcement disabling duration in hours when transfering from land to
    carrier and vice versa
THRUST_WEIGHT_AGILITY_FACTOR:
  def: '0.5'
  type: float
  cmt: For plane designs, additive agility bonus per point of thrust exceeding weight
MAX_QUICK_WING_SELECTION:
  def: '3'
  type: int
  cmt: Max possible selection for airwing quick deploy
USE_SINGLE_NAVAL_ARMAMENT_CATEGORY:
  def: 'true'
  type: bool
  cmt: If true, only the armament module category that inflicts the greatest damage to
    naval targets will contribute naval strike and port strike mission specific stats.
    Only modules with both naval_strike_attack and naval_strike_targetting are
    considered. This is used to prevent torpedo_mounting and bomb_locks stats from
    stacking.
PORT_STRIKE_DAMAGE_FACTOR:
  def: '1.0'
  type: float
  cmt: How much damage is dealt to ports during a port strike (per plane damage [complex
    number] * num flying planes * define)
```
