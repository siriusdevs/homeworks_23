"""pytest tests for hw2 module."""
import json
import os
import tempfile
from datetime import datetime
from typing import Any

import pytest

from . import fields_hw2, hw2, types_hw2

EMPTY_INPUT_FILE = 'test_data/empty.json'
HAPPY_PATHS = (
    (EMPTY_INPUT_FILE, {
        fields_hw2.LESS_TWO_DAYS: 0,
        fields_hw2.LESS_WEEK: 0,
        fields_hw2.LESS_MONTH: 0,
        fields_hw2.LESS_HALFYEAR: 0,
        fields_hw2.GREATER_HALFYEAR: 0,
        fields_hw2.AGE_MAX: 0,
        fields_hw2.AGE_MIN: 0,
        fields_hw2.AGE_AVERAGE: 0,
        fields_hw2.AGE_MEDIAN: 0,
    }),
    ('test_data/example.json', {
        fields_hw2.LESS_TWO_DAYS: 0,
        fields_hw2.LESS_WEEK: 36,
        fields_hw2.LESS_MONTH: 36,
        fields_hw2.LESS_HALFYEAR: 36,
        fields_hw2.GREATER_HALFYEAR: 18,
        fields_hw2.AGE_MAX: 36,
        fields_hw2.AGE_MIN: 18,
        fields_hw2.AGE_AVERAGE: 27,
        fields_hw2.AGE_MEDIAN: 27,
    }),
    ('test_data/complex.json', {
        fields_hw2.LESS_TWO_DAYS: 11,
        fields_hw2.LESS_WEEK: 11,
        fields_hw2.LESS_MONTH: 14.67,
        fields_hw2.LESS_HALFYEAR: 23,
        fields_hw2.GREATER_HALFYEAR: 29.4,
        fields_hw2.AGE_MAX: 60,
        fields_hw2.AGE_MIN: 10,
        fields_hw2.AGE_AVERAGE: 25,
        fields_hw2.AGE_MEDIAN: 20,
    }),
)

ERROR_PATHS = (
    ('test_data/invalid_json.json', types_hw2.InvalidInputFileException),
    ('test_data/does_not_exist', types_hw2.InvalidInputFileException),
    ('test_data/invalid_date.json', types_hw2.InvalidDateException),
    ('test_data/missing_age.json', types_hw2.MissingFieldException),
)


# Since aggregate_users_stats() works with time.now,
# we need to mock it, so that tests don't become invalid after time passes.
# MOCK_NOW is passed in the hidden _now parameter to aggregate_users_stats().
# TODO: use a proper mocking library
MOCK_NOW = datetime(year=2023, month=11, day=4, hour=16)


def test_aggregate_users_stats_file_creation():
    """Asserts that aggregate_users_stats() creates the output file and path to it."""
    with tempfile.TemporaryDirectory() as tempdir:
        output_path = os.path.join(tempdir, 'test', 'inner', 'more_inner', 'output.json')
        hw2.aggregate_users_stats(EMPTY_INPUT_FILE, output_path)
        assert os.path.exists(output_path)


@pytest.mark.parametrize('input_path, expected', HAPPY_PATHS)
def test_aggregate_users_stats(input_path: str, expected: dict[str, Any]):
    """Asserts that calling aggregate_users_stats(input_path, output_file) writes $expected.

    Args:
        input_path: path to a file from which to get users stats
        expected: the json value that should be written by aggregate_users_stats()
    """
    with tempfile.NamedTemporaryFile() as output:
        hw2.aggregate_users_stats(input_path, output.name, _now=MOCK_NOW)
        got = json.load(output)
        assert sorted(got.items()) == sorted(expected.items())


@pytest.mark.parametrize('input_path, expected', ERROR_PATHS)
def test_aggregate_users_stats_exceptions(input_path: str, expected: type):
    """Asserts that calling aggregate_users_stats(input_path, output_file) raises $expected.

    Args:
        input_path: path to a file from which to get users stats
        expected: the exception that tested function must raise
    """
    with pytest.raises(expected):
        hw2.aggregate_users_stats(input_path, tempfile.mkstemp()[1])
