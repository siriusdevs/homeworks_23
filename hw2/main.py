"""Module for calculate stats."""

import json
from math import ceil

import dateparser

DAYS_CONST = 60 * 60 * 24
HALF_YEAR = 183


def validate_email(email: str) -> bool:
    """Check email for accuracy.

    Args:
        email (str): user email

    Returns:
        bool: valid or invalid email
    """
    return email.count('@') == 1 and not email.startswith('@')


def duration_dispersion(clients: dict[str, dict]) -> tuple[dict[str, dict]]:
    """Calculate duration on site for each user.

    Args:
        clients (dict[str, dict]): dict of users information

    Returns:
        tuple[dict[str, dict]]: calculated durations and sum of all timelines
    """
    duration_disp = {
        'under_2_days': 0,
        'under_week': 0,
        'under_half_year': 0,
        'over_half_year': 0,
    }
    for users in clients.items():
        registered = dateparser.parse(clients[users[0]]['registered'])
        last_login = dateparser.parse(clients[users[0]]['last_login'])
        how_long = ceil((last_login.timestamp() - registered.timestamp()) / DAYS_CONST)

        if how_long < 2:
            duration_disp['under_2_days'] += 1
        elif how_long < 7:
            duration_disp['under_week'] += 1
        elif how_long < HALF_YEAR:
            duration_disp['under_half_year'] += 1
        else:
            duration_disp['over_half_year'] += 1
    return duration_disp, sum(duration_disp.values())


def email_dispersion(clients: dict[str, dict]) -> tuple[dict[str, dict]]:
    """Calculate email dispersion among users.

    Args:
        clients (dict[str, dict]): users and information about them

    Returns:
        tuple[dict[str, dict]]: stat of usage each email and sum of all usages
    """
    email_disp = {}

    for users in clients.items():
        if not validate_email(clients[users[0]]['email']):
            continue
        email_host = clients[users[0]]['email'].split('@')[1]
        if email_host in email_disp.keys():
            email_disp[email_host] += 1
        else:
            email_disp[email_host] = 1

    return email_disp, sum(email_disp.values())


def process_data(path_in: str, path_out: str) -> None:
    """Calculate email hosts and site experience duration dispersion.

    Args:
        path_in (str): path to input file
        path_out (str): path to output file

    Result:
        Json file with calculated stats
    """
    with open(path_in, 'r') as data_file:
        clients = json.loads(data_file.read())
    email_disp, duration_disp = email_dispersion(clients), duration_dispersion(clients)

    stats = {'email_scatter': {}, 'duration_scatter': {}}
    for host in email_disp[0].keys():
        stats['email_scatter'][host] = (email_disp[0][host] / email_disp[1]) * 100

    for duration in duration_disp[0].keys():
        stats['duration_scatter'][duration] = (duration_disp[0][duration] / duration_disp[1]) * 100

    with open(path_out, 'w') as output_file:
        json.dump(stats, fp=output_file, indent=4)
