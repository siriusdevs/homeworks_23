"""Test module for function calculate_salary_stats from HW_1.py."""

import pytest

from hw1 import calculate_salary_stats

TESTING_DATA = (
    (
        (
            ('Development', [430.0, 230.7, 8708.32]),
            ('Marketing', [1355.0, 350.3, 1453.53]),
            ('Sales', [9245.0, 3110.56, 7921.23]),
        ),
        2000,
        (
            [9245.0, 8708.32, 7921.23],
            89.27,
        ),
    ),
    (
        (
            ('Teachers', [5644.0, 1234.5, 3253.75]),
            ('Marketing', [1355.0, 350.3]),
            ('Sales', [2245.0]),
        ),
        None,
        (
            [5644.0, 3253.75, 2245.0],
            79.12,
        ),
    ),
    (
        (
            ('IT', [5554.0, 12434.5, 3253.75]),
            ('Teachers', [154255.0, 35250.3]),
        ),
        20000,
        (
            [154255.0, 35250.3],
            100,
        ),
    ),
)


@pytest.mark.parametrize('company, limit, expected', TESTING_DATA)
def test_data(
    company: tuple[str, list[float]],
    limit: float | None,
    expected: tuple[list[float], float],
):
    """
    Test the calculate_salary_stats function with data.

    Args:
        company: tuple with departments names their values.
        limit: the maximum wage value (float) to be taken into account.
        expected: A tuple containing top salary and the ratio of the amount \
            of this top to the entire amount of payments in the company
    """
    assert calculate_salary_stats(*company, salary_limit=limit) == expected
