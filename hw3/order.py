"""This module includes the Order class."""
from typing import List
from dish import Dish
from hw3 import Client


class Order:
    """This class describes an order."""

    def __init__(self, client: Client, dishes: List[Dish]) -> None:
        """Initialize the Order class.

        Args:
            client (Client): An object of type Client.
            dishes (List[Dish]): A list of objects of type Dish.
        """
        self.client = client
        self.dishes = dishes

    def add_dish(self, new_dish: Dish) -> None:
        """Add a new dish to the order.

        Args:
            new_dish (Dish): An object of type Dish.

        Raises:
            TypeError: If the type of new_dish is not Dish.
        """
        if not isinstance(new_dish, Dish):
            raise TypeError(f'{new_dish} must be an object of type Dish')
        self.dishes.append(new_dish)

    def remove_dish(self, removed_dish: Dish) -> None:
        """Remove a dish from the order.

        Args:
            removed_dish (Dish): The dish to be removed.
        """
        if removed_dish in self.dishes:
            self.dishes.remove(removed_dish)

    def get_dish_names(self) -> str:
        """Get dish names as a string.

        Returns:
            str: Dish names as a string.
        """
        return ', '.join(dish.name for dish in self.dishes)

    def __eq__(self, other: 'Order') -> bool:
        """Check equality between two Order objects.

        Args:
            other (Order): Another object of type Order.

        Returns:
            bool: True if the two objects are considered equal, False otherwise.
        """
        if isinstance(other, Order):
            return self.client == other.client and self.dishes == other.dishes
        return NotImplemented
