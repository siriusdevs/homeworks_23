"""Module for testing Person class."""
import pytest
from person.person import Person

person1 = Person('Ilya', 'Kirillov', 23)
person2 = Person('Sanya', 'Cherniy', 34)
person3 = Person('Harry', 'Potter', 17)

persons = [person1, person2, person3]


def create_new_user() -> 'Person':
    """Create a clean person.

    Returns:
        Person: Clean Person.
    """
    return Person('noname', 'nosurname', 50)


# getter name
TEST_PERSONS_NAME_DATA = zip(persons, ('Ilya', 'Sanya', 'Harry'))


@pytest.mark.parametrize('person, expected', TEST_PERSONS_NAME_DATA)
def test_getter_name(person: 'Person', expected: str) -> None:
    """Test getter name.

    Args:
        person(Person): The given person.
        expected(str): expected result.
    """
    assert person.name == expected


# getter surname
TEST_PERSONS_SURNAME_DATA = zip(persons, ('Kirillov', 'Cherniy', 'Potter'))


@pytest.mark.parametrize('person, expected', TEST_PERSONS_SURNAME_DATA)
def test_getter_surname(person: 'Person', expected: str) -> None:
    """Test getter surname.

    Args:
        person(Person): The given person.
        expected(str): expected result.
    """
    assert person.surname == expected


# getter age
TEST_PERSONS_AGE_DATA = zip(persons, (23, 34, 17))


@pytest.mark.parametrize('person, expected', TEST_PERSONS_AGE_DATA)
def test_getter_age(person: 'Person', expected: int) -> None:
    """Test getter age.

    Args:
        person(Person): The given person.
        expected(int): expected result.
    """
    assert person.age == expected


# setter name
def test_setter_name() -> None:
    """Test setter name."""
    new_name = '__new_name__'
    new_person = create_new_user()
    new_person.name = new_name

    assert new_person.name == new_name


@pytest.mark.xfail(raises=TypeError)
def test_setter_name_incorrect_type() -> None:
    """Test setter name by incorrect type."""
    create_new_user().name = 34  # type: ignore


@pytest.mark.xfail(raises=ValueError)
def test_setter_name_incorrect_value() -> None:
    """Test setter name by incorrect value."""
    create_new_user().name = ''


# setter surname
def test_setter_surname() -> None:
    """Test setter surname."""
    new_surname = '__new_surname__'
    new_person = create_new_user()
    new_person.surname = new_surname

    assert new_person.surname == new_surname


@pytest.mark.xfail(raises=TypeError)
def test_setter_surname_incorrect_type() -> None:
    """Test setter surname by type."""
    create_new_user().surname = 34  # type: ignore


@pytest.mark.xfail(raises=ValueError)
def test_setter_surname_incorrect_value() -> None:
    """Test setter surname by value."""
    create_new_user().surname = ''


# setter age
def test_setter_age() -> None:
    """Test setter age."""
    new_age = 36
    new_person = create_new_user()
    new_person.age = new_age

    assert new_person.age == new_age


@pytest.mark.xfail(raises=TypeError)
def test_setter_age_incorrect_type() -> None:
    """Test setter age by type."""
    create_new_user().age = '34'  # type: ignore


@pytest.mark.xfail(raises=ValueError)
@pytest.mark.parametrize('expected', (-5, 150))
def test_setter_age_incorrect_value(expected: int) -> None:
    """Test setter age by value.

    Args:
        expected(int): expected result.
    """
    create_new_user().age = expected
