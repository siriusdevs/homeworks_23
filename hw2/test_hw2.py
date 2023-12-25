"""tests for hw2 module."""
import json
from datetime import datetime

import pytest

from hw2 import process_data

OUTPUT_FILE = 'data_hw2.json'
TEST_CASES = (
    ['tests/test1.json', OUTPUT_FILE, 'tests/output1.json'],
    ['tests/test2.json', OUTPUT_FILE, 'tests/output2.json'],
    ['tests/test3.json', OUTPUT_FILE, 'tests/output3.json'],
)

TODAY = datetime.strptime('2023-12-20', '%Y-%m-%d')


@pytest.mark.parametrize('input_file_json, output_file_json, answer_file_json', TEST_CASES)
def test_process_data(input_file_json, output_file_json, answer_file_json) -> None:
    """Test function for dates and hosts.

    Args:
        input_file_json: str - represents the path to the JSON file.
        output_file_json: str - represents the path to the output JSON file.
        answer_file_json: str - test answer file.

    Asserts:
        True if answer is correct.
    """
    process_data(input_file_json, output_file_json, TODAY)
    with open(output_file_json, 'r') as output:
        with open(answer_file_json, 'r') as answer:
            assert json.load(output) == json.load(answer)


def test_process_data_no_file_error():
    """Test function for process_data when input file does not exist.

    Asserts:
        FileNotFoundError is raised.
    """
    with pytest.raises(FileNotFoundError):
        process_data('nonexistent_file.json', OUTPUT_FILE, TODAY)
