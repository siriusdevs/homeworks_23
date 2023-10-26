"""This module include test for function."""


import pytest

from hw1 import statistic_salary

COMPANS = (
    (
        1000,
        (
            'TVD', {'Ivanov': 800.0},
        ),
        (800.0, 800.0, 800.0),
    ),
    (
        900,
        (
            'IVN', {'Ivanov': 650.0, 'Petrov': 500.0},
        ),
        (575.0, 650.0, 575.0),
    ),
    (
        1200,
        (
            'PVN', {'Ivanov': 450.0, 'Pupkin': 450.0, 'Petrov': 600.0},
        ),
        (500.0, 600.0, 450.0),
    ),
    (None, (), (0, 0, 0)),
)


@pytest.mark.parametrize('limit, args, expected', COMPANS)
def test_statistic_salary_vp(limit: int, args: tuple, expected: tuple) -> None:
    """Test function for salary.

    Args:
        limit: the numerical limit above which wages cannot be,
        args: positional arguments,
        expected: expected result of a degree function.
    """
    assert statistic_salary(args, limit=limit) == expected
