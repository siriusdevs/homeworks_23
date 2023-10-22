"""Module that includes the implemented function from Vasilenko's second task."""
import json
from datetime import datetime, timedelta
from enum import Enum

DEFAULT_DATE_FORMAT = '%Y-%m-%d'

NOW = datetime.now()


class Period(Enum):
    TWO_DAYS = 2
    WEEK = 7
    MONTH = 31
    HALF_OF_YEAR = 365 // 2


def find_insertion_index(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left


def user_was_offline_lt_target_num_of_days(user_item, target_period) -> bool:
    last_login_date = datetime.strptime(user_item['last_login'], DEFAULT_DATE_FORMAT)
    target_date = timedelta(days=target_period.value)

    return NOW - last_login_date < target_date


def get_lt_certain_period_offline_users_average_age(users_data, target_period) -> int:
    filtered_by_offline_period = list(filter(
        lambda user_item: user_was_offline_lt_target_num_of_days(user_item, target_period),
        users_data.values()
    ))
    number_of_users = len(filtered_by_offline_period)
    if not number_of_users:
        return 0
    return sum(map(lambda user: user['age'], filtered_by_offline_period)) // number_of_users


def get_mt_half_of_year_offline_users_avg_age(users_data) -> int:
    mt_half_year_offline_users = []
    for user_item in users_data.values():
        last_login_date = datetime.strptime(user_item['last_login'], DEFAULT_DATE_FORMAT)
        target_date = timedelta(days=Period.HALF_OF_YEAR.value)

        if NOW - last_login_date > target_date:
            mt_half_year_offline_users.append(user_item['age'])

    number_of_users = len(mt_half_year_offline_users)
    if not number_of_users:
        return 0
    return sum(mt_half_year_offline_users) // number_of_users


def process_data(data_file_path: str, output_file_path: str) -> None:
    with open(data_file_path, 'r') as data_file:
        users_data: dict = json.load(data_file)

    all_ages = []
    min_age, max_age = float('inf'), 0
    for user in users_data.values():
        user_age = user['age']
        if user_age > max_age:
            max_age = user_age
        if user_age < min_age:
            min_age = user_age
        insertion_index = find_insertion_index(all_ages, user_age)
        all_ages.insert(insertion_index, user_age)

    number_of_users = len(all_ages)

    avg_age = sum(all_ages) // number_of_users
    median_age = all_ages[number_of_users // 2]
    if number_of_users % 2 == 0:
        median_age = (all_ages[number_of_users // 2] + all_ages[number_of_users // 2 - 1]) // 2

    lt_two_days_offline_users_average_age = get_lt_certain_period_offline_users_average_age(
        users_data=users_data,
        target_period=Period.TWO_DAYS,
    )
    lt_week_offline_users_average_age = get_lt_certain_period_offline_users_average_age(
        users_data=users_data,
        target_period=Period.WEEK,
    )
    lt_month_offline_users_average_age = get_lt_certain_period_offline_users_average_age(
        users_data=users_data,
        target_period=Period.MONTH,
    )
    lt_half_of_year_offline_users_average_age = get_lt_certain_period_offline_users_average_age(
        users_data=users_data,
        target_period=Period.HALF_OF_YEAR,
    )
    mt_half_of_year_offline_users_average_age = get_mt_half_of_year_offline_users_avg_age(
        users_data=users_data,
    )

    with open(output_file_path, 'w') as output_file:
        json.dump(
            obj={
                'max_age': max_age,
                'min_age': min_age,
                'avg_age': avg_age,
                'median_age': median_age,
                'lt_two_days_offline_users_average_age': lt_two_days_offline_users_average_age,
                'lt_week_offline_users_average_age': lt_week_offline_users_average_age,
                'lt_month_offline_users_average_age': lt_month_offline_users_average_age,
                'lt_half_of_year_offline_users_average_age': lt_half_of_year_offline_users_average_age,
                'mt_half_of_year_offline_users_average_age': mt_half_of_year_offline_users_average_age,
            },
            fp=output_file,
            indent=4,
            ensure_ascii=False
        )
