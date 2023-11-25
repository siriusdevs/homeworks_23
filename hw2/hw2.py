"""Main module."""

import json

from generate_stats import generate_stats
from open_file import open_file


def process_data(file_data_for_stats: str, output_file: str) -> str:
    """Write the statistics.

    Args:
        file_data_for_stats (str): file which has info for stats
        output_file (str): file with final stats

    Returns:
        str: file is written.
    """
    res_dict = {}
    stats = [{}, {}]

    file_data = open_file(file_data_for_stats)
    count_users = len(file_data.keys())

    for user in file_data.keys():
        for name_of_user_data, user_data in file_data[user].items():
            if name_of_user_data == 'region':
                generate_stats(user_data, stats[0], res_dict, count_users, 'City')

            if name_of_user_data == 'registered':
                generate_stats(user_data, stats[1], res_dict, count_users, 'Years')

    with open(output_file, 'w') as result_file:
        result_file.write(json.dumps(res_dict))
        return f'Data was successfully added to {output_file}.'
