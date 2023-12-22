"""Tests for hw3.py."""

from typing import Any

import pytest

import hw3

# testing objects
teacher = hw3.Teacher('Trebla', 'Programming')
teacher2 = hw3.Teacher('Valsehcayv', 'Networks')
student = hw3.Student('Nikita', 17)
student2 = hw3.Student('Egor', 16)
student3 = hw3.Student('Yaroslav', 15)
course = hw3.Course('Python', teacher, [student, student2])
course2 = hw3.Course('JavaScript', teacher, [student2, student3])
group = hw3.Group('К0709-23/2', [student, student3])
group2 = hw3.Group('К0709-23/4', [student2, student3])
institution = hw3.Institution('Better', [course], [group])

TEST_OPERATIONS_DATA = (
    (course, 'course_student', [str(elem) for elem in course.course_students], student3),
    (group, 'group_student', [str(elem) for elem in group.group_students], student2),
    (
        institution,
        'institution_course',
        [str(elem) for elem in institution.institution_courses],
        course2,
    ),
    (
        institution,
        'institution_group',
        [str(elem) for elem in institution.institution_groups],
        group2,
    ),
)

TEST_GET_SET_DATA = (
    (teacher, 'teacher_name', teacher.teacher_name, 'Sirob'),
    (teacher, 'faculty', teacher.faculty, 'Art'),
    (student, 'student_name', student.student_name, 'Daniel'),
    (student, 'age', student.age, 18),
    (course, 'course_name', course.course_name, 'IP'),
    (course, 'course_teacher', course.course_teacher, teacher2),
    (course, 'course_students', course.course_students, [student2, student3]),
    (group, 'group_name', group.group_name, 'К0709-25/5'),
    (group, 'group_students', group.group_students, [student, student2]),
    (institution, 'institution_name', institution.institution_name, 'Best'),
    (institution, 'institution_courses', institution.institution_courses, [course2]),
    (institution, 'institution_groups', institution.institution_groups, [group2]),
)


@pytest.mark.parametrize('test_obj, attribute, curr_values, new_value', TEST_OPERATIONS_DATA)
def test_operations(test_obj: type, attribute: str, curr_values: Any, new_value: Any) -> None:
    """Test all methods with attributes: add, remove and get_all.

    Args:
        test_obj: object that will be tested
        attribute: attribute that will be tested (e.g. student, not students!)
        curr_values: current values of the object attribute (for testing get all)
        new_value: new value that need to append and then remove

    Asserts:
        True if function with current test data returns right value.
    """
    assert getattr(test_obj, f'get_all_{attribute}s')() == curr_values, \
        "Get all method don't work"
    getattr(test_obj, f'add_{attribute}')(new_value)
    assert getattr(test_obj, f'get_all_{attribute}s')() == curr_values + [str(new_value)], \
        "Add method don't work"
    getattr(test_obj, f'remove_{attribute}')(new_value)
    assert getattr(test_obj, f'get_all_{attribute}s')() == curr_values, \
        "Remove method don't work"


@pytest.mark.parametrize('test_obj, attribute, curr_value, new_value', TEST_GET_SET_DATA)
def test_getters_setters(test_obj: type, attribute: str, curr_value: Any, new_value: Any) -> None:
    """Test all getters and setters.

    Args:
        test_obj: object that will be tested
        attribute: attribute that will be tested
        curr_value: current value of the object attribute (for testing getter)
        new_value: new value of the object attribute (for testing setter)

    Asserts:
        True if function with current test data returns right value.
    """
    assert getattr(test_obj, attribute) == curr_value, "Getter don't work"
    setattr(test_obj, attribute, new_value)
    assert getattr(test_obj, attribute) == new_value, "Setter don't work"
