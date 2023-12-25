"""Архитектура классов для учета товаров в ресторане."""
from typing import List


class Product:
    """Класс, представляющий товар."""

    def __init__(self, name: str, price: float):
        """
        Инициализирует новый экземпляр класса Product.

        Args:
            name (str): название продукта
            price (float): цена продукта
        """
        self._name = name
        self._price = price

    @property
    def name(self) -> str:
        """
        Возвращает название товара.

        Returns:
            _name (str): название продукта
        """
        return self._name

    @name.setter
    def name(self, name_value: str):
        """
        Устанавливает название товара.

        Args:
            name_value (str): значения имени

        Raises:
            TypeError: если значение не является str
        """
        if not isinstance(name_value, str):
            raise TypeError('Имя {0} должно быть str, а не {1}'.format(
                name_value,
                type(name_value).name
            ))
        self._name = name_value

    @property
    def price(self) -> float:
        """
        Возвращает цену товара.

        Returns:
            _price (float): цена продукта
        """
        return self._price

    @price.setter
    def price(self, price_value: float):
        """
        Устанавливает цену товара.

        Args:
            price_value (str)

        Raises:
            TypeError: если значение не является str
            ValueError: если цена меньше 0
        """
        if not isinstance(price_value, float):
            raise TypeError('Цена {0} должно быть float, а не {1}'.format(
                price_value,
                type(price_value).price
            ))
        if price_value <= 0:
            raise ValueError('Цена должна быть положительным числом')
        self._price = price_value


class Dish:
    """Класс, представляющий блюдо."""

    def __init__(self, name: str):
        """
        Инициализирует новый экземпляр класса Dish.

        Args:
            name (str): имя блюда
        """
        self._name = name
        self._products = []

    @property
    def name(self) -> str:
        """
        Возвращает название блюда.

        Returns:
            _name (str): значение имени
        """
        return self._name

    @name.setter
    def name(self, name_value: str):
        """
        Устанавливает название блюда.

        Args:
            name_value (str): название блюда

        Raises:
            TypeError: если значение не является str
        """
        if not isinstance(name_value, str):
            raise TypeError('Имя {0} должно быть str, а не {1}'.format(
                name_value,
                type(name_value).name
            ))
        self._name = name_value

    @property
    def products(self) -> List[Product]:
        """
        Возвращает список продуктов в блюде.

        Returns:
            List: список продуктов в блюде.
        """
        return self._products

    def add_product(self, product: Product):
        """
        Добавляет продукт в блюдо.

        Args:
            product (Product): объект продукта.
        """
        self._products.append(product)

    def remove_product(self, product: Product):
        """
        Удаляет продукт из блюда.

        Args:
            product (Product): объект продукта
        """
        self._products.remove(product)


class Restaurant:
    """Класс, представляющий ресторан."""

    def __init__(self, name: str, dishes: List[Dish], inventory: List[Product]):
        """
        Инициализирует новый экземпляр класса Restaurant.

        Args:
            name (str): название ресторана
            dishes (List): список блюд
            inventory (List): список продуктов, из которых приготовлено блюдо
        """
        self._name = name
        self._dishes = dishes
        self._inventory = inventory

    @property
    def name(self) -> str:
        """
        Возвращает название ресторана.

        Returns:
            _name (str): название ресторана
        """
        return self._name

    @name.setter
    def name(self, name_value: str):
        """
        Устанавливает название ресторана.

        Args:
            name_value (str): значение названия ресторана

        Raises:
            TypeError: если значение не является str
        """
        if not isinstance(name_value, str):
            raise TypeError('Имя {0} должно быть str, а не {1}'.format(
                name_value,
                type(name_value).name
            ))
        self._name = name_value

    @property
    def dishes(self) -> List[Dish]:
        """
        Возвращает список блюд, предлагаемых рестораном.

        Returns:
            List: список блюд
        """
        return self._dishes

    def add_dish(self, dish: Dish):
        """
        Добавляет блюдо в меню.

        Args:
            dish (Dish): объект продукта
        """
        self._dishes.append(dish)

    def remove_dish(self, dish: Dish):
        """
        Удаляет блюдо из меню.

        Args:
            dish: объект продукта
        """
        self._dishes.remove(dish)

    @property
    def inventory(self) -> List[Product]:
        """
        Возвращает инвентарь ресторана.

        Returns:
            List (list): список продуктов для блюда.
        """
        return self._inventory

    def order_dish(self, dish: Dish) -> str:
        """
        Заказывает блюдо, и обновляет инвентарь соответственно.

        Args:
            dish: объект продукта

        Returns:
            str: уведомление о статусе заказа
        """
        dish_products = dish.products
        for product in dish_products:
            if product not in self._inventory:
                return 'Не хватает товаров на складе'
        for product in dish_products:
            self._inventory.remove(product)
        return 'Блюдо заказано успешно'
