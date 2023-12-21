"""Module in which the process_data function creates statistics."""
import json
import os
from collections import Counter
from datetime import datetime
from statistics import mean, median

INTERVALS = (0, 2, 7, 14, 31, 92, 186, float('inf'))
INTERVAL_NAMES = (
    'Less than 2 days ago',
    '2 days ago',
    '1 weeks ago',
    '2 weeks ago',
    '1 month ago',
    '3 months ago',
    '6 months ago',
)


def check_file(input_file: str, output_file: str) -> None | str:
    """Check if the input and output files exist.

    Args:
        input_file: The path to the input JSON file containing user data
        output_file: The path to the output JSON file where processed data will be saved

    Returns:
        str if input_file is not a file.
    """
    if not os.path.isfile(input_file):
        return f'{input_file} is not a file'
    if not os.path.isfile(output_file):
        out_directory = os.path.dirname(output_file)
        if not os.path.exists(out_directory):
            os.makedirs(out_directory, exist_ok=True)


def get_datafile(data_in: str) -> dict:
    """
    Retrieve data from a JSON file.

    Args:
        data_in (str): The path to the JSON file.

    Returns:
        dict: The data loaded from the JSON file.
    """
    with open(data_in, 'r') as data_file:
        try:
            datafile = json.load(data_file)
        except json.JSONDecodeError:
            return 'Input file is empty'
    return datafile


def get_age(datafile: dict) -> dict:
    """
    Calculate statistics for ages in a dictionary of user data.

    Args:
        datafile: dict: A dictionary containing user data.

    Returns:
        return dict: a dictionary containing the calculate statistics for ages,
        including the mean age, maximum age, and median age.
    """
    ages = []
    for user_data in datafile.values():
        user_age = user_data.get('age', None)
        if isinstance(user_age, int):
            ages.append(user_age)
    if not ages:
        return 'Error'
    mean_age = round(mean(ages), 2)
    max_age = max(ages)
    median_age = round(median(ages), 2)
    return {
        'mean age': mean_age,
        'max age': max_age,
        'median age': median_age,
    }


def is_valid_date(date: str) -> bool:
    """
    Check if the given date is valid and not in the future.

    Parameters:
        date (str): The date to be checked in the format 'YYYY-MM-DD'.

    Returns:
        return True if the date is valid and not in the future else False
    """
    if not date:
        return 'Error, date is not found'
    try:
        date = datetime.fromisoformat(date)
    except ValueError:
        return f"Date '{date}' does not match the format 'YYYY-MM-DD'."
    if date > datetime.now():
        return f'{date} is in the future.'
    return date


def get_login_data(datafile: dict) -> dict:
    """
    Create the login data from a dictionary of data and returns a list of last login dates.

    Parameters:
        datafile (dict): A dictionary containing the login data.

    Returns:
        return dict: A dict of datetime objects representing the last login dates.
    """
    last_login_stats = []

    for last_login_data in datafile.values():
        last_login = last_login_data.get('last_login')
        date = is_valid_date(last_login)
        if not isinstance(date, datetime):
            return date
        last_login_stats.append(date)

    return last_login_stats


def get_login_stats(datafile: dict) -> dict:
    """
    Calculate the login statistics based on the given datafile.

    Parameters:
        datafile (dict): A dictionary containing login data.

    Returns:
        dict: A dictionary containing the login statistics.
    """
    last_logins = get_login_data(datafile)
    if isinstance(last_logins, str):
        return last_logins
    days_since_last_login = [(datetime.now() - login_date).days for login_date in last_logins]
    login_stats = Counter()

    for days in days_since_last_login:
        for index, inter in enumerate(INTERVALS[:-1]):
            if inter <= days < INTERVALS[index + 1]:
                login_stats[INTERVAL_NAMES[index]] += 1
                break

    if not login_stats:
        return 'Login statistic is empty'

    return {interval: (count / len(last_logins)) * 100 for interval, count in login_stats.items()}


def process_data(data_in: str, data_out: str) -> None | str:
    """
    Process the input data and write the combined data to the output file.

    Args:
        data_in (str): The path to the input data file.
        data_out (str): The path to the output file.

    Returns:
        Error message

    """
    file_check = check_file(data_in, data_out)
    if isinstance(file_check, str):
        return file_check
    datafile = get_datafile(data_in)
    if not isinstance(datafile, dict):
        return datafile
    combined_data = {}
    login_stats = get_login_stats(datafile)
    if isinstance(login_stats, str):
        return login_stats
    age_statistic = get_age(datafile)
    if isinstance(age_statistic, str):
        return age_statistic
    combined_data.update(login_stats)
    combined_data.update(age_statistic)

    with open(data_out, 'w') as json_file:
        json.dump(combined_data, json_file, indent=4)
