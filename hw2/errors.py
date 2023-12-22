"""File with custom errors and error processing."""
import sys


class PathError(Exception):
    """
    Exception raised for errors in the input path.

    Attributes:
        path (str): The path that caused the error.
    """

    def __init__(self, path: str) -> None:
        """
        Initialize the PathError exception with a specific file path.

        Args:
            path (str): The path of the file that does not exist.
        """
        super().__init__(f'File with path: {path} is not exist')


class ExtensionError(Exception):
    """
    Exception raised for errors in the file extension.

    Attributes:
        extension (str): The actual extension of the file.
        expected (str): The expected extension of the file.
    """

    def __init__(self, extension: str, expected: str) -> None:
        """
        Initialize the ExtensionError exception with the file extension and the expected extension.

        Args:
            extension (str): The actual extension of the file.
            expected (str): The expected extension for the file.
        """
        super().__init__(f'File must be {expected}, but got {extension}')


def print_error(path_to_file: str, text: str) -> None:
    """
    Write an error message to a file and then exit the program.

    Args:
        path_to_file (str): Path to the file where the error message will be written.
        text (str): Error message to be written.
    """
    with open(path_to_file, 'w') as file_to_write:
        file_to_write.write(text)
    sys.exit()
