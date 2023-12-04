"""Module for calculating the last login of users and the percentage of email hosts."""

import json
from datetime import datetime
from typing import Any


class NonExistentField(Exception):
    """Custom error, calls if field isn't exists."""

    def __init__(self, client: str, field: str) -> None:
        """Initialize error for non existent field.

        Args:
            client: str - client name
            field: str name of non existent field
        """
        super().__init__(f'{field} field does not exists for client {client}.')


class EmptyField(Exception):
    """Custom error, calls if field is empty."""

    def __init__(self, client: str, field: str) -> None:
        """Initialize error for empty field.

        Args:
            client: str - client name.
            field: str name of non existent field.
        """
        super().__init__(f'{field} field is empty for client {client}.')


class EmailError(Exception):
    """Custom error, calls if email is incorrect."""

    def __init__(self, client: str) -> None:
        """Initialize error for email address without host name.

        Args:
            client: str - client name.
        """
        super().__init__(f'Wrong email address: empty host name for client {client}.')


online_status_count = {
    'less_than_2_days': 0,
    'less_than_a_week': 0,
    'less_than_a_month': 0,
    'less_than_six_months': 0,
    'more_than_six_months': 0,
}


def process_data(input_path: str, output_path: str) -> None:
    """Process the input_path and write statistics to output_path.

    Args:
        input_path: str - file with data for process.
        output_path: str - file to write statistics.
    """
    hosts_percentage = {}
    with open(input_path, 'r') as input_file:
        json_data = json.load(input_file)
    for client, client_info in json_data.items():
        change_online_status_counter(client, client_info)
    for host_name, count in get_hosts_count(json_data).items():
        hosts_percentage[host_name] = round((count / len(json_data)) * 100, 2)
    with open(output_path, 'w') as output_file:
        json.dump((online_status_count, hosts_percentage), output_file)


def get_last_login(client: str, client_info: dict) -> str:
    """Find client email host.

    Args:
        client: str - client name.
        client_info: dict - info about client: region, registered, last_login, email, age.

    Returns:
        str: last login date.

    Raises:
        NonExistentField: calls if client have not last_login field.
        EmptyField: calls if last_login field is empty.
    """
    try:
        last_login = client_info['last_login']
    except KeyError:
        raise NonExistentField(client, 'last_login')
    if not last_login:
        raise EmptyField(client, 'last_login')
    return last_login


def get_host(client: str, client_info: dict) -> str:
    """Find client email host.

    Args:
        client: str - client name.
        client_info: dict - info about client: region, registered, last_login, email, age.

    Returns:
        str: name of email host.

    Raises:
        EmailError: calls if client have not correct email.
        EmptyField: calls if at client email does not exists host name.
    """
    try:
        host = client_info['email'].split('@')[1]
    except KeyError:
        raise EmailError(client)
    if not host:
        raise EmptyField(client, 'email')
    return host


def get_hosts_count(json_data: Any) -> dict:
    """Count the number of different hosts.

    Args:
        json_data: Any - loaded json file.

    Returns:
        dict: email host and the number of times it appears among users.
    """
    hosts_count = {}
    for client, client_info in json_data.items():
        host = get_host(client, client_info)
        hosts_count[host] = hosts_count.get(host, 0) + 1
    return hosts_count


def change_online_status_counter(client: str, client_info: dict) -> None:
    """Change online status counter using last login ago.

    Args:
        client: str - client name.
        client_info: dict - info about client: region, registered, last_login, email, age.
    """
    date = datetime.strptime(get_last_login(client, client_info), '%Y-%m-%d')
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


process_data('/home/tire/Documents/Sirius_dev/homeworks_23/data_hw2.json', 'ululu.json')
