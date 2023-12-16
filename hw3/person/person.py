"""Module with Person."""
from typing import Any


class Person:
    """Person who has name, surname, age.

    Arguments:
        name(str): Person's name.
        surname(str): Person's surname.
        age(int): Person's age.
    """

    __min_age = 0
    __max_age = 120

    def __init__(self, name: str, surname: str, age: int, **kwargs: Any) -> None:
        """Init person's instance.

        Args:
            name(str): Person's name.
            surname(str): Person's surname.
            age(int): Person's age.
            kwargs(Any): arguments for any classes in the inheritance chain.
        """
        self.name = name
        self.surname = surname
        self.age = age
        super().__init__(**kwargs)

    @property
    def name(self) -> str:
        """Get person's name.

        Returns:
            str: Person's name.
        """
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        """Set new peron's name.

        Args:
            new_name(str): New person's name.

        Raises:
            TypeError: The given name is not a string value.
            ValueError: The given name is empty.
        """
        if not isinstance(new_name, str):
            raise TypeError('The new name has to be a string value!')

        if not len(new_name):
            raise ValueError('The new name does not have to be a empty string!')

        self.__name = new_name

    @property
    def surname(self) -> str:
        """Get person's surname.

        Returns:
            str: Person's surname.
        """
        return self.__surname

    @surname.setter
    def surname(self, new_surname: str) -> None:
        """Set new peron's surname.

        Args:
            new_surname(str): New person's surname.

        Raises:
            TypeError: The given surname is not a string value.
            ValueError: The given surname is empty.
        """
        if not isinstance(new_surname, str):
            raise TypeError('The new surname has to be a string value!')

        if not len(new_surname):
            raise ValueError('The new surname does not have to be a empty string!')

        self.__surname = new_surname

    @property
    def age(self) -> int:
        """Get person's age.

        Returns:
            int: Person's age.
        """
        return self.__age

    @age.setter
    def age(self, new_age) -> None:
        """Set new peron's age.

        Args:
            new_age(str): New person's age.

        Raises:
            TypeError: The given age is not a int value.
            ValueError: The given age is empty.
        """
        if not isinstance(new_age, int):
            raise TypeError('The new age has to be a integer value!')

        is_right_age = self.__min_age <= new_age <= self.__max_age

        if not is_right_age:
            raise ValueError('The new age has to be from 0 to 120!')

        self.__age = new_age

    def __str__(self) -> str:
        """Get the person as a string.

        Returns:
            str: The person as a string.
        """
        return f'Person: {self.surname} {self.name}'

    def __repr__(self) -> str:
        """Get the person as a string in command line.

        Returns:
            str: The person as a string.
        """
        return f'Person: {self.surname} {self.name}'
