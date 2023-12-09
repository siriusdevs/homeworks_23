from abc import ABC, abstractmethod
import hw3.courses_owner


class AbstractCourse(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def add_course_owner(self, new_owner: 'hw3.courses_owner.CoursesOwner') -> None:
        pass

    @abstractmethod
    def remove_course_owner(self, new_owner: 'hw3.courses_owner.CoursesOwner') -> None:
        pass
