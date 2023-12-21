"""Homework about processing user data statistics."""

import json
import os
from datetime import datetime

AGE_CATEGORIES = ('0-18', '18-25', '25-45', '45-60', '60+')
ONLINE_STATUS_CATEGORIES = ('<2 days', '1 week', '1 month', '6 months', '>6 months')

AGE_THRESHOLD = (18, 25, 45, 60)
ONLINE_THRESHOLD = (2, 7, 30, 180)


def process_data(input_file_path: str, output_file_path: str) -> None:
    """Process data from a JSON file and generate statistics.

    Args:
        input_file_path (str): The path to the input JSON file.
        output_file_path (str): The path to the output JSON file.

    Returns:
        output (dict): Output data with calculated percentages.
    """
    try:
        with open(input_file_path, 'r') as input_file:
            database = json.load(input_file)
    except FileNotFoundError:
        return {'msg': 'Input file not found'}

    total_users = len(database)
    age_categories = {cat: 0 for cat in AGE_CATEGORIES}
    online_status = {cat: 0 for cat in ONLINE_STATUS_CATEGORIES}

    for user in database.values():
        categorize_age(user, age_categories)
        calculate_online_status(user, online_status)

    output = {
        'age_percentages': calculate_percentages(age_categories, total_users),
        'online_percentages': calculate_percentages(online_status, total_users),
    }

    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
    try:
        with open(output_file_path, 'w') as out_file:
            json.dump(output, out_file, indent=2)
    except OSError as error:
        return {'msg': f'Error writing to output file: {error}'}
    return output


def categorize_age(user: dict, age_categories: dict) -> None:
    """Categorize the age of a user and update the age categories dictionary.

    Args:
        user (dict): User data dictionary.
        age_categories (dict): Dictionary to store the count of users in different age categories.
    """
    age = user.get('age', 0)
    category_switch = {
        age <= AGE_THRESHOLD[0]: '0-18',
        AGE_THRESHOLD[0] < age <= AGE_THRESHOLD[1]: '18-25',
        AGE_THRESHOLD[1] < age <= AGE_THRESHOLD[2]: '25-45',
        AGE_THRESHOLD[2] < age <= AGE_THRESHOLD[3]: '45-60',
        age > AGE_THRESHOLD[3]: '60+',
    }
    age_category = category_switch.get(True, 'Unknown')
    age_categories[age_category] += 1


def calculate_online_status(user: dict, online_status: dict) -> None:
    """Calculate the online status of a user and update the online status dictionary.

    Args:
        user (dict): User data dictionary.
        online_status (dict): Count of users in different online status categories.
    """
    last_login_date = datetime.strptime(user.get('last_login', ''), '%Y-%m-%d')
    days_since_last_login = (datetime.now() - last_login_date).days

    status_switch = {
        days_since_last_login < ONLINE_THRESHOLD[0]: '<2 days',
        ONLINE_THRESHOLD[0] <= days_since_last_login < ONLINE_THRESHOLD[1]: '1 week',
        ONLINE_THRESHOLD[1] <= days_since_last_login < ONLINE_THRESHOLD[2]: '1 month',
        ONLINE_THRESHOLD[2] <= days_since_last_login < ONLINE_THRESHOLD[3]: '6 months',
        days_since_last_login >= ONLINE_THRESHOLD[3]: '>6 months',
    }
    # If the number of days does not match any of the existing keys, the default value is Unknown
    online_status_category = status_switch.get(True, 'Unknown')
    online_status[online_status_category] += 1


def calculate_percentages(data_dict: dict, total_users: dict) -> dict:
    """Calculate the percentage of users in each category.

    Args:
        data_dict (dict): Dictionary containing the count of users in different categories.
        total_users (dict): Total number of users.

    Returns:
        dict: Dictionary containing the percentage of users in each category.
    """
    return {key: (count / total_users) * 100 for key, count in data_dict.items()}
