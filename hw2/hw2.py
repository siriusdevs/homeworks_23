"""Module for processing data."""


import json
import os
from typing import Callable

from app_exceptions import NotFoundAgeException
from user_statistic import UserStatistic


def exceptions_to_json(function: Callable) -> None:
    """Convert exceptions to json.

    Args:
        function (Callable): function.

    Returns:
        None: returns function-wrapper
    """
    def wrapper(*args):
        try:
            function(*args)
        except (TypeError, NotFoundAgeException, ValueError) as error:
            error_message = json.dumps({'error': str(error)})
            write_json(args[1], error_message)
    return wrapper


@exceptions_to_json
def process_data(input_path: str, output_path: str) -> None:
    """Take data and writes the statictic by age and registrations by years to the json file.

    Args:
        input_path (str): the path where the json comes from.
        output_path (str): path where json is saved.

    Raises:
        NotFoundAgeException: raise exception if we don't find 'age' in users.
    """
    users = get_users_from_json(input_path)
    try:
        ages = [user['age'] for user in users.values()]
    except KeyError:
        raise NotFoundAgeException('The parametr <age> is not found.')

    check_ages_type(ages)

    stats = get_years_statistic(users)

    user_stats = UserStatistic(ages, stats).to_json()

    write_json(output_path, user_stats)


def write_json(output: str, message: any) -> None:
    """Write json with message to output.

    Args:
        output (str): The place where we save json file.
        message (any): Some data which we write.
    """
    if not os.path.exists(output):
        os.mkdir('test_data_hw2')
    with open(output, 'w+') as output_file:
        output_file.write(message)


def get_users_from_json(path: str) -> dict:
    """Get users from the json file.

    Args:
        path (str): The path to json file

    Raises:
        ValueError: raise this exception if file is incorrect

    Returns:
        dict: The dict of users
    """
    try:
        with open(path) as users_file:
            return json.load(users_file)
    except FileNotFoundError:
        raise ValueError(f'The file with path: {path} is not found!')
    except json.decoder.JSONDecodeError:
        raise ValueError(f'The file with path: {path} is not valid!')


def check_ages_type(ages: list):
    """Check type of ages.

    Args:
        ages (list): Checking ages

    Raises:
        TypeError: raise exception if age is not int
    """
    for age in ages:
        if not isinstance(age, int):
            raise TypeError('All ages must be <int> !')


def get_years_statistic(users: list[dict]) -> dict:
    """Get statistic registered users by years.

    Args:
        users (list[dict]): list of users

    Raises:
        ValueError: raise excepton if a field "registered": is not found

    Returns:
        dict: The statistic of registered users by years
    """
    all_count = len(users)
    stats = {}
    try:
        for user in users.values():
            date = user['registered']
            stats[date] = stats.get(date, 0) + 1
    except KeyError:
        raise ValueError('The parametr <registered> is not found.')

    return {year: ratio(count, all_count) for year, count in stats.items()}


def ratio(figure: int | float, to_figure: int | float):
    """Get the ratio one figure to other figure.

    Args:
        figure (int | float): the number whose difference we will check
        to_figure (int | float): From what date will we look at the ratio

    Returns:
        float: The ratio one figure to other figure
    """
    return round(figure / to_figure * 100, 2)
