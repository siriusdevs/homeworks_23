"""Class architecture for managing a computer hardware store."""


class Product:
    def __init__(self, name: str, price: int | float) -> None:
        self.name = name
        self.price = price

    def is_str(self, operand: str) -> None:
        if not isinstance(operand, str):
            object_type = type(operand).__name__
            err_message = f'{operand} should be str not {object_type}'
            raise TypeError(err_message)

    def is_int_or_float(self, operand: int | float) -> None:
        if not isinstance(operand, (int, float)):
            object_type = type(operand).__name__
            err_message = f'{operand} should be int or float not {object_type}'
            raise TypeError(err_message)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        self.is_str(new_name)
        self._name = new_name

    @property
    def price(self) -> int | float:
        return self._price

    @price.setter
    def price(self, new_price: int | float) -> None:
        self.is_int_or_float(new_price)
        self._price = new_price


class Computer(Product):
    __op_systems = ('windows', 'ubuntu', 'macos')
    __processor_types = ('amd', 'intel')

    def __init__(self, name: str, price: int | float, os: str, processor: str) -> None:
        self.os = os
        self.processor = processor
        super().__init__(name, price)

    @property
    def os(self) -> str:
        return self._os

    @os.setter
    def os(self, new_os: str) -> None:
        self.is_str(new_os)
        if new_os.lower() not in self.__op_systems:
            systems = ', '.join(self.__op_systems)
            raise ValueError(f'Wrong value for OS. Supported: {systems}')
        self._os = new_os

    @property
    def processor(self) -> str:
        return self._processor

    @processor.setter
    def processor(self, new_processor: str) -> None:
        self.is_str(new_processor)
        if not new_processor.lower().startswith(self.__processor_types):
            types = ' or '.join(self.__processor_types)
            raise ValueError(f'Processor name should starts with {types}')
        self._processor = new_processor


class Monitor(Product):
    __con_types = ('usb', 'hdmi', 'thunderbolt', 'vga', 'display port', 'dvi')

    def __init__(self, name: str, price: int | float, size: int | float, con_type: str) -> None:
        self.size = size
        self.con_type = con_type
        super().__init__(name, price)

    @property
    def size(self) -> int | float:
        return self._size

    @size.setter
    def size(self, new_size: int | float) -> None:
        self.is_int_or_float(new_size)
        self._size = new_size

    @property
    def con_type(self) -> str:
        return self._con_type

    @con_type.setter
    def con_type(self, new_con_type: str) -> None:
        self.is_str(new_con_type)
        if new_con_type.lower() not in self.__con_types:
            types = ', '.join(self.__con_types)
            raise ValueError(f'Wrong value for connection_type. Supported: {types}')
        self._con_type = new_con_type


class Shop:
    def __init__(self, product_list: tuple[Product] | list[Product]) -> None:
        self.product_list = product_list

    def is_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            product_type = type(product).__name__
            err_message = f'{product} should be Product not {product_type}'
            raise TypeError(err_message)

    @property
    def product_list(self) -> list[Product]:
        return self._product_list

    @product_list.setter
    def product_list(self, new_product_list: tuple[Product] | list[Product]) -> None:
        if not isinstance(new_product_list, (tuple, list)):
            list_type = type(new_product_list).__name__
            err_message = f'{new_product_list} should be tuple or list not {list_type}'
            raise TypeError(err_message)
        for product in new_product_list:
            self.is_product(product)
        self._product_list = list(new_product_list)

    def add_product(self, product: Product) -> None:
        self.is_product(product)
        self._product_list.append(product)

    def remove_product(self, product: Product) -> None:
        self.is_product(product)
        self._product_list.remove(product)

    def get_all_products(self) -> list[Product]:
        return self._product_list


pc = Computer('gig', 12, 'WINDOWS', 'AMg')
