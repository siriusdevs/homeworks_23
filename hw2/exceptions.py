"""Exceptions classes for hw2."""
from datetime import date


class InvalidInputFileError(Exception):
    """Exception that causes when reading input JSON file failed."""

    def __init__(self, path: str) -> None:
        """Initialize the exception.

        Args:
            path: path to specified input JSON file
        """
        super().__init__(f'Failed to read input file {path} as JSON!')


class InvalidDateError(Exception):
    """Exception that causes when invalid date was specified based today date."""

    def __init__(self, invalid_date: date) -> None:
        """Initialize the exception.

        Args:
            invalid_date: specified date
        """
        today_date = date.strftime(date.today(), '%Y-%m-%d')
        super().__init__(f'Invalid date: {invalid_date}! Today is {today_date}.')


class InvalidDateFormatError(Exception):
    """Exception that causes when date was specified in invalid format."""

    def __init__(self, invalid_date: date) -> None:
        """Initialize the exception.

        Args:
            invalid_date: specified date
        """
        date_example = '2024-01-01 (year-month-day)'
        super().__init__(f'Invalid date format: {invalid_date}. Expected: {date_example}.')


class MissingFieldError(Exception):
    """Exception that causes when expected field was missed."""

    def __init__(self, field: str):
        """Initialize the exception.

        Args:
            field: missed field
        """
        super().__init__(f'Field {field} is missing in JSON!')
