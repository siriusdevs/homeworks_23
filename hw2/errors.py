"""Provides custom exceptions."""


class InvalidFilePathException(Exception):
    """Exception that occurs if reading JSON by not existing path."""

    def __init__(self, file_path: str) -> None:
        """Initialize the exception.

        Args:
            file_path (str): input file path provided by user
        """
        super().__init__(f'Not found file by path {file_path}. Check if such file of path exists')


class JSONIncorrectFieldFormat(Exception):
    """Exception that occurs if format of field is incorrect."""

    def __init__(self, field_value: str, correct_format: str) -> None:
        """Initialize the exception.

        Args:
            field_value (str): field's string that is incorrect
            correct_format (str): correct format of string
        """
        super().__init__(f'Incorrect {field_value} format. User {correct_format}')


class JSONMissingFieldException(Exception):
    """Excpetion that occurs if JSON does not have provided field."""

    def __init__(self, field: tuple[str]) -> None:
        """Initialize the exception.

        Args:
            field (tuple[str]): the missing field(s) in JSON.
        """
        super().__init__(f"Cannot find reference of '{field}' in data")
