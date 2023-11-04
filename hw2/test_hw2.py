"""pytest tests for hw2 module."""
import json
import os
import tempfile
from datetime import datetime
from typing import Any

import const
import pytest

from hw2 import AgeStats, aggregate_users_stats

EMPTY_INPUT_FILE = 'test_data/empty.json'
TESTS_TABLE = (
    (EMPTY_INPUT_FILE, {
        const.LESS_TWO_DAYS: AgeStats().to_json(),
        const.LESS_WEEK: AgeStats().to_json(),
        const.LESS_MONTH: AgeStats().to_json(),
        const.LESS_HALFYEAR: AgeStats().to_json(),
        const.GREATER_HALFYEAR: AgeStats().to_json(),
    }),
    ('test_data/example.json', {
        const.LESS_TWO_DAYS: AgeStats().to_json(),
        const.LESS_WEEK: AgeStats(max=36, min=36, average=36, median=36).to_json(),
        const.LESS_MONTH: AgeStats(max=36, min=36, average=36, median=36).to_json(),
        const.LESS_HALFYEAR: AgeStats(max=36, min=36, average=36, median=36).to_json(),
        const.GREATER_HALFYEAR: AgeStats(max=18, min=18, average=18, median=18).to_json(),
    }),
    ('test_data/complex.json', {
        const.LESS_TWO_DAYS: AgeStats(max=11, min=11, average=11, median=11).to_json(),
        const.LESS_WEEK: AgeStats(min=10, max=12, average=11, median=11).to_json(),
        const.LESS_MONTH: AgeStats(min=10, max=22, average=14.67, median=13.5).to_json(),
        const.LESS_HALFYEAR: AgeStats(min=10, max=60, average=23, median=16).to_json(),
        const.GREATER_HALFYEAR: AgeStats(min=10, max=42, average=29.4, median=32).to_json(),
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
