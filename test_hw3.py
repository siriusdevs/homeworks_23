"""test module for hw3.py."""

import pytest

from hw3 import Dish, Product, Restaurant

MIDDLE_PRICE = 5.0
LOW_PRICE = 2.0


def test_product():
    """Test Product class."""
    product = Product('Burger', MIDDLE_PRICE)
    assert product.name == 'Burger'
    assert product.price == MIDDLE_PRICE
    with pytest.raises(ValueError):
        product.price = -1.0
    with pytest.raises(ValueError):
        product.name = 123


def test_dish():
    """Test Dish class."""
    product1 = Product('Cotlet', MIDDLE_PRICE)
    product2 = Product('Fries', LOW_PRICE)
    dish = Dish('Cotlet and Fries', [product1, product2])
    assert dish.name == 'Cotlet and Fries'
    assert dish.ingredients == [product1, product2]
    with pytest.raises(ValueError):
        dish.name = 123
    with pytest.raises(ValueError):
        dish.ingredients = ['Cotlet', 'Fries']


def test_restaurant():
    """Test Restaurant class."""
    product1 = Product('Salad', MIDDLE_PRICE)
    product2 = Product('Eggs', LOW_PRICE)
    dish = Dish('Salad and Eggs', [product1, product2])
    restaurant = Restaurant('Fast Food', [dish], [product1, product2])
    assert restaurant.name == 'Fast Food'
    assert restaurant.dishes == [dish]
    assert restaurant.products == [product1, product2]
    with pytest.raises(ValueError):
        restaurant.name = 123
    with pytest.raises(ValueError):
        restaurant.dishes = ['Salad and Eggs']
    with pytest.raises(ValueError):
        restaurant.products = ['Salad', 'Eggs']
    assert restaurant.order_dish(dish) is not None
    restaurant.remove_dish(dish)
    assert restaurant.order_dish(dish) is False
