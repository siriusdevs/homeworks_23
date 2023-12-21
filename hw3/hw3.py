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
