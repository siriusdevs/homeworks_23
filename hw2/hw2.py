"""Module in which the process_data function creates statistics."""
import json
from datetime import datetime
from statistics import mean, median

import const


def get_datafile(data_in: str) -> dict:
    """
    Retrieve data from a JSON file.

    Args:
        data_in (str): The path to the JSON file.

    Returns:
        dict: The data loaded from the JSON file.
    """
    with open(data_in, 'r') as data_file:
        datafile = json.load(data_file)
    return datafile


def get_age(datafile: dict) -> dict:
    """
    Calculate statistics for ages in a dictionary of user data.

    Args:
        datafile: dict: A dictionary containing user data.

    Returns:
        return dict: a dictionary containing the calculated statistics for ages,
        including the mean age, maximum age, and median age.

    Raises:
        ValueError: If any of the ages in the datafile are not integers.
    """
    ages = [user['age'] for user in datafile.values() if isinstance(user['age'], int)]

    if not ages:
        raise ValueError('File dont have a number for age statistic')

    stats_age = {
        'mean age': round(mean(ages), 2),
        'max age': max(ages),
        'median age': round(median(ages), 2),
    }

    return stats_age


def is_valid_date(date: str) -> bool:
    """
    Check if the given date is valid and not in the future.

    Parameters:
        date (str): The date to be checked in the format 'YYYY-MM-DD'.

    Raises:
        ValueError: If date does not match the format 'YYYY-MM-DD' or is in the future.

    Returns:
        return True if the date is valid and not in the future, False otherwise.
    """
    if not date:
        return False
    try:
        date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError(f"Date '{date}' does not match the format 'YYYY-MM-DD'.")
    if date > datetime.now():
        raise ValueError(f'{date} is in the future.')
    return True


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
        if last_login and is_valid_date(last_login):
            last_login = datetime.strptime(last_login, '%Y-%m-%d')
            last_login_stats.append(last_login)

    return last_login_stats


def get_login_stats(datafile: dict) -> dict:
    """
    Calculate the login statistics based on the given datafile.

    Parameters:
        datafile (dict): A dictionary containing login data.

    Returns:
        dict: A dictionary containing the login statistics.
    """
    login_stats = {interval_name: 0 for interval_name in const.LoginCategories}
    for last_login in get_login_data(datafile):
        days_since_login = (datetime.now() - last_login).days
        for index, interval_days in const.IntervalsCounter.INTERVALS:
            if days_since_login <= interval_days:
                login_stats[const.LoginCategories.INTERVAL_NAME[index]] += 1

    total_users = len(get_login_data(datafile))

    if total_users == 0:
        return login_stats

    for user_data, user_stat in login_stats.items():
        login_stats[user_data] = round(user_stat / total_users * 100, 2)

    return login_stats


def process_data(data_in: str, data_out: str) -> None:
    """
    Process the input data and write the combined data to the output file.

    Args:
        data_in (str): The path to the input data file.
        data_out (str): The path to the output file.

    """
    datafile = get_datafile(data_in)

    combined_data = {
        'login_stats': get_login_stats(datafile),
        'stats_age': get_age(datafile),
    }

    with open(data_out, 'w') as json_file:
        json.dump(combined_data, json_file, indent=4)
