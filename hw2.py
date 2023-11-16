"""A module that includes the functions for working with json files."""


import json
from datetime import datetime, timedelta


def update_online_stats(
    online_stats: dict,
    time_online: timedelta,
    month: int, six_months: int,
) -> None:
    """Update online statistics.

    Args:
        online_stats (dict): Dictionary with statistics of being online for different periods.
        time_online (timedelta): The period when the user is online.
        month (int): Month with 31 days.
        six_months (int): Six months with 186 days.
    """
    lt_two_days = 'less than 2 days'
    lt_week = 'less than 2 days'
    lt_month = 'less than month'
    lt_six_months = 'less than 6 months'
    gt_six_months = 'great than 6 months'
    if time_online < timedelta(days=2):
        online_stats[lt_two_days] += 1
    elif time_online < timedelta(days=7):
        online_stats[lt_week] += 1
    elif time_online < timedelta(days=month):
        online_stats[lt_month] += 1
    elif time_online < timedelta(days=six_months):
        online_stats[lt_six_months] += 1
    else:
        online_stats[gt_six_months] += 1


def online(usr_data: dict) -> dict:
    """Make online statistics.

    Args:
        usr_data (dict): User information.

    Returns:
        dict: Dictionary with statistics of being online for different periods.
    """
    month = 31
    six_months = 186
    online_stats = {
        'less than 2 days': 0,
        'less than week': 0,
        'less than month': 0,
        'less than 6 months': 0,
        'great than 6 months': 0,
        }
    for user_info in usr_data.values():
        registr = datetime.strptime(user_info.get('registered'), '%Y-%m-%d')
        last_log = datetime.strptime(user_info.get('last_login'), '%Y-%m-%d')
        time_online = (last_log - registr)
        update_online_stats(online_stats, time_online, month, six_months)
    return online_stats


def geo(usr_data: dict) -> dict:
    """Make geographical statistics.

    Args:
        usr_data (dict): User information.

    Returns:
        dict: Dictionary with statistics on the distribution of users by city.
    """
    city_stats = {}
    for user_info in usr_data.values():
        region = user_info.get('region')
        if region not in city_stats:
            city_stats[region] = 0
        city_stats[region] += 1
    return city_stats


def process_data(data_file: str, output_file: str) -> None:
    """Make other statistics as a percentage.

    Args:
        data_file (str): Path to input json file with user data.
        output_file (str): Path to output json file.
    """
    with open(data_file, 'rt') as inp_f:
        usr_data = json.load(inp_f)
        geo_distribution = {city: num / len(usr_data) for city, num in geo(usr_data).items()}
        online_stats = {period: num / len(usr_data) for period, num in online(usr_data).items()}
    with open(output_file, 'w') as out_f:
        json.dump(
            {
                'geo_distribution': geo_distribution, 'online_stats': online_stats,
            },
            out_f, indent=4,
        )
