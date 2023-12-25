"""Count statistic for each user at json-files."""
import json
from datetime import datetime


def filter_users(input_data: dict) -> tuple[dict, dict]:
    """
    Функция фильтрации пользователей.

    Args:
        input_data (dict): словарь входных данных.

    Returns:
        tuple[dict, dict]: отфильтрованный словарь.
    """
    regions = {}
    registration_years = {}

    for _, user_info in input_data.items():
        region = user_info['region']
        registration_year = datetime.strptime(
            user_info['registered'], '%Y-%m-%d',
        ).year
        if region:
            if region not in regions:
                regions[region] = 0
            regions[region] += 1

        if registration_year:
            if registration_year not in registration_years:
                registration_years[registration_year] = 0
            registration_years[registration_year] += 1

    return regions, registration_years


def count_statistic(input_data: dict) -> dict:
    """
    Функция подсчета статистики.

    Args:
        input_data (dict): входной словарь.

    Returns:
        dict: словарь с собранной статистикой.
    """
    regions, registration_years = filter_users(input_data)

    return {
        'region_distribution': {
            region: (count / len(input_data)) *
            100 for region, count in regions.items()
        },
        'registration_years_distribution': {
            year: (count / len(input_data)) *
            100 for year, count in registration_years.items()
        },
    }


def process_data(input_path: str, output_path: str) -> None:
    """
    Analyzes the existing JSON data and collects new statistics.

    Args:
        input_path: Path where the .json file is located.
        output_path: Path for writing the resulting .json file.
    """
    with open(input_path, 'r') as input_file:
        input_data = json.load(input_file)

    stats = count_statistic(input_data)

    with open(output_path, 'w') as output_file:
        json.dump(stats, output_file)


process_data('data_hw2.json', 'hw2/data_result.json')
