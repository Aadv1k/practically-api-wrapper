from dotenv import load_dotenv

load_dotenv()

from practically.practically import Practically

p = Practically()
p.create_session_from_env("USERNAME", "PASSWORD")


def test_if_can_get_classroom():
    classrooms = p.get_classrooms()
    assert classrooms != None and len(classrooms) > 0


def test_if_classroom_is_initialized():
    classrooms = p.get_classrooms()
    assert classrooms[0].name != None
