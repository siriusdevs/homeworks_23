"""Test module for function process_data from hw2.py."""
import json

import pytest

from hw2 import process_data

INPUT_FILES_DIR_PATH = 'hw2/test_files/input'
OUTPUT_FILES_DIR_PATH = 'hw2/test_files/output'
EXPECTED_FILES_DIR_PATH = 'hw2/test_files/expected_output'

NUMBER_OF_FILES = 10


def initialise_test_data():
    """Create a function that initialises test_data and returns it.

    Returns:
        The test_data containing the tuples of the following format: \
            ( \
                input_file_path: path to file with users data, \
                output_file_path: path file where we save necessary stats, \
                expected_output_data: dict with correct statistics \
            )
    """
    test_data = []
    for filename in range(1, NUMBER_OF_FILES + 1):
        input_file_path = f'{INPUT_FILES_DIR_PATH}/{filename}.json'
        output_file_path = f'{OUTPUT_FILES_DIR_PATH}/{filename}.json'

        with open(f'{EXPECTED_FILES_DIR_PATH}/{filename}.json') as expected_output_file:
            expected_output_data = json.load(expected_output_file)

        test_data.append((input_file_path, output_file_path, expected_output_data))
    return tuple(test_data)


TEST_DATA = initialise_test_data()


@pytest.mark.parametrize('input_file_path, output_file_path, expected_output_data', TEST_DATA)
def test_process_data(input_file_path, output_file_path, expected_output_data):
    """Create function (extended by pytest decorator) that tests process_data function.

    Args:
        input_file_path: path to file with users data
        output_file_path: path file where we save necessary stats
        expected_output_data: dict with correct statistics
    """
    process_data(input_file_path, output_file_path)
    with open(output_file_path) as output_file:
        output_data = json.load(output_file)

    assert output_data == expected_output_data
