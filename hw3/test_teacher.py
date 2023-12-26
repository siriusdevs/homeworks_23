"""Module that tests functionality class Teacher."""
from enum import IntEnum

import pytest

from hw3 import Teacher


class NumberEnum(IntEnum):
    """Enumeration class representing board for age and salary."""

    eighteen = 18
    onethousnd = 1000000
    check = 99


info_of_teacher = (
    ('Boris', 'Gomzaykov', NumberEnum.eighteen, 'Higher mathematics', NumberEnum.onethousnd),
    )


@pytest.mark.parametrize('name, surname, age, faculty, salary', info_of_teacher)
def test_teacher_info(name: str, surname: str, age: int, faculty: str, salary: int) -> None:
    """Test parametrs.

    Args:
        name (str): name of teacher
        surname (str): surname of teacher
        age (int): age of teacher
        faculty (str): faculty of teacher
        salary (int): salary of teacher
    """
    teacher = Teacher(name, surname, age, faculty, salary)
    assert teacher.name == name
    assert teacher.surname == surname
    assert teacher.age == age
    assert teacher.faculty == faculty
    assert teacher.salary == salary


@pytest.mark.xfail(raises=TypeError)
def test_info_invalid():
    """Check setters work."""
    with pytest.raises(TypeError):
        Teacher(
            'Boris',
            'Gomzaykov',
            NumberEnum.eighteen,
            NumberEnum.check,
            NumberEnum.onethousnd,
            )
    with pytest.raises(TypeError):
        Teacher('Boris', 'Gomzaykov', NumberEnum.eighteen, 'Higher mathematics', '1000000')
