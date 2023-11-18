"""Module for calculating users' stats from users' data and outputting it to a new json."""
import json
import os

import increment_field
import transform_stats


def process_data(users_path: str, result_path: str) -> None:
    """Calculate users' stats from users' data json file and write it to a new json file.

    Args:
        users_path (str): the path that has users' data in json format.
        result_path (str): the path that will been written in users' stats in json format.
    """
    for_not_specified = 'not_specified'

    for path in (users_path, result_path):
        if os.path.exists(path):
            continue

        raise FileNotFoundError(
            f'Check your given file ({path} in {os.getcwd()}) because it was not found!',
        )

    with open(users_path) as users_file:
        users: dict[str, dict[str, str | int]] = json.load(users_file)

    users_domains: dict[str, int] = {}
    users_by_year: dict[str, int] = {}
    users_count: int = 0

    for user_name, user_statistics in users.items():
        email = user_statistics.get('email', for_not_specified)
        years = user_statistics.get('age', for_not_specified)

        if not isinstance(email, str):
            raise TypeError(f'The email of {user_name} must be a string!')

        if not isinstance(years, int):
            raise TypeError(f'The years of {user_name} must be a integer!')

        if email != for_not_specified:
            email = email.split('@')[-1]

        increment_field.increment_field(users_domains, email)
        increment_field.increment_field(users_by_year, str(years))
        users_count += 1

    with open(result_path, 'w') as result_file:
        json.dump(
            {
                'domains': transform_stats.transform_stats(users_domains, users_count),
                'years': transform_stats.transform_stats(users_by_year, users_count),
            },
            result_file,
            indent=2,
        )
