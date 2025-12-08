---
domain: defines_list
concept: NIndustrialOrganisation
version: 1.17.2
requires: [defines]
relates: [mios]
---

```yaml
ASSIGN_DESIGN_TEAM_PP_COST_PER_DAY:
  def: '0.1'
  type: float
  cmt: Cost in Political Power daily generation when one MIO is assigned to a research
    slot. If 0, cost is entirely disabled.
ASSIGN_INDUSTRIAL_MANUFACTURER_PP_COST_PER_DAY:
  def: '0.0'
  type: float
  cmt: Cost in Political Power daily generation when one MIO is assigned to a production
    line. If 0, cost is entirely disabled.
FUNDS_FOR_SIZE_UP:
  def: '700'
  type: int
  cmt: Funds needed for a MIO to increment its size and get points to unlock traits
FUNDS_FOR_SIZE_UP_LEVEL_FACTOR:
  def: '100'
  type: int
  cmt: How much each level mutliplies the funds for size up
FUNDS_FOR_SIZE_UP_LEVEL_POW:
  def: '1.8'
  type: float
  cmt: the power we applie to the mio size when calculating funds to level up.
UNLOCKED_TRAITS_PER_SIZE_UP:
  def: '1'
  type: int
  cmt: Number of points for unlocking traits obtained when the MIO increments its size
DESIGN_TEAM_CHANGE_XP_COST:
  def: '0'
  type: int
  cmt: Flat cost added to the XP cost of a new equipment design. If 0, cost is entirely
    disabled.
FUNDS_FOR_RESEARCH_COMPLETION_PER_RESEARCH_COST:
  def: '500'
  type: int
  cmt: Funds added to MIO when the Design Team has completed a research, multiplied by
    research_cost in technology template
FUNDS_FOR_CREATING_EQUIPMENT_VARIANT:
  def: '0'
  type: int
  cmt: Funds added to MIO when a new variant is created with the Design Team assigned to
    it
FUNDS_FROM_MANUFACTURER_PER_IC_PER_DAY:
  def: '0.1'
  type: float
  cmt: Funds added to MIO when a manufacturer is attached to a production line. Added
    every day proportional to IC produced.
MAX_FUNDS_FROM_MANUFACTURER_PER_DAY:
  def: '100'
  type: int
  cmt: Max funds generated per manufacturer per day. Set to 0 for no Maximum.
DESIGN_TEAM_RESEARCH_BONUS:
  def: '0.05'
  type: float
  cmt: Research bonus for applying a Design Team that matches the technology
ENABLE_TASK_CAPACITY:
  def: 'false'
  type: bool
  cmt: Enable limited task capacity for MIOs
DEFAULT_INITIAL_TASK_CAPACITY:
  def: '0'
  type: int
  cmt: Default start task capacity for each MIO (may be overriden in DB)
DEFAULT_INITIAL_POLICY_ATTACH_COST:
  def: '25'
  type: int
  cmt: Default start attach cost in PP for policies
DEFAULT_INITIAL_ATTACH_POLICY_COOLDOWN:
  def: '180'
  type: int
  cmt: Default start cooldown in days after attaching a policy
LEGACY_COST_FACTOR_SCALE:
  def: '1.0'
  type: float
  cmt: Multiplier to use when legacy Designer cost factors is applied to MIOs
    (<IdeaGroup>_cost_factor)
```
