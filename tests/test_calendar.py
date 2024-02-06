from dotenv import load_dotenv
from practically.practically import Practically

p = Practically()
p.create_session_from_env("USERNAME", "PASSWORD")

def test_calendar_is_not_empty():
    p.get_calendar("")
    pass

def test_handles_invalid_date():
    pass
