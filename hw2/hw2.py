"""HW2."""
import json
import os
from datetime import date, datetime, timedelta
from typing import Any

MONTH = 30
TIMEDELTAS = (
    ('less_two_days', timedelta(days=2), False),
    ('less_week', timedelta(weeks=1), False),
    ('less_month', timedelta(days=MONTH), False),
    ('less_half_year', timedelta(days=6 * MONTH), False),
    ('greater_half_year', timedelta(days=6 * MONTH), True),
)

GEOGRAPHY_STATS = 'geography_stats'
LAST_LOGIN_STATS = 'last_login_stats'

Stats = dict[str, dict[str, float]]
JSONDict = dict[str, Any]


def process_data(input_path: str, output_path: str) -> None:
    """Read json files in input_path and write in output_path.

    Args:
        input_path: input json files
        output_path: output json files
    """
    users = _read_json(input_path)
    stats = get_region_stats(users) | get_login_stats(users)
    _write_json(output_path, stats)


def _read_json(path: str) -> JSONDict:
    try:
        with open(path, 'r') as json_file:
            return json.load(json_file)
    except Exception:
        raise FileNotFoundError(f'Failed to read input JSON file {path}')


def _write_json(path: str, stats: Stats) -> None:
    dirs = os.path.dirname(path)
    os.makedirs(os.path.abspath(dirs), exist_ok=True)

    with open(path, 'w') as output_file:
        json.dump(stats, output_file)


def _get_field(json_object: JSONDict, field: str) -> Any:
    try:
        return json_object[field]
    except KeyError:
        raise KeyError(f'Field {field} is missing in JSON')


def get_region_stats(users: JSONDict) -> Stats:
    """Get statistics about regions.

    Args:
        users: users from json file in dict

    Returns:
        statistics about regions in json format
    """
    region_stats = {}

    for _, user_data in users.items():
        region = _get_field(user_data, 'region')
        if region not in region_stats:
            region_stats[region] = 0
        region_stats[region] += 1

    return {
        GEOGRAPHY_STATS: {
            name: 100 * round(repeats / len(users), 2)
            if users else None
            for name, repeats in region_stats.items()
        },
    }


def _get_login_delta(json_object: JSONDict) -> timedelta:
    last_login = _get_field(json_object, 'last_login')
    try:
        login_date = datetime.strptime(last_login, '%Y-%m-%d').date()
    except ValueError:
        raise TypeError(f'Last login ({last_login}) is invalid! Example: 2024-01-01.')

    if login_date > date.today():
        raise ValueError(f'Last login ({last_login}) in the future! Today is {date.today()}.')
    return date.today() - login_date


def get_login_stats(users: JSONDict) -> Stats:
    """Get statistics about last login.

    Args:
        users: users from json file in dict

    Returns:
        statistics about last login in json format
    """
    login_stats = {name: [] for name, _, _ in TIMEDELTAS}

    for _, user_data in users.items():
        login_delta = _get_login_delta(user_data)

        for delta_name, delta, is_greater in TIMEDELTAS:
            if is_greater == (login_delta > delta):
                login_stats[delta_name].append(_get_field(user_data, 'age'))

    return {
        LAST_LOGIN_STATS: {
            name: round(sum(age) / len(age), 2)
            if age else None
            for name, age in login_stats.items()
        },
    }
