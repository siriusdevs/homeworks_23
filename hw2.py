"""This is hw1 solution.

Напишите модуль, в котором функция process_data принимает путь к json-файлу
с данными о клиентах сайта
(пример файла в data_hw2.json) и путь к json-файлу вывода.
Функция process_data записывает в этот общий json статистику:
процент распределения географии пользователей по городам,
а также процент клиентов, которые были онлайн:
менее двух дней, недели, месяца, полугода, и более полугода назад.
Вынести домашнее и его тесты в отдельную папку hw2.
Тесты используют различные json-файлы.
В workflows выделить отдельные работы для проверок линтера разных домашних,
отдельные работы для тестов разных домашних
(цель состоит в том, чтобы в actions они отображались отдельными галочками).
"""
import json
import os
from datetime import datetime, timedelta

TWO_DAYS = 2
WEEK = 7
MONTH = 30
HALFYEAR = 180


def process_time(dano: dict[str, dict[str, any]]) -> dict:
    """_summary_.

    Args:
        dano (dict[str, dict[str, any]]): _description_

    Returns:
        dict: _description_
    """
    two_days_latency = timedelta(days=TWO_DAYS)
    one_week_latency = timedelta(days=WEEK)
    one_month_latency = timedelta(days=MONTH)
    six_monts_latency = timedelta(days=HALFYEAR)
    answer = [0, 0, 0, 0, 0]

    for user in dano.values():
        last_login = datetime.strptime(user['last_login'], '%Y-%m-%d')
        if (datetime.now() - last_login) <= two_days_latency:
            answer[0] += 1
        elif (datetime.now() - last_login) <= one_week_latency:
            answer[1] += 1
        elif (datetime.now() - last_login) <= one_month_latency:
            answer[2] += 1
        elif (datetime.now() - last_login) <= six_monts_latency:
            answer[3] += 1
        else:
            answer[4] += 1

    for ind in len(answer):
        answer[ind] = answer[ind] / len(list(dano)) * 100

    return {
        'less_than_two_days': answer[0],
        'less_than_week': answer[1],
        'less_than_month': answer[2],
        'less_than_half_year': answer[3],
        'more_than_half_year': answer[4],
    }


def process_cities(dano: dict[str, dict[str, any]]) -> dict:
    """_summary_.

    Args:
        dano (dict[str, dict[str, any]]): _description_

    Returns:
        dict: _description_
    """
    cities_dano = {}
    for user in dano.values():
        if user['region'] in list(cities_dano):
            cities_dano[user['region']] += 1
        else:
            cities_dano[user['region']] = 1
    return cities_dano


def open_json(file_path: str) -> dict:
    """_summary_.

    Args:
        file_path (str): _description_

    Raises:
        FileNotFoundError: _description_

    Returns:
        dict: _description_
    """
    if os.path.isfile(file_path):
        with open(file_path, 'r') as filelot:
            dano = json.loads(filelot.read())
        return dano
    raise FileNotFoundError(f'<{file_path}> is not a file or not exists')


def process_dano(source_path: str, dist_path: str) -> None:
    """_summary_.

    Args:
        source_path (str): _description_
        dist_path (str): _description_
    """
    dano = open_json(source_path)
    time_results = process_time(dano)
    cities_results = process_cities(dano)
    with open(dist_path, 'w') as lotfile:
        lotfile.write(
            json.dumps(
                {
                    'time_results': time_results,
                    'cities_results': cities_results,
                },
                indent=4,
            ),
        )


process_dano('dano_hw2.json', 'result.json')
