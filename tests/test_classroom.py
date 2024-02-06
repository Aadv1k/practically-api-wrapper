from dotenv import load_dotenv
import pytest

load_dotenv()

from practically.practically import Practically
from practically.exceptions import *

p = Practically()
p.create_session_from_env("USERNAME", "PASSWORD")


def test_if_can_get_classrooms():
    classrooms = p.get_classrooms()
    assert len(classrooms) > 0
