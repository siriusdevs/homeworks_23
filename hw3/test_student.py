"""Module that tests functionality class Student."""
from enum import IntEnum

import pytest

from hw3 import Student


class AgesNumebrEnum(IntEnum):
    """Enumeration class representing board for age and scholarship."""

    twentynine = 29
    threethousand = 3000
    check = 123


info_of_student = (
    ('Egor', 'Krid', AgesNumebrEnum.twentynine, 'K0709-22/1', AgesNumebrEnum.threethousand),
    )


@pytest.mark.parametrize('name, surname, age, group, scholarship', info_of_student)
def test_students_info(name: str, surname: str, age: int, group: str, scholarship: int) -> None:
    """Tests parametrs.

    Args:
        name (str): name of students
        surname (str): surname of students
        age (int): age of students
        group (str): group of students
        scholarship (int): scholarship of students
    """
    student = Student(name, surname, age, group, scholarship)
    assert student.name == name
    assert student.surname == surname
    assert student.age == age
    assert student.group == group
    assert student.scholarship == scholarship


@pytest.mark.xfail(raises=TypeError)
def test_info_invalid():
    """Check setters work."""
    with pytest.raises(TypeError):
        Student(
            'Egor',
            'Krid',
            AgesNumebrEnum.twentynine,
            AgesNumebrEnum.check,
            AgesNumebrEnum.threethousand,
            )
    with pytest.raises(TypeError):
        Student('Egor', 'Krid', AgesNumebrEnum.twentynine, 'K0709-22/1', '3000')
