"""Module for calculating the percentage of online and hosts."""

import datetime
import json

TWO_DAYS = 2
WEEK = 7
MONTH = 30
HALF_YEAR = 182
MORE_THAN_HALF_YEAR = 1e9


class NoRequiredDataException(Exception):
    """
    An exception thrown if required data is missing.

    Attributes:
        message (str): Message about missing required data.

    Methods:
        __init__(): The class initializes an exception object with the specified message.

    Usage:
        raise NoRequiredDataException()
    """

    def __init__(self, message: str) -> None:
        """
        Construct for the NoRequiredDataException class.

        Initializes an exception object with a message that required data is missing.

        Parameters:
            message: str - error message.
        """
        super().__init__(f'Error: {message}')


def process_data(input_file_json: str, output_file_json: str, fixed_data: str = None) -> None:
    """
    Process data from a JSON file.

    Args:
        input_file_json: str - represents the path to the JSON file.
        output_file_json: str - represents the path to the output JSON file.
        fixed_data: str = None - date to calculate the interval.

    Retuns:
        None
    """
    try:
        _record_all_data(input_file_json, output_file_json, fixed_data)
    except NoRequiredDataException as error:
        with open(output_file_json, 'w') as output:
            json.dump({'error': str(error)}, output, indent=4)


def _record_all_data(input_file_json: str, output_file_json: str, fixed_data: str = None) -> None:
    with open(input_file_json, 'r') as config:
        information = json.load(config)
    all_hosts = host_output(information)
    percentage_of_every_host = interst_calculation(all_hosts)
    percentage_of_online = online_calculation(users_dates(information), fixed_data=fixed_data)
    all_percentage = percentage_of_every_host
    all_percentage.update(percentage_of_online)
    with open(output_file_json, 'w') as output:
        json.dump(all_percentage, output, indent=4)


def host_output(information: dict) -> list[str]:
    """
    Get user hosts from a JSON file.

    Args:
        information: dict - all information from JSON file.

    Returns:
        hosts: list[str] - list for hosts.

    Raises:
        NoRequiredDataException: an error indicating that the required data is missing.
    """
    hosts = []
    for person in information.keys():
        if information[person].get('email') is None:
            raise NoRequiredDataException('No emails')
        if information[person]['email'].count('@') == 1:
            host = information[person]['email'].split('@')[-1]
            hosts.append(host)
    return hosts


def interst_calculation(hosts: list[str]) -> dict[str, float]:
    """
    Calculate percentages hosts.

    Args:
        hosts: list[str] - list for hosts.

    Returns:
        quantity_hosts: dict[str, float] - hosts and their percentages.

    """
    quantity_hosts = {}
    for host in set(hosts):
        quantity = str(hosts.count(host) / len(hosts) * 100)
        quantity_hosts.update({host: f'{quantity} %'})
    return quantity_hosts


def users_dates(information: dict) -> list[str]:
    """
    Get user registration time from file.

    Args:
        information: dict - all information from JSON file.

    Returns:
        user_lastlogin_date: list[str] - list with user last login date.

    Raises:
        NoRequiredDataException: an error indicating that the required data is missing.
    """
    user_lastlogin_date = []
    for user in information.keys():
        if information[user].get('last_login') is None:
            raise NoRequiredDataException('No lastlogins')
        if information[user]['last_login'].count('-') == 2:
            user_data = information[user]['last_login']
            user_lastlogin_date.append(user_data)
    return user_lastlogin_date


def online_calculation(user_lastlogin_date: list[str], fixed_data: str) -> dict[str, float]:
    """
    Calculate of percentage of online user.

    Args:
        user_lastlogin_date: list[str] - list with user last login date.
        fixed_data: str - current date.

    Returns:
        online_status: dict[str, float] - dict with percentage of how many users use mail.
    """
    online_status = {
        'two_days_online': 0,
        'one_week_online': 0,
        'one_month_online': 0,
        'half_year_online': 0,
        'more_half_year_online': 0,
    }
    if fixed_data is None:
        fixed_data = datetime.date.today()
    else:
        fixed_data = datetime.date.fromisoformat(fixed_data)

    new_user_lastlogin = []
    intervals = [
        ('two_days_online', datetime.timedelta(days=TWO_DAYS)),
        ('one_week_online', datetime.timedelta(days=WEEK)),
        ('one_month_online', datetime.timedelta(days=MONTH)),
        ('half_year_online', datetime.timedelta(days=HALF_YEAR)),
        ('more_half_year_online', datetime.timedelta(days=MORE_THAN_HALF_YEAR-1)),
    ]
    for login_date in user_lastlogin_date:
        new_user_lastlogin.append(datetime.date(*list(map(int, login_date.split('-')))))
        for interval in intervals:
            if fixed_data - new_user_lastlogin[-1] <= interval[1]:
                online_status[interval[0]] += 1
                break

    for status in online_status:
        current_status = str(online_status.get(status) / len(online_status) * 100)
        online_status.update({status: f'{current_status} %'})
    return online_status
