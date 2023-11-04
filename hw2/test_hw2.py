"""pytest tests for hw2 module."""
from datetime import datetime
import json
import os
import tempfile
from typing import Any

import const
import pytest

from hw2 import AgeStats, aggregate_users_stats

# Since aggregate_users_stats() works with time.now,
# we need to mock it, so that tests don't become invalid after time passes.
# MOCK_NOW is passed in the hidden _now parameter to aggregate_users_stats().
# TODO: use a proper mocking library
MOCK_NOW = datetime(year=2023, month=10, day=4, hour=16)

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
        const.LESS_WEEK: AgeStats(max=36, min=36, mean=36, median=36).to_json(),
        const.LESS_MONTH: AgeStats(max=36, min=36, mean=36, median=36).to_json(),
        const.LESS_HALFYEAR: AgeStats(max=36, min=36, mean=36, median=36).to_json(),
        const.GREATER_HALFYEAR: AgeStats(max=18, min=18, mean=18, median=18).to_json(),
    }),
)


@pytest.mark.parametrize('input_file, expected', TESTS_TABLE)
def test_aggregate_users_stats(input_file: str, expected: dict[str, Any]):
    """Asserts that calling aggregate_users_stats(input_file, output_file) writes expected.

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
