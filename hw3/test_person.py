"""Module that tests functionality class Person."""
from enum import IntEnum

import pytest

from hw3 import Person


class AgeNumebrEnum(IntEnum):
    """Enumeration class representing board for age."""

    thirtythree = 33
    thirtyone = 31


info_of_person = (
    ('Anna', 'Asti', AgeNumebrEnum.thirtythree),
    ('Mari', 'Kraimbrery', AgeNumebrEnum.thirtyone),
    )


@pytest.mark.parametrize('name, surname, age', info_of_person)
def test_persons_info(name: str, surname: str, age: int) -> None:
    """Tests parametrs.

    Args:
        name (str): name of person
        surname (str): surname of person
        age (int): age of person
    """
    person = Person(name, surname, age)
    assert person.name == name
    assert person.surname == surname
    assert person.age == age


@pytest.mark.xfail(raises=TypeError)
def test_info_invalid():
    """Check setters work."""
    with pytest.raises(TypeError):
        Person(4, 'Asti', AgeNumebrEnum.thirtythree)
    with pytest.raises(TypeError):
        Person('Mari', 3, AgeNumebrEnum.thirtyone)
    with pytest.raises(TypeError):
        Person('Mari', 'Kraimbrery', '31')
