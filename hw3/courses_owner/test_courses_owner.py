"""Module for testing CoursesOwner."""
from typing import Any

import pytest
from course.course import Course
from courses_owner.courses_owner import CoursesOwner


class TestCoursesOwner(CoursesOwner):
    """Class for testing abstract class - CoursesOwner."""

    __test__ = False

    def __init__(self, name: str, surname: str, age: int) -> None:
        """Init new courses owner.

        Args:
            name(str): Person's name.
            surname(str): Person's surname.
            age(int): Person's age.
        """
        super().__init__(name, surname, age)


course1 = Course('Math')
course2 = Course('Programming')
courses = (course1, course2)


def create_test_courses_owner() -> TestCoursesOwner:
    """Create a clear courses owner.

    Returns:
        TestCoursesOwner: _description_
    """
    return TestCoursesOwner('noname', 'nosurname', 33)


# test getter courses and add_course
def test_getter_courses_and_add_course() -> None:
    """Test getter courses and adding new course."""
    courses_owner = create_test_courses_owner()
    courses_owner.add_course(course1)
    courses_owner.add_course(course2)

    assert len(courses_owner.courses) == 2

    for course in courses_owner.courses:
        assert isinstance(course, Course)


# test setter courses
def test_setter_courses() -> None:
    """Test setter courses."""
    courses_owner = create_test_courses_owner()
    courses_owner.courses = list(courses)

    assert len(courses_owner.courses) == 2

    for course in courses_owner.courses:
        assert isinstance(course, Course)


@pytest.mark.xfail(raises=TypeError)
@pytest.mark.parametrize('test_data', (courses, [1, 2, 3]))
def test_setter_courses_incorrect_type(test_data: Any) -> None:
    """Test setter courses with incorrect type.

    Args:
        test_data(Any): Test data.
    """
    create_test_courses_owner().courses = test_data


# test remove course
def test_remove_course() -> None:
    """Test removing course."""
    courses_owner = create_test_courses_owner()
    courses_owner.add_course(course1)
    courses_owner.add_course(course2)
    courses_owner.remove_course(course1)

    assert courses_owner.courses[0].title == course2.title
