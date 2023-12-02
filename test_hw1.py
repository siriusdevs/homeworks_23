"""This module include test for function."""

from typing import Optional

import pytest

from hw1 import statistic_salary

compans = (
    (
        1000,
        (
            (('TVD', {'Ivanov': 800.0}),)
        ),
        (800.0, 800.0, 800.0),
    ),
    (
        900,
        (
            (('IVN', {'Ivanov': 650.0, 'Petrov': 500.0}),)
        ),
        (575.0, 650.0, 575.0),
    ),
    (
        1200,
        (
            (('PVN', {'Ivanov': 450.0, 'Pupkin': 450.0, 'Petrov': 600.0}),)
        ),
        (500.0, 600.0, 450.0),
    ),
    (None, (), (0, 0, 0)),
)


@pytest.mark.parametrize('limit, departments, expected', compans)
def test_statistic_salary_vp(limit: Optional[int], departments: tuple, expected: tuple) -> None:
    """Test function for salary.

    Args:
        limit: the numerical limit above which wages cannot be,
        departments: positional arguments,
        expected: expected result of a degree function.
    """
    assert statistic_salary(*departments, limit=limit) == expected
