from traitlets import Any


def check_type(obj_: Any, class_or_tuple: tuple[type] | type):
    if not isinstance(obj_, class_or_tuple):
        raise TypeError(f"{obj_} is not {class_or_tuple}.")


def check_type_of_list(list_: list[Any], class_or_tuple: tuple[type] | type):
    check_type(list_, list)
    for item in list_:
        check_type(item, class_or_tuple)


class Product:
    def __init__(self, name: str, price: int) -> None:
        self.name, self.price = name, price

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        check_type(new_name, str)
        self._name = new_name


class Dish:
    def __init__(self, name: str, products: list[Product]) -> None:
        self.name, self.products = name, products

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        check_type(new_name, str)
        self._name = new_name

    @property
    def products(self) -> list[Product]:
        return self._products

    @products.setter
    def products(self, new_products: list[Product]) -> None:
        check_type_of_list(new_products, Product)
        self._products = new_products

    def add_product(self, product: Product):
        check_type(product, Product)
        self.products.append(product)

    def remove_product(self, product: Product):
        check_type(product, Product)
        if product not in self.products:
            ValueError(f'{product} is not exist.')
        self.products.remove(product)


class Restaurant:
    def __init__(self, name: str, dishes: list[Dish], products: list[Product]) -> None:
        self.name, self.dishes = name, dishes
        self.products = products

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        check_type(new_name, str)
        self._name = new_name

    @property
    def dishes(self) -> list[Dish]:
        return self._dishes

    @dishes.setter
    def dishes(self, new_dishes: list[Dish]) -> None:
        check_type_of_list(new_dishes, Dish)
        self._dishes = new_dishes

    def add_dish(self, dish: Dish):
        check_type(dish, Dish)
        self.dishes.append(dish)

    def remove_dish(self, dish: Dish):
        check_type(dish, Dish)
        if dish not in self.dishes:
            ValueError(f'{dish} is not exist.')
        self.dishes.remove(dish)

    @property
    def products(self) -> list[Product]:
        return self._products

    @products.setter
    def products(self, new_products: list[Product]) -> None:
        check_type_of_list(new_products, Product)
        self._products = new_products

    def add_product(self, product: Product):
        check_type(product, Product)
        self.products.append(product)

    def remove_product(self, product: Product):
        check_type(product, Product)
        if product not in self.products:
            ValueError(f'{product} is not exist.')
        self.products.remove(product)

    def order_dish(self, dish_name: str) -> Dish | None:
        dishes = list(filter(lambda dish: dish.name == dish_name, self.dishes))
        if not dishes:
            return None
        first_dish = dishes[0]
        if set(first_dish.products).issubset(self.products):
            self.products = list(filter(lambda i: i not in first_dish.products, self.products))
            self.remove_dish(first_dish)
            return first_dish
        return None
