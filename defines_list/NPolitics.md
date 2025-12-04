```yaml
BASE_LEADER_TRAITS:
  def: '3'
  type: int
  cmt: Base amount of leader traits.
BASE_POLITICAL_POWER_INCREASE:
  def: '2'
  type: int
  cmt: Weekly increase of PP.
NAVY_LEADER_COST:
  def: '5'
  type: int
  cmt: command power cost for recruiting new leaders, 'this value' * number_of_existing_leaders_of_type
NAVY_LEADER_MAX_COST:
  def: '80'
  type: int
  cmt: max cost BEFORE modifiers
REVOLTER_PARTY_POPULARITY:
  def: '0.4'
  type: float
  cmt: Revolter party loses 80% popularity when the civil war breaks out
NUM_OCCUPATION_POLICIES:
  def: '4'
  type: int
  cmt: Number of potential occupation policies
INSTANT_WIN_REVOLTER_POPULARITY_RATIO:
  def: '0.4'
  type: float
  cmt: Min party popularity for instant win in one province state
```
