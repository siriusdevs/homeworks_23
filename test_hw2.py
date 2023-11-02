"""This module include test of function process_data."""

import json

import pytest

from hw2 import NotCorrectFormatDate, process_data


def make_tests():
    """Create test data.

    Returns:
        A tuple with data test.
    """
    res = []
    for num in range(1, 5):
        input_file = f'hw2/input/{num}.json'
        output_file = f'hw2/output/{num}.json'

        with open(f'hw2/expected/{num}.json') as file_excepted:
            excepted = json.load(file_excepted)
        res.append((input_file, output_file, excepted))
    return tuple(res)


TEST_PROCESS_DATA = make_tests()
TEST_ERROR_PROCESS_DATA = (
    ('/home/runner/work/homeworks_23/hw2/data.json',
     '/home/runner/work/homeworks_23/hw2/datas_output.json', 'Is not a file path',
     ),
    ('/home/runner/work/homeworks_23/hw2/data_hw2.json',
     '/home/runner/work/homeworks_23/hw2/data.json', 'Is not a file path',
     ),
    ('hw2/input/5.json',
     'hw2/output/5.json', 'Input file is empty',
     ),
    ('hw2/input/6.json',
     'hw2/output/6.json', '201212-24 not in format YYYY-MM-DD',
     ),
)


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


@pytest.mark.parametrize('input_filepath,output_filepath,expected', TEST_ERROR_PROCESS_DATA)
def test_errors_process_data(input_filepath: str, output_filepath: str, expected: str) -> None:
    """A function that tests process_data function.

    Args:
        input_filepath: path to json file with data on site clients
        output_filepath: path to json output file
        expected:  expected function output.
    """
    try:
        process_data(input_filepath, output_filepath)
    except (FileNotFoundError, NotCorrectFormatDate) as err:
        assert expected == str(err)
