"""Module with courses participant."""
from abc import ABC, abstractmethod
from copy import deepcopy
from typing import Any, Optional

import course_with_participants.course_with_participants as course_with_participants


class CoursesParticipant(ABC):
    """The person that has connected courses.

    Attributes:
        courses(list[CourseWithParticipants]): Courses that are connected with this person.

    Methods:
        add_course(
            new_course(CourseWithParticipants): the new given course to add,
            need_add_participant_to_course: Optional[bool] = True,
        ) -> None:
            Add a course to participant's collection
            and add the participants to the given course' collection
            if need_add_participant_to_course is True.

        remove_course(
            course: CourseWithParticipants,
            need_remove_participant_from_course: Optional[bool] = True,
        ) -> None:
            Remove course from participant's collection
            and remove the participant from course' collection
            if need_remove_participant_from_course is True.
    """

    @abstractmethod
    def __init__(self, **kwargs: Any) -> None:
        """Init courses participant.

        Args:
            kwargs(Any): arguments for any classes in the inheritance chain.
        """
        self.__courses: list['course_with_participants.CourseWithParticipants'] = []
        super().__init__(**kwargs)

    def add_course(
        self,
        new_course: 'course_with_participants.CourseWithParticipants',
        need_add_participant_to_course: Optional[bool] = True,
    ) -> None:
        """Add course to participant's collection and add this person to the given course \
        if need_add_participant_to_course is True.

        Args:
            new_course(CourseWithParticipants): The new course for adding.
            need_add_participant_to_course(Optional[bool] = True): \
                need to add participant to the given course?

        Raises:
            TypeError: It is not a CourseWithParticipants.
            ValueError: This course has been added to participants's collection.
        """
        if not isinstance(new_course, course_with_participants.CourseWithParticipants):
            raise TypeError('This new course has to be a CourseWithParticipants instance!')

        if new_course in self.__courses:
            raise ValueError("This course has added in the participant's collection")

        self.__courses.append(new_course)

        if need_add_participant_to_course:
            new_course.add_course_participant(self, need_add_course_to_participant=False)

    def remove_course(
        self,
        course: 'course_with_participants.CourseWithParticipants',
        need_remove_participant_from_course: Optional[bool] = True,
    ) -> None:
        """Remove course from participant's collection.

        Args:
            course(CourseWithParticipants): The given course for removing.
            need_remove_participant_from_course(Optional[bool] = True): \
                need to remove participant from the given course?

        Raises:
            TypeError: It's not a CourseWithParticipants.
            ValueError: This course hasn't been added to participant's collection.
        """
        if not isinstance(course, course_with_participants.CourseWithParticipants):
            raise TypeError('This new course has to be a Course instance!')

        if course not in self.__courses:
            raise ValueError("This course has not been in the participant's courses")

        self.__courses.remove(course)

        if need_remove_participant_from_course:
            course.remove_course_participant(self, need_remove_course_from_participant=False)

    @property
    def courses(self) -> list['course_with_participants.CourseWithParticipants']:
        """Get courses.

        Returns:
            list[Course]: person's courses.
        """
        return deepcopy(self.__courses)

    @courses.setter
    def courses(
        self,
        new_courses: list['course_with_participants.CourseWithParticipants'],
    ) -> None:
        """Set new courses.

        Args:
            new_courses(list[Course]): New courses.

        Raises:
            TypeError: It's not a list of courses.
            TypeError: The list has value that is not a CourseWithParticipants' instance.
        """
        if not isinstance(new_courses, list):
            raise TypeError('The new courses has to be a list!')

        for index, course in enumerate(new_courses):
            if not isinstance(course, course_with_participants.CourseWithParticipants):
                raise TypeError(
                    f'The new course of {index} index has to be a instance of Course',
                )

        for old_course in self.__courses:
            old_course.remove_course_participant(self)

        for new_course in new_courses:
            new_course.add_course_participant(self)
