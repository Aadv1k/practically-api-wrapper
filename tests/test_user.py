import practically.Practically

p = Practically()


def test_if_user_can_login():
    p.create_session_from_env("USERNAME", "PASSWORD")

    user = p.get_user()
    assert str(user) is not None
