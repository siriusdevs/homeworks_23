"""Module for calculate stats."""

import re
import sys
from helper import get_dispersion, opener, write_to_json

HALF_YEAR = 183
DURATIONS = (
    ('under_2_days', 2),
    ('under_week', 7),
    ('under_half_year', HALF_YEAR),
    ('over_half_year', float('inf')),
)


def validate_email(email: str) -> bool:
    """Check email for accuracy.

    Args:
        email (str): user email

    Returns:
        bool: valid or invalid email
    """
    pattern = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
    try:
        if re.match(pattern, email) is None:
            return False
    except KeyError:
        return False
    return True


def duration_dispersion(clients: dict[str, dict]) -> tuple[dict[str, dict], int]:
    """Calculate duration on site for each user.

    Args:
        clients (dict[str, dict]): dict of users information

    Returns:
        tuple[dict[str, dict], int]: calculated durations and sum of them
    """
    duration_mask = {key[0]: 0 for key in DURATIONS}
    for users in clients.items():
        how_long = get_dispersion(users[1])
        for duration in DURATIONS:
            if how_long < duration[1]:
                duration_mask[duration[0]] += 1
                break
        sum_durations = sum(duration_mask.values())
    return duration_mask, sum_durations if sum_durations else 1


def email_dispersion(clients: dict[str, dict]) -> tuple[dict[str, dict], int]:
    """Calculate email dispersion among users.

    Args:
        clients (dict[str, dict]): users and information about them

    Raises:
        KeyError: register or last login date is missing

    Returns:
        tuple[dict[str, dict]]: stat of usage each email and sum of all usages
    """
    email_disp = {}
    count_emails = 0

    for users in clients.items():
        if not validate_email(users[1]['email']):
            continue
        email_host = users[1]['email'].split('@')[1]
        count_emails += 1
        if email_host in email_disp.keys():
            email_disp[email_host] += 1
        else:
            email_disp[email_host] = 1
    if not count_emails:
        sys.stdout.write(str('data doesn`t have email fields!'))
        sys.exit(1)
    return email_disp, sum(email_disp.values())


def process_data(path_in: str, path_out: str) -> None:
    """Calculate email hosts and site experience duration dispersion.

    Args:
        path_in (str): path to input file
        path_out (str): path to output file

    Raises:
        ValueError: file is empty error

    Result:
        Json file with calculated stats
    """
    clients = opener(path_in)

    if not clients:
        sys.stdout.write('data file is empty!')
        sys.exit(1)

    email_disp, duration_disp = email_dispersion(clients), duration_dispersion(clients)

    stats = {'email_scatter': {}, 'duration_scatter': {}}
    for host in email_disp[0].keys():
        stats['email_scatter'][host] =  \
            round((email_disp[0][host] / email_disp[1]) * 100, 2)

    for duration in duration_disp[0].keys():
        stats['duration_scatter'][duration] = \
            round((duration_disp[0][duration] / duration_disp[1]) * 100, 2)
    write_to_json(path_out, stats)
