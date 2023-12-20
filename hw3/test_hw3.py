"""Test for hw3 modul."""

import pytest

from .hw3 import Dish, Product, Restaurant

RAISES_TYPE_ERROR = pytest.raises(TypeError)
RAISES_TYPE_VALUE = pytest.raises(ValueError)


def _get_banana(): return Product('banana', 13)


def _get_apple(): return Product('apple', 10)


def _get_cereal(): return Product('cereal', 5)


def test_dish_property_error() -> None:
    """Test dish property for an error call."""
    numbers = [1, 2, 3]
    porridge = Dish('porrige', [])
    with RAISES_TYPE_ERROR:
        porridge.products = _get_apple()
    with RAISES_TYPE_ERROR:
        porridge.products = numbers
    with RAISES_TYPE_ERROR:
        porridge.name = numbers


def test_dish_method() -> None:
    """Test add_product, remove_product for correct working."""
    apple, banana, cereal = _get_apple(), _get_banana(), _get_cereal()
    porridge = Dish('porridge', [apple, banana, cereal])
    porridge.remove_product(apple)
    honey = Product('honey', 30)
    porridge.add_product(honey)
    assert porridge.products == [banana, cereal, honey]


def test_dish_method_error() -> None:
    """Test dish add_product and remove_product method for an error call."""
    porridge = Dish('porrige', [])
    with RAISES_TYPE_ERROR:
        porridge.add_product('')
    with RAISES_TYPE_VALUE:
        porridge.remove_product(_get_apple())
    with RAISES_TYPE_ERROR:
        porridge.remove_product('')


def test_restorant_property_error() -> None:
    """Test restorant property for an error call."""
    apple_juice = Dish('apple juice', [_get_apple()])
    restaurant = Restaurant('', [], [])
    numbers = [1, 2, 3]
    with RAISES_TYPE_ERROR:
        restaurant.dishes = apple_juice
    with RAISES_TYPE_ERROR:
        restaurant.dishes = numbers
    with RAISES_TYPE_ERROR:
        restaurant.products = numbers
    with RAISES_TYPE_ERROR:
        restaurant.name = 5


def test_restorant_methods_error() -> None:
    """Test dish add_product and remove_product method for an error call."""
    restaurant = Restaurant('', [], [])
    with RAISES_TYPE_ERROR:
        restaurant.add_dish('')
    with RAISES_TYPE_ERROR:
        restaurant.remove_dish(5)
    with RAISES_TYPE_ERROR:
        restaurant.add_product('')
    with RAISES_TYPE_ERROR:
        restaurant.remove_product('')


def test_restorant_methods() -> None:
    """Test add_product, add_dish, remove_product, remove_dish for correct working."""
    apple, banana, cereal = _get_apple(), _get_banana(), _get_cereal()
    apple_juice = Dish('apple juice', [apple])
    porridge = Dish('porridge', [cereal, banana])
    restaurant = Restaurant('', [apple_juice], [apple])
    restaurant.add_product(banana)
    restaurant.add_dish(porridge)
    restaurant.remove_dish(apple_juice)
    restaurant.remove_product(apple)
    assert restaurant.products == [banana]
    assert restaurant.dishes == [porridge]


def test_order_dish() -> None:
    """Test order_dish method."""
    banana, apple = _get_banana(), _get_apple()
    banana_porridge = Dish('banan_porridge', [banana])
    restaurant = Restaurant('', [banana_porridge], [banana])
    restaurant.add_product(apple)
    order_dish = restaurant.order_dish(banana_porridge.name)
    assert order_dish == banana_porridge
    assert banana_porridge not in restaurant.dishes
    assert apple not in restaurant.dishes
