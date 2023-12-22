"""Module that keeps records of students and courses at an educational institution."""

import random


class Person:
    """A person who has a name, surname and age."""

    def __init__(self, name: str, surname: str, age: int) -> None:
        """Name, surname and age of person.

        Args:
            name (str): name of person
            surname (str): surname of person
            age (int): age of person
        """
        self.name, self.surname, self.age = name, surname, age

    @property
    def name(self) -> str:
        """Name of person.

        Returns:
            str: Name of person.
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Set new_name.

        Args:
            new_name (str): new name person

        Raises:
            TypeError: if type of new_name not str.
        """
        if not isinstance(new_name, str):
            raise TypeError(f'{new_name} is be str')
        self._name = new_name

    @property
    def surname(self) -> str:
        """Surname of person.

        Returns:
            str: Surname of person.
        """
        return self._surname

    @surname.setter
    def surname(self, new_surname: str) -> None:
        """Set new_surname.

        Args:
            new_surname (str): new surname person

        Raises:
            TypeError: if type of new_surname not str.
        """
        if not isinstance(new_surname, str):
            raise TypeError(f'{new_surname} should be str')
        self._surname = new_surname

    @property
    def age(self) -> int:
        """Age of person.

        Returns:
            int: Age of person.
        """
        return self._age

    @age.setter
    def age(self, new_age: int) -> None:
        """Set new age.

        Args:
            new_age (int): new age person

        Raises:
            TypeError: if type of new_age not int.
        """
        if not isinstance(new_age, int):
            raise TypeError(f'{new_age} must be int')
        self._age = new_age


class Student(Person):
    """Student that is inherited from a Person."""

    def __init__(self, name: str, surname: str, age: int, group: str, scholarship: int):
        """Name, surname, age, group and scholarship of student.

        Args:
            name (str): name of person
            surname (str): surname of person
            age (int): age of person
            group (str): group of student
            scholarship (int): scholarship of student
        """
        super().__init__(name, surname, age)
        self.group, self.scholarship = group, scholarship

    @property
    def group(self) -> str:
        """Group of student.

        Returns:
            str: Group of student.
        """
        return self._group

    @group.setter
    def group(self, new_group: str) -> None:
        """Set new group.

        Args:
            new_group (str): new group student

        Raises:
            TypeError: if type of new_group not str.
        """
        if not isinstance(new_group, str):
            raise TypeError(f'{new_group} is be str')
        self._group = new_group

    @property
    def scholarship(self) -> int:
        """Scholarship of student.

        Returns:
            int: Scholarship of student.
        """
        return self._scholarship

    @scholarship.setter
    def scholarship(self, new_scholarship: int) -> None:
        """Set new scholarship.

        Args:
            new_scholarship (int): new scholarship student

        Raises:
            TypeError: if Faculty of teacher.
        """
        if not isinstance(new_scholarship, int):
            raise TypeError(f'{new_scholarship} should be int')
        self._scholarship = new_scholarship


class Teacher(Person):
    """Teacher that is inherited from a Person."""

    def __init__(self, name: str, surname: str, age: int, faculty: str, salary: int) -> None:
        """Name, surname, age, faculty and salary of student.

        Args:
            name (str): name of person
            surname (str): surname of person
            age (int): age of person
            faculty (str): faculty of teacher
            salary (int): saalry of teacher
        """
        super().__init__(name, surname, age)
        self.faculty, self.salary = faculty, salary

    @property
    def faculty(self) -> str:
        """Faculty of teacher.

        Returns:
            str: Faculty of teacher.
        """
        return self._faculty

    @faculty.setter
    def faculty(self, new_faculty: str) -> None:
        """Set new faculty.

        Args:
            new_faculty (str): new faculty of teacher

        Raises:
            TypeError: if type of new_faculty not str.
        """
        if not isinstance(new_faculty, str):
            raise TypeError(f'{new_faculty} must be str')
        self._faculty = new_faculty

    @property
    def salary(self) -> int:
        """Salary of teacher.

        Returns:
            int: Salary of teacher.
        """
        return self._salary

    @salary.setter
    def salary(self, new_salary: int) -> None:
        """Set new salary.

        Args:
            new_salary (int): new salary of teacher

        Raises:
            TypeError: if type of new_salary not int.
        """
        if not isinstance(new_salary, int):
            raise TypeError(f'{new_salary} must be int')
        self._salary = new_salary


