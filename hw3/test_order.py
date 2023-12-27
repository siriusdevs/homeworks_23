"""Module for testing class Ordering."""
import pytest

from dish import Dish
from hw3 import Client
from order import Order

clients = [Client('Alla'), [Dish('Apple', 5)]]
add_remove_dishes = [Dish('Argun', 4), Dish('Milk', 2), Dish('banan', 9)]
order = Order(Client('Alla'), [Dish('Milk', 5)])
test_getdishnames_data = [
    (Order(Client('Anna'), [Dish('Waffles', 5), Dish('Ice Cream', 2)]), 'Waffles, Ice Cream'),
    (Order(Client('Artem'), [Dish('Toast', 5), Dish('Ice Cream', 2)]), 'Toast, Ice Cream'),
]


@pytest.mark.parametrize('clients_name, dishes', [clients])
def test_order_ptrs(clients_name: Client, dishes: list[Dish]) -> None:
    """Test for checking parameters.

    Args:
        clients_name (Client): object type Client
        dishes (list[Dish]): list of object type Dish
    """
    order_check = Order(clients_name, dishes)
    assert order_check.client == clients_name and order_check.dishes == dishes


@pytest.mark.parametrize('dish', add_remove_dishes)
def test_add_remove(dish: Dish) -> None:
    """Function which test add_dish and remove_dish.

    Args:
        dish (Dish): dish object type Dish
    """
    order.add_dish(dish)
    assert order.dishes[-1] == dish

    order.remove_dish(dish)
    assert dish not in order.dishes


@pytest.mark.parametrize('orders, expected', test_getdishnames_data)
def test_get_dishname(orders: Order, expected: str) -> None:
    """Function which checking work get_dishname.

    Args:
        orders (Order): object type Order
        expected (str): expected result
    """
    assert orders.get_dish_names() == expected
