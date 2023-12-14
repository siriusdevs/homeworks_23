"""Module with courses owner."""
from abc import ABC, abstractmethod
from copy import deepcopy

import course.abstract_course as abstract_course
from person.person import Person


class CoursesOwner(ABC, Person):
    """The person that owners courses.

    Attributes:
        name: Person's name.
        surname: Person's surname.
        age: Person's age.
        courses: Courses that are being learnt of person.

    Methods:
        add_course_owner(new_owner: CourseOwner) -> None:
            Add course owner to course's collection of the type of the given new_owner.
        remove_course_owner(owner: CourseOwner) -> None:
            Remove course owner from course's of the type of the given owner.
    """

    @abstractmethod
    def __init__(self, name: str, surname: str, age: int) -> None:
        """Init courses owner.

        Args:
            name(str): Person's name.
            surname(str): Person's surname.
            age(int): Person's age.
        """
        self.__courses: list['abstract_course.AbstractCourse'] = []
        super().__init__(name, surname, age)

    def add_course(self, new_course: 'abstract_course.AbstractCourse') -> None:
        """Add course for person.

        Args:
            new_course(AbstractCourse): New course.

        Raises:
            TypeError: It is not a course.
            ValueError: This course has been added to person's courses.
        """
        if not isinstance(new_course, abstract_course.AbstractCourse):
            raise TypeError('This new course has to be a Course instance!')

        if new_course in self.__courses:
            raise ValueError("This course has added in the owner's courses")

        self.__courses.append(new_course)
        new_course.add_course_owner(self)

    def remove_course(self, course: 'abstract_course.AbstractCourse') -> None:
        """Remove course for person.

        Args:
            course(AbstractCourse): Course that has been added to person's courses.

        Raises:
            TypeError: It's not a course.
            ValueError: This course hasn't been added to person's courses.
        """
        if not isinstance(course, abstract_course.AbstractCourse):
            raise TypeError('This new course has to be a Course instance!')

        if course not in self.__courses:
            raise ValueError("This course has not been in the owner's courses")

        self.__courses.remove(course)
        course.remove_course_owner(self)

    @property
    def courses(self) -> list['abstract_course.AbstractCourse']:
        """Get courses.

        Returns:
            list[AbstractCourse]: person's courses.
        """
        return deepcopy(self.__courses)

    @courses.setter
    def courses(self, new_courses: list['abstract_course.AbstractCourse']) -> None:
        """Set new courses.

        Args:
            new_courses(list[AbstractCourse]): New courses.

        Raises:
            TypeError: It's not a list of courses.
            TypeError: The list has value that is not a course.
        """
        if not isinstance(new_courses, list):
            raise TypeError('The new courses has to be a list!')

        for index, course in enumerate(new_courses):
            if not isinstance(course, abstract_course.AbstractCourse):
                raise TypeError(
                    f'The new course of {index} index has to be a instance of AbstractCourse',
                )

        for old_course in self.__courses:
            old_course.remove_course_owner(self)

        for new_course in new_courses:
            new_course.add_course_owner(self)

        self.__courses = new_courses
