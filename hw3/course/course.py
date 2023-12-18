"""Module with course that has a teacher and students."""
from copy import deepcopy
from typing import Optional

import courses_participant.courses_participant as courses_participant
from course.abstract_course import AbstractCourse
from student.student import Student
from teacher.teacher import Teacher


class Course(AbstractCourse):
    """Course that has a teacher and students.

    Attributes:
        title: The title of course.
        teacher: The person that is teaching this course.
        students: The persons that are learning this course.

    Methods:
        add_course_participant(new_participant: CoursesParticipant) -> None:
            Add course participant to course's collection of the type of the given new_participant.
        remove_course_participant(participant: CoursesParticipant) -> None:
            Remove course participant from course's of the type of the given participant.
    """

    def __init__(self, title: str) -> None:
        """Init course's instances.

        Args:
            title(str): The title of this course.
        """
        self.__students: list[Student] = []
        self.__teacher: Optional[Teacher] = None
        super().__init__(title)

    def add_course_participant(
        self,
        new_participant: 'courses_participant.CoursesParticipant',
    ) -> None:
        """Add course participant to course (It can be teacher or student).

        Args:
            new_participant(CoursesParticipant): course participant (teacher or student).

        Raises:
            TypeError: The given new_participant is not a CoursesParticipant's instance.
        """
        if not isinstance(new_participant, courses_participant.CoursesParticipant):
            raise TypeError(
                'The new course participant has to be a instance of CoursesParticipant!',
            )

        if isinstance(new_participant, Teacher):
            self.teacher = new_participant
        elif isinstance(new_participant, Student):
            self.__add_student(new_participant)

    def remove_course_participant(
        self,
        new_participant: 'courses_participant.CoursesParticipant',
    ) -> None:
        """Remove course participant from course (It can be teacher or student).

        Args:
            new_participant(CoursesParticipant): course participant (teacher or student).

        Raises:
            TypeError: The given new_participant is not a CoursesParticipant's instance.
            ValueError: Student is not in this courses or teacher is not teach this course.
        """
        if not isinstance(new_participant, courses_participant.CoursesParticipant):
            raise TypeError(
                'The new course participant has to be a instance of CoursesParticipant!',
            )

        if isinstance(new_participant, Teacher):
            if self.__teacher != new_participant:
                raise ValueError('The given teacher is not teach this course!')

            self.__teacher = None
        elif isinstance(new_participant, Student):
            self.__remove_student(new_participant)

    @property
    def teacher(self) -> Optional[Teacher]:
        """Get teacher.

        Returns:
            Optional[Teacher]: teacher of this course (can be None).
        """
        return deepcopy(self.__teacher)

    @teacher.setter
    def teacher(self, new_teacher: Teacher) -> None:
        """Set new teacher.

        Args:
            new_teacher(Teacher): The given instance of teacher.

        Raises:
            TypeError: The given teacher is not a teacher's instance.
        """
        if not isinstance(new_teacher, Teacher):
            raise TypeError('The new teacher has to be a instance of Teacher class!')

        self.__teacher = new_teacher

    @property
    def students(self) -> list[Student]:
        """Get students.

        Returns:
            list[Student]: The students of this course.
        """
        return deepcopy(self.__students)

    @students.setter
    def students(self, new_students: list[Student]) -> None:
        """Set new students.

        Args:
            new_students(list[Student]): The given students.

        Raises:
            TypeError: The given object is not a list.
            TypeError: Some object in list is not a student.
        """
        if not isinstance(new_students, list):
            raise TypeError('The new students has to a list!')

        for index, new_student in enumerate(new_students):
            if not isinstance(new_student, Student):
                raise TypeError(f'The student of {index} index is not a instance of Student!')

        self.__students = list(new_students)

    def __add_student(self, new_student: Student) -> None:
        """Add a new student.

        Args:
            new_student(Student): New student.

        Raises:
            TypeError: The given object is not a student.
            ValueError: The given student has added in this course already.
        """
        if not isinstance(new_student, Student):
            raise TypeError('The new student has to be a instance of Student!')

        if new_student in self.__students:
            raise ValueError('This student has added in this course already!')

        self.__students.append(new_student)

    def __remove_student(self, student: Student) -> None:
        """Remove student.

        Args:
            student(Student): The given student.

        Raises:
            TypeError: The given student is not a student.
            ValueError: The given student is not in this course.
        """
        if not isinstance(student, Student):
            raise TypeError('The new student has to be a instance of Student!')

        if student not in self.__students:
            raise ValueError('This student has not been in this course!')

        self.__students.remove(student)
