import hashlib
from datetime import datetime, timedelta


def str_to_md5(s: str) -> str:
    h = hashlib.md5(s.encode())
    return h.hexdigest()


"""Expects: 30 Jan 2024 04:00 PM IST (UTC +5:30)"""


def parse_str_as_datestring(date_string):
    date_string = date_string[:-12]

    month_mapping = {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12,
    }

    day, month_abbr, year, time, am_pm, timezone = date_string.split()

    # Convert month abbreviation to month number
    month = month_mapping[month_abbr]

    # Convert time to 24-hour format
    if am_pm == "PM":
        hour, minute = map(int, time.split(":"))
        hour = (hour + 12) % 24
    else:
        hour, minute = map(int, time.split(":"))

    # Create a datetime object
    parsed_date = datetime(int(year), month, int(day), hour, minute)

    return parsed_date
