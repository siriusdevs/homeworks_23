"""Generate module."""


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
