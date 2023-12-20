"""Architecture course management."""


class Teacher:
    """Represents a teacher in a school.

    Attributes:
        name (str): The name of the teacher.
    """

    def __init__(self, name):
        """Initialize a Student object with the given student name.

        Args:
            name (str): The name of the Teacher.
        """
        self.name = name

    def create_course(self, course_name):
        """Create the course as the teacher.

        Args:
            course_name (str): The name of course.

        Returns:
            Course: The created course.
        """
        return Course(course_name, self)

    def assign_student(self, course, student):
        """Assign the student as the teacher.

        Args:
            course (Course): The assigned course.
            student (Student): Thr assigned student.
        """
        course.add_student(student)


class Student:
    """Represents a student in a school.

    Attributes:
        name (str): The name of the student.
    """

    def __init__(self, name):
        """Initialize a Student object with the given student name.

        Args:
            name (str): The name of student
        """
        self.name = name

    def enroll(self, course):
        """Enrolls the student in a specific course.

        Args:
            course (Course): The course to enroll in.
        """
        course.add_student(self)

    def drop_course(self, course):
        """Remove the course from the student.

        Args:
            course (Course): The course to remove in.
        """
        course.remove_student(self)


class Course:
    """
    Represents a course in a school.

    Attributes:
        course_name (str): The name of the course.
        teacher (Teacher): The teacher of the course.
        students (list): The students enrolled in the course.
    """

    def __init__(self, course_name, teacher):
        """Initialize a Course object with the given course name.

        Args:
            course_name (str): The name of the course.
            teacher (str): The name of the teacher.
        """
        self.course_name = course_name
        self.teacher = teacher
        self.students = []

    @property
    def course_name(self):
        """Return the value of the course name.

        Returns:
            str: The value of the course name.
        """
        return self._course_name

    @property
    def teacher(self):
        """Return the teacher object.

        Returns:
            _type_: _description_
        """
        return self._teacher

    @property
    def students(self):
        """Return the list of students enrolled in the course.

        Returns:
            list: The list of Students in the course.
        """
        return self._students

    @course_name.setter
    def course_name(self, new_name):
        """Check the type a new_name.

        Args:
            new_name (str): New name for the course name.

        Raises:
            TypeError: The new_name must be str.
        """
        if not isinstance(new_name, str):
            raise TypeError(f'{new_name:} must be str')
        self._course_name = new_name

    @teacher.setter
    def teacher(self, new_teacher):
        """Check the type a teacher.

        Args:
            new_teacher (Teacher): New Teacher for the course.

        Raises:
            TypeError: The teacher must be Teacher.
        """
        if not isinstance(new_teacher, Teacher):
            raise TypeError(f'{new_teacher} must be Teacher')
        self._teacher = new_teacher

    @students.setter
    def students(self, new_students):
        if not isinstance(new_students, list):
            raise TypeError(f'{new_students=} must be list')
        for student in new_students:
            if not isinstance(student, Student):
                raise TypeError(f'{student:} must be Student')
        self._students = new_students

    def add_student(self, student):
        """Add a student to the course.

        Args:
            student (Student): The student to add.

        Raises:
            TypeError: The student must be Student.
        """
        if not isinstance(student, Student):
            raise TypeError(f'{student:} must be Student')
        self.students.append(student)

    def remove_student(self, student):
        """Remove a student from the course.

        Args:
            student (Student): The student to remove.
        """
        self.students.remove(student)


class Group:
    """Represents a Group.

    Attributes:
        group_number (int): The number of the group.
        students (list): The students in the group.
    """

    def __init__(self, group_number):
        """Initialize a Group whis given a group name.

        Args:
            group_number (str): The name of the group.
        """
        self.group_number = group_number
        self.students = []

    def add_student(self, student):
        """Add a student to the group.

        Args:
            student (Student): The student added in group.
        """
        self.students.append(student)

    def remove_student(self, student):
        """Remove student to the group.

        Args:
            student (Student): The student removed in group.
        """
        self.students.remove(student)

    def take_students(self):
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

    def __init__(self):
        """Initialize an EducationalInstitution object."""
        self.courses = []
        self.groups = []

    def add_course(self, course):
        """Add a course to the educational institution.

        Args:
            course (Course): The course to add.
        """
        self.courses.append(course)

    def remove_course(self, course):
        """Remove a course from the educational institution.

        Args:
            course (Course): The course to remove.
        """
        self.courses.remove(course)

    def take_courses(self):
        """Return the list of courses in educational institution.

        Returns:
            list: The list of courses.
        """
        return self.courses

    def add_group(self, group):
        """Add a group to the educational institution.

        Args:
            group (Group): The added group.
        """
        self.groups.append(group)

    def remove_group(self, group):
        """Remove a group from the educational institution.

        Args:
            group (Group): The removed group.
        """
        self.groups.remove(group)

    def take_groups(self):
        """Return the list of groups in educational institution.

        Returns:
            list: The list of groups in educational institution.
        """
        return self.groups
