"""Module with check functions."""


import os.path

import hw2_exceptions

USER = 'user'
REGION = 'region'
REGISTERED = 'registered'
LAST_LOGIN = 'last_login'
EMAIL = 'email'
AGE = 'age'

valid_user_chars = [REGION, REGISTERED, LAST_LOGIN, EMAIL, AGE]
len_valid_user_chars = len(valid_user_chars)


def check_file_format(user_data: dict) -> None:
    """Check the validly of the format of the data in a json file.

    Args:
        user_data (dict): names and values of user characteristicsы.

    Raises:
        TypeError: if the user_data is not a dict.
        TypeError: if the user_char is not an int or str.
    """
    if not isinstance(user_data, dict):
        type_name = type(user_data).__name__
        raise TypeError(f'{user_data} should be dict, not {type_name}')
    for user_char in user_data.values():
        if not isinstance(user_char, int | str):
            type_name = type(user_char).__name__
            raise TypeError(f'{user_char} should be int or str, not {type_name}')


def check_file_path(file_path: str) -> None:
    """Check the validly of the file path.

    Args:
        file_path (str): path to the file.

    Raises:
        TypeError: if the file path is not a str.
        FileIsNotJsonError: if the file has a extension other than .json.
        FileNotFoundError: if the file was not found.
    """
    if not isinstance(file_path, str):
        type_name = type(file_path).__name__
        raise TypeError(f'file_path should be str, not {type_name}')
    if not file_path.endswith('.json'):
        raise hw2_exceptions.FileIsNotJsonError(file_path)
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f'The file on the path {file_path} was not found')


def check_emptiness_file(file_path: str) -> None:
    """Check the file for emptiness.

    Args:
        file_path (str): path to the file.

    Raises:
        FileIsEmptyError: if the file is empty.
    """
    if os.stat(file_path).st_size == 0:
        raise hw2_exceptions.FileIsEmptyError(file_path)


def check_input_data(input_data: dict) -> None:
    """Check the validly of the input data from json file.

    Args:
        input_data (dict): users data from the json file.
    """
    for user_data in input_data.values():
        user_chars_names = user_data.keys()
        user_chars = list(user_data.values())
        check_user_chars_names(user_chars_names)
        check_user_chars(user_chars)


def check_user_chars_names(user_chars_names: list) -> None:
    """Check the validly of the user characteristics names from input data.

    Args:
        user_chars_names (list): user characteristics names.

    Raises:
        IndexError: if the number of user characteristics is not equal to len_valid_chars.
        ValueError: if user characteristic name has an invalid name.
    """
    if len(user_chars_names) != len_valid_user_chars:
        raise IndexError(f'The number of user characteristics should be {len_valid_user_chars}')
    for number, user_char_name in enumerate(user_chars_names):
        if user_char_name != valid_user_chars[number]:
            raise ValueError(f'{user_char_name} should be called {valid_user_chars[number]}')


def check_user_chars(user_chars: list) -> None:
    """Check the validly of the user characteristics from input data.

    Args:
        user_chars (list): user characteristics.

    Raises:
        TypeError: if the user_char is not a str.
        TypeError: if the user_chars[-1] is not an int.
    """
    for user_char in user_chars[:-1]:
        if not isinstance(user_char, str):
            type_name = type(user_char).__name__
            raise TypeError(f'{user_char} should be str, not {type_name}')
    last_user_char = user_chars[-1]
    if not isinstance(last_user_char, int):
        type_name = type(last_user_char).__name__
        raise TypeError(f'{last_user_char} should be int, not {type_name}')
