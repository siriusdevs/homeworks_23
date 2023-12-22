"""Module for hw3 tests."""

import pytest
from dish import Dish
from product import Product
from restaurant import Restaurant

BASE_PRICE = 50
dought = Product('dough', BASE_PRICE)
apple = Product('Apple', BASE_PRICE)
flour = Product('Flour', BASE_PRICE)
product_apple_cake = [apple, dought, flour]
product_banana_cake = [Product('Banana', BASE_PRICE), Product('dough', BASE_PRICE)]
banana_cake = Dish('banana_cake', product_banana_cake)
apple_cake = Dish('apple_cake', product_apple_cake)
delikates = Dish('delikates', [Product('sueta', BASE_PRICE)])
dishes = {apple_cake, banana_cake}
sicilia = 'Sicilia'

data_setter_products = (
    ('Apple', 'Obama', TypeError),
    ('Apple', -50, ValueError),
    (50, 30, TypeError),
)

data_setter_dishes = (
    ('Apple Cake', 'Abrokadabra', TypeError),
    ('Apple Cake', ['Romodanov'], TypeError),
    (666, [Product('Apple', BASE_PRICE)], TypeError),
)

data_setter_restaurant = (
    (666, dishes, product_apple_cake, TypeError),
    (sicilia, 1, product_apple_cake, TypeError),
    (sicilia, {1, 2}, product_apple_cake, TypeError),
    (sicilia, dishes, 1, TypeError),
    (sicilia, dishes, [1, 2, 3], TypeError),
)

data_remove_products = (
    (product_apple_cake.copy(), [dought, flour].copy(), [apple]),
    (product_banana_cake.copy(), product_banana_cake.copy(), []),
    (product_banana_cake.copy(), [], product_banana_cake.copy()),
)

data_order_dishes = (
    (dishes.copy(), product_apple_cake.copy(), [banana_cake], [None]),
    (dishes.copy(), product_banana_cake.copy(), [banana_cake], [banana_cake]),
    (dishes.copy(), product_banana_cake.copy(), [banana_cake, banana_cake], [banana_cake, None]),
    (dishes.copy(), product_banana_cake.copy(), [], [None]),
    (dishes.copy(), product_banana_cake.copy(), [delikates], [None]),
)


@pytest.mark.parametrize('name, price, error', data_setter_products)
def test_setter_product(name, price, error):
    """Test setter for Product.

    Args:
        name (str): a product name
        price (int | float): a product price
        error (TypeError | ValueError): error for different wrong values
    """
    with pytest.raises(error):
        Product(name, price)


def test_flyweight_product():
    """Test flyweight pattern on Product."""
    first_apple = Product('Apple', BASE_PRICE)
    second_apple = Product('Apple', BASE_PRICE)
    gold_apple = Product('Gold Apple', BASE_PRICE)
    assert first_apple == second_apple
    assert first_apple != gold_apple


@pytest.mark.parametrize('dish_name, products, error', data_setter_dishes)
def test_setter_dish(dish_name, products, error):
    """Test setter for Dish.

    Args:
        dish_name (str): a dish name
        products (list[Product]): products
        error (TypeError): error for setter
    """
    with pytest.raises(error):
        Dish(dish_name, products)


def test_flyweight_dish():
    """Test flyweight parrent for Dish."""
    first_apple_cake = Dish('Apple Cake', [Product('Apple', BASE_PRICE)])
    second_apple_cake = Dish('Apple Cake', [Product('Apple', BASE_PRICE)])
    new_banana_cake = Dish('Banana Cake', [Product('Banana', BASE_PRICE)])
    assert first_apple_cake == second_apple_cake
    assert first_apple_cake != new_banana_cake


@pytest.mark.xfail(raises=TypeError)
def test_add_product_dish():
    """Test exception adding product with a wrong type."""
    dish = Dish('Apple Cake', [apple])
    dish.add_product('Java Spring Boot')


@pytest.mark.xfail(raises=TypeError)
def test_remove_product_dish():
    """Test exception removing product with a wrong type."""
    dish = Dish('Apple Cake', [Product('Apple', BASE_PRICE)])
    dish.remove_product('PostgreSQL')


@pytest.mark.parametrize('name, test_dishes, products, error', data_setter_restaurant)
def test_setter_restaurant(name, test_dishes, products, error):
    """Test setter restaurant with wrong types.

    Args:
        name (str): a restaurant name
        test_dishes (list[Dish]): dishes for restaurant
        products (list[Product]): product that restaurant has
        error (TypeError): exception for wrong types
    """
    with pytest.raises(error):
        Restaurant(name, test_dishes, products)


@pytest.mark.xfail(raises=TypeError)
def test_error_remove_products():
    """Text removing product with a wrong type."""
    restaurant = Restaurant(sicilia, dishes, product_apple_cake)
    restaurant.remove_products('CREATE INDEX ON..')


@pytest.mark.parametrize('products, removing_products, remaining_products', data_remove_products)
def test_remove_products(products, removing_products, remaining_products):
    """Test removing products.

    Args:
        products (list[Product]): products that restaurant has
        removing_products (list[Product]): products that we remove
        remaining_products (list[Product]): products that must be remain
    """
    restaurant = Restaurant(sicilia, dishes.copy(), products)
    restaurant.remove_products(removing_products.copy())

    assert restaurant.products == remaining_products


@pytest.mark.xfail(raises=TypeError)
def test_add_dish_error():
    """Test adding dish with wrong type."""
    restaurant = Restaurant(sicilia, dishes, product_banana_cake)
    restaurant.add_dish('Beans, RequestMapping')


def test_add_dish():
    """Test adding dish."""
    restaurant = Restaurant(sicilia, dishes.copy(), product_banana_cake)
    new_dish = Dish('Olivie', [Product('sausage', BASE_PRICE), Product('mayo', BASE_PRICE)])
    restaurant.add_dish(new_dish)
    excepted = dishes.copy()
    excepted.add(new_dish)

    assert restaurant.suggest_dishes == excepted


@pytest.mark.xfail(raises=TypeError)
def test_remove_dish_error():
    """Test removing dish with wrong type."""
    restaurant = Restaurant(sicilia, dishes, product_banana_cake)
    restaurant.remove_dish('GetMapping')


def test_remove_dish():
    """Test removing dish."""
    restaurant = Restaurant(sicilia, dishes.copy(), product_apple_cake)
    restaurant.remove_dish(Dish('apple_cake', product_apple_cake))
    assert restaurant.suggest_dishes == {Dish('banana_cake', product_banana_cake)}


@pytest.mark.parametrize('test_dishes, products, order_dishes, excepteds', data_order_dishes)
def test_order_dish(test_dishes, products, order_dishes, excepteds):
    """Test ordering dishes.

    Args:
        test_dishes (list[Dish]): suggested dishes at restaurant
        products (list[Product]): products that restaurant has
        order_dishes (list[Dish]): dishes that we order
        excepteds (list[Dish]): the excepted values
    """
    restaurant = Restaurant(sicilia, test_dishes, products)
    for num, el in enumerate(order_dishes):
        assert restaurant.order_dish(el) == excepteds[num]


@pytest.mark.xfail(raises=TypeError)
def test_order_dish_error():
    """Test 'order_dish' function on TypeError."""
    restaurant = Restaurant(sicilia, dishes, product_apple_cake)
    restaurant.order_dish('CREATE INDEX ... ON ...')
