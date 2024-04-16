"""Testing module 'modul.py'."""

import json

import modul
import pytest

OUTPUT_PATH = 'hw2/tests_folder/output.json'

ERROR_MESSAGE = 'The processed data does not match expected results'
FILE_DESC = 'Path to the file with test data.'
WITH_OPEN = 'r'
IN_EX_FILE = 'input_file, expected_file'


different_arguments_tests = [
    ('hw2/tests_folder/test1.json', 'hw2/expected_folder/expected1.json'),
    ('hw2/tests_folder/test2.json', 'hw2/expected_folder/expected2.json'),
]

without_different_arguments_tests = [
    ('hw2/tests_folder/test3.json', 'hw2/expected_folder/expected3.json'),
    ('hw2/tests_folder/test4.json', 'hw2/expected_folder/expected4.json'),
    ('hw2/tests_folder/test5.json', 'hw2/expected_folder/expected5.json'),
]

with_wrong_type_variables_tests = [
    ('hw2/tests_folder/test6.json', 'hw2/expected_folder/expected6.json'),
]

with_errors_tests = [
    ('hw2/tests_folder/test7.json', 'hw2/expected_folder/expected7.json'),
    ('hw2/tests_folder/test8.txt', 'hw2/expected_folder/expected8.json'),
    ('hw2/tests_folder/test9.txt', 'hw2/expected_folder/expected9.json'),
    ('hw2/tests_folder/test10.txt', 'hw2/expected_folder/expected10.json'),
    ('hw2/tests_folder/test11.json', 'hw2/expected_folder/expected11.json'),
]


@pytest.mark.parametrize(IN_EX_FILE, different_arguments_tests)
def test_different_arguments(input_file, expected_file):
    """We are testing the process_data function on various datasets.

    Args:
        input_file (str): {FILE_DESC}
        expected_file (str): {FILE_DESC}
    """
    modul.process_data(input_file, OUTPUT_PATH)

    with open(expected_file, WITH_OPEN) as file_json:
        expected_data = json.load(file_json)

    with open(OUTPUT_PATH, WITH_OPEN) as file_output:
        output_data = json.load(file_output)

    assert output_data == expected_data, ERROR_MESSAGE


@pytest.mark.parametrize(IN_EX_FILE, without_different_arguments_tests)
def test_without_different_arguments(input_file, expected_file):
    """We are testing the process_data function on datasets with missing arguments.

    Args:
        input_file (str): {FILE_DESC}
        expected_file (str): {FILE_DESC}
    """
    modul.process_data(input_file, OUTPUT_PATH)

    with open(expected_file, WITH_OPEN) as file_json:
        expected_data = json.load(file_json)

    with open(OUTPUT_PATH, WITH_OPEN) as file_output:
        output_data = json.load(file_output)

    assert output_data == expected_data, ERROR_MESSAGE


@pytest.mark.parametrize(IN_EX_FILE, with_wrong_type_variables_tests)
def test_with_wrong_type_variables(input_file, expected_file):
    """We are testing the process_data function on datasets with incorrect variable types.

    Args:
        input_file (str): {FILE_DESC}
        expected_file (str): {FILE_DESC}

    Returns:
        tuple: Tuple with error message and error object
    """
    try:
        modul.process_data(input_file, OUTPUT_PATH)
    except Exception as er:
        return 'An error occurred:', er

    with open(expected_file, WITH_OPEN) as file_json_expected:
        expected_data = json.load(file_json_expected)

    with open(OUTPUT_PATH, WITH_OPEN) as file_output:
        output_data = json.load(file_output)

    assert output_data == expected_data, ERROR_MESSAGE


@pytest.mark.parametrize(IN_EX_FILE, with_errors_tests)
def test_with_errors(input_file, expected_file):
    """We are testing the process_data function on datasets with errors.

    Args:
        input_file (str): {FILE_DESC}
        expected_file (str): {FILE_DESC}

    Returns:
        tuple: Tuple with error message and error object
    """
    try:
        modul.process_data(input_file, OUTPUT_PATH)
    except Exception as er:
        return 'An error occurred:', er

    with open(expected_file, WITH_OPEN) as file_json_expected:
        expected_data = json.load(file_json_expected)

    with open(OUTPUT_PATH, WITH_OPEN) as file_output:
        output_data = json.load(file_output)

    assert output_data == expected_data, ERROR_MESSAGE


with_empty_file_test = [
    ('hw2/tests_folder/test8.json', 'hw2/expected_folder/expected8.json'),
]


@pytest.mark.parametrize(IN_EX_FILE, with_empty_file_test)
def test_with_empty_file(input_file, expected_file):
    """We are testing the process_data function on datasets with an empty file.

    Args:
        input_file (str): {FILE_DESC}
        expected_file (str): {FILE_DESC}

    """
    with pytest.raises(ValueError) as error_info:
        modul.process_data(input_file, OUTPUT_PATH)
    
    assert str(error_info.value) == "Input file 'hw2/tests_folder/test8.json' no valid JSON data."
