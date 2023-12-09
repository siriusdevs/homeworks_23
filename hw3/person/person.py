class Person:
    def __init__(self, name: str, surname: str, age: int) -> None:
        self.name = name
        self.surname = surname
        self.age = age

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            raise TypeError('The new name has to be a string value!')

        if not len(new_name):
            raise ValueError('The new name does not have to be a empty string!')

        self.__name = new_name

    @property
    def surname(self) -> str:
        return self.__surname

    @surname.setter
    def surname(self, new_surname: str) -> None:
        if not isinstance(new_surname, str):
            raise TypeError('The new surname has to be a string value!')

        if not len(new_surname):
            raise ValueError('The new surname does not have to be a empty string!')

        self.__surname = new_surname

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, new_age) -> None:
        if not isinstance(new_age, int):
            raise TypeError('The new age has to be a integer value!')

        if not (0 <= new_age <= 120):
            raise ValueError('The new age has to be from 0 to 120!')

        self.__age = new_age

    def __str__(self) -> str:
        return f'Person: {self.surname} {self.name}'

    def __repr__(self) -> str:
        return f'Person: {self.surname} {self.name}'
