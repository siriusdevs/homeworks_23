"""Class architecture for managing a computer hardware store."""


class Product:
    def __init__(self, name: str, price: int | float) -> None:
        self.name = name
        self.price = price

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            type_name = type(new_name).__name__
            err_message = f'{new_name} should be str not {type_name}'
            raise TypeError(err_message)
        self._name = new_name

    @property
    def price(self) -> int | float:
        return self._price

    @price.setter
    def price(self, new_price: int | float) -> None:
        if not isinstance(new_price, (int, float)):
            type_name = type(new_price).__name__
            err_message = f'{new_price} should be int or float not {type_name}'
            raise TypeError(err_message)
        self._price = new_price
