"""Module with a course."""


class Course:
    """Course with its title.

    Attributes:
        title: The title of course (getter, setter).
    """

    def __init__(self, title: str) -> None:
        """Init course.

        Args:
            title(str): the title of current course.
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
