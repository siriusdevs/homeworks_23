"""help functions module"."""
import json
from math import ceil

import dateparser

DAYS_CONST = 60 * 60 * 24


def opener(path_in: str) -> dict[str, dict]:
    """Json file opener.

    Args:
        path_in (str): path to file

    Raises:
        ValueError: file not found error
        ValueError: file is not valid (ex. invalid syntax)

    Returns:
        dict[str, dict]: read data
    """
    try:
        with open(path_in, 'r') as data_file:
            clients = json.loads(data_file.read())
    except FileNotFoundError:
        raise ValueError(f'file <{path_in}> not found')
    except json.decoder.JSONDecodeError:
        raise ValueError(f'file <{path_in}> is not valid')
    return clients


def writer(path_out: str, stats: dict[str, dict]):
    """Write data to json.

    Args:
        path_out (str): path to output file
        stats (dict[str, dict]): calculated stats

    Raises:
        ValueError: file not found error
    """
    try:
        with open(path_out, 'w') as output_file:
            json.dump(stats, fp=output_file, indent=4)
    except FileNotFoundError:
        raise ValueError(f'file <{path_out}> not found')


def parser(user: dict[str, str | int]) -> int:
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
