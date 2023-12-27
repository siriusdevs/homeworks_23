"""Main Module."""
from abc import ABC, abstractmethod


class Product(ABC):
    """Base class Product."""

    @abstractmethod
    def __init__(self, title: str, price: int | float):
        """Init Product.

        Args:
            title (str): product name
            price (int | float): price of the product
        """
        self.title = title
        self.price = price

    @property
    def title(self) -> str:
        """Get title of the product.

        Returns:
            str: title of the product
        """
        return self._title

    @title.setter
    def title(self, new_title: str) -> None:
        """Set new title of the product.

        Args:
            new_title (str): new product name

        Raises:
            TypeError: if new name is not a string
        """
        if not isinstance(new_title, str):
            raise TypeError(f'{new_title} is not a string')
        self._title = new_title

    @property
    def price(self) -> int | float:
        """Get price of the product.

        Returns:
            int | float: price of the product
        """
        return self._price

    @price.setter
    def price(self, new_price: int | float) -> None:
        """Set new price of the product.

        Args:
            new_price (int | float): new product price

        Raises:
            TypeError: if new price is not a integer or a float
            ValueError: if the new price is less than zero
        """
        if not isinstance(new_price, int | float):
            raise TypeError(f'{new_price} is not an integer or float')
        if new_price < 0:
            raise ValueError(f'{new_price} is less than zero')
        self._price = new_price


class Computer(Product):
    """Class Computer."""

    def __init__(self, title: str, price: int | float, operate_system: str, cpu: str):
        """Init Computer.

        Args:
            title (str): copmuter name
            price (int | float): price of the computer
            operate_system (str): computer operating system
            cpu (str): computer processor
        """
        super().__init__(title, price)
        self.operate_system = operate_system
        self.cpu = cpu

    @property
    def operate_system(self) -> str:
        """Get operating system of the computer.

        Returns:
            str: operating system of the computer
        """
        return self._operate_system

    @operate_system.setter
    def operate_system(self, new_operate_system: str) -> None:
        """Set new operating system of the computer.

        Args:
            new_operate_system (str): new operating system of the computer

        Raises:
            TypeError: if new operating system is not a string
        """
        if not isinstance(new_operate_system, str):
            raise TypeError(f'{new_operate_system} is not a string')
        self._operate_system = new_operate_system

    @property
    def cpu(self) -> str:
        """Get processor of the computer.

        Returns:
            str: processor of the computer
        """
        return self._cpu

    @cpu.setter
    def cpu(self, new_cpu: str) -> None:
        """Set new processor of the copmuter.

        Args:
            new_cpu (str): new processor of the computer

        Raises:
            TypeError: if new processor is not a string
        """
        if not isinstance(new_cpu, str):
            raise TypeError(f'{new_cpu} is not a string value')
        self._cpu = new_cpu


class Monitor(Product):
    """Class Monitor."""

    def __init__(self, title: str, price: int | float, screen_size: int, type_connection: str):
        """Init Monitor.

        Args:
            title (str): name of the monitor
            price (int | float): price of the monitor
            screen_size (int): screen size of the monitor
            type_connection (str): type connection of the monitor
        """
        super().__init__(title, price)
        self.screen_size = screen_size
        self.type_connection = type_connection

    @property
    def screen_size(self) -> int:
        """Get screen size of the monitor.

        Returns:
            int: screen size of the monitor
        """
        return self._screen_size

    @screen_size.setter
    def screen_size(self, new_screen_size: int) -> None:
        """Set new screen size of the monitor.

        Args:
            new_screen_size (int): new screen size of the monitor

        Raises:
            TypeError: if new screen size is not a integer
            ValueError: if new screen size is less than zero
        """
        if not isinstance(new_screen_size, int):
            raise TypeError(f'{new_screen_size} is not an integer')
        if new_screen_size < 0:
            raise ValueError(f'{new_screen_size} is less than zero')
        self._screen_size = new_screen_size

    @property
    def type_connection(self) -> str:
        """Get type connection of the monitor.

        Returns:
            str: type connection of the monitor
        """
        return self._type_connection

    @type_connection.setter
    def type_connection(self, new_type_connection: str) -> None:
        """Set new type connection of the monitor.

        Args:
            new_type_connection (str): new type connection of the monitor

        Raises:
            TypeError: if new type connection is not a string
        """
        if not isinstance(new_type_connection, str):
            raise TypeError(f'{new_type_connection} is not a srting value')
        self._type_connection = new_type_connection


class Store:
    """Class Store with products."""

    def __init__(self, products: list[Product]) -> None:
        """Init Store.

        Args:
            products (list[Product], optional): list with products
        """
        self.products = products

    @property
    def products(self) -> list[Product]:
        """Get products from the Store.

        Returns:
            list[Product]: products in the Store
        """
        return [product.title for product in self._products]

    @products.setter
    def products(self, new_products: list[Product]) -> None:
        """Set new products from the Store.

        Args:
            new_products (list[Product]): new list with the products

        Raises:
            TypeError: if the products are not a list
            TypeError: if products are not an object of the Product class
        """
        if not isinstance(new_products, list):
            raise TypeError(f'{new_products} is not a list')
        for product in new_products:
            if not isinstance(product, Product):
                raise TypeError(f'{product} must be a Product object')
        self._products = new_products

    def add_product(self, product: Product) -> None:
        """Add product to the Store.

        Args:
            product (Product): product for Store

        Raises:
            TypeError: if product is not an object of the Product class
        """
        if not isinstance(product, Product):
            raise TypeError(f'{product} must be a Product object')
        self._products.append(product)

    def remove_product(self, product: Product) -> None:
        """Remove product from Store.

        Args:
            product (Product): Store product

        Raises:
            TypeError: if product is not an object of the Product class
            ValueError: if the product is not in the Store
        """
        if not isinstance(product, Product):
            raise TypeError(f'{product} must be a Product object')
        if product not in self._products:
            raise ValueError(f'{product} is not in store')
        self._products.remove(product)

    def receive_products(self) -> list:
        """Receive a list of Store products.

        Returns:
            list: Store products list
        """
        return [product.title for product in self._products]
