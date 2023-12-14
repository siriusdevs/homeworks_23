import courses_owner.courses_owner as course_owner


class Student(course_owner.CoursesOwner):
    def __init__(self, name: str, surname: str, age: int) -> None:
        super().__init__(name, surname, age)
