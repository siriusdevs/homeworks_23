import json

import pytest

from hw2 import process_data

INPUT_FILES_DIR_PATH = 'hw2/test_files/input'
OUTPUT_FILES_DIR_PATH = 'hw2/test_files/output'
EXPECTED_FILES_DIR_PATH = 'hw2/test_files/expected_output'


def initialise_test_data():
    result = []
    for i in range(1, 11):
        input_file_path = f'{INPUT_FILES_DIR_PATH}/{i}.json'
        output_file_path = f'{OUTPUT_FILES_DIR_PATH}/{i}.json'

        with open(f'{EXPECTED_FILES_DIR_PATH}/{i}.json') as expected_output_file:
            expected_output_data = json.load(expected_output_file)

        result.append((input_file_path, output_file_path, expected_output_data))
    return tuple(result)


TEST_DATA = initialise_test_data()


@pytest.mark.parametrize('input_file_path, output_file_path, expected_output_data', TEST_DATA)
def test_process_data(input_file_path, output_file_path, expected_output_data):
    process_data(input_file_path, output_file_path)
    with open(output_file_path) as output_file:
        output_data = json.load(output_file)

    assert output_data == expected_output_data
