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


def create_file(output_file: str) -> None:
    """Create an output file if it is missing.

    Args:
        output_file: str - the file with the result.
    """
    if os.path.dirname(output_file) and not os.path.exists(output_file):
        os.makedirs(os.path(output_file))


def check_is_file(input_file: str, output_file: str) -> bool:
    """Check inputing file.

    Args:
        input_file: str - input data file.
        output_file: str - the file with the result.

    Returns:
        bool: if the file contains an error.
    """
    try:
        os.path.isfile(input_file)
    except FileNotFoundError as invalid_info:
        message = 'Is not a file'
        error_info(output_file, type(invalid_info).__name__, message)
        return False


def check_input_file(input_file: str, output_file: str) -> bool:
    """Check inputing file.

    Args:
        input_file: str - input data file.
        output_file: str - the file with the result.

    Returns:
        bool: if the file contains an error.
    """
    try:
        load_input_data(input_file)
    except json.decoder.JSONDecodeError as invalid_info:
        message = 'Input file is not a valid JSON string or is empty'
        error_info(output_file, type(invalid_info).__name__, message)
        return False


def error_info(output_file: str, invalid_file: str, message: str) -> None:
    """
    Add text in outputing file if there is an error.

    Args:
        output_file: str - the file with the result.
        invalid_file: str - input data file, which does not meet the conditions.
        message: str - text, that occurs in an error.
    """
    create_file(output_file)
    with open(output_file, 'w') as out_file:
        json.dump(
            obj={'error': invalid_file, 'information': message},
            fp=out_file,
            indent=4,
        )


def load_input_data(input_file: str) -> dict[str, dict]:
    """Take data from the input file.

    Args:
        input_file: str - input data file.

    Returns:
        dict[str, dict]: data from the input file.
    """
    with open(input_file, 'r') as json_file_int:
        input_data: dict[str, dict] = json.load(json_file_int)
    return input_data


def record_age(information: dict, age_category: dict) -> None:
    """Record the number of people by age.

    Args:
        information: dict - data with one person's information.
        age_category: dict - data on the age of people.
    """
    age = information.get('age')
    if not isinstance(age, (int, float)):
        age = None
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


def calculate_age(input_file: str) -> dict:
    """Calculate people by age.

    Args:
        input_file: str - input data file.

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
    input_data: dict[str, dict] = load_input_data(input_file)
    for _, information in input_data.items():
        record_age(information, age_category)

    return age_category


def calculate_year(input_file: str) -> dict:
    """Calculate people by year of registration.

    Args:
        input_file: str - input data file.

    Returns:
        dict: statistics of the years of registration of all entered people.
    """
    regist_y = {}
    input_data: dict[str, dict] = load_input_data(input_file)
    for _, information in input_data.items():
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
    create_file(output_file)
    with open(output_file, 'w') as json_file_out:
        json.dump(output_data, json_file_out, indent=4)


def process_data(input_file, output_file) -> None:
    """Calculate statistics of ages and years of user registration.

    Args:
        input_file: str - input data file.
        output_file: str - the file with the result.
    """
    if not check_is_file(input_file, output_file):
        return
    if not check_input_file(input_file, output_file):
        return
    input_data: dict[str, dict] = load_input_data(input_file)
    age_category = calculate_age(input_file)
    regist_y = calculate_year(input_file)
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
    save_output_data(output_file, output_data)
