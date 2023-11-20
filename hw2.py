"""A module that includes the functions for working with json files."""

import json
import os
from datetime import datetime, timedelta

from config import (GT_SIX_MONTHS, LT_MONTH, LT_SIX_MONTHS, LT_TWO_DAYS,
                    LT_WEEK, MONTH, ONLINE_STATS, SIX_MONTHS)


def update_online_stats(
    time_online: timedelta,
) -> None:
    """Update online statistics.

    Args:
        time_online (timedelta): The period when the user is online.
    """
    if time_online < timedelta(days=2):
        ONLINE_STATS[LT_TWO_DAYS] += 1
    elif time_online < timedelta(days=7):
        ONLINE_STATS[LT_WEEK] += 1
    elif time_online < timedelta(days=MONTH):
        ONLINE_STATS[LT_MONTH] += 1
    elif time_online < timedelta(days=SIX_MONTHS):
        ONLINE_STATS[LT_SIX_MONTHS] += 1
    else:
        ONLINE_STATS[GT_SIX_MONTHS] += 1


def onl(usr_data: dict) -> dict:
    """Make online statistics.

    Args:
        usr_data (dict): User information.

    Returns:
        dict: Dictionary with statistics of being online for different periods.
    """
    for user_info in usr_data.values():
        user_info = {details.lower(): _ for details, _ in user_info.items()}
        if user_info.get('registered') and user_info.get('last_login'):
            registr = datetime.strptime(user_info.get('registered'), '%Y-%m-%d')
            last_log = datetime.strptime(user_info.get('last_login'), '%Y-%m-%d')
            time_online = (last_log - registr)
            update_online_stats(time_online)
    return ONLINE_STATS


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
        if region:
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
    if os.path.exists(data_file):
        with open(data_file, 'rt') as inp_f:
            usr_data = json.load(inp_f)
            geo_distrb = {city: num / len(usr_data) for city, num in geo(usr_data).items()}
            onl_sts = {period: num / len(usr_data) for period, num in onl(usr_data).items()}
            geo_distrb = {city: round(num, 2) for city, num in geo_distrb.items()}
            onl_sts = {period: round(num, 2) for period, num in onl_sts.items()}
    else:
        geo_distrb = 0
        onl_sts = 0
    with open(output_file, 'w') as out_f:
        json.dump(
            {
                'geo_distribution': geo_distrb, 'online_stats': onl_sts,
            },
            out_f, indent=4,
        )
