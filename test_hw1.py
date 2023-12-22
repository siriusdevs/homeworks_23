# --encoding: utf-8
"""Test main file."""

import pytest

from hw1 import check_sum_salary

test_argument = [
    (
        (('v', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),),
        9,
        ([8, 7, 6], 23.08),
    ), (
        (('b', [1, 0.1, 3]), ('n', [0, 5, 1.1])),
        None,
        ([5, 3, 1.1], 89.22),
    ), (
        (('z', [1, 0.2, 3]), ('t', [0, 5, 1.2]), ('ba', [10, 11.1, 14.1])),
        None,
        ([14.1, 11.1, 10], 77.19),
    ), (
        (('a', [-1, -2, -3]), ('u', [0, -7, -1.1])),
        None,
        0,
    ),
]


@pytest.mark.parametrize('departments, salary_cap, answer', test_argument)
def test_func(
    departments: tuple[str, list[float]],
    salary_cap: None or float,
    answer: tuple[list[float], float],
        ) -> None:
    """Checks answers.

    Parameters:
        departments: tuple[str, list[float]] - accepts department name and their salaries
        answer: tuple[list[float], float] - top three salaries in company and percentage of salary
        salary_cap: None or float - maximum salary
    """
    assert check_sum_salary(*departments, salary_cap=salary_cap) == answer
