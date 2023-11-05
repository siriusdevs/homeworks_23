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
from typing import Iterable

import const


def aggregate_users_stats(input_file: str, output_file: str, _now: datetime = None) -> None:
    """Read user stats from input_file, aggregate them and write to output_file.

    Schema of the output file is a json object with fields corresponding to keys of
    const.TIMEDELTAS and values corresponding to average age of users
    who have been online according to these timedeltas.
    The output file also contains total age stats with these keys:
    const.AGE_MAX, const.AGE_MIN, const.AGE_AVERAGE, const.AGE_MEDIAN.

    Args:
        input_file: path to a json file containing user stats
        output_file: path to an output file. json aggregate stats will be written there.
    """
    with open(input_file, 'r') as inp:
        users = json.load(inp).values()
    stats = _aggregate_stats(users, _now)
    with open(output_file, 'w') as out:
        json.dump(stats, out)


def _aggregate_stats(users: const.JsonDict, _now: datetime = None) -> const.JsonDict:
    now = datetime.now() if _now is None else _now  # for tests
    return {
        name: _average(_ages(filter(
            _filter_by_activity(filter_type, timebound=now - delta),
            users,
        )))
        for filter_type, name, delta in const.TIMEDELTAS
    } | _total_stats(_ages(users))


def _total_stats(ages: list[int]) -> const.JsonDict:
    return {
       const.AGE_MAX: max(ages, default=0),
       const.AGE_MIN: min(ages, default=0),
       const.AGE_AVERAGE: _average(ages),
       const.AGE_MEDIAN: _median(ages),
    }


def _filter_by_activity(filter_type: const.TimeFilterType, timebound: datetime) -> callable:
    return lambda user: (
        _get_login_time(user) > timebound if filter_type == const.LESS else
        _get_login_time(user) < timebound
    )


def _get_login_time(user: dict) -> datetime:
    return datetime.strptime(user['last_login'], '%Y-%m-%d')


def _ages(users: Iterable[const.JsonDict]) -> list[int]:
    return [user['age'] for user in users]


def _average(nums: list[float]) -> float:
    return round(sum(nums) / max(len(nums), 1), const.ROUND_UPTO)


def _median(nums: list[float]) -> float:
    nums = sorted(nums)
    center = len(nums) // 2
    return (
        nums[center]
        if len(nums) % 2
        else _average(nums[center - 1:center + 1])
    )
