import pytest
from typing import Any
from course.course import Course
from teacher.teacher import Teacher
from student.student import Student

teacher1 = Teacher('Teacher1', 'NoSurname1', 30)
teacher2 = Teacher('Teacher2', 'NoSurname2', 50)

student1 = Student('Denis', 'Romodanov', 18)
student2 = Student('Sanya', 'Black', 20)
student3 = Student('New', 'Student', 30)
students = (student1, student2, student3)

def create_new_course() -> Course:
    return Course('Test title')


# test getter teacher
def test_getter_teacher_empty() -> None:
    assert create_new_course().teacher is None

def test_getter_teacher_no_empty() -> None:
    course = create_new_course()
    course.add_course_owner(teacher1)

    assert course.teacher.name == teacher1.name # type: ignore


# test setter teacher
def test_setter_teacher() -> None:
    course = create_new_course()
    course.teacher = teacher1

    assert course.teacher.name == teacher1.name # type: ignore

def test_setter_teacher_some() -> None:
    course = create_new_course()
    course.teacher = teacher1
    course.teacher = teacher2

    assert course.teacher.name == teacher2.name # type: ignore

@pytest.mark.xfail(raises=TypeError)
def test_setter_teacher_incorrect_type() -> None:
    create_new_course().teacher = '23' # type: ignore


# test getter students
def test_getter_student_empty() -> None:
    assert len(create_new_course().students) == 0

def test_getter_students() -> None:
    course = create_new_course()

    for student in students:
        course.add_course_owner(student)

    assert len(course.students) == 3

    for course_student, student in zip(course.students, students):
        assert course_student.name == student.name


# test setter students
def test_setter_students() -> None:
    course = create_new_course()

    course.students = list(students)

    assert len(course.students) == 3

    for course_student, student in zip(course.students, students):
        assert course_student.name == student.name

@pytest.mark.xfail(raises=TypeError)
@pytest.mark.parametrize('test_data', (students, [1, 2, 3]))
def test_setter_students_incorrect_type(test_data: Any) -> None:
    create_new_course().students = test_data # type: ignore


# test add_course_owner
def test_add_course_owner_teacher() -> None:
    course = create_new_course()
    course.add_course_owner(teacher1)

    assert course.teacher.name == teacher1.name # type: ignore

def test_add_course_owner_student() -> None:
    course = create_new_course()
    course.add_course_owner(student1)

    assert course.students[0].name == student1.name

@pytest.mark.xfail(raises=TypeError)
def test_add_course_owner_incorrect_type() -> None:
    create_new_course().add_course_owner(3) # type: ignore


# test add_remove_owner
def test_remove_course_owner_teacher() -> None:
    course = create_new_course()
    course.add_course_owner(teacher1)
    course.remove_course_owner(teacher1)

    assert course.teacher is None

def test_remove_course_owner_student() -> None:
    course = create_new_course()
    course.add_course_owner(student1)
    course.add_course_owner(student2)
    course.remove_course_owner(student1)

    assert course.students[0].name == student2.name

@pytest.mark.xfail(raises=TypeError)
def test_remove_course_owner_incorrect_type() -> None:
    create_new_course().remove_course_owner(3) # type: ignore

@pytest.mark.xfail(raises=ValueError)
def test_remove_course_owner_incorrect_student_value() -> None:
    course = create_new_course()
    course.add_course_owner(student1)
    course.remove_course_owner(student2)
