"""Module for testing abstract course class."""
import course.abstract_course as abstract_course
import courses_owner.courses_owner as courses_owner
import pytest


class TestCourse(abstract_course.AbstractCourse):
    """Class for testing abstract class - AbstractCourse."""

    __test__ = False

    def __init__(self, title: str) -> None:
        """Init TestCourse instance.

        Args:
            title(str): title of test course.
        """
        super().__init__(title)

    def add_course_owner(self, _: 'courses_owner.CoursesOwner') -> None:
        """Stub for add_course_owner.

        Args:
            _(courses_owner.CoursesOwner): courses owner.
        """
        pass

    def remove_course_owner(self, _: 'courses_owner.CoursesOwner') -> None:
        """Stub for add_course_owner.

        Args:
            _(courses_owner.CoursesOwner): courses owner.
        """
        pass


def create_new_test_course() -> TestCourse:
    """Create a clean test course.

    Returns:
        TestCourse: Clean test course.
    """
    return TestCourse('test_course')


test_course1 = TestCourse('first')
test_course2 = TestCourse('second')

TEST_GETTER_TITLE_DATA = zip((test_course1, test_course2), ('first', 'second'))


@pytest.mark.parametrize('test_course, expected', TEST_GETTER_TITLE_DATA)
def test_getter_title(test_course: TestCourse, expected: str) -> None:
    """Test getter title.

    Args:
        test_course(TestCourse): The given test course.
        expected(str): expected value.
    """
    assert test_course.title == expected


@pytest.mark.xfail(raises=TypeError)
def test_getter_title_incorrect_type() -> None:
    """Test getter title by type."""
    create_new_test_course().title = 34  # type: ignore


@pytest.mark.xfail(raises=ValueError)
def test_getter_title_incorrect_value() -> None:
    """Test getter title by value."""
    create_new_test_course().title = ''
