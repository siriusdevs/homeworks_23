"""Tests for hw1.py."""
from dataclasses import dataclass
from typing import Type

import pytest

from hw1 import AbsenceError, Deps, SalaryStats, UsedDeps, get_salary_stats


@dataclass
class SalaryStatsTestCase:
    """Test case for hw1 (get_salary_stats function) tests.

    Args:
        name: name of test case
        deps: test deps
        used_deps: test used_deps
        expected: expected value for current test data
    """

    name: str
    deps: tuple[Deps, ...]
    used_deps: UsedDeps
    # expected value or error message
    expected: SalaryStats | str


@dataclass
class SalaryStatsErrorTestCase(SalaryStatsTestCase):
    """Test case for hw1 (get_salary_stats function) tests ending with error.

    Args:
        name: name of test case
        deps: test deps
        used_deps: test used_deps
        expected: expected value for current test data
        error_type: type of error that current test should end with
    """

    error_type: Type[Exception]


TEST_DEPS_DATA = (
    (
        'development',
        {'name1': 111.111, 'name2': 10, 'name3': 25.207},
    ),
    (
        'testing',
        {'name4': 123.456, 'name5': 0},
    ),
    (
        'marketing',
        {'name6': 77.78},
    ),
)

TEST_DATA = (
    SalaryStatsTestCase(
        name='one departament',
        deps=(
            ('test_dep', {'test_name': 43.56}),
        ),
        used_deps=None,
        expected=SalaryStats(
            top_salaries=[43.56],
            top_salaries_percent=100,
        ),
    ),
    SalaryStatsTestCase(
        name='used all departments',
        deps=TEST_DEPS_DATA,
        used_deps=None,
        expected=SalaryStats(
            top_salaries=[123.46, 111.11, 77.78],
            top_salaries_percent=89.87,
        ),
    ),
    SalaryStatsTestCase(
        name='used specific departments',
        deps=TEST_DEPS_DATA,
        used_deps=('development', 'testing'),
        expected=SalaryStats(
            top_salaries=[123.46, 111.11, 25.21],
            top_salaries_percent=96.29,
        ),
    ),
    SalaryStatsTestCase(
        name='wrong specific departments',
        deps=TEST_DEPS_DATA,
        used_deps=('development', 'integrating', 'designing'),
        expected=SalaryStats(
            top_salaries=[111.11, 25.21, 10.0],
            top_salaries_percent=100,
        ),
    ),
)

TEST_ERROR_DATA = (
    SalaryStatsErrorTestCase(
        name='empty arguments',
        deps=(
            ('', {}),
        ),
        used_deps=None,
        expected='No one salary was found.',
        error_type=AbsenceError,
    ),
    SalaryStatsErrorTestCase(
        name='all salaries are 0',
        deps=(
            (
                'developing',
                {'name1': 0, 'name2': 0, 'name3': 0},
            ),
        ),
        used_deps=None,
        expected='All salaries are 0.',
        error_type=ValueError,
    ),
)


@pytest.mark.parametrize('test_case', TEST_DATA, ids=lambda tc: tc.name)
def test_get_salary_stats(test_case: SalaryStatsTestCase):
    """Test salary stats function (get_salary_stats) with test data and expected value.

    Args:
        test_case: test and expected data in SalaryStatsTestCase format

    Asserts:
        True if function with current test data returns right answer.
    """
    assert get_salary_stats(*test_case.deps, used_deps=test_case.used_deps) == test_case.expected


@pytest.mark.parametrize('test_case', TEST_ERROR_DATA, ids=lambda tc: tc.name)
def test_get_salary_stats_errors(test_case: SalaryStatsErrorTestCase):
    """Test salary stats function (get_salary_stats) with test data and expected error.

    Args:
        test_case: test and expected error data in SalaryStatsTestCase format

    Asserts:
        True if function with current test data returns right error type and error message.
    """
    # check error type
    with pytest.raises(test_case.error_type) as exc:
        get_salary_stats(*test_case.deps, used_deps=test_case.used_deps)

        # check error message
        exc_msg = exc.value.args[0]
        assert exc_msg == test_case.expected
