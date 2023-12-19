"""Module for main exceptions."""


class NotFoundAgeException(Exception):
    """Exception for age if it is not found."""

    def __init__(self) -> None:
        """init."""
        super().__init__('The parametr <age> is not found!')
