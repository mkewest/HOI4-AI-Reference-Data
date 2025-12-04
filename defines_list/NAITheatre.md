```yaml
AI_THEATRE_GENERATION_HOME_THEATRE_DEPTH_RESTRICTION:
  def: '2'
  type: int
  cmt: The home theatre is generated based off a initial depth restriction
AI_THEATRE_GENERATION_DEPTH_TO_START_CONSIDERING_BORDERSTATES:
  def: '2'
  type: int
  cmt: Distance from capital in terms of states
AI_THEATRE_GENERATION_MAX_DISTANCE_TO_MERGE:
  def: '200'
  type: int
  cmt: Small Theatres - Dont merge with too far away theatres, higher value means
    less merging will occur
AI_THEATRE_DISTRIBUTION_SAME_THEATRE_SCORE_MODIFIER:
  def: '0.25'
  type: float
  cmt: Value that affects the score of units when distributing to fronts within the
    same theatre, its a percentage multiplier, the higher it is the higher the chance
    of units staying in close proximity
AI_THEATRE_DISTRIBUTION_PERCENTAGE_OF_MINIMUM_UNITS_TO_KEEP:
  def: '1.0'
  type: float
  cmt: How much should a frontline adheer to its minimum unit demand, when removing/reassigning
    units
AI_THEATRE_STATE_UPDATE_MAX_STATE_COUNT_TO_EXPAND:
  def: '25'
  type: int
  cmt: Max theatre size
AI_THEATRE_BREAKDOWN_MAX_DISTANCE_TO_MERGE:
  def: '200'
  type: int
  cmt: Dont merge with too far away theatres, higher value means less merging will
    occur
AI_THEATRE_SEARCH_SUPPLY_NODE_MAX_DEPTH:
  def: '5'
  type: int
  cmt: Max depth of breadth-first search while looking for supply nodes when out of
    supply
AI_THEATRE_AI_FRONT_MIN_DESIRED_RATIO:
  def: '0.18'
  type: float
  cmt: Fronts are sorted based on priority, we nudge unit demand based on this sorting,
    the higher the value the more units the most important front gets
```
