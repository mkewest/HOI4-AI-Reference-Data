```yaml
RAILWAY_GUN_POSSIBLE_RANGES:
  def:
    - [30, 15, 45]
  type: table
  cmt: Possible values for railway gun range in pixel.
ATTACK_TO_FORTS_MODIFIER_FACTOR:
  def: '1.333'
  type: float
  cmt: Forts modifier is calculated by multiplying railway gun attack value with this
    and dividing by 100
ATTACK_TO_ENTRENCHMENT_MODIFIER_FACTOR:
  def: '0.8'
  type: float
  cmt: Entrenchment modifier is calculated by multiplying railway gun attack value with
    this and dividing by 100
ATTACK_TO_BOMBARDMENT_MODIFIER_FACTOR:
  def: '0.4'
  type: float
  cmt: Bombardment modifier is calculated by multiplying railway gun attack value with
    this and dividing by 100
DAILY_MANPOWER_GAIN_RATIO:
  def: '0.05'
  type: float
  cmt: Railway Guns will be able to gain this ratio of their max manpower daily
DISBAND_MANPOWER_LOSS:
  def: '0.0'
  type: float
  cmt: The ration of manpower lost on disbanding railway guns
ENCIRCLED_DISBAND_MANPOWER_FACTOR:
  def: '0.2'
  type: float
  cmt: The percentage of manpower returned when an encircled unit is disbanded
OUT_OF_SUPPLY_SPEED:
  def: '-0.8'
  type: float
  cmt: Max speed reduction from supply for railway guns
BASE_CAPTURE_CHANCE:
  def: '0.2'
  type: float
  cmt: The base chance of railway guns being captured during an overrrun. Will be
    further modified by the equipment capture chance of the capturing unit.
DISTRIBUTION_RAILWAY_GUN_PRESENCE_SCORE:
  def: '-100'
  type: int
  cmt: Score for Railway Guns in nearby provs. x3 if on that province. x2 if adjacent.
    x1 if 2 away.
DISTRIBUTION_OUR_UNITS_PRESENCE_SCORE:
  def: '1'
  type: int
  cmt: Score for our units in province when distributing Railway Guns
DISTRIBUTION_FRIENDLY_UNITS_PRESENCE_SCORE:
  def: '0'
  type: int
  cmt: Score for friendly units in province when distributing Railway Guns
DISTRIBUTION_HOSTILE_UNITS_PRESENCE_SCORE:
  def: '-45'
  type: int
  cmt: Score for hostile units in province when distributing Railway Guns
DISTRIBUTION_COMBATS_PRESENCE_SCORE:
  def: '-30'
  type: int
  cmt: Score for combats in province when distributing Railway Guns
DISTRIBUTION_COMBATS_INRANGE_SCORE:
  def: '15'
  type: int
  cmt: Score for combats in range when distributing Railway Guns
DISTRIBUTION_OUR_UNITS_INRANGE_SCORE:
  def: '2.5'
  type: float
  cmt: Score for our units in range when distributing Railway Guns
DISTRIBUTION_FRIENDLY_UNITS_INRANGE_SCORE:
  def: '1.5'
  type: float
  cmt: Score for friendly units in range when distributing Railway Guns
DISTRIBUTION_HOSTILE_UNITS_INRANGE_SCORE:
  def: '6'
  type: int
  cmt: Score for hostile units in range when distributing Railway Guns
DISTRIBUTION_DISTANCE_SCORE:
  def: '-0.08'
  type: float
  cmt: Score for distance to province when distributing Railway Guns
DISTRIBUTION_PROVINCE_CONTROLLED_BY_ENEMY_SCORE:
  def: '-3'
  type: int
  cmt: Score for staying in province controlled by enemy
DISTRIBUTION_PROVINCES_CONTROLLED_BY_ENEMY_INRANGE_SCORE:
  def: '15'
  type: int
  cmt: Score for provinces controlled by enemy in range when distributing Railway Guns
DISTRIBUTION_HOLD_POSITION_SCORE:
  def: '30'
  type: int
  cmt: Score for staying in the same province when distributing Railway Guns
DISTRIBUTION_NO_RAILWAY_SCORE:
  def: '-500'
  type: int
  cmt: Score for provinces with no railways (need to be low, but we allow RG to enter
    port provinces without railways)
DISTRIBUTION_SUPPLY_DEFICIT_SCORE:
  def: '-100'
  type: int
  cmt: Score for provinces without sufficient supply cap
```
