"""
Module for homework_2.

Напишите модуль, в котором функция process_data принимает путь к json-файлу
с данными о клиентах сайта (пример файла в data_hw2.json) и путь к json-файлу вывода.

Функция process_data записывает в этот общий json статистику:
минимальный, максимальный, средний и медианный возраст пользователя,
а также процент клиентов, которые были онлайн:
менее двух дней, недели, месяца, полугода, и более полугода назад.
"""
import json
import os
from datetime import datetime

import consts_hw2 as cnst
import exceptions_hw2

TWO_DAYS = 2
WEEK = 7
MONTH = 30
HALFYEAR = 180

ROUND_UP_TO_TWO = 2


def _median(inp_values: list[int | float]) -> int | float:
    inp_values = sorted(inp_values)
    length = len(inp_values)
    middle = length // 2
    if length % 2 == 0:
        median = (inp_values[middle - 1] + inp_values[middle]) / 2
    else:
        median = inp_values[middle]
    return round(median, ROUND_UP_TO_TWO)


def _average(inp_values: list[int | float]) -> int | float:
    return round(sum(inp_values) / max(len(inp_values), 1), ROUND_UP_TO_TWO)


def _last_login_date(user: dict) -> datetime:
    try:
        return datetime.strptime(user[cnst.LAST_LOGIN], '%Y-%m-%d')
    except KeyError:
        raise exceptions_hw2.MissingFieldError(cnst.LAST_LOGIN)
    except ValueError:
        raise exceptions_hw2.InvalidDateFormatError(user[cnst.LAST_LOGIN])


def calculate_ages_stats(users: dict) -> dict:
    """Calculate statistics of the user ages.

    Args:
        users (dict): user input from JSON file.

    Raises:
        MissingFieldError: if field does not exist.

    Returns:
        dict: statistics of user ages.
    """
    try:
        ages = [users[user][cnst.AGE] for user in users]
    except Exception:
        raise exceptions_hw2.MissingFieldError(cnst.AGE)

    ages_processed = {}
    ages_processed[cnst.AGE_MAX] = max(ages)
    ages_processed[cnst.AGE_MIN] = min(ages)
    ages_processed[cnst.AGE_AVERAGE] = _average(ages)
    ages_processed[cnst.AGE_MEDIAN] = _median(ages)

    return ages_processed


def calculate_dates_stats(users: dict) -> dict:
    """Calculate statistics of the dates of last user logins.

    Args:
        users (dict): user input from JSON file.

    Returns:
        dict: statistics of last user login, percent of total users.
    """
    last_login_dates = [_last_login_date(user) for user in users.values()]

    last_login_statistics = {
        cnst.LESS_TWO_DAYS: 0,
        cnst.LESS_WEEK: 0,
        cnst.LESS_MONTH: 0,
        cnst.LESS_HALFYEAR: 0,
        cnst.MORE_HALFYEAR: 0,
    }

    current_date = datetime.now()

    for last_login_date in last_login_dates:
        days_passed = (current_date - last_login_date).days
        match days_passed:
            case _ if days_passed < TWO_DAYS:
                last_login_statistics[cnst.LESS_TWO_DAYS] += 1
            case _ if days_passed < WEEK:
                last_login_statistics[cnst.LESS_WEEK] += 1
            case _ if days_passed < MONTH:
                last_login_statistics[cnst.LESS_MONTH] += 1
            case _ if days_passed < HALFYEAR:
                last_login_statistics[cnst.LESS_HALFYEAR] += 1
            case _:
                last_login_statistics[cnst.MORE_HALFYEAR] += 1

    quantity_users = len(last_login_dates)
    for period in last_login_statistics.keys():
        percent = round(last_login_statistics[period] / quantity_users * 100, ROUND_UP_TO_TWO)
        last_login_statistics[period] = f'{percent}%'

    return last_login_statistics


def _aggregate_data(users: dict) -> dict:
    age_stats = calculate_ages_stats(users)
    data_stats = calculate_dates_stats(users)
    return {
        **age_stats,
        **data_stats,
    }


def _save_data(input_path: str, output_path: str) -> None:
    try:
        with open(input_path, 'r') as input_file:
            users = json.load(input_file)
    except ValueError:
        raise exceptions_hw2.InvalidJSONFormatError(input_path)
    except FileNotFoundError:
        raise exceptions_hw2.InputFilepathError(input_path)
    if not users:
        raise exceptions_hw2.EmptyJSONError(input_path)

    statistics = _aggregate_data(users)
    os.makedirs(os.path.abspath(os.path.dirname(output_path)), exist_ok=True)
    with open(output_path, 'w') as out:
        json.dump(statistics, out, indent=4)


def process_data(input_path: str = 'input.json', output_path: str = 'output.json'):
    """Process data from input json and write statistics to output json file.

    Args:
        input_path (str): path to source json file. Defaults to 'input.json'.
        output_path (str): path to destionation json file. Defaults to 'output.json'.
    """
    try:
        _save_data(input_path, output_path)
    except Exception as error:
        with open(output_path, 'w') as out:
            json.dump({'ERROR': str(error)}, out, indent=4)
