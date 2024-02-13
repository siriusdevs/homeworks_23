"""A module with extra functions for hw2."""
import os
from datetime import date
from typing import Any

TWO_DAYS = 2
WEEK = 7
MONTH = 30
HALFYEAR = 180


def check_paths(input_path: str, output_path: str) -> None:
    """
    Check the file paths for errors.

    Args:
        input_path (str): Input path to JSON file.
        output_path (str): Outpu path to JSON file.

    Raises:
        ValueError: If transferred a non-existent file.
        ValueError: If the file contains nothing.
        TypeError: If the input file is in the wrong extension.
    """
    if not os.path.exists(input_path):
        raise ValueError('Input file does not exist.')
    if os.stat(input_path).st_size == 0:
        raise ValueError('Input file is empty.')

    _, input_extension = os.path.splitext(input_path)
    _, out_extension = os.path.splitext(output_path)

    if input_extension != '.json' or out_extension != '.json':
        raise TypeError('Files do not have JSON extension.')


def process_last_login(clients: dict[str, dict[str, Any]]) -> dict:
    """
    Collect clietns statistics by last login as a percentage.

    Args:
        clients (dict[str, dict[str, Any]]): Clients data.

    Returns:
        dict: Last logins statistics.
    """
    last_login_stats = {
        'less_than_two_days': 0,
        'less_than_one_week': 0,
        'less_than_one month': 0,
        'less_than_half_year': 0,
        'more_than_half_year': 0,
    }

    count_logins = 0
    for client in clients.values():
        if 'last_login' not in client:
            continue
        client_last_login = client['last_login']
        last_login = get_last_login(client_last_login)
        last_login_stats[last_login] += 1
        count_logins += 1
    try:
        return {
            last_login: count_login / count_logins * 100
            for last_login, count_login in last_login_stats.items()
        }
    except ZeroDivisionError:
        return last_login_stats


def get_last_login(date_str: str) -> str:
    """
    Determine when the client last logged in.

    Args:
        date_str (str): Last login date.

    Returns:
        str: Clients last login.
    """
    last_login_date = date.fromisoformat(date_str)
    delta = date.today() - last_login_date
    match delta:
        case delta if delta.days <= TWO_DAYS:
            return 'less_than_two_days'
        case delta if delta.days <= WEEK:
            return 'less_than_one_week'
        case delta if delta.days <= MONTH:
            return 'less_than_one month'
        case delta if delta.days <= HALFYEAR:
            return 'less_than_half_year'
        case _:
            return 'more_than_half_year'


def process_regions(clients: dict[str, dict[str, Any]]) -> dict:
    """
    Collect clietns statistics by city as a percentage.

    Args:
        clients (dict[str, dict[str, Any]]): Clients data.

    Returns:
        dict: Clients cities.
    """
    regions = {}

    count_regions = 0
    for client in clients.values():
        if 'region' not in client:
            continue
        region = client['region']
        regions[region] = regions[region] + 1 if region in regions else 1
        count_regions += 1

    return {
        region_name: count_region / count_regions * 100
        for region_name, count_region in regions.items()
    }
