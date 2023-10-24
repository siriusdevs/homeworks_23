"""Tests for hw1.py."""
import pytest

from hw1 import SalaryStats, get_salary_stats

test_data = (
    ((), {}, SalaryStats(maximum=0, average=0, median=0)),
)


@pytest.mark.parametrize('args, kwargs, expected', test_data)
def test_get_salary_stats(args: tuple, kwargs: dict, expected: SalaryStats):
    """Asserts that calling get_salary_stats with args and kwargs returns expected.

    Args:
        args: arguments to forward to get_salary_stats
        kwargs: keyword arguments to forward to get_salary_stats
        expected: expected result of the get_salary_stats call
    """
    assert get_salary_stats(*args, **kwargs) == expected
