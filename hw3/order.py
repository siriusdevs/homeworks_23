"""This module include class Order."""
from typing import Self

from client import Client
from dish import Dish


class Order:
    """This class discribe order."""

    def __init__(self, clients: list[Client], dishes: list[Dish]) -> None:
        """Init the class Order.

        Args:
            clients (list[Client]): list of object type Client
            dishes (list[Dish]): list of object type Dish
        """
        self.clients, self.dishes = clients, dishes

    def add_dish(self, new_dish: Dish) -> None:
        """Add dishes new dish.

        Args:
            new_dish (Dish): dish object type Dish

        Raises:
            TypeError: if type of new_dish not Dish
        """
        if not isinstance(new_dish, Dish):
            raise TypeError(f'{new_dish} must be object Dish')
        self.dishes.append(new_dish)

    def remove_dishes(self, remove_dish: Dish) -> None:
        """Remove dish from dishes.

        Args:
            remove_dish (Dish): dish which we should remove
        """
        if remove_dish in self.dishes:
            self.dishes.remove(remove_dish)

    def get_name_dish(self) -> str:
        """Get dishname as str.

        Returns:
            Dishname as str
        """
        return ', '.join(dish.name for dish in self.dishes)

    def __eq__(self, __value: Self) -> bool:
        """Check equality two object type Order.

        Args:
            __value (Self): object type Order

        Returns:
            bool: equal two object
        """
        if isinstance(__value, Order):
            return self.clients == __value.clients and self.dishes == __value.dishes
        return NotImplemented
