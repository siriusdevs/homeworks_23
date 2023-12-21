"""Functions for processing data about clients."""
import json

from utilites import get_age_stats, get_last_login_stats


def process_data(input_file: str, output_file: str) -> int:
    """
    Read data from input_file, calculate stats, and write it to output_file.

    Args:
        input_file: json file with data about clients
        output_file: json file with stats

    Returns:
        0 if all is ok
        1 if input_file not found
        2 if input_file is not a valid json file
        3 if output_file not found
        4 if output_file is not writable
    """
    try:
        with open(input_file, 'r') as input_file_data:
            input_dict = json.load(input_file_data)
    except FileNotFoundError:
        return 1
    except json.decoder.JSONDecodeError:
        return 2

    stats = {
        'age_stats': get_age_stats(input_dict),
        'last_login_stats': get_last_login_stats(input_dict),
    }
    try:
        with open(output_file, 'w') as output_file_data:
            json.dump(stats, output_file_data, indent=4)
    except FileNotFoundError:
        return 3
    except PermissionError:
        return 4
    return 0
