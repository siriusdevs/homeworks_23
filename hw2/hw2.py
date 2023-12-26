"""Module hw2."""
import json
import re
import statistics
from pathlib import Path

AGE = 'age'
MAX_AGE = 'max_age'
MIN_AGE = 'min_age'
AVERAGE_AGE = 'average_age'
MEDIAN_AGE = 'median_age'


def process_data(src_file: str = 'input.json', dst_file: str = 'output.json') -> None:
    """Process data from the source file and write the result to the destination file.

    Args:
        src_file (str): The path to the source file.
        dst_file (str): The path to the destination file.

    Raises:
        ValueError: If an error occurs during data processing.
        FileNotFoundError: If the source file or destination file is not found.
    """
    try:
        _collect_results(src_file, dst_file)
    except (ValueError, FileNotFoundError) as error:
        with open(dst_file, 'w') as output_json:
            json.dump({'error': str(error)}, output_json, indent=4)
        raise


def _collect_results(src_file: str, dst_file: str) -> None:
    """
    Collect results from the source file and write them to the destination file.

    Args:
        src_file (str): The path to the source file.
        dst_file (str): The path to the destination file.
    """
    output_path = Path(dst_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(src_file, 'r') as input_json:
        users = json.load(input_json)
    years_result = _year_percentage(users)
    age_result = _age_stats(users)
    full_result = {
        **age_result,
    }
    full_result.update({'years_statistics': years_result})
    with open(dst_file, 'x') as output_json:
        json.dump(full_result, output_json, indent=4)


def _age_stats(users: dict) -> dict:
    """
    Calculate statistics for user ages.

    Args:
        users (dict): Dictionary with user data.

    Returns:
        dict: Age statistics including maximum, minimum, average, and median age.
    """
    result_ages = {}
    ages = [users[user][AGE] for user in users] or [0]
    result_ages[MAX_AGE] = max(ages)
    result_ages[MIN_AGE] = min(ages)
    result_ages[AVERAGE_AGE] = sum(ages) / max(len(ages), 1)
    result_ages[MEDIAN_AGE] = statistics.median(ages)
    return result_ages


def _year_percentage(users: dict) -> dict:
    """
    Calculate the percentage of user registrations for each year.

    Args:
        users (dict): Dictionary with user data.

    Returns:
        dict: Percentage distribution of user registration years.

    Raises:
        ValueError: If an error occurs during percentage calculation.
    """
    years = {}
    for user in users.keys():
        if 'registered' not in users[user]:
            return ValueError(f'No "registered" entry in user "{user}"')
        year = users[user]['registered']
        if re.match(r'\d{4}-\d{2}-\d{2}', year):
            year = year.split('-')[0]
        else:
            raise ValueError(f'Incorrect date format - {year}. Use YYYY-MM-DD')
        if years.get(year):
            years[year] += 1
        else:
            years[year] = 1
    count_of_years = len(years)
    for elem in years:
        years[elem] = (years.get(elem, 0) / max(count_of_years, 1)) * 100
    return years
