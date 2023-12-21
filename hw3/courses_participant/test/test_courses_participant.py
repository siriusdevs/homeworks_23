"""Module for testing CoursesParticipant."""
from typing import Any

import pytest
from course_with_participants.course_with_participants import \
    CourseWithParticipants
from courses_participant.courses_participant import CoursesParticipant


class TestCoursesParticipant(CoursesParticipant):
    """Class for testing abstract class - CoursesParticipant."""

    __test__ = False

    def __init__(self) -> None:
        """Init new courses participant."""
        super().__init__()


course1 = CourseWithParticipants('Math')
course2 = CourseWithParticipants('Programming')
courses = (course1, course2)


def create_test_courses_participant() -> TestCoursesParticipant:
    """Create a clear courses participant.

    Returns:
        TestCoursesParticipant: _description_
    """
    return TestCoursesParticipant()


# test getter courses and add_course
def test_getter_courses_and_add_course() -> None:
    """Test getter courses and adding new course."""
    courses_participant = create_test_courses_participant()
    courses_participant.add_course(course1)
    courses_participant.add_course(course2)

    assert len(courses_participant.courses) == 2

    for course in courses_participant.courses:
        assert isinstance(course, CourseWithParticipants)


# test setter courses
def test_setter_courses() -> None:
    """Test setter courses."""
    courses_participant = create_test_courses_participant()
    courses_participant.courses = list(courses)

    assert len(courses_participant.courses) == 2

    for course in courses_participant.courses:
        assert isinstance(course, CourseWithParticipants)


@pytest.mark.xfail(raises=TypeError)
@pytest.mark.parametrize('test_data', (courses, [1, 2, 3]))
def test_setter_courses_incorrect_type(test_data: Any) -> None:
    """Test setter courses with incorrect type.

    Args:
        test_data(Any): Test data.
    """
    create_test_courses_participant().courses = test_data


# test remove course
def test_remove_course() -> None:
    """Test removing course."""
    courses_participant = create_test_courses_participant()
    courses_participant.add_course(course1)
    courses_participant.add_course(course2)
    courses_participant.remove_course(course1)

    assert courses_participant.courses[0].title == course2.title
