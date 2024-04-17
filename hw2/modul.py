"""Module for processing user data and generating statistics."""
import json
from collections import Counter
from datetime import datetime, timedelta


def calculate_age_category(age):
    """Calculate the age category based on the given age.

    Args:
        age (int): The age of the user.

    Returns:
        str: The age category.
    """
    eighteen = 18
    twenty_five = 25
    forty_five = 45
    sixty = 60
    if age <= eighteen:
        return '0-18'
    if age <= twenty_five:
        return '19-25'
    if age <= forty_five:
        return '26-45'
    if age <= sixty:
        return '46-60'
    if age > sixty:
        return '60+'


def calculate_online_intervals(login_dates):
    """Calculate the distribution of online intervals based on login dates.

    Args:
        login_dates (list): List of login dates in '%Y-%m-%d' format.

    Returns:
        dict: Distribution of online intervals.

    Raises:
        ValueError: Input file is empty or contains no login dates.
    """
    if not login_dates:
        raise ValueError('Input file is empty or contains no login dates.')

    intervals = initialize_intervals()
    today = datetime.now()
    for date_str in login_dates:
        delta = calculate_delta(today, date_str)
        update_intervals(intervals, delta)
    total_logins = len(login_dates)
    return normalize_intervals(intervals, total_logins)


def initialize_intervals():
    """Initialize dictionary for online intervals.

    Returns:
        dict: Dictionary with online intervals initialized to zero.
    """
    return {
        '<2 days': 0,
        '<1 week': 0,
        '<1 month': 0,
        '<6 months': 0,
        '>6 months': 0,
    }


def calculate_delta(today, date_str):
    """Calculate time difference between today and login date.

    Args:
        today (datetime): Current date and time.
        date_str (str): Login date in '%Y-%m-%d' format.

    Returns:
        timedelta: Time difference between today and login date.
    """
    login_date = datetime.strptime(date_str, '%Y-%m-%d')
    return today - login_date


def update_intervals(intervals, delta):
    """Update intervals dictionary based on time difference.

    Args:
        intervals (dict): Dictionary containing online intervals.
        delta (timedelta): Time difference between today and login date.
    """
    if delta < timedelta(days=2):
        intervals['<2 days'] += 1
    elif delta < timedelta(weeks=1):
        intervals['<1 week'] += 1
    elif delta < timedelta(weeks=4):
        intervals['<1 month'] += 1
    elif delta < timedelta(weeks=24):
        intervals['<6 months'] += 1
    else:
        intervals['>6 months'] += 1


def normalize_intervals(intervals, total_logins):
    """Normalize interval counts by total number of logins.

    Args:
        intervals (dict): Dictionary containing online intervals.
        total_logins (int): Total number of login dates.

    Returns:
        dict: Normalized distribution of online intervals.
    """
    return {key: (value_d / total_logins) * 100 for key, value_d in intervals.items()}


def process_data(input_file, output_file):
    """Process user data and save the results to a JSON file.

    Args:
        input_file (str): Path to the input JSON file.
        output_file (str): Path to save the output JSON file.

    Raises:
        FileNotFoundError: Input file '{input_file}' not found.
        ValueError: Input file '{input_file}' no valid.
    """
    try:
        with open(input_file, 'r') as file_json:
            data_j = json.load(file_json)
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file '{input_file}' not found.")
    except json.decoder.JSONDecodeError:
        raise ValueError(f"Input file '{input_file}' no valid.")

    age_percentage, online_intervals = extract_data_statistics(data_j)

    result_payload = {
        'age_distribution': age_percentage,
        'online_intervals': online_intervals,
    }

    with open(output_file, 'w') as f_output:
        json.dump(result_payload, f_output, indent=4)


def extract_data_statistics(data_j):
    """Extract age distribution and online intervals statistics from user data.

    Args:
        data_j (dict): User data in JSON format.

    Returns:
        tuple: Tuple containing age distribution dictionary and online intervals dictionary.

    Raises:
        ValueError: No user age data found.
    """
    ages = [
        user.get('age', 0)
        for user in data_j.values()
        if isinstance(user.get('age'), int)
    ]
    if not ages:
        raise ValueError('No user age data found.')

    age_counter = Counter(calculate_age_category(age) for age in ages)

    login_dates = [
        user.get('last_login', '')
        for user in data_j.values()
        if isinstance(user.get('last_login'), str)
    ]
    if not login_dates:
        raise ValueError('No user login date data found.')

    online_intervals = calculate_online_intervals(login_dates)

    total_users = len(data_j)

    age_percentage = {
        category: (count / total_users) * 100
        for category, count in age_counter.items()
    }

    return age_percentage, online_intervals
