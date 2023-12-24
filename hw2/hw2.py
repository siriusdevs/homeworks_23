"""Module for solving task_2.

Task_2:
Напишите модуль,
в котором функция process_data принимает путь к json-файлу с данными о клиентах сайта
(пример файла в data_hw2.json) и путь к json-файлу вывода.
Функция process_data записывает в этот общий json статистику:
минимальный, максимальный, средний и медианный возраст пользователя,
а также средний возраст клиентов,
которые были онлайн менее двух дней, недели, месяца, полугода, и более полугода назад.
"""
import json
import os
from statistics import get_all_stats
from typing import Iterable

from constants import STATS_JSON, USERS_JSON
from exceptions import InvalidInputFileError


def process_data(input_path: str, output_path: str) -> None:
    """Read input JSON file and write statistics in output file.

    Input JSON file must contain users with user_name as key and
    'last_login' and 'age' fields as value.

    Args:
        input_path: path to input JSON file with users data
        output_path: path to output JSON file to write statistics
    """
    users = _read_json(input_path)
    stats = get_all_stats(users)
    _write_json(output_path, stats)


def _read_json(path: str) -> Iterable[USERS_JSON]:
    try:
        with open(path, 'r') as json_file:
            return json.load(json_file).values()
    except Exception:
        raise InvalidInputFileError(path)


def _write_json(path: str, stats: STATS_JSON) -> None:
    dirs = os.path.dirname(path)
    os.makedirs(os.path.abspath(dirs), exist_ok=True)

    with open(path, 'w') as output_file:
        json.dump(stats, output_file)
