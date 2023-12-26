"""This module calculate age statistics by age category and year of user registration."""
import json
import os
from collections import Counter
from datetime import datetime
from enum import IntEnum, StrEnum


def user_year_reg(year_reg: Counter, count_year: int) -> dict:
    """Calculate the percentage distribution of registered users by year.

    Args:
        year_reg: the number of users registered in each year
        count_year: total number of year

    Returns:
        dict: the percentage of the number of users registered in a given year.
    """
    return {yr: (count / count_year) * 100 if count_year else 0 for yr, count in year_reg.items()}


def load_input_file(input_file: str) -> dict | str:
    """Read the file data.

    Args:
        input_file: The path to the input JSON file containing user data

    Returns:
        dict with file data or str if file is empty.
    """
    with open(input_file, 'r') as input_f:
        try:
            user_data = json.load(input_f)
        except json.decoder.JSONDecodeError:
            return f'The file {input_file} is empty'
        return user_data


def user_age(age_categories: dict) -> dict:
    """Calculate the percentage distribution of age categories.

    Args:
        age_categories: A dictionary with age categories

    Returns:
        dict: A dictionary with a percentage distribution of age categories.
    """
    age_count = sum(age_categories.values()) if sum(age_categories.values()) else 0
    return {age: (count / age_count) * 100 for age, count in age_categories.items()}


def process_data(input_file: str, output_file: str) -> None | str:
    """Generate statistics from the input file.

    Args:
        input_file: The path to the input JSON file containing user data
        output_file: The path to the output JSON file where processed data will be saved

    Returns:
        message about error.
    """
    checkfileresult = check_file(input_file, output_file)
    if checkfileresult is not None:
        return checkfileresult
    user_data = load_input_file(input_file)
    if not isinstance(user_data, dict):
        return user_data
    user_data = get_data(user_data)
    if not isinstance(user_data, dict):
        return user_data
    age_categoties, year_reg = user_data
    res_dct = {}
    res_dct.update(user_age(age_categoties))
    res_dct.update(user_year_reg(Counter(year_reg), len(year_reg)))
    with open(output_file, 'w') as output_f:
        user_data = json.dump(res_dct, output_f, indent=3)


def check_file(input_file: str, output_file: str) -> None | str:
    """Check if the input and output files exist.

    Args:
        input_file: The path to the input JSON file containing user data
        output_file: The path to the output JSON file where processed data will be saved

    Returns:
        str if input_file is not a file.
    """
    if not os.path.isfile(input_file):
        return f'{input_file} is not a file'
    if not os.path.isfile(output_file):
        out_directory = os.path.dirname(output_file)
        if not os.path.exists(out_directory):
            os.makedirs(out_directory, exist_ok=True)


def get_data(age_data: dict[str, dict]) -> tuple[dict, list] | str:
    """Calculate statistics by age categories and registration years.

    Args:
        age_data: A dictionary contain information about the users

    Returns:
        tuple: a tuple with calculated statistics.
    """
    age_categoties = {
        AgeCategories.from_zero_to_eighteen: 0,
        AgeCategories.from_eighteen_to_twentyfive: 0,
        AgeCategories.from_twentysix_to_fourtyfive: 0,
        AgeCategories.from_fourtyfive_to_sixty: 0,
        AgeCategories.greater_than_sixty: 0,
        }
    year_reg = []
    for user in age_data.values():
        age = user.get('age', 0)
        key = get_key(age)
        age_categoties[key] += 1
        try:
            year_reg.append(datetime.fromisoformat(user.get('registered', 0)).year)
        except ValueError:
            return 'The registration number entered is of the wrong type'
    return age_categoties, year_reg


class AgeCategories(StrEnum):
    """Enumeration class representing age categories."""

    from_zero_to_eighteen = '0-18'
    from_eighteen_to_twentyfive = '18-25'
    from_twentysix_to_fourtyfive = '26-45'
    from_fourtyfive_to_sixty = '45-59'
    greater_than_sixty = '60+'


class AgesCategories(IntEnum):
    """Enumeration class representing age categories."""

    zero = 0
    eighteen = 18
    nineteen = 19
    twenty_five = 25
    twenty_six = 26
    fourty_five = 45
    fourty_six = 46
    sixty = 60


def get_key(age: int) -> str:
    """Calculate statistics.

    Args:
        age: user age

    Returns:
        str: the age range in which the age is located.
    """
    if AgesCategories.zero <= age <= AgesCategories.eighteen:
        return AgeCategories.from_zero_to_eighteen
    elif AgesCategories.nineteen <= age <= AgesCategories.twenty_five:
        return AgeCategories.from_eighteen_to_twentyfive
    elif AgesCategories.twenty_six <= age <= AgesCategories.fourty_five:
        return AgeCategories.from_twentysix_to_fourtyfive
    elif AgesCategories.fourty_six <= age < AgesCategories.sixty:
        return AgeCategories.from_fourtyfive_to_sixty
    return AgeCategories.greater_than_sixty
