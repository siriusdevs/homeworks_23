"""Module include tests on every classes."""
from hw3 import Client, Dish, Order, Restorant

client = Client('Albert')
dish = Dish('Domácí termix', 9)
clients = [Client('Anna') for _ in range(4)]
dishes = [Dish('Zajíčkový dort', 1000) for _ in range(4)]
order = Order(clients, dishes)
orders = [Order(clients, dishes) for _ in range(4)]
av_dishes = dishes[1::2]
restorant = Restorant(orders, dishes, av_dishes)


def test_for_client() -> None:
    """Tests for Client class."""
    assert str(client) == 'Albert'
    client.name = 'Artem'
    assert client.name == 'Artem'
    try:
        client.name = 12
    except TypeError as err:
        assert str(err) == '12 must be str'


def test_for_dish() -> None:
    """Tests for Dish class."""
    assert str(dish) == 'Domácí termix: 9'
    dish.name_dish, dish.price = 'Utopencův salát', 9
    assert dish.name_dish == 'Utopencův salát' and dish.price == 9
    try:
        dish.name_dish, dish.price = 2020, 'Utopencův salát'
    except TypeError as err:
        expected = ('2020 must be str', 'Utopencův salát must be a number')
        assert str(err) in expected


def test_for_order() -> None:
    """Tests for Order class."""
    assert order.get_dishname() == 'Zajíčkový dort, Zajíčkový dort, Zajíčkový dort, Zajíčkový dort'
    add_dish = Dish('Domácí termix', 9)
    order.add_dish(add_dish)
    assert order.dishes[-1] == add_dish
    order.remove_dishes(add_dish)
    assert add_dish not in order.dishes
    try:
        order.dishes = ['Anna']
    except TypeError as err:
        assert str(err) == 'All value must be object type Dish'


def test_for_restourant() -> None:
    """Tests for Restorant class."""
    restorant.make_order(order)
    assert restorant.orders[-1] == order
    restorant.remove_order(order)
    assert order not in restorant.orders
    exp = 'Zajíčkový dort: 1000, Zajíčkový dort: 1000, Zajíčkový dort: 1000, Zajíčkový dort: 1000'
    assert restorant.get_order() == exp
