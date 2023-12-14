from person.person import Person
import pytest

person1 = Person('Ilya', 'Kirillov', 23)
person2 = Person('Sanya', 'Cherniy', 34)
person3 = Person('Harry', 'Potter', 17)

persons = [person1, person2, person3]

def create_new_user() -> 'Person':
    return Person('noname', 'nosurname', 50)

# getter name
TEST_PERSONS_NAME_DATA = zip(persons, ('Ilya', 'Sanya', 'Harry'))

@pytest.mark.parametrize('person, expected', TEST_PERSONS_NAME_DATA)
def test_getter_name(person: 'Person', expected: str) -> None:
    assert person.name == expected

# getter surname
TEST_PERSONS_SURNAME_DATA = zip(persons, ('Kirillov', 'Cherniy', 'Potter'))

@pytest.mark.parametrize('person, expected', TEST_PERSONS_SURNAME_DATA)
def test_getter_surname(person: 'Person', expected: str) -> None:
    assert person.surname == expected

# getter age
TEST_PERSONS_AGE_DATA = zip(persons, (23, 34, 17))

@pytest.mark.parametrize('person, expected', TEST_PERSONS_AGE_DATA)
def test_getter_age(person: 'Person', expected: int) -> None:
    assert person.age == expected

# setter name
def test_setter_name() -> None:
    NEW_NAME = '__new_name__'
    new_person = create_new_user()
    new_person.name = NEW_NAME

    assert new_person.name == NEW_NAME

@pytest.mark.xfail(raises=TypeError)
def test_setter_name_incorrect_type() -> None:
    create_new_user().name = 34 # type: ignore

@pytest.mark.xfail(raises=ValueError)
def test_setter_name_incorrect_value() -> None:
    create_new_user().name = ''

# setter surname
def test_setter_surname() -> None:
    NEW_SURNAME = '__new_surname__'
    new_person = create_new_user()
    new_person.surname = NEW_SURNAME

    assert new_person.surname == NEW_SURNAME

@pytest.mark.xfail(raises=TypeError)
def test_setter_surname_incorrect_type() -> None:
    create_new_user().surname = 34 # type: ignore

@pytest.mark.xfail(raises=ValueError)
def test_setter_surname_incorrect_value() -> None:
    create_new_user().surname = ''

# setter age
def test_setter_age() -> None:
    NEW_AGE = 36
    new_person = create_new_user()
    new_person.age = NEW_AGE

    assert new_person.age == NEW_AGE

@pytest.mark.xfail(raises=TypeError)
def test_setter_age_incorrect_type() -> None:
    create_new_user().age = '34' # type: ignore

@pytest.mark.xfail(raises=ValueError)
@pytest.mark.parametrize('expected', (-5, 150))
def test_setter_age_incorrect_value(expected: int) -> None:
    create_new_user().age = expected
