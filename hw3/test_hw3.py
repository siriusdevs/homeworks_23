import pytest
from .hw3 import Product, Dish, Restaurant

NUMBERS = [1, 2, 3]

def _get_banana(): return Product('banana', 13)


def _get_apple(): return Product('apple', 10)


def _get_cereal(): return Product('cereal', 5)


def _get_honey(): return Product('honey', 30)


def test_dish_property():
    apple, banana, cereal, honey = _get_apple(), _get_banana(), _get_cereal(), _get_honey()
    porridge = Dish('porridge', [apple, banana, cereal])
    porridge.remove_product(apple)
    porridge.add_product(honey)
    assert porridge.products == [banana, cereal, honey]


def test_dish_error():
    porridge = Dish('porrige', [])
    with pytest.raises(TypeError):
        return porridge.add_product('')
    with pytest.raises(ValueError):
        return porridge.remove_product(_get_apple())
    with pytest.raises(TypeError):
        return porridge.remove_product('')
    with pytest.raises(TypeError):
        porridge.name = 54321
    with pytest.raises(TypeError):
        porridge.products = _get_apple()
    with pytest.raises(TypeError):
        porridge.products = NUMBERS


def test_restorant_property():
    apple, banana, cereal = _get_apple(), _get_banana(), _get_cereal()
    apple_juice = Dish('apple juice', [apple])
    porridge = Dish('porridge', [cereal, banana])
    restaurant = Restaurant('noname', [apple_juice], [apple])
    restaurant.add_product(banana)
    restaurant.add_dish(porridge)
    restaurant.remove_dish(apple)
    restaurant.remove_product(apple)
    restaurant.name 
    assert


def test_restorant_error():
    apple_juice = Dish('apple juice', [_get_apple()])
    restaurant = Restaurant('noname', [], [])
    with pytest.raises(TypeError):
        restaurant.dishes = apple_juice
    with pytest.raises(TypeError):
        restaurant.dishes = NUMBERS
    with pytest.raises(TypeError):
        return restaurant.add_product('')
    with pytest.raises(ValueError):
        return restaurant.remove_product(_get_apple())
    with pytest.raises(TypeError):
        return restaurant.remove_product('')
    with pytest.raises(TypeError):
        restaurant.products = NUMBERS

def test_order_dish():
    banana, apple = _get_banana(), _get_apple()
    banana_porridge = Dish('banan_porridge', [banana])
    restaurant = Restaurant('noname', [banana_porridge], [banana])
    restaurant.add_product(apple)
    result = restaurant.order_dish(banana_porridge.name)
    assert result == banana_porridge
    assert banana_porridge not in restaurant.dishes
    assert apple not in restaurant.dishes