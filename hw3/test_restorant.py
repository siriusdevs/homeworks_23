"""This module include tests for class Restorant."""
import pytest

from order import Client, Dish, Order
from restorant import Restorant
from test_data import test_data


@pytest.mark.parametrize('orders, dishes, av_dishes', test_data)
def test_restorant(orders: list[Order], dishes: list[Dish], av_dishes: list[Dish]):
    """Test restorant class.

    Args:
        orders (list[Order]): list object type Order
        dishes (list[Dish]): list object type Dish
        av_dishes (list[Dish]): list avaibe object type Dish
    """
    restorant = Restorant(orders, dishes, av_dishes)
    assert restorant.orders == orders and restorant.dishes == dishes
    assert restorant.av_dishes == av_dishes
    order = Order([Client('Nina')], [Dish('Water', 5)])
    restorant.make_order(order)
    assert restorant.orders[-1] == order
    restorant.remove_order(order)
    assert order not in restorant.orders
    assert restorant.get_order() == '[Waffles: 5] [Albert]'


@pytest.mark.xfail(raises=(TypeError, ValueError))
def test_restorant_invalid():
    """Test function make_order."""
    restorant = Restorant(
        [Order([Client('Artem')], [Dish('Rice', 5)])],
        [Dish('Rice', 5), Dish('Cheeze', 100)],
        [Dish('Rice', 5)],
    )
    with pytest.raises(TypeError):
        restorant.make_order(1)

    with pytest.raises(ValueError):
        restorant.make_order(Order([Client('Anton')], [Dish('Eggs', 2)]))
