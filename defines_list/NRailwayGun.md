```yaml
ATTACK_TO_FORTS_MODIFIER_FACTOR:
  def: '1.333'
  type: float
  cmt: Forts modifier is calculated by multiplying railway gun attack value with this
    and dividing by 100
ATTACK_TO_BOMBARDMENT_MODIFIER_FACTOR:
  def: '0.4'
  type: float
  cmt: Bombardment modifier is calculated by multiplying railway gun attack value
    with this and dividing by 100
DISBAND_MANPOWER_LOSS:
  def: '0.0'
  type: float
  cmt: The ration of manpower lost on disbanding railway guns
OUT_OF_SUPPLY_SPEED:
  def: '-0.8'
  type: float
  cmt: Max speed reduction from supply for railway guns
ANNEX_RATIO:
  def: '0.5'
  type: float
  cmt: How many railway guns will be transferred on annexation
DISTRIBUTION_RAILWAY_GUN_PRESENCE_SCORE:
  def: '-100'
  type: int
  cmt: Score for Railway Guns in nearby provs. x3 if on that province. x2 if adjacent.
    x1 if 2 away.
DISTRIBUTION_FRIENDLY_UNITS_PRESENCE_SCORE:
  def: '0'
  type: int
  cmt: Score for friendly units in province when distributing Railway Guns
DISTRIBUTION_COMBATS_PRESENCE_SCORE:
  def: '-30'
  type: int
  cmt: Score for combats in province when distributing Railway Guns
DISTRIBUTION_OUR_UNITS_INRANGE_SCORE:
  def: '2.5'
  type: float
  cmt: Score for our units in range when distributing Railway Guns
DISTRIBUTION_HOSTILE_UNITS_INRANGE_SCORE:
  def: '6'
  type: int
  cmt: Score for hostile units in range when distributing Railway Guns
DISTRIBUTION_PROVINCE_CONTROLLED_BY_ENEMY_SCORE:
  def: '-3'
  type: int
  cmt: Score for staying in province controlled by enemy
DISTRIBUTION_HOLD_POSITION_SCORE:
  def: '30'
  type: int
  cmt: Score for staying in the same province when distributing Railway Guns
DISTRIBUTION_SUPPLY_DEFICIT_SCORE:
  def: '-100'
  type: int
  cmt: Score for provinces without sufficient supply cap
```
