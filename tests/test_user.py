from dotenv import load_dotenv

load_dotenv()

from practically.practically import Practically

p = Practically()
p.create_session_from_env("USERNAME", "PASSWORD")

def test_if_session_is_valid():
    assert p.is_session_expired_or_invalid() is False

def test_if_user_info_can_be_fetched():
    user = p.get_user()
    assert user.first_name is not None

def test_if_session_is_invalid():
    p.session_id = "foobarbaz"
    p.create_session_from_env("USERNAME", "PASSWORD")

    user = p.get_user()

    assert user.first_name is not None
