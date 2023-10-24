"""Tests for hw1.py."""

from dataclasses import dataclass

import pytest

from hw1 import Salaries, SalaryStats, Units, get_salary_stats


@dataclass
class SalaryStatsTestCase:
    """A test case for get_salary_stats."""

    name: str
    units: Units
    salaries: dict[str, Salaries]
    expected_stats: SalaryStats


TEST_COMPANY = {
    'IT': {'John': 100, 'Bob': 200, 'Alice': 50},
    'Banking': {'name1': 10, 'name2': 20, 'name3': 30, 'name4': 40}, 
    'Marketing': {'name5': 1.5, 'name6': 1.6, 'name7': 1.7, 'name8': 1.8},
}

TESTS_TABLE = (
    SalaryStatsTestCase(
        name='empty arguments',
        units=None,
        salaries={},
        expected_stats=SalaryStats(maximum=0, average=0, median=0),
    ),
    SalaryStatsTestCase(
        name='without excluded units',
        units=None,
        salaries=TEST_COMPANY,
        expected_stats=SalaryStats(maximum=200, average=41.51, median=20),
    ),
)


@pytest.mark.parametrize('tc', TESTS_TABLE, ids=lambda tc: tc.name)
def test_get_salary_stats(tc: SalaryStatsTestCase):
    """Assert that the provided SalaryStatsTestCase passes.

    Args:
        tc: a test case with input and expected output
    """
    assert get_salary_stats(None, **tc.salaries) == tc.expected_stats
