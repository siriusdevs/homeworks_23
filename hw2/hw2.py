"""
Provides types and functions for solving task_2.

Напишите модуль, в котором функция process_data принимает путь к json-файлу с данными
о клиентах сайта (пример файла в data_hw2.json) и путь к json-файлу вывода.
Функция process_data записывает в этот общий json статистику:
минимальный, максимальный, средний и медианный возраст пользователя, а также средний возраст
клиентов, которые были онлайн менее двух дней, недели, месяца, полугода, и более полугода назад.
"""

import dataclasses
import json
from datetime import datetime
from typing import Callable, Iterable

import const


@dataclasses.dataclass
class AgeStats:
    """Basic stats for a list of ages."""

    min: float = 0
    max: float = 0
    average: float = 0
    median: float = 0

    def to_json(self) -> dict:
        """Convert AgeStats to a dict for json encoding.

        Returns:
            A dictionary with all fields
        """
        return dataclasses.asdict(self)


def aggregate_users_stats(input_file: str, output_file: str, _now: datetime = None) -> None:
    """Read user stats from input_file, aggregate them and write to output_file.

    Schema of the output file is a json object with fields corresponding to keys of
    TIMEDELTAS_LESS and TIMEDELTAS_GREATER and values corresponding to AgeStats of users
    who have been online according to these timedeltas.

    Args:
        input_file: path to a json file containing user stats
        output_file: path to an output file. json aggregate stats will be written there.
    """
    with open(input_file, 'r') as inp:
        users = json.load(inp).values()
    stats = _aggregate_stats_usecase(users, _now)
    json_stats = {name: age_stats.to_json() for name, age_stats in stats.items()}
    with open(output_file, 'w') as out:
        json.dump(json_stats, out)


def _aggregate_stats_usecase(users: list[dict], _now: datetime = None) -> dict[str, AgeStats]:
    now = datetime.now() if _now is None else _now
    stats = {}
    for less_name, less_delta in const.TIMEDELTAS_LESS:
        bound = now - less_delta
        stats[less_name] = _get_age_stats(
            filter(_with_login_newer_than(bound), users),
        )
    for greater_name, greater_delta in const.TIMEDELTAS_GREATER:
        bound = now - greater_delta
        stats[greater_name] = _get_age_stats(
            filter(_with_login_older_than(bound), users),
        )
    return stats


def _with_login_newer_than(dt: datetime) -> Callable[[dict], bool]:
    return lambda user: _get_login_time(user) > dt


def _with_login_older_than(dt: datetime) -> Callable[[dict], bool]:
    return lambda user: _get_login_time(user) < dt


def _get_login_time(user: dict) -> datetime:
    return datetime.strptime(user['last_login'], '%Y-%m-%d')


ROUND_UPTO = 2


def _get_age_stats(users: Iterable[dict]) -> AgeStats:
    ages = [user['age'] for user in users]
    return AgeStats(
        min=min(ages),
        max=max(ages),
        average=round(_average(ages), 2),
        median=round(_median(ages), 2),
    ) if ages else AgeStats()


def _average(nums: Iterable[float]) -> float:
    return sum(nums) / len(nums)


def _median(nums: Iterable[float]) -> float:
    nums = sorted(nums)
    center = len(nums) // 2
    return (
        nums[center]
        if len(nums) % 2
        else _average(nums[center - 1:center + 1])
    )
