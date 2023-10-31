"""Module that includes the implemented function from Vasilenko's second task."""
import json
from typing import NoReturn

from hw2.utils import UserStatsUtils, find_insertion_index


def process_data(data_file_path: str, output_file_path: str) -> NoReturn:
    """Create the main function that reads users data from data_file \
        and writes the necessary statistics by task into output_file.

    Args:
        data_file_path (str): the path to file with users data
        output_file_path (str): the path to file in which we save the necessary statistics
    """
    user_stats_utils: UserStatsUtils = UserStatsUtils(data_file_path, output_file_path)

    all_ages: list[int] = []
    for user in user_stats_utils.users:
        user_age: int = user.age
        all_ages.insert(find_insertion_index(all_ages, user_age), user_age)

    user_stats_utils.all_ages = all_ages
    with open(output_file_path, 'w') as output_file:
        json.dump(
            obj=user_stats_utils.user_stats,
            fp=output_file,
            indent=4,
            ensure_ascii=False,
        )
