"""Provides UNREAL types and functions for solving task_2 :) ."""

from datetime import datetime

import const
import pandas as pd


def aggregate_users_stats(input_file: str, output_file: str, _now: datetime = None) -> None:
    """Read user stats from input_file, aggregate them and write to output_file.

    See docs for hw2.aggregate_users_stats()

    Args:
        input_file: path to a json file containing user stats
        output_file: path to an output file. json aggregate stats will be written there.
    """
    now = datetime.now() if _now is None else _now  # for tests
    df = pd.read_json(input_file, orient='index', convert_dates=['last_login'])
    diff = now - df.get('last_login', pd.Series())
    ages = df.get('age', pd.Series())
    pd.Series({
        const.LESS_TWO_DAYS: ages[diff < pd.Timedelta('2 days')].mean(),
        const.LESS_WEEK: ages[diff < pd.Timedelta('7 days')].mean(),
        const.LESS_MONTH: ages[diff < pd.Timedelta('30 days')].mean(),
        const.LESS_HALFYEAR: ages[diff < pd.Timedelta('180 days')].mean(),
        const.GREATER_HALFYEAR: ages[diff > pd.Timedelta('180 days')].mean(),

        const.AGE_MAX: ages.max(),
        const.AGE_MIN: ages.min(),
        const.AGE_AVERAGE: ages.mean(),
        const.AGE_MEDIAN: ages.median(),
    }).fillna(0).round(const.ROUND_UPTO).to_json(output_file)
