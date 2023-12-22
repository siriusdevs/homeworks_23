"""Module for HW3."""

from typing import Any, Callable


def _check_type(attr_value: Any, attr_name: str, expected_type: Any) -> None:
    if not isinstance(attr_value, expected_type):
        got_type = type(attr_value).__name__
        raise TypeError(f'{attr_name} expected to be {expected_type}, not {got_type}')


def _checker(attr: str, check: Callable, expected_type: Any) -> Callable:
    def add_property(cls: type) -> type:
        def getter(self):
            return getattr(self, f'_{attr}')

        def setter(self, new_value: Any) -> None:
            check(new_value, attr, expected_type)
            setattr(self, f'_{attr}', new_value)

        setattr(cls, attr, property(getter, setter))
        return cls
    return add_property


@_checker('name', _check_type, str)
class Teacher:
    """This is Teacher instance."""

    def __init__(self, name: str) -> None:
        """Create teacher.

        Args:
            name (str): teacher's name
        """
        self.name = name

    def create_new_course(self, title: str) -> Any:
        """Create new course, with teachers in author.

        Args:
            title (str): title of new course

        Returns:
            Any: new course object
        """
        return Course(title, self, [])

    def assign_student_to_course(self, course: Any, new_student: Any):
        """Enroll student to choosen course.

        Args:
            course (Any): course to add
            new_student (Any): student to add
        """
        _check_type(course, 'course', Course)
        _check_type(new_student, 'new_student', Student)
        course.students.append(new_student)

    def __str__(self) -> str:
        """Show student name.

        Returns:
            str: student name.
        """
        return f'{self.name}'


@_checker('name', _check_type, str)
class Student:
    """This is Student instance."""

    def __init__(self, name: str) -> None:
        """Create student.

        Args:
            name (str): student name
        """
        self.name = name

    def subscribe_course(self, course: Any):
        """Add student to choosen course.

        Args:
            course (Any): course to add
        """
        _check_type(course, 'course', Course)
        course.students.append(self)

    def unsubscribe_course(self, course: Any):
        """Remove student from course.

        Args:
            course (Any): course from which to remove

        Raises:
            ValueError: if student not subcriber
        """
        _check_type(course, 'course', Course)
        if self not in course.students:
            raise ValueError(f'{self} is not subscribe in this Course')
        while self in self.students:
            self.students.remove(self)

    def __str__(self) -> str:
        """Show student name.

        Returns:
            str: student name.
        """
        return f'{self.name}'

    def __repr__(self) -> str:
        """Show student name.

        Returns:
            str: student name.
        """
        return f'{self.name}'


@_checker('title', _check_type, str)
@_checker('teacher', _check_type, Teacher)
class Course:
    """This is Course instance."""

    def __init__(
        self,
        title: str,
        teacher: Teacher,
        students: list[Student],
    ) -> None:
        """Create course.

        Args:
            title (str): title of course
            teacher (Teacher): teacher of the course
            students (list[Student]): students subscribed to course
        """
        self.title = title
        self.teacher = teacher
        self.students = students

    @property
    def students(self) -> list[Student]:
        """Return list of students.

        Returns:
            list[Student]: all students on course.
        """
        return self._students

    @students.setter
    def students(self, new_students: list[Student]) -> None:
        _check_type(new_students, 'new_students', list)
        for new_student in new_students:
            _check_type(new_student, 'new_student', Student)
        self._students = new_students

    def __str__(self) -> str:
        """Show info about course.

        Returns:
            str: course info.
        """
        return f'{self.title} {self.teacher} {self.students}'

    def __repr__(self) -> str:
        """Show info about course.

        Returns:
            str: course info.
        """
        return f'{self.title} {self.teacher} {self.students}'


@_checker('number', _check_type, str)
class Group:
    """This is Group instance."""

    def __init__(
        self,
        number: str,
        students: list[Student],
    ) -> None:
        """Create Group.

        Args:
            number (str): number of group
            students (list[Student]): all students of group
        """
        self.number = number
        self.students = students

    def add_student(self, new_student: Student) -> None:
        """Add student to group.

        Args:
            new_student (Student): student to add
        """
        _check_type(new_student, 'new_student', Student)
        self.students.append(new_student)

    def remove_student(self, old_student: Student) -> None:
        """Remove student from group.

        Args:
            old_student (Student): student to remove

        Raises:
            ValueError: if student not exists
        """
        _check_type(old_student, 'old_student', Student)
        if old_student not in self.students:
            raise ValueError(f'{old_student} is not present in this Group')
        while old_student in self.students:
            self.students.remove(old_student)

    def get_all_students(self) -> list[Student]:
        """Return all students in group.

        Returns:
            list[Student]: all students
        """
        return self.students

    def __str__(self) -> str:
        """Show info about group.

        Returns:
            str: group info.
        """
        return f'{self.number} {self.students}'

    def __repr__(self) -> str:
        """Show info about group.

        Returns:
            str: group info.
        """
        return f'{self.number} {self.students}'


class EducationalInstitution:
    """This is Educational Institution instance."""

    def __init__(
        self,
        courses: list[Course],
        groups: list[Group],
    ) -> None:
        """Create Educational Institution.

        Args:
            courses (list[Course]): all courses in Educational Institution.
            groups (list[Group]): all groups in Educational Institution.
        """
        self.courses = courses
        self.groups = groups

    def add_course(self, new_course: Course) -> None:
        """Add course to Educational Institution.

        Args:
            new_course (Course): course to add
        """
        _check_type(new_course, 'new_course', Course)
        self.courses.append(new_course)

    def remove_course(self, old_course: Course) -> None:
        """Remove course from Educational Institution.

        Args:
            old_course (Course): course to remove

        Raises:
            ValueError: if course not presented.
        """
        _check_type(old_course, 'old_course', Course)
        if old_course not in self.courses:
            raise ValueError(f'{old_course} is not present in this EducationalInstitution')
        while old_course in self.courses:
            self.courses.remove(old_course)

    def get_all_courses(self) -> list[Course]:
        """Return all courses from Educational Institution.

        Returns:
            list[Course]: all courses
        """
        return self.courses

    def add_group(self, new_group: Group) -> None:
        """Add group to EducationalInstitution list.

        Args:
            new_group (Group): group to add
        """
        _check_type(new_group, 'new_group', Group)
        self.groups.append(new_group)

    def remove_group(self, old_group: Group) -> None:
        """Remove group from Educational Institution.

        Args:
            old_group (Group): group to remove

        Raises:
            ValueError: if group not exist.
        """
        _check_type(old_group, 'old_group', Group)
        if old_group not in self.groups:
            raise ValueError(f'{old_group} is not present in this EducationalInstitution')
        while old_group in self.groups:
            self.groups.remove(old_group)

    def get_all_groups(self) -> list[Group]:
        """Return all groups from EducationalInstitution.

        Returns:
            list[Group]: all groups
        """
        return self.groups
