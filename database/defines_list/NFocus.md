---
domain: defines_list
concept: NFocus
version: 1.17.2
requires: [defines]
relates: [national_focus]
---

```yaml
FOCUS_POINT_DAYS:
  def: '7'
  type: int
  cmt: Each point takes a week
FOCUS_PROGRESS_PEACE:
  def: '1'
  type: int
  cmt: Progress during peace
FOCUS_PROGRESS_WAR:
  def: '1'
  type: int
  cmt: Progress during war
MAX_SAVED_FOCUS_PROGRESS:
  def: '10'
  type: int
  cmt: This much progress can be saved while not having a focus selected
```
