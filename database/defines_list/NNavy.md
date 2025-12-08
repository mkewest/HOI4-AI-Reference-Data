```yaml
WAR_SCORE_GAIN_FOR_SUNK_SHIP_MANPOWER_FACTOR:
  def: '0.004'
  type: float
  cmt: war score gained for every manpower killed when sinking a ship
WAR_SCORE_GAIN_FOR_SUNK_SHIP_PRODUCTION_COST_FACTOR:
  def: '0.10'
  type: float
  cmt: war score gained for every IC of the sunk ship
WAR_SCORE_GAIN_FOR_SUNK_CONVOY:
  def: '0.10'
  type: float
  cmt: war score gained for every sunk convoy
PEACE_ACTION_TRANSFER_NAVY_EXPERIENCE_RETAINED:
  def: '0.25'
  type: float
  cmt: % of experience to retain after being transferred in a peace conference
CARRIER_OFFENSIVE_STANCE_SORTIE_RATIO:
  def:
    - [0.0, 0.25, 0.50, 0.75, 1.0]
  type: table
  cmt: The defensive stance sortie is 1.0 - value in index so their sum equals 1
CARRIER_OFFENSIVE_STANCE_DEFAULT_INDEX:
  def: '2'
  type: int
  cmt: The default offensive sortie index in CARRIER_OFFENSIVE_STANCE_SORTIE_RATIO
SELECTED_SORTIE_INITIAL_TIME:
  def: '24'
  type: int
  cmt: Amount of hours from combat start where the selected sortie will override the
    default one
SHIP_SUPPORT_NEED_FACTOR:
  def: '0.1'
  type: float
  cmt: The support need for a ship. This factor is multiplied with the ships dominance
    value
MAX_ADMIRAL_HEADQUARTER_ASSIGNMENTS:
  def: '3'
  type: int
  cmt: Max amount of admirals that can be assigned to naval headquarters
NAVAL_HEADQUARTER_ADJACENCY:
  def: '2'
  type: int
  cmt: How many extra steps of strategic regions from the first the naval headquarter
    provides benefits.
CONVOY_BLOCKED_BY_ENEMY_CONTROLLED_REGION:
  def: 'true'
  type: bool
  cmt: If an enemy control a sea region, consider that region as blocked
NAVAL_DOMINANCE_STRIKE_FORCE_FRACTION:
  def: '0.0006'
  type: float
  cmt: How much dominance points goes into one percent of the multiplier from strike
    force missions. ( e.g. a taskforce of 1000 dominance generates a 60% multiplier )
NAVAL_DOMINANCE_STRIKE_FORCE_MULTIREGION_DECAY:
  def: '0.05'
  type: float
  cmt: Percentage that the strike force mission's naval dominance multiplier decreases
    with for each additional assigned region
NAVAL_DOMINANCE_SPOTTING_BONUS:
  def: '0.05'
  type: float
NAVAL_DOMINANCE_ORG_RECOVERY:
  def: '0.1'
  type: float
NAVAL_DOMINANCE_SHIP_RECOVERY_CHANCE:
  def: '0.1'
  type: float
NAVAL_DOMINANCE_MINES_PLANTING_BONUS:
  def: '0.2'
  type: float
  cmt: Naval planting bonus when having naval dominance in the region
NAVAL_DOMINANCE_MINES_SWEEPING_BONUS:
  def: '0.2'
  type: float
  cmt: Naval sweeping bonus when having naval dominance in the region
NAVAL_DOMINANCE_CHANCE_OF_ACCIDENT_REDUCTION:
  def: '0.25'
  type: float
  cmt: The chance to encounter an accident during naval training would be reduced when
    having naval dominance in the region
NAVAL_INVASION_PRIORITY:
  def: '1'
  type: int
  cmt: Default convoy priority for naval invasions
NAVAL_TRANSFER_PRIORITY:
  def: '1'
  type: int
  cmt: Default convoy priority for naval transports
SUPPLY_PRIORITY:
  def: '2'
  type: int
  cmt: Default convoy priority for supplying units via sea
RESOURCE_LENDLEASE_PRIORITY:
  def: '3'
  type: int
  cmt: Default convoy priority for export lend lease
RESOURCE_EXPORT_PRIORITY:
  def: '4'
  type: int
  cmt: Default convoy priority for export trade
RESOURCE_ORIGIN_PRIORITY:
  def: '5'
  type: int
  cmt: Default convoy priority for resources shipped internally
RESOURCE_PURCHASE_PRIORITY:
  def: '6'
  type: int
  cmt: Default convoy priority for export equipment purchase
UNDERWAY_REPLENISHMENT_PRIORITY:
  def: '7'
  type: int
  cmt: Default convoy priority for underway replenishment
NAVAL_HOMEBASE_CALCULATION_DISTANCE_CUTOFF:
  def: '1000'
  type: int
  cmt: Tuning parameter for homebase calculation. Distance to normalize against.
    Everything above said value will be treated as score = 0.
NAVAL_HOMEBASE_BUILDING_SCORE_FACTOR:
  def: '0.02'
  type: float
  cmt: Tuning parameter for homebase calculation. Multiplier for how much the level of
    the naval base impacts its total score.
NAVAL_HOMEBASE_OWNERSHIP_BONUS:
  def: '0.04'
  type: float
  cmt: Tuning parameter for homebase calculation. Adds to total score based on if the
    base is owned by the country doing the calculation.
ADMIRAL_TASKFORCE_CAP:
  def: '10'
  type: int
  cmt: admirals will start getting penalties after this amount of taskforces
DETECTION_CHANCE_MULT_BASE:
  def: '0.1'
  type: float
  cmt: base multiplier value for detection chance. Later the chance is an average
    between our detection and enemy visibility, mult by surface/sub detection chance in
    the following defines.
DETECTION_CHANCE_MULT_RADAR_BONUS:
  def: '0.1'
  type: float
  cmt: detection chance bonus from radars.
DETECTION_CHANCE_MULT_AIR_SUPERIORITY_BONUS:
  def: '0.25'
  type: float
  cmt: bonus from air superiority.
MAX_CAPITALS_PER_AUTO_TASK_FORCE:
  def: '5'
  type: int
  cmt: maximum number of capital ships the auto-task force creation will put together
    when designing SurfaceActionGroup
MAX_SUBMARINES_PER_AUTO_TASK_FORCE:
  def: '30'
  type: int
  cmt: maximum number of submarines the auto-task force creation will put together when
    designing wolfpack
BEST_CAPITALS_TO_CARRIER_RATIO:
  def: '1'
  type: int
  cmt: capitals / carriers ratio used when auto-task force creation designs
    CarrierTaskForce
BEST_CAPITALS_TO_SCREENS_RATIO:
  def: '0.25'
  type: float
  cmt: capitals / screens ratio used for creating FEX groups in naval combat
COMBAT_BASE_HIT_CHANCE:
  def: '0.1'
  type: float
  cmt: base chance for hit
COMBAT_MIN_HIT_CHANCE:
  def: '0.05'
  type: float
  cmt: never less hit chance then this?
COMBAT_EVASION_TO_HIT_CHANCE:
  def: '0.007'
  type: float
  cmt: we take ship evasion stats, and mult by this value, so it gives hit chance
    reduction. So if reduction is 0.025 and ship evasion = 10, then there will be 0.25
    (25%) lower hit chance. (Fe. 50% base -25% from evasion +10% bcoz it's very close).
COMBAT_EVASION_TO_HIT_CHANCE_TORPEDO_MULT:
  def: '10.0'
  type: float
  cmt: the above evasion hit chance is multiplied by 400% if shooting with torpedoes.
    Torpedoes are slow, so evasion matters more.
MIN_HIT_PROFILE_MULT:
  def: '0.0'
  type: float
  cmt: largest hit profile penalty to hitting
COMBAT_LOW_ORG_HIT_CHANCE_PENALTY:
  def: '-0.5'
  type: float
  cmt: % of penalty applied to hit chance when ORG is very low.
COMBAT_LOW_MANPOWER_HIT_CHANCE_PENALTY:
  def: '-0.25'
  type: float
  cmt: % of penalty applied to hit chance when manpower is very low.
COMBAT_DAMAGE_RANDOMNESS:
  def: '0.5'
  type: float
  cmt: random factor in damage. So if max damage is fe. 10, and randomness is 30%, then
    damage will be between 7-10.
COMBAT_TORPEDO_CRITICAL_CHANCE:
  def: '0.1'
  type: float
  cmt: chance for critical hit from torpedo.
COMBAT_TORPEDO_CRITICAL_DAMAGE_MULT:
  def: '2.0'
  type: float
  cmt: multiplier to damage when got critical hit from torpedo. (Critical hits are
    devastating as usualy torpedo_attack are pretty high base values).
COMBAT_DAMAGE_TO_STR_FACTOR:
  def: '0.6'
  type: float
  cmt: casting damage value to ship strength multiplier. Use it ot balance the game
    difficulty.
COMBAT_DAMAGE_TO_ORG_FACTOR:
  def: '1.0'
  type: float
  cmt: casting damage value to ship organisation multiplier. Use it to balance the game
    difficulty.
NAVY_MAX_XP:
  def: '100'
  type: int
COMBAT_ON_THE_WAY_INIT_DISTANCE_BALANCE:
  def: '0.25'
  type: float
  cmt: Value to balance initial distance to arrive for ships that are "on the way"
COMBAT_CHASE_RESIGNATION_HOURS:
  def: '8'
  type: int
  cmt: Before we resign chasing enemy, give them some minimum time so the combat doesn't
    end instantly.
COMBAT_MAX_GROUPS:
  def: '1'
  type: int
  cmt: Max amount of "Fire Exchange" groups (FEX).
COMBAT_MIN_DURATION:
  def: '8'
  type: int
  cmt: Min combat duration before we can retreat. It's a balancing variable so it's not
    possible to always run with our weak ships agains big flotillas.
COMBAT_INITIAL_DURATION:
  def: '6'
  type: int
  cmt: Number of hours that is considered the "initial phase" of naval combat, used for
    modifiers like surprise attack during "initial combat"
COMBAT_RETREAT_DECISION_CHANCE:
  def: '0.22'
  type: float
  cmt: There is also random factor in deciding if we should retreat or not. That causes
    a delay in taking decision, that sooner or later will be picked. It's needed so
    damaged fast ships won't troll the combat.
COMBAT_DETECTED_CONVOYS_FROM_SURFACE_DETECTION_STAT:
  def: '0.1'
  type: float
  cmt: Each 1.0 of surface_detection that ship has (equipment stat), gives x% of convoys
    discovered from total travelling along the route.
COMBAT_BASE_CRITICAL_CHANCE:
  def: '0.05'
  type: float
  cmt: Base chance for receiving a critical chance. It get's scaled down with ship
    reliability.
COMBAT_CRITICAL_DAMAGE_MULT:
  def: '5.0'
  type: float
  cmt: Multiplier for the critical damage. Scaled down with the ship reliability.
COMBAT_ARMOR_PIERCING_CRITICAL_BONUS:
  def: '1.0'
  type: float
  cmt: Bonus to critical chance when shooter armor piercing is higher then target armor.
COMBAT_ARMOR_PIERCING_DAMAGE_REDUCTION:
  def: '0'
  type: int
  cmt: All damage reduction % when target armor is >= then shooter armor piercing.
    (depricated)
REPAIR_AND_RETURN_PRIO_LOW:
  def: '0.2'
  type: float
  cmt: % of total Strength. When below, navy will go to home base to repair.
REPAIR_AND_RETURN_PRIO_MEDIUM:
  def: '0.5'
  type: float
  cmt: % of total Strength. When below, navy will go to home base to repair.
REPAIR_AND_RETURN_PRIO_HIGH:
  def: '0.9'
  type: float
  cmt: % of total Strength. When below, navy will go to home base to repair.
REPAIR_AND_RETURN_PRIO_LOW_COMBAT:
  def: '0.6'
  type: float
  cmt: % of total Strength. When below, navy will go to home base to repair (in combat).
REPAIR_AND_RETURN_PRIO_MEDIUM_COMBAT:
  def: '0.3'
  type: float
  cmt: % of total Strength. When below, navy will go to home base to repair (in combat).
REPAIR_AND_RETURN_PRIO_HIGH_COMBAT:
  def: '0.1'
  type: float
  cmt: % of total Strength. When below, navy will go to home base to repair (in combat).
REPAIR_AND_RETURN_AMOUNT_SHIPS_LOW:
  def: '0.2'
  type: float
  cmt: % of total damaged ships, that will be sent for repair-and-return in one call.
REPAIR_AND_RETURN_AMOUNT_SHIPS_MEDIUM:
  def: '0.4'
  type: float
  cmt: % of total damaged ships, that will be sent for repair-and-return in one call.
REPAIR_AND_RETURN_AMOUNT_SHIPS_HIGH:
  def: '0.8'
  type: float
  cmt: % of total damaged ships, that will be sent for repair-and-return in one call.
REPAIR_AND_RETURN_UNIT_DYING_STR:
  def: '0.2'
  type: float
  cmt: Str below this point is considering a single ship "dying", and a high priority to
    send to repair.
AI_MAX_TASKFORCES_PER_TRAINING_OBJECTIVE:
  def: '5'
  type: int
  cmt: Max number of taskforces we desire for AI to put in each fleet that is training.
EXPERIENCE_LOSS_FACTOR:
  def: '1.00'
  type: float
  cmt: percentage of experienced solders who die when manpower is removed
NAVY_EXPENSIVE_IC:
  def: '5500'
  type: int
  cmt: How much IC is considering the fleet to be expensive. Those expensive will triger
    the alert, when are on low STR.
MISSION_MAX_REGIONS:
  def: '0'
  type: int
  cmt: Limit of the regions that can be assigned to naval mission. Set to 0 for
    unlimited.
CONVOY_EFFICIENCY_LOSS_MODIFIER:
  def: '1.25'
  type: float
  cmt: How much efficiency drops when losing convoys. If modifier is 0.5, then losing
    100% of convoys in short period, the efficiency will drop by 50%.
CONVOY_EFFICIENCY_REGAIN_AFTER_DAYS:
  def: '7'
  type: int
  cmt: Convoy starts regaining it's efficiency after X days without any convoys being
    sink.
CONVOY_EFFICIENCY_REGAIN_BASE_SPEED:
  def: '0.04'
  type: float
  cmt: How much efficiency regains every day.
CONVOY_EFFICIENCY_MIN_VALUE:
  def: '0.05'
  type: float
  cmt: To avoid complete 0% efficiency, set the lower limit.
CONVOY_ROUTE_SIZE_CONVOY_SCALE:
  def: '0.5'
  type: float
  cmt: scales impact of convoy route size (0 to turn off)
ANTI_AIR_TARGETTING_TO_CHANCE:
  def: '0.2'
  type: float
  cmt: Balancing value to convert averaged equipment stats (anti_air_targetting and
    naval_strike_agility) to probability chances of airplane being hit by navies AA.
ANTI_AIR_ATTACK_TO_AMOUNT:
  def: '0.01'
  type: float
  cmt: Balancing value to convert equipment stat anti_air_attack to the random % value
    of airplanes being hit.
CONVOY_SINKING_SPILLOVER:
  def: '0.5'
  type: float
  cmt: Damaged convoys roll for if they sink in the end of combat by accumulating the
    damage. This scales that chance.
UNIT_EXPERIENCE_PER_COMBAT_HOUR:
  def: '10'
  type: int
UNIT_EXPERIENCE_SCALE:
  def: '1'
  type: int
EXPERIENCE_FACTOR_CONVOY_ATTACK:
  def: '0.04'
  type: float
EXPERIENCE_FACTOR_NON_CARRIER_GAIN:
  def: '0.04'
  type: float
  cmt: Xp gain by non-carrier ships in the combat
EXPERIENCE_FACTOR_CARRIER_GAIN:
  def: '0.08'
  type: float
  cmt: Xp gain by carrier ships in the combat
FIELD_EXPERIENCE_SCALE:
  def: '0.075'
  type: float
FIELD_EXPERIENCE_MAX_PER_DAY:
  def: '50'
  type: int
  cmt: Most xp you can gain per day
LEADER_EXPERIENCE_SCALE:
  def: '1.0'
  type: float
NAVAL_HEADQUARTERS_EXPERIENCE_SCALE:
  def: '0.125'
  type: float
  cmt: Characters assigned to a naval HQ will gain 15% of all experience from taskforces
    in their regions
BATTLE_NAME_VP_FACTOR:
  def: '100'
  type: int
  cmt: Name is given by ((VP value) * BATTLE_NAME_VP_FACTOR) / (Distance VP -> battle)
BATTLE_NAME_VP_CUTOFF:
  def: '1.0'
  type: float
  cmt: If best score of above calculation is below this, name will be that of region.
AMPHIBIOUS_LANDING_PENALTY:
  def: '-0.5'
  type: float
  cmt: amphibious landing penalty
AMPHIBIOUS_INVADE_SPEED_BASE:
  def: '0.5'
  type: float
  cmt: every hour movement progress on amphibious invasion
AMPHIBIOUS_INVADE_MOVEMENT_COST:
  def: '24.0'
  type: float
  cmt: total progress cost of movement while amphibious invading
AMPHIBIOUS_INVADE_ATTACK_LOW:
  def: '0.2'
  type: float
  cmt: low and high cap of attack modifier scale. Scale interpolated by invasion
    progress.
AMPHIBIOUS_INVADE_ATTACK_HIGH:
  def: '1.0'
  type: float
AMPHIBIOUS_INVADE_DEFEND_LOW:
  def: '1.5'
  type: float
  cmt: low and high cap of defend modifier scale. Scale interpolated by invasion
    progress.
AMPHIBIOUS_INVADE_DEFEND_HIGH:
  def: '1.0'
  type: float
AMPHIBIOUS_INVADE_LANDING_PENALTY_DECREASE:
  def: '3.5'
  type: float
  cmt: scale of bonus that decreases "amphibious penalty" during combat, relative to
    invading transporter tech.
BASE_CARRIER_SORTIE_EFFICIENCY:
  def: '0.5'
  type: float
  cmt: factor of planes that can sortie by default from a carrier
CONVOY_ATTACK_BASE_FACTOR:
  def: '0.15'
  type: float
  cmt: base % of convoys that get intercepted
NAVAL_SPEED_MODIFIER:
  def: '0.1'
  type: float
  cmt: basic speed control
NAVAL_RANGE_TO_INGAME_DISTANCE:
  def: '0.12'
  type: float
  cmt: Scale the ship stats "naval_range" to the ingame distance
NAVAL_INVASION_PREPARE_DAYS:
  def: '60'
  type: int
  cmt: base days needed to prepare a naval invasion
NAVAL_INVASION_PLAN_CAP:
  def: '1'
  type: int
  cmt: base cap of naval invasions can be planned at the same time
BASE_NAVAL_INVASION_DIVISION_CAP:
  def: '4'
  type: int
  cmt: base cap of divisions that can be assigned in a naval invasion
NAVAL_COMBAT_RESULT_TIMEOUT_YEARS:
  def: '2'
  type: int
  cmt: after that many years, we clear the naval combat results, so they don't get stuck
    forever in the memory.
CONVOY_LOSS_HISTORY_TIMEOUT_MONTHS:
  def: '24'
  type: int
  cmt: after this many months remove the history of lost convoys to not bloat savegames
    and memory since there is no way to see them anyway
NAVAL_TRANSFER_BASE_SPEED:
  def: '6'
  type: int
  cmt: base speed of units on water being transported
NAVAL_TRANSFER_BASE_NAVAL_DIST_ADD:
  def: '100'
  type: int
  cmt: Extra cost for naval movement ( compared to land movement ) when deciding what
    ports to use for a naval transfer
NAVAL_TRANSFER_BASE_NAVAL_DIST_MULT:
  def: '20'
  type: int
  cmt: Multiplier for the cost of naval movement ( compared to land movement ) when
    deciding what ports to use for naval transfer
NAVAL_COMBAT_PLANE_MIN_STACKING_PENALTY:
  def: '80'
  type: int
  cmt: How many planes flying in a naval combat before penalties are introduced
NAVAL_COMBAT_PLANE_STACKING_PENALTY_EFFECT:
  def: '0.005'
  type: float
  cmt: Each plane above the optimal amount decreases the amount of airplanes being able
    to takeoff by such %. Subject to diminishing returns
SHIP_SILHOUETTE_VALUE_PLANES_CAPITAL:
  def: '10'
  type: int
  cmt: For dynamic plane efficacy, silhouette value (nominally in planes, but very
    abstract)
SHIP_SILHOUETTE_VALUE_PLANES_SCREEN:
  def: '5'
  type: int
  cmt: As Above. This one would be nice to split by type, but that's problematic.
SHIP_SILHOUETTE_VALUE_PLANES_CARRIER:
  def: '16'
  type: int
  cmt: As Above
SHIP_SILHOUETTE_VALUE_PLANES_SUPPORT:
  def: '3'
  type: int
  cmt: As Above
SHIP_SILHOUETTE_VALUE_PLANES_CONVOY:
  def: '4'
  type: int
  cmt: As Above
SHIP_SILHOUETTE_VALUE_PLANES_SUBMARINE:
  def: '7'
  type: int
  cmt: As Above
SCREEN_CAP_REDUCTION_FACTOR:
  def: '0.02'
  type: float
  cmt: Reduces screen silhouette weight if there are caps present, screenval *
    1/(1+caps*weight)
SHORE_BOMBARDMENT_CAP:
  def: '0.33'
  type: float
ANTI_AIR_TARGETING:
  def: '0.9'
  type: float
  cmt: how good ships are at hitting aircraft
MIN_TRACTED_ASSIST_DAMAGE_RATIO:
  def: '0.05'
  type: float
  cmt: How much damage counts as assist damage
SUPPLY_NEED_FACTOR:
  def: '1'
  type: int
  cmt: multiplies supply usage
DECRYPTION_SPOTTING_BONUS:
  def: '0.2'
  type: float
DISBAND_MANPOWER_LOSS:
  def: '0.0'
  type: float
MANPOWER_LOSS_RATIO_ON_SUNK:
  def: '0.5'
  type: float
  cmt: sunk ships will lose this ratio of their current manpower
MANPOWER_LOSS_RATIO_ON_STR_LOSS:
  def: '0.5'
  type: float
  cmt: losing strength will make you also lose manpower at this ratio of total manpower
MIN_MANPOWER_RATIO_TO_DROP:
  def: '0.1'
  type: float
  cmt: ships will not lose man power to below this ratio
DAILY_MANPOWER_GAIN_RATIO:
  def: '0.05'
  type: float
  cmt: the ships not in combat will be able to gain this ratio of their max manpower
PRIDE_OF_THE_FLEET_UNASSIGN_COST:
  def: '100'
  type: int
  cmt: cost to unassign/replace pride of the fleet
PRIDE_OF_THE_FLEET_LOST_TEMP_MODIFIER_DURATION:
  def: '30'
  type: int
  cmt: duration for temp modifiers that you get when you lose your pride of the fleet
XP_GAIN_FACTOR:
  def: '1.0'
  type: float
  cmt: xp gain factor for navy
NAVAL_TRANSFER_DAMAGE_REDUCTION:
  def: '0.25'
  type: float
  cmt: its hard to specifically balance 1-tick naval strikes vs unit transports so here
    is a factor for it
CARRIER_ONLY_COMBAT_ACTIVATE_TIME:
  def: '0'
  type: int
  cmt: hours from start of combat when carriers get to fight
CAPITAL_ONLY_COMBAT_ACTIVATE_TIME:
  def: '6'
  type: int
  cmt: hours from start of combat when only carriers, capitals and subs get to attack
ALL_SHIPS_ACTIVATE_TIME:
  def: '8'
  type: int
  cmt: hours where all get to attack
MINIMUM_SHIP_SPEED:
  def: '1.0'
  type: float
  cmt: slowest speed a ship can have
REPAIR_SPLIT_TASKFORCE_SIZE:
  def: '5'
  type: int
  cmt: if a country does not have empty naval naval bases for repairs, it will split
    ships with this sizes and distribute them around
NAVY_REPAIR_BASE_SEARCH_SCORE_PER_SHIP_WAITING_EXTRA_SHIP:
  def: '5'
  type: int
  cmt: if a naval base has more ships than it can repair, it will get penalties
NAVY_REPAIR_BASE_SEARCH_SCORE_PER_SLOT:
  def: '1.0'
  type: float
  cmt: while searching for a naval base for repairs, the bases gets a bonus to their
    scores per empty slot they have
NAVY_REPAIR_BASE_SEARCH_BOOST_FOR_SAME_COUNTRY:
  def: '5'
  type: int
  cmt: while searching for a naval base for repairs, your own bases gets a bonus
NAVY_REPAIR_BASE_PRIORITY_THRESHOLD_LOW:
  def: '2'
  type: int
  cmt: bases with a level above this value will be set to low prio     (bases between
    these levels will get medium prio)
NAVY_REPAIR_BASE_PRIORITY_THRESHOLD_HIGH:
  def: '7'
  type: int
  cmt: bases with a level above this value will be set to high prio (bases between these
    levels will get medium prio)
CONVOY_SPOTTING_COOLDOWN:
  def: '0.3'
  type: float
  cmt: % of travel time
CONVOY_SPOTTING_COOLDOWN_MIN:
  def: '36'
  type: int
  cmt: minimum cooldown time
CONVOY_SPOTTING_COOLDOWN_MAX:
  def: '168'
  type: int
  cmt: maximum cooldown time
CONVOY_SPOTTING_COOLDOWN_MIN_FROM_EFFICIENCY:
  def: '15'
  type: int
  cmt: clamped min value after screening efficiency has been applied
AIR_BASE_DOMINANCE_FACTOR:
  def: '0.02'
  type: float
  cmt: Percentage factor per air base level in region towards naval dominance target
    value
RADAR_DOMINANCE_FACTOR:
  def: '0.05'
  type: float
  cmt: Percentage factor per radar level in region towards naval dominance target value
DOMINANCE_CONTROLLED_THRESHOLD_RATIO:
  def: '0.60'
  type: float
  cmt: Percentage of needed dominance control over enemies for you and friendlies to
    control a strategic sea region
MISSION_FUEL_COSTS:
  def:
    - [0.0]  # HOLD (consumes fuel HOLD_MISSION_MOVEMENT_COST fuel while moving)
    - [1.0]  # PATROL
    - [1.0]  # STRIKE FORCE (does not cost fuel at base, and uses IN_COMBAT_FUEL_COST in combat. this is just for the movement in between)
    - [1.0]  # CONVOY RAIDING
    - [1.0]  # CONVOY ESCORT
    - [1.0]  # MINES PLANTING
    - [1.0]  # MINES SWEEPING
    - [0.6]  # TRAIN
    - [0.0]  # RESERVE_FLEET (consumes fuel HOLD_MISSION_MOVEMENT_COST fuel while moving)
    - [1.0]  # NAVAL_INVASION_SUPPORT (does not cost fuel at base, only costs while doing bombardment and escorting units)
  type: table
  cmt: fuel cost for each mission
MISSION_FUEL_COSTS_PRIO_FACTOR:
  def:
    - [0.0]  # HOLD (consumes fuel HOLD_MISSION_MOVEMENT_COST fuel while moving)
    - [1.0]  # PATROL
    - [1.0]  # STRIKE FORCE (does not cost fuel at base, and uses IN_COMBAT_FUEL_COST in combat. this is just for the movement in between)
    - [0.6]  # CONVOY RAIDING
    - [0.6]  # CONVOY ESCORT
    - [0.5]  # MINES PLANTING
    - [0.3]  # MINES SWEEPING
    - [0.6]  # TRAIN
    - [0.0]  # RESERVE_FLEET (consumes fuel HOLD_MISSION_MOVEMENT_COST fuel while moving)
    - [1.0]  # NAVAL_INVASION_SUPPORT (does not cost fuel at base, only costs while doing bombardment and escorting units)
  type: table
  cmt: Prio fuel cost ratio for each mission. Highet value means that mission is more
    important to perform with regards to fuel usage
HOLD_MISSION_MOVEMENT_COST:
  def: '1.0'
  type: float
  cmt: ships on hold cost this much fuel while moving
ON_BASE_FUEL_COST:
  def: '0.0'
  type: float
  cmt: ships that waits at naval bases cost this ratio
STRIKE_FORCE_ON_BASE_FUEL_COST_FACTOR:
  def: '0.25'
  type: float
  cmt: fuel cost for naval strike mission in port
IN_COMBAT_FUEL_COST:
  def: '2.0'
  type: float
  cmt: ships in combat will get this ratio for fuel cost
TRAINING_FUEL_COST_FOR_ESCORT_SHIPS:
  def: '0.15'
  type: float
  cmt: ships that are on training mission but not training (ie they are at max xp and
    training will cancel at max xp) will consume this ratio of fuel
MAX_FUEL_FLOW_MULT:
  def: '2.0'
  type: float
  cmt: max fuel flow ratio for ships, which will be multiplied by supply
FUEL_COST_MULT:
  def: '0.10'
  type: float
  cmt: fuel multiplier for all naval missions
OUT_OF_FUEL_SPEED_FACTOR:
  def: '-0.75'
  type: float
OUT_OF_FUEL_RANGE_FACTOR:
  def: '0'
  type: int
OUT_OF_FUEL_ATTACK_FACTOR:
  def: '-0.5'
  type: float
OUT_OF_FUEL_TORPEDO_FACTOR:
  def: '-0.8'
  type: float
UNDERWAY_REPLENISHMENT_RANGE_FACTOR:
  def: '0.4'
  type: float
  cmt: bonus factor applied to task force's range when underway replenishment is
    activated (e.g. 0.2 means +20%)
UNDERWAY_REPLENISHMENT_CONVOY_COST_PER_FUEL:
  def: '0.28'
  type: float
  cmt: Cost in convoys for underway replenishment multiplied by max daily fuel
    consumption (rounded up)
MISSION_SPREADS:
  def:
    - [0.0]  # HOLD
    - [0.0]  # PATROL
    - [0.0]  # STRIKE FORCE
    - [0.0]  # CONVOY RAIDING
    - [0.0]  # CONVOY ESCORT
    - [0.7]  # MINES PLANTING
    - [0.7]  # MINES SWEEPING
    - [0.5]  # TRAIN
    - [0.0]  # RESERVE_FLEET
    - [0.0]  # NAVAL_INVASION_SUPPORT
  type: table
  cmt: mission spreads in the case a ship join combat, which is calculated for number of
    ships that will be in combat. 1 means no ship will be at start
MISSION_DEFAULT_SPREAD_BASE:
  def: '1.0'
  type: float
  cmt: multiplier for mission spreads. higher = less ships on start
AGGRESSION_SETTINGS_VALUES:
  def:
    - [0]  # do not engage
    - [0.5]  # low
    - [0.9]  # medium
    - [2.0]  # high
    - [10000]  # I am death incarnate!
  type: table
  cmt: ships will use this values while deciding to attack enemies
AGGRESION_MULTIPLIER_FOR_COMBAT:
  def: '1.2'
  type: float
  cmt: ships are more aggresive in combat
AGGRESSION_ARMOR_EFFICIENCY_MULTIPLIER:
  def: '1.0'
  type: float
  cmt: armor to enemy piercing ratio is multiplied by this value, which will increase
    the strength of ships while considering them for aggression
AGGRESSION_MIN_ARMOR_EFFICIENCY:
  def: '0.5'
  type: float
  cmt: armor multiplier has a min and max caps while being factored in aggression
AGGRESSION_MAX_ARMOR_EFFICIENCY:
  def: '1.5'
  type: float
  cmt: armor multiplier has a min and max caps while being factored in aggression
AGGRESSION_LIGHT_GUN_EFFICIENCY_ON_LIGHT_SHIPS:
  def: '1.0'
  type: float
  cmt: ratio for scoring for different gun types against light ships
AGGRESSION_HEAVY_GUN_EFFICIENCY_ON_LIGHT_SHIPS:
  def: '0.25'
  type: float
  cmt: ratio for scoring for different gun types against light ships
AGGRESSION_TORPEDO_EFFICIENCY_ON_LIGHT_SHIPS:
  def: '0.1'
  type: float
  cmt: ratio for scoring for different gun types against light ships
AGGRESSION_LIGHT_GUN_EFFICIENCY_ON_HEAVY_SHIPS:
  def: '0.1'
  type: float
  cmt: ratio for scoring for different gun types against heavy ships
AGGRESSION_HEAVY_GUN_EFFICIENCY_ON_HEAVY_SHIPS:
  def: '1.0'
  type: float
  cmt: ratio for scoring for different gun types against heavy ships
AGGRESSION_TORPEDO_EFFICIENCY_ON_HEAVY_SHIPS:
  def: '1.1'
  type: float
  cmt: ratio for scoring for different gun types against heavy ships
AGGRESSION_CONVOY_STRENGTH_FACTOR:
  def: '0.3'
  type: float
  cmt: convoys in combat gets a penalty to their strength in aggression calculations
SUBMARINE_ESCAPE_RATIOS:
  def:
    - [1000]  # do not engage
    - [3.0]  # low
    - [1.0]  # medium
    - [0.5]  # high
    - [0.1]  # I am death incarnate!
  type: table
  cmt: subs will escape battle in convoy raid if there are enemies that can attack
MIN_REPAIR_FOR_JOINING_COMBATS:
  def:
    - [0.0]  # do not repair
    - [0.5]  # low
    - [0.7]  # medium
    - [0.9]  # high
  type: table
  cmt: strikeforces/patrol forces will not join combats if they are not repaired enough
ORG_COST_WHILE_MOVING:
  def:
    - [0.3]  # HOLD
    - [0.2]  # PATROL
    - [0.25]  # STRIKE FORCE
    - [0.2]  # CONVOY RAIDING
    - [0.2]  # CONVOY ESCORT
    - [0.2]  # MINES PLANTING
    - [0.2]  # MINES SWEEPING
    - [0.2]  # TRAIN
    - [0.3]  # RESERVE_FLEET
    - [0.2]  # NAVAL_INVASION_SUPPORT
  type: table
  cmt: org cost while the ships are moving
ORG_COST_WHILE_MOVING_IN_MISSION_ZONE:
  def:
    - [0.0]  # HOLD
    - [0.0]  # PATROL
    - [0.0]  # STRIKE FORCE
    - [0.0]  # CONVOY RAIDING
    - [0.0]  # CONVOY ESCORT
    - [0.0]  # MINES PLANTING
    - [0.0]  # MINES SWEEPING
    - [0.0]  # TRAIN
    - [0.0]  # RESERVE_FLEET
    - [0.0]  # NAVAL_INVASION_SUPPORT
  type: table
  cmt: org cost while moving in mission zone
MAX_ORG_ON_MANUAL_MOVE:
  def: '0.66'
  type: float
  cmt: org will clamped to this ratio on manual move
MIN_ORG_ON_MANUAL_MOVE:
  def: '0.1'
  type: float
  cmt: org will clamped to this ratio on manual move
INITIAL_ALLOWED_DOCKYARD_RATIO_FOR_REPAIRS:
  def: '0.25'
  type: float
  cmt: initially countries will allocate this ratio of dockyards for repairs
FIELD_EXPERIENCE_FACTOR:
  def: '0.7'
  type: float
  cmt: Factor all naval experience gain from missions by this
MISSION_DAILY_EXP_GAIN_PER_SHIP:
  def: '0.3'
  type: float
  cmt: Amount of exp each ship gain every 24h while training (before modifiers)
MISSION_DAILY_COUNTRY_EXP_FACTOR:
  def: '0.01'
  type: float
  cmt: Factor used to scale the Daily Country Navy XP gain
MISSION_DAILY_COUNTRY_EXP_MANPOWER_FACTOR:
  def: '0.006'
  type: float
  cmt: Factor used to scale the sum of the on mission manpower for the Daily Country
    Navy XP gain
MISSION_DAILY_COUNTRY_EXP_MANPOWER_RATIO_FACTOR:
  def: '0.01'
  type: float
  cmt: Factor used to scale the sum of the manpower divided by the country's number of
    ship for the Daily Country Navy XP gain
MISSION_DAILY_COUNTRY_EXP_SHIP_RATIO_FACTOR:
  def: '300.0'
  type: float
  cmt: Factor used to scale the ratio of ships on mission for the Daily Country Navy XP
    gain
MISSION_EXP_RATIOS:
  def:
    - [0.0]  # HOLD
    - [0.005]  # PATROL
    - [0.005]  # STRIKE FORCE
    - [0.005]  # CONVOY RAIDING
    - [0.005]  # CONVOY ESCORT
    - [0.005]  # MINES PLANTING
    - [0.005]  # MINES SWEEPING
    - [1.0]  # TRAIN
    - [0.0]  # RESERVE_FLEET
    - [0.005]  # NAVAL_INVASION_SUPPORT
  type: table
  cmt: experience multipliers for different mission types
MISSION_DOMINANCE_RATIOS:
  def:
    - [0.0]  # HOLD
    - [1.0]  # PATROL
    - [1.0]  # STRIKE FORCE
    - [0.5]  # CONVOY RAIDING
    - [0.5]  # CONVOY ESCORT
    - [0.3]  # MINES PLANTING
    - [0.3]  # MINES SWEEPING
    - [0.0]  # TRAIN
    - [0.0]  # RESERVE_FLEET
    - [1.0]  # NAVAL_INVASION_SUPPORT
  type: table
  cmt: dominance multipliers for different mission types
DOMINANCE_PER_SHIP_PER_RANGE_NEUTRAL:
  def: '2000'
  type: int
  cmt: ship range where there is no penalty nor bonus to naval dominance, below or above
    this will be scaled accordingly with penalty or bonus, min value is 0
DOMINANCE_PER_SHIP_PER_SPEED_NEUTRAL:
  def: '20'
  type: int
  cmt: ship speed where there is no penalty nor bonus to naval dominance, below or above
    this will be scaled accordingly with penalty or bonus, min value is 0
DOMINANCE_PER_SHIP_PER_CARRIER_SIZE:
  def: '0.1'
  type: float
  cmt: bonus to dominance based on the carrier size - e.g. regular carrier hangar has
    carrier_size of 2, so it would be a bonus of 2 *
    DOMINANCE_PER_SHIP_PER_CARRIER_SIZE, min value is 0
DOMINANCE_PER_SHIP_PER_HEAVY_GUN_ATTACK:
  def: '0.01'
  type: float
  cmt: bonus to dominance based on the heavy attack, min value is 0
NAVAL_MINES_IN_REGION_MAX:
  def: '1000.0'
  type: float
  cmt: Max number of mines that can be layed by the ships. The value should be hidden
    from the user, as we present % so it's an abstract value that should be used for
    balancing.
NAVAL_MINES_PLANTING_SPEED_MULT:
  def: '0.01'
  type: float
  cmt: Value used to overall balance of the speed of planting naval mines
NAVAL_MINES_SWEEPING_SPEED_MULT:
  def: '0.009'
  type: float
  cmt: Value used to overall balance of the speed of sweeping naval mines
NAVAL_MINES_DECAY_AT_PEACE_TIME:
  def: '0.25'
  type: float
  cmt: How fast mines are decaying in peace time. Planting mines in peace time may be
    exploitable, so it's blocked atm. That's why after war we should decay them too.
NAVAL_MINES_SWEEPERS_REDUCTION_ON_PENALTY_EFFECT:
  def: '3.3'
  type: float
  cmt: How much is the task force's sweeping attribute reducing the penalty effect.
NAVAL_MINES_INTEL_DIFF_FACTOR:
  def: '0.5'
  type: float
  cmt: Better our decryption over enemy encryption will reduce the penalties from the
    enemy mines in the region. This value is a factor to be used for balancing.
ATTRITION_WHILE_MOVING_FACTOR:
  def: '1.2'
  type: float
  cmt: attrition multiplier while moving & doing missions
ATTRITION_DAMAGE_ORG:
  def: '0.01'
  type: float
  cmt: damage from attrition to Organisation (relative to max org)
ATTRITION_DAMAGE_STR:
  def: '0.03'
  type: float
  cmt: damage from attrition to str (relative to max str)
ATTRITION_STR_DAMAGE_CHANCE:
  def: '0.2'
  type: float
  cmt: chance to get damaged at highest attrition
NAVAL_ACCIDENT_CHANCE_REDUCTION_ON_POTF:
  def: '0.01'
  type: float
  cmt: Scale of the current chance for an accident to happen, applied for the pride of
    the fleet.
NAVAL_ACCIDENT_CRITICAL_HIT_CHANCE_REDUCTION_POTF:
  def: '0.01'
  type: float
  cmt: Scale of the current chance for a critical hit when an accident happens, applied
    for the pride of the fleet.
NAVAL_MINES_ACCIDENT_CRITICAL_HIT_CHANCES:
  def: '0.14'
  type: float
  cmt: If an accident happens, how likely it is to be a critical hit (caused by naval
    mines)
NAVAL_MINES_ACCIDENT_CRITICAL_HIT_DAMAGE_SCALE:
  def: '5.0'
  type: float
  cmt: Scale the value below in case of critical hit (caused by naval mines)
NAVAL_MINES_ACCIDENT_STRENGTH_LOSS:
  def: '50.0'
  type: float
  cmt: Amount of strength loss when hit by naval mine
NAVAL_MINES_ACCIDENT_ORG_LOSS_FACTOR:
  def: '0.5'
  type: float
  cmt: Amount of strength loss when hit by naval mine
TRAINING_ACCIDENT_CHANCES:
  def: '0.02'
  type: float
  cmt: Chances one ship get damage each hour while on training
TRAINING_ACCIDENT_CRITICAL_HIT_CHANCES:
  def: '0.3'
  type: float
  cmt: If an accident happens, how likely it is to be a critical hit
TRAINING_ACCIDENT_CRITICAL_HIT_DAMAGE_SCALE:
  def: '4.0'
  type: float
  cmt: Scale the value below in case of critical hit
TRAINING_ACCIDENT_STRENGTH_LOSS:
  def: '4.0'
  type: float
  cmt: Amount of strength loss in a training accident
TRAINING_ACCIDENT_STRENGTH_LOSS_FACTOR:
  def: '0.05'
  type: float
  cmt: Amount of strength loss in a training accident, propotional to the maximum
    strength of the ship
TRAINING_ACCIDENT_ORG_LOSS_FACTOR:
  def: '0.3'
  type: float
  cmt: Amount of current organization the ship lose
ACCIDENTS_CHANCE_BALANCE_FACTOR:
  def: '0.04'
  type: float
  cmt: General chance for naval accidents for balancing the gameplay.
TRAINING_EXPERIENCE_FACTOR:
  def: '0.3'
  type: float
  cmt: Amount of exp each ship gain every 24h while training (before modifiers)
TRAINING_DAILY_COUNTRY_EXP_FACTOR:
  def: '0.001'
  type: float
  cmt: Factor used to scale the Daily Country Navy XP gain from training
TRAINING_DAILY_COUNTRY_EXP_MANPOWER_FACTOR:
  def: '0.006'
  type: float
  cmt: Factor used to scale the sum of the training manpower for the Daily Country Navy
    XP gain
TRAINING_DAILY_COUNTRY_EXP_MANPOWER_RATIO_FACTOR:
  def: '0.01'
  type: float
  cmt: Factor used to scale the sum of the manpower divided by the country's number of
    ship for the Daily Country Navy XP gain
TRAINING_DAILY_COUNTRY_EXP_SHIP_RATIO_FACTOR:
  def: '300.0'
  type: float
  cmt: Factor used to scale the ratio of training ships for the Daily Country Navy XP
    gain
TRAINING_MAX_DAILY_COUNTRY_EXP:
  def: '1'
  type: int
  cmt: Maximum navy XP daily gain
TRAINING_MIN_STRENGTH:
  def: '0.1'
  type: float
  cmt: if strength is less than this, the unit will not contribute to training and cant
    be damaged by training
TRAINING_ORG:
  def: '0.2'
  type: float
  cmt: max organization on traiaing mission
BASE_SPOTTING:
  def: '1'
  type: int
  cmt: base spotting percentage for navy
BASE_SPOTTING_FROM_RADAR:
  def: '5'
  type: int
  cmt: base spotting percentage that comes from full radar coverage
NAVY_SPOTTER_DETECTION_FACTOR:
  def: '0.1'
  type: float
  cmt: multiplier for task forces' detection value before logistic transform
BASE_SPOTTING_FROM_NAVY:
  def: '10'
  type: int
  cmt: base spotting percentage that comes from task forces in area
AIR_SPOTTER_NORMALIZED_AIRWING_SIZE:
  def: '100'
  type: int
  cmt: each plane will contribute 1/this of the air-wing's detection stat
AIR_SPOTTER_DETECTION_FACTOR:
  def: '0.025'
  type: float
  cmt: multiplier for air-wings' detection value before logistic transform
BASE_SPOTTING_FROM_AIR:
  def: '20'
  type: int
  cmt: base spotting percentage that comes from air-wings in area
BASE_SPOTTING_FROM_DECRYPTION:
  def: '10'
  type: int
  cmt: base spotting percentage that comes from decryption, can go negative (enemy
    decryption is subtracted)
MIN_SPOTTING_PROGRESS:
  def: '0.01'
  type: float
  cmt: Minimum spotting progress (in percent) per hourly tick
AIR_MISSION_SPOTTING_FACTORS:
  def:
    - [0.50]  # AIR_SUPERIORITY
    - [0]  # CAS
    - [0.25]  # INTERCEPTION
    - [0]  # STRATEGIC_BOMBER
    - [0.50]  # NAVAL_BOMBER
    - [0]  # DROP_NUKE
    - [0]  # PARADROP
    - [0.25]  # NAVAL_KAMIKAZE
    - [0]  # PORT_STRIKE
    - [0]  # ATTACK_LOGISTICS
    - [0]  # AIR_SUPPLY
    - [0]  # TRAINING
    - [0.25]  # NAVAL_MINES_PLANTING
    - [0.50]  # NAVAL_MINES_SWEEPING
    - [1.00]  # RECON
    - [1.50]  # NAVAL_PATROL
  type: table
  cmt: Multiplier for air-wings' spotting contribution per mission type
MIN_HOURS_TO_SHUFFLE_NEWLY_ASSIGNED_PATROLS:
  def: '7 * 24'
  type: string
  cmt: if a fleet has less patrol than it needs to cover all of it areas, it will
    shuffle the patrols around. it will wait this much hour before shuffling a task
    force to new area
SPOTTING_ENEMY_SPOTTING_MULTIPLIER_FOR_RUNNING_AWAY:
  def: '0.80'
  type: float
  cmt: enemy spotting is multiplied by this value to simulate running away
SPOTTING_MULTIPLIER_FOR_SURFACE:
  def: '1.0'
  type: float
  cmt: task force surface spotting value is multiplied by this and added to spotting
    percentage every hour
SPOTTING_MULTIPLIER_FOR_SUB:
  def: '1.0'
  type: float
  cmt: task force sub spotting value is multiplied by this and added to spotting
    percentage every hour
SPOTTING_SPEED_MULT_FOR_RUNNING_AWAY:
  def: '0.5'
  type: float
  cmt: task forces that does not want to engage will reduce enemy spotting rate every
    hour by speed diff mult this ratio
SPOTTING_SPEED_MULT_FOR_CATCHING_UP:
  def: '0.2'
  type: float
  cmt: speed diff bonus rate that is added to spotting every hour
SPOTTING_MISSION_DETECTION_THRESHOLD_LOW:
  def: '10.0'
  type: float
  cmt: value between 0 and 100 above which to show very coarse information about the
    spotted task force
SPOTTING_MISSION_DETECTION_THRESHOLD_MEDIUM:
  def: '70.0'
  type: float
  cmt: value between 0 and 100 above which to show coarse information about the spotted
    task force. Note: accurate information are shown when spotting reach 100.
NAVY_VISIBILITY_BONUS_ON_RETURN_FOR_REPAIR:
  def: '0.9'
  type: float
  cmt: Multiplier for the surface/sub visiblity when the heavily damaged fleet is
    returning to the home base for reparation. 1.0 = no bonus. 0.0 = invisible.
VISIBILITY_MULTIPLIER_FOR_SPOTTING:
  def: '0.1'
  type: float
  cmt: multiplier for visibility stat
INTEL_LEVEL_LOW_HALF_RANGE_PERCENTAGE:
  def: '10'
  type: int
  cmt: Integer representing the maximum offset of the displayed value to the original,
    in percentage (divided by 100 in code). For spotting level "low".
INTEL_LEVEL_MEDIUM_HALF_RANGE_PERCENTAGE:
  def: '5'
  type: int
  cmt: Same as above but for the spotting level "medium"
INTEL_LEVEL_LOW_HALF_RANGE_MIN_SHIPS:
  def: '3'
  type: int
  cmt: If the percentage of the value is lower than this, use this value instead. For
    spotting level "low"
INTEL_LEVEL_LOW_HALF_RANGE_MIN_CAPITALS:
  def: '1'
  type: int
  cmt: Same as above but for capital ships
INTEL_LEVEL_MEDIUM_HALF_RANGE_MIN_SHIPS:
  def: '1'
  type: int
  cmt: If the percentage of the value is lower than this, use this value instead. For
    spotting level "medium"
INTEL_LEVEL_MEDIUM_HALF_RANGE_MIN_CAPITALS:
  def: '1'
  type: int
  cmt: Same as above but for capital ships. NOTE: overriden to 0 if the total number of
    ships in the task force is less than four.
INTEL_LEVEL_LOW_STRENGTH_ESTIMATE_HALF_RANGE_PERCENTAGE:
  def: '20'
  type: int
  cmt: Integer representing the maximum offset of the estimated enemy strength to the
    original, in percentage (divided by 100 in code). For spotting level "low".
INTEL_LEVEL_MEDIUM_STRENGTH_ESTIMATE_HALF_RANGE_PERCENTAGE:
  def: '10'
  type: int
  cmt: Same as above for spotting level "medium"
BASE_SPOTTING_SPEED:
  def: '0.0'
  type: float
  cmt: daily base spotting speed
BASE_ESCAPE_SPEED:
  def: '0.045'
  type: float
  cmt: daily base escape speed (gained as percentagE)
SPEED_TO_ESCAPE_SPEED:
  def: '0.95'
  type: float
  cmt: ratio to converstion from ship speed to escape speed (divided by hundred)
ESCAPE_SPEED_PER_COMBAT_DAY:
  def: '0.01'
  type: float
  cmt: daily increase in escape speed during combat duration
MAX_ESCAPE_SPEED_FROM_COMBAT_DURATION:
  def: '0.15'
  type: float
  cmt: max escape speed that will be gained from combat duration
ESCAPE_SPEED_SUB_BASE:
  def: '0.08'
  type: float
  cmt: subs get faster escape speed. gets replaced by hidden version below if hidden
ESCAPE_SPEED_HIDDEN_SUB:
  def: '0.18'
  type: float
  cmt: hidden subs get faster escape speed
SUB_DETECTION_CHANCE_BASE:
  def: '5'
  type: int
  cmt: to start spotting a submarine, a dice is rolled and checked if it succeeds this
    percentage. if not, that enemy sub force won't be spotted on this tick
SUB_DETECTION_CHANCE_BASE_SPOTTING_EFFECT:
  def: '0.5'
  type: float
  cmt: effect of base spotting for initial spotting of pure submarine forces. this along
    with next value is added together and rolled against a random to start spotting
SUB_DETECTION_CHANCE_SPOTTING_SPEED_EFFECT:
  def: '2.0'
  type: float
  cmt: effect of spotting speed for initial spotting of pure submarine forces. this
    along with prev value is added together and rolled against a random to start
    spotting
SUB_DETECTION_CHANCE_BASE_SPOTTING_POW_EFFECT:
  def: '1.5'
  type: float
  cmt: effect of spotting speed will be powered by this for initial spotting of pure
    submarine forces. this along with prev value is added together and rolled against a
    random to start spotting
BASE_CONVOY_SPOTTING_SPEED:
  def: '0.0'
  type: float
  cmt: daily base spotting speed against convoys
BASE_UNIT_TRANSFER_SPOTTING_SPEED:
  def: '0.0'
  type: float
  cmt: daily base spotting speed against unit trans
BASE_NAVAL_INVASION_SPOTTING_SPEED:
  def: '0.0'
  type: float
  cmt: daily base spotting speed against unit transfers
CONVOY_SPOTTING_SPEED_MULT:
  def: '1.0'
  type: float
  cmt: spotting speed mult against convoys
UNIT_TRANSFER_SPOTTING_SPEED_MULT:
  def: '5.0'
  type: float
  cmt: spotting speed mult against unit transfers
NAVAL_INVASION_SPOTTING_SPEED_MULT:
  def: '10.0'
  type: float
  cmt: spotting speed mult against naval invasion armies
CONVOY_DETECTION_CHANCE_BASE:
  def: '4.12'
  type: float
  cmt: regular convoy base chance detection percentage (if this fails, no detection is
    done on that tick)
BASE_SPOTTING_EFFECT_FOR_INITIAL_CONVOY_SPOTTING:
  def: '0.05'
  type: float
  cmt: effect of base convoy spotting for initial spotting of regular convoys. this
    along with next value is added together and rolled a random  once for every convoy
    to check for spotting
SPOTTING_SPEED_EFFECT_FOR_INITIAL_CONVOY_SPOTTING:
  def: '0.50'
  type: float
  cmt: effect of convoy spotting speed for initial spotting of regular convoys. this
    along with prev value is added together and rolled a random once for every convoy to
    check for spotting
SPOTTING_MOD_FOR_CONVOY_COUNT:
  def: '0.2'
  type: float
  cmt: a modifier for scaling the count of convoys on a parabolic curve (counvoy_count ^
    SPOTTING_MOD_FOR_CONVOY_COUNT)
UNIT_TRANSFER_DETECTION_CHANCE_BASE:
  def: '8.0'
  type: float
  cmt: unit transfer and naval invasion base chance detection percentage (if this fails,
    no detection is done on that tick)
BASE_SPOTTING_EFFECT_FOR_INITIAL_UNIT_TRANSFER_SPOTTING:
  def: '2.4'
  type: float
  cmt: same as BASE_SPOTTING_EFFECT_FOR_INITIAL_CONVOY_SPOTTING, but for naval transfer
    convoys
SPOTTING_SPEED_EFFECT_FOR_INITIAL_UNIT_TRANSFER_SPOTTING:
  def: '0.12'
  type: float
  cmt: same as SPOTTING_SPEED_EFFECT_FOR_INITIAL_CONVOY_SPOTTING, but for naval transfer
    convoys
BASE_SPOTTING_EFFECT_FOR_INITIAL_NAVAL_INVASION_SPOTTING:
  def: '2.4'
  type: float
  cmt: same as BASE_SPOTTING_EFFECT_FOR_INITIAL_CONVOY_SPOTTING, but for naval invasion
    convoys
SPOTTING_SPEED_EFFECT_FOR_INITIAL_NAVAL_INVASION_SPOTTING:
  def: '0.12'
  type: float
  cmt: same as SPOTTING_SPEED_EFFECT_FOR_INITIAL_CONVOY_SPOTTING, but for naval invasion
    convoys
MIN_GUN_COOLDOWN:
  def: '0.1'
  type: float
  cmt: minimum cooldown for a gun
BASE_GUN_COOLDOWNS:
  def:
    - [1.0]  # big guns
    - [4.0]  # torpedoes
    - [1.0]  # small guns
  type: table
  cmt: number of hours for a gun to be ready after shooting
BASE_JOIN_COMBAT_HOURS:
  def: '2'
  type: int
  cmt: the taskforces that wants to join existing combats will wait for at least this
    amount
LOW_ORG_FACTOR_ON_JOIN_COMBAT_DURATION:
  def: '4.0'
  type: float
  cmt: low org of the ships will be factored in when a taskforce wants to join combat
BASE_POSITIONING:
  def: '1.0'
  type: float
  cmt: base value for positioning
DOMINANCE_DAILY_GAIN_FACTOR:
  def: '0.02'
  type: float
  cmt: Daily dominance gain, as a fraction of target value
DOMINANCE_DAILY_LOSS_FACTOR:
  def: '0.04'
  type: float
  cmt: Daily dominance loss, as a fraction of previous target value
SUPPORT_SHIP_RECOVERY_BASE_STRENGTH_FACTOR:
  def: '0.01'
  type: float
  cmt: Percentage of strength of max strength a recovered ship gets on recovery.
RELATIVE_SURFACE_DETECTION_TO_POSITIONING_FACTOR:
  def: '0.01'
  type: float
  cmt: multiples the surface detection difference between two sides. the side with
    higher detection will get a bonus of this value
MAX_POSITIONING_BONUS_FROM_SURFACE_DETECTION:
  def: '0.25'
  type: float
  cmt: will clamp the bonus that you get from detection
HIGHER_SHIP_RATIO_POSITIONING_PENALTY_FACTOR:
  def: '0.25'
  type: float
  cmt: if one side has more ships than the other, that side will get this penalty for
    each +100% ship ratio it has
MAX_POSITIONING_PENALTY_FROM_HIGHER_SHIP_RATIO:
  def: '0.75'
  type: float
  cmt: maximum penalty to get from larger fleets
MIN_SHIPS_FOR_HIGHER_SHIP_RATIO_PENALTY:
  def: '4'
  type: int
  cmt: the minimum fleet size in ships that a fleet must be before having the large
    fleet penalty applied to them
HIGHER_CARRIER_RATIO_POSITIONING_PENALTY_FACTOR:
  def: '0.2;'
  type: string
  cmt: penalty if other side has stronger carrier air force
MAX_CARRIER_RATIO_POSITIONING_PENALTY_FACTOR:
  def: '0.2;'
  type: string
  cmt: max penalty from stronger carrier air force
POSITIONING_PENALTY_FOR_SHIPS_JOINED_COMBAT_AFTER_IT_STARTS:
  def: '0.01'
  type: float
  cmt: each ship that joins the combat will have this penalty to be added into
    positioning
MAX_POSITIONING_PENALTY_FOR_NEWLY_JOINED_SHIPS:
  def: '0.25'
  type: float
  cmt: the accumulated penalty from new ships will be clamped to this value
POSITIONING_PENALTY_HOURLY_DECAY_FOR_NEWLY_JOINED_SHIPS:
  def: '0.05'
  type: float
  cmt: the accumulated penalty from new ships will decay hourly by this value
DAMAGE_PENALTY_ON_MINIMUM_POSITIONING:
  def: '0.5'
  type: float
  cmt: damage penalty at 0% positioning
SCREENING_EFFICIENCY_PENALTY_ON_MINIMUM_POSITIONING:
  def: '0.5'
  type: float
  cmt: screening efficiency (screen to capital ratio) at 0% positioning
AA_EFFICIENCY_PENALTY_ON_MINIMUM_POSITIONING:
  def: '0.7'
  type: float
  cmt: AA penalty at 0% positioning
SUBMARINE_REVEAL_ON_MINIMUM_POSITIONING:
  def: '2.0'
  type: float
  cmt: submarine reveal change on 0% positioning
SHIP_TO_FLEET_ANTI_AIR_RATIO:
  def: '0.25'
  type: float
  cmt: total sum of fleet's anti air will be multiplied with this ratio and added to
    calculations anti-air of individual ships while air damage reduction
ANTI_AIR_POW_ON_INCOMING_AIR_DAMAGE:
  def: '0.225'
  type: float
  cmt: received air damage is calculated using following: 1 - ( (ship_anti_air +
    fleet_anti_air * SHIP_TO_FLEET_ANTI_AIR_RATIO )^ANTI_AIR_POW_ON_INCOMING_AIR_DAMAGE
    ) * ANTI_AIR_MULT_ON_INCOMING_AIR_DAMAGE
ANTI_AIR_MULT_ON_INCOMING_AIR_DAMAGE:
  def: '0.18'
  type: float
MAX_ANTI_AIR_REDUCTION_EFFECT_ON_INCOMING_AIR_DAMAGE:
  def: '0.75'
  type: float
  cmt: damage reduction for incoming air attacks is clamped to this value at maximum.
CHANCE_TO_DAMAGE_PART_ON_CRITICAL_HIT:
  def: '0.1'
  type: float
  cmt: the game will roll between 0-1 and will damage a random part if below this val on
    naval critical hits
CHANCE_TO_DAMAGE_PART_ON_CRITICAL_HIT_FROM_AIR:
  def: '0.1'
  type: float
  cmt: the game will roll between 0-1 and will damage a random part if below this val on
    air critical hits
SCREEN_RATIO_FOR_FULL_SCREENING_FOR_CAPITALS:
  def: '3.0'
  type: float
  cmt: this screen ratio to num capital/carriers is needed for full screening beyond
    screen line
SCREEN_RATIO_FOR_FULL_SCREENING_FOR_CONVOYS:
  def: '0.5'
  type: float
  cmt: this screen ratio to num convoys is needed for full screening beyond screen line
CAPITAL_RATIO_FOR_FULL_SCREENING_FOR_CARRIERS:
  def: '1.0'
  type: float
  cmt: this capital ratio to num carriers is needed for full screening beyond screen
    line
CAPITAL_RATIO_FOR_FULL_SCREENING_FOR_CONVOYS:
  def: '0.25'
  type: float
  cmt: this capital ratio to num convoys is needed for full screening beyond screen line
TASK_FORCE_ROLE_TO_INSIGNIA:
  def:
    - [6]  # Role undefined
    - [15]  # Wolfpack
    - [22]  # Carrier task force
    - [26]  # Surface action group
    - [16]  # Mine layers
    - [17]  # Mine sweepers
    - [29]  # Patrol task force
    - [1]  # Convoy escort
  type: table
  cmt: define the index of the insignia to use for a task force designed for a specific
    role
MIN_SHIP_COUNT_FOR_TASK_FORCE_ROLE_ASSIGNMENT:
  def: '4'
  type: int
  cmt: define the minimum number of ship that should be in a task force for it to be
    considered a patrol or an escort task force (used to the insignia assignment, see
    TASK_FORCE_ROLE_TO_INSIGNIA)
SURFACE_DETECTION_STAT_FOR_SHIP_TO_BE_PATROL:
  def: '16'
  type: int
  cmt: amount of surface detection required for a ship to be considered as part of a
    patrol task force
DEPTH_CHARGE_STAT_FOR_SHIP_TO_BE_SUB_HUNTER:
  def: '15'
  type: int
  cmt: amount of depth charge required for a ship to be considred a sub hunter and so
    good for convoy escort
SUB_DETECTION_STAT_FOR_SHIP_TO_BE_SUB_HUNTER:
  def: '2'
  type: int
  cmt: amount of sub detection required for a ship to be considered a sub hunter
HEAVY_GUN_ATTACK_TO_SHORE_BOMBARDMENT:
  def: '0.05'
  type: float
  cmt: heavy gun attack value is divided by this value * 100 and added to shore
    bombardment modifier
LIGHT_GUN_ATTACK_TO_SHORE_BOMBARDMENT:
  def: '0.025'
  type: float
  cmt: light gun attack value is divided by this value * 100 and added to shore
    bombardment modifier
GUN_HIT_PROFILES:
  def:
    - [80.0]  # big guns
    - [100.0]  # torpedoes
    - [45.0]  # small guns
  type: table
  cmt: hit profiles for guns, if target ih profile is lower the gun will have lower
    accuracy
DEPTH_CHARGES_HIT_CHANCE_MULT:
  def: '1.1'
  type: float
  cmt: multiplies hit chance of small guns
DEPTH_CHARGES_DAMAGE_MULT:
  def: '0.7'
  type: float
  cmt: multiplies damage of depth charges
DEPTH_CHARGES_HIT_PROFILE:
  def: '100.0'
  type: float
  cmt: hit profile for depth charges
CONVOY_HIT_PROFILE:
  def: '85.0'
  type: float
  cmt: convoys has this contant hit profile
HIT_PROFILE_MULT:
  def: '100.0'
  type: float
  cmt: multiplies hit profile of every ship
HIT_PROFILE_SPEED_FACTOR:
  def: '0.5'
  type: float
  cmt: factors speed value when determining it profile (Vis * HIT_PROFILE_MULT * Ship
    Hit Profile Mult)
HIT_PROFILE_SPEED_BASE:
  def: '20'
  type: int
  cmt: Base value added to hitprofile speed calulation
CONVOY_RAID_MAX_REGION_TO_TASKFORCE_RATIO:
  def: '1.5'
  type: float
  cmt: each taskforce in convoy raid mission can at most cover this many regions without
    losing efficiency
CONVOY_DEFENSE_MAX_CONVOY_TO_SHIP_RATIO:
  def: '12.0'
  type: float
  cmt: each ship in convoy defense mission can at most cover this many convoys without
    losing efficiency
CONVOY_DEFENSE_MAX_REGION_TO_TASKFORCE_RATIO:
  def: '5.0'
  type: float
  cmt: each taskforce in convoy defense mission can at most cover this many regions
    without losing efficiency
MINE_SWEEPING_REGION_TO_TASKFORCE_RATIO:
  def: '1.0'
  type: float
  cmt: ratio of taskforce to regions assigned ratio of efficiency, modified by
    coordination
MINE_PLANTING_REGION_TO_TASKFORCE_RATIO:
  def: '1.0'
  type: float
  cmt: ratio of taskforce to regions assigned ratio of efficiency, modified by
    coordination
EFFICIENCY_TO_JOIN_COMBAT_RATIO_PENALTY:
  def: '1.0'
  type: float
  cmt: at lower efficiencies less ships will be able to join combat
EFFICIENCY_TO_TIME_TO_JOIN_COMBAT_PENALTY:
  def: '100.0'
  type: float
  cmt: at lower efficiencies less time to join combat hour will be increased
COORDINATION_EFFECT_ON_CONVOY_RAID_EFFICIENCY:
  def: '1.5'
  type: float
  cmt: coordination will increase the number of areas you can cover in convoy raid
COORDINATION_EFFECT_ON_CONVOY_DEFENSE_EFFICIENCY:
  def: '1.5'
  type: float
  cmt: coordination will increase the number of convoys you can cover in convoy defense
COORDINATION_EFFECT_ON_TIME_TO_JOIN_COMBAT:
  def: '1.0'
  type: float
  cmt: coordination will reduce the time to join combat penalties
COORDINATION_EFFECT_ON_MINE_LAYING_SPEED:
  def: '0.5'
  type: float
  cmt: affect of coordination modifier in mine laying speed
COORDINATION_EFFECT_ON_MINE_SWEEPING_SPEED:
  def: '0.5'
  type: float
  cmt: affect of coordination modifier in mine sweeping speed
COORDINATION_EFFECT_ON_PATROL_SPOTTING:
  def: '1.0'
  type: float
  cmt: affect of coordination modifier in spotting speed
COORDINATION_EFFECT_ON_MINE_SWEEPING:
  def: '1.0'
  type: float
  cmt: modifies coordination by multiplication for mine sweeping
COORDINATION_EFFECT_ON_MINE_PLANTING:
  def: '1.0'
  type: float
  cmt: modifies coordination by multiplication for mine laying
DOMINANCE_EFFECT_ON_POSITIONING_FOR_CONVOY_ESCORT_MAX_RATIO:
  def: '2.0'
  type: float
  cmt: The ratio which gives the max possible gain of positioning bonus from dominance
    in region of combat (e.g. to get max bonus you need 'dominance threshold * 2.0'
    dominance in the region)
DOMINANCE_EFFECT_ON_POSITIONING_FOR_CONVOY_ESCORT:
  def: '0.15'
  type: float
  cmt: Increase of positioning when at max ratio (full control and dominance is
    >=DOMINANCE_EFFECT_ON_POSITIONING_FOR_CONVOY_ESCORT_MAX_RATIO times the competing
    dominance)
MISSION_EFFICIENCY_POW_FACTOR:
  def: '1.7'
  type: float
  cmt: mission efficiencies will be powered up by this to further penalize low
    efficiencies
NAVAL_COMBAT_SUB_DETECTION_FACTOR:
  def: '1.0'
  type: float
  cmt: balance value for sub detection in combat by ships
SUBMARINE_HIDE_TIMEOUT:
  def: '20'
  type: int
  cmt: Amount of in-game-hours that takes the submarine (with position unrevealed), to
    hide.
SUBMARINE_REVEALED_TIMEOUT:
  def: '16'
  type: int
  cmt: Amount of in-game-hours that makes the submarine visible if it is on the defender
    side.
SUBMARINE_REVEAL_BASE_CHANCE:
  def: '11'
  type: int
  cmt: Base factor for submarine detection. It's modified by the difference of a
    spotter's submarines detection vs submarine visibility. Use this variable for game
    balancing. setting this too low will cause bad spotting issues.
SUBMARINE_REVEAL_POW:
  def: '3.0'
  type: float
  cmt: A scaling factor that is applied to the reveal chance in order to make large
    differences in detection vs visibility more pronounced
SUBMARINE_BASE_TORPEDO_REVEAL_CHANCE:
  def: '0.035'
  type: float
  cmt: Chance of a submarine being revealed when it fires. 1.0 is 100%. this chance is
    then multiplied with modifier created by comparing firer's visibiility and target's
    detection
MAX_NUM_HOURS_TO_WAIT_AT_ALLY_DOCKYARDS_FOR_REPAIRS:
  def: '48'
  type: int
  cmt: taskforces will wait at most this amount of hours in ally bases for repairs
    before switching to another base for repairs
COMBAT_RESULT_PRIORITY_THRESHOLDS:
  def:
    - [0]  # low (keep at zero)
    - [4000]  # medium
    - [20000]  # high
  type: table
  cmt: the game will use this thresholds to define importance of a naval combat result.
    it will use the highest level that has higher threshold than the amount of
    production lost in combat
COMBAT_RESULT_PRIORITY_DAY_TO_LIVE:
  def:
    - [7]
    - [30]
    - [120]
  type: table
  cmt: the game will delete the combat results after some duration depending on its
    importance
NAVAL_ACCIDENTS_DAYS_TO_LIVE:
  def: '120'
  type: int
NAVAL_MINE_DANGER_RATIOS:
  def:
    - [0.1]  # not owned
    - [0.5]  # near controlled
    - [1.0]  # near owned
    - [1.0]  # controlled
    - [3.0]  # owned
  type: table
NAVAL_MINE_DANGER_TRIGGER_MIN:
  def: '0.0'
  type: float
NAVAL_MINE_DANGER_TRIGGER_MAX:
  def: '2.0'
  type: float
NAVAL_CONVOY_DANGER_RATIOS:
  def:
    - [0.10]  # not owned
    - [0.10]  # near controlled
    - [0.10]  # near owned
    - [0.15]  # controlled
    - [0.15]  # owned
  type: table
NAVAL_CONVOY_DANGER_TRIGGER_MIN:
  def: '0.0'
  type: float
NAVAL_CONVOY_DANGER_TRIGGER_MAX:
  def: '100.0'
  type: float
NAVAL_COMBAT_AIR_SUB_DETECTION_MAX:
  def: '10.0'
  type: float
NAVAL_COMBAT_AIR_SUB_DETECTION_SLOPE:
  def: '10.0'
  type: float
  cmt: lower means sharper curve (ramps up very fast, then flatten out very fast). Must
    be >0
NAVAL_COMBAT_AIR_SUB_DETECTION_EXTERNAL_FACTOR:
  def: '1.0'
  type: float
  cmt: Factor applied to the stats of external air planes
NAVAL_COMBAT_AIR_SUB_DETECTION_INTERNAL_EFFICIENCY_FACTOR:
  def: '1.0'
  type: float
  cmt: Factor of Carrier's sortie efficiency on the stats bellow
NAVAL_COMBAT_AIR_AGILITY_TO_SUB_DETECTION:
  def: '0.0'
  type: float
  cmt: Factor to apply to the agility of air planes active in a naval combat to deduce
    their contibution to sub detection
NAVAL_COMBAT_AIR_STRIKE_ATTACK_TO_SUB_DETECTION:
  def: '0.0'
  type: float
  cmt: Same, but for strike attack (aka naval attack)
NAVAL_COMBAT_AIR_STRIKE_TARGETING_TO_SUB_DETECTION:
  def: '0.0'
  type: float
  cmt: Same, but for strike targeting (aka naval targeting)
NAVAL_COMBAT_AIR_MAX_SPEED_TO_SUB_DETECTION:
  def: '0.0'
  type: float
  cmt: Same, but for Max Speed
NAVAL_COMBAT_AIR_PLANE_COUNT_TO_SUB_DETECTION:
  def: '1.0'
  type: float
  cmt: Factor applied to the number of active plane in a naval combat to deduce their
    contribution to sub detection
NAVAL_COMBAT_AIR_SUB_DETECTION_DECAY_RATE:
  def: '1.0'
  type: float
  cmt: Factor to decay the value of sub detection contributed by planes on the last
    hour. Note: the maximum value between the decayed value and the newly computed one
    is taken into account. A decay rate of 1 means that nothing is carried over, the
    previous value is zerod out. A decay rate of 0 means that the previous value is
    carried over as is.
NAVAL_COMBAT_AIR_SUB_DETECTION_FACTOR:
  def: '0.0'
  type: float
  cmt: A global factor that applies after all others, right before the sub detection
    contributed by plane is added to the global sub detection of a combatant
NAVAL_COMBAT_AIR_SUB_TARGET_BASE:
  def: '10'
  type: int
  cmt: base scoring for target picking for planes inside naval combat based on screening
    efficency, one define per ship typ
NAVAL_COMBAT_AIR_SCREEN_TARGET_BASE:
  def: '10'
  type: int
NAVAL_COMBAT_AIR_CAPITAL_TARGET_BASE:
  def: '10'
  type: int
NAVAL_COMBAT_AIR_CARRIER_TARGET_BASE:
  def: '10'
  type: int
NAVAL_COMBAT_AIR_CONVOY_TARGET_BASE:
  def: '1.0'
  type: float
NAVAL_COMBAT_AIR_SUB_TARGET_SCALE:
  def: '10'
  type: int
  cmt: scaled scoring for target picking for planes inside naval combat, max value when
    zero screening efficency, one define per ship typ
NAVAL_COMBAT_AIR_SCREEN_TARGET_SCALE:
  def: '10'
  type: int
NAVAL_COMBAT_AIR_CAPITAL_TARGET_SCALE:
  def: '50'
  type: int
NAVAL_COMBAT_AIR_CARRIER_TARGET_SCALE:
  def: '200'
  type: int
NAVAL_COMBAT_AIR_CONVOY_TARGET_SCALE:
  def: '1.0'
  type: float
NAVAL_COMBAT_AIR_STRENGTH_TARGET_SCORE:
  def: '5'
  type: int
  cmt: how much score factor from low health (scales between 0->this number)
NAVAL_COMBAT_AIR_LOW_AA_TARGET_SCORE:
  def: '5'
  type: int
  cmt: how much score factor from low AA guns (scales between 0->this number)
NAVAL_BASE_DOMINANCE_FACTOR:
  def: '0.01'
  type: float
  cmt: base naval dominance buff based on naval bases in the region
NAVAL_HEADQUARTERS_FIRST_ADJACENT_FACTOR:
  def: '0.5'
  type: float
  cmt: naval dominance from naval headquarters is multiplied by this value for the first
    adjacent region
NAVAL_HEADQUARTERS_SECOND_ADJACENT_FACTOR:
  def: '0.25'
  type: float
  cmt: naval dominance from naval headquarters is multiplied by this value for the
    second adjacent region
NEW_NAVY_LEADER_LEVEL_CHANCES:
  def:
    - [0.95]  # 95% for level one
    - [0.05]  # 5% for level two
  type: table
  cmt: chances for new navy leaders to start at a given level
NAVY_PIERCING_THRESHOLDS:
  def:
    - [2.00]
    - [1.00]
    - [0.75]
    - [0.50]
    - [0.10]
    - [0.00]  # there isn't much point setting this higher than 0
  type: table
  cmt: Our piercing / their armor must be this value to deal damage fraction equal to
    the index in the array below [higher number = higher penetration]. If armor is 0,
    1.00 will be returned.
NAVY_PIERCING_THRESHOLD_CRITICAL_VALUES:
  def:
    - [2.00]
    - [1.00]
    - [0.75]
    - [0.50]
    - [0.10]
    - [0.00]  # For criticals, you could reduce crit chance unlike damage in army combat, but we do not for now.
  type: table
  cmt: 0 armor will always receive maximum damage (so add overmatching at your own
    peril). the system expects at least 2 values, with no upper limit.
NAVY_PIERCING_THRESHOLD_DAMAGE_VALUES:
  def:
    - [1.00]
    - [1.00]
    - [0.70]
    - [0.40]
    - [0.30]
    - [0.10]
  type: table
  cmt: 0 armor will always receive maximum damage (so add overmatching at your own
    peril). the system expects at least 2 values, with no upper limit.
```
