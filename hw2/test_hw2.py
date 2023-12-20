"""Unit tests for modul hw2."""

import json
import os
from datetime import date

import pytest

from hw2 import process_data

TESTS_DIRECTOTY = 'test_data'
INPUT_FILE_NAME = 'input.json'
OUTPUT_FILE_NAME = 'output.json'
TEST_FILE_NAME = 'test.json'
DATE_VALUES = 2023, 12, 5
DATE = date(*DATE_VALUES)

TEST_DATA = (
    'simple',
    'empty',
    'complex',
)


@pytest.mark.parametrize('test_dir_path', TEST_DATA)
def test_process_data(test_dir_path: str) -> None:
    """Test process_date function.

    Args:
        test_dir_path: the path to the directory containing input.json and output.json files.
    """
    process_data(
        os.path.join(TESTS_DIRECTOTY, test_dir_path, INPUT_FILE_NAME),
        TEST_FILE_NAME,
        current_date=DATE,
    )
    expected_path = os.path.join(TESTS_DIRECTOTY, test_dir_path, OUTPUT_FILE_NAME)
    with open(expected_path, 'r') as expected_josn:
        expected_result = json.loads(expected_josn.read())
    with open(TEST_FILE_NAME, 'r') as output_json:
        output_result = json.loads(output_json.read())
    os.remove(TEST_FILE_NAME)
    assert expected_result == output_result
