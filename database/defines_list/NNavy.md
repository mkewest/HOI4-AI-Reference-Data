```yaml
WAR_SCORE_GAIN_FOR_SUNK_SHIP_MANPOWER_FACTOR:
  def: '0.004'
  type: float
  cmt: Peace Conference war score gained for every manpower killed when sinking a
    ship
WAR_SCORE_GAIN_FOR_SUNK_CONVOY:
  def: '0.08'
  type: float
  cmt: war score gained for every sunk convoy
PEACE_ACTION_TRANSFER_NAVY_EXPERIENCE_RETAINED:
  def: '0.25'
  type: float
  cmt: '% of experience to retain after being transferred in a peace conference'
NAVAL_TRANSFER_PRIORITY:
  def: '1'
  type: int
  cmt: Default convoy priority for naval transports
RESOURCE_LENDLEASE_PRIORITY:
  def: '3'
  type: int
  cmt: Default convoy priority for export lend lease
RESOURCE_ORIGIN_PRIORITY:
  def: '5'
  type: int
  cmt: Default convoy priority for resources shipped internally
ADMIRAL_TASKFORCE_CAP:
  def: '10'
  type: int
  cmt: Convoy Priorities END admirals will start getting penalties after this amount
    of taskforces
DETECTION_CHANCE_MULT_RADAR_BONUS:
  def: '0.1'
  type: float
  cmt: detection chance bonus from radars.
MAX_CAPITALS_PER_AUTO_TASK_FORCE:
  def: '5'
  type: int
  cmt: maximum number of capital ships the auto-task force creation will put together
    when designing SurfaceActionGroup
BEST_CAPITALS_TO_CARRIER_RATIO:
  def: '1'
  type: int
  cmt: capitals / carriers ratio used when auto-task force creation designs CarrierTaskForce
COMBAT_BASE_HIT_CHANCE:
  def: '0.1'
  type: float
  cmt: base chance for hit
COMBAT_EVASION_TO_HIT_CHANCE:
  def: '0.007'
  type: float
  cmt: we take ship evasion stats, and mult by this value, so it gives hit chance
    reduction. So if reduction is 0.025 and ship evasion = 10, then there will be
    0.25 (25%) lower hit chance. (Fe. 50% base -25% from evasion +10% bcoz it's very
    close).
MIN_HIT_PROFILE_MULT:
  def: '0.0'
  type: float
  cmt: largest hit profile penalty to hitting
COMBAT_LOW_MANPOWER_HIT_CHANCE_PENALTY:
  def: '-0.25'
  type: float
  cmt: '% of penalty applied to hit chance when manpower is very low.'
COMBAT_TORPEDO_CRITICAL_CHANCE:
  def: '0.1'
  type: float
  cmt: chance for critical hit from torpedo.
COMBAT_DAMAGE_TO_STR_FACTOR:
  def: '0.6'
  type: float
  cmt: casting damage value to ship strength multiplier. Use it ot balance the game
    difficulty.
NAVY_MAX_XP:
  def: '100'
  type: int
COMBAT_CHASE_RESIGNATION_HOURS:
  def: '8'
  type: int
  cmt: Before we resign chasing enemy, give them some minimum time so the combat doesn't
    end instantly.
COMBAT_MIN_DURATION:
  def: '8'
  type: int
  cmt: Min combat duration before we can retreat. It's a balancing variable so it's
    not possible to always run with our weak ships agains big flotillas.
COMBAT_RETREAT_DECISION_CHANCE:
  def: '0.22'
  type: float
  cmt: There is also random factor in deciding if we should retreat or not. That causes
    a delay in taking decision, that sooner or later will be picked. It's needed so
    damaged fast ships won't troll the combat.
COMBAT_BASE_CRITICAL_CHANCE:
  def: '0.05'
  type: float
  cmt: Base chance for receiving a critical chance. It get's scaled down with ship
    reliability.
COMBAT_ARMOR_PIERCING_CRITICAL_BONUS:
  def: '1.0'
  type: float
  cmt: Bonus to critical chance when shooter armor piercing is higher then target
    armor.
REPAIR_AND_RETURN_PRIO_LOW:
  def: '0.2'
  type: float
  cmt: '% of total Strength. When below, navy will go to home base to repair.'
REPAIR_AND_RETURN_PRIO_HIGH:
  def: '0.9'
  type: float
  cmt: '% of total Strength. When below, navy will go to home base to repair.'
REPAIR_AND_RETURN_PRIO_MEDIUM_COMBAT:
  def: '0.3'
  type: float
  cmt: '% of total Strength. When below, navy will go to home base to repair (in combat).'
REPAIR_AND_RETURN_AMOUNT_SHIPS_LOW:
  def: '0.2'
  type: float
  cmt: '% of total damaged ships, that will be sent for repair-and-return in one call.'
REPAIR_AND_RETURN_AMOUNT_SHIPS_HIGH:
  def: '0.8'
  type: float
  cmt: '% of total damaged ships, that will be sent for repair-and-return in one call.'
EXPERIENCE_LOSS_FACTOR:
  def: '1.00'
  type: float
  cmt: percentage of experienced solders who die when manpower is removed
MISSION_MAX_REGIONS:
  def: '0'
  type: int
  cmt: Limit of the regions that can be assigned to naval mission. Set to 0 for unlimited.
CONVOY_EFFICIENCY_REGAIN_AFTER_DAYS:
  def: '7'
  type: int
  cmt: Convoy starts regaining it's efficiency after X days without any convoys being
    sink.
CONVOY_EFFICIENCY_MIN_VALUE:
  def: '0.05'
  type: float
  cmt: To avoid complete 0% efficiency, set the lower limit.
ANTI_AIR_TARGETTING_TO_CHANCE:
  def: '0.2'
  type: float
  cmt: Balancing value to convert averaged equipment stats (anti_air_targetting and
    naval_strike_agility) to probability chances of airplane being hit by navies AA.
CONVOY_SINKING_SPILLOVER:
  def: '0.5'
  type: float
  cmt: Damaged convoys roll for if they sink in the end of combat by accumulating
    the damage. This scales that chance.
UNIT_EXPERIENCE_SCALE:
  def: '1'
  type: int
EXPERIENCE_FACTOR_NON_CARRIER_GAIN:
  def: '0.04'
  type: float
  cmt: Xp gain by non-carrier ships in the combat
FIELD_EXPERIENCE_SCALE:
  def: '0.075'
  type: float
LEADER_EXPERIENCE_SCALE:
  def: '1.0'
  type: float
BATTLE_NAME_VP_CUTOFF:
  def: '1.0'
  type: float
  cmt: If best score of above calculation is below this, name will be that of region.
AMPHIBIOUS_INVADE_SPEED_BASE:
  def: '0.5'
  type: float
  cmt: every hour movement progress on amphibious invasion
AMPHIBIOUS_INVADE_ATTACK_LOW:
  def: '0.2'
  type: float
  cmt: low and high cap of attack modifier scale. Scale interpolated by invasion progress.
AMPHIBIOUS_INVADE_DEFEND_LOW:
  def: '1.5'
  type: float
  cmt: low and high cap of defend modifier scale. Scale interpolated by invasion progress.
AMPHIBIOUS_INVADE_LANDING_PENALTY_DECREASE:
  def: '3.5'
  type: float
  cmt: scale of bonus that decreases "amphibious penalty" during combat, relative
    to invading transporter tech.
CONVOY_ATTACK_BASE_FACTOR:
  def: '0.15'
  type: float
  cmt: base % of convoys that get intercepted
NAVAL_RANGE_TO_INGAME_DISTANCE:
  def: '0.12'
  type: float
  cmt: Scale the ship stats "naval_range" to the ingame distance
NAVAL_COMBAT_RESULT_TIMEOUT_YEARS:
  def: '2'
  type: int
  cmt: after that many years, we clear the naval combat results, so they don't get
    stuck forever in the memory.
NAVAL_TRANSFER_BASE_SPEED:
  def: '6'
  type: int
  cmt: base speed of units on water being transported
NAVAL_TRANSFER_BASE_NAVAL_DIST_MULT:
  def: '20'
  type: int
  cmt: Multiplier for the cost of naval movement ( compared to land movement ) when
    deciding what ports to use for naval transfer
CARRIER_STACK_PENALTY:
  def: '4'
  type: int
  cmt: The most efficient is 4 carriers in combat. 5+ brings the penalty to the amount
    of wings in battle.
SHORE_BOMBARDMENT_CAP:
  def: '0.25'
  type: float
MIN_TRACTED_ASSIST_DAMAGE_RATIO:
  def: '0.05'
  type: float
  cmt: How much damage counts as assist damage
DECRYPTION_SPOTTING_BONUS:
  def: '0.2'
  type: float
MANPOWER_LOSS_RATIO_ON_SUNK:
  def: '0.5'
  type: float
  cmt: sunk ships will lose this ratio of their current manpower
MIN_MANPOWER_RATIO_TO_DROP:
  def: '0.1'
  type: float
  cmt: ships will not lose man power to below this ratio
PRIDE_OF_THE_FLEET_UNASSIGN_COST:
  def: '100'
  type: int
  cmt: cost to unassign/replace pride of the fleet
XP_GAIN_FACTOR:
  def: '1.0'
  type: float
  cmt: xp gain factor for navy
CARRIER_ONLY_COMBAT_ACTIVATE_TIME:
  def: '0'
  type: int
  cmt: hours from start of combat when carriers get to fight
ALL_SHIPS_ACTIVATE_TIME:
  def: '8'
  type: int
  cmt: hours where all get to attack
REPAIR_SPLIT_TASKFORCE_SIZE:
  def: '5'
  type: int
  cmt: if a country does not have empty naval naval bases for repairs, it will split
    ships with this sizes and distribute them around
NAVY_REPAIR_BASE_SEARCH_SCORE_PER_SLOT:
  def: '1.0'
  type: float
  cmt: while searching for a naval base for repairs, the bases gets a bonus to their
    scores per empty slot they have
CONVOY_SPOTTING_COOLDOWN:
  def: '0.3'
  type: float
  cmt: '% of travel time'
CONVOY_SPOTTING_COOLDOWN_MAX:
  def: '168'
  type: int
  cmt: maximum cooldown time
MISSION_FUEL_COSTS:
  def: '{ 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.6, 0.0, 1.0 }'
  type: array
  cmt: fuel cost for each mission HOLD (consumes fuel HOLD_MISSION_MOVEMENT_COST fuel
    while moving) PATROL STRIKE FORCE (does not cost fuel at base, and uses IN_COMBAT_FUEL_COST
    in combat. this is just for the movement in between) CONVOY RAIDING CONVOY ESCORT
    MINES PLANTING MINES SWEEPING TRAIN RESERVE_FLEET (consumes fuel HOLD_MISSION_MOVEMENT_COST
    fuel while moving) NAVAL_INVASION_SUPPORT (does not cost fuel at base, only costs
    while doing bombardment and escorting units)
ON_BASE_FUEL_COST:
  def: '0.0'
  type: float
  cmt: ships that waits at naval bases cost this ratio
TRAINING_FUEL_COST_FOR_ESCORT_SHIPS:
  def: '0.15'
  type: float
  cmt: ships that are on training mission but not training (ie they are at max xp
    and training will cancel at max xp) will consume this ratio of fuel
FUEL_COST_MULT:
  def: '0.10'
  type: float
  cmt: fuel multiplier for all naval missions
OUT_OF_FUEL_RANGE_FACTOR:
  def: '-0.75'
  type: float
OUT_OF_FUEL_TORPEDO_FACTOR:
  def: '-0.8'
  type: float
MISSION_DEFAULT_SPREAD_BASE:
  def: '1.0'
  type: float
  cmt: multiplier for mission spreads. higher = less ships on start
AGGRESION_MULTIPLIER_FOR_COMBAT:
  def: '1.2'
  type: float
  cmt: ships are more aggresive in combat
AGGRESSION_MIN_ARMOR_EFFICIENCY:
  def: '0.5'
  type: float
  cmt: armor multiplier has a min and max caps while being factored in aggression
AGGRESSION_LIGHT_GUN_EFFICIENCY_ON_LIGHT_SHIPS:
  def: '1.0'
  type: float
  cmt: ratio for scoring for different gun types against light ships
AGGRESSION_TORPEDO_EFFICIENCY_ON_LIGHT_SHIPS:
  def: '0.1'
  type: float
  cmt: ratio for scoring for different gun types against light ships
AGGRESSION_HEAVY_GUN_EFFICIENCY_ON_HEAVY_SHIPS:
  def: '1.0'
  type: float
  cmt: ratio for scoring for different gun types against heavy ships
AGGRESSION_CONVOY_STRENGTH_FACTOR:
  def: '0.3'
  type: float
  cmt: convoys in combat gets a penalty to their strength in aggression calculations
MIN_REPAIR_FOR_JOINING_COMBATS:
  def: '{ 0.0, 0.5, 0.7, 0.9 }'
  type: array
  cmt: strikeforces/patrol forces will not join combats if they are not repaired enough
    do not repair low medium high
ORG_COST_WHILE_MOVING_IN_MISSION_ZONE:
  def: '{ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 }'
  type: array
  cmt: org cost while moving in mission zone HOLD PATROL STRIKE FORCE CONVOY RAIDING
    CONVOY ESCORT MINES PLANTING MINES SWEEPING TRAIN RESERVE_FLEET NAVAL_INVASION_SUPPORT
MIN_ORG_ON_MANUAL_MOVE:
  def: '0.1'
  type: float
  cmt: org will clamped to this ratio on manual move
MISSION_SUPREMACY_RATIOS:
  def: '{ 0.0, 1.0, 1.0, 0.5, 0.5, 0.3, 0.3, 0.0, 0.0, 1.0 }'
  type: array
  cmt: supremacy multipliers for different mission types HOLD PATROL STRIKE FORCE
    CONVOY RAIDING CONVOY ESCORT MINES PLANTING MINES SWEEPING TRAIN RESERVE_FLEET
    NAVAL_INVASION_SUPPORT
SUPREMACY_PER_SHIP_PER_IC:
  def: '0.005'
  type: float
NAVAL_MINES_IN_REGION_MAX:
  def: '1000.0'
  type: float
  cmt: Max number of mines that can be layed by the ships. The value should be hidden
    from the user, as we present % so it's an abstract value that should be used for
    balancing.
NAVAL_MINES_SWEEPING_SPEED_MULT:
  def: '0.009'
  type: float
  cmt: Value used to overall balance of the speed of sweeping naval mines
NAVAL_MINES_SWEEPERS_REDUCTION_ON_PENALTY_EFFECT:
  def: '3.3'
  type: float
  cmt: How much is the task force's sweeping attribute reducing the penalty effect.
NAVAL_MINES_NAVAL_SUPREMACY_FACTOR:
  def: '1.0'
  type: float
  cmt: Factor for max amount of mines increasing naval supremacy
ATTRITION_DAMAGE_ORG:
  def: '0.01'
  type: float
  cmt: damage from attrition to Organisation (relative to max org)
ATTRITION_STR_DAMAGE_CHANCE:
  def: '0.2'
  type: float
  cmt: chance to get damaged at highest attrition
NAVAL_ACCIDENT_CRITICAL_HIT_CHANCE_REDUCTION_POTF:
  def: '0.01'
  type: float
  cmt: Scale of the current chance for a critical hit when an accident happens, applied
    for the pride of the fleet.
NAVAL_MINES_ACCIDENT_CRITICAL_HIT_DAMAGE_SCALE:
  def: '5.0'
  type: float
  cmt: Scale the value below in case of critical hit (caused by naval mines)
NAVAL_MINES_ACCIDENT_ORG_LOSS_FACTOR:
  def: '0.5'
  type: float
  cmt: Amount of strength loss when hit by naval mine
TRAINING_ACCIDENT_CRITICAL_HIT_CHANCES:
  def: '0.3'
  type: float
  cmt: If an accident happens, how likely it is to be a critical hit
TRAINING_ACCIDENT_STRENGTH_LOSS:
  def: '4.0'
  type: float
  cmt: Amount of strength loss in a training accident
TRAINING_ACCIDENT_ORG_LOSS_FACTOR:
  def: '0.3'
  type: float
  cmt: Amount of current organization the ship lose
TRAINING_EXPERIENCE_FACTOR:
  def: '0.3'
  type: float
  cmt: 'The Formula: Min( TRAINING_MAX_DAILY_COUNTRY_EXP * Ratio, TRAINING_DAILY_COUNTRY_EXP_FACTOR
    * ( TRAINING_DAILY_COUNTRY_EXP_SHIP_RATIO_FACTOR * TrainingShipCount / CountryShipCount
    + TRAINING_DAILY_COUNTRY_EXP_MANPOWER_FACTOR * Manpower + TRAINING_DAILY_COUNTRY_EXP_MANPOWER_RATIO_FACTOR
    * Manpower / CountryShipCount ) ) Amount of exp each ship gain every 24h while
    training (before modifiers)'
TRAINING_DAILY_COUNTRY_EXP_MANPOWER_FACTOR:
  def: '0.006'
  type: float
  cmt: Factor used to scale the sum of the training manpower for the Daily Country
    Navy XP gain
TRAINING_DAILY_COUNTRY_EXP_SHIP_RATIO_FACTOR:
  def: '300.0'
  type: float
  cmt: Factor used to scale the ratio of training ships for the Daily Country Navy
    XP gain
TRAINING_MIN_STRENGTH:
  def: '0.1'
  type: float
  cmt: if strength is less than this, the unit will not contribute to training and
    cant be damaged by training
BASE_SPOTTING:
  def: '1'
  type: int
  cmt: base spotting percentage for navy
NAVY_SPOTTER_DETECTION_FACTOR:
  def: '0.1'
  type: float
  cmt: multiplier for task forces' detection value before logistic transform
AIR_SPOTTER_NORMALIZED_AIRWING_SIZE:
  def: '100'
  type: int
  cmt: each plane will contribute 1/this of the air-wing's detection stat
BASE_SPOTTING_FROM_AIR:
  def: '20'
  type: int
  cmt: base spotting percentage that comes from air-wings in area
MIN_SPOTTING_PROGRESS:
  def: '0.01'
  type: float
  cmt: Minimum spotting progress (in percent) per hourly tick
MIN_HOURS_TO_SHUFFLE_NEWLY_ASSIGNED_PATROLS:
  def: 7*24
  type: mixed
  cmt: if a fleet has less patrol than it needs to cover all of it areas, it will
    shuffle the patrols around. it will wait this much hour before shuffling a task
    force to new area
SPOTTING_MULTIPLIER_FOR_SURFACE:
  def: '1.0'
  type: float
  cmt: task force surface spotting value is multiplied by this and added to spotting
    percentage every hour
SPOTTING_SPEED_MULT_FOR_RUNNING_AWAY:
  def: '0.5'
  type: float
  cmt: task forces that does not want to engage will reduce enemy spotting rate every
    hour by speed diff mult this ratio
SPOTTING_MISSION_DETECTION_THRESHOLD_LOW:
  def: '10.0'
  type: float
  cmt: value between 0 and 100 above which to show very coarse information about the
    spotted task force
NAVY_VISIBILITY_BONUS_ON_RETURN_FOR_REPAIR:
  def: '0.9'
  type: float
  cmt: Multiplier for the surface/sub visiblity when the heavily damaged fleet is
    returning to the home base for reparation. 1.0 = no bonus. 0.0 = invisible.
INTEL_LEVEL_LOW_HALF_RANGE_PERCENTAGE:
  def: '10'
  type: int
  cmt: Integer representing the maximum offset of the displayed value to the original,
    in percentage (divided by 100 in code). For spotting level "low".
INTEL_LEVEL_LOW_HALF_RANGE_MIN_SHIPS:
  def: '3'
  type: int
  cmt: If the percentage of the value is lower than this, use this value instead.
    For spotting level "low"
INTEL_LEVEL_MEDIUM_HALF_RANGE_MIN_SHIPS:
  def: '1'
  type: int
  cmt: If the percentage of the value is lower than this, use this value instead.
    For spotting level "medium"
INTEL_LEVEL_LOW_STRENGTH_ESTIMATE_HALF_RANGE_PERCENTAGE:
  def: '20'
  type: int
  cmt: Integer representing the maximum offset of the estimated enemy strength to
    the original, in percentage (divided by 100 in code). For spotting level "low".
BASE_SPOTTING_SPEED:
  def: '0.0'
  type: float
  cmt: daily base spotting speed
SPEED_TO_ESCAPE_SPEED:
  def: '0.95'
  type: float
  cmt: ratio to converstion from ship speed to escape speed (divided by hundred)
MAX_ESCAPE_SPEED_FROM_COMBAT_DURATION:
  def: '0.15'
  type: float
  cmt: max escape speed that will be gained from combat duration
ESCAPE_SPEED_HIDDEN_SUB:
  def: '0.18'
  type: float
  cmt: hidden subs get faster escape speed
SUB_DETECTION_CHANCE_BASE_SPOTTING_EFFECT:
  def: '0.5'
  type: float
  cmt: effect of base spotting for initial spotting of pure submarine forces. this
    along with next value is added together and rolled against a random to start spotting
SUB_DETECTION_CHANCE_BASE_SPOTTING_POW_EFFECT:
  def: '1.5'
  type: float
  cmt: effect of spotting speed will be powered by this for initial spotting of pure
    submarine forces. this along with prev value is added together and rolled against
    a random to start spotting
BASE_UNIT_TRANSFER_SPOTTING_SPEED:
  def: '0.0'
  type: float
  cmt: daily base spotting speed against unit trans
CONVOY_SPOTTING_SPEED_MULT:
  def: '1.0'
  type: float
  cmt: spotting speed mult against convoys
NAVAL_INVASION_SPOTTING_SPEED_MULT:
  def: '10.0'
  type: float
  cmt: spotting speed mult against naval invasion armies
BASE_SPOTTING_EFFECT_FOR_INITIAL_CONVOY_SPOTTING:
  def: '0.05'
  type: float
  cmt: effect of base convoy spotting for initial spotting of regular convoys. this
    along with next value is added together and rolled a random  once for every convoy
    to check for spotting
SPOTTING_MOD_FOR_CONVOY_COUNT:
  def: '0.2'
  type: float
  cmt: a modifier for scaling the count of convoys on a parabolic curve (counvoy_count
    ^ SPOTTING_MOD_FOR_CONVOY_COUNT)
BASE_SPOTTING_EFFECT_FOR_INITIAL_UNIT_TRANSFER_SPOTTING:
  def: '2.4'
  type: float
  cmt: same as BASE_SPOTTING_EFFECT_FOR_INITIAL_CONVOY_SPOTTING, but for naval transfer
    convoys
BASE_SPOTTING_EFFECT_FOR_INITIAL_NAVAL_INVASION_SPOTTING:
  def: '2.4'
  type: float
  cmt: same as BASE_SPOTTING_EFFECT_FOR_INITIAL_CONVOY_SPOTTING, but for naval invasion
    convoys
MIN_GUN_COOLDOWN:
  def: '0.1'
  type: float
  cmt: minimum cooldown for a gun
BASE_JOIN_COMBAT_HOURS:
  def: '2'
  type: int
  cmt: the taskforces that wants to join existing combats will wait for at least this
    amount
BASE_POSITIONING:
  def: '1.0'
  type: float
  cmt: base value for positioning
MAX_POSITIONING_BONUS_FROM_SURFACE_DETECTION:
  def: '0.0'
  type: float
  cmt: will clamp the bonus that you get from detection
MAX_POSITIONING_PENALTY_FROM_HIGHER_SHIP_RATIO:
  def: '0.75'
  type: float
  cmt: maximum penalty to get from larger fleets
MAX_CARRIER_RATIO_POSITIONING_PENALTY_FACTOR:
  def: '0.2'
  type: float
  cmt: max penalty from stronger carrier air force
MAX_POSITIONING_PENALTY_FOR_NEWLY_JOINED_SHIPS:
  def: '0.25'
  type: float
  cmt: the accumulated penalty from new ships will be clamped to this value
DAMAGE_PENALTY_ON_MINIMUM_POSITIONING:
  def: '0.5'
  type: float
  cmt: damage penalty at 0% positioning
AA_EFFICIENCY_PENALTY_ON_MINIMUM_POSITIONING:
  def: '0.7'
  type: float
  cmt: AA penalty at 0% positioning
SHIP_TO_FLEET_ANTI_AIR_RATIO:
  def: '0.25'
  type: float
  cmt: total sum of fleet's anti air will be multiplied with this ratio and added
    to calculations anti-air of individual ships while air damage reduction
ANTI_AIR_MULT_ON_INCOMING_AIR_DAMAGE:
  def: '0.18'
  type: float
CHANCE_TO_DAMAGE_PART_ON_CRITICAL_HIT:
  def: '0.1'
  type: float
  cmt: the game will roll between 0-1 and will damage a random part if below this
    val on naval critical hits
SCREEN_RATIO_FOR_FULL_SCREENING_FOR_CAPITALS:
  def: '3.0'
  type: float
  cmt: this screen ratio to num capital/carriers is needed for full screening beyond
    screen line
CAPITAL_RATIO_FOR_FULL_SCREENING_FOR_CARRIERS:
  def: '1.0'
  type: float
  cmt: this capital ratio to num carriers is needed for full screening beyond screen
    line
TASK_FORCE_ROLE_TO_INSIGNIA:
  def: '{ 6, 15, 22, 26, 16, 17, 29, 1 }'
  type: array
  cmt: define the index of the insignia to use for a task force designed for a specific
    role Role undefined Wolfpack Carrier task force Surface action group Mine layers
    Mine sweepers Patrol task force Convoy escort
SURFACE_DETECTION_STAT_FOR_SHIP_TO_BE_PATROL:
  def: '16'
  type: int
  cmt: amount of surface detection required for a ship to be considered as part of
    a patrol task force
SUB_DETECTION_STAT_FOR_SHIP_TO_BE_SUB_HUNTER:
  def: '2'
  type: int
  cmt: amount of sub detection required for a ship to be considered a sub hunter
LIGHT_GUN_ATTACK_TO_SHORE_BOMBARDMENT:
  def: '0.05'
  type: float
  cmt: light gun attack value is divided by this value * 100 and added to shore bombardment
    modifier
DEPTH_CHARGES_HIT_CHANCE_MULT:
  def: '1.1'
  type: float
  cmt: multiplies hit chance of small guns
DEPTH_CHARGES_HIT_PROFILE:
  def: '100.0'
  type: float
  cmt: hit profile for depth charges
HIT_PROFILE_MULT:
  def: '100.0'
  type: float
  cmt: multiplies hit profile of every ship
HIT_PROFILE_SPEED_BASE:
  def: '20'
  type: int
  cmt: Base value added to hitprofile speed calulation
CONVOY_DEFENSE_MAX_CONVOY_TO_SHIP_RATIO:
  def: '12.0'
  type: float
  cmt: each ship in convoy defense mission can at most cover this many convoys without
    losing efficiency
MINE_SWEEPING_SUPREMACY_EFFICIENCY_MAX_REGION_TO_TASKFORCE_RATIO:
  def: '1.0'
  type: float
  cmt: mine missions will get lower supremacies if they are assigned more regions
    than this
EFFICIENCY_TO_JOIN_COMBAT_RATIO_PENALTY:
  def: '1.0'
  type: float
  cmt: at lower efficiencies less ships will be able to join combat
COORDINATION_EFFECT_ON_CONVOY_RAID_EFFICIENCY:
  def: '1.5'
  type: float
  cmt: coordination will increase the number of areas you can cover in convoy raid
COORDINATION_EFFECT_ON_TIME_TO_JOIN_COMBAT:
  def: '1.0'
  type: float
  cmt: coordination will reduce the time to join combat penalties
COORDINATION_EFFECT_ON_MINE_SWEEPING_SPEED:
  def: '0.5'
  type: float
  cmt: affect of coordination modifier in mine sweeping speed
COORDINATION_EFFECT_ON_MINE_SWEEPING_SUPREMACY_EFFICIENCY:
  def: '1.0'
  type: float
  cmt: mine missions supremacy can be buffed by coordination
MISSION_EFFICIENCY_POW_FACTOR:
  def: '1.7'
  type: float
  cmt: mission efficiencies will be powered up by this to further penalize low efficiencies
SUBMARINE_HIDE_TIMEOUT:
  def: '20'
  type: int
  cmt: Amount of in-game-hours that takes the submarine (with position unrevealed),
    to hide.
SUBMARINE_REVEAL_BASE_CHANCE:
  def: '11'
  type: int
  cmt: Base factor for submarine detection. It's modified by the difference of a spotter's
    submarines detection vs submarine visibility. Use this variable for game balancing.
    setting this too low will cause bad spotting issues.
SUBMARINE_BASE_TORPEDO_REVEAL_CHANCE:
  def: '0.035'
  type: float
  cmt: Chance of a submarine being revealed when it fires. 1.0 is 100%. this chance
    is then multiplied with modifier created by comparing firer's visibiility and
    target's detection
COMBAT_RESULT_PRIORITY_THRESHOLDS:
  def: '{ 0, 4000, 20000 }'
  type: array
  cmt: the game will use this thresholds to define importance of a naval combat result.
    it will use the highest level that has higher threshold than the amount of production
    lost in combat low (keep at zero) medium high
NAVAL_ACCIDENTS_DAYS_TO_LIVE:
  def: '120'
  type: int
NAVAL_MINE_DANGER_TRIGGER_MIN:
  def: '0.0'
  type: float
NAVAL_CONVOY_DANGER_RATIOS:
  def: '{ 0.10, 0.10, 0.10, 0.15, 0.15 }'
  type: array
  cmt: not owned near controlled near owned controlled owned
NAVAL_CONVOY_DANGER_TRIGGER_MAX:
  def: '100.0'
  type: float
NAVAL_COMBAT_AIR_SUB_DETECTION_SLOPE:
  def: '10.0'
  type: float
  cmt: lower means sharper curve (ramps up very fast, then flatten out very fast).
    Must be >0
NAVAL_COMBAT_AIR_SUB_DETECTION_INTERNAL_EFFICIENCY_FACTOR:
  def: '1.0'
  type: float
  cmt: Factor of Carrier's sortie efficiency on the stats bellow
NAVAL_COMBAT_AIR_STRIKE_ATTACK_TO_SUB_DETECTION:
  def: '0.0'
  type: float
  cmt: Same, but for strike attack (aka naval attack)
NAVAL_COMBAT_AIR_MAX_SPEED_TO_SUB_DETECTION:
  def: '0.0'
  type: float
  cmt: Same, but for Max Speed
NAVAL_COMBAT_AIR_SUB_DETECTION_DECAY_RATE:
  def: '1.0'
  type: float
  cmt: 'Factor to decay the value of sub detection contributed by planes on the last
    hour. Note: the maximum value between the decayed value and the newly computed
    one is taken into account. A decay rate of 1 means that nothing is carried over,
    the previous value is zerod out. A decay rate of 0 means that the previous value
    is carried over as is.'
NAVAL_COMBAT_AIR_SUB_TARGET_SCORE:
  def: '10'
  type: int
  cmt: scoring for target picking for planes inside naval combat, one define per ship
    typ
NAVAL_COMBAT_AIR_CARRIER_TARGET_SCORE:
  def: '200'
  type: int
NAVAL_COMBAT_AIR_STRENGTH_TARGET_SCORE:
  def: '5'
  type: int
  cmt: how much score factor from low health (scales between 0->this number)
NEW_NAVY_LEADER_LEVEL_CHANCES:
  def: '{ 0.95, 0.05 }'
  type: array
  cmt: chances for new navy leaders to start at a given level 95% for level one 5%
    for level two 0% for level three to ten
NAVY_PIERCING_THRESHOLD_CRITICAL_VALUES:
  def: '{ 2.00, 1.00, 0.75, 0.50, 0.10, 0.00 }'
  type: array
  cmt: 0 armor will always receive maximum damage (so add overmatching at your own
    peril). the system expects at least 2 values, with no upper limit. For criticals,
    you could reduce crit chance unlike damage in army combat, but we do not for now.
```
