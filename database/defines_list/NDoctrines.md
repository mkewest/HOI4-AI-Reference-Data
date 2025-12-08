---
domain: defines_list
concept: NDoctrines
version: 1.17.2
requires: [defines]
relates: [doctrines, military]
---

```yaml
DEFAULT_REWARD_MASTERY:
  def: '100.0'
  type: float
  cmt: How much mastery is required for unlocking a doctrine reward, if no override is
    set
BASE_MASTERY_GAIN_TARGET_MANPOWER:
  def: '100000.0'
  type: float
  cmt: Beyond this amount of manpower contributing to mastery, mastery gain will start
    having diminishing returns (see doctrines documentation)
TRAINING_MASTERY_GAIN_FACTOR:
  def: '0.1'
  type: float
  cmt: How much training contributes to doctrine mastery relative to combat/missions
MAX_MONTHLY_MASTERY_GAIN:
  def: '50.0'
  type: float
  cmt: Monthly mastery gain will not exceed this value
MIN_MASTERY_GAIN_PER_DAY:
  def: '0.0'
  type: float
  cmt: If we have any mastery gain, it will be boosted to be at least this much per day
    (lower cap)
MASTERY_BAR_ANIMATION_SPEED_PER_DAILY_MASTERY:
  def: '5.0'
  type: float
  cmt: Multiplier of how fast the mastery bar animates based on daily mastery gain
MASTERY_BAR_MAX_ANIMATION_SPEED:
  def: '50.0'
  type: float
  cmt: Max speed of the mastery bar animation
MASTERY_BANK_CONVERSION_RATE:
  def: '0.25'
  type: float
  cmt: The rate at which mastery gained when a track is finished or empty is "banked"
MASTERY_BANK_MAX:
  def: '200.0'
  type: float
  cmt: The maximum amount of mastery that can be banked
MILITARY_ATTACHE_MASTERY_TRANSFER_FACTOR:
  def: '0.1'
  type: float
  cmt: For each mastery track, military attaches will add this fraction of their
    visiting country's mastery gain (from units only) in that track
THEATER_COMMANDER_UNITS_MASTERY_GAIN_FACTOR_PER_SKILL:
  def: '0.01'
  type: float
  cmt: Unit in a theater commander's theater will contribute this fraction of their
    mastery gain to the theater commander's country, for each skill point they have in
    attack + defense
NAVAL_MISSION_MASTERY_GAIN_FACTORS:
  def:
    - [0.0]  # HOLD
    - [0.2]  # PATROL
    - [0.0]  # STRIKE FORCE
    - [0.2]  # CONVOY RAIDING
    - [0.2]  # CONVOY ESCORT
    - [0.2]  # MINES PLANTING
    - [0.2]  # MINES SWEEPING
    - [0.0]  # TRAIN # NOT USED - handled by TRAINING_MASTERY_GAIN_FACTOR
    - [0.0]  # RESERVE_FLEET
    - [0.0]  # NAVAL_INVASION_SUPPORT
  type: table
  cmt: Mastery gain from naval missions is reduced, just like training
```
