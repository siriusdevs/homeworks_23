"""Homework №2. Module for processing data.

Напишите модуль, в котором функция process_data принимает путь к json-файлу
с данными о клиентах сайта (пример файла в data_hw2.json) и путь к json-файлу вывода.
Функция process_data записывает в этот общий json статистику: процент распределения географии
пользователей по городам, а также средний возраст клиентов, которые были онлайн менее двух дней,
недели, месяца, полугода, и более полугода назад. Вынести домашнее и его тесты в отдельную папку
hw2. Тесты используют различные json-файлы. В workflows выделить отдельные работы для проверок
линтера разных домашних, отдельные работы для тестов разных домашних (цель состоит в том,
чтобы в actions они отображались отдельными галочками).
"""
import json
import os
import re
from datetime import datetime, timedelta
from typing import Any

LESS_TWO_DAYS = 2, 'active_in_last_two_days_average_age'
LESS_WEEK = 1, 'active_in_last_week_average_age'
LESS_MONTH = 30, 'active_in_last_month_average_age'
LESS_HALF_YEAR = 180, 'active_in_last_half_year_average_age'
GREATER_HALF_YEAR = 'active_for_more_than_half_year_average_age'


class InvalidFilePath(Exception):
    """Invalid file path exception."""

    def __init__(self, path_to_file: str) -> None:
        """Initialize an exception.

        Args:
            path_to_file: str - the path to  the file that does not open.
        """
        super().__init__(f'file {path_to_file} does not exist.')


def _aggregate_users_stats(input_path: str, output_path: str) -> None:
    try:
        with open(input_path, 'r') as input_json:
            users = json.load(input_json)
    except FileNotFoundError:
        raise InvalidFilePath(input_path)

    users_stat = get_regions_stat(users)

    cur_date = datetime.now()

    dates = [
        (timedelta(days=LESS_TWO_DAYS[0]), LESS_TWO_DAYS[1]),
        (timedelta(weeks=LESS_WEEK[0]), LESS_WEEK[1]),
        (timedelta(days=LESS_MONTH[0]), LESS_MONTH[1]),
        (timedelta(days=LESS_HALF_YEAR[0]), LESS_HALF_YEAR[1]),
    ]
    dates = [(cur_date - date[0], date[1]) for date in dates]
    users_stat.update(filter_users_by_dates(users, dates))

    with open(output_path, 'w') as output_json:
        json.dump(users_stat, output_json)


def process_data(path_to_input_json: str, path_to_output_json: str) -> None:
    """Process user data.

    Args:
        path_to_input_json: str - the path to the json file with users.
        path_to_output_json: str - the path to the file where the processed data is saved.
    """
    os.makedirs(os.path.abspath(os.path.dirname(path_to_output_json)), exist_ok=True)
    try:
        _aggregate_users_stats(path_to_input_json, path_to_output_json)
    except Exception as error:
        with open(path_to_output_json, 'w') as output_json:
            json.dump({'error': '{0}: {1}'.format(type(error).__name__, error)}, output_json)


def _check_date(date: str) -> None:
    if not re.match(r'\d{4}-\d{2}-\d{2}', date):
        raise ValueError(f'Incorrect date format - {date}. Use YYYY-MM-DD')


def to_datetime(date: str) -> datetime:
    """Convert string to datetime object.

    Args:
        date: str - date that write as str.

    Returns:
        datetime object
    """
    _check_date(date)
    return datetime(*list(map(int, date.split('-'))))


def _check_age(age: int) -> None:
    if not isinstance(age, int):
        raise TypeError(f'age "{age}" should be int')
    if age < 0:
        raise ValueError(f'age {age} should be positive')


def get_avg_age(users: dict[str, Any]) -> float | None:
    """Calculate average age of users.

    Args:
        users: dict[str, Any] - json file with users.

    Returns:
        float: average age of users.
    """
    all_ages, ages_summ = 0, 0
    for users_data in users.values():
        if 'age' in users_data:
            _check_age(users_data.get('age'))
            ages_summ += users_data.get('age')
            all_ages += 1
    if all_ages == 0:
        return None
    return ages_summ / all_ages


def filter_users_by_dates(
    users: dict[str, Any], dates: list[tuple[datetime, str]],
) -> dict[str, Any]:
    """Filter users by given dates.

    Args:
        users: dict[str, Any] - json file with users.
        dates: list[tuple[datetime, str]] - a list of dates by which users should be filtered.

    Returns:
        dict[str, Any]: filtered user dictionary.
    """
    filtered_users = {date[1]: {} for date in dates}
    filtered_users[GREATER_HALF_YEAR] = {}

    for name, user_data in users.items():
        if 'last_login' not in user_data:
            continue

        user_date = to_datetime(user_data['last_login'])
        fl = True
        for date in dates:
            if date[0] <= user_date:
                filtered_users[date[1]][name] = user_data
                fl = False

        if fl:
            filtered_users[GREATER_HALF_YEAR][name] = user_data

    return {
        time_flag: get_avg_age(users_data)
        for time_flag, users_data in filtered_users.items()
    }


def get_regions_stat(users: dict[str, Any]) -> dict[str, float]:
    """Get statistics of distribution by region.

    Args:
        users: dict[str, Any] - json file with users.

    Returns:
        dict[str, float]: distribution by city as a percentage.
    """
    regions = {}

    cnt_regions = 0
    for user_data in users.values():
        if 'region' not in user_data:
            continue

        user_region = user_data['region']
        regions[user_region] = regions[user_region] + 1 if user_region in regions else 1
        cnt_regions += 1

    return {
        region_name: cnt_region / cnt_regions * 100
        for region_name, cnt_region in regions.items()
    }
