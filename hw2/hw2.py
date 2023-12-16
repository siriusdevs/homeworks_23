"""Module for calculating the last login of users and the percentage of email hosts."""

import json
import sys
from datetime import datetime
from typing import Any

import error_classes as errors
import multi_util as utils


def get_last_login(client: str, client_info: dict, output_path: str) -> str:
    """Find client email host.

    Args:
        client: str - client name.
        client_info: dict - info about client: region, registered, last_login, email, age.
        output_path: str - file to write

    Returns:
        str: last login date.
    """
    try:
        last_login = client_info['last_login']
    except KeyError:
        errors.NonExistentField(client, 'last_login', output_path)
    if not last_login:
        errors.EmptyField(client, 'last_login', output_path)
    return last_login


def get_host(client: str, client_info: dict, output_path: str) -> str:
    """Find client email host.

    Args:
        client: str - client name.
        client_info: dict - info about client: region, registered, last_login, email, age.
        output_path: str - file to write

    Returns:
        str: name of email host.
    """
    try:
        host = client_info['email'].split('@')[1]
    except IndexError:
        errors.EmailError(client, output_path)
    except KeyError:
        errors.NonExistentField(client, 'email', output_path)
    if not host:
        errors.EmptyField(client, 'email', output_path)
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


def change_online_status_counter(
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
    json_data = None
    try:
        with open(input_path, 'r') as input_file:
            json_data = json.load(input_file)
    except FileNotFoundError:
        errors.NoInputFile(input_path, output_path)
    except json.JSONDecodeError:
        utils.write('', output_path)
        sys.exit()
    try:
        for client, client_info in json_data.items():
            change_online_status_counter(online_status_count, client, client_info, output_path)
    except AttributeError:
        errors.ListNotExpected(output_path)
    for host_name, count in get_hosts_count(json_data, output_path).items():
        hosts_percentage[host_name] = round((count / len(json_data)) * 100, 2)
    utils.write((online_status_count, hosts_percentage), output_path)
