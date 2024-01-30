# Practically API Wrapper

Unofficial api wrapper for [practically](https://www.practically.com) which is an OS used by many schools to publish assignments, report cards and lectures.

## Quickstart

```python
from practically import Practically

p = Practically()
p.create_session("your-assigned-username", "your-password")

user = p.get_user()
print(user.first_name, user.last_name)
```
