import os

from errors import ExtensionError, PathError


def check_path(path_to_file: str) -> None:
    """
    Check if the given file path points to an existing file.

    Raises:
        PathError: If the file at the given path does not exist.

    Args:
        path_to_file (str): Path to the file to check.
    """
    if not os.path.isfile(path_to_file):
        raise PathError(path_to_file)


def check_extension(path_to_file: str, extension: str) -> None:
    """
    Check if the file at the given path has the specified extension.

    Raises:
        ExtensionError: If the file's extension does not match the expected extension.

    Args:
        path_to_file (str): Path to the file to check.
        extension (str): Expected file extension.
    """
    current_extension = os.path.splitext(path_to_file)[1]
    if current_extension != extension:
        raise ExtensionError(current_extension, extension)