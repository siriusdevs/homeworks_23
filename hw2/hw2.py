"""Module for writing statistics to a json file."""


import json

import check_functions as check
from operations_functions.compilation_statistic_functions import get_data

USER = 'user'
REGION = 'region'
REGISTERED = 'registered'
LAST_LOGIN = 'last_login'
EMAIL = 'email'
AGE = 'age'


def read_json(input_file_path: str) -> dict:
    """Read data from the input json file.

    Args:
        input_file_path (str): path to the input json file.

    Returns:
        dict: users data from the json file.
    """
    check.check_file_path(input_file_path)
    check.check_emptiness_file(input_file_path)
    with open(input_file_path, 'r') as input_file:
        input_data = json.load(input_file)
        for user_data in input_data.values():
            check.check_file_format(user_data)
        check.check_input_data(input_data)
        return input_data


def write_to_json(output_file_path: str, output_data: dict) -> None:
    """Write statistics about the ages and logins of users to the output json file.

    Args:
        output_file_path (str): path to the output json file.
        output_data (dict): statistics about ages and last logins of users.
    """
    check.check_file_path(output_file_path)
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        json.dump(output_data, output_file, ensure_ascii=False, indent=4)


def write_output_data(input_data: dict) -> dict:
    """Get data on the ages and last logins of users and return statistics on this data.

    Args:
        input_data (dict): users data from the json file.

    Returns:
        dict: statistics about ages and last logins of users.
    """
    if not len(input_data):
        return {}
    users_ages = []
    users_last_logins = []
    for user_data in input_data.values():
        users_ages.append(user_data.get(AGE))
        users_last_logins.append(user_data.get(LAST_LOGIN))
    return get_data(users_ages, users_last_logins)


def process_data(input_file_path: str, output_file_path: str) -> None:
    """Read data from the input json file and write statistics about the ages and \
        logins of users to the output json file.

    Args:
        input_file_path (str): path to the input json file.
        output_file_path (str): path to the output json file.
    """
    input_data = read_json(input_file_path)
    output_data = write_output_data(input_data)

    write_to_json(output_file_path, output_data)
