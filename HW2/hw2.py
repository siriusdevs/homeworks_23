"""Contains functions for processing data from input file and saving results to output file."""

import json
from datetime import datetime


def process_data(input_file: str, output_file: str) -> str:
    """
    Process data from input_file and save results to output_file.

    Args:
        input_file (str): Path to the input file.
        output_file (str): Path to the output file.

    Returns:
        str: A status message indicating the result of the data processing.
    """
    try:
        with open(input_file, 'r') as input_filee:
            dataa = json.load(input_filee)
    except FileNotFoundError:
        return f'{input_file} not found'
    except json.decoder.JSONDecodeError:
        return f'{input_file} has not json'

    output_data = get_stat(dataa)

    try:
        with open(output_file, 'w') as output_filee:
            json.dump(output_data, output_filee)
    except FileNotFoundError:
        return f'invalid file path {output_file}'
    except PermissionError:
        return f'not permission to write to file {output_file}'


def get_stat(dataa: dict) -> dict:
    """
    Return dict with stat.

    Args:
        dataa (dict): Dict with data.

    Returns:
        dict: Dict with stat.
    """
    city_distrib = {}
    year_distrib = {}

    try:
        for user in dataa.keys():
            if 'region' in dataa[user] and 'registered' in dataa[user]:
                city = dataa[user]['region']
                city_distrib[city] = city_distrib.get(city, 0) + 1
                year_of_regisrt = datetime.strptime(dataa[user]['registered'], '%Y-%m-%d').year
                year_distrib[year_of_regisrt] = year_distrib.get(year_of_regisrt, 0) + 1
            else:
                return f'Keys not found in user data: {user}'
    except Exception:
        return 'Error processing data'
    total_users = len(dataa.keys())
    city_distrib = {city: count / total_users * 100 for city, count in city_distrib.items()}
    year_distrib = {year: count / total_users * 100 for year, count in year_distrib.items()}
    return {
        'city_distribution': city_distrib,
        'year_distribution': year_distrib,
    }
