from practically import Practically

p = Practically()


def test_if_user_can_login():
    p.create_session_from_env("USERNAME", "PASSWORD")

    user = p.get_user()
    assert user.display_name is not None


def test_if_session_persists():
    assert p.create_session(id=p.session.id) is None
