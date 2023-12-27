"""Module with custom exceptions."""


class FileIsNotJsonError(Exception):
    """Error that is thrown if the file has a extension other than .json."""

    def __init__(self, file_path: str) -> None:
        """Initialize the exception.

        Args:
            file_path (str): path to the file.
        """
        super().__init__(f'The file on the path {file_path} has a extension other than .json')


class FileIsEmptyError(Exception):
    """Error that is thrown if the file is empty."""

    def __init__(self, file_path: str) -> None:
        """Initialize the exception.

        Args:
            file_path (str): path to the file.
        """
        super().__init__(f'The file on the path {file_path} is empty')
