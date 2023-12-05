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
