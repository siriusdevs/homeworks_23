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
        self._os = new_os

    @property
    def processor(self) -> str:
        return self._processor

    @processor.setter
    def processor(self, new_processor: str) -> None:
        self.is_str(new_processor)
        self._processor = new_processor


class Monitor(Product):
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
        self._con_type = new_con_type
