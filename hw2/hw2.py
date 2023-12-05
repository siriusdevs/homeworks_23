"""
Provides types and functions for solving task_2.

Напишите модуль, в котором функция process_data принимает путь к json-файлу с данными
о клиентах сайта (пример файла в data_hw2.json) и путь к json-файлу вывода.
Функция process_data записывает в этот общий json статистику:
минимальный, максимальный, средний и медианный возраст пользователя, а также средний возраст
клиентов, которые были онлайн менее двух дней, недели, месяца, полугода, и более полугода назад.
"""

import json
import os
from datetime import datetime
from typing import Callable, Iterable

from hw2 import types_hw2

from .const_hw2 import LESS_FILTER, ROUND_UPTO, TIMEDELTAS
from .fields_hw2 import AGE_AVERAGE, AGE_MAX, AGE_MEDIAN, AGE_MIN
from .types_hw2 import JsonDict, TimeFilterType


def aggregate_users_stats(input_path: str, output_path: str, _now=None) -> None:
    """Read user stats from input_path, aggregate them and write to output_path.

    Schema of the output file is a json object with fields corresponding to keys of
    const_hw2.TIMEDELTAS and values corresponding to average age of users
    who have been online according to these timedeltas.
    The output file also contains total age stats with these keys:
    const_hw2.AGE_MAX, const_hw2.AGE_MIN, const_hw2.AGE_AVERAGE, const_hw2.AGE_MEDIAN.

    Args:
        input_path: path to a json file containing user stats
        output_path: path to an output file. json aggregate stats will be written there.

    Raises:
        InvalidInputFileException: when input_path is invalid
    """
    try:
        with open(input_path, 'r') as inp:
            users = json.load(inp).values()
    except Exception:
        raise types_hw2.InvalidInputFileException(input_path)
    stats = _aggregate_stats(users, _now)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as out:
        json.dump(stats, out)


def _aggregate_stats(users: Iterable[JsonDict], _now=None) -> JsonDict:
    now = datetime.now() if _now is None else _now  # for tests
    return {
        name: _average(_ages(filter(
            _filter_by_activity(filter_type, timebound=now - delta),
            users,
        )))
        for filter_type, name, delta in TIMEDELTAS
    } | _total_stats(_ages(users))


def _total_stats(ages: list[int]) -> JsonDict:
    return {
       AGE_MAX: max(ages, default=0),
       AGE_MIN: min(ages, default=0),
       AGE_AVERAGE: _average(ages),
       AGE_MEDIAN: _median(ages),
    }


def _filter_by_activity(ftype: TimeFilterType, timebound: datetime) -> Callable[[JsonDict], bool]:
    return lambda user: (
        _get_login_time(user) > timebound if ftype == LESS_FILTER else
        _get_login_time(user) < timebound
    )


def _get_login_time(user: JsonDict) -> datetime:
    try:
        return datetime.strptime(user['last_login'], '%Y-%m-%d')
    except ValueError:
        raise types_hw2.InvalidDateException(user['last_login'], '2006-08-02')


def _ages(users: Iterable[JsonDict]) -> list[int]:
    try:
        return [user['age'] for user in users]
    except KeyError:
        raise types_hw2.MissingFieldException('age')


def _average(nums: list[float] | list[int]) -> float:
    return round(sum(nums) / max(len(nums), 1), ROUND_UPTO)


def _median(nums: list[float] | list[int]) -> float:
    nums = sorted(nums)
    center = len(nums) // 2
    return (
        nums[center]
        if len(nums) % 2
        else _average(nums[center - 1:center + 1])
    )
