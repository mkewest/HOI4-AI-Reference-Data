---
domain: defines_list
concept: NAirGfx
version: 1.17.2
requires: [defines]
relates: [air_graphics]
---

```yaml
AIRPLANES_ANIMATION_GLOBAL_SPEED_PER_GAMESPEED:
  def:
    - [0.22, 0.28, 0.32, 0.38, 0.44, 0.50]
  type: table
  cmt: Speed factor for each game speed (begin with paused). Larger value = faster
    animation.
ROCKET_SPEED:
  def: '15.0'
  type: float
  cmt: Speed of rockets launched from rocket sites
AIRPLANES_CURVE_POINT_DENSITY:
  def: '2.0'
  type: float
  cmt: LOWER value = more midpoints in the flight path.
AIRPLANES_CURVE_MAX_EXTRAPOLATION:
  def: '20.0'
  type: float
  cmt: It's the limit value that avoid making gigantic curves that may happen when
    flight path is very long.
AIRPLANES_CURVE_MIN_ELEVATION:
  def: '4.0'
  type: float
  cmt: Minimum height above the ground that the curve will generate it's points.
    Excludes first and last point (takeoff/landing).
AIRPLANES_SCALE_TAKEOFF_DIST:
  def: '0.1'
  type: float
  cmt: Until first x% of the flight path, the airplane will scale up.
AIRPLANES_SCALE_MIN:
  def: '0.1'
  type: float
  cmt: Minimum airplane scale down when takeoff/landing.
AIRPLANES_SCALE_LANDING_DIST:
  def: '0.9'
  type: float
  cmt: After last x% of the flight path, the airplane will scale down.
AIRPLANES_SMOOTH_INTERPOLATION_MOVE:
  def: '0.13'
  type: float
  cmt: How smooth is the movement interpolation.
AIRPLANES_SMOOTH_INTERPOLATION_TURN:
  def: '0.12'
  type: float
  cmt: How smooth is the turning interpolation.
AIRPLANES_BANK_STRENGTH:
  def: '210.0'
  type: float
  cmt: Multiplier of how much the curve affects the wings banking. (angle limited by the
    following value)
AIRPLANES_BANK_ANGLE_LIMIT:
  def: '55.0'
  type: float
  cmt: Bank angle limit.
AIRPLANES_GROUND_COLLISION_OFFSET_Y:
  def: '0.0'
  type: float
  cmt: Set's the height (Y) offset before 3d airplanes disappear after going to the
    ground.
AIRPLANES_GROUND_EXPLOSION_TIME_DELAY:
  def: '0.6'
  type: float
  cmt: Time in seconds to play explosion animation when plane hit ground before the
    plane entity is deleted
AIRPLANES_1_FIGHTER_PATROL_ANIM:
  def: '1'
  type: int
  cmt: Number of fighters needed for a single instance of this animation
AIRPLANES_3_FIGHTER_PATROL_ANIM:
  def: '3'
  type: int
  cmt: Number of fighters needed for a single instance of this animation
AIRPLANES_1_BOMBER_BOMBING_ANIM:
  def: '1'
  type: int
  cmt: Number of bombers needed for a single instance of this animation
AIRPLANES_3_BOMBER_BOMBING_ANIM:
  def: '3'
  type: int
  cmt: Number of bombers needed for a single instance of this animation
AIRPLANES_1_FIGHTER_VS_1_FIGHTER_ANIM:
  def: '1'
  type: int
  cmt: Number of fighters needed per side for a single instance of this animation
AIRPLANES_3_FIGHTER_VS_3_FIGHTER_ANIM:
  def: '3'
  type: int
  cmt: Number of bombers needed per side for a single instance of this animation
AIRPLANES_1_TRANSPORT_SUPPLY_ANIM:
  def: '1'
  type: int
  cmt: Number of planes needed for a single instance of this animation
AIRPLANES_3_TRANSPORT_SUPPLY_ANIM:
  def: '3'
  type: int
  cmt: Number of planes needed for a single instance of this animation
AIRPLANES_1_SCOUT_PLANE_PATROL_ANIM:
  def: '1'
  type: int
AIRPLANES_3_SCOUT_PLANE_PATROL_ANIM:
  def: '3'
  type: int
RANDOM_SCENARIO_ANIMATION_MAX_DELAY:
  def: '3.0'
  type: float
  cmt: Maximum delay until an animation for a gfx airplane (Currently SAM and gun
    emplacments) starts
STRAT_BOMBER_FIREBOMB_THRESHOLD:
  def: '42.0'
  type: float
  cmt: If a strategic bomber has a strat_bomber value >= this, then the firebombing
    animation will be used
STRAT_BOMBER_CARPETBOMB_THRESHOLD:
  def: '16.0'
  type: float
  cmt: If a strategic bomber has a strat_bomber value >= this, then the carpet-bombing
    animation will be used
BOMBERS_DIVISION_FACTOR:
  def: '30'
  type: int
  cmt: Number of bombers in a strategic region will be divided by this factor.
MISSILES_DIVISION_FACTOR:
  def: '60'
  type: int
  cmt: Number of missiles shown in a strategic region will be divided by this factor.
FIGHTERS_DIVISION_FACTOR:
  def: '30'
  type: int
  cmt: Number of missiles shown in a strategic region will be divided by this factor.
SCOUT_PLANE_DIVISION_FACTOR:
  def: '30'
  type: int
  cmt: Number of missiles shown in a strategic region will be divided by this factor.
TRANSPORT_DIVISION_FACTOR:
  def: '30'
  type: int
MAX_MISSILE_BOMBING_SCENARIOS:
  def: '2'
  type: int
  cmt: Max number of missile bombing scenarios in a strategic region.
MAX_PATROL_SCENARIOS:
  def: '2'
  type: int
  cmt: Max number of patrol scenarios in a strategic region.
MAX_BOMBING_SCENARIOS:
  def: '2'
  type: int
  cmt: Max number of bombings scenarios in a strategic region.
MAX_DOGFIGHTS_SCENARIOS:
  def: '3'
  type: int
  cmt: Max number of dogfight scenarios in a strategic region.
MAX_TRANSPORT_SCENARIOS:
  def: '2'
  type: int
  cmt: Max number of transport scenarios in a strategic region
MAX_TRAINING_SCENARIOS:
  def: '2'
  type: int
  cmt: Max number of training scenarios in a strategic region
MAX_SCOUT_SCENARIOS:
  def: '2'
  type: int
```
