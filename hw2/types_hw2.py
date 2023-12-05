"""Provides custom types for hw2."""


from typing import Any

JsonDict = dict[str, Any]
TimeFilterType = str


class InvalidInputFileException(Exception):
    """Exception that occurs when reading provided input file as JSON failed."""

    def __init__(self, filepath: str) -> None:
        """Initialize the exception.

        Args:
            filepath (str): input file path provided by user
        """
        super().__init__(self, f'Не удалось прочитать файл {filepath} как JSON')


class InvalidDateException(Exception):
    """Exception that occurs when one of the users has a date field in invalid format."""

    def __init__(self, got_date: str, want_format: str) -> None:
        """Initialize the exception.

        Args:
            got_date (str): the date read from json
            want_format (str): the expected format
        """
        super().__init__(self, f'Неверная дата: "{got_date}". Ожидается формат "{want_format}"')


class MissingFieldException(Exception):
    """Exception that occurs when one of the users is missing a field."""

    def __init__(self, field: str) -> None:
        """Initialize the exception.

        Args:
            field: missing field name
        """
        super().__init__(self, f'У каждого из пользователей должно быть поле "{field}"')
