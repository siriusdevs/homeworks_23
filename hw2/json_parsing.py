"""Module that parses and calculates statistics of emails and registration years in JSON."""
import json
import os
import re

import errors as err
from consts import SEARCHING_REFERENCES, Error, JsonData, JsonStats, UserData


def _calculate_statistics_in_json(json_data: JsonData) -> JsonStats:
    statistics = {}

    for reference in SEARCHING_REFERENCES:
        aggregate_attrs = 0

        if reference not in statistics:
            statistics[reference] = {}
        statistics_field = statistics[reference]
        for name, user_info in json_data.items():
            attr = _get_value_from_field(user_info, reference, name)
            if attr not in statistics_field:
                statistics_field[attr] = 1
            else:
                statistics_field[attr] += 1
            aggregate_attrs += 1

        for note in statistics_field.keys():
            statistics_field[note] = round(statistics_field[note] / aggregate_attrs * 100, 2)

    return statistics


def _get_value_from_field(user_info: UserData, field: str, name: str) -> str:
    if field not in user_info:
        raise err.JSONMissingFieldException((field))

    string = user_info[field]

    match field:
        case 'email':
            separ = '@'
            if string.count(separ) != 1:
                raise err.JSONIncorrectFieldFormat(f'email [{string}]', '<username>@<domain>')

            return string.split(separ)[1]

        case 'registered':
            separ = '-'
            if re.match(r'\d{4}-\d{2}-\d{2}', string) is None:
                raise err.JSONIncorrectFieldFormat(f'date [{string}]', 'YYYY-MM-DD')

            return string.split(separ)[0]


def get_abspath(filename: str, directory: str) -> str:
    """Return absolute path to desire file by destination.

    Args:
        filename (str): name of the desired file.
        directory (str): 'inputs' or 'outputs' directory where JSONs are stored.

    Returns:
        str: absolute path to JSON file.
    """
    return os.path.join(os.getcwd(), 'hw2', 'src', directory, filename)


def assemble_data(input_filename: str, output_filename: str) -> None:
    """Read data from input file and write calculated statistics into output file.

    Args:
        input_filename (str): name of input JSON file to read.
        output_filename (str): name of output JSON file to write.

    Raises:
        InvalidFilePathException: occurs if reading JSON by not existing path.
    """
    input_abspath = get_abspath(input_filename, 'inputs')
    if not os.path.exists(input_abspath):
        raise err.InvalidFilePathException(input_abspath)

    with open(input_abspath, 'r') as input_file:
        json_data = json.load(input_file)

    statistics = _calculate_statistics_in_json(json_data)
    output_abspath = get_abspath(output_filename, 'outputs')
    os.makedirs(os.path.abspath(os.path.dirname(output_abspath)), exist_ok=True)
    with open(output_abspath, 'w') as output_file:
        json.dump(statistics, fp=output_file, indent=4)


def log_error_to_json(error: Error, output_filename: str) -> None:
    """Write error log message into output JSON.

    Args:
        error (Error): class of occured error.
        output_filename (str): name of output JSON file to write.
    """
    with open(get_abspath(output_filename, 'outputs'), 'w') as output_file:
        json.dump(error, fp=output_file, indent=4)
