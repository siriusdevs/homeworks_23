from copy import deepcopy
from abc import ABC, abstractmethod
from person.person import Person
from copy import deepcopy
import course.abstract_course as abstract_course


class CoursesOwner(ABC, Person):
    @abstractmethod
    def __init__(self, name: str, surname: str, age: int) -> None:
        self.__courses: list['abstract_course.AbstractCourse'] = []
        super().__init__(name, surname, age)


    def add_course(self, new_course: 'abstract_course.AbstractCourse') -> None:
        if not isinstance(new_course, abstract_course.AbstractCourse):
            raise TypeError('This new course has to be a Course instance!')

        if new_course in self.__courses:
            raise ValueError("This course has added in the owner's courses")

        self.__courses.append(new_course)
        new_course.add_course_owner(self)

    def remove_course(self, new_course: 'abstract_course.AbstractCourse') -> None:
        if not isinstance(new_course, abstract_course.AbstractCourse):
            raise TypeError('This new course has to be a Course instance!')

        if new_course not in self.__courses:
            raise ValueError("This course has not been in the owner's courses")

        self.__courses.remove(new_course)
        new_course.remove_course_owner(self)

    @property
    def courses(self) -> list['abstract_course.AbstractCourse']:
        return deepcopy(self.__courses)

    @courses.setter
    def courses(self, new_courses: list['abstract_course.AbstractCourse']) -> None:
        if not isinstance(new_courses, list):
            raise TypeError('The new courses has to be a list!')

        for index, new_course in enumerate(new_courses):
            if not isinstance(new_course, abstract_course.AbstractCourse):
                raise TypeError(
                    f'The new course of {index} index has to be a instance of AbstractCourse'
                )

        for old_course in self.__courses:
            old_course.remove_course_owner(self)

        for new_course in new_courses:
            new_course.add_course_owner(self)

        self.__courses = new_courses

