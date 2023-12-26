"""
Functions for processing data about clients.

This module contains functions for processing data about clients, calculating statistics related
to their age and last login dates, and writing the results to an output file.

Attributes:
    MONTH: An integer representing the number of days in a month (assumed as 30 days).
    HALF_YEAR: An integer representing the number of days in half a year (assumed as 180 days).

Constants:
    LESS_THAN_TWO_DAYS: String constant representing the label for the category of users
    who logged in less than 2 days ago.
    LESS_THAN_ONE_WEEK: String constant representing the label for the category of users
    who logged in less than 1 week ago.
    LESS_THAN_ONE_MONTH: String constant representing the label for the category of users
    who logged in less than 1 month ago.
    LESS_THAN_SIX_MONTHS: String constant representing the label for the category of users
    who logged in less than 6 months ago.
    MORE_THAN_SIX_MONTHS: String constant representing the label for the category of users
    who logged in more than 6 months ago.
"""

import json
from datetime import datetime

MONTH = 30
HALF_YEAR = 180

LESS_THAN_TWO_DAYS = 'less_than_2_days'
LESS_THAN_ONE_WEEK = 'less_than_1_week'
LESS_THAN_ONE_MONTH = 'less_than_1_month'
LESS_THAN_SIX_MONTHS = 'less_than_6_months'
MORE_THAN_SIX_MONTHS = 'more_than_6_months'


def last_login_date(user_info: dict) -> datetime:
    """
    Get the last login date from user_info.

    Args:
        user_info: A dictionary representing the user's information.

    Returns:
        datetime: The last login date as a datetime object.

    If the last login date is not available or in an incorrect format,
    it returns the current date and time.
    """
    try:
        date = datetime.strptime(user_info.get('last_login'), '%Y-%m-%d')
    except (ValueError, TypeError):
        date = datetime.today()
    if datetime.now() < date:
        return datetime.today()
    return date


def stats_by_time(information: dict) -> dict[str, list]:
    """
    Calculate statistics based on the time since last login for users.

    Args:
        information: A dictionary containing information about the users.

    Returns:
        dict[str, list]: A dictionary containing statistics based on the time
        since last login for different user groups.
    """
    time_stats = {
        LESS_THAN_TWO_DAYS: [],
        LESS_THAN_ONE_WEEK: [],
        LESS_THAN_ONE_MONTH: [],
        LESS_THAN_SIX_MONTHS: [],
        MORE_THAN_SIX_MONTHS: [],
    }

    for user_info in information.values():
        age = user_info.get('age')
        online = get_time_since_last_login(user_info)
        categorize_user_by_time(time_stats, online, age)

    calculate_average(time_stats)

    return time_stats


def get_time_since_last_login(user_info) -> int:
    """
    Calculate the number of days since the user's last login.

    Args:
        user_info: Information about the user.

    Returns:
        An integer representing the number of days since the user's last login.
    """
    last_login = last_login_date(user_info)
    return (datetime.now() - last_login).days


def categorize_user_by_time(time_stats: dict[str, list], online: int, age: int) -> None:
    """
    Categorizes the user based on online duration and age into different time categories.

    Args:
        time_stats: A dictionary containing time categories and corresponding age lists.
        online: An integer representing the online duration.
        age: An integer representing the user's age.
    """
    if online <= 2:
        time_stats[LESS_THAN_TWO_DAYS].append(age)
    elif 2 < online <= 7:
        time_stats[LESS_THAN_ONE_WEEK].append(age)
    elif 7 < online <= MONTH:
        time_stats[LESS_THAN_ONE_MONTH].append(age)
    elif MONTH < online <= HALF_YEAR:
        time_stats[LESS_THAN_SIX_MONTHS].append(age)
    else:
        time_stats[MORE_THAN_SIX_MONTHS].append(age)


def calculate_average(time_stats: dict[str, list]) -> None:
    """
    Calculate the average time for each time category based on the user's age.

    Args:
        time_stats: A dictionary containing time categories and corresponding age lists.
    """
    for time, quantity in time_stats.items():
        if quantity:
            time_stats[time] = round(sum(quantity) / len(quantity), 2)
        else:
            time_stats[time] = 0


def get_age_group(age: int) -> str:
    """
    Categorize the age into different groups.

    Args:
        age: An integer representing the age of a user.

    Returns:
        str: The age group to which the user belongs.

    The function categorizes the age into different groups such
    as '0-18', '18-25', '25-45', '45-60', and '60+'.
    """
    first_group = 18
    second_group = 25
    third_group = 45
    last_group = 60

    if age < first_group:
        return '0-18'
    elif age < second_group:
        return '18-25'
    elif age < third_group:
        return '25-45'
    elif age < last_group:
        return '45-60'
    return '60+'


def get_age_stats(input_dict: dict) -> dict:
    """
    Calculate statistics based on the age of users.

    Args:
        input_dict: A dictionary containing information about the users.

    Returns:
        dict: A dictionary containing statistics based on the age of users.

    This function calculate the number of users in different age groups and returns the statistics.
    """
    age_stats = {
        '0-18': 0,
        '18-25': 0,
        '25-45': 0,
        '45-60': 0,
        '60+': 0,
    }
    for user in input_dict.values():
        age = user['age']
        age_group = get_age_group(age)
        age_stats[age_group] += 1
    return age_stats


def process_data(input_file: str, output_file: str) -> str:
    """
    Read data from input_file, calculate stats, and write it to output_file.

    Args:
        input_file: A string representing the path to the JSON file with data about clients.
        output_file: A string representing the path to the JSON file
        where the stats will be written.

    Returns:
        A string message indicating the completion of the program or an error.
    """
    try:
        with open(input_file, 'r') as input_file_data:
            input_dict = json.load(input_file_data)
    except FileNotFoundError:
        return f'file {input_file} does not exist!'
    except json.decoder.JSONDecodeError:
        return f'file {input_file} is not in JSON format!'

    time_stats = stats_by_time(input_dict)

    stats = {
        'age_stats': get_age_stats(input_dict),
        'time_stats': time_stats,
    }
    try:
        with open(output_file, 'w') as output_file_data:
            json.dump(stats, output_file_data, indent=4)
    except FileNotFoundError:
        return f'invalid file path {output_file}'
    except PermissionError:
        return f'not permission to write to file {output_file}'
    return 'The program was completed without errors.'
