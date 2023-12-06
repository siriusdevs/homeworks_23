"""Module for testing class Ordering."""
import pytest

from client import Client
from dish import Dish
from order import Order
from test_data import add_remove_dishes, clients, order, test_getdishnames_data


@pytest.mark.parametrize('clients_name, dishes', clients)
def test_order_ptrs(clients_name: list[Client], dishes: list[Dish]) -> None:
    """Test for checking parameters.

    Args:
        clients_name (list[Client]): list of object type Client
        dishes (list[Dish]): list of object type Dish
    """
    order_check = Order(clients_name, dishes)
    assert order_check.clients == clients_name and order_check.dishes == dishes


@pytest.mark.parametrize('dish', add_remove_dishes)
def test_add_remove(dish: Dish) -> None:
    """Function which test add_dish and remove_dish.

    Args:
        dish (Dish): dish object type Dish
    """
    order.add_dish(dish)
    assert order.dishes[-1] == dish
    order.remove_dishes(dish)
    assert dish not in order.dishes


@pytest.mark.parametrize('orders, expected', test_getdishnames_data)
def test_get_dishname(orders: Order, expected: str) -> None:
    """Function which checking work get_dishname.

    Args:
        orders (Order): object type Order
        expected (str): expected result
    """
    assert orders.get_dishname() == expected