class Course:
    """Course that has title, list_students, list_teachers."""

    def __init__(
        self,
        title: str,
        list_students: list[Student] | tuple[Student],
        list_teachers: list[Teacher] | tuple[Teacher],
    ) -> None:
        """Title, list_students, list_teachers of course.

        Args:
            title (str): title of course
            list_students (list[Student] | tuple[Student]): list_students of course
            list_teachers (list[Teacher] | tuple[Teacher]): list_teachers of course
        """
        self.title, self.list_students, self.list_teachers = title, list_students, list_teachers

    @property
    def title(self) -> str:
        """Title of course.

        Returns:
            str: Title of course.
        """
        return self._title

    @title.setter
    def title(self, new_title: str) -> None:
        """Set a new title.

        Args:
            new_title (str): new title of course.

        Raises:
            TypeError: if type of new_title not str.
        """
        if not isinstance(new_title, str):
            raise TypeError(f'{new_title} must be str')
        self._title = new_title

    @property
    def list_students(self) -> list[Student]:
        """List students of course.

        Returns:
            list[Student]: list students of course.
        """
        return self._list_students

    @list_students.setter
    def list_students(self, new_list_students: list[Student] | tuple[Student]) -> None:
        """Set new list students.

        Args:
            new_list_students (list[Student] | tuple[Student]): new list students of course

        Raises:
            TypeError: if type of new_list_students not list | tuple.
            TypeError: if student is not object of class Student.
        """
        if not isinstance(new_list_students, list | tuple):
            raise TypeError(f'{new_list_students} must be list or tuple')
        for student in new_list_students:
            if not isinstance(student, Student):
                raise TypeError(f'{student} must be object of class Student')
        self._list_students = new_list_students

    @property
    def list_teachers(self) -> list[Teacher]:
        """List teachers of course.

        Returns:
            list[Teacher]: list teachers of course.
        """
        return self._list_teachers

    @list_teachers.setter
    def list_teachers(self, new_list_teacher: list[Teacher] | tuple[Teacher]) -> None:
        """Set new list teachers.

        Args:
            new_list_teacher (list[Teacher] | tuple[Teacher]): new_list_teachers of course.

        Raises:
            TypeError: if type of new_list_teachers not list | tuple.
            TypeError: if teachers is not object of class Teacher.
        """
        if not isinstance(new_list_teacher, list | tuple):
            raise TypeError(f'{new_list_teacher} must be list or tuple')
        for teacher in new_list_teacher:
            if not isinstance(teacher, Teacher):
                raise TypeError(f'{teacher} must be object of class Teacher')
        self._list_teachers = new_list_teacher

    def conduct_a_class(self):
        """Generate a random teacher and students to conduct classes.

        Raises:
            ValueError: if self_list_teachers is empty.
            ValueError: if self_list_students is empty.
        """
        people_of_course = []
        if not self.list_teachers:
            raise ValueError('The list of teachers is empty')
        if not self.list_students:
            raise ValueError('The list of students is empty')
        random_teacher = random.choice(self.list_teachers)
        people_of_course.append(f'Teacher: {random_teacher.name} {random_teacher.surname}')
        num_students_to_attend = random.randint(1, len(self.list_students))
        random_students = random.sample(self.list_students, num_students_to_attend)
        people_of_course.append('Students attending the class:')
        for student in random_students:
            people_of_course.append(f'{student.name} {student.surname}')
