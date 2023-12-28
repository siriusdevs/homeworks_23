"""Module with custom exceptions."""

from typing import Any


class VariableHasInvalidWriteFormat(Exception):
    """Error that is thrown if the variable has an invalid write format."""

    def __init__(self, var_name: str, var_value: Any) -> None:
        """Initialize the exception.

        Args:
            var_name (str): name of the variable.
            var_value (Any): value of the variable.
        """
        super().__init__(f'The {var_name} with value <{var_value}> has an invalid write format')
