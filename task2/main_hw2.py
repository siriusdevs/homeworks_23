"""Main module."""
import json
import os


def process_data(file_data_for_stats: str, output_file: str) -> str:

    """Procces_data function for writing the statistics.

    Args:
        file_data_for_stats (str): file which has info for stats
        output_file (str): file with final stats

    Returns:
        str: file is written.
    """

    res_dict = {}
    stats = [{}, {}]

    file_data = open_file(file_data_for_stats)
    count_users = max(len(file_data), 1)

    for user in file_data.keys():

        for name_of_user_data, user_data in file_data[user].items():

            if name_of_user_data == 'region':
                generate_stats(user_data, stats[0], res_dict, count_users, 'City')

            if name_of_user_data == 'registered':
                generate_stats(user_data, stats[1], res_dict, count_users, 'Years')

    make_dir(output_file)

    with open(output_file, 'w') as result_file:
        result_file.write(json.dumps(res_dict))
    return f'Data was successfully added to {output_file}.'


def make_dir(output_file):

    """Initialize the path.

    Args:
        output_file (str): file for stats
    """

    os.makedirs(os.path.dirname(output_file), exist_ok=True)


def open_file(file_with_data: str) -> dict:

    """Open json file.

    Args:
        file_with_data (str): json file

    Returns:
        dict: info from json file
    """

    try:
        with open(file_with_data, 'r') as name_file:
            return json.loads(name_file.read())
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


def generate_stats(
    user_data: str,
    dict_stats: dict,
    res_dict: dict,
    count_users: int,
    text_key: str,
) -> dict:

    """Generate a dict with statistics.

    Args:
        user_data (str): user information from json file
        dict_stats (dict): dict with statistics
        res_dict (dict): final stats for json file
        count_users (int): amount of users from json file
        text_key (str): cities/years

    Returns:
        dict: statistics
    """

    if dict_stats.get(user_data):
        dict_stats[user_data] += 1 / count_users * 100

    else:
        dict_stats[user_data] = 1 / count_users * 100

    res_dict[text_key] = dict_stats

    return res_dict
