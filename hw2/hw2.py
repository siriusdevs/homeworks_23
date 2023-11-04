"""
Provides types and functions for solving task_2.

Напишите модуль, в котором функция process_data принимает путь к json-файлу с данными
о клиентах сайта (пример файла в data_hw2.json) и путь к json-файлу вывода.
Функция process_data записывает в этот общий json статистику:
минимальный, максимальный, средний и медианный возраст пользователя, а также средний возраст
клиентов, которые были онлайн менее двух дней, недели, месяца, полугода, и более полугода назад.
"""

import json
from datetime import datetime

import const
from age_stats import AgeStats, get_age_stats


def aggregate_users_stats(input_file: str, output_file: str, _now: datetime = None) -> None:
    """Read user stats from input_file, aggregate them and write to output_file.

    Schema of the output file is a json object with fields corresponding to keys of
    const.TIMEDELTAS and values corresponding to AgeStats of users
    who have been online according to these timedeltas.

    Args:
        input_file: path to a json file containing user stats
        output_file: path to an output file. json aggregate stats will be written there.
    """
    with open(input_file, 'r') as inp:
        users = json.load(inp).values()
    stats = _aggregate_stats(users, _now)
    json_stats = {name: age_stats.to_json() for name, age_stats in stats.items()}
    with open(output_file, 'w') as out:
        json.dump(json_stats, out)


def _aggregate_stats(users: list[dict], _now: datetime = None) -> dict[str, AgeStats]:
    now = datetime.now() if _now is None else _now  # for tests
    return {
        name: get_age_stats(filter(
            _last_login_filter(filter_type, timebound=now - delta),
            users,
        ))
        for filter_type, name, delta in const.TIMEDELTAS
    }


def _last_login_filter(filter_type: const.TimeFilterType, timebound: datetime) -> callable:
    return lambda user: (
        _get_login_time(user) > timebound if filter_type == const.LESS else
        _get_login_time(user) < timebound
    )


def _get_login_time(user: dict) -> datetime:
    return datetime.strptime(user['last_login'], '%Y-%m-%d')
