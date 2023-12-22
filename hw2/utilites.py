"""Utils for HW2."""
from datetime import date

AGE18 = 18
AGE25 = 25
AGE45 = 45
AGE60 = 60


def get_age_group(age: int) -> str:
    """
    Return age group for age.

    Args:
        age (int): age of client

    Returns:
        str: age group
    """
    if age < AGE18:
        return '0-18'
    elif age < AGE25:
        return '18-25'
    elif age < AGE45:
        return '25-45'
    elif age < AGE60:
        return '45-60'
    return '60+'


def get_age_stats(input_dict: dict) -> dict:
    """
    Calculate age stats for input_dict and return a dictionary with the stats.

    Args:
        input_dict (dict): dict with data about clients

    Returns:
        dict: dict with age stats
    """
    age_stats = {
        '0-18': 0,
        '18-25': 0,
        '25-45': 0,
        '45-60': 0,
        '60+': 0,
    }
    for user in input_dict.keys():
        age = input_dict[user]['age']
        age_group = get_age_group(age)
        age_stats[age_group] += 1
    return age_stats


def get_last_login_stats(input_dict: dict) -> dict:
    """
    Calculate last login stats for input_dict and return a dictionary with the stats.

    Args:
        input_dict (dict): dict with data about clients

    Returns:
        dict: dict with last login stats
    """
    last_login = {
        'less2days': 0,
        'less1week': 0,
        'less1month': 0,
        'less6months': 0,
        '6months+': 0,
    }
    for user in input_dict.keys():
        last_login_str = input_dict[user]['last_login']
        last_login_group = get_last_login_group(last_login_str)
        last_login[last_login_group] += 1
    return last_login


def get_last_login_group(last_login_str: str) -> str:
    """
    Return last login group for last_login_str.

    Args:
        last_login_str (str): last login of client

    Returns:
        str: last login group
    """
    six_months = 180
    month = 30
    week = 7
    date_today = date.today()
    last_login_date = date.fromisoformat(last_login_str)
    delta = date_today - last_login_date
    if delta.days < 2:
        return 'less2days'
    elif delta.days < week:
        return 'less1week'
    elif delta.days < month:
        return 'less1month'
    elif delta.days < six_months:
        return 'less6months'
    return '6months+'
