"""Module that includes the implemented function from Vasilenko's second task."""
import json
from datetime import datetime, timedelta
from enum import Enum

NOW = datetime.now()


class Period(Enum):
    """Class-enum representing all the necessary periods."""

    two_days = 2
    week = 7
    month = 31
    half_of_year = 182


def find_insertion_index(nums: list[int], target: int) -> int:
    """Create function that finds the index for insertion using binary search algorithm and returns it.

    Args:
        nums (list[int]): the list where we want to insert the target number
        target (int): the value we want to insert into the list

    Returns:
        Index to insert
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left


def user_was_offline_lt_target_num_of_days(user_item: dict, target_period: Period) -> bool:
    """Create a function that returns whether the user is offline for less then target period or not.

    Args:
        user_item (dict): the dict that includes all the user params such as age, last_login, etc.
        target_period (Period): the value that represents the target period in days

    Returns:
        Bool value whether the user is offline for less then target period or not
    """
    last_login_date = datetime.fromisoformat(user_item['last_login'])
    target_date = timedelta(days=target_period.value)

    return NOW - last_login_date < target_date


def get_lt_period_offline_users_avg_age(users_data: dict, target_period) -> int:
    """Create a function that returns whether the user is offline for lt target period or not.

    Args:
        users_data (dict): the dict that includes data about all users
        target_period (Period): the value that represents the target period in days

    Returns:
        The avg age of the filtered by 'num of offline days lt target period' condition users
    """
    filtered_by_offline_period = list(filter(
        lambda user_item: user_was_offline_lt_target_num_of_days(user_item, target_period),
        users_data.values(),
    ))
    number_of_users = len(filtered_by_offline_period)
    if not number_of_users:
        return 0
    return sum(user['age'] for user in filtered_by_offline_period) // number_of_users


def get_mt_half_of_year_offline_users_avg_age(users_data) -> int:
    """Create a function that returns whether the user is offline for more then half of year or not.

    Args:
        users_data (dict): the dict that includes data about all users

    Returns:
        The avg age of the filtered by 'num of offline days more then half of year' condition users
    """
    mt_half_year_offline_users = []
    for user_item in users_data.values():
        last_login_date = datetime.fromisoformat(user_item['last_login'])
        target_date = timedelta(days=Period.half_of_year.value)

        if NOW - last_login_date > target_date:
            mt_half_year_offline_users.append(user_item['age'])

    number_of_users = len(mt_half_year_offline_users)
    if not number_of_users:
        return 0
    return sum(mt_half_year_offline_users) // number_of_users


def process_data(data_file_path: str, output_file_path: str) -> None:
    """Create the main function that reads users data from data_file \
        and writes the necessary statistics by task into output_file.

    Args:
        data_file_path (str): the path to file with users data
        output_file_path (str): the path to file in which we save the necessary statistics
    """
    with open(data_file_path, 'r') as data_file:
        users_data: dict = json.load(data_file)

    all_ages = []
    for user in users_data.values():
        user_age = user['age']
        all_ages.insert(find_insertion_index(all_ages, user_age), user_age)

    number_of_users = len(all_ages)

    median_age = all_ages[number_of_users // 2]
    if number_of_users % 2 == 0:
        median_age = (all_ages[number_of_users // 2] + all_ages[number_of_users // 2 - 1]) // 2

    with open(output_file_path, 'w') as output_file:
        json.dump(
            obj={
                'max_age': all_ages[-1],
                'min_age': all_ages[0],
                'avg_age': sum(all_ages) // number_of_users,
                'median_age': median_age,
                'lt_two_days_offline_users_average_age': get_lt_period_offline_users_avg_age(
                    users_data=users_data,
                    target_period=Period.two_days,
                ),
                'lt_week_offline_users_average_age': get_lt_period_offline_users_avg_age(
                    users_data=users_data,
                    target_period=Period.week,
                ),
                'lt_month_offline_users_average_age': get_lt_period_offline_users_avg_age(
                    users_data=users_data,
                    target_period=Period.month,
                ),
                'lt_half_of_year_offline_users_average_age': get_lt_period_offline_users_avg_age(
                    users_data=users_data,
                    target_period=Period.half_of_year,
                ),
                'mt_half_of_year_offline_users_average_age':
                    get_mt_half_of_year_offline_users_avg_age(
                        users_data=users_data,
                    ),
            },
            fp=output_file,
            indent=4,
            ensure_ascii=False,
        )
