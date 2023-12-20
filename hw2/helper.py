"""help functions module"."""
import json
import sys
from math import ceil
from os import getcwd
from pathlib import Path
from typing import Any

import dateparser

DAYS_CONST = 60 * 60 * 24
DIRECTORY = 'hw2/test_data_hw2/'


def opener(path_in: str) -> dict[str, dict]:
    """Json file opener.

    Args:
        path_in (str): path to file

    Returns:
        dict[str, dict]: read data
    """
    try:
        with open(path_in, 'r') as data_file:
            clients = json.loads(data_file.read())
    except FileNotFoundError as notfoundmsg:
        write_to_json(f'{DIRECTORY}error_log.json', str(notfoundmsg))
        sys.exit(1)
    except json.decoder.JSONDecodeError as jsonerrormsg:
        write_to_json(f'{DIRECTORY}error_log.json', str(jsonerrormsg))
        sys.exit(1)
    return clients


def write_to_json(path_out: str, data_or_error: dict[str, dict] | Any):
    """Write data to json.

    Args:
        path_out (str): path to output file
        data_or_error (dict[str, dict] | Any): calculated stats, or error message
    """
    try:
        with open(path_out, 'w') as output_file:
            json.dump(data_or_error, fp=output_file, indent=4)
    except FileNotFoundError as notfoundmsg:
        sys.stdout.write('{0} is exists: {1}'.format(DIRECTORY, str(Path(DIRECTORY).exists())))
        write_to_json(getcwd(), notfoundmsg)
        sys.exit(1)


def get_dispersion(user: dict[str, str | int]) -> int:
    """Parse date to days between register and last login.

    Args:
        user (dict[str, str  |  int]): single user information

    Returns:
        int: days between register and last login
    """
    try:
        registered, last_login = dateparser.parse(user['registered']), \
            dateparser.parse(user['last_login'])
    except KeyError:
        return 0
    return ceil((last_login.timestamp() - registered.timestamp()) / DAYS_CONST)
