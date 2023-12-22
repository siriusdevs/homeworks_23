"""Module with tests for hw3."""

import pytest

from hw3 import Course, EducationalInstitution, Group, Student, Teacher


def test_invalid_instance_creation():
    """Test the creation of class with wrong attributes."""
    with pytest.raises(TypeError):
        Student(1)
    with pytest.raises(TypeError):
        Teacher(2)
    with pytest.raises(TypeError):
        Course(1, 1, 1)
    with pytest.raises(TypeError):
        Group(1, 1, 1)


def test_valid_student_instance_creation():
    """Test of creating Student instance with correct attributes."""
    student = Student('s')
    assert student.name == 's'


def test_valid_teacher_instance_creation():
    """Test of creating Teacher instance with correct attributes."""
    student = Teacher('user')
    assert student.name == 'user'


def test_valid_course_instance_creation():
    """Test of creating Course instance with correct attributes."""
    student1 = Student('s0')
    test_course = Course('AaDS', Teacher('ZernovGA'), [student1])
    assert test_course.title == 'AaDS'
    assert test_course.teacher.name == 'ZernovGA'
    assert test_course.students == [student1]


def test_valid_group_instance_creation():
    """Test of creating Group instance with correct attributes."""
    student = Student('s4')
    test_group = Group('1.9.7.1', [student])
    assert test_group.number == '1.9.7.1'
    assert test_group.students == [student]


def test_valid_edu_institution_instance_creation():
    """Test of creating EducationalInstitution with correct attributes."""
    student = Student('s8')
    courses = Course('kkkk', Teacher('teach2'), [student])
    groups = Group('1.9.7.5', [student])
    university = EducationalInstitution([courses], [groups])
    assert university.courses == [courses]
    assert university.groups == [groups]


def test_educational_institution_operations():
    """Test methods of EducationalInstitution class."""
    student = Student('s1')
    course = Course('AaDS', Teacher('ZernovGA'), [student])
    group = Group('1.9.7.2', [student])
    university = EducationalInstitution([course], [group])
    student2 = Student('s2')
    student3 = Student('s3')
    course2 = Course('proga', Teacher('teacher1'), [student2])
    university.add_course(course2)
    assert university.courses == [course, course2]
    university.remove_course(course2)
    assert university.courses == [course]
    group2 = Group('1.9.7.3', [student3])
    university.add_group(group2)
    assert university.groups == [group, group2]
    university.remove_group(group2)
    assert university.groups == [group]
