---
domain: defines_list
concept: NTechnology
version: 1.14+
requires: [defines]
relates: [technologies_core]
---

```yaml
MAX_SUBTECHS:
  def: '3'
  type: int
  cmt: Max number of sub technologies a technology can have.
BASE_YEAR_AHEAD_PENALTY_FACTOR:
  def: '2'
  type: int
  cmt: Base year ahead penalty
MAX_TECH_SHARING_BONUS:
  def: '0.5'
  type: float
  cmt: Max technology sharing bonus that can be applied instantly
DEFAULT_XP_UNLOCK_RESEARCH_COST:
  def: '0'
  type: int
  cmt: default xp cost of a research to unlock directly
DEFAULT_XP_BOOST_RESEARCH_BONUS:
  def: '0'
  type: int
  cmt: default boost research bonus gained when xp is used to research an item
USE_BONUS_REGRET_TIMER:
  def: '3'
  type: int
  cmt: Number of days the player has to regret using a limited tech bonus
```
