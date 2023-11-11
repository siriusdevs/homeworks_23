"""Contain class-helper for process data function."""
import json
import logging
import os
from dataclasses import dataclass
from datetime import datetime, timedelta

import hw2.src.bbtypes as bbtypes
import hw2.src.schemas as schemas
from hw2.src.enums import Period

from .common import create_file, find_insertion_index
from .validate_data_file import validate_data_file


@dataclass
class UserStatsUtils:
    """Help to simplify and reduce the code in process_data function."""

    data_file_path: str
    output_file_path: str
    logger: logging.Logger

    def __post_init__(self):
        """Post initialization logic."""
        if not os.path.exists(self.output_file_path):
            self.logger.info('Output file does not exist. Creating..')
            create_file(self.output_file_path)

        data_file_is_valid, error_msg = validate_data_file(
            self.data_file_path,
        )
        self.data_file_is_valid = data_file_is_valid
        self.error_msg = error_msg

    @property
    def users(self) -> schemas.Users:
        """The users data.

        Returns:
            List of user models.
        """
        with open(self.data_file_path, 'r') as data_file:
            users_data: bbtypes.Users = json.load(data_file)
        return self.get_users_as_models(users_data)

    @property
    def user_stats(self) -> bbtypes.UserStats:
        """The necessary user stats.

        Returns:
            The user_stats property
        """
        number_of_users: int = 0
        all_ages: list[int] = []

        for user in self.users:
            user_age: int = user.age
            all_ages.insert(find_insertion_index(all_ages, user_age), user_age)
            number_of_users += 1

        if not number_of_users:
            return {}

        half_num_of_users = number_of_users // 2

        median_age: int = all_ages[half_num_of_users]
        if number_of_users % 2 == 0:
            median_age = (
                (all_ages[half_num_of_users] + all_ages[half_num_of_users - 1])
                // 2
            )
        return {
            'max_age': all_ages[-1],
            'min_age': all_ages[0],
            'avg_age': sum(all_ages) // number_of_users,
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
            'gt_half_of_year_offline_users_average_age':
                self.get_gt_half_of_year_offline_users_avg_age(),
        }

    @staticmethod
    def user_is_offline_lt_target_period(
        user_item: schemas.User,
        target_period: Period,
    ) -> bool:
        """Check whether the user is offline for less then target period or not.

        Args:
            user_item (User): the dict that includes all the user params such as age, last_login
            target_period (Period): the value that represents the target period in days

        Returns:
            Bool value whether the user is offline for less then target period or not
        """
        last_login_date = datetime.fromisoformat(str(user_item.last_login))
        target_date = timedelta(days=target_period.value)

        return datetime.now() - last_login_date < target_date

    def get_users_as_models(self, users_data):
        """Return users as list of the msgspec class-models.

        Args:
            users_data (Users): the dict where the keys are the user's name and \
            the value is a dict of the User model attributes

        Returns:
            List of user models.
        """
        users: schemas.Users = []
        for user_data in users_data.values():
            users.append(schemas.User(**user_data))
        return users

    def get_lt_period_offline_users_avg_age(self, target_period: Period) -> int:
        """Get the avg age of the filtered by \
        'num of offline days lt target period' condition users.

        Args:
            target_period (Period): the value that represents the target period in days

        Returns:
            The avg age of the filtered by 'num of offline days lt target period' condition users
        """
        filtered_by_offline_period = list(filter(
            lambda user_item: self.user_is_offline_lt_target_period(user_item, target_period),
            self.users,
        ))
        number_of_users = len(filtered_by_offline_period)
        if not number_of_users:
            return 0
        return sum(user.age for user in filtered_by_offline_period) // number_of_users

    def get_gt_half_of_year_offline_users_avg_age(self) -> int:
        """Check if the user has been offline for more than half of the year or not.

        Returns:
            The avg age of the filtered by 'num of offline days more then half of year' \
            condition users
        """
        gt_half_of_year_offline_users = []
        for user in self.users:
            last_login_date = datetime.fromisoformat(str(user.last_login))
            target_date = timedelta(days=Period.half_of_year.value)

            if datetime.now() - last_login_date > target_date:
                gt_half_of_year_offline_users.append(user.age)

        number_of_users = len(gt_half_of_year_offline_users)
        if not number_of_users:
            return 0
        return sum(gt_half_of_year_offline_users) // number_of_users
