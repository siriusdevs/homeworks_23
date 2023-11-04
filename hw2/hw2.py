"""
Provides types and functions for solving task_2.

Напишите модуль, в котором функция process_data принимает путь к json-файлу с данными
о клиентах сайта (пример файла в data_hw2.json) и путь к json-файлу вывода.
Функция process_data записывает в этот общий json статистику:
минимальный, максимальный, средний и медианный возраст пользователя, а также средний возраст
клиентов, которые были онлайн менее двух дней, недели, месяца, полугода, и более полугода назад.
"""

import dataclasses
import datetime
import json


@dataclasses.dataclass
class AgeStats:
    """Basic stats for a list of ages."""

    min: float = 0
    max: float = 0
    mean: float = 0
    median: float = 0


YEAR_DAYS = 365
TIMEDELTAS_LESS = (
    ('less_2_days', datetime.timedelta(days=2)),
    ('less_week', datetime.timedelta(weeks=1)),
    ('less_month', datetime.timedelta(weeks=4)),
    ('less_halfyear', datetime.timedelta(days=YEAR_DAYS/2)),
)


TIMEDELTAS_GREATER = (
    ('greater_halfyear', datetime.timedelta(days=YEAR_DAYS/2)),
)


def aggregate_users_stats(input_file: str, output_file: str) -> None:
    """Read user stats from input_file, aggregate them and write to output_file.

    Schema of the output file is a json object with fields corresponding to keys of
    TIMEDELTAS_LESS and TIMEDELTAS_GREATER and values corresponding to AgeStats of users
    who have been online according to these timedeltas.

    Args:
        input_file: path to a json file containing user stats
        output_file: path to an output file. json aggregate stats will be written there.
    """
    stats = {}
    for less_name, _ in TIMEDELTAS_LESS:
        stats[less_name] = dataclasses.asdict(AgeStats())
    for greater_name, _ in TIMEDELTAS_GREATER:
        stats[greater_name] = dataclasses.asdict(AgeStats())
    with open(output_file, 'w') as out:
        json.dump(stats, out)
