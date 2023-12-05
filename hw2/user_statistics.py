"""Calculate user statistics."""

from abc import ABC, abstractmethod
from datetime import date, datetime, timedelta
from typing import Any


def _calculate_percent(amount: int, total: int) -> int:
    if amount == 0:
        return 0
    return 100 * amount / total


class Statistics(ABC):
    """Base class for statistics."""

    @abstractmethod
    def __init__(
        self,
        users_data: dict[dict[str, Any]],
        statistic_field: str,
        output_format: dict[str, Any],
    ) -> None:
        """Init statistics class.

        Args:
            users_data: contains information about users.
            statistic_field: name of the user property key.
            output_format: json file output format.
        """
        self.users_data = users_data
        self.statistic_field = statistic_field
        self.output_format = output_format

    @abstractmethod
    def get_statistics(self) -> dict[str, Any]:
        """Get statistics dict.

        Raises:
            NotImplementedError: function is not implemented

        Returns:
            dict[str, Any]: dict with statistics, key is statistics name.
        """
        raise NotImplementedError

    @property
    def users_data(self) -> dict[dict[str, Any]]:
        """Get users dict with their information.

        Returns:
            dict: users property.
        """
        return self._users_data

    @users_data.setter
    def users_data(self, users_data: dict[dict[str, Any]]) -> None:
        """Set new user_date.

        Args:
            users_data: a dictionary with custom dictionaries that contain properties.
        """
        self._users_data = users_data


class AgeStatistics(Statistics):
    """Calculate age statistics."""

    def __init__(
        self,
        users_data: dict[dict[str, Any]],
        statistics_field_name: str,
        output_format: dict[str, tuple[int | float, int | float]],
    ) -> None:
        """Create statistics with user_date, statistics_field_name and output_format.

        Args:
            users_data: contains information about users.
            statistics_field_name: name of the user property containing the age.
            output_format: key is field name value is age duration
        """
        super().__init__(users_data, statistics_field_name, output_format)

    def get_statistics(self) -> dict[str, Any]:
        """Сounts the percentage of users by age.

        Returns:
            dict: age statistic.
        """
        statistics, ages = {}, []
        for user in self.users_data.values():
            user_age = user.get(self.statistic_field)
            if user_age is not None:
                ages.append(user[self.statistic_field])
        for name, age_range in self.output_format.items():
            concrete_user = self._filter_ages(age_range[0], age_range[1], ages)
            statistics[name] = _calculate_percent(len(concrete_user), len(ages))
        return statistics

    def _filter_ages(self, start_age: int, end_age: int, ages: list[int]):
        return list(filter(lambda age: start_age <= age < end_age, ages))


class DateStatistics(Statistics):
    """Calculacte date statistic."""

    def __init__(
        self,
        users_data: dict[dict[str, Any], Any],
        statistic_field: str,
        output_format: dict[str, timedelta],
        date_format: str = '%Y-%m-%d',
    ) -> None:
        """Create statistics with user_date, statistics_field_name, output_format and date_fromat.

        Args:
            users_data:  contains information about users.
            statistic_field: name of the user property key.
            output_format: key is name, value is date duration.
            date_format: date parsing format.
        """
        super().__init__(users_data, statistic_field, output_format)
        self.date_format = date_format

    def get_statistics(self) -> dict[str, Any]:
        """Сounts the percentage of users by day.

        Returns:
            dict: date statistic.
        """
        dates, statistics = [], {}
        for user in self.users_data.values():
            last_login_date = user.get(self.statistic_field)
            if (last_login_date is not None):
                dates.append(datetime.strptime(last_login_date, self.date_format).date())
        for name, duration in self.output_format.items():
            concrete_user = self._filter_dates(duration[0], duration[1], dates)
            statistics[name] = _calculate_percent(len(concrete_user), len(dates))
        return statistics

    def _filter_dates(
        self,
        furst_duradion: timedelta,
        second_duration: timedelta,
        dates: list[date],
    ) -> list[date]:
        return list(
            filter
            (
                lambda login_date: furst_duradion <= date.today() - login_date < second_duration,
                dates,
            ),
        )
