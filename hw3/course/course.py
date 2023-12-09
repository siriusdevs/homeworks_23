from hw3.course.abstract_course import AbstractCourse
from hw3.teacher import Teacher
from hw3.student import Student
import hw3.courses_owner
from typing import Optional, Iterable
from copy import deepcopy


class Course(AbstractCourse):
    def __init__(self, title: str) -> None:
        self.title = title
        self.__students: list[Student] = []
        self.__teacher: Optional[Teacher] = None

    def add_course_owner(self, new_owner: 'hw3.courses_owner.CoursesOwner') -> None:
        if not isinstance(new_owner, hw3.courses_owner.CoursesOwner):
            raise TypeError('The new course owner has to be a instance of CoursesOwner!')

        match new_owner:
            case Teacher() as new_teacher:
                self.teacher = new_teacher
            case Student() as new_student:
                self.__add_student(new_student)
            case _:
                raise TypeError('add_new_owner does not know how to handle your course owner!')

    def remove_course_owner(self, new_owner: 'hw3.courses_owner.CoursesOwner') -> None:
        if not isinstance(new_owner, hw3.courses_owner.CoursesOwner):
            raise TypeError('The new course owner has to be a instance of CoursesOwner!')

        match new_owner:
            case Teacher() as new_teacher:
                self.teacher = new_teacher
            case Student() as new_student:
                self.__remove_student(new_student)
            case _:
                raise TypeError('remove_course_owner does not know how to handle your course owner!')

    @property
    def teacher(self) -> Optional[Teacher]:
        return deepcopy(self.__teacher)

    @teacher.setter
    def teacher(self, new_teacher: Optional[Teacher]) -> None:
        if not isinstance(new_teacher, Teacher):
            raise TypeError('The new teacher has to be a instance of Teacher class!')

        self.__teacher = new_teacher

    @property
    def students(self) -> list[Student]:
        return deepcopy(self.__students)

    @students.setter
    def students(self, new_students: Iterable[Student]) -> None:
        if not hasattr(new_students, '__iter__'):
            raise TypeError('The new students has to a iterable object!')

        for index, new_student in enumerate(new_students):
            if not isinstance(new_student, Student):
                raise TypeError(f'The student of {index} index is not a instance of Student!')

        self.__students = list(new_students)

    def __add_student(self, new_student: Student) -> None:
        if not isinstance(new_student, Student):
            raise TypeError('The new student has to be a instance of Student!')

        if new_student in self.__students:
            raise ValueError('This student has added in this course!')

        self.__students.append(new_student)

    def __remove_student(self, student: Student) -> None:
        if not isinstance(student, Student):
            raise TypeError('The new student has to be a instance of Student!')

        if student not in self.__students:
            raise ValueError('This student has not been in this course!')

        self.__students.remove(student)

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
        return f'Course with title = {self.title}'

    def __repr__(self) -> str:
        return f'Course with title = {self.title}'
