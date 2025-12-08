---
domain: defines_list
concept: NProject
version: 1.17.2
requires: [defines]
relates: []
---

```yaml
FACILITY_SUPPLY_WARNING_RED_RATIO:
  def: '0.66'
  type: float
  cmt: When lacking supply for a facility it will be a yellow icon shown until the
    supply is less than this value, where it will turn red.
DEFAULT_COMPLEXITY:
  def: '100'
  type: int
  cmt: Default special project prototype phase to only require one iteration.
DEFAULT_EMPTY_REWARD_WEIGHT:
  def: '1.0'
  type: float
  cmt: The weight for no reward being given after a prototype iteration.
DEFAULT_STOP_PROJECT_DAYS:
  def: '10'
  type: int
  cmt: The amount of days it takes for a cancelled project to be stopped.
DAYS_TO_REMOVE_SCIENTIST:
  def: '10'
  type: int
  cmt: Amount of days needed for a scientist to be unassigned.
DISMANTLE_FACILITY_DAYS:
  def: '100'
  type: int
  cmt: Amount of days needed to dismantle a facility.
PROTOTYPE_PHASE_MAX_PROGRESS:
  def: '100'
  type: int
  cmt: the number of progress points needed to finish the prototype phase and complete
    the project
MINIMUM_PROJECT_SPEED_FACTOR_FROM_SUPPLY:
  def: '0.2'
  type: float
  cmt: Minimum special project research speed based on supply
NEEDED_SUPPLY_FOR_FULL_SPEED_PROJECT:
  def: '3.0'
  type: float
  cmt: Supply needed in province to get full research speed for special project
MINIMUM_PROJECT_SPEED_FACTOR_FROM_RESOURCE_SHORTAGE:
  def: '0.2'
  type: float
  cmt: Minimum special project research speed factor based on resource shortage^M
ITERATION_REWARD_DEFAULT_WEIGHT:
  def: '1.0'
  type: float
  cmt: If no weight is specified, set it to 1.0
DEFAULT_PROJECT_COMPLETION_SCIENTIST_EXPERIENCE_GAIN:
  def: '192.0'
  type: float
  cmt: Default experience gain for assigned scientist when a project is completed
SCIENTIST_INJURED_FACTOR:
  def: '0.0'
  type: float
  cmt: A factor to reduce the amount of progress gained in a program with attached
    injured scientist. E.g. 0.5 reduces the progress by 50%
RECRUIT_SCIENTIST_ONE_TRAIT_CHANCE:
  def: '0.35'
  type: float
  cmt: Chance to get one trait when creating a scientist. E.g. 0.35 = 35% chance to get
    a trait
SCIENTIST_BASIC_RESEARCH_DAILY_XP_GAIN:
  def: '0.28'
  type: float
  cmt: Daily experience gain for doing basic research
RECRUIT_SCIENTIST_COST:
  def:
    - [25]  # pp cost if no available scientist
    - [50]  # pp cost if 1 available scientist
    - [75]  # pp cost if 2 available scientist
    - [100]  # pp cost if more than 2 available scientist
  type: table
  cmt: Amount of pp to hire a scientist based on available scientist
SCIENTIST_SKILL_LEVEL_THRESHOLDS:
  def:
    - [100]  # to go from level 0 to level 1
    - [100]  # to go from level 1 to level 2
    - [300]  # to go from level 2 to level 3
    - [700]  # ...
    - [1500]  # Max level = Array size
  type: table
  cmt: Threshold for scientist to level up
SCIENTIST_SKILL_LEVEL_SPEED_MODIFIER:
  def:
    - [-1.0]  # -1.0 means -100%         also name loc key is SCIENTIST_SKILL_LEVEL_NAME_0
    - [-0.05]  # -0.05 means -5%			also name loc key is SCIENTIST_SKILL_LEVEL_NAME_1
    - [0.05]  # 0 means no change		also name loc key is SCIENTIST_SKILL_LEVEL_NAME_2
    - [0.1]  # 0.15 means +15%			...
    - [0.15]
    - [0.25]  # Size MUST be SCIENTIST_SKILL_LEVEL_THRESHOLDS's size + 1
  type: table
  cmt: Bonus to apply to daily phase progress according to the skill level of the
    scientist
PROJECT_LOSS_FACTOR_ON_CAPTURE:
  def: '0.2'
  type: float
  cmt: Factor of lost progress on project when facility is captured
PROJECT_CAPTURE_GAIN_RATIO:
  def: '0.2'
  type: float
  cmt: Ratio of difference from captured facilities ongoing project to receive to the
    captors' progress
PROJECT_CAPTURE_BREAKTHROUGH_PROGRESS:
  def: '0.1'
  type: float
  cmt: Ratio of breakthrough progress on capture to the captor for the facilities
    specialization
PROJECT_CAPTURE_DIMINISHING_RETURN:
  def: '0.6'
  type: float
  cmt: Reduced amount of gain when capturing a facility with a project you already
    gained. Will apply the factor each time a capture occurs. 0.6 means a reduction of
    60% on next project capture.
BASIC_RESEARCH_TECHNOLOGY_BONUS_FACTOR:
  def: '0.02'
  type: float
  cmt: Bonus research factor applied to technologies per scientist skill level when
    performing basic research in a matching facility.
BASIC_RESEARCH_TECHNOLOGY_BONUS_DIMINISHING_RETURN_FACTOR:
  def: '0.5'
  type: float
  cmt: Diminishing return on BASIC_RESEARCH_TECHNOLOGY_BONUS_FACTOR for each extra
    scientist performing basic research for multiple facilities.
BREAKTHROUGH_DAILY_TECHNOLOGY_GAIN:
  def: '12'
  type: int
  cmt: Amount in 1/100th percentage. E.g. 25 = 0.25%
BREAKTHROUGH_DAILY_SCIENTIST_SKILL_GAIN:
  def: '5'
  type: int
  cmt: Amount in 1/100th percentage gained per skill when doing basic research. E.g. 5 =
    0.05% per skill level.
BREAKTHROUGH_DAILY_ROCKET_SITE_GAIN:
  def: '1'
  type: int
  cmt: Amount in 1/100th percentage gained per rocket site level. E.g. 1 = 0.01% per
    rocket site level.
BREAKTHROUGH_DAILY_NUCLEAR_REACTOR_GAIN:
  def: '1'
  type: int
  cmt: Amount in 1/100th percentage gained per nuclear reactor. E.g. 2 = 0.02% per
    nuclear reactor.
BREAKTHROUGH_GAIN_ANIMATION_SPEED_MAX:
  def: '1.0'
  type: float
  cmt: The animation for gaining breakthrough progress is a ratio of this value and
    current daily gain.
AMOUNT_OF_SUPPORTIVE_SCIENTISTS:
  def: '3'
  type: int
  cmt: The amount of supportive scientists a facility can have
SUPPORTIVE_SCIENTISTS_FRACTION:
  def: '0.25'
  type: float
  cmt: how effective supportive scientists are compared to how strong they would be on
    default
SUPPORTIVE_SCIENITST_PROGRESS_BONUS:
  def: '0.1'
  type: float
  cmt: How much of the progress will be given to the additional scientist countries
    project. percentage of how much the current project got from its iteration
SUPPORTIVE_SCIENTISTS_SHARING_BONUS:
  def: '0.05'
  type: float
  cmt: Research sharing % per supportive scientist. Global per faction.
```
