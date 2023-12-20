"""Process client data, analyze emails and last login, and save statistics in JSON file."""

import json
from datetime import datetime

online_duration = {
    'Less than 2 days': 0,
    'Less than 1 week': 0,
    'Less than 1 month': 0,
    'Less than 6 months': 0,
    'More than 6 months': 0,
    }

len_month = 30
len_half_year = 180
hosts_count = {}


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
    elif days_since_last_login < len_month:
        online_duration['Less than 1 month'] += 1
    elif days_since_last_login < len_half_year:
        online_duration['Less than 6 months'] += 1
    else:
        online_duration['More than 6 months'] += 1


def process_data(input_file_path: str, output_file_path: str) -> None:
    """
    Process data about site clients and writes statistics to a JSON file.

    Args:
        input_file_path (str): Path to the JSON file with customer data.
        output_file_path (str): Path to the JSON file output.
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

    for host_item in hosts_count.items():
        hosts_count[host_item[0]] = host_item[1] / total_clients * 100

    for onlene_item in online_duration.items():
        online_duration[onlene_item[0]] = onlene_item[1] / total_clients * 100

    export_file(output_file_path, {
        'hosts_count': hosts_count,
        'online_duration': online_duration,
    })
