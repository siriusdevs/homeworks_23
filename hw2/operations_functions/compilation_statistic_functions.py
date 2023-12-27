"""Module for writing statistics to dictionaries."""


import operations_functions.arithmetic_operations_functions as aof
import operations_functions.operations_on_dates_functions as oodf

LESS_THAN = 'Percentage of users who logged in less than'
MORE_THAN = 'Percentage of users who logged in more than'

TWO_DAYS_AGO = 'two days ago'
WEEK_AGO = 'week ago'
MONTH_AGO = 'month ago'
HALF_YEAR_AGO = 'half year ago'

time_intervals = [TWO_DAYS_AGO, WEEK_AGO, MONTH_AGO, HALF_YEAR_AGO]


def get_ages_data(users_ages: list[int]) -> dict:
    """Write statistics about ages of users in the dictionary.

    Args:
        users_ages (list[int]): ages of users.

    Returns:
        dict: statistics about ages of users.
    """
    statistics = {}
    statistics['Minimum age among users'] = min(users_ages)
    statistics['Maximum age among users'] = max(users_ages)
    statistics['Average age of users'] = aof.get_average(users_ages)
    statistics['Median age of users'] = aof.get_median(users_ages)
    return statistics


def get_last_logins_data(users_last_logins: list[str]) -> dict:
    """Write statistics about last logins of users in the dictionary.

    Args:
        users_last_logins (list[str]): last logins of users.

    Returns:
        dict: statistics about last logins of users.
    """
    statistics = {}
    users_last_logins_percentage = oodf.comparing_dates(users_last_logins)
    statistics = {}
    statistics[LESS_THAN] = {}
    for number, time_interval in enumerate(time_intervals):
        statistics[LESS_THAN][time_interval] = users_last_logins_percentage[number]
    statistics[MORE_THAN] = {}
    statistics[MORE_THAN][time_intervals[-1]] = users_last_logins_percentage[-1]
    return statistics


def get_data(users_ages: list[int], users_last_logins: list[str]):
    """Write statistics about ages and last logins of users in the general dictionary.

    Args:
        users_ages (list[int]): ages of users.
        users_last_logins (list[str]): last logins of users.

    Returns:
        dict: statistics about ages and last logins of users.
    """
    statistics = {}
    statistics['Ages data'] = get_ages_data(users_ages)
    statistics['Last logins data'] = get_last_logins_data(users_last_logins)
    return statistics
