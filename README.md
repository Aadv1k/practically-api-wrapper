# Practically API Wrapper

[![Test Practically API Wrapper](https://github.com/Aadv1k/practically-api-wrapper/actions/workflows/python-app.yml/badge.svg)](https://github.com/Aadv1k/practically-api-wrapper/actions/workflows/python-app.yml)

**Unofficial** api wrapper for [practically](https://www.practically.com) which is an OS used by many schools to publish assignments, report cards and lectures.

- [Quickstart](#quickstart)
- [Guide](#guide)
  - [Session](#session)
  - [Get User](#get-user)
  - [Get Calendar](#get-calendar)
  - [Get Classrooms](#get-classrooms)
  - [Get Assignments](#get-assignments)
- [Recipes](#recipes)
  - [Get all assignments that are due in the future](#get-all-assignments-that-are-due-in-the-future)

## Quickstart

```python
from practically import Practically

p = Practically()
p.create_session("your-assigned-username", "your-password")

user = p.get_user()
print(user.first_name, user.last_name)
```

## Guide

```python
prac = Practically(
    base_url = "https://teach.practically.com",
    session_file = "session.pickle"
)
```

### Session

```python
prac.create_session("username", "password")
```

or, if you are using dotenv you can 

```python
prac.create_session_from_env("username_key", "password_key")
```

If a valid `session_id` is not found in the `session_file` it will create a new one. You can check if the current session is invalid using. 

```python
prac.is_session_expired_or_invalid()
```

### Get User

```python
user = prac.get_user()
```
- `user.email`
- `user.first_name`
- `user.last_name`
- `user.display_name`
- `user.phone_number`

### Get Calendar

```python
calendar = prac.get_calendar(datetime.date(2023, 12, 12))
```

Returns a collection of `CalendarEntry`

- `calendar[0].teacher_name`
- `calendar[0].start_time`
- `calendar[0].title`

### Get Classrooms

A user can be enrolled in one or more classrooms.

```python
c = prac.get_classrooms()
print(len(c)) # __getitem__ and __len__ can be used
```

A single clasroom looks like so

- `c.classroom_name`
- `c.classroom_owner_name`
- `c.classroom_id`

### Get Assignments

This returns all the assignments for the user 

```python
assignments = prac.get_assignments("123456") // you can get this through classrooms
print(len(assignments)) # __getitem__ and __len__ can be used
```

A single clasroom looks like so

- `assignment.title`: string
- `assignment.start_time`: returns a datetime object
- `assignment.end_time`: returns a datetime object
- `assignment.pdf_url`: return the link to the pdf CDN

## Recipes

### Get all assignments that are due in the future

```python
from practically.practically import Practically

from datetime import datetime

from dotenv import load_dotenv
load_dotenv()

p = Practically()
p.create_session_from_env("USERNAME", "PASSWORD")

classroom_id = p.get_classrooms()[0].id
assignments = [
    a.title 
    for a in p.get_assignments(classroom_id)
    if a.end_time > datetime.today()
]

```
