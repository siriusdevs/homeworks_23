"""Module for exceptions."""

from typing import Any


class InvalidType(Exception):
    """Invalid type of data exception.

    Args:
        Exception (Exception): base class of exceptions
    """

    def __init__(self, new_value: Any, _type: type[Any]) -> None:
        """Initialize InvalidType.

        Args:
            new_value (Any): some value that does not match type
            _type (type[Any]): correct type
        """
        super().__init__(f'Value: <{new_value}> is not {_type}')


class NegativeNumber(Exception):
    """Negative or zero value exception.

    Args:
        Exception (Exception): base class of exceptions
    """

    def __init__(self, new_num: int) -> None:
        """Initialize NegativeNumber.

        Args:
            new_num (int): number that is negative or zero
        """
        super().__init__(f'Number: {new_num} should be positive')
