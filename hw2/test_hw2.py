"""Testing for module 'process_data' from hw2."""
import json

import pytest

from hw2 import process_data

VALID_TEST_DATA = (
    ('input/data_1.json', 'output/result_1.json', 'expected/expected_1.json'),
    ('input/data_2.json', 'output/result_2.json', 'expected/expected_2.json'),
    ('input/data_3.json', 'output/result_3.json', 'expected/expected_3.json'),
    ('input/data_4.json', 'output/result_4.json', 'expected/expected_4.json'),
    ('input/data_5.json', 'output/result_5.json', 'expected/expected_5.json'),
)


@pytest.mark.parametrize('input_file, output_file, expected', VALID_TEST_DATA)
def test_process_data(input_file: str, output_file: str, expected: str) -> None:
    """Test detective function with process_data.

    Args:
        input_file: str - input data file.
        output_file: str - the file with the result.
        expected: str - the file with the expected data.
    """
    process_data(input_file, output_file)
    with open(expected) as expected_file:
        expected_data = json.load(expected_file)
    with open(output_file, 'r') as file_result:
        result_data = json.load(file_result)
    assert result_data == expected_data


INVALID_TEST_DATA = (
    ('input/data_6.json', 'error/result_1.json', 'expected/expected_6.json'),
    ('input/data_.json', 'error/result_2.json', 'expected/expected_7.json'),
    ('input/data_7.txt', 'error/result_3.json', 'expected/expected_8.json'),
)


@pytest.mark.parametrize('input_file, output_file, expected', INVALID_TEST_DATA)
def test_process_data_failed(input_file: str, output_file: str, expected: dict) -> None:
    """Tests with error output with process_data.

    Args:
        input_file: str - input data file.
        output_file: str - the file with the result.
        expected: str - the file with the expected data.
    """
    process_data(input_file, output_file)
    with open(expected) as expected_file:
        expected_data = json.load(expected_file)
    with open(output_file, 'r') as file_result:
        result_data = json.load(file_result)
    assert result_data == expected_data
