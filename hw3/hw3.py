"""Module for ordering dishes and managing products."""

from traitlets import Any

UNDERSCORE = '_'
PRODUCTS = 'products'
PRODUCT = 'product'
DISHES = 'dishes'
DISH = 'dish'
NAME = 'name'
PRICE = 'price'


def _check_type(object_being_checked: Any, class_or_tuple: tuple[type] | type) -> type:
    if not isinstance(object_being_checked, class_or_tuple):
        raise TypeError(f'{object_being_checked} is not {class_or_tuple}.')


def _check_type_of_list(entries: list[Any], class_or_tuple: tuple[type, ...] | type) -> type:
    _check_type(entries, list)
    for entry in entries:
        _check_type(entry, class_or_tuple)


def _add_property(property_name: str, class_or_tuple: type | tuple[type, ...]) -> type:
    def wrapper(cls):
        def _get(self):
            return getattr(cls, f'{UNDERSCORE}{property_name}')

        def _set(self, new_value):
            _check_type(new_value, class_or_tuple)
            setattr(cls, f'{UNDERSCORE}{property_name}', new_value)
        getter = property(_get)
        setattr(cls, property_name, getter)
        setattr(cls, property_name, getter.setter(_set))
        return cls
    return wrapper


def _add_list_property(list_name: str, class_or_tuple: type | tuple[type, ...]) -> type:
    def wrapper(cls):
        def _get(self):
            return getattr(cls, f'{UNDERSCORE}{list_name}')

        def _set(self, new_value: list[Any]):
            _check_type_of_list(new_value, class_or_tuple)
            setattr(cls, f'{UNDERSCORE}{list_name}', new_value)

        getter = property(_get)
        setattr(cls, list_name, getter)
        setattr(cls, list_name, getter.setter(_set))
        return cls
    return wrapper


def _add_adding_removeing_method(
    list_name: str,
    method_name: str,
    class_or_tuple: type | tuple[type, ...],
) -> type:
    def wrapper(cls):
        def remove(self, entry: Any):
            _check_type(entry, class_or_tuple)
            entries = getattr(cls, f'{UNDERSCORE}{list_name}')
            if entry not in entries:
                ValueError(f"{entry} doesn't exist.")
            entries.remove(entry)

        def add(self, entry: Any):
            _check_type(entry, class_or_tuple)
            entries = getattr(cls, f'{UNDERSCORE}{list_name}')
            entries.append(entry)

        setattr(cls, f'remove_{method_name}', remove)
        setattr(cls, f'add_{method_name}', add)
        return cls
    return wrapper


@_add_property(NAME, str)
@_add_property(PRICE, int)
class Product:
    """Product for eating."""

    def __init__(self, name: str, price: int) -> None:
        """Create a named product with a price.

        Args:
            name: product name.
            price (int): product price.
        """
        self.name, self.price = name, price


@_add_adding_removeing_method(PRODUCTS, PRODUCT, Product)
@_add_list_property(PRODUCTS, Product)
@_add_property(NAME, str)
class Dish:
    """Dish consisting of products.

    Methods
    -------
    add_products(product: Product)
        add the product to the list of products.
    remove_products(product: Product)
        delete the existing product from the product list.
    """

    def __init__(self, name: str, products: list[Product]) -> None:
        """Create named dish with create a named dish with the products it consists of.

        Args:
            name (str): _description_
            products (list[Product]): _description_
        """
        self.name, self.products = name, products


@_add_adding_removeing_method(PRODUCTS, PRODUCT, Product)
@_add_list_property(PRODUCTS, Product)
@_add_adding_removeing_method(DISHES, DISH, Dish)
@_add_list_property(DISHES, Dish)
@_add_property(NAME, str)
class Restaurant:
    """Restaurant with dishes and a warehouse for products.

    Methods
    -------
    add_products(product: Product)
        add the product to the list of products.
    remove_products(product: Product)
        delete the existing product from the product list.
    add_dish(dish: Dish)
        add the dish to the list of dishes.
    remove_products(dish: Dish)
        delete the existing dish from the dish list.
    order_dish(dish_name: str)
        return the dish if it is in the restaurant, otherwise return None.
    """

    def __init__(self, name: str, dishes: list[Dish], products: list[Product]) -> None:
        """Create restaurant with dishes and products.

        Args:
            name: product name.
            dishes: list of dishes.
            products: list of products.
        """
        self.name, self.dishes, self.products = name, dishes, products

    def order_dish(self, dish_name: str) -> Dish | None:
        """Find selected dish by name.

        Args:
            dish_name (str): name of the selected dish.

        Returns:
            Dish | None: dish if it is in the restaurant, otherwise return None.
        """
        dishes = list(filter(lambda dish: dish.name == dish_name, self.dishes))
        if not dishes:
            return None
        first_dish = dishes[0]
        if not set(first_dish.products).issubset(self.products):
            return None
        self.products = list(filter(
            lambda product: product not in first_dish.products, self.products,
        ))
        self.remove_dish(first_dish)
        return first_dish
