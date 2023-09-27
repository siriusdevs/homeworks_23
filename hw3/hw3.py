"""
hw3 module.

Управление учебными курсами

Опишите архитектуру классов для управления учебными курсами. Вам нужно создать следующие классы:

Класс "Преподаватель":
Поля:
Имя преподавателя
Методы:
Создать новый курс
Назначить студента на курс

Класс "Студент":
Поля:
Имя студента
Методы:
Записаться на курс
Отписаться от курса

Класс "Курс":
Поля:
Название курса
Преподаватель - объект класса "Преподаватель"
Список студентов - массив или список объектов класса "Студент"
Методы:
Геттеры и сеттеры для полей

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
Список курсов - массив или список объектов класса "Курс"
Методы:
Добавить курс в учебное заведение
Удалить курс из учебного заведения
Получить список всех курсов в учебном заведении
Добавить группу в учебное заведение
Удалить группу из учебного заведения
Получить список всех групп в учебном заведении
"""


from typing import Any


def check_type(
    input_value: Any,
    types: tuple[type, ...] | type,
) -> None:
    """
    Check if value is of type `types`.

    Args:
        input_value (Any): The value to check.
        types (tuple[type, ...]): The type to check against.

    Raises:
        TypeError: If value is not of type `types`.
    """
    if not isinstance(input_value, types):
        value_type = type(input_value)
        error_msg = f'Expected type {types.__name__}, got {value_type.__name__}'
        raise TypeError(error_msg)


class Teacher:
    """Represents a teacher.

    Attributes:
        name (str): The name of the teacher.
    """

    def __init__(self, name: str) -> None:
        """Initialize a Student object with the given student name.

        Args:
            name (str): The name of the Teacher.
        """
        check_type(name, str)
        self.name = name

    def create_course(self, course_name: str) -> 'Course':
        """Create the course as the teacher.

        Args:
            course_name (str): The name of course.

        Returns:
            Course: The created course.
        """
        check_type(course_name, str)
        return Course(course_name, self)

    def assign_student(self, course: 'Course', student: 'Student') -> None:
        """Assign the student as the teacher.

        Args:
            course (Course): The assigned course.
            student (Student): Thr assigned student.
        """
        check_type(course, Course)
        check_type(student, Student)
        course.add_student(student)


class Student:
    """Represents a student.

    Attributes:
        name (str): The name of the student.
    """

    def __init__(self, name: str) -> None:
        """Initialize a Student object with the given student name.

        Args:
            name (str): The name of student
        """
        check_type(name, str)
        self.name = name

    def enroll(self, course: 'Course') -> None:
        """Enrolls the student in a specific course.

        Args:
            course (Course): The course to enroll in.
        """
        check_type(course, Course)
        course.add_student(self)

    def drop_course(self, course: 'Course') -> None:
        """Remove the course from the student.

        Args:
            course (Course): The course to remove in.
        """
        check_type(course, Course)
        course.remove_student(self)


class AbstractCourse:
    """Represents a course in a school.

    Attributes:
        course_name (str): The name of the course.
        teacher (Teacher): The teacher of the course.
        students (list): The students enrolled in the course.
    """

    def __init__(self, course_name: str, teacher: Teacher) -> None:
        """Initialize a Course object with the given course name.

        Args:
            course_name (str): The name of the course.
            teacher (Teacher): The name of the teacher.
        """
        self.course_name = course_name
        self.teacher = teacher
        self.students: list[Student] = []

    @property
    def course_name(self) -> str:
        """Return the value of the course name.

        Returns:
            str: The value of the course name.
        """
        return self._course_name

    @course_name.setter
    def course_name(self, new_name: str) -> None:
        """Check the type a new_name.

        Args:
            new_name (str): New name for the course name.
        """
        check_type(new_name, str)
        self._course_name = new_name

    @property
    def teacher(self) -> Teacher:
        """Return the teacher object.

        Returns:
            Teacher: The teacher of the course.
        """
        return self._teacher

    @teacher.setter
    def teacher(self, new_teacher: Teacher) -> None:
        """Check the type a teacher.

        Args:
            new_teacher (Teacher): New Teacher for the course.
        """
        check_type(new_teacher, Teacher)
        self._teacher = new_teacher

    @property
    def students(self) -> list[Student]:
        """Return the list of students enrolled in the course.

        Returns:
            list: The list of Students in the course.
        """
        return self._students

    @students.setter
    def students(self, new_students: list[Student]) -> None:
        """Check the type a new_students.

        Args:
            new_students (list): New list of students.
        """
        check_type(new_students, list)
        for student in new_students:
            check_type(student, Student)
        self._students = new_students


class Course(AbstractCourse):
    """Represents a course in a school."""

    def add_student(self, student: Student) -> None:
        """Add a student to the course.

        Args:
            student (Student): The student to add.
        """
        check_type(student, Student)
        self.students.append(student)

    def remove_student(self, student: Student) -> None:
        """Remove a student from the course.

        Args:
            student (Student): The student to remove.
        """
        check_type(student, Student)
        self.students.remove(student)


class Group:
    """Represents a Group.

    Attributes:
        group_number (str): The number of the group.
        students (list): The students in the group.
    """

    def __init__(self, group_number: str) -> None:
        """Initialize a Group whis given a group name.

        Args:
            group_number (str): The number of the group.
        """
        check_type(group_number, str)
        self.group_number = group_number
        self.students: list[Student] = []

    def add_student(self, student: Student) -> None:
        """Add a student to the group.

        Args:
            student (Student): The student added in group.
        """
        check_type(student, Student)
        self.students.append(student)

    def remove_student(self, student: Student) -> None:
        """Remove student to the group.

        Args:
            student (Student): The student removed in group.
        """
        check_type(student, Student)
        self.students.remove(student)

    def take_students(self) -> list[Student]:
        """Return the list of students added in the group.

        Returns:
            list: The list of Students in the gruop.
        """
        return self.students


class EducationalInstitution:
    """Represents an educational institution.

    Attributes:
        courses (list): The courses offered in the institution.
        groups (list): The groups in the institution.
    """

    def __init__(self) -> None:
        """Initialize an EducationalInstitution object."""
        self.courses: list[Course] = []
        self.groups: list[Group] = []

    def add_course(self, course: Course) -> None:
        """Add a course to the educational institution.

        Args:
            course (Course): The course to add.
        """
        check_type(course, Course)
        self.courses.append(course)

    def remove_course(self, course: Course) -> None:
        """Remove a course from the educational institution.

        Args:
            course (Course): The course to remove.
        """
        check_type(course, Course)
        self.courses.remove(course)

    def take_courses(self) -> list[Course]:
        """Return the list of courses in educational institution.

        Returns:
            list: The list of courses in educational institution.
        """
        return self.courses

    def add_group(self, group: Group) -> None:
        """Add a group to the educational institution.

        Args:
            group (Group): The added group.
        """
        check_type(group, Group)
        self.groups.append(group)

    def remove_group(self, group: Group) -> None:
        """Remove a group from the educational institution.

        Args:
            group (Group): The removed group.
        """
        check_type(group, Group)
        self.groups.remove(group)

    def take_groups(self) -> list[Group]:
        """Return the list of groups in educational institution.

        Returns:
            list: The list of groups in educational institution.
        """
        return self.groups
