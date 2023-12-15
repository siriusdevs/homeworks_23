"""This module include class Dish."""
from typing import Self


class Dish:
    """This class describe dish."""

    def __init__(self, name_dish: str, price: int | float) -> None:
        """Init the class Dish.

        Args:
            name_dish (str): name of dish
            price (int | float): price of dish
        """
        self.name_dish, self.price = name_dish, price

    @property
    def name_dish(self) -> str:
        """Get name_dish.

        Returns:
            str: name_dish
        """
        return self._name_dish

    @name_dish.setter
    def name_dish(self, new_dish: str) -> None:
        """Set name_dish.

        Args:
            new_dish (str): new name dish

        Raises:
            TypeError: if type of new_dish not str
        """
        if not isinstance(new_dish, str):
            raise TypeError(f'{new_dish} must be str')
        self._name_dish = new_dish

    @property
    def price(self) -> int | float:
        """Get price.

        Returns:
            Price of dish
        """
        return self._price

    @price.setter
    def price(self, new_price: int | float) -> None:
        """Set price.

        Args:
            new_price (int | float): new price of dish

        Raises:
            TypeError: if type of new_price not int or float
        """
        if not isinstance(new_price, int | float):
            raise TypeError(f'{new_price} must be a number')
        self._price = new_price

    def __repr__(self) -> str:
        """Str represent of the object for debug.

        Returns:
            str:  A string representation of the object.
        """
        return f'{self.name_dish}: {self.price}'

    def __eq__(self, __value: Self) -> bool:
        """Check equality two object type Dish.

        Args:
            __value (Self): object type Dish

        Returns:
            bool: equal two object
        """
        if isinstance(__value, Dish):
            return self.name_dish == __value.name_dish and self.price == __value.price
        return NotImplemented
