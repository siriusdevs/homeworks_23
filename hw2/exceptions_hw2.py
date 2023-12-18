"""Provides exceptions for hw2."""


class InputFilepathError(Exception):
    """Error that is thrown when the file could not be read."""

    def __init__(self, filepath: str) -> None:
        """Initialize the exception.

        Args:
            filepath (str): path to file.
        """
        super().__init__(f'Path {filepath} does not exist.')


class MissingFieldError(Exception):
    """Error that is thrown when one of the users missing a field."""

    def __init__(self, fld: str) -> None:
        """Initialize the exception.

        Args:
            fld (str): field name.
        """
        super().__init__(f'"{fld}" field does not exist. Every user should have "{fld}" field.')


class InvalidDateFormatError(Exception):
    """Error that is thrown when date format in field is not correct."""

    def __init__(self, got_format: str) -> None:
        """Initialize the exception.

        Args:
            got_format (str): date format.
        """
        super().__init__(f'Wrong date format, expected format: 2020-12-30, but got {got_format}.')


class InvalidJSONFormatError(Exception):
    """Error that is thrown when JSON structure is not correct."""

    def __init__(self, filepath: str) -> None:
        """Initialize the exception.

        Args:
            filepath (str): path to file.
        """
        super().__init__(f'An incorrect json file structure was found at path {filepath}.')


class EmptyJSONError(Exception):
    """Error that is thrown when was given empty json file."""

    def __init__(self, filepath: str) -> None:
        """Initialize the exception.

        Args:
            filepath (str): path to file.
        """
        super().__init__(f'Empty json file was found at path {filepath}.')
