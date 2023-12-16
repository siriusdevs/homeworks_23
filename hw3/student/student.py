"""Module with Student."""
from courses_owner.courses_owner import CoursesOwner
from person.person import Person


class Student(Person, CoursesOwner):
    """Student with name, surname, age, courses."""

    def __init__(self, name: str, surname: str, age: int) -> None:
        """Init a new student.

        Args:
            name(str): Person's name.
            surname(str): Person's surname.
            age(int): Person's age.
        """
        super().__init__(name, surname, age)
