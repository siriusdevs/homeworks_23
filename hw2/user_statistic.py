"""Module for 'UserStatistic class which fills itself with other functions'."""

import json

from ages_operations import get_average_age, get_median_age


class UserStatistic:
    """Class for statistic of users."""

    def __init__(self, ages: list[int], statictic: dict) -> None:
        """init.

        Args:
            ages (list[int]): all ages
            statictic (dict): statistic by years
        """
        self.min_age = min(ages)
        self.avg_age = get_average_age(ages)
        self.max_age = max(ages)
        self.median_age = get_median_age(ages)
        self.statictic = statictic

    def to_json(self):
        """Convert class to json format.

        Returns:
            str: json format of this class
        """
        return json.dumps(self.__dict__)
