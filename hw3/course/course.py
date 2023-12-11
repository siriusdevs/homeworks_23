from hw3.course.abstract_course import AbstractCourse
from hw3.teacher.teacher import Teacher
from hw3.student.student import Student
from typing import Optional, Iterable, TypeGuard
from copy import deepcopy
import hw3.courses_owner.courses_owner as courses_owner


class Course(AbstractCourse):
    def __init__(self, title: str) -> None:
        self.__students: list[Student] = []
        self.__teacher: Optional[Teacher] = None
        super().__init__(title)

    def add_course_owner(self, new_owner: 'courses_owner.CoursesOwner') -> None:
        if not isinstance(new_owner, courses_owner.CoursesOwner):
            raise TypeError('The new course owner has to be a instance of CoursesOwner!')

        match new_owner:
            case Teacher() as new_teacher:
                self.teacher = new_teacher
            case Student() as new_student:
                self.__add_student(new_student)

    def remove_course_owner(self, new_owner: 'courses_owner.CoursesOwner') -> None:
        if not isinstance(new_owner, courses_owner.CoursesOwner):
            raise TypeError('The new course owner has to be a instance of CoursesOwner!')

        match new_owner:
            case Teacher() as teacher:
                if self.__teacher != teacher:
                    raise ValueError('The given teacher is not teach this course!')

                self.__teacher = None
            case Student() as student:
                self.__remove_student(student)

    @property
    def teacher(self) -> Optional[Teacher]:
        return deepcopy(self.__teacher)

    @teacher.setter
    def teacher(self, new_teacher: Teacher) -> None:
        if not isinstance(new_teacher, Teacher):
            raise TypeError('The new teacher has to be a instance of Teacher class!')

        self.__teacher = new_teacher

    @property
    def students(self) -> list[Student]:
        return deepcopy(self.__students)

    @students.setter
    def students(self, new_students: list[Student]) -> None:
        if not isinstance(new_students, list):
            raise TypeError('The new students has to a list!')

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
