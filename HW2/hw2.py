"""Contains functions for processing data from input file and saving results to output file."""

import json
from collections import defaultdict
from datetime import datetime


def process_data(input_file: str, output_file: str):
    """
    Process data from input_file and save results to output_file.

    Args:
        input_file (str): Path to the input file.
        output_file (str): Path to the output file.
    """
    with open(input_file, 'r') as input_filee:
        dataa = json.load(input_filee)

    output_data = get_stat(dataa)

    with open(output_file, 'w') as output_filee:
        json.dump(output_data, output_filee)


def get_stat(dataa: dict) -> dict:
    """
    Return dict with stat.

    Args:
        dataa (dict): Dict with data.

    Returns:
        dict: Dict with stat.
    """
    city_distrib = defaultdict(int)
    year_distrib = defaultdict(int)

    for user in dataa.values():
        city_distrib[user['region']] += 1
        year_distrib[datetime.strptime(user['registered'], '%Y-%m-%d').year] += 1
    total_users = len(dataa.keys())
    city_distrib = {city: count / total_users * 100 for city, count in city_distrib.items()}
    year_distrib = {year: count / total_users * 100 for year, count in year_distrib.items()}
    return {
        'city_distribution': city_distrib,
        'year_distribution': year_distrib,
    }
