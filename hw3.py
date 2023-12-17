"""Module for managing a restaurant."""
from typing import Any, List


def check_value_type(value: Any, type_: Any) -> bool:
    """
    Check type of value.

    :param value: Value to check
    :param type_: Expected type
    :return: True if value is of expected type, False otherwise
    :raises ValueError: If value is not of expected type
    """
    if not isinstance(value, type_):
        raise ValueError(f'Value must be {type_}')
    return True


class Product:
    """Class representing a product."""

    def __init__(self, name: str, price: float):
        """
        Create product.

        :param name: Name of the product
        :param price: Price of the product
        """
        self.name = name
        self.price = price

    @property
    def price(self) -> float:
        """
        Return price.

        :return: Price of the product
        """
        return self._price

    @price.setter
    def price(self, price_value: float):
        """
        Set price.

        :param price_value: New price
        :raises ValueError: If price is not positive
        """
        check_value_type(price_value, float)
        if price_value < 0:
            raise ValueError('Price must be positive')
        self._price = price_value

    @property
    def name(self) -> str:
        """
        Return name.

        :return: Name of the product
        """
        return self._name

    @name.setter
    def name(self, name_value: str):
        """
        Set name.

        :param name_value: New name
        """
        check_value_type(name_value, str)
        self._name = name_value


class Dish:
    """
    Class representing a dish.
    """

    def __init__(self, name: str, ingredients: List[Product]):
        """Create dish.

        :param name: Name of the dish
        :param ingredients: List of ingredients"""
        self.name = name
        self.ingredients = ingredients

    @property
    def name(self) -> str:
        """
        Return name.

        :return: Name of the dish
        """
        return self._name

    @name.setter
    def name(self, name_value: str):
        """
        Set name.

        :param name_value: New name
        """
        check_value_type(name_value, str)
        self._name = name_value

    @property
    def ingredients(self) -> List[Product]:
        """
        Return ingredients.

        :return: List of ingredients
        """
        return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients_value: List[Product]):
        """
        Set ingredients.

        :param ingredients_value: New list of ingredients
        """
        check_value_type(ingredients_value, list)
        for ingredient in ingredients_value:
            check_value_type(ingredient, Product)
        self._ingredients = ingredients_value

    def add_ingredient(self, product: Product):
        """
        Add ingredient.

        :param product: Product to add
        """
        check_value_type(product, Product)
        self._ingredients.append(product)

    def remove_ingredient(self, product: Product):
        """
        Delete ingredient.

        :param product: Product to remove
        """
        check_value_type(product, Product)
        self._ingredients.remove(product)


class Restaurant:
    """
    Class representing a restaurant.
    """

    def __init__(self, name: str, dishes: List[Dish], products: List[Product]):
        """Create restaurant.

        :param name: Name of the restaurant
        :param dishes: List of dishes
        :param products: List of products"""
        self.name = name
        self.dishes = dishes
        self.products = products

    @property
    def name(self) -> str:
        """
        Return name.

        :return: Name of the restaurant
        """
        return self._name

    @name.setter
    def name(self, name_value: str):
        """
        Set name.

        :param name_value: New name
        """
        check_value_type(name_value, str)
        self._name = name_value

    @property
    def dishes(self) -> List[Dish]:
        """
        Return dishes.

        :return: List of dishes
        """
        return self._dishes

    @dishes.setter
    def dishes(self, dishes_value: List[Dish]):
        """
        Set dishes.

        :param dishes_value: New list of dishes
        """
        check_value_type(dishes_value, list)
        for dish in dishes_value:
            check_value_type(dish, Dish)
        self._dishes = dishes_value

    @property
    def products(self) -> List[Product]:
        """
        Return products.

        :return: List of products
        """
        return self._products

    @products.setter
    def products(self, products_value: List[Product]):
        """
        Set products.

        :param products_value: New list of products
        """
        check_value_type(products_value, list)
        for product in products_value:
            check_value_type(product, Product)
        self._products = products_value

    def add_dish(self, dish: Dish):
        """
        Add dish.

        :param dish: Dish to add
        """
        check_value_type(dish, Dish)
        self._dishes.append(dish)

    def remove_dish(self, dish: Dish):
        """
        Delete dish.

        :param dish: Dish to remove
        """
        check_value_type(dish, Dish)
        self._dishes.remove(dish)

    def order_dish(self, dish: Dish) -> bool:
        """
        Order dish.

        :param dish: Dish to order
        :return: True if order is successful, False otherwise
        """
        check_value_type(dish, Dish)
        for ingredient in dish.ingredients:
            if ingredient not in self._products:
                return False
        return True
