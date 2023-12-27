"""Module with operations on dates functions."""


import datetime

TWO_DAYS = 2
WEEK = 7
MONTH = 30
HALF_YEAR = 182

CURRENT_DAY = '2023-12-23'

time_intervals = [TWO_DAYS, WEEK, MONTH, HALF_YEAR]


def comparing_dates(dates: list[str]) -> list[int | float]:
    """Calculate the percentage of users who logged in less or more \
        than a specific intervals of time ago.

    Args:
        dates (list[int]): dates.

    Returns:
        list[int | float]: the percentage of users who logged in less or more \
            than a specific intervals of time ago.
    """
    current_day = datetime.datetime.strptime(CURRENT_DAY, '%Y-%m-%d').date()
    users_last_logins_numbers = [0 for _ in range(len(time_intervals) + 1)]
    for date in dates:
        compared_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        diff = (current_day - compared_date).days
        for number, time_interval in enumerate(time_intervals):
            if diff < time_interval:
                users_last_logins_numbers[number] += 1
        if diff >= time_intervals[-1]:
            users_last_logins_numbers[-1] += 1
    return [str(round(elem / len(dates) * 100, 2)) for elem in users_last_logins_numbers]
