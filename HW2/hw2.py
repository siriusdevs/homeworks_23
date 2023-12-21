"""Functions for processing data about clients."""
import json

from utilites import get_age_stats, get_last_login_stats


def process_data(input_file: str, output_file: str) -> str:
    """
    Read data from input_file, calculate stats, and write it to output_file.

    Args:
        input_file: json file with data about clients
        output_file: json file with stats

    Returns:
        str: error message
    """
    try:
        with open(input_file, 'r') as input_file_data:
            input_dict = json.load(input_file_data)
    except FileNotFoundError:
        return f'file {input_file} does not exist!'
    except json.decoder.JSONDecodeError:
        return f'file {input_file} is not in JSON format!'

    stats = {
        'age_stats': get_age_stats(input_dict),
        'last_login_stats': get_last_login_stats(input_dict),
    }
    try:
        with open(output_file, 'w') as output_file_data:
            json.dump(stats, output_file_data, indent=4)
    except FileNotFoundError:
        return f'invalid file path {output_file}'
    except PermissionError:
        return f'not permission to write to file {output_file}'
    return 'The prograp was completed without errors.'
