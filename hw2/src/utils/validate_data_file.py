"""Contain functions for validating file with users data."""
import json
from typing import NoReturn

import msgspec

from hw2.src import bbtypes, schemas

from .common import get_valid_dict_to_str

# Built-in interpreter errors and text messages for them
builtin_error_messages: dict[BaseException, str] = {
    FileNotFoundError: 'Invalid path to data file',
    PermissionError: 'You don`t have permission to read the data file',
}


def validate_data_file(data_file_path: str) -> tuple[bool, str | None]:
    """Validate data file.

    Args:
        data_file_path (str): path to file we need to check.

    Returns:
        whether the file is valid and error message if not
    """
    error_msg = None
    try:
        with open(data_file_path, 'r') as data_file:
            users_data = json.load(data_file)
            _validate_users_from_data_file(
                users_data=users_data,
            )

    # handling built-in interpreter errors
    except (FileNotFoundError, PermissionError) as builtin_error:
        builtin_error_msg = builtin_error_messages[builtin_error.__class__]
        error_msg = f'{builtin_error_msg} ({data_file_path})'

    # handling errors from built-in libs
    except json.JSONDecodeError:
        error_msg = f'Invalid JSON file provided ({data_file_path})'

    # handling errors from external libs
    except msgspec.ValidationError as ve:
        error_msg = f'Validation error for user items in data file ({data_file_path}): {ve}'

    # If there is no error message the file passed validation
    return error_msg is None, error_msg


def _validate_users_from_data_file(users_data: bbtypes.Users) -> NoReturn:
    """Validate  all the user data dicts using msgspec \
    and returns users as list of the class-models.

    Args:
        users_data (Users): the dict where the keys are the user's name and \
        the value is a dict of the User model attributes
    """
    for user_data in users_data.values():
        msgspec.json.decode(
            get_valid_dict_to_str(user_data).encode(),
            type=schemas.User,
        )
