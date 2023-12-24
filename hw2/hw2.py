"""Module, that provide analyzing of JSON."""
import json
from datetime import datetime
from statistics import mean
from typing import Any

from checkers import check_extension, check_path
from errors import ExtensionError, PathError, print_error


def open_json(path_to_file: str, output_path: str) -> dict:
    """
    Open a JSON file and return its contents as a dictionary.

    Args:
        path_to_file (str): Path to the JSON file.
        output_path (str): Path for the output file to write errors if any.

    Returns:
        dict: Contents of the JSON file.
    """
    try:
        check_path(path_to_file)
    except PathError:
        text = 'A file with an invalid path is given. Have a nice day!'
        print_error(output_path, text)

    try:
        check_extension(path_to_file, '.json')
    except ExtensionError:
        text = 'The input file should have a JSON extension, but another one is given. \
            Have a nice day!'
        print_error(output_path, text)

    with open(path_to_file) as file_to_read:
        result_of_reading = json.load(file_to_read)

    return result_of_reading


def count_email_domain(json_file: dict, output_path: str) -> dict:
    """
    Count the occurrence of each email domain in the provided JSON file.

    Args:
        json_file (dict): A dictionary representing the JSON file.
        output_path (str): Path for the output file to write errors if any.

    Returns:
        dict: A dictionary mapping each email domain to its occurrence percentage.
    """
    users = json_file.keys()
    amount_of_users = len(users)
    email_statistics = {}

    if amount_of_users == 0:
        text = 'There is no user information in the file. Have a nice day!'
        print_error(output_path, text)

    for user in users:
        try:
            email = json_file[user]['email'].split('@')[1]
        except IndexError:
            text = 'Mail with an invalid email has been entered in the file. Have a nice day!'
            print_error(output_path, text)

        email_statistics[email] = email_statistics.get(email, 0) + 1

    for mail in email_statistics.keys():
        percent = round(email_statistics[mail] / amount_of_users * 100, 2)
        email_statistics[mail] = f'{percent}%'

    return email_statistics


def get_required_variables(
    json_file: dict[str, dict[str, Any]],
) -> tuple[datetime, list[str], dict, dict]:
    """
    Extract and compute necessary variables from a JSON file.

    Args:
        json_file: A dictionary representing the JSON file contents.

    Returns:
        A tuple containing the current date, list of users, time steps,\
            and average age categorized by time lapses.

    Note:
        The current date is set to a fixed date '2023-12-20' for consistent testing.
    """
    current_date = datetime.strptime('2023-12-20', '%Y-%m-%d')
    users = list(json_file.keys())
    time_steps = {
        'Less than 2 days': 2,
        'Less than a week': 7,
        'Less than a month': 31,
        'Less than half a year': 186,
    }
    average_age = {time_lapse: [] for time_lapse in time_steps.keys()}
    average_age['More than half a year'] = []

    return current_date, users, time_steps, average_age


def parse_user_data(
    user: str, json_file: dict[str, dict[str, Any]], current_date: datetime, output_file,
) -> tuple[int, int]:
    """
    Parse and validate the age and last login data for a given user.

    Args:
        user: The user for whom the data is being parsed.
        json_file: A dictionary representing the JSON file contents.
        current_date: The current date for calculating days from last login.
        output_file: The output file for logging errors.

    Returns:
        tuple containing the age of the user and days from last login.
    """
    age = json_file[user]['age']
    if not isinstance(age, int):
        text = 'An incorrect age value has been entered. Have a nice day!'
        print_error(output_file, text)

    try:
        last_login = datetime.strptime(json_file[user]['last_login'], '%Y-%m-%d')
    except ValueError:
        text = 'The file contains a date in a non-correct format. Have a nice day!'
        print_error(output_file, text)

    days_from_last_login = (current_date - last_login).days
    return age, days_from_last_login


def categorize_by_time_lapse(
    age: int,
    days_from_last_login: int,
    time_steps: dict[str, int],
    average_age: dict[str, list[int]],
):
    """
    Categorizes a user's age into a time lapse category based on days from last login.

    Args:
        age: The age of the user.
        days_from_last_login: Days elapsed since the user's last login.
        time_steps: A dictionary defining time lapse categories.
        average_age: A dictionary to store the average ages categorized by time lapses.
    """
    added = False
    for time_lapse, days in time_steps.items():
        if days_from_last_login < days:
            average_age[time_lapse].append(age)
            added = True
            break

    if not added:
        average_age['More than half a year'].append(age)


def calculate_average_ages(average_age: dict[str, list[int]]) -> dict:
    """
    Calculate the average age for each time lapse category.

    Args:
        average_age: A dictionary containing ages categorized by time lapses.

    Returns:
        A dictionary with the average age for each time lapse category.
    """
    for time_lapse in average_age.keys():
        if average_age[time_lapse]:
            mean_age = mean(average_age[time_lapse])
            average_age[time_lapse] = mean_age
        else:
            average_age[time_lapse] = 'NaN'
    return average_age


def count_user_age(json_file: dict[str, dict[str, Any]], output_file) -> dict:
    """
    Count the average age of users categorized by time since their last login.

    Args:
        json_file: A dictionary representing the JSON file contents.
        output_file: The output file for logging errors.

    Returns:
        A dictionary with the average age for each time lapse category.
    """
    current_date, users, time_steps, average_age = get_required_variables(json_file)

    for user in users:
        age, days_from_last_login = parse_user_data(
            user, json_file, current_date, output_file,
        )
        categorize_by_time_lapse(age, days_from_last_login, time_steps, average_age)

    return calculate_average_ages(average_age)


def write_result_to_json(
    path_to_file: str,
    email_statistics: dict[str, str],
    average_age: dict[str, float | str],
) -> None:
    """
    Write email statistics and average age data to a JSON file.

    Args:
        path_to_file: The path to the file where the data will be written.
        email_statistics: A dictionary containing email statistics.
        average_age: A dictionary containing the average age data.

    This function converts the combined data into a JSON format\
        and writes it to the specified file.
    """
    to_json = {'email statistics': email_statistics, 'average_age': average_age}

    with open(path_to_file, 'w') as file_to_write:
        json.dump(to_json, file_to_write)


def analyze_json(path_to_json: str, path_to_result: str) -> None:
    """
    Analyzes a JSON file and writes the results to another file.

    Args:
        path_to_json: The path to the JSON file to be analyzed.
        path_to_result: The path to the file where the analysis results will be written.

    This function opens and processes the JSON file, then invokes write_result_to_json
    to write the analysis results.
    """
    json_data = open_json(path_to_json, path_to_result)
    write_result_to_json(
        path_to_result,
        count_email_domain(json_data, path_to_result),
        count_user_age(json_data, path_to_result),
    )


if __name__ == '__main__':
    analyze_json('hw2/data_hw2.json', 'hw2/test.json')
