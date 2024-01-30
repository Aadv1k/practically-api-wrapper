from dotenv import load_dotenv
import pytest

load_dotenv()

from practically.practically import Practically

p = Practically()
p.create_session_from_env("USERNAME", "PASSWORD")
id = p.get_classrooms()[0].id


@pytest.mark.skip
def test_if_assignments_exist():
    assignments = p.get_assignments(id)
    assert len(assignments) != 0


def test_if_assignment_has_fluff():
    assignments = p.get_assignments(id)

    assert len(assignments) > 0

    a = assignments[0]

    print(a.title, a.start_time, a.end_time, a.attached_pdf_url)

    assert a.title is not None
    assert a.start_time is not None
    assert a.end_time is not None
    assert a.attached_pdf_url is not None
