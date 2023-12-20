"""Additional module for hw3."""
from typing import Callable, Iterable


def ensure(attr: str, funcs: Iterable[Callable]) -> Callable:
    """
    Add property with specified checks to a class.

    Args:
        attr (str): Name of the attribute.
        funcs (Iterable[Callable]): List of functions to check the attribute.

    Returns:
        Callable: Decorator function.
    """
    def add_property(class_name: type) -> type:
        """
        Add property to a class.

        Args:
            class_name (type): Class to which property is added.

        Returns:
            type: Class with added property.
        """
        def getter(self):
            """
            Getter method for the property.

            Args:
                self: self.

            Returns:
                Any: The value of the property.
            """
            return getattr(self, f'_{attr}')

        def setter(self, input_value):
            """
            Setter method for the property.

            Args:
                self: self.
                input_value: The value to set for the property.
            """
            for func in funcs:
                func(input_value)
            setattr(self, f'_{attr}', input_value)

        setattr(class_name, attr, property(getter, setter))
        return class_name
    return add_property


def check_int(input_value):
    """
    Check if the value is an integer.

    Args:
        input_value: Value to be checked.

    Raises:
        TypeError: If the value is not an integer.
    """
    if not isinstance(input_value, int):
        raise TypeError('Value is expected to be int.')


def check_float(input_value):
    """
    Check if the value is an integer or float.

    Args:
        input_value: Value to be checked.

    Raises:
        TypeError: If the value is not an integer or float.
    """
    if not isinstance(input_value, (float, int)):
        raise TypeError('Value is expected to be int or float.')


def check_positive(input_value):
    """
    Check if the value is positive.

    Args:
        input_value: Value to be checked.

    Raises:
        ValueError: If the value is not positive.
    """
    if input_value < 0:
        raise ValueError('Value is expected to be positive.')


def check_str(input_value):
    """
    Check if the value is a string.

    Args:
        input_value: Value to be checked.

    Raises:
        TypeError: If the value is not a string.
    """
    if not isinstance(input_value, str):
        raise TypeError('Name is expected to be str.')
