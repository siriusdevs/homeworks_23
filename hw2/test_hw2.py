"""Module that tests the main function from hw2 module."""
import json

import errors as err
import pytest
from consts import JsonStats
from json_parsing import assemble_data, get_abspath

GOOD_RESULT = (
    ('empty.json', {
        'email': {},
        'registered': {},
    }),
    ('example.json', {
        'email': {
            'mail.ru': 42.86,
            'gmail.com': 28.57,
            'mail.bel': 14.29,
            'soplya.ru': 14.29,
        },
        'registered': {
            '2012': 57.14,
            '2011': 28.57,
            '2013': 14.29,
        },
    }),
    ('simple.json', {
        'email': {
            'yandex.ru': 50.0,
            'gmail.com': 50.0,
        },
        'registered': {
            '2012': 50.0,
            '2022': 50.0,
        },
    }),
)

INVALID_PATH = 'invalid_path.json'
ERROR_RESULTS = (
    (INVALID_PATH, err.InvalidFilePathException),
    ('raspisanie_sessii.json', err.InvalidFilePathException),
    ('invalid_format.json', err.JSONIncorrectFieldFormat),
    ('missing_year.json', err.JSONMissingFieldException),
    ('nothing.json', json.decoder.JSONDecodeError),
)


@pytest.mark.parametrize('test_filename, expected', GOOD_RESULT)
def test_assemble_data(test_filename: str, expected: JsonStats) -> None:
    """Asserts that function assemble_data(input_filename, output_filename) writes $expected.

    Args:
        test_filename (str): name of a file that is used for testing.
        expected (JsonStats): expected JSON output value that main function writes.
    """
    assemble_data(test_filename, test_filename)
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
