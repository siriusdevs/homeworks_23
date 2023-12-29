"""Calculates statistics based on users json data."""

from datetime import date, datetime, timedelta
from typing import Callable, Iterable

from constants import (AVERAGE, MAXIMUM, MEDIAN, MINIMUM, ROUND_UPTO,
                       STATS_JSON, TIMEDELTAS, USERS_JSON)
from exceptions import (InvalidDateError, InvalidDateFormatError,
                        MissingFieldError)


def get_all_stats(users: Iterable[USERS_JSON]) -> STATS_JSON:
    """Calculate statistics based on users json data.

    Args:
        users: users data from json file

    Returns:
        age statistics in JSON format
    """
    return _get_ages_stats(users) | _get_logins_stats(users)


def _get_ages(users: Iterable[USERS_JSON]) -> list[int | float]:
    try:
        return [user['age'] for user in users]
    except KeyError:
        raise MissingFieldError('age')


def _average(ages: list[int]) -> int | float:
    return round(sum(ages) / len(ages), ROUND_UPTO) if ages else 0


def _median(ages: list[int | float]) -> int | float:
    if not ages:
        return 0
    ages.sort()
    center = len(ages) // 2

    return (
        ages[center] if len(ages) % 2
        else _average([ages[center], ages[center - 1]])
    )


def _get_ages_stats(users: Iterable[USERS_JSON]) -> STATS_JSON:
    ages = _get_ages(users)
    return {
        MINIMUM: min(ages, default=0),
        MAXIMUM: max(ages, default=0),
        AVERAGE: _average(ages),
        MEDIAN: _median(ages),
    }


def _get_last_login_delta(user: USERS_JSON) -> timedelta:
    try:
        login_date = datetime.strptime(user['last_login'], '%Y-%m-%d').date()
    except KeyError:
        raise MissingFieldError('last_login')
    except ValueError:
        raise InvalidDateFormatError(user['last_login'])

    if login_date > date.today():
        raise InvalidDateError(login_date)
    return date.today() - login_date


def _is_date_in_delta(name: str, delta: timedelta) -> Callable[[USERS_JSON], bool]:
    return lambda user: (
        _get_last_login_delta(user) < delta
        if name.startswith('less')
        else _get_last_login_delta(user) > delta
    )


def _get_logins_stats(users: Iterable[USERS_JSON]) -> STATS_JSON:
    return {
        name: _average(_get_ages(filter(
            _is_date_in_delta(name, delta),
            users,
        )))
        for name, delta in TIMEDELTAS
    }
