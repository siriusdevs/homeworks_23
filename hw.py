from typing import Any
def chech_type(value: Any, type_: Any) -> bool:
    """Check type of value"""
    if not isinstance(value, type_):
        raise ValueError(f'Value must be {type_}')

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    
    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self, value):
        chech_type(value, float)
        if value < 0:
            raise ValueError('Price must be positive')
        self._price = value
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value):
        chech_type(value, str)
        self._name = value
    