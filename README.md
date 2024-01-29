# Practically API Wrapper

Unofficial api wrapper for [practically](https://www.practically.com) which is an OS used by many schools to publish assignments, report cards and lectures.

> Read Up on the [Reverse Engineering](./Reverse_Engineering.md) doc to see the process of doing thi. I feel a lot could've been done better, I will gladly take any criticisms or suggestions. Thanks

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
