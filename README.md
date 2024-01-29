# Practically API Wrapper

Unofficial api wrapper for [practically](https://www.practically.com) which is an OS used by many schools to publish assignments, report cards and lectures.

## Quickstart

```
pip install practically-api-wrapper
```

```python
from practically import Practically

p = Practically("your-assigned-id", "your-assigned-password")

for assignment in p.get_assignments():
    print(assignment.title)
```
