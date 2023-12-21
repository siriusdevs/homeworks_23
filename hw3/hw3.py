"""Class architecture for managing a computer hardware store."""


from abc import ABC, abstractmethod
from typing import Any


class Product(ABC):
    """Abstract base class representing a generic product."""

    @abstractmethod
    def __init__(self, name: str, price: int | float) -> None:
        """Initialize a new Product instance with a name and price.

        Args:
            name: str - product name.
            price: int | float - product price.
        """
        self.name = name
        self.price = price

    def is_str(self, operand: Any) -> None:
        """Check if the operand is a string.

        Args:
            operand: Any - operand to check.

        Raises:
            TypeError: if the operand is not a string.
        """
        if not isinstance(operand, str):
            object_type = type(operand).__name__
            err_message = f'{operand} should be str not {object_type}'
            raise TypeError(err_message)

    def is_int_or_float(self, operand: Any) -> None:
        """Check if the operand is an int or a float.

        Args:
            operand: Any - operand to check.

        Raises:
            TypeError: if the operand is not an integer or a float.
        """
        if not isinstance(operand, (int, float)):
            object_type = type(operand).__name__
            err_message = f'{operand} should be int or float not {object_type}'
            raise TypeError(err_message)

    @property
    def name(self) -> str:
        """Get the name of the product.

        Returns:
            str: name of the product.
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Set the name of the product.

        Args:
            new_name: str - new name for the product.
        """
        self.is_str(new_name)
        self._name = new_name

    @property
    def price(self) -> int | float:
        """Get the price of the product.

        Returns:
            int | float: price of the product.
        """
        return self._price

    @price.setter
    def price(self, new_price: int | float) -> None:
        """Set the price of the product.

        Args:
            new_price: int | float - new price for the product.
        """
        self.is_int_or_float(new_price)
        self._price = new_price


class Computer(Product):
    """Class representing a computer product, inheriting from Product."""

    __op_systems = ('windows', 'ubuntu', 'macos')
    __processor_types = ('amd', 'intel')

    def __init__(self, name: str, price: int | float, os: str, processor: str) -> None:
        """Initialize a new Computer instance.

        Args:
            name: str - computer name.
            price: int | float - price of computer.
            os: str - operation system installed on computer.
            processor: str - processor in a computer.
        """
        self.os = os
        self.processor = processor
        super().__init__(name, price)

    @property
    def os(self) -> str:
        """Get the operating system of the computer.

        Returns:
            str: operating system of the computer.
        """
        return self._os

    @os.setter
    def os(self, new_os: str) -> None:
        """Set the operating system of the computer.

        Args:
            new_os: str - new operating system for the computer.

        Raises:
            ValueError: if the OS is not one of the known.
        """
        self.is_str(new_os)
        if new_os.lower() not in self.__op_systems:
            systems = ', '.join(self.__op_systems)
            raise ValueError(f'Wrong value for OS. Supported: {systems}')
        self._os = new_os

    @property
    def processor(self) -> str:
        """Get the processor type of the computer.

        Returns:
            str: processor type of the computer.
        """
        return self._processor

    @processor.setter
    def processor(self, new_processor: str) -> None:
        """Set the processor type of the computer.

        Args:
            new_processor: str - new processor type for the computer.

        Raises:
            ValueError: if the processor does not start with a resolved name.
        """
        self.is_str(new_processor)
        if not new_processor.lower().startswith(self.__processor_types):
            types = ' or '.join(self.__processor_types)
            raise ValueError(f'Processor name should starts with {types}')
        self._processor = new_processor


class Monitor(Product):
    """Class representing a monitor product, inheriting from Product."""

    __con_types = ('usb', 'hdmi', 'thunderbolt', 'vga', 'display port', 'dvi')

    def __init__(self, name: str, price: int | float, size: int | float, con_type: str) -> None:
        """Initialize a new Monitor instance.

        Args:
            name: str - monitor name.
            price: int | float - monitor price.
            size: int | float - monitor size (diagonal).
            con_type: str - type of connector for connecting a monitor to a computer.
        """
        self.size = size
        self.con_type = con_type
        super().__init__(name, price)

    @property
    def size(self) -> int | float:
        """Get the diagonal size of the monitor.

        Returns:
            int | float: diagonal size of the monitor.
        """
        return self._size

    @size.setter
    def size(self, new_size: int | float) -> None:
        """Set the diagonal size of the monitor.

        Args:
            new_size: int | float - new diagonal size for the monitor.
        """
        self.is_int_or_float(new_size)
        self._size = new_size

    @property
    def con_type(self) -> str:
        """Get the connection type of the monitor.

        Returns:
            str: connection type of the monitor.
        """
        return self._con_type

    @con_type.setter
    def con_type(self, new_con_type: str) -> None:
        """Set the connection type of the monitor.

        Args:
            new_con_type: str - new connection type for the monitor.

        Raises:
            ValueError: if the connection type is unknown.
        """
        self.is_str(new_con_type)
        if new_con_type.lower() not in self.__con_types:
            types = ', '.join(self.__con_types)
            raise ValueError(f'Wrong value for connection_type. Supported: {types}')
        self._con_type = new_con_type


class Shop:
    """Class representing a computer hardware store."""

    def __init__(self, product_list: tuple[Product] | list[Product]) -> None:
        """Initialize a new Shop instance.

        Args:
            product_list: tuple[Product] | list[Product] - list of products available in the store.
        """
        self.product_list = product_list

    def is_product(self, product: Any) -> None:
        """Check if the given object is an instance of the Product class.

        Args:
            product: Any - object to check.

        Raises:
            TypeError: if the object is not an instance of the Product class.
        """
        if not isinstance(product, Product):
            product_type = type(product).__name__
            err_message = f'{product} should be Product not {product_type}'
            raise TypeError(err_message)

    @property
    def product_list(self) -> list[Product]:
        """Get the list of products available in the store.

        Returns:
            list[Product]: list of products available in the store.
        """
        return self._product_list

    @product_list.setter
    def product_list(self, new_product_list: tuple[Product] | list[Product]) -> None:
        """Set the list of products available in the store.

        Args:
            new_product_list: tuple | list - new list of products for the store.

        Raises:
            TypeError: if the input is not a tuple or list, or if any item inside is not a Product.
        """
        if not isinstance(new_product_list, (tuple, list)):
            list_type = type(new_product_list).__name__
            err_message = f'{new_product_list} should be tuple or list not {list_type}'
            raise TypeError(err_message)
        for product in new_product_list:
            self.is_product(product)
        self._product_list = list(new_product_list)

    def add_product(self, product: Product) -> None:
        """Add a product to the store product list.

        Args:
            product: Product - product to add to the product list.
        """
        self.is_product(product)
        self._product_list.append(product)

    def remove_product(self, product: Product) -> None:
        """Remove a product from the store product list.

        Args:
            product: Product - product to remove from the product list.
        """
        self.is_product(product)
        self._product_list.remove(product)

    def get_all_products(self) -> str:
        """Get names of all products available in the store.

        Returns:
            str: names of all products available in the store.
        """
        products_string = ', '.join([product.name for product in self._product_list])
        return f'Products are: {products_string}'
