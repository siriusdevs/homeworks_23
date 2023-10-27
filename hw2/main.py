"""Module for calculating users' stats from users' data and outputting it to a new json."""
import json

import create_stats
import increment_field


def process_data(users_path: str, result_path: str) -> None:
    """Calculate users' stats from users' data json file and write it to a new json file.

    Args:
        users_path (str): the path that has users' data in json format.
        result_path (str): the path that will been written in users' stats in json format.
    """
    with open(users_path) as users_file:
        users: dict[str, dict[str, str | int]] = json.load(users_file)

    users_domains: dict[str, int] = {}
    users_by_year: dict[str, int] = {}
    users_count: int = 0

    for user in users.values():
        email_domain = str(user['email']).split('@')[-1]  # str because email can be int

        increment_field.increment_field(users_domains, email_domain)
        increment_field.increment_field(users_by_year, str(user['age']))
        users_count += 1

    with open(result_path, 'w') as result_file:
        json.dump(
            {
                'domains': create_stats.create_stats(users_domains, users_count),
                'years': create_stats.create_stats(users_by_year, users_count),
            },
            result_file,
            indent=2,
        )
