"""The module which contains class-helper for process data function."""
import json
from datetime import datetime, timedelta

import msgspec

from hw2.enums import Period
from hw2.schemas import UserDataSchema
from hw2.typesdev import Users

from .common import get_valid_dict_to_str


def user_is_offline_lt_target_period(user_item: dict, target_period: Period) -> bool:
    """Create a function that returns whether the user is offline for less then target period or not.

    Args:
        user_item (dict): the dict that includes all the user params such as age, last_login
        target_period (Period): the value that represents the target period in days

    Returns:
        Bool value whether the user is offline for less then target period or not
    """
    last_login_date = datetime.fromisoformat(user_item['last_login'])
    target_date = timedelta(days=target_period.value)

    return datetime.now() - last_login_date < target_date


class UserStatsUtils:
    """Create the class which helps to simplify and reduce code in process_data function."""

    necessary_user_keys = {'region', 'registered', 'last_login', 'email', 'age'}

    def __init__(self, data_file_path: str, output_file_path: str) -> None:
        """Create initial method of the UserStatsUtils class which sets necessary attributes on instance.

        Args:
            data_file_path (str): the input JSON file with data about users
            output_file_path (str): the output file where we save necessary statistics
        """
        self.data_file_path = data_file_path
        self.output_file_path = output_file_path
        self.all_ages = []

    @property
    def users_data(self) -> Users:
        """The property of the which returns users_data from the input JSON file or raises an error.

        Raises:
            json.JSONDecodeError: if the input JSON file is invalid
            msgspec.ValidationError: if the users data in input JSON file invalid

        Returns:
            the dict of the user's names and its data
        """
        with (
            open(self.data_file_path, 'r') as data_file,
        ):
            with open(self.output_file_path, 'w') as output_file:
                # If the provided JSON file has invalid syntax then an error occurs. \
                # We catch it and write an error message to the output file
                try:
                    users_data: Users = json.load(data_file)
                except json.JSONDecodeError:
                    json.dump(
                        obj={
                            'status': 'Error',
                            'details': {
                                'msg': 'Invalid JSON file provided',
                            },
                        },
                        fp=output_file,
                    )
                    raise

                # If the provided JSON file doesn't satisfy our Users model then an error occurs. \
                # We catch it and write an error message to the output file
                try:
                    self.validate_user_models(users_data)
                except msgspec.ValidationError:
                    json.dump(
                        obj={
                            'status': 'Error',
                            'details': {
                                'msg': 'Validation error for user items',
                            },
                        },
                        fp=output_file,
                    )
                    raise
                return users_data

    @property
    def user_stats(self) -> dict[str, int]:
        """Create a function that returns necessary user statistics.

        Returns:
            The user_stats property
        """
        number_of_users: int = len(self.all_ages)

        if not number_of_users:
            return {}

        half_num_of_users = number_of_users // 2

        median_age: int = self.all_ages[half_num_of_users]
        if number_of_users % 2 == 0:
            median_age = (
                self.all_ages[half_num_of_users] + self.all_ages[half_num_of_users - 1]
            ) // 2
        return {
            'max_age': self.all_ages[-1],
            'min_age': self.all_ages[0],
            'avg_age': sum(self.all_ages) // number_of_users,
            'median_age': median_age,
            'lt_two_days_offline_users_average_age': self.get_lt_period_offline_users_avg_age(
                target_period=Period.two_days,
            ),
            'lt_week_offline_users_average_age': self.get_lt_period_offline_users_avg_age(
                target_period=Period.week,
            ),
            'lt_month_offline_users_average_age': self.get_lt_period_offline_users_avg_age(
                target_period=Period.month,
            ),
            'lt_half_of_year_offline_users_average_age': self.get_lt_period_offline_users_avg_age(
                target_period=Period.half_of_year,
            ),
            'mt_half_of_year_offline_users_average_age':
                self.get_mt_half_of_year_offline_users_avg_age(),
        }

    def validate_user_models(self, users_data: Users) -> None:
        """Create a function that validates all the user data dicts using msgspec model.

        Args:
            users_data (Users): the dict where the keys are the user's name and \
            the value is a dict of the User model attributes

        Raises:
            ValidationError: if any of the users values doesn't have necessary keys \
            then this error raises
        """
        for user_data in users_data.values():
            msgspec.json.decode(
                get_valid_dict_to_str(user_data).encode(),
                type=UserDataSchema,
            )
            if set(user_data.keys()) != type(self).necessary_user_keys:
                raise msgspec.ValidationError

    def get_lt_period_offline_users_avg_age(self, target_period: Period) -> int:
        """Create a function that returns whether the user is offline for lt target period or not.

        Args:
            target_period (Period): the value that represents the target period in days

        Returns:
            The avg age of the filtered by 'num of offline days lt target period' condition users
        """
        filtered_by_offline_period = list(filter(
            lambda user_item: user_is_offline_lt_target_period(user_item, target_period),
            self.users_data.values(),
        ))
        number_of_users = len(filtered_by_offline_period)
        if not number_of_users:
            return 0
        return sum(user['age'] for user in filtered_by_offline_period) // number_of_users

    def get_mt_half_of_year_offline_users_avg_age(self) -> int:
        """Create a function that returns whether the user is offline for more then half of year or not.

        Returns:
            The avg age of the filtered by 'num of offline days more then half of year' \
            condition users
        """
        mt_half_year_offline_users = []
        for user_data in self.users_data.values():
            last_login_date = datetime.fromisoformat(user_data['last_login'])
            target_date = timedelta(days=Period.half_of_year.value)

            if datetime.now() - last_login_date > target_date:
                mt_half_year_offline_users.append(user_data['age'])

        number_of_users = len(mt_half_year_offline_users)
        if not number_of_users:
            return 0
        return sum(mt_half_year_offline_users) // number_of_users
