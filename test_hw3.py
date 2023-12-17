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
    teacher = Teacher('Jane', 'Doe', AGE35, [])
    course = Course('Math', teacher, [])
    student = Student('John', 'Doe', AGE20, [course])
    assert student.name == 'John'
    assert student.surname == 'Doe'
    assert student.age == AGE20
    assert student.courses == [course]


def test_course():
    """Test the Course class."""
    teacher = Teacher('Jane', 'Doe', AGE35, [])
    student = Student('John', 'Doe', AGE20, [])
    course = Course('Math', teacher, [student])
    assert course.name == 'Math'
    assert course.teacher == teacher
    assert course.students == [student]
