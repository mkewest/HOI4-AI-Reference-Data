```yaml
ASSIGN_DESIGN_TEAM_PP_COST_PER_DAY:
  def: '0.1'
  type: float
  cmt: Cost in Political Power daily generation when one MIO is assigned to a research
    slot. If 0, cost is entirely disabled.
FUNDS_FOR_SIZE_UP:
  def: '700'
  type: int
  cmt: Funds needed for a MIO to increment its size and get points to unlock traits
FUNDS_FOR_SIZE_UP_LEVEL_POW:
  def: '1.8'
  type: float
  cmt: the power we applie to the mio size when calculating funds to level up.
DESIGN_TEAM_CHANGE_XP_COST:
  def: '0'
  type: int
  cmt: Flat cost added to the XP cost of a new equipment design. If 0, cost is entirely
    disabled.
FUNDS_FOR_CREATING_EQUIPMENT_VARIANT:
  def: '0'
  type: int
  cmt: Funds added to MIO when a new variant is created with the Design Team assigned
    to it
MAX_FUNDS_FROM_MANUFACTURER_PER_DAY:
  def: '100'
  type: int
  cmt: Max funds generated per manufacturer per day. Set to 0 for no Maximum.
ENABLE_TASK_CAPACITY:
  def: 'false'
  type: bool
  cmt: Enable limited task capacity for MIOs
DEFAULT_INITIAL_POLICY_ATTACH_COST:
  def: '25'
  type: int
  cmt: Default start attach cost in PP for policies
LEGACY_COST_FACTOR_SCALE:
  def: '1.0'
  type: float
  cmt: Multiplier to use when legacy Designer cost factors is applied to MIOs (_cost_factor)
```
