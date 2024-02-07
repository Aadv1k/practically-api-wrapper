from dotenv import load_dotenv
import re

load_dotenv()

from practically.practically import Practically

p = Practically()
p.create_session_from_env("USERNAME", "PASSWORD")


def test_if_session_is_valid():
    assert p.is_session_expired_or_invalid() is False


user = p.get_user()


def test_if_user_info_can_be_fetched():
    assert user.first_name is not None


def test_if_user_has_all_attributes():
    assert user.first_name is not None
    assert user.last_name is not None
    assert user.display_name is not None

    assert user.phone_number is not None
    assert user.login_id is not None
    assert user.email is not None

    email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    assert re.match(
        email_regex, user.email
    ), f"Email '{user.email}' does not match the expected format."

    phone_number_regex = r"^\+\d{1,3}\s\d{3,}$"
    assert re.match(
        phone_number_regex, user.phone_number
    ), f"Phone number '{user.phone_number}' does not match the expected format."


def test_if_session_is_invalid():
    p.session_id = "foobarbaz"
    p.create_session_from_env("USERNAME", "PASSWORD")

    user = p.get_user()

    assert user.first_name is not None
