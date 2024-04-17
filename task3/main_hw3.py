"""This module contains classes for representing a person, a student, a teacher, and a course."""

from typing import Any, Optional


def check_type(
    input_value: Any, types: tuple[type, ...] | type,
    check_positive: Optional[bool] = False,
) -> None:
    """Check if value is of type `types`.

    Args:
        input_value (Any): The value to check.
        types (tuple[type, ...]): The type to check against.
        check_positive (Optional[bool], optional): Check if value is positive. Defaults to False.

    Raises:
        TypeError: If value is not of type `types`.
        ValueError: If value is not positive.
    """
    if not isinstance(input_value, types):
        value_type = type(input_value)
        error_msg = f'Expected type {types}, got {value_type}'
        raise TypeError(error_msg)

    if check_positive and input_value < 0:
        raise ValueError(f'Expected positive value, but got {input_value}')


class Person:
    """Class representing a person."""

    def __init__(self, name: str, surname: str, age: int) -> None:
        """Initialize a Person object.

        Args:
            name (str): The name of the person.
            surname (str): The surname of the person.
            age (int): The age of the person.
        """
        self.name = name
        self.surname = surname
        self.age = age

    @property
    def name(self) -> str:
        """Return the name of the person.

        Returns:
            str: The name of the person.
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """Set the name of the person.

        Args:
            name (str): The name of the person.
        """
        check_type(name, str)
        self._name = name

    @property
    def surname(self) -> str:
        """Return the surname of the person.

        Returns:
            str: The surname of the person.
        """
        return self._surname

    @surname.setter
    def surname(self, surname: str) -> None:
        """Set the surname of the person.

        Args:
            surname (str): The surname of the person.
        """
        check_type(surname, str)
        self._surname = surname

    @property
    def age(self) -> int:
        """Return the age of the person.

        Returns:
            int: The age of the person.
        """
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        """Set the age of the person.

        Args:
            age (int): The age of the person.
        """
        check_type(age, int, check_positive=True)
        self._age = age


class Student(Person):
    """Class representing a student."""

    def __init__(self, name: str, surname: str, age: int, courses: list['Course']) -> None:
        """Initialize a Student object.

        Args:
            name (str): The name of the student.
            surname (str): The surname of the student.
            age (int): The age of the student.
            courses (list[Course]): The courses of the student.
        """
        super().__init__(name, surname, age)
        self.courses = courses

    @property
    def courses(self) -> list['Course']:
        """Return the courses of the student.

        Returns:
            list[Course]: The courses of the student.
        """
        return self._courses

    @courses.setter
    def courses(self, courses: list['Course']) -> None:
        """Set the courses of the student.

        Args:
            courses (list[Course]): The courses of the student.
        """
        check_type(courses, list)

        for course in courses:
            check_type(course, Course)

        self._courses = courses

    def add_course(self, new_course: 'Course') -> None:
        """Add a new course to the list of courses of the student.

        Args:
            new_course (Course): The course to add.
        """
        check_type(new_course, Course)
        self._courses.append(new_course)
        new_course.students.append(self)

    def remove_course(self, course: 'Course') -> None:
        """Remove a course from the list of courses of the student.

        Args:
            course (Course): The course to remove.

        Raises:
            ValueError: If the course is not in the list of courses of the student.
        """
        if course not in self._courses:
            raise ValueError(f'Course {course.name} is not in the list of courses')

        self._courses.remove(course)
        course.students.remove(self)


class Teacher(Person):
    """Class representing a teacher."""

    def __init__(self, name: str, surname: str, age: int, courses: list['Course']) -> None:
        """Initialize a Teacher object.

        Args:
            name (str): The name of the teacher.
            surname (str): The surname of the teacher.
            age (int): The age of the teacher.
            courses (list[Course]): The courses of the teacher.
        """
        super().__init__(name, surname, age)
        self.courses = courses

    @property
    def courses(self) -> list['Course']:
        """Return the courses of the teacher.

        Returns:
            list[Course]: The courses of the teacher.
        """
        return self._courses

    @courses.setter
    def courses(self, courses: list['Course']) -> None:
        """Set the courses of the teacher.

        Args:
            courses (list[Course]): The courses of the teacher.
        """
        check_type(courses, list)

        for course in courses:
            check_type(course, Course)

        self._courses = courses

    def add_course(self, new_course: 'Course') -> None:
        """Add a new course to the list of courses of the teacher.

        Args:
            new_course (Course): The course to add.

        Raises:
            ValueError: If the course is already in the list of courses of the teacher.
        """
        check_type(new_course, Course)

        if new_course in self._courses:
            raise ValueError(f'Course {new_course.name} is already in the list of courses')

        self._courses.append(new_course)

        if new_course.teacher is not None:
            new_course.teacher.remove_course()

        new_course.teacher = self

    def remove_course(self, course: 'Course') -> None:
        """Remove a course from the list of courses of the teacher.

        Args:
            course (Course): The course to remove.

        Raises:
            ValueError: If the course is not in the list of courses of the teacher.
        """
        if course not in self._courses:
            raise ValueError(f'Course {course.name} is not in the list of courses')

        self._courses.remove(course)
        course.teacher = None


class Course:
    """Class representing a course."""

    def __init__(
        self,
        name: str,
        teacher: Teacher | None,
        students: list['Student'],
    ) -> None:
        """Initialize a Course object.

        Args:
            name (str): The name of the course.
            teacher (Teacher): The teacher of the course.
            students (list[Student]): The students of the course.
        """
        self.name = name
        self.teacher = teacher
        self.students = students

    @property
    def name(self) -> str:
        """Return the name of the course.

        Returns:
            str: The name of the course.
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """Set the name of the course.

        Args:
            name (str): The name of the course.
        """
        check_type(name, str)
        self._name = name

    @property
    def teacher(self) -> 'Teacher':
        """Return the teacher of the course.

        Returns:
            Teacher: The teacher of the course.
        """
        return self._teacher

    @teacher.setter
    def teacher(self, teacher: 'Teacher') -> None:
        """Set the teacher of the course.

        Args:
            teacher (Teacher): The teacher of the course.
        """
        if teacher is not None:
            check_type(teacher, Teacher)

        self._teacher = teacher

    @property
    def students(self) -> list['Student']:
        """Return the students of the course.

        Returns:
            list[Student]: The students of the course.
        """
        return self._students

    @students.setter
    def students(self, students: list['Student']) -> None:
        """Set the students of the course.

        Args:
            students (list[Student]): The students of the course.
        """
        check_type(students, list)

        for student in students:
            check_type(student, Student)

        self._students = students
