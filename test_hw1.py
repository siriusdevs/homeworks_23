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


TESTS_TABLE = (
    SalaryStatsTestCase(
        name='empty arguments',
        units=None,
        salaries={},
        expected_stats=SalaryStats(maximum=0, average=0, median=0),
    ),
)


@pytest.mark.parametrize('tc', TESTS_TABLE, ids=lambda tc: tc.name)
def test_get_salary_stats(tc: SalaryStatsTestCase):
    """Assert that the provided SalaryStatsTestCase passes.

    Args:
        tc: a test case with input and expected output
    """
    assert get_salary_stats(None, **tc.salaries) == tc.expected_stats
