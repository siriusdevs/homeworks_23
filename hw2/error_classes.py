"""Module with custom errors."""


import sys

import multi_util as utils


class NonExistentField:
    """Custom error, calls if field isn't exists."""

    def __init__(self, client: str, field: str, output_path: str) -> None:
        """Initialize error for non existent field.

        Args:
            client: str - client name
            field: str name of non existent field
            output_path: str - file to write error.
        """
        message = f'{field} field does not exists for client {client}.'
        utils.write(message, output_path)


class EmptyField:
    """Custom error, calls if field is empty."""

    def __init__(self, client: str, field: str, output_path: str) -> None:
        """Initialize error for empty field.

        Args:
            client: str - client name.
            field: str name of non existent field.
            output_path: str - file to write error.
        """
        message = f'{field} field is empty for client {client}.'
        utils.write(message, output_path)


class EmailError:
    """Custom error, calls if email is incorrect."""

    def __init__(self, client: str, output_path: str) -> None:
        """Initialize error for email address without host name.

        Args:
            client: str - client name.
            output_path: str - file to write error.
        """
        message = f'Wrong email address: empty host name for client {client}.'
        utils.write(message, output_path)


class NoInputFile:
    """Custom error, calls if input file not exists."""

    def __init__(self, input_file: str, output_path: str) -> None:
        """Initialize error for non existent input file.

        Args:
            input_file: str - unexistent file.
            output_path: str - file to write error.
        """
        message = f'File {input_file} does not exists. Processing is not possible.'
        utils.write(message, output_path)


class ListNotExpected:
    """Custom error, calls if in input file appear list."""

    def __init__(self, output_path: str) -> None:
        """Initialize error for list in input file.

        Args:
            output_path: str - file to write error.
        """
        message = 'List not expected in input file.'
        utils.write(message, output_path)
