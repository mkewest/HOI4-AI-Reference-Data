---
domain: defines_list
concept: NTechnology
version: 1.17.2
requires: [defines]
relates: [technologies_core]
---

```yaml
MAX_SUBTECHS:
  def: '3'
  type: int
  cmt: Max number of sub technologies a technology can have.
BASE_RESEARCH_POINTS_SAVED:
  def: '30.0'
  type: float
  cmt: Base amount of research points a country can save per slot.
BASE_YEAR_AHEAD_PENALTY_FACTOR:
  def: '2'
  type: int
  cmt: Base year ahead penalty
BASE_TECH_COST:
  def: '110'
  type: int
  cmt: Base cost for a tech. multiplied with tech cost and ahead of time penalties
MAX_TECH_SHARING_BONUS:
  def: '0.5'
  type: float
  cmt: Max technology sharing bonus that can be applied instantly
LICENSE_PRODUCTION_TECH_BONUS:
  def: '0.2'
  type: float
  cmt: License production tech bonus
DEFAULT_XP_UNLOCK_RESEARCH_COST:
  def: '0'
  type: int
  cmt: default xp cost of a research to unlock directly
DEFAULT_XP_BOOST_RESEARCH_COST:
  def: '0'
  type: int
  cmt: default xp cost of a research to speed up the process
DEFAULT_XP_BOOST_RESEARCH_BONUS:
  def: '0'
  type: int
  cmt: default boost research bonus gained when xp is used to research an item
MIN_RESEARCH_SPEED:
  def: '0.1'
  type: float
  cmt: research speed can't go below this value
USE_BONUS_REGRET_TIMER:
  def: '3'
  type: int
  cmt: Number of days the player has to regret using a limited tech bonus
```
