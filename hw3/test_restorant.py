"""This module include tests for class Restorant."""
import pytest

from order import Client, Dish, Order
from restaurant import Restaurant

order = Order(Client('Albert'), [Dish('Waffles', 5)])
restaurant_data = ((
    [order],
    [Dish('Rice', 5), Dish('Cheeze', 10), Dish('Butter', 5)],
    [Dish('Rice', 5), Dish('Butter', 5)],
),
)
restaurant = Restaurant(
    [order],
    [Dish('Croissant', 5), Dish('Cheeze', 10), Dish('Noodles', 5)],
    [Dish('Croissant', 5), Dish('Noodles', 5)],
)


@pytest.mark.parametrize('orders, dishes, av_dishes', restaurant_data)
def test_restorant(orders: list[Order], dishes: list[Dish], av_dishes: list[Dish]):
    """Test restorant class.

    Args:
        orders (list[Order]): list object type Order
        dishes (list[Dish]): list object type Dish
        av_dishes (list[Dish]): list avaibe object type Dish
    """
    restor = Restaurant(orders, dishes, av_dishes)

    assert restor.orders == orders and restor.dishes == dishes
    assert restor.av_dishes == av_dishes

    order_toadd = Order([Client('Nina')], [Dish('Butter', 5)])

    restor.make_order(order_toadd)

    assert restor.orders[-1] == order_toadd

    restor.remove_order(order_toadd)

    assert order_toadd not in restor.orders
    assert restor.get_order() == '[Waffles: 5] Albert'


@pytest.mark.xfail(raises=(TypeError, ValueError))
def test_restorant_invalid():
    """Test function make_order."""
    with pytest.raises(TypeError):
        restaurant.make_order(1)

    with pytest.raises(ValueError):
        restaurant.make_order(Order([Client('Anton')], [Dish('Eggs', 2)]))
