"""This module include test of function process_data."""

import json

import pytest

from hw2 import process_data

COUNTTESTFILE = 12


def make_tests():
    """Create test data.

    Returns:
        A tuple with data test.
    """
    res = []
    for num in range(1, COUNTTESTFILE):
        input_file = f'input/{num}.json'
        output_file = f'output/{num}.json'

        with open(f'expected/{num}.json') as file_excepted:
            excepted = json.load(file_excepted)
        res.append((input_file, output_file, excepted))
    return tuple(res)


TEST_PROCESS_DATA = make_tests()


@pytest.mark.parametrize('input_filepath,output_filepath,expected', TEST_PROCESS_DATA)
def test_process_data(input_filepath: str, output_filepath: str, expected: dict) -> None:
    """A function that tests process_data function.

    Args:
        input_filepath: path to json file with data on site clients
        output_filepath: path to json output file
        expected:  expected function output.
    """
    process_data(input_filepath, output_filepath)
    with open(output_filepath, 'r') as file1:
        input_file = json.load(file1)
    assert input_file == expected
