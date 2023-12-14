import course.abstract_course as abstract_course
import courses_owner.courses_owner as courses_owner
import pytest


class TestCourse(abstract_course.AbstractCourse):
    __test__ = False

    def __init__(self, title: str) -> None:
        super().__init__(title)

    def add_course_owner(self, _: 'courses_owner.CoursesOwner') -> None:
        pass

    def remove_course_owner(self, _: 'courses_owner.CoursesOwner') -> None:
        pass

def create_new_test_course() -> TestCourse:
    return TestCourse('test_course')

test_course1 = TestCourse('first')
test_course2 = TestCourse('second')

TEST_GETTER_TITLE_DATA = zip((test_course1, test_course2), ('first', 'second'))

@pytest.mark.parametrize('test_course, expected', TEST_GETTER_TITLE_DATA)
def test_getter_title(test_course: TestCourse, expected: str) -> None:
    assert test_course.title == expected


@pytest.mark.xfail(raises=TypeError)
def test_getter_title_incorrect_type() -> None:
    create_new_test_course().title = 34 # type: ignore

@pytest.mark.xfail(raises=ValueError)
def test_getter_title_incorrect_value() -> None:
    create_new_test_course().title = ''
