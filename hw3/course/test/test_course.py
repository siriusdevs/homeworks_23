"""Module for testing course class."""


import pytest
from course.course import Course


def create_new_course() -> 'Course':
    """Create a clean course for testing.

    Returns:
        Course: Clean course for testing.
    """
    return Course('test_course')


test_course1 = Course('first')
test_course2 = Course('second')

TEST_GETTER_TITLE_DATA = zip((test_course1, test_course2), ('first', 'second'))


@pytest.mark.parametrize('test_course, expected', TEST_GETTER_TITLE_DATA)
def test_getter_title(test_course: 'Course', expected: str) -> None:
    """Test getter title.

    Args:
        test_course(Course): The given test course.
        expected(str): expected value.
    """
    assert test_course.title == expected


@pytest.mark.xfail(raises=TypeError)
def test_getter_title_incorrect_type() -> None:
    """Test getter title by type."""
    create_new_course().title = 34  # type: ignore


@pytest.mark.xfail(raises=ValueError)
def test_getter_title_incorrect_value() -> None:
    """Test getter title by value."""
    create_new_course().title = ''
