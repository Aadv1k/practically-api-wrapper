from dotenv import load_dotenv
from practically.practically import Practically

import datetime 

load_dotenv()

p = Practically()
p.create_session_from_env("USERNAME", "PASSWORD")

def test_calendar_is_not_empty():
    cal = p.get_calendar(datetime.date(2023, 12, 29))
    assert len(cal) == 11
