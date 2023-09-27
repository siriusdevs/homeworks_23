"""tests for hw3 module."""
import pytest

from hw3 import Course, EducationalInstitution, Group, Student, Teacher


def test_teacher_create_course():
    """Test teacher create course."""
    teacher = Teacher('Albert')
    course = teacher.create_course('Programming')
    assert course.course_name == 'Programming'
    assert course.teacher == teacher


def test_teacher_assign_student():
    """Test teacher assign student."""
    teacher = Teacher('Boris')
    course = Course('Math', teacher)
    student = Student('Fedor')
    teacher.assign_student(course, student)
    assert student in course.students


def test_student_enroll_and_drop_course():
    """Test student enroll."""
    student = Student('Matvey')
    course = Course('Physics', Teacher('Sergey'))
    student.enroll(course)
    assert student in course.students
    student.drop_course(course)
    assert student not in course.students


def test_group_add_and_remove_student():
    """Test group add student."""
    group = Group('К0709')
    student = Student('Vlad')
    group.add_student(student)
    assert student in group.students
    group.remove_student(student)
    assert student not in group.students


def test_edu_institution_add_and_remove_course():
    """Test educational institution add course."""
    institution = EducationalInstitution()
    course = Course('Networks', Teacher('Vyacheslav'))
    institution.add_course(course)
    assert course in institution.courses
    institution.remove_course(course)
    assert course not in institution.courses


def test_edu_institution_add_and_remove_group():
    """Test educational institution add and remove group."""
    institution = EducationalInstitution()
    group = Group('К0609')
    institution.add_group(group)
    assert group in institution.groups
    institution.remove_group(group)
    assert group not in institution.groups


def test_creation_raises_error():
    """Test for wrong arguments."""
    with pytest.raises(TypeError):
        Teacher(1)
    with pytest.raises(TypeError):
        EducationalInstitution(5)
    with pytest.raises(TypeError):
        Group.add_student(1)
    with pytest.raises(TypeError):
        Course.remove_student('MARKO')
