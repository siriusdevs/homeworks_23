"""Module with Teacher."""
from courses_owner.courses_owner import CoursesOwner


class Teacher(CoursesOwner):
    """Teacher with name, surname, age, courses."""

    def __init__(self, name: str, surname: str, age: int) -> None:
        """Init a new teacher.

        Args:
            name(str): Person's name.
            surname(str): Person's surname.
            age(int): Person's age.
        """
        super().__init__(name, surname, age)
