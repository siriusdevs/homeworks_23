"""pytest tests for hw2 module."""
import json
import os
import tempfile
from datetime import datetime
from typing import Any

import pytest

import const
from hw2 import aggregate_users_stats

EMPTY_INPUT_FILE = 'test_data/empty.json'
TESTS_TABLE = (
    (EMPTY_INPUT_FILE, {
        const.LESS_TWO_DAYS: 0,
        const.LESS_WEEK: 0,
        const.LESS_MONTH: 0,
        const.LESS_HALFYEAR: 0,
        const.GREATER_HALFYEAR: 0,
        const.AGE_MAX: 0,
        const.AGE_MIN: 0,
        const.AGE_AVERAGE: 0,
        const.AGE_MEDIAN: 0,
    }),
    ('test_data/example.json', {
        const.LESS_TWO_DAYS: 0,
        const.LESS_WEEK: 36,
        const.LESS_MONTH: 36,
        const.LESS_HALFYEAR: 36,
        const.GREATER_HALFYEAR: 18,
        const.AGE_MAX: 36,
        const.AGE_MIN: 18,
        const.AGE_AVERAGE: 27,
        const.AGE_MEDIAN: 27,
    }),
    ('test_data/complex.json', {
        const.LESS_TWO_DAYS: 11,
        const.LESS_WEEK: 11,
        const.LESS_MONTH: 14.67,
        const.LESS_HALFYEAR: 23,
        const.GREATER_HALFYEAR: 29.4,
        const.AGE_MAX: 60,
        const.AGE_MIN: 10,
        const.AGE_AVERAGE: 25,
        const.AGE_MEDIAN: 20,
    }),
)

# Since aggregate_users_stats() works with time.now,
# we need to mock it, so that tests don't become invalid after time passes.
# MOCK_NOW is passed in the hidden _now parameter to aggregate_users_stats().
# TODO: use a proper mocking library
MOCK_NOW = datetime(year=2023, month=11, day=4, hour=16)


@pytest.mark.parametrize('input_file, expected', TESTS_TABLE)
def test_aggregate_users_stats(input_file: str, expected: dict[str, Any]):
    """Asserts that calling aggregate_users_stats(input_file, output_file) writes $expected.

    Args:
        input_file: path to a file from which to get users stats
        expected: the json value that should be written by aggregate_users_stats()
    """
    with tempfile.NamedTemporaryFile() as output:
        aggregate_users_stats(input_file, output.name, _now=MOCK_NOW)
        got = json.load(output)
        assert sorted(got.items()) == sorted(expected.items())


def test_aggregate_users_stats_file_creation():
    """Asserts that aggregate_users_stats() creates the output file if it doesn't exist."""
    tmp_output = tempfile.TemporaryFile()
    output_path = str(tmp_output.name)
    tmp_output.close()  # deletes this file, so that we can check file creation by tested function

    aggregate_users_stats(EMPTY_INPUT_FILE, output_path)
    assert os.path.exists(output_path)
    os.remove(output_path)
