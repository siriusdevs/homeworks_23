"""This is module for testing salary_calculation_statistic function from main module."""

from typing import Optional

import pytest
from main_hw1 import salary_calculation_statistic

compans = (
    (
        100,

        (
            (('KFC', [10, 15, 30, 65, 150, 500, 700])),

        ),

        (30.0, 65.0, 22.0),

    ),

    (
        900,

        (
            (('BurgerKing', [1000, 1655, 300, 965, 1500, 500, 700])),

        ),

        (500.0, 700.0, 500.0),

    ),

    (
        1200,

        (
            (('Yummy and dot))))', [999, 666, 333, 555, 150, 15, 10])),

        ),

        (389.71, 999.0, 333.0),

    ),

    (None, (), (0, 0, 0)),

)


@pytest.mark.parametrize('limit, arguments, expected', compans)
def test_statistic_salary_vp(
    limit: Optional[int],
    arguments: tuple[float],
    expected: tuple[float, float, float]
) -> None:

    """Test function for salary_calculation_statistic function from main module.

    Args:
        limit: the numerical limit above which wages cannot be,
        arguments: positional arguments,
        expected: expected result of a degree function.
    """

    assert salary_calculation_statistic(*arguments, limit=limit) == expected
