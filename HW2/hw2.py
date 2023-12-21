"""Module with percentage of usage of each mail host and of user registrations by year."""

import json
import os


def process_data(input_file_path: str, output_file_path: str):
    """
    Process data from the input file and write the result to the output file.

    Args:
        input_file_path (str): The path to the input file path.
        output_file_path (str): The path to the output file path.

    Returns:
        0 - all good work
        'Input file not found!' - input_file_path  not found
        'File is not json' - input_file_path is not a valid json file
        'No write permission' - output_file_path is not writable
    """
    try:
        with open(input_file_path, 'r') as input_file:
            input_data = json.load(input_file)
    except FileNotFoundError:
        return 'Input file not found!'
    except json.JSONDecodeError:
        return 'File is not json'

    email_host_percentages = calculate_email_host(input_data)
    registration_year_percentages = calculate_registration_year(input_data)

    percentages = {
        'email_host_percentages': email_host_percentages,
        'registration_year_percentages': registration_year_percentages,
    }
    if not os.path.exists(os.path.dirname(output_file_path)):
        os.makedirs(os.path.dirname(output_file_path))
    try:
        with open(output_file_path, 'w') as output_file:
            json.dump(percentages, output_file, indent=4)
    except PermissionError:
        return 'No write permission'


def calculate_email_host(data_dict: dict) -> dict:
    """
    Calculate percentage of usage of each mail host in client mails.

    Args:
        data_dict (dict): The value to check.

    Returns:
        dict: percentage of usage of each mail host in client mails.
    """
    email_hosts = {}
    total_emails = 0

    for client in data_dict.keys():
        try:
            if 'email' not in data_dict[client].keys():
                return 'Email key not found'
        except KeyError:
            return 'Email key not found'

        email_domain = data_dict[client]['email'].split('@')[1]
        email_hosts[email_domain] = email_hosts.get(email_domain, 0) + 1
        total_emails += 1

    return {
        host: (count / total_emails) * 100 for host, count in email_hosts.items()
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
    total_users = len(data_dict.keys())

    for client in data_dict.keys():
        try:
            if 'registered' not in data_dict[client].keys():
                return 'Registered key not found'
        except KeyError:
            return 'Registered key not found'

        registration_year = data_dict[client]['registered'].split('-')[0]
        registration_years[registration_year] = registration_years.get(registration_year, 0) + 1

    return {
        year: (count / total_users) * 100 for year, count in registration_years.items()
    }


# Пример использования:
if __name__ == '__main__':
    process_data('./HW2/input/data_hw2.json', './aaaa/aaaaa/aaaa/a.json')
