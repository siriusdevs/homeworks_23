"""Module with Student."""
from courses_participant.courses_participant import CoursesParticipant
from person.person import Person


class Student(Person, CoursesParticipant):
    """Student with name, surname, age, courses."""

    def __init__(self, name: str, surname: str, age: int) -> None:
        """Init a new student.

        Args:
            name(str): Person's name.
            surname(str): Person's surname.
            age(int): Person's age.
        """
        super().__init__(name, surname, age)
