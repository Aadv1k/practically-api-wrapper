from dotenv import load_dotenv
import pathlib

load_dotenv()

from practically.practically import Practically

p = Practically()

def test_if_user_can_login():
    p.create_session_from_env("USERNAME", "PASSWORD")

    user = p.get_user()
    assert len(user.first_name) > 1

def test_should_work_if_session_is_invalid():
    p.session_id = "foobarbaz"
    p.create_session_from_env("USERNAME", "PASSWORD")

    user = p.get_user()
    assert len(user.last_name) > 1
