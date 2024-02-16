"""Module with percentage of usage of each mail host and of user registrations by year."""

import json
import os
from pathlib import Path


def write_file(file_path: str, writable_data: str):
    """
    Write errors to output file.

    Args:
        file_path (str): The path to the output file.
        writable_data (str): Writable data.
    """
    path = Path(file_path)
    if not path.exists():
        os.makedirs(path.parent)
    with open(file_path, 'w') as output_file:
        output_file.write(writable_data)


def process_data(input_file_path: str, output_file_path: str):
    """
    Process data from the input file and write the result to the output file.

    Args:
        input_file_path (str): The path to the input file path.
        output_file_path (str): The path to the output file path.

    Raises:
        FileNotFoundError: If input file not found.
        ValueError: If input file is incorrect.
    """
    try:
        with open(input_file_path, 'r') as input_file:
            input_data = json.load(input_file)
    except FileNotFoundError:
        write_file(output_file_path, 'Input file not found!')
        raise FileNotFoundError(f'Input file {input_file_path} not found!')
    except json.JSONDecodeError:
        write_file(output_file_path, 'File is not json!')
        raise ValueError(f'File {input_file_path} is not json')

    if not input_data:
        write_file(output_file_path, 'Received empty data')
        raise ValueError('Received empty data')

    email_host_percentages = calculate_email_host(input_data)
    registration_year_percentages = calculate_registration_year(input_data)

    percentages = {
        'email_host_percentages': email_host_percentages,
        'registration_year_percentages': registration_year_percentages,
    }
    if not os.path.exists(os.path.dirname(output_file_path)):
        os.makedirs(os.path.dirname(output_file_path))
    with open(output_file_path, 'w') as output_file:
        json.dump(percentages, output_file, indent=4)


def calculate_email_host(clients_data: dict) -> dict:
    """
    Calculate percentage of usage of each mail host in client mails.

    Args:
        clients_data (dict): The value to check.

    Returns:
        dict: percentage of usage of each mail host in client mails.
    """
    email_hosts = {}
    for client_data in clients_data.values():
        if 'email' not in client_data:
            continue
        email_host = client_data['email'].split('@')[1]
        if email_host not in email_hosts:
            email_hosts[email_host] = 0
        email_hosts[email_host] += 1

    return {
        host: (count / len(clients_data)) * 100 for host, count in email_hosts.items()
    }


def calculate_registration_year(data_dict: dict) -> dict:
    """
    Calculate percentage of user registrations by year.

    Args:
        data_dict (dict): The value to check.

    Returns:
        dict: percentage of user registrations by year.
    """
    registration_years = {}
    for client_data in data_dict.values():
        if 'registered' not in client_data:
            continue
        registration_year = client_data['registered'].split('-')[0]
        if registration_year not in registration_years:
            registration_years[registration_year] = 0
        registration_years[registration_year] += 1

    return {
        year: (count / len(data_dict)) * 100 for year, count in registration_years.items()
    }
