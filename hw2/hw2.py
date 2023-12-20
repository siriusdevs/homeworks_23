"""Module for calculating the last login of users and the percentage of email hosts."""

import json
from datetime import datetime
from typing import Any

import error_classes as errors
import multi_util as utils


def call_change_counter(
    online_status_count: dict[str: int],
    output_path: str,
    json_data: Any,
        ) -> None:
    """Call change_counter for every client.

    Args:
        online_status_count: dict[str: int] - variable with statuses.
        output_path: str - path for write.
        json_data: Any - loaded json.

    Raises:
        ListNotExpected: raises if program meets list in input file.
    """
    try:
        for client, client_info in json_data.items():
            change_counter(online_status_count, client, client_info, output_path)
    except AttributeError:
        raise errors.ListNotExpected(output_path)


def get_last_login(client: str, client_info: dict, output_path: str) -> str:
    """Find client email host.

    Args:
        client: str - client name.
        client_info: dict - info about client: region, registered, last_login, email, age.
        output_path: str - file to write.

    Returns:
        str: last login date.

    Raises:
        NonExistentField: raises if the last_login field does not exist.
        EmptyField: raises if the last_login field are empty.
    """
    try:
        last_login = client_info['last_login']
    except KeyError:
        raise errors.NonExistentField(client, 'last_login', output_path)
    if not last_login:
        raise errors.EmptyField(client, 'last_login', output_path)
    return last_login


def get_host(client: str, client_info: dict, output_path: str) -> str:
    """Find client email host.

    Args:
        client: str - client name.
        client_info: dict - info about client: region, registered, last_login, email, age.
        output_path: str - file to write

    Returns:
        str: name of email host.

    Raises:
        EmailError: calls if email haven't @ symbol.
        NonExistentField: raises if the email field does not exist.
        EmptyField: raises if the email field are empty.
    """
    try:
        host = client_info['email'].split('@')[1]
    except IndexError:
        raise errors.EmailError(client, output_path)
    except KeyError:
        raise errors.NonExistentField(client, 'email', output_path)
    if not host:
        raise errors.EmptyField(client, 'email', output_path)
    return host


def get_hosts_count(json_data: Any, output_path: str) -> dict:
    """Count the number of different hosts.

    Args:
        json_data: Any - loaded json file.
        output_path: str - file to write

    Returns:
        dict: email host and the number of times it appears among users.
    """
    hosts_count = {}
    for client, client_info in json_data.items():
        host = get_host(client, client_info, output_path)
        hosts_count[host] = hosts_count.get(host, 0) + 1
    return hosts_count


def fill_hosts_percentage(json_data: Any, output_path: str, hosts_percentage: dict) -> None:
    """Fill meets percantage for every host.

    Args:
        json_data: Any - loaded json.
        output_path: str - file to write.
        hosts_percentage: dict - hosts and meet percentage.
    """
    for host_name, count in get_hosts_count(json_data, output_path).items():
        hosts_percentage[host_name] = round((count / len(json_data)) * 100, 2)


def change_counter(
    online_status_count: dict[str: int],
    client: str,
    client_info: dict,
    output_path: str,
        ) -> None:
    """Change online status counter using last login ago.

    Args:
        online_status_count: dict[str: int] - list with online statisctic.
        client: str - client name.
        client_info: dict - info about client: region, registered, last_login, email, age.
        output_path: str - file to write
    """
    date = datetime.strptime(get_last_login(client, client_info, output_path), '%Y-%m-%d')
    last_login_ago = (datetime.now() - date).days
    two_days = 2
    week = 7
    month = 30
    six_months = month * 6
    if last_login_ago < two_days:
        online_status_count['less_than_2_days'] += 1
    elif last_login_ago < week:
        online_status_count['less_than_a_week'] += 1
    elif last_login_ago < month:
        online_status_count['less_than_a_month'] += 1
    elif last_login_ago < (six_months):
        online_status_count['less_than_six_months'] += 1
    else:
        online_status_count['more_than_six_months'] += 1


def process_data(input_path: str, output_path: str) -> None:
    """Process the input_path and write statistics to output_path.

    Args:
        input_path: str - file with data for process.
        output_path: str - file to write statistics.
    """
    online_status_count = {
        'less_than_2_days': 0,
        'less_than_a_week': 0,
        'less_than_a_month': 0,
        'less_than_six_months': 0,
        'more_than_six_months': 0,
    }
    hosts_percentage = {}
    try:
        with open(input_path, 'r') as input_file:
            json_data = json.load(input_file)
    except FileNotFoundError:
        errors.NoInputFile(input_path, output_path)
        return
    except json.JSONDecodeError:
        utils.write('', output_path)
        return
    try:
        call_change_counter(online_status_count, output_path, json_data)
    except Exception:
        return
    try:
        fill_hosts_percentage(json_data, output_path, hosts_percentage)
    except Exception:
        return
    utils.write((online_status_count, hosts_percentage), output_path)
