"""Module that tests the main function from hw2 module."""
import json

import errors as err
import pytest
from json_parsing import assemble_data, get_abspath

GOOD_RESULT = (
    ('example.json'),
    ('empty.json'),
    ('simple.json'),
)

INVALID_PATH = 'invalid_path.json'
ERROR_RESULTS = (
    (INVALID_PATH, err.InvalidFilePathException),
    ('raspisanie_sessii.json', err.InvalidFilePathException),
    ('invalid_format.json', err.JSONIncorrectFieldFormat),
    ('missing_year.json', err.JSONMissingFieldException),
    ('nothing.json', json.decoder.JSONDecodeError),
)


@pytest.mark.parametrize('test_filename', GOOD_RESULT)
def test_assemble_data(test_filename: str) -> None:
    """Asserts that function assemble_data(input_filename) writes $expected.

    Args:
        test_filename (str): name of a file that is used for testing.
    """
    assemble_data(test_filename, test_filename)
    with open(get_abspath(test_filename, 'expected'), 'r') as expect_out:
        expected = json.load(expect_out)
    with open(get_abspath(test_filename, 'outputs'), 'r') as output:
        collected = json.load(output)
    assert collected == expected


@pytest.mark.parametrize('test_filename, expected', ERROR_RESULTS)
def test_assemble_data_exceptions(test_filename: str, expected: type):
    """Asserts that function assemble_data(input_filename, output_filename) raises $expected.

    Args:
        test_filename (str): name of a file that is used for testing.
        expected (type): exception that would be raised by function.
    """
    with pytest.raises(expected):
        assemble_data(test_filename, test_filename)
