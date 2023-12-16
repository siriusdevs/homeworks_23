from typing import Self

def check(new_list_course: list, list_course: list):
    if not isinstance(new_list_course, list | tuple):
        raise TypeError (f'{new_list_course} must be list or tuple')
    for course in list_course:
       if not isinstance(course, Course):
            raise TypeError(f'{course} must be object Course')

class Person:
    def __init__(self, name: str, surname: str, age: int) -> None:
        self.name, self.surname, self.age = name, surname, age

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            raise TypeError(f'{new_name} must be str, not {type(new_name).__name__}')
        self._name = new_name

    @property
    def surname(self) -> str:
        return self._surname
    
    @surname.setter
    def surname(self, new_surname: str) -> None:
        if not isinstance(new_surname, str):
            raise TypeError(f'{new_surname} must be str, not {type(new_surname).__name__}')
        self._surname = new_surname
        
    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, new_age: int) -> None:
        if not isinstance(new_age, int):
            raise TypeError(f'{new_age} must be int, not {type(new_age).__name__}')
        self._age = new_age

class Course:
    def __init__(self, name: str, ) -> None:
        self.name = name
    
    def __eq__(self, other: Self) -> bool:
        if isinstance(other, Course):
            return self.name == other.name
        return NotImplemented

class Teacher(Person):
    def __init__(self, list_course: list[Course]) -> None:
        self.list_course = list_course

    @property
    def list_course(self) -> list[Course]:
        return self._list_course
    
    @list_course.setter
    def list_course(self, new_list_course) -> None:
        check(new_list_course, list)
        self._list_course = new_list_course

    def add_course(self, course: Course):
        if not isinstance(course, Course):
            raise TypeError(f'{course} must be object Course')
        self.list_course.append(course)

    
    

class Student(Person):
    def __init__(self, name: str, surname: str, age: int, list_course: list[Course]):
        super().__init__(name, surname, age)
        self.list_course = list_course

    @property
    def list_course(self) -> list[Course]:
        return self._list_course
    
    @list_course.setter
    def list_course(self, new_list_course: list[Course]):
        check(new_list_course, self.list_course)
        self._list_course = new_list_course

    def add_course(self, course: Course):
        if not isinstance(course, Course):
            raise TypeError(f'{course} must be object Course')
        self.list_course.append(course)

    def remove_course(self, course: Course):
        if not isinstance(course, Course):
            raise TypeError(f'{course} must be object Course')
        if not course in self.list_course:
            raise ValueError(f'{course.name} not on the list')
        self.list_course.remove(course)

a = Student("Asd", 'sdf', 32, [Course("as")])
a.remove_course(Course("as"))
