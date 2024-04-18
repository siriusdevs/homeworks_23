"""Process client data analyze emails and last login and save statistics in JSON file."""

import json
from datetime import datetime

CALENDAR = (('lt_2_days', 2), ('lt_1_week', 7), ('lt_1_month', 30), ('lt_6_months', 180))
LEN_MONTH = 30
LEN_HALF_YEAR = 180


class InvalidAddress(Exception):
    """Exception raised when an email is not valid."""

    def __init__(self) -> None:
        """Initialize the InvalidAddress with a default error message."""
        super().__init__('The email is not valid.')


class EmptyFileError(Exception):
    """Exception raised when a JSON file is empty."""

    def __init__(self) -> None:
        """Initialize the EmptyFileError with a default error message."""
        super().__init__('The json file is empty.')


def load_file(file_name: str) -> dict:
    """Load the file.

    Args:
        file_name (str): The name of load file.

    Returns:
        dict: The file contents.
    """
    with open(file_name, 'r') as file_input:
        return json.load(file_input)


def export_file(file_name: str, data_output: dict) -> None:
    """Export the data with the file name.

    Args:
        file_name (str): The name of file.
        data_output (dict): The data for output.
    """
    with open(file_name, 'w') as file_output:
        json.dump(data_output, file_output, indent=4)


def host_counter(email: str, hosts_count: dict) -> None:
    """Count the number of hosts.

    Args:
        email (str): The counted host.
        hosts_count (dict): The counts of hosts.

    Raises:
        InvalidAddress: If the email is not valids.

    Returns:
        dict: The total number of hosts.
    """
    try:
        _, host = email.split('@')
    except Exception:
        raise InvalidAddress()
    hosts_count[host] = hosts_count.get(host, 0) + 1
    return hosts_count


def online_count(days_since_last_login: int, online_duration: dict) -> None:
    """Count the number of online duration.

    Args:
        days_since_last_login (int): The last login.
        online_duration (dict): The online duration.

    Returns:
        dict: The updated online duration.
    """
    days_since_last_login = (datetime.now().date() - days_since_last_login).days
    for category, days in CALENDAR:
        if days_since_last_login < days:
            online_duration[category] += 1
        elif category == 'lt_6_months' and days_since_last_login >= days:
            online_duration['mt_6_months'] += 1
    return online_duration


def hosts_percents(total_clients: int, hosts_count: dict) -> None:
    """Calculate the percentage of each host item based on the total number of clients.

    Parameters:
        total_clients (int): The total number of clients.
        hosts_count (dict): The counts of hosts.

    Raises:
        EmptyFileError: If the total_clients is 0, which would lead to a division by zero error.

    Returns:
        dict: The total number of hosts.
    """
    try:
        for host_item in hosts_count.items():
            hosts_count[host_item[0]] = host_item[1] / total_clients * 100
    except ZeroDivisionError:
        raise EmptyFileError()
    return hosts_count


def process_data(input_file_path: str, output_file_path: str) -> None:
    """
    Process data about site clients and writes statistics to a JSON file.

    Args:
        input_file_path (str): Path to the JSON file with customer data.
        output_file_path (str): Path to the JSON file output.

    Raises:
        EmptyFileError: If the file is empty.
    """
    online_duration = {
        'lt_2_days': 0,
        'lt_1_week': 0,
        'lt_1_month': 0,
        'lt_6_months': 0,
        'mt_6_months': 0,
        }

    hosts_count = {}

    data_json = load_file(input_file_path)

    total_clients = len(data_json)

    for client in data_json.values():
        email = client.get('email')
        if email:
            hosts_count = host_counter(email, hosts_count)

        last_login = client.get('last_login')
        if last_login:
            online_count(datetime.fromisoformat(last_login).date(), online_duration)

    hosts_count = hosts_percents(total_clients, hosts_count)

    try:
        for online_item in online_duration.items():
            online_duration[online_item[0]] = online_item[1] / total_clients * 100
    except ZeroDivisionError:
        raise EmptyFileError()

    export_file(output_file_path, {
        'hosts_count': hosts_count,
        'online_duration': online_duration,
    })
