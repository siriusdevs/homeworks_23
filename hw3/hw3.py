"""Module for solving task_3.

Task3: Управление учебными курсами
Опишите архитектуру классов для управления учебными курсами.
Вам нужно создать следующие классы:

Класс "Преподаватель":
Поля:
Имя преподавателя
Факультет

Класс "Студент":
Поля:
Имя студента
Возраст

Класс "Курс":
Поля:
Название курса
Преподаватель - объект класса "Преподаватель"
Список студентов - массив или список объектов класса "Студент"
Методы:
Геттеры и сеттеры для полей
Назначить студента на курс
Удалить студента с курса

Класс "Группа":
Поля:
Номер группы
Список студентов - массив или список объектов класса "Студент"
Методы:
Добавить студента в группу
Удалить студента из группы
Получить список всех студентов в группе

Класс "Учебное заведение":
Поля:
Название
Список групп - массив или список объектов класса "Группа"
Список курсов - массив или список объектов класса "Курс"
Методы:
Добавить курс в учебное заведение
Удалить курс из учебного заведения
Получить список всех курсов в учебном заведении
Добавить группу в учебное заведение
Удалить группу из учебного заведения
Получить список всех групп в учебном заведении
"""

from add_decorators import add_simple_list_operations, add_simple_property


@add_simple_property('teacher_name', str)
@add_simple_property('faculty', str)
class Teacher:
    """Teacher of instituion class."""

    def __init__(self, teacher_name: str, faculty: str) -> None:
        """Teacher initialization.

        Args:
            teacher_name: teacher's name
            faculty: teacher's faculty
        """
        self.teacher_name, self.faculty = teacher_name, faculty

    def __str__(self) -> str:
        """Get string representation of the teacher object.

        Returns:
            string representation
        """
        return f'Teacher "{self.teacher_name}" on faculty "{self.faculty}"'


@add_simple_property('student_name', str)
@add_simple_property('age', int)
class Student:
    """Student of instituion class."""

    def __init__(self, student_name: str, age: int) -> None:
        """Student initialization.

        Args:
            student_name: student's name
            age: student's age
        """
        self.student_name, self.age = student_name, age

    def __str__(self) -> str:
        """Get string representation of the student object.

        Returns:
            string representation
        """
        return f'Student "{self.student_name}" {self.age} y.o.'


@add_simple_property('course_name', str)
@add_simple_property('course_teacher', Teacher)
@add_simple_property('course_students', Student, is_list=True)
@add_simple_list_operations('course_students', 'course_student', Student)
class Course:
    """Course of institution class."""

    def __init__(
        self,
        course_name: str,
        course_teacher: Teacher,
        course_students: list[Student],
    ) -> None:
        """Course initialization.

        Args:
            course_name: course's name
            course_teacher: course's teacher
            course_students: students who study on the course
        """
        self.course_name = course_name
        self.course_teacher = course_teacher
        self.course_students = course_students

    def __str__(self) -> str:
        """Get string representation of the course object.

        Returns:
            string representation
        """
        name, teacher, students = self.course_name, self.course_teacher, len(self.course_students)
        return f'Course "{name}" with teacher "{teacher}" and {students} students'


@add_simple_property('group_name', str)
@add_simple_property('group_students', Student, is_list=True)
@add_simple_list_operations('group_students', 'group_student', Student)
class Group:
    """Group of instituion class."""

    def __init__(self, group_name: str, group_students: list[Student]) -> None:
        """Group initialization.

        Args:
            group_name: group's name
            group_students: students who are in the group
        """
        self.group_name, self.group_students = group_name, group_students

    def __str__(self) -> str:
        """Get string representation of the group object.

        Returns:
            string representation
        """
        name, students = self.group_name, len(self.group_students)
        return f'Group "{name}" with {students} students'


@add_simple_property('institution_name', str)
@add_simple_property('institution_courses', Course, is_list=True)
@add_simple_property('institution_groups', Group, is_list=True)
@add_simple_list_operations('institution_courses', 'institution_course', Course)
@add_simple_list_operations('institution_groups', 'institution_group', Group)
class Institution:
    """Institution class."""

    def __init__(
        self,
        institution_name: str,
        institution_courses: list[Course],
        institution_groups: list[Group],
    ) -> None:
        """Institution initialization.

        Args:
            institution_name: institutuion's name
            institution_courses: courses that teach in the institution
            institution_groups: groups that are in the institution
        """
        self.institution_name = institution_name
        self.institution_courses = institution_courses
        self.institution_groups = institution_groups

    def __str__(self) -> str:
        """Get string representation of the institution object.

        Returns:
            string representation
        """
        name = self.institution_name
        courses = len(self.institution_courses)
        groups = len(self.institution_groups)
        return f'Institution "{name}" with {courses} courses and {groups} groups'
