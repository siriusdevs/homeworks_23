"""Tests for hw2.py."""
import json
import os
from datetime import date
from tempfile import NamedTemporaryFile, TemporaryDirectory
from typing import Type
from unittest.mock import patch

import constants
import exceptions
import pytest

from hw2 import process_data

TEST_DATA_FOLDER = 'hw2/test_data/'
LONG_PATH = 'the/longest/path/ever/output.json'
OUTPUT_FILE_PATH = f'{TEST_DATA_FOLDER}/output.json'

TEST_DATA = (
    ('empty.json', {
        constants.MINIMUM: 0,
        constants.MAXIMUM: 0,
        constants.AVERAGE: 0,
        constants.MEDIAN: 0,
        constants.LESS_TWO_DAYS: 0,
        constants.LESS_WEEK: 0,
        constants.LESS_MONTH: 0,
        constants.LESS_HALF_YEAR: 0,
        constants.GREATER_HALF_YEAR: 0,
    }),
    ('ok.json', {
        constants.MINIMUM: 8,
        constants.MAXIMUM: 84,
        constants.AVERAGE: 37.67,
        constants.MEDIAN: 29,
        constants.LESS_TWO_DAYS: 29.67,
        constants.LESS_WEEK: 42.25,
        constants.LESS_MONTH: 35.4,
        constants.LESS_HALF_YEAR: 33,
        constants.GREATER_HALF_YEAR: 47,
    }),
)

EXCEPTIONS_TEST_DATA = (
    ('not_found.json', exceptions.InvalidInputFileError),
    ('invalid.json', exceptions.InvalidInputFileError),
    ('invalid_date.json', exceptions.InvalidDateError),
    ('invalid_date_format.json', exceptions.InvalidDateFormatError),
    ('missing_last_login.json', exceptions.MissingFieldError),
    ('missing_age.json', exceptions.MissingFieldError),
)


def test_long_path_file():
    """Test creating output file with very long path."""
    with TemporaryDirectory() as testdir:
        full_path = os.path.join(testdir, LONG_PATH)
        process_data(f'{TEST_DATA_FOLDER}/empty.json', full_path)
        assert os.path.exists(full_path)


@patch('statistics.date')
@pytest.mark.parametrize('input_path, expected', TEST_DATA)
def test_process_data(mock_date, input_path: str, expected: constants.STATS_JSON) -> None:
    """Test process_data() function with correct test_data.

    Args:
        mock_date: mocking object for datetime.date in statistics module
        input_path: path to input JSON file with current test data
        expected: expected value for current test data

    Asserts:
        True if function with current test data returns right error type and error message.
    """
    mock_date.today.return_value = date(2022, 9, 1)
    with NamedTemporaryFile() as output:
        process_data(f'{TEST_DATA_FOLDER}{input_path}', str(output.name))
        assert sorted(json.load(output)) == sorted(expected)


@pytest.mark.parametrize('input_path, error_type', EXCEPTIONS_TEST_DATA)
def test_exceptions(input_path: str, error_type: Type[Exception]) -> None:
    """Test exceptions that causes process_data() function.

    Args:
        input_path: path to input JSON file with current test data
        error_type: expected error for current test data

    Asserts:
        True if function with current test data returns correct error type.
    """
    with pytest.raises(error_type):
        process_data(f'{TEST_DATA_FOLDER}{input_path}', OUTPUT_FILE_PATH)
