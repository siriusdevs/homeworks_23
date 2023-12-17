from typing import Any


def check_type(value: Any, type_: Any) -> bool:
    """Check type of value."""
    if not isinstance(value, type_):
        raise ValueError(f'Value must be {type_}')


class Product:
    def __init__(self, name: str, price: float):
        """Create product."""
        self.name = name
        self.price = price

    @property
    def price(self) -> float:
        """Return price."""
        return self._price

    @price.setter
    def price(self, value):
        """Set price."""
        check_type(value, float)
        if value < 0:
            raise ValueError('Price must be positive')
        self._price = value

    @property
    def name(self) -> str:
        """Return name."""
        return self._name

    @name.setter
    def name(self, value):
        """Set name."""
        check_type(value, str)
        self._name = value


class Dish:
    def __init__(self, name: str, ingredients: list[Product]):
        """Create dish."""
        self.name = name
        self.ingredients = ingredients

    @property
    def name(self) -> str:
        """Return name."""
        return self._name

    @name.setter
    def name(self, value):
        """Set name."""
        check_type(value, str)
        self._name = value

    @property
    def ingredients(self) -> list[Product]:
        """Return ingredients."""
        return self._ingredients

    @ingredients.setter
    def ingredients(self, value):
        """Set ingredients."""
        check_type(value, list)
        for item in value:
            check_type(item, Product)
        self._ingredients = value

    def add_ingredient(self, product: Product):
        """Add ingredient."""
        check_type(product, Product)
        self._ingredients.append(product)

    def remove_ingredient(self, product: Product):
        """Delete ingredient."""
        check_type(product, Product)
        self._ingredients.remove(product)


class Restaurant:
    def __init__(self, name: str, dishes: list[Dish], products: list[Product]):
        """Create restaurant."""
        self.name = name
        self.dishes = dishes
        self.products = products

    @property
    def name(self) -> str:
        """Return name."""
        return self._name

    @name.setter
    def name(self, value):
        """Set name."""
        check_type(value, str)
        self._name = value

    @property
    def dishes(self) -> list[Dish]:
        """Return dishes."""
        return self._dishes

    @dishes.setter
    def dishes(self, value):
        """Set dishes."""
        check_type(value, list)
        for item in value:
            check_type(item, Dish)
        self._dishes = value

    @property
    def products(self) -> list[Product]:
        """Return products."""
        return self._products

    @products.setter
    def products(self, value):
        """Set products."""
        check_type(value, list)
        for item in value:
            check_type(item, Product)
        self._products = value

    def add_dish(self, dish: Dish):
        """Add dish."""
        check_type(dish, Dish)
        self._dishes.append(dish)

    def remove_dish(self, dish: Dish):
        """Delete dish."""
        check_type(dish, Dish)
        self._dishes.remove(dish)

    def order_dish(self, dish: Dish) -> bool:
        """Order dish."""
        check_type(dish, Dish)
        for ingredient in dish.ingredients:
            if ingredient not in self._products:
                print(f'Not enough {ingredient.name}')
        print(f'Order {dish.name}')