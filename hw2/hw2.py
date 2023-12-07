"""Module that includes the implemented function from Nudga's second task."""
import json
from datetime import datetime, timedelta

import module_hw2


def get_online_intervals(data_login: list[str]) -> list[str]:
    """
    Calculate online intervals based on login data.

    Args:
        data_login (list): List of login data.

    Returns:
        dict: Dictionary containing online intervals.
    """
    t_intervals = [
        datetime.now() - datetime.strptime(login, '%Y-%m-%d')
        for login in data_login
        ]
    online_intervals = {
        '<2 d': len(list(filter(
            lambda dt: dt < timedelta(days=2), t_intervals,
            ),
            ),
            ),
        '<1 w': len(list(filter(
            lambda dt: timedelta(days=2) <= dt < timedelta(weeks=1), t_intervals,
            ),
            ),
            ),
        '<1 m': len(list(filter(
            lambda dt: timedelta(weeks=1) <= dt < timedelta(weeks=4), t_intervals,
            ),
            ),
            ),
        '<6 m': len(list(filter(
            lambda dt: timedelta(weeks=4) <= dt < timedelta(weeks=24), t_intervals,
            ),
            ),
            ),
        '>6 m': len(list(filter(
            lambda dt: timedelta(weeks=24) < dt, t_intervals,
            ),
            ),
            ),
    }
    if t_intervals:
        total_count = len(t_intervals)
        for time_key in online_intervals.keys():
            online_intervals[time_key] = round(online_intervals[time_key] / total_count * 100, 1)
    return online_intervals


def create_output_file(result_json: dict, path: str) -> None:
    """
    Write the result JSON to an output file.

    Args:
        result_json (dict): Result data.
        path (str): File path to write the output JSON.
    """
    with open(path, 'w') as output_file:
        json.dump(result_json, output_file, indent=4)


def get_data(input_data: dict) -> tuple[list[int], list[str]]:
    """
    Extract age and login data from input data.

    Args:
        input_data (dict): Input data in dictionary format.

    Returns:
        tuple: Tuple containing lists of age and login data.
    """
    data_age = [
        json_values.get('age')
        for json_values in input_data.values()
        if json_values.get('age')
        ]
    data_login = [
        json_values.get('last_login')
        for json_values in input_data.values()
        if json_values.get('last_login')
        ]

    for age in data_age:
        if not isinstance(age, int):
            data_age.remove(age)
    for login in data_login:
        if not isinstance(login, str):
            data_login.remove(login)
    return data_age, data_login


def process_data(input_path: str, output_path: str) -> None:
    """
    Process input data, calculate statistics, and write to the output file.

    Args:
        input_path (str): Path of the input file.
        output_path (str): Path of the output file.
    """
    if module_hw2.check_errors(input_path, output_path):
        return

    with open(input_path) as input_file:
        input_data = json.load(input_file)

    if not isinstance(input_data, dict):
        module_hw2.handle_error('Type of the data should be dict')
        return

    data_age, data_login = get_data(input_data)
    online_intervals = get_online_intervals(data_login)

    result_json = {
        'min age': min(data_age) if data_age else 0,
        'max age': max(data_age) if data_age else 0,
        'avg age': int(sum(data_age) // len(data_age)) if data_age else 0,
        'median age': int(module_hw2.median_age(data_age)),
        '< 2 days': online_intervals['<2 d'],
        '< 1 week': online_intervals['<1 w'],
        '< 1 month': online_intervals['<1 m'],
        '< 6 months': online_intervals['<6 m'],
        '> 6 months': online_intervals['>6 m'],
    }
    create_output_file(result_json, path=module_hw2.check_output_extension(output_path))
