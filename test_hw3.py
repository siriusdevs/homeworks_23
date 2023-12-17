import pytest
from hw3 import Product, Dish, Restaurant

def test_product():
    """Test Product class."""
    product = Product('Burger', 5.0)
    assert product.name == 'Burger'
    assert product.price == 5.0
    with pytest.raises(ValueError):
        product.price = -1.0
    with pytest.raises(ValueError):
        product.name = 123

def test_dish():
    """Test Dish class."""
    product1 = Product('Burger', 5.0)
    product2 = Product('Fries', 2.0)
    dish = Dish('Burger and Fries', [product1, product2])
    assert dish.name == 'Burger and Fries'
    assert dish.ingredients == [product1, product2]
    with pytest.raises(ValueError):
        dish.name = 123
    with pytest.raises(ValueError):
        dish.ingredients = ['Burger', 'Fries']

def test_restaurant():
    """Test Restaurant class."""
    product1 = Product('Burger', 5.0)
    product2 = Product('Fries', 2.0)
    dish = Dish('Burger and Fries', [product1, product2])
    restaurant = Restaurant('Fast Food', [dish], [product1, product2])
    assert restaurant.name == 'Fast Food'
    assert restaurant.dishes == [dish]
    assert restaurant.products == [product1, product2]
    with pytest.raises(ValueError):
        restaurant.name = 123
    with pytest.raises(ValueError):
        restaurant.dishes = ['Burger and Fries']
    with pytest.raises(ValueError):
        restaurant.products = ['Burger', 'Fries']
    assert restaurant.order_dish(dish) is not None
    restaurant.remove_dish(dish)
    assert restaurant.order_dish(dish) is False