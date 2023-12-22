"""Module for testing Course class."""
from typing import Any

import pytest
from course_with_participants.course_with_participants import \
    CourseWithParticipants
from student.student import Student
from teacher.teacher import Teacher

teacher1 = Teacher('Teacher1', 'NoSurname1', 30)
teacher2 = Teacher('Teacher2', 'NoSurname2', 50)

student1 = Student('Denis', 'Romodanov', 18)
student2 = Student('Sanya', 'Black', 20)
student3 = Student('New', 'Student', 32)
students = (student1, student2, student3)


def create_new_course() -> 'CourseWithParticipants':
    """Create a clean course.

    Returns:
        Course: Clean course.
    """
    return CourseWithParticipants('Test title')


# test getter teacher
def test_getter_teacher_empty() -> None:
    """Test teacher getter with empty value."""
    assert create_new_course().teacher is None


def test_getter_teacher_no_empty() -> None:
    """Test teacher getter with some value."""
    course = create_new_course()
    course.add_course_participant(teacher1)

    assert course.teacher.name == teacher1.name  # type: ignore


# test setter teacher
def test_setter_teacher() -> None:
    """Test teacher setter firstly."""
    course = create_new_course()
    course.teacher = teacher1

    assert course.teacher.name == teacher1.name  # type: ignore


def test_setter_teacher_some() -> None:
    """Test teacher setter more once."""
    course = create_new_course()
    course.teacher = teacher1
    course.teacher = teacher2

    assert course.teacher.name == teacher2.name  # type: ignore


@pytest.mark.xfail(raises=TypeError)
def test_setter_teacher_incorrect_type() -> None:
    """Test teacher setter by incorrect type."""
    create_new_course().teacher = '23'  # type: ignore


# test getter students
def test_getter_students_empty() -> None:
    """Test students getter with empty value."""
    assert not create_new_course().students


def test_getter_students() -> None:
    """Test students getter with value."""
    course = create_new_course()

    for student in students:
        course.add_course_participant(student)

    assert len(course.students) == 3

    for course_student, course_student in zip(course.students, students):
        assert course_student.name == course_student.name


# test setter students
def test_setter_students() -> None:
    """Test students setter."""
    course = create_new_course()

    course.students = list(students)

    assert len(course.students) == 3

    for course_student, student in zip(course.students, students):
        assert course_student.name == student.name


@pytest.mark.xfail(raises=TypeError)
@pytest.mark.parametrize('test_data', (students, [1, 2, 3]))
def test_setter_students_incorrect_type(test_data: Any) -> None:
    """Test students setter by incorrect type.

    Args:
        test_data(Any): test data for testing.
    """
    create_new_course().students = test_data  # type: ignore


# test add_course_participant
def test_add_course_participant_teacher() -> None:
    """Test adding teacher in course."""
    course = create_new_course()
    course.add_course_participant(teacher1)

    assert course.teacher.name == teacher1.name  # type: ignore


def test_add_course_participant_student() -> None:
    """Test adding student in course."""
    course = create_new_course()
    course.add_course_participant(student1)

    assert course.students[0].name == student1.name


@pytest.mark.xfail(raises=TypeError)
def test_add_course_participant_incorrect_type() -> None:
    """Test adding course participant that has incorrect type."""
    create_new_course().add_course_participant(3)  # type: ignore


# test add_remove_participant
def test_remove_course_participant_teacher() -> None:
    """Test removing teacher from course."""
    course = create_new_course()
    course.add_course_participant(teacher1)
    course.remove_course_participant(teacher1)

    assert course.teacher is None


def test_remove_course_participant_student() -> None:
    """Test removing student from course."""
    course = create_new_course()
    course.add_course_participant(student1)
    course.add_course_participant(student2)
    course.remove_course_participant(student1)

    assert course.students[0].name == student2.name


@pytest.mark.xfail(raises=TypeError)
def test_remove_course_participant_incorrect_type() -> None:
    """Test removing course participant that has incorrect type."""
    create_new_course().remove_course_participant(3)  # type: ignore


@pytest.mark.xfail(raises=ValueError)
def test_remove_course_participant_wrong_student() -> None:
    """Test removing course participant that has incorrect value."""
    course = create_new_course()
    course.add_course_participant(student1)
    course.remove_course_participant(student2)
