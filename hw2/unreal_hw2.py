"""Provides UNREAL :) types and functions for solving task_2."""

import os
from datetime import datetime

import pandas as pd

from . import const_hw2, fields_hw2, types_hw2


def aggregate_users_stats(input_path: str, output_path: str, _now=None) -> None:
    """Read user stats from input_path, aggregate them and write to output_path.

    See docs for hw2.aggregate_users_stats()

    Args:
        input_path: path to a json file containing user stats
        output_path: path to an output file. json aggregate stats will be written there.

    Raises:
        InvalidInputFileException: when input_path is invalid
    """
    now = datetime.now() if _now is None else _now  # for tests
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    try:
        df = pd.read_json(input_path, orient='index', convert_dates=['last_login'])
    except Exception:
        raise types_hw2.InvalidInputFileException(input_path)
    time_since_login = now - df.get('last_login', pd.Series())
    ages = df.get('age', pd.Series())
    pd.Series({
        fields_hw2.LESS_TWO_DAYS: ages[time_since_login < pd.Timedelta('2 days')].mean(),
        fields_hw2.LESS_WEEK: ages[time_since_login < pd.Timedelta('7 days')].mean(),
        fields_hw2.LESS_MONTH: ages[time_since_login < pd.Timedelta('30 days')].mean(),
        fields_hw2.LESS_HALFYEAR: ages[time_since_login < pd.Timedelta('180 days')].mean(),
        fields_hw2.GREATER_HALFYEAR: ages[time_since_login > pd.Timedelta('180 days')].mean(),

        fields_hw2.AGE_MAX: ages.max(),
        fields_hw2.AGE_MIN: ages.min(),
        fields_hw2.AGE_AVERAGE: ages.mean(),
        fields_hw2.AGE_MEDIAN: ages.median(),
    }).fillna(0).round(const_hw2.ROUND_UPTO).to_json(output_path)
