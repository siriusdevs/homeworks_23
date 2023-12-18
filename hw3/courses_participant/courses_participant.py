"""Module with courses participant."""
from abc import ABC, abstractmethod
from copy import deepcopy
from typing import Any

import course.abstract_course as abstract_course


class CoursesParticipant(ABC):
    """The person that participants courses.

    Attributes:
        courses(list[AbstractCourse]): Courses that are being learnt of person.

    Methods:
        add_course_participant(new_participant: CoursesParticipant) -> None:
            Add course participant to course's collection of the type of the given new_participant.
        remove_course_participant(participant: CoursesParticipant) -> None:
            Remove course participant from course's of the type of the given participant.
    """

    @abstractmethod
    def __init__(self, **kwargs: Any) -> None:
        """Init courses participant.

        Args:
            kwargs(Any): arguments for any classes in the inheritance chain.
        """
        self.__courses: list['abstract_course.AbstractCourse'] = []
        super().__init__(**kwargs)

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
            raise ValueError("This course has added in the participant's courses")

        self.__courses.append(new_course)
        new_course.add_course_participant(self)

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
            raise ValueError("This course has not been in the participant's courses")

        self.__courses.remove(course)
        course.remove_course_participant(self)

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
            old_course.remove_course_participant(self)

        for new_course in new_courses:
            new_course.add_course_participant(self)

        self.__courses = new_courses
