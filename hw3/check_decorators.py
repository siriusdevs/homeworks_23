"""Module with decorators, that check types."""


from typing import Any, Type


def check_type(var_name, var_value, correct_type: Type[Any]) -> None:
    """Check type of variable.

    Args:
        var_name: variable name
        var_value: variable value
        correct_type: type that must be variable

    Raises:
        TypeError: if type is not correct_type
    """
    if not isinstance(var_value, correct_type):
        correct_type = correct_type.__name__
        value_type = type(var_value).__name__
        full_name = f'{var_name} ({var_value})'

        raise TypeError(f'{full_name} must be {correct_type} type, not {value_type} type')


def check_list_types(list_name, list_values, correct_type: Type[Any]) -> None:
    """Check type of variable with list type.

    Args:
        list_name: variable (list) name
        list_values: variable (list) values
        correct_type: type that must be all elements of list
    """
    check_type(list_name, list_values, list)
    for list_value in list_values:
        check_type(f'{list_name} element', list_value, correct_type)
