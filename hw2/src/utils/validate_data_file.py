"""Contain functions for validating file with users data."""
import json
from typing import NoReturn

import msgspec

from hw2.src import bbtypes, schemas

from .common import get_valid_dict_to_str


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
    except FileNotFoundError:
        error_msg = f'Invalid path to data file ({data_file_path})'
    except json.JSONDecodeError:
        error_msg = f'Invalid JSON file provided ({data_file_path})'
    except msgspec.ValidationError as ve:
        error_msg = f'Validation error for user items in data file ({data_file_path}): {ve}'

    if error_msg:
        return False, error_msg
    return True, None


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
