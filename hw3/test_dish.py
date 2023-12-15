"""Module include tests on Client and Dish classes."""
import pytest

from dish import Dish

names_price_of_dish = (('Eggs', 350), ('Ice cream', 120))


@pytest.mark.parametrize('name_dish, price', names_price_of_dish)
def test_dish_ptrs(name_dish: str, price: int | float) -> None:
    """Check parameters.

    Args:
        name_dish (str): name of dish
        price (int | float): price of dish
    """
    dish = Dish(name_dish, price)
    assert dish.name_dish == name_dish and dish.price == price


@pytest.mark.xfail(raises=TypeError)
def test_dish_invalid():
    """Check setter work."""
    with pytest.raises(TypeError):
        Dish(2, 3)
    with pytest.raises(TypeError):
        Dish('Waffels', '350')
