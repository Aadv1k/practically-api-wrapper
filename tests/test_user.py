from dotenv import load_dotenv
load_dotenv()

from practically.practically import Practically

p = Practically()

def test_if_user_can_login():
    #p.create_session_from_env("USERNAME", "PASSWORD")

    p.session_id = "b14ef77393091fd4b8d9d0e4b53247ffa4dd7988"

    user = p.get_user()
    assert str(user) is not None
