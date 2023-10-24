"""Tests for hw1.py."""

from dataclasses import dataclass
from types import MappingProxyType

import pytest

from hw1 import Salaries, SalaryStats, Units, get_salary_stats


@dataclass
class SalaryStatsTestCase:
    """A test case for get_salary_stats."""

    name: str
    units: Units
    salaries: dict[str, Salaries]
    expected_stats: SalaryStats


# MappingProxyType is used for ensuring inmutability of the underlying dictionary
TEST_COMPANY = MappingProxyType({
    'IT': {'John': 100.0, 'Bob': 200.0, 'Alice': 50.0},
    'Banking': {'name1': 10.0, 'name2': 20.0, 'name3': 30.0, 'name4': 40.0},
    'Marketing': {'name5': 1.5, 'name6': 1.6, 'name7': 1.7, 'name8': 1.8},
})

TESTS_TABLE = (
    SalaryStatsTestCase(
        name='with empty arguments',
        units=None,
        salaries={},
        expected_stats=SalaryStats(maximum=0, average=0, median=0),
    ),
    SalaryStatsTestCase(
        name='simple with all units',
        units=None,
        salaries={'A': {'1': 1, '2': 2, '3': 3}, 'B': {'4': 4, '5': 5}},
        expected_stats=SalaryStats(maximum=5, average=3, median=3),
    ),
    SalaryStatsTestCase(
        name='simple with specific units',
        units=('C', 'D'),
        salaries={
            'C': {'name1': 500.42, 'name2': 30.12, 'name3': 50_000},
            'D': {'name4': 4, 'name5': 5},
            'Should be excluded': {'name6': 100_000, 'name7': 0.01},
            'Should also be excluded': {'name8': 200_000, 'name9': 0.001},
        },
        expected_stats=SalaryStats(maximum=50_000, average=10107.91, median=30.12),
    ),
    SalaryStatsTestCase(
        name='complex with all units',
        units=None,
        salaries=dict(TEST_COMPANY),
        expected_stats=SalaryStats(maximum=200, average=41.51, median=20),
    ),
    SalaryStatsTestCase(
        name='complex with specific units',
        units=('Banking', 'Marketing'),
        salaries=dict(TEST_COMPANY),
        expected_stats=SalaryStats(maximum=40, average=13.32, median=5.9),
    ),
    SalaryStatsTestCase(
        name='should round max',
        units=None,
        salaries={'A': {'person': 100.123456}},
        expected_stats=SalaryStats(maximum=100.12, average=100.12, median=100.12),
    ),
)


@pytest.mark.parametrize('tc', TESTS_TABLE, ids=lambda tc: tc.name)
def test_get_salary_stats(tc: SalaryStatsTestCase):
    """Assert that the provided SalaryStatsTestCase passes.

    Args:
        tc: a test case with input and expected output
    """
    assert get_salary_stats(tc.units, **tc.salaries) == tc.expected_stats
