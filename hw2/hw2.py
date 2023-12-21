"""Output statistics: percentages of users registration by age and city."""

import json
import os


def check_extension(input_path: str, output_path: str) -> tuple[str]:
    """
    Check if the input and output file paths have the correct extension.

    Args:
        input_path: The path of the input file.
        output_path: The path of the output file.

    Returns:
        tuple: A tuple containing the updated input and output file paths.
    """
    if not input_path.endswith('.json'):
        input_path = ''

    if not output_path.endswith('.json') and not output_path.endswith('/'):
        output_path, _ = os.path.splitext(output_path)
        output_path = f'{output_path}.json'
    return input_path, output_path


def check_path(input_path: str, output_path: str) -> tuple[str]:
    """
    Check the existence of input and output paths. Modifies the paths if necessary.

    Args:
        input_path (str): The input path to check.
        output_path (str): The output path to check.

    Returns:
        tuple[str]: A tuple containing the modified input and output paths.
    """
    if not os.path.exists(input_path):
        input_path = ''

    if not os.path.exists(output_path):
        if output_path.endswith('/'):
            os.makedirs(output_path)
            output_path = os.path.join(output_path, 'default_output.json')

        if os.path.dirname(output_path):
            os.makedirs(os.path.dirname(output_path))
    return input_path, output_path


def is_file_empty(input_path: str) -> bool:
    """
    Check if a file is empty.

    Args:
        input_path: The path of the file to check.

    Returns:
        bool: True if the file is empty, False otherwise.
    """
    return os.stat(input_path).st_size == 0


def check_type_in_file(input_path: str) -> str:
    """
    Check if the input_data has type "dict".

    Args:
        input_path: The input data to be checked.

    Returns:
        str: an empty string if the input data is of type "dict" else an error message.
    """
    with open(input_path, 'r') as input_file:
        input_data = json.load(input_file)
    if not isinstance(input_data, dict):
        return 'TypeError: Type of input data is not a dictionary'
    return ''


def filter_user_inf(input_path: str) -> tuple[dict, dict]:
    """Filter input json-file for function 'process_data'.

    Args:
        input_path: path of file, which stores information about users

    Returns:
        Two dictionaries, which store quantity users with a certain age, city
    """
    with open(input_path, 'r') as input_file:
        input_data = json.load(input_file)

    regions = {}
    ages = {}
    for user in input_data.keys():
        user_dict = input_data[user]
        age_key = user_dict.get('age')
        if age_key:
            if user_dict['age'] in ages:
                ages[age_key] += 1
            else:
                ages[age_key] = 1

        region = user_dict.get('region')
        if region:
            if user_dict['region'] in regions:
                regions[region] += 1
            else:
                regions[region] = 1

    return ages, regions


def count_statistic(input_path: str, output_path: str):
    """Count and calculate statistics based on user information data.

    Args:
        input_path: The path to the input file containing user information data.
        output_path: The path to the output file where the calculated statistics will be written.

    Returns:
        dict: A dictionary containing the calculated statistics for ages and regions.
    """
    filtered_data = filter_user_inf(input_path)
    output_data = {'ages': {}, 'regions': {}}

    for age, time in filtered_data[0].items():
        percentage = time/sum(filtered_data[0].values())*100
        output_data['ages'][age] = round(percentage, 2)

    for region, vol in filtered_data[1].items():
        percentage = vol/sum(filtered_data[1].values())*100
        output_data['regions'][region] = round(percentage, 2)

    return output_data


def dumps_to_file_error(msg: str, output_path: str) -> None:
    """Write the given error message to a file using JSON serialization.

    Args:
        msg (str): The error message to be written to the file.
        output_path (str): The path to the output file.
    """
    with open(output_path, 'w') as output_file:
        json.dump(msg, output_file)


def process_data(input_path: str, output_path: str) -> None:
    """Calculate and put statistics of users registration in the output file.

    Args:
        input_path: path of file, which stores input datas about users.
        output_path: path of file, in which send output statistics.
    """
    input_path, output_path = check_extension(input_path, output_path)
    if not input_path:
        dumps_to_file_error('FileExtensionError: extension of input file is wrong', output_path)
        return

    input_path, output_path = check_path(input_path, output_path)
    if not input_path:
        dumps_to_file_error('FileError: input file does not exists', output_path)
        return

    if is_file_empty(input_path):
        dumps_to_file_error('FileError: input file is empty', output_path)
        return

    type_in_file = check_type_in_file(input_path)
    if type_in_file:
        dumps_to_file_error(type_in_file, output_path)
        return

    output_data = count_statistic(input_path, output_path)

    with open(output_path, 'w') as output_file:
        json.dump(output_data, output_file, indent=4)
