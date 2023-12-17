"""Module for managing a restaurant."""
from typing import Any, List


def check_type_of_input(input_value: Any, expected_type: Any) -> bool:
    """
    Check type of input_value.

    Args:
        input_value: Input value
        expected_type: Expected type
    Raises:
        ValueError: If input_value is not expected_type
    """
    if not isinstance(input_value, expected_type):
        raise ValueError(f'Input value must be {expected_type}')
    return True


class Product:
    """Class representing a product."""

    def __init__(self, name: str, price: float):
        """
        Create product.

        Args:
            name (str): Name of the product
            price (float): Price of the product
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

        Args:
            price_value (float): New price
        Raises:
            ValueError: If price_value is negative
        """
        check_type_of_input(price_value, float)
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

        Args:
            name_value (str): New name
        """
        check_type_of_input(name_value, str)
        self._name = name_value


class Dish:
    """
    Class representing a dish.
    """

    def __init__(self, name: str, ingredients: List[Product]):
        """Create dish.

        Args:
            name (str): Name of the dish
            ingredients (list): List of ingredients
        """
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

        Args:
            name_value (str): New name
        """
        check_type_of_input(name_value, str)
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

        Args:
            ingredients_value (list): New list of ingredients
        """
        check_type_of_input(ingredients_value, list)
        for ingredient in ingredients_value:
            check_type_of_input(ingredient, Product)
        self._ingredients = ingredients_value

    def add_ingredient(self, product: Product):
        """
        Add ingredient.

        Args:
            product (Product): Product to add
        """
        check_type_of_input(product, Product)
        self._ingredients.append(product)

    def remove_ingredient(self, product: Product):
        """
        Delete ingredient.

        Args:
            product (Product): Product to remove
        """
        check_type_of_input(product, Product)
        self._ingredients.remove(product)


class Restaurant:
    """
    Class representing a restaurant.
    """

    def __init__(self, name: str, dishes: List[Dish], products: List[Product]):
        """Create restaurant.

        Args:
            name (str): Name of the restaurant
            dishes (list): List of dishes
            products (list): List of products
        """
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

        Args:
            name_value (str): New name
        """
        check_type_of_input(name_value, str)
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

        Args:
            dishes_value (list): New list of dishes
        """
        check_type_of_input(dishes_value, list)
        for dish in dishes_value:
            check_type_of_input(dish, Dish)
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

        Args:
            products_value (list): New list of products
        """
        check_type_of_input(products_value, list)
        for product in products_value:
            check_type_of_input(product, Product)
        self._products = products_value

    def add_dish(self, dish: Dish):
        """
        Add dish.

        Args:
            dish (Dish): Dish to add
        """
        check_type_of_input(dish, Dish)
        self._dishes.append(dish)

    def remove_dish(self, dish: Dish):
        """
        Delete dish.

        Args:
            dish (Dish): Dish to remove
        """
        check_type_of_input(dish, Dish)
        self._dishes.remove(dish)

    def order_dish(self, dish: Dish) -> bool:
        """
        Order dish.

        Args:
            dish (Dish): Dish to order
        :return: True if order is successful, False otherwise
        """
        check_type_of_input(dish, Dish)
        for ingredient in dish.ingredients:
            if ingredient not in self._products:
                return False
        return True
    