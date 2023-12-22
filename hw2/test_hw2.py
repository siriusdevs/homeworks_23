"""Tests for hw2."""
import json
import tempfile
from typing import Any

import pytest

import consts_hw2 as cnst
import hw2

ZEROS = '0.0%'
ERROR = 'ERROR'
CORRECT_DATA = (
    ('tests/normal.json', {
        cnst.AGE_MAX: 143,
        cnst.AGE_MIN: 18,
        cnst.AGE_AVERAGE: 80.5,
        cnst.AGE_MEDIAN: 80.5,
        cnst.LESS_TWO_DAYS: ZEROS,
        cnst.LESS_WEEK: ZEROS,
        cnst.LESS_MONTH: '0.0%',
        cnst.LESS_HALFYEAR: '50.0%',
        cnst.MORE_HALFYEAR: '50.0%',
    }),
    ('tests/normal2.json', {
        cnst.AGE_MAX: 90,
        cnst.AGE_MIN: 4,
        cnst.AGE_AVERAGE: 45.0,
        cnst.AGE_MEDIAN: 38.5,
        cnst.LESS_TWO_DAYS: ZEROS,
        cnst.LESS_WEEK: '0.0%',
        cnst.LESS_MONTH: '16.67%',
        cnst.LESS_HALFYEAR: '50.0%',
        cnst.MORE_HALFYEAR: '33.33%',
    }),
)

INVALID_DATA = (
    ('tests/empty.json', {
        ERROR: 'Empty json file was found at path tests/empty.json.',
    }),
    ('tests/incorrect_data.json', {
        ERROR: 'Wrong date format, expected format: 2020-12-30, but got 2012-1001.',
    }),
    ('tests/invalid_format.json', {
        'ERROR': 'An incorrect json file structure was found at path tests/invalid_format.json.',
    }),
    ('tests/no_age.json', {
        ERROR: '\"age\" field does not exist. Every user should have \"age\" field.',
    }),
    ('tests/no_last_login.json', {
        ERROR: '\"last_login\" field does not exist. Every user should have \"last_login\" field.',
    }),
)


@pytest.mark.parametrize('input_path, expected', CORRECT_DATA)
def test_correct_data(input_path: str, expected: dict[str, Any]):
    """Checks that the process data function correctly calculates and saves data.

    Args:
        input_path (str): path to source json file.
        expected (dict[str, Any]): expected processed stats.
    """
    with tempfile.NamedTemporaryFile() as output:
        hw2.process_data(input_path, output.name)
        got = json.load(output)
        assert got == expected


@pytest.mark.parametrize('input_path, expected', INVALID_DATA)
def test_exceptions(input_path: str, expected: type):
    """Checks that the process data function correctly calls exceptions.

    Args:
        input_path (str): path to source json file.
        expected (type): exception that should be called.
    """
    with tempfile.NamedTemporaryFile() as output:
        hw2.process_data(input_path, output.name)
        got = json.load(output)
        assert got.items() == expected.items()
