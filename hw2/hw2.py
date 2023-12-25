"""Module for calculating statistics of the age category and user registration by year."""


import datetime
import json
import os

REGISTERED = 'registered'
AGE = 'age percent'
EIGHTEEN = 18
TWENTY_FIVE = 25
FORTY_FIVE = 45
SIXTY = 60

BELOW_LA_AGE_STRING = '0-18'
LA_TO_MA_AGE_STRING = '19-25'
MA_TO_LAP_AGE_STRING = '26-45'
LAP_TO_HAP_AGE_STRING = '46-60'
HIGHEST_AND_ABOVE_AP_AGE_STRING = '60+'


def error_info(output_file: str, invalid_file: str, message: str) -> None:
    """
    Add text in outputing file if there is an error.

    Args:
        output_file: str - the file with the result.
        invalid_file: str - input data file, which does not meet the conditions.
        message: str - text, that occurs in an error.
    """
    if os.path.dirname(output_file) and not os.path.exists(output_file):
        os.makedirs(os.path.dirname(output_file))
    with open(output_file, 'w') as out_file:
        json.dump(
            obj={'error': invalid_file, 'information': message},
            fp=out_file,
            indent=4,
        )


def load_input_data(input_file: str, output_file: str) -> dict[str, dict] | bool:
    """Take data from the input file.

    Args:
        input_file: str - input data file.
        output_file: str - the file with the result.

    Returns:
        dict[str, dict]: data from the input file.
    """
    try:
        with open(input_file, 'r') as test_json:
            input_data = json.load(test_json)
    except FileNotFoundError as invalid_info:
        message = 'Is not a file'
        error_info(output_file, type(invalid_info).__name__, message)
        return False
    except json.decoder.JSONDecodeError as invalid_info:
        message = 'Input file is not a valid JSON string or is empty'
        error_info(output_file, type(invalid_info).__name__, message)
        return False

    return input_data


def record_age(information: dict, age_category: dict) -> None:
    """Record the number of people by age.

    Args:
        information: dict - data with one person's information.
        age_category: dict - data on the age of people.
    """
    age = information.get('age')
    if age <= EIGHTEEN:
        age_category['0-18'] += 1
    elif age <= TWENTY_FIVE:
        age_category['19-25'] += 1
    elif age <= FORTY_FIVE:
        age_category['26-45'] += 1
    elif age <= SIXTY:
        age_category['46-60'] += 1
    else:
        age_category['60+'] += 1


def calculate_age(input_data: dict[str, dict]) -> dict:
    """Calculate people by age.

    Args:
        input_data: dict[str, dict] - data from input file.

    Returns:
        dict: statistics on the ages of all people being entered.
    """
    age_category = {
        BELOW_LA_AGE_STRING: 0,
        LA_TO_MA_AGE_STRING: 0,
        MA_TO_LAP_AGE_STRING: 0,
        LAP_TO_HAP_AGE_STRING: 0,
        HIGHEST_AND_ABOVE_AP_AGE_STRING: 0,
        }
    for information in input_data.values():
        record_age(information, age_category)

    return age_category


def calculate_year(input_data: dict[str, dict]) -> dict:
    """Calculate people by year of registration.

    Args:
        input_data: dict[str, dict] - data from input file.

    Returns:
        dict: statistics of the years of registration of all entered people.
    """
    regist_y = {}
    for information in input_data.values():
        registered_year = information.get(REGISTERED)
        if registered_year:
            regist_year_obj = str((datetime.datetime.strptime(registered_year, '%Y-%m-%d')).year)
            regist_y[regist_year_obj] = regist_y.get(regist_year_obj, 0) + 1
        else:
            regist_y[regist_year_obj] = None
    return regist_y


def save_output_data(output_file: str, output_data: dict[str, dict]) -> None:
    """Save the result to the output file.

    Args:
        output_file: str - the file with the result.
        output_data: str - the resulting data with statistics.
    """
    with open(output_file, 'w') as json_file_out:
        json.dump(output_data, json_file_out, indent=4)


def process_data(input_file, output_file) -> None:
    """Calculate statistics of ages and years of user registration.

    Args:
        input_file: str - input data file.
        output_file: str - the file with the result.
    """
    input_data = load_input_data(input_file, output_file)
    age_category = calculate_age(input_data)
    regist_y = calculate_year(input_data)
    if input_data:
        output_data = {
            AGE: {ctg: (cnt / len(input_data)) * 100 for ctg, cnt in age_category.items()},
            REGISTERED: {year: (cnt / len(input_data)) * 100 for year, cnt in regist_y.items()},
        }
    else:
        output_data = {
            AGE: 0,
            REGISTERED: 0,
        }
    if os.path.dirname(output_file) and not os.path.exists(output_file):
        os.makedirs(os.path.dirname(output_file))
    save_output_data(output_file, output_data)
