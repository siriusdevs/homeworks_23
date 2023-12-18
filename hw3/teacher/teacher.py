"""Module with Teacher."""
from courses_participant.courses_participant import CoursesParticipant
from person.person import Person


class Teacher(Person, CoursesParticipant):
    """Teacher with name, surname, age, courses."""

    def __init__(self, name: str, surname: str, age: int) -> None:
        """Init a new teacher.

        Args:
            name(str): Person's name.
            surname(str): Person's surname.
            age(int): Person's age.
        """
        super().__init__(name, surname, age)
