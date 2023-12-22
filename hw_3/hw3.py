"""Architecture classes for managing a computer hardware store."""


from abc import ABC, abstractmethod
from typing import Any


class Product(ABC):
    """An abstract base class that represents a common product."""

    @abstractmethod
    def __init__(self, name: str, price: int | float) -> None:
        """Initialize a new instance of a product that has a name and a price.

        Args:
            name: str - name of product.
            price: int | float - price of product.
        """
        self.price = price
        self.name = name

    def check_str_type(self, exmple_value: Any) -> None:
        """Check if the value is a str.

        Args:
            exmple_value: Any - value to check.

        Raises:
            TypeError: if the value is not a str.
        """
        if not isinstance(exmple_value, str):
            exmple_value_type = type(exmple_value).__name__
            msg = f'{exmple_value} should be str not {exmple_value_type}'
            raise TypeError(msg)

    def check_num_type(self, exmple_value: Any) -> None:
        """Check if the value is an int or a float.

        Args:
            exmple_value: Any - value to check.

        Raises:
            TypeError: if the value is not an integer or a float.
        """
        if not isinstance(exmple_value, (int, float)):
            exmple_value_type = type(exmple_value).__name__
            msg = f'{exmple_value} should be int or float, not {exmple_value_type}'
            raise TypeError(msg)

    @property
    def name(self) -> str:
        """Find out the name of the product.

        Returns:
            str: product name.
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Set a new product name.

        Args:
            new_name: str - product new name.
        """
        self.check_str_type(new_name)
        self._name = new_name

    @property
    def price(self) -> int | float:
        """Find out the price of the product.

        Returns:
            int | float: price of product.
        """
        return self._price

    @price.setter
    def price(self, new_price: int | float) -> None:
        """Set a new price of the product.

        Args:
            new_price: int | float - new price of product.

        Raises:
            ValueError: will be obtained if the price is negative.
        """
        self.check_num_type(new_price)
        if new_price < 0:
            raise ValueError('The price must be greater than or equal to zero!')
        self._price = new_price


class Computer(Product):
    """Class that represents a computer product and inherits from Product."""

    __operating_systems = ('windows', 'linux', 'mac')
    __processor_form = ('amd', 'intel')

    def __init__(self, name: str, price: int | float, os: str, processor: str) -> None:
        """Initialize a new Computer instance.

        Args:
            name: str - computer name.
            price: int | float - computer price.
            os: str - computer operation system.
            processor: str - computer processor.
        """
        self.os = os
        self.processor = processor
        super().__init__(name, price)

    @property
    def processor(self) -> str:
        """Find out the processor type of the computer.

        Returns:
            str: computer processor form.
        """
        return self._processor

    @processor.setter
    def processor(self, new_processor: str) -> None:
        """Set a new processor form of the computer.

        Args:
            new_processor: str - new processor form for the computer.

        Raises:
            ValueError: will be obtained if the processor does not initiate with a recognized name.
        """
        self.check_str_type(new_processor)
        if not new_processor.lower().startswith(self.__processor_form):
            msg = ' or '.join(self.__processor_form)
            raise ValueError(f'Processor name should starts with {msg}')
        self._processor = new_processor

    @property
    def os(self) -> str:
        """Find out the operating system of the computer.

        Returns:
            str: computer operating system.
        """
        return self._os

    @os.setter
    def os(self, new_os: str) -> None:
        """Set a new operating system of the computer.

        Args:
            new_os: str - new operating system for the computer.

        Raises:
            ValueError: will be obtained if the OS is not one of the recognized options.
        """
        self.check_str_type(new_os)
        if new_os.lower() not in self.__operating_systems:
            systems = ', '.join(self.__operating_systems)
            raise ValueError(f'Incorrect value for the operating system, need one of: {systems}')
        self._os = new_os


class Screen(Product):
    """Class representing a screen product, inheriting from Product."""

    __connection_method = ('usb', 'vga', 'hdmi', 'display port')

    def __init__(self, name: str, price: int | float, diag: int | float, con_method: str) -> None:
        """Initialize a new instance of the Screen.

        Args:
            name: str - screen name.
            price: int | float - screen price.
            diag: int | float - screen diagonal.
            con_method: str - type of connector for connecting a screen to a computer.
        """
        self.diag = diag
        self.con_method = con_method
        super().__init__(name, price)

    @property
    def con_method(self) -> str:
        """Find out the connection type of the screen.

        Returns:
            str: connection type of the screen.
        """
        return self._con_method

    @con_method.setter
    def con_method(self, new_con_method: str) -> None:
        """Set a new connection type of the screen.

        Args:
            new_con_method: str - new connection type for the screen.

        Raises:
            ValueError: will be obtained if the type of connection is unspecified.
        """
        self.check_str_type(new_con_method)
        if new_con_method.lower() not in self.__connection_method:
            types = ', '.join(self.__connection_method)
            raise ValueError(f'Invalid value for connection_type, need one of: {types}')
        self._con_method = new_con_method

    @property
    def diag(self) -> int | float:
        """Find out the diagonal of the screen.

        Returns:
            int | float: diagonal of the screen.
        """
        return self._diag

    @diag.setter
    def diag(self, new_diag: int | float) -> None:
        """Set a new diagonal of the screen.

        Args:
            new_diag: int | float - new diagonal for the screen.
        """
        self.check_num_type(new_diag)
        self._diag = new_diag


class Store:
    """Class that embodies a computer hardware store."""

    def __init__(self, grocery_list: tuple[Product] | list[Product]) -> None:
        """Initialize a new Store instance.

        Args:
            grocery_list: tuple[Product] | list[Product] - list of products available in the store.
        """
        self.grocery_list = grocery_list

    def check_product(self, product: Any) -> None:
        """Check if the given object is an instance of the Product class.

        Args:
            product: Any - object to check.

        Raises:
            TypeError: if the object is not an instance of the Product class.
        """
        if not isinstance(product, Product):
            product_type = type(product).__name__
            msg = f'{product} should be Product not {product_type}'
            raise TypeError(msg)

    @property
    def grocery_list(self) -> list[Product]:
        """Find out the list of products available in the store.

        Returns:
            list[Product]: list of products available in the store.
        """
        return self._grocery_list

    @grocery_list.setter
    def grocery_list(self, new_grocery_list: tuple[Product] | list[Product]) -> None:
        """Set a new list of products available in the store.

        Args:
            new_grocery_list: tuple | list - new list of products for the store.

        Raises:
            TypeError: if the input is not a tuple or list, or if any item is not a Product.
        """
        if not isinstance(new_grocery_list, (tuple, list)):
            list_type = type(new_grocery_list).__name__
            msg = f'{new_grocery_list} should be tuple or list not {list_type}'
            raise TypeError(msg)
        for product in new_grocery_list:
            self.check_product(product)
        self._grocery_list = list(new_grocery_list)

    def get_all_products(self) -> str:
        """Find out names of products available in the store.

        Returns:
            str: names of products available in the store.
        """
        products_string = ', '.join([product.name for product in self._grocery_list])
        return f'Products are: {products_string}'

    def add_product(self, product: Product) -> None:
        """Add a product to the store product list.

        Args:
            product: Product - product to add to the product list.
        """
        self.check_product(product)
        self._grocery_list.append(product)

    def remove_product(self, product: Product) -> None:
        """Remove a product from the store product list.

        Args:
            product: Product - product to remove from the product list.
        """
        self.check_product(product)
        self._grocery_list.remove(product)
