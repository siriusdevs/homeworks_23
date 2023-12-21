"""
Test module for hw3.

This module contains tests for the classes and functions defined in hw3.
"""

import pytest
from hw3 import Course, Person, Student, Teacher, check_type

AGE30 = 30
AGE20 = 20
AGE35 = 35


def test_check_type():
    """Test the check_type function."""
    assert check_type(5, int) is None
    with pytest.raises(TypeError):
        check_type(5, str)
    with pytest.raises(ValueError):
        check_type(-5, int, check_positive=True)


def test_person():
    """Test the Person class."""
    person = Person('John', 'Doe', AGE30)
    assert person.name == 'John'
    assert person.surname == 'Doe'
    assert person.age == AGE30


def test_student():
    """Test the Student class."""
    teacher = Teacher('Albert', 'Tenigin', AGE35, [])
    course = Course('OOP', teacher, [])
    student = Student('Alex', 'Murphy', AGE20, [course])
    assert student.name == 'Alex'
    assert student.surname == 'Murphy'
    assert student.age == AGE20
    assert student.courses == [course]


def test_course():
    """Test the Course class."""
    teacher = Teacher('Maxim', 'Mikhaylov', AGE35, [])
    student = Student('Ivan', 'Ivanov', AGE20, [])
    course = Course('Administrirovanie', teacher=teacher, students=[student])
    assert course.name == 'Administrirovanie'
    assert course.teacher == teacher
    assert course.students == [student]


def test_teacher():
    """Test the Teacher class."""
    course = Course('UstanovkaINastroykaPeriferiynogoOborudovaniya', None, [])
    teacher = Teacher('Dmitry', 'Torshin', AGE20, [])
    teacher.add_course(course)
    assert course.teacher == teacher
    assert teacher.courses == [course]
    assert teacher.courses[0].name == 'UstanovkaINastroykaPeriferiynogoOborudovaniya'
