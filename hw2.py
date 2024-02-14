"""Process client data analyze emails and last login and save statistics in JSON file."""

import json
from datetime import datetime

online_duration = {
    'Less than 2 days': 0,
    'Less than 1 week': 0,
    'Less than 1 month': 0,
    'Less than 6 months': 0,
    'More than 6 months': 0,
    }

LEN_MONTH = 30
LEN_HALF_YEAR = 180
hosts_count = {}


class EmptyFileError(Exception):
    """Exception raised when a JSON file is empty.

    Attributes:
        message -- explanation of the error
    """

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


def host_counter(email: str) -> None:
    """Count the number of hosts.

    Args:
        email (str): The counted host.
    """
    _, host = email.split('@')
    hosts_count[host] = hosts_count.get(host, 0) + 1


def online_count(days_since_last_login: int) -> None:
    """Count the number of online duration.

    Args:
        days_since_last_login (int): The last login.
    """
    if days_since_last_login < 2:
        online_duration['Less than 2 days'] += 1
    elif days_since_last_login < 7:
        online_duration['Less than 1 week'] += 1
    elif days_since_last_login < LEN_MONTH:
        online_duration['Less than 1 month'] += 1
    elif days_since_last_login < LEN_HALF_YEAR:
        online_duration['Less than 6 months'] += 1
    else:
        online_duration['More than 6 months'] += 1


def hosts_percents(total_clients: int) -> None:
    """Calculate the percentage of each host item based on the total number of clients.

    Parameters:
        total_clients (int): The total number of clients.

    Raises:
        EmptyFileError: If the total_clients is 0, which would lead to a division by zero error.
    """
    try:
        for host_item in hosts_count.items():
            hosts_count[host_item[0]] = host_item[1] / total_clients * 100
    except ZeroDivisionError:
        raise EmptyFileError()


def process_data(input_file_path: str, output_file_path: str) -> None:
    """
    Process data about site clients and writes statistics to a JSON file.

    Args:
        input_file_path (str): Path to the JSON file with customer data.
        output_file_path (str): Path to the JSON file output.

    Raises:
        EmptyFileError: If the file is empty.
    """
    data_json = load_file(input_file_path)

    total_clients = len(data_json)

    for client in data_json.values():
        email = client.get('email')
        if email:
            host_counter(email)

        last_login = client.get('last_login')
        if last_login:
            online_count((datetime.now().date() - datetime.fromisoformat(last_login).date()).days)

    hosts_percents(total_clients)

    try:
        for online_item in online_duration.items():
            online_duration[online_item[0]] = online_item[1] / total_clients * 100
    except ZeroDivisionError:
        raise EmptyFileError()

    export_file(output_file_path, {
        'hosts_count': hosts_count,
        'online_duration': online_duration,
    })
