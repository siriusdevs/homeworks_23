import pytest
from typing import Any
from hw3.courses_owner.courses_owner import CoursesOwner
from hw3.course.course import Course

class TestCoursesOwner(CoursesOwner):
    __test__ = False

    def __init__(self, name: str, surname: str, age: int) -> None:
        super().__init__(name, surname, age)

course1 = Course('Math')
course2 = Course('Programming')
courses = (course1, course2)

def create_test_courses_owner() -> TestCoursesOwner:
    return TestCoursesOwner('noname', 'nosurname', 33)

# test getter courses and add_course
def test_getter_courses_and_add_course() -> None:
    courses_owner = create_test_courses_owner()
    courses_owner.add_course(course1)
    courses_owner.add_course(course2)

    assert len(courses_owner.courses) == 2

    for course in courses_owner.courses:
        assert isinstance(course, Course)


# test setter courses
def test_setter_courses() -> None:
    courses_owner = create_test_courses_owner()
    courses_owner.courses = list(courses)

    assert len(courses_owner.courses) == 2

    for course in courses_owner.courses:
        assert isinstance(course, Course)

@pytest.mark.xfail(raises=TypeError)
@pytest.mark.parametrize('test_data', (courses, [1, 2, 3]))
def test_setter_courses_incorrect_type(test_data: Any) -> None:
    create_test_courses_owner().courses = test_data


# test remove course
def test_add_course() -> None:
    courses_owner = create_test_courses_owner()
    courses_owner.add_course(course1)
    courses_owner.add_course(course2)
    courses_owner.remove_course(course1)

    assert courses_owner.courses[0].title == course2.title
