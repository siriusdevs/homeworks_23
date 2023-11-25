"""Opening module."""


import json


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
