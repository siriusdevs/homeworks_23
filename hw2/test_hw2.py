"""pytest tests for hw2 module."""
import dataclasses
import json
import tempfile
from typing import Any

import const
import pytest

from hw2 import AgeStats, aggregate_users_stats

TESTS_TABLE = (
    ('test_data/empty.json', {
        const.LESS_TWO_DAYS: dataclasses.asdict(AgeStats()),
        const.LESS_WEEK: dataclasses.asdict(AgeStats()),
        const.LESS_MONTH: dataclasses.asdict(AgeStats()),
        const.LESS_HALFYEAR: dataclasses.asdict(AgeStats()),
        const.GREATER_HALFYEAR: dataclasses.asdict(AgeStats()),
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
        aggregate_users_stats(input_file, output.name)
        got = json.load(output)
        assert sorted(got.items()) == sorted(expected.items())
