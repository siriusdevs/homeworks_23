"""Test for hw2."""


import json

import pytest

from hw2 import process_data

OUTPUT_FILE_NAME = 'hw2/output_file.json'
TEST_CASES = (
    ['hw2/tests/test1.json', OUTPUT_FILE_NAME, 'hw2/tests/answertest1.json'],
    ['hw2/tests/test2.json', OUTPUT_FILE_NAME, 'hw2/tests/answertest2.json'],
    ['hw2/tests/test3.json', OUTPUT_FILE_NAME, 'hw2/tests/answertest3.json'],
    ['hw2/tests/test4.json', OUTPUT_FILE_NAME, 'hw2/tests/answertest4.json'],
    ['hw2/tests/test5.json', OUTPUT_FILE_NAME, 'hw2/tests/answertest5.json']
)


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
    process_data(input_file_json, output_file_json, '2023-11-21')
    with (  # noqa: WPS316
        open(output_file_json, 'r') as output,
        open(answer_file_json, 'r') as answer,
    ):
        assert json.load(output) == json.load(answer)
