"""Module include tests on Client and Dish classes."""
import pytest

from client import Client
from dish import Dish
from test_data import names_of_clients, names_price_of_dish


@pytest.mark.parametrize('name', names_of_clients)
def test_clients_ptrs(name: str) -> None:
    """Test for checking parameters.

    Args:
        name (str): name of client
    """
    assert Client(name).name == name


@pytest.mark.xfail(raises=TypeError)
def test_client_invalid():
    """Function check setter work."""
    with pytest.raises(TypeError):
        Client(9)


@pytest.mark.parametrize('name_dish, price', names_price_of_dish)
def test_dish_ptrs(name_dish: str, price: int | float) -> None:
    """Test for checking parameters.

    Args:
        name_dish (str): name of dish
        price (int | float): price of dish
    """
    dish = Dish(name_dish, price)
    assert dish.name_dish == name_dish and dish.price == price


@pytest.mark.xfail(raises=TypeError)
def test_dish_invalid():
    """Function check setter work."""
    with pytest.raises(TypeError):
        Dish(2, 3)
    with pytest.raises(TypeError):
        Dish('Waffels', '350')
