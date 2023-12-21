"""Testing class Restaraunt from module hw3.py."""
import pytest

from hw3 import Client, Dish, Order, Restaurant


def test_restaurant_management():
    """
    Test case for restaurant management.

    Tests the creation of a Restaurant object and management of dishes and orders.
    Asserts attribute assignment errors and value errors.
    Also tests creating and removing orders from the restaurant.
    """
    price1, price2, fake_price = 12, 18, 30
    dish1 = Dish('Burger', price1)
    dish2 = Dish('Chicken', price2)
    fake_dish = Dish('Bread', fake_price)

    client1 = Client('Alice')
    client2 = Client('Bob')
    fake_client = Client('Steve')

    order1 = Order(client1, [dish1])
    order2 = Order(client2, [dish2])
    fake_order = Order(fake_client, [fake_dish])

    available_dishes = [dish1, dish2]
    all_dishes = [dish1, dish2]

    restaurant = Restaurant(all_dishes, available_dishes, [order1, order2])

    with pytest.raises(TypeError):
        restaurant.all_dishes = 5.5

    with pytest.raises(ValueError):
        restaurant.all_dishes = [dish1, dish2, 'cake']

    with pytest.raises(TypeError):
        restaurant.available_dishes = 935

    with pytest.raises(ValueError):
        restaurant.available_dishes = [dish1, dish2, 'no_food']

    with pytest.raises(TypeError):
        restaurant.orders = 0

    with pytest.raises(ValueError):
        restaurant.orders = ['real_order', order1]

    with pytest.raises(ValueError):
        restaurant.orders = [fake_order, order1]

    client_create = Client('Alex')
    order_create = Order(client_create, [dish1])
    restaurant.create_order(order_create)
    assert order_create in restaurant.take_orders()

    with pytest.raises(ValueError):
        restaurant.create_order(fake_order)

    restaurant.remove_order(order_create)
    assert order_create not in restaurant.take_orders()

    with pytest.raises(ValueError):
        restaurant.remove_order(fake_order)
