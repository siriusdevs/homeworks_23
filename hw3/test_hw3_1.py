"""Testing classes Client, Dish, Order from module hw3.py."""
import pytest

from hw3 import Client, Dish, Order


def test_dish_attributes():
    """
    Test case for checking the attributes of a Dish object.

    Creates a Dish object with a name and price. Asserts that the name and price
    attributes of the Dish object are set correctly. Also tests for attribute
    assignment errors and invalid price values.
    """
    dish = Dish('Pizza', 10)
    assert dish.name == 'Pizza'
    assert dish.price == 10

    with pytest.raises(TypeError):
        dish.name = 123

    with pytest.raises(TypeError):
        dish.price = 'Much money'

    with pytest.raises(ValueError):
        dish.price = -5


def test_client_attributes():
    """
    Test case for checking the attributes of a Client object.

    Creates a Client object with a name. Asserts that the name attribute of the
    Client object is set correctly. Also tests for attribute assignment errors.
    """
    client = Client('John Doe')
    assert client.name == 'John Doe'

    with pytest.raises(TypeError):
        client.name = 123


def test_order_management():
    """
    Test case for order management in a restaurant.

    Tests the creation of an Order object, managing the client and list of dishes.
    Asserts attribute assignment errors and value errors.
    Also tests adding and removing dishes from the order.
    """
    price1 = 15
    dish1 = Dish('Pasta', price1)
    client1 = Client('Jane Smith')
    order = Order(client1, [dish1])

    with pytest.raises(TypeError):
        order.client = 123

    with pytest.raises(TypeError):
        order.list_of_dishes = {dish1: Dish('Egg', 5)}

    with pytest.raises(ValueError):
        order.list_of_dishes = [dish1, 5]

    assert order.client == client1
    assert order.get_list() == [dish1]

    dish_create = Dish('Salad', 8)
    order.add(dish_create)
    assert order.get_list() == [dish1, dish_create]

    with pytest.raises(ValueError):
        order.add(dish1)

    with pytest.raises(TypeError):
        order.add('dish')

    order.remove(dish_create)
    assert order.get_list() == [dish1]

    with pytest.raises(ValueError):
        order.remove(dish_create)
