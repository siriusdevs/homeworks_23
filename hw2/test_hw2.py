"""pytest tests for hw2 module."""
import json
import os
import tempfile
from datetime import datetime
from typing import Any

import pytest

import const_hw2
from hw2 import aggregate_users_stats

EMPTY_INPUT_FILE = 'test_data/empty.json'
TESTS_TABLE = (
    (EMPTY_INPUT_FILE, {
        const_hw2.LESS_TWO_DAYS: 0,
        const_hw2.LESS_WEEK: 0,
        const_hw2.LESS_MONTH: 0,
        const_hw2.LESS_HALFYEAR: 0,
        const_hw2.GREATER_HALFYEAR: 0,
        const_hw2.AGE_MAX: 0,
        const_hw2.AGE_MIN: 0,
        const_hw2.AGE_AVERAGE: 0,
        const_hw2.AGE_MEDIAN: 0,
    }),
    ('test_data/example.json', {
        const_hw2.LESS_TWO_DAYS: 0,
        const_hw2.LESS_WEEK: 36,
        const_hw2.LESS_MONTH: 36,
        const_hw2.LESS_HALFYEAR: 36,
        const_hw2.GREATER_HALFYEAR: 18,
        const_hw2.AGE_MAX: 36,
        const_hw2.AGE_MIN: 18,
        const_hw2.AGE_AVERAGE: 27,
        const_hw2.AGE_MEDIAN: 27,
    }),
    ('test_data/complex.json', {
        const_hw2.LESS_TWO_DAYS: 11,
        const_hw2.LESS_WEEK: 11,
        const_hw2.LESS_MONTH: 14.67,
        const_hw2.LESS_HALFYEAR: 23,
        const_hw2.GREATER_HALFYEAR: 29.4,
        const_hw2.AGE_MAX: 60,
        const_hw2.AGE_MIN: 10,
        const_hw2.AGE_AVERAGE: 25,
        const_hw2.AGE_MEDIAN: 20,
    }),
)

# Since aggregate_users_stats() works with time.now,
# we need to mock it, so that tests don't become invalid after time passes.
# MOCK_NOW is passed in the hidden _now parameter to aggregate_users_stats().
# TODO: use a proper mocking library
MOCK_NOW = datetime(year=2023, month=11, day=4, hour=16)


@pytest.mark.parametrize('input_path, expected', TESTS_TABLE)
def test_aggregate_users_stats(input_path: str, expected: dict[str, Any]):
    """Asserts that calling aggregate_users_stats(input_path, output_file) writes $expected.

    Args:
        input_path: path to a file from which to get users stats
        expected: the json value that should be written by aggregate_users_stats()
    """
    with tempfile.NamedTemporaryFile() as output:
        aggregate_users_stats(input_path, output.name, _now=MOCK_NOW)
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
