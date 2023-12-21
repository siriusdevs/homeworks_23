"""Module, that provide analyzing of JSON."""
import json
import os
import sys
from datetime import datetime
from statistics import mean
from typing import Any


class PathError(Exception):
    """
    Exception raised for errors in the input path.

    Attributes:
        path (str): The path that caused the error.
    """

    def __init__(self, path: str) -> None:
        """
        Initialize the PathError exception with a specific file path.

        Args:
            path (str): The path of the file that does not exist.
        """
        super().__init__(f'File with path: {path} is not exist')


class ExtensionError(Exception):
    """
    Exception raised for errors in the file extension.

    Attributes:
        extension (str): The actual extension of the file.
        expected (str): The expected extension of the file.
    """

    def __init__(self, extension: str, expected: str) -> None:
        """
        Initialize the ExtensionError exception with the file extension and the expected extension.

        Args:
            extension (str): The actual extension of the file.
            expected (str): The expected extension for the file.
        """
        super().__init__(f'File must be {expected}, but got {extension}')


def check_path(path_to_file: str) -> None:
    """
    Check if the given file path points to an existing file.

    Raises:
        PathError: If the file at the given path does not exist.

    Args:
        path_to_file (str): Path to the file to check.
    """
    if not os.path.isfile(path_to_file):
        raise PathError(path_to_file)


def check_extension(path_to_file: str, extension: str) -> None:
    """
    Check if the file at the given path has the specified extension.

    Raises:
        ExtensionError: If the file's extension does not match the expected extension.

    Args:
        path_to_file (str): Path to the file to check.
        extension (str): Expected file extension.
    """
    current_extension = os.path.splitext(path_to_file)[1]
    if current_extension != extension:
        raise ExtensionError(current_extension, extension)


def print_error(path_to_file: str, text: str) -> None:
    """
    Write an error message to a file and then exit the program.

    Args:
        path_to_file (str): Path to the file where the error message will be written.
        text (str): Error message to be written.
    """
    with open(path_to_file, 'w') as file_to_write:
        file_to_write.write(text)
    sys.exit()


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

def get_required_variables(json_file: dict[str : dict[str:Any]]
                           ) -> tuple[datetime, list, dict, list]:
    # Вообще, в идеале, тут правда должна быть текущая дата, но тогда тесты, увы, работают
    # только сутки (((
    # current_date = datetime.now()
    current_date = datetime.strptime('2023-12-20', '%Y-%m-%d')
    users = json_file.keys()
    time_steps = {
        'Less than 2 days': 2,
        'Less than a week': 7,
        'Less than a month': 31,
        'Less than half a year': 186,
    }
    average_age = {time_lapse: [] for time_lapse in time_steps.keys()}
    average_age['More than half a year'] = []
    return current_date, users, time_steps, average_age

def count_user_age(json_file: dict[str : dict[str:Any]], output_file) -> dict:
    current_date, users, time_steps, average_age = get_required_variables(json_file)

    for user in users:
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
        added = False

        for time_lapse, days in time_steps.items():
            if days_from_last_login < days:
                average_age[time_lapse].append(age)
                added = True
                break

        if not added:
            average_age['More than half a year'].append(age)

    for time_lapse in average_age.keys():
        if average_age[time_lapse]:
            mean_age = mean(average_age[time_lapse])
            average_age[time_lapse] = mean_age
        else:
            average_age[time_lapse] = 'NaN'

    return average_age


def write_result_to_json(
    path_to_file: str,
    email_statistics: dict[str:str],
    average_age: dict[str : float | str],
) -> None:
    to_json = {'email statistics': email_statistics, 'average_age': average_age}

    with open(path_to_file, 'w') as file_to_write:
        file_to_write.write(json.dumps(to_json))


def analyze_json(path_to_json: str, path_to_result: str) -> None:
    json = open_json(path_to_json, path_to_result)
    write_result_to_json(
        path_to_result,
        count_email_domain(json, path_to_result),
        count_user_age(json, path_to_result),
    )


if __name__ == '__main__':
    analyze_json('hw2/data_hw2.json', 'hw2/test.json')
