"""Testing for module 'process_data' from hw2."""
import json

import pytest

from hw2 import process_data

OUTPUT_FILE = 'result.json'
VALID_TEST_DATA = (
    ('input/data_1.json', OUTPUT_FILE, 'expected/expected_1.json'),
    ('input/data_2.json', OUTPUT_FILE, 'expected/expected_2.json'),
    ('input/data_3.json', OUTPUT_FILE, 'expected/expected_3.json'),
    ('input/data_4.json', OUTPUT_FILE, 'expected/expected_4.json'),
    ('input/data_5.json', OUTPUT_FILE, 'expected/expected_5.json'),
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


@pytest.mark.xfail
def test_process_data_failed_first() -> None:
    """First negative test."""
    process_data('input/data_6.json', 'result_1.json')


@pytest.mark.xfail
def test_process_data_failed_second() -> None:
    """Second negative test."""
    process_data('input/data_.json', 'result_2.json')
