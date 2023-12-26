"""Tests for HW2."""
import json
import os
from datetime import date
from typing import Type
from unittest.mock import patch

import pytest

from hw2 import GEOGRAPHY_STATS, LAST_LOGIN_STATS, Stats, process_data

TEST_DATA_FOLDER = 'hw2/test_json/'
LONG_PATH = f'{TEST_DATA_FOLDER}/folder1/folder2/folder3'
OUTPUT_FILE_PATH = f'{TEST_DATA_FOLDER}/output.json'

TEST_DATA = (
    ('empty.json', {
        GEOGRAPHY_STATS: None,
        LAST_LOGIN_STATS: None,
    }),
    ('ok.json', {
        GEOGRAPHY_STATS: {
            'Vladimir': 20.0,
            'Saratov': 40.0,
            'Krasnodar': 20.0,
            'Sirius': 20.0,
        },
        LAST_LOGIN_STATS: {
            'less_two_days': 44.0,
            'less_week': 33.0,
            'less_month': 42.0,
            'less_half_year': 40.5,
            'greater_half_year': 45.0,
        },
    }),
)

EXCEPTIONS_TEST_DATA = (
    ('not_found.json', FileNotFoundError),
    ('invalid.json', FileNotFoundError),
    ('invalid_date.json', ValueError),
    ('invalid_date_format.json', TypeError),
    ('missing_last_login.json', KeyError),
    ('missing_age.json', KeyError),
    ('missing_region.json', KeyError),
)


def test_long_path_file():
    """Test for long path file.

    Asserts:
        True if long path is existing, else False
    """
    process_data(f'{TEST_DATA_FOLDER}/empty.json', f'{LONG_PATH}/output.json')
    assert os.path.exists(LONG_PATH)

    os.remove(f'{LONG_PATH}/output.json')
    os.removedirs(LONG_PATH)


@patch('hw2.date')
@pytest.mark.parametrize('input_path, expected', TEST_DATA)
def test_process_data(mock_date, input_path: str, expected: Stats) -> None:
    """Tests process data.

    Args:
        mock_date: mock object for fixing today date
        input_path: input json file
        expected: expected dict of statistics
    """
    mock_date.today.return_value = date(2022, 4, 13)

    process_data(f'{TEST_DATA_FOLDER}{input_path}', OUTPUT_FILE_PATH)
    with open(OUTPUT_FILE_PATH, 'r') as output:
        assert sorted(json.load(output)) == sorted(expected)
    os.remove(OUTPUT_FILE_PATH)


@pytest.mark.parametrize('input_path, error_type', EXCEPTIONS_TEST_DATA)
def test_exceptions(input_path: str, error_type: Type[Exception]) -> None:
    """Tests errors.

    Args:
        input_path: input json file
        error_type: type of error
    """
    with pytest.raises(error_type):
        process_data(f'{TEST_DATA_FOLDER}{input_path}', OUTPUT_FILE_PATH)
