"""Homework about processing user data statistics."""

import json
from datetime import datetime


def process_data(input_file: str, output_file: str) -> None:
    """Process data from a JSON file and generate statistics.

    Args:
        input_file (str): The path to the input JSON file containing user data.
        output_file (str): The path to the output JSON file where the statistics will be written.
    """
    with open(input_file, 'r') as file:
        data = json.load(file)

    total_users = len(data)
    age_categories = {'0-18': 0, '18-25': 0, '25-45': 0, '45-60': 0, '60+': 0}
    online_status = {'<2 days': 0, '1 week': 0, '1 month': 0, '6 months': 0, '>6 months': 0}

    for user in data.values():
        categorize_age(user, age_categories)
        calculate_online_status(user, online_status)

    age_percentages = calculate_percentages(age_categories, total_users)
    online_percentages = calculate_percentages(online_status, total_users)

    result = {
        'age_percentages': age_percentages,
        'online_percentages': online_percentages
    }

    with open(output_file, 'w') as out_file:
        json.dump(result, out_file, indent=2)


def categorize_age(user: dict, age_categories: dict) -> None:
    """Categorize the age of a user and update the age categories dictionary.

    Args:
        user (dict): User data dictionary.
        age_categories (dict): Dictionary to store the count of users in different age categories.
    """
    age = user.get('age', 0)
    category_switch = {
        age <= 18: '0-18',
        18 < age <= 25: '18-25',
        25 < age <= 45: '25-45',
        45 < age <= 60: '45-60',
        age > 60: '60+',
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
        days_since_last_login < 2: '<2 days',
        2 <= days_since_last_login < 7: '1 week',
        7 <= days_since_last_login < 30: '1 month',
        30 <= days_since_last_login < 180: '6 months',
        days_since_last_login >= 180: '>6 months',
    }
    # If the number of days does not match any of the existing keys, the default value is Unknown
    online_status_category = status_switch.get(True, 'Unknown')
    online_status[online_status_category] += 1


def calculate_percentages(data_dict: dict, total_users: dict) -> dict:
    """Calculate the percentage of users in each category.

    Args:
        data_dict (dict): Dictionary containing the count of users in different categories.
        total_users (int): Total number of users.

    Returns:
        dict: Dictionary containing the percentage of users in each category.
    """
    return {key: (count / total_users) * 100 for key, count in data_dict.items()}
