---
domain: defines_list
concept: NPolitics
version: 1.17.2
requires: [defines]
relates: [politics_ideology]
---

```yaml
BASE_LEADER_TRAITS:
  def: '3'
  type: int
  cmt: Base amount of leader traits.
MAX_RANDOM_LEADERS:
  def: '1'
  type: int
  cmt: Maximum amount random leader to have per party.
BASE_POLITICAL_POWER_INCREASE:
  def: '2'
  type: int
  cmt: Weekly increase of PP.
ARMY_LEADER_COST:
  def: '5'
  type: int
  cmt: command power cost for recruiting new leaders, 'this value' *
    number_of_existing_leaders_of_type
NAVY_LEADER_COST:
  def: '5'
  type: int
  cmt: command power cost for recruiting new leaders, 'this value' *
    number_of_existing_leaders_of_type
ARMY_LEADER_MAX_COST:
  def: '80'
  type: int
  cmt: max cost BEFORE modifiers
NAVY_LEADER_MAX_COST:
  def: '80'
  type: int
  cmt: max cost BEFORE modifiers
LEADER_TRAITS_XP_SHOW:
  def: '0.05'
  type: float
  cmt: Amount of XP a trait needs to be shown in tooltips of a leader.
REVOLTER_PARTY_POPULARITY:
  def: '0.4'
  type: float
  cmt: Revolter party loses 80% popularity when the civil war breaks out
MIN_OVERTHROWN_GOVERNMENT_SUPPORT_RATIO:
  def: '0.4'
  type: float
  cmt: Min possible support for new government after puppeting the government
NUM_OCCUPATION_POLICIES:
  def: '4'
  type: int
  cmt: Number of potential occupation policies
DEFAULT_OCCUPATION_POLICY:
  def: '1'
  type: int
  cmt: Defaullt value for occupation policy
INSTANT_WIN_REVOLTER_POPULARITY_RATIO:
  def: '0.4'
  type: float
  cmt: Min party popularity for instant win in one province state
INSTANT_WIN_POPULARITY_WIN:
  def: '50'
  type: int
  cmt: New party popularity
```
