"""This module includes the definition of the Dish class."""

from typing import Self


class Dish:
    """A class representing a Dish entity."""

    def __init__(self, dish_name: str, dish_price: int | float) -> None:
        """Initialize the Dish class.

        Args:
            dish_name (str): The name of the dish.
            dish_price (int | float): The price of the dish.
        """
        self.name, self.price = dish_name, dish_price

    @property
    def name(self) -> str:
        """Retrieve the name of the dish.

        Returns:
            str: The name of the dish.
        """
        return self._name

    @name.setter
    def name(self, new_dish_name: str) -> None:
        """Set the name of the dish.

        Args:
            new_dish_name (str): The new name for the dish.

        Raises:
            TypeError: If the type of new_dish_name is not str.
        """
        if not isinstance(new_dish_name, str):
            raise TypeError(f'{new_dish_name} must be str')
        self._name = new_dish_name

    @property
    def price(self) -> int | float:
        """Retrieve the price of the dish.

        Returns:
            int | float: The price of the dish.
        """
        return self._price

    @price.setter
    def price(self, new_dish_price: int | float) -> None:
        """Set the price of the dish.

        Args:
            new_dish_price (int | float): The new price for the dish.

        Raises:
            TypeError: If the type of new_dish_price is not int or float.
        """
        if not isinstance(new_dish_price, int | float):
            raise TypeError(f'{new_dish_price} must be a number')
        self._price = new_dish_price

    def __repr__(self) -> str:
        """Get a string representation of the Dish object for debugging.

        Returns:
            str: A string representation of the Dish object.
        """
        return f'{self.name}: {self.price}'

    def __eq__(self, other: Self) -> bool:
        """Check whether two Dish objects are equal.

        Args:
            other (Self): Another object of type Dish.

        Returns:
            bool: True if the two objects are considered equal, False otherwise.
        """
        if isinstance(other, Dish):
            return self.name == other.name and self.price == other.price
        return NotImplemented
