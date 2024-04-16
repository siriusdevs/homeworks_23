"""Test module for main module.

This test module contains tests for the classes and functions defined in module main."""

import pytest

from main_hw3 import Course, Person, Student, Teacher, check_type

AGE20 = 20
AGE30 = 30
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

    person = Person('Vladislav', 'Nesterov', AGE30)
    assert person.name == 'Vladislav'
    assert person.surname == 'Nesterov'
    assert person.age == AGE30


def test_student():

    """Test the Student class."""

    teacher = Teacher('Ivan', 'Golodnuk', AGE20, [])
    course = Course('OOP', teacher, [])
    student = Student('Alex', 'Karateev', AGE20, [course])
    assert student.name == 'Alex'
    assert student.surname == 'Karateev'
    assert student.age == AGE20
    assert student.courses == [course]


def test_course():

    """Test the Course class."""

    teacher = Teacher('Vladislav', 'Nesterov', AGE35, [])
    student = Student('Alex', 'Karateev', AGE20, [])
    course = Course('VibivanieDuri', teacher=teacher, students=[student])
    assert course.name == 'VibivanieDuri'
    assert course.teacher == teacher
    assert course.students == [student]


def test_teacher():

    """Test the Teacher class."""

    course = Course('PinanieBolta', None, [])
    teacher = Teacher('Kaplan', 'Narotov', AGE20, [])
    teacher.add_course(course)
    assert course.teacher == teacher
    assert teacher.courses == [course]
    assert teacher.courses[0].name == 'PinanieBolta'
