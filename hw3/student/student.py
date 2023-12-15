"""Module with Student."""

import courses_owner.courses_owner as course_owner


class Student(course_owner.CoursesOwner):
    """Student with name, surname, age, courses."""

    def __init__(self, name: str, surname: str, age: int) -> None:
        """Init a new student.

        Args:
            name(str): Person's name.
            surname(str): Person's surname.
            age(int): Person's age.
        """
        super().__init__(name, surname, age)
