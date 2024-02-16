"""Functions for processing data about clients."""
import json
from datetime import date

TEENAGER = 18
MIDDLE = 25
NOT_OLD = 45
OLD = 60


def get_the_age(age: int) -> str:
    """
    Return the age group for the given age.

    Args:
        age (int): Age of the client.

    Returns:
        str: Age group.
    """
    if age < TEENAGER:
        return '0-18'
    elif age < MIDDLE:
        return '18-25'
    elif age < NOT_OLD:
        return '25-45'
    elif age < OLD:
        return '45-60'
    return '60+'


def statistics_by_age(input_dict: dict) -> dict:
    """
    Calculate age statistics for the given input dictionary and return a dictionary.

    Args:
        input_dict (dict): Dictionary with client data.

    Returns:
        dict: Dictionary with age statistics.
    """
    age_stats = {}
    for user in input_dict.keys():
        age = input_dict[user]['age']
        age_group = get_the_age(age)
        age_stats[age_group] = age_stats.get(age_group, 0) + 1
    return age_stats


def last_entrance(last_login_str: str) -> str:
    """
    Return the last login group for the given last login string.

    Args:
        last_login_str (str): Last login of the client.

    Returns:
        str: Last login group.
    """
    half_year = 180
    month = 30
    week = 7
    date_today = date.today()
    last_login_date = date.fromisoformat(last_login_str)
    quantity = date_today - last_login_date
    if quantity.days < 2:
        return 'less 2 days'
    elif quantity.days < week:
        return 'less 1 week'
    elif quantity.days < month:
        return 'less 1 month'
    elif quantity.days < half_year:
        return 'less half year'
    return 'above half year'


def last_entrance_stats(input_dict: dict) -> dict:
    """
    Calculate last login statistics for the given input dictionary and return a dictionary.

    Args:
        input_dict (dict): Dictionary with client data.

    Returns:
        dict: Dictionary with last login statistics.
    """
    last_login = {}
    for user in input_dict.keys():
        last_login_str = input_dict[user]['last_login']
        last_login_group = last_entrance(last_login_str)
        last_login[last_login_group] = last_login.get(last_login_group, 0) + 1
    return last_login


def process_data(input_file: str, output_file: str) -> str:
    """
    Read data from the input file, calculate statistics, and write the results to the output file.

    Args:
        input_file: JSON file with client data.
        output_file: JSON file to store the calculated statistics.

    Returns:
        str: Error message or success confirmation.
    """
    try:
        with open(input_file, 'r') as input_data:
            input_dict = json.load(input_data)
    except FileNotFoundError:
        return f'file {input_file} does not exist!'
    except json.decoder.JSONDecodeError:
        return f'file {input_file} is not in JSON format!'

    stats = {
        'age_stats': statistics_by_age(input_dict),
        'last_login_stats': last_entrance_stats(input_dict),
    }
    try:
        with open(output_file, 'w') as output_data:
            json.dump(stats, output_data, indent=3)
    except FileNotFoundError:
        return f'invalid file path {output_file}'
    except PermissionError:
        return f'not permission to write to file {output_file}'
    return 'The prograp was completed without errors.'
