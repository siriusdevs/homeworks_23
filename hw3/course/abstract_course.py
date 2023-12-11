from abc import ABC, abstractmethod
import hw3.courses_owner.courses_owner as courses_owner


class AbstractCourse(ABC):
    @abstractmethod
    def __init__(self, title: str) -> None:
        self.title = title

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, new_title: str) -> None:
        if not isinstance(new_title, str):
            raise TypeError('The new title has to be a string value!')

        if not len(new_title):
            raise ValueError('The new title does not have to be a empty string!')

        self.__title = new_title

    def __str__(self) -> str:
        return f'Course {self.title}'

    def __repr__(self) -> str:
        return f'Course {self.title}'


    @abstractmethod
    def add_course_owner(self, new_owner: 'courses_owner.CoursesOwner') -> None:
        pass

    @abstractmethod
    def remove_course_owner(self, new_owner: 'courses_owner.CoursesOwner') -> None:
        pass
