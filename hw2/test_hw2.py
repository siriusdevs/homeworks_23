"""Module for testing hw2.py."""


import json

import hw2_exceptions as exceptions
import pytest

from hw2 import process_data

valid_test_data = (
    (
        './hw2/test_data/IO_data/valid_data/input_data/input_1.json',
        './hw2/test_data/IO_data/valid_data/output_data/output_1.json',
        './hw2/test_data/expected_data/expected_1.json',
    ),
    (
        './hw2/test_data/IO_data/valid_data/input_data/input_2.json',
        './hw2/test_data/IO_data/valid_data/output_data/output_2.json',
        './hw2/test_data/expected_data/expected_2.json',
    ),
    (
        './hw2/test_data/IO_data/valid_data/input_data/input_3.json',
        './hw2/test_data/IO_data/valid_data/output_data/output_3.json',
        './hw2/test_data/expected_data/expected_3.json',
    ),
    (
        './hw2/test_data/IO_data/valid_data/input_data/input_4.json',
        './hw2/test_data/IO_data/valid_data/output_data/output_4.json',
        './hw2/test_data/expected_data/expected_4.json',
    ),
    (
        './hw2/test_data/IO_data/valid_data/input_data/input_5.json',
        './hw2/test_data/IO_data/valid_data/output_data/output_5.json',
        './hw2/test_data/expected_data/expected_5.json',
    ),
)


@pytest.mark.parametrize('input_file_path, output_file_path, expected', valid_test_data)
def test_process_data(input_file_path: str, output_file_path: str, expected: tuple):
    """Test process_data function from hw2.py.

    Args:
        input_file_path (str): path to the input json file.
        output_file_path (str): path to the output json file.
        expected (tuple): expected data.
    """
    process_data(input_file_path, output_file_path)
    with open(output_file_path, 'r') as output_file:
        output_data = json.loads(output_file.read())
    with open(expected, 'r') as expected_file:
        expected_data = json.loads(expected_file.read())
    assert output_data == expected_data


invalid_test_data = (
    (123, './hw2/test_data/IO_data/valid_data/output_data/output_1.json', TypeError),
    (
        './hw2/test_data/IO_data/invalid_data/not_json.txt',
        './hw2/test_data/IO_data/valid_data/output_data/output_1.json',
        exceptions.FileIsNotJsonError,
    ),
    (
        'non_existent_file.json',
        './hw2/test_data/IO_data/valid_data/output_data/output_1.json',
        FileNotFoundError,
    ),
    (
        './hw2/test_data/IO_data/invalid_data/empty.json',
        './hw2/test_data/IO_data/valid_data/output_data/output_1.json',
        exceptions.FileIsEmptyError,
    ),
    (
        './hw2/test_data/IO_data/invalid_data/input_1.json',
        './hw2/test_data/IO_data/valid_data/output_data/output_1.json',
        TypeError,
    ),
    (
        './hw2/test_data/IO_data/invalid_data/input_2.json',
        './hw2/test_data/IO_data/valid_data/output_data/output_1.json',
        TypeError,
    ),
    (
        './hw2/test_data/IO_data/invalid_data/input_3.json',
        './hw2/test_data/IO_data/valid_data/output_data/output_1.json',
        IndexError,
    ),
    (
        './hw2/test_data/IO_data/invalid_data/input_4.json',
        './hw2/test_data/IO_data/valid_data/output_data/output_1.json',
        ValueError,
    ),
    (
        './hw2/test_data/IO_data/invalid_data/input_5.json',
        './hw2/test_data/IO_data/valid_data/output_data/output_1.json',
        TypeError,
    ),
    (
        './hw2/test_data/IO_data/invalid_data/input_6.json',
        './hw2/test_data/IO_data/valid_data/output_data/output_1.json',
        TypeError,
    ),

    ('./hw2/test_data/IO_data/valid_data/input_data/input_1.json', 123, TypeError),
    (
        './hw2/test_data/IO_data/valid_data/input_data/input_1.json',
        './hw2/test_data/IO_data/invalid_data/not_json.txt',
        exceptions.FileIsNotJsonError,
    ),
    (
        './hw2/test_data/IO_data/valid_data/input_data/input_1.json',
        'non_existent_file.json',
        FileNotFoundError,
    ),
)


def test_invalid_test_data():
    """Test invalid test data."""
    for input_file_path, output_file_path, error in invalid_test_data:
        with pytest.raises(error):
            process_data(input_file_path, output_file_path)
