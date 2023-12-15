"""Module for processing data."""


import json

from app_exceptions import NotFoundAgeException
from user_statistic import UserStatistic


def process_data(input: str, output: str) -> None:
    """Take data and writes the statictic by age and registrations by years to the json file.

    Args:
        input (str): the path where the json comes from.
        output (str): path where json is saved.

    Raises:
        NotFoundAgeException: raise exception if we don't find 'age' in users.
    """
    users = get_users_from_json(input)
    try:
        ages = [user['age'] for user in users.values()]
    except KeyError:
        raise NotFoundAgeException('The paramers "age" is not found.')

    check_ages_type(ages)

    stats = get_years_statistic(users)

    user_stats = UserStatistic(ages, stats).to_json()

    with open(output, 'w+') as file:
        file.write(user_stats)


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
        with open(path) as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise ValueError(f'The file with path: {path} is not found!')
    except json.decoder.JSONDecodeError:
        raise ValueError(f'The file: {file.name} is not valid!')


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

    Returns:
        dict: The statistic of registered users by years
    """
    all_count = len(users)
    stats = {}
    for user in users.values():
        date = user['registered']
        stats[date] = stats.get(date, 0) + 1

    stats = {year: ratio(count, all_count) for year, count in stats.items()}

    return stats


def ratio(figure: int | float, to_figure: int | float):
    """Get the ratio one figure to other figure.

    Args:
        figure (int | float): the number whose difference we will check
        to_figure (int | float): From what date will we look at the ratio

    Returns:
        float: The ratio one figure to other figure
    """
    return round(figure / to_figure * 100, 2)
