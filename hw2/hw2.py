"""
hw2 module.

Напишите модуль, в котором функция process_data принимает
путь к json-файлу с данными о клиентах сайта (пример файла в data_hw2.json)
и путь к json-файлу вывода. Функция process_data
записывает в этот общий json статистику: процент распределения географии
пользователей по городам, а также процент клиентов, которые были онлайн:
менее двух дней, недели, месяца, полугода, и более полугода назад.
Вынести домашнее и его тесты в отдельную папку hw2.
Тесты используют различные json-файлы. В workflows выделить
отдельные работы для проверок линтера разных домашних,
отдельные работы для тестов разных домашних
(цель состоит в том, чтобы в actions они отображались отдельными галочками).
"""

import json
import os
from datetime import datetime
from typing import Optional as Op

LESS_TWO_DAYS = 'less_than_two_days'
LESS_WEEK = 'less_than_a_week'
LESS_MONTH = 'less_than_a_month'
LESS_HALF_YEAR = 'less_than_half_a_year'
MORE_THAN_HALF_YEAR = 'more_than_half_a_year'
TWO_DAYS = 2
WEEK = 7
MONTH = 30
HALF_YEAR = 180


def process_data(input_path: str, output_path: str, today: Op[datetime]) -> None:
    """
    Process the data from the input file and create a JSON file with calculated statistics.

    Args:
        input_path (str): The path to the input file.
        output_path (str): The path to the output JSON file.
        today (optional): The current date and time. Defaults to datetime.now().

    Raises:
        FileNotFoundError: If the input file is not found.
    """
    folder_path = os.path.dirname(output_path)
    if folder_path != '' and not os.path.exists(folder_path):
        os.makedirs(folder_path)
    try:
        _create_json(_make_percentages(*_calculate_statistics(input_path, today)), output_path)
    except FileNotFoundError:
        raise FileNotFoundError('File not found')


def _calculate_statistics(json_file: str, today: datetime) -> tuple:
    """
    Calculate statistics based on the data in the given JSON file.

    Args:
        json_file (str): The path to the JSON file containing user data.
        today (datetime): The current date and time.

    Returns:
        tuple: A tuple containing the data, the city distribution and the online distribution.
    """
    with open(json_file, 'r') as j_file:
        datafile = json.load(j_file)

    city_distrib = _calculate_city_distribution(datafile)
    online_distrib = _calculate_online_distribution(datafile, today)
    return datafile, city_distrib, online_distrib


def _calculate_city_distribution(datafile: dict) -> dict:
    """
    Calculate the distribution of cities based on the data in the given JSON file.

    Args:
        datafile (dict): A dictionary containing user data.

    Returns:
        dict: A dictionary containing the distribution of cities.
    """
    city_distrib = {}

    for user in datafile.values():
        city = user['region']
        if city not in city_distrib:
            city_distrib[city] = 0
        city_distrib[city] += 1

    return city_distrib


def _calculate_online_distribution(datafile: dict, today: datetime) -> dict:
    """
    Calculate the distribution of online periods based on the data in the given JSON file.

    Args:
        datafile (dict): A dictionary containing user data.
        today (datetime): The current date and time.

    Returns:
        dict: A dictionary containing the distribution of online periods.
    """
    online_distrib = {
        LESS_TWO_DAYS: 0,
        LESS_WEEK: 0,
        LESS_MONTH: 0,
        LESS_HALF_YEAR: 0,
        MORE_THAN_HALF_YEAR: 0,
    }

    for user in datafile.values():
        days_since_online = _calculate_days_since_online(user, today)
        _update_online_distribution(online_distrib, days_since_online)

    return online_distrib


def _calculate_days_since_online(user: dict, today: datetime) -> int:
    """
    Calculate the number of days since the user was last online.

    Args:
        user (dict): A dictionary containing user information, including the 'last_login' date.
        today (datetime): The current date and time.

    Returns:
        int: The number of days since the user was last online.
    """
    last_online = datetime.strptime(user['last_login'], '%Y-%m-%d')
    return (today - last_online).days


def _update_online_distribution(online_distrib: dict, days_since_online: int) -> None:
    """
    Update the online distribution based on the given number of days.

    Args:
        online_distrib (dict): A dictionary containing the online distribution.
        days_since_online (int): The number of days since the user was last online.
    """
    if days_since_online < TWO_DAYS:
        online_distrib[LESS_TWO_DAYS] += 1
    elif days_since_online < WEEK:
        online_distrib[LESS_WEEK] += 1
    elif days_since_online < MONTH:
        online_distrib[LESS_MONTH] += 1
    elif days_since_online < HALF_YEAR:
        online_distrib[LESS_HALF_YEAR] += 1
    else:
        online_distrib[MORE_THAN_HALF_YEAR] += 1


def _make_percentages(datafile: dict, city_distrib, online_distrib) -> dict:
    """
    Create a dictionary with the percentages of each city and online period.

    Args:
        datafile (dict): A dictionary containing user data.
        city_distrib (dict): A dictionary containing the city distribution.
        online_distrib (dict): A dictionary containing the online distribution.

    Returns:
        dict: A dictionary with the percentages of each city and online period.
    """
    users = len(datafile)
    city_distrib = {city: cnt / (users or 1) * 100 for city, cnt in city_distrib.items()}
    online_distrib = {period: cnt / (users or 1) * 100 for period, cnt in online_distrib.items()}
    return {**city_distrib, **online_distrib}


def _create_json(datafile: dict, output_file: str) -> None:
    """
    Create a JSON file with the given data.

    Args:
        datafile (dict): The data to be written to the JSON file.
        output_file (str): The path of the output JSON file.
    """
    with open(output_file, 'w') as o_file:
        json.dump(datafile, o_file, indent=4)
