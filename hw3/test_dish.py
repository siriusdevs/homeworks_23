"""Module includes tests for the Dish class."""
import pytest

from dish import Dish

names_price_of_dish = (('Apple', 30), ('Milk', 10))


@pytest.mark.parametrize('name, price', names_price_of_dish)
def test_dish_properties(name: str, price: int | float) -> None:
    """Check parameters.

    Args:
        name (str): Name of the dish.
        price (int | float): Price of the dish.
    """
    dish = Dish(name, price)
    assert dish.name == name and dish.price == price
