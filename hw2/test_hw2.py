"""Tests for hw2.py."""
import json
import os

import pytest

from hw2 import process_data

correct_output_file = './hw2/test_output.json'


ERROR_CHECKING = (
    (
        'vydumanniy_file.json',
        'test_output.json',
        'file vydumanniy_file.json does not exist!',
    ),
    (
        './hw2/test_error.json',
        'test_output.json',
        'file ./hw2/test_error.json is not in JSON format!',
    ),
    (
        './hw2/test1.json',
        './hw2/writing.json',
        'not permission to write to file ./hw2/writing.json',
    ),
    (
        './hw2/data_hw2.json',
        './hw2/test_output.json',
        'The prograp was completed without errors.',
    ),
    (
        './hw2/data_hw2.json',
        './hw2/test.json',
        'The prograp was completed without errors.',
    ),
)


@pytest.mark.parametrize('input_file, output_file, expected', ERROR_CHECKING)
def test_with_error_code(input_file: str, output_file: str, expected: int):
    """
    Validates error codes returned by the process_data function.

    Args:
        input_file (str): Name of the input file.
        output_file (str): Name of the output file.
        expected (int): Expected function error code.
    """
    assert process_data(input_file, output_file) == expected


def test_data():
    """Tests data processing functionality."""
    process_data('./hw2/data_hw2.json', correct_output_file)
    with open(correct_output_file, 'r') as output_file:
        output_dict = json.load(output_file)
        assert output_dict == {
            'age_stats': {
                '18-25': 1,
                '25-45': 1,
            },
            'last_login_stats': {
                'less half year': 1,
                'above half year': 1,
            },
        }
    os.remove(correct_output_file)
