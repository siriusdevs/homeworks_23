"""Module with a abstract course."""
from abc import ABC, abstractmethod
import courses_owner.courses_owner as courses_owner


class AbstractCourse(ABC):
    """Abstract course that has to be inheritable.

    Attributes:
        title: The title of course.

    Methods:
        add_course_owner(new_owner: CourseOwner) -> None:
            Add course owner to course's collection of the type of the given new_owner.
        remove_course_owner(owner: CourseOwner) -> None:
            Remove course owner from course's of the type of the given owner.
    """
    @abstractmethod
    def __init__(self, title: str) -> None:
        """Init course.

        Args:
            title(str): the course's title.
        """
        self.title = title

    @property
    def title(self) -> str:
        """Get title of the current course.

        Returns:
            str: title of the current course.
        """
        return self.__title

    @title.setter
    def title(self, new_title: str) -> None:
        """Set new title for the current course.

        Args:
            new_title(str): New title.

        Raises:
            TypeError: If the given title is not a string.
            ValueError: If the given title is a empty string.
        """
        if not isinstance(new_title, str):
            raise TypeError('The new title has to be a string value!')

        if not len(new_title):
            raise ValueError('The new title does not have to be a empty string!')

        self.__title = new_title

    def __str__(self) -> str:
        """Get string presentation for course object.

        Returns:
            str: f'Course {self.title}'
        """
        return f'Course {self.title}'

    def __repr__(self) -> str:
        """Get string presentation for course object in debug mode.

        Returns:
            str: f'Course {self.title}'
        """
        return f'Course {self.title}'


    @abstractmethod
    def add_course_owner(self, new_owner: 'courses_owner.CoursesOwner') -> None:
        pass

    @abstractmethod
    def remove_course_owner(self, new_owner: 'courses_owner.CoursesOwner') -> None:
        pass
