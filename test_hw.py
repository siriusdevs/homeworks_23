# --encoding: utf-8
import pytest
from typing import Tuple, List

from hw1 import check_sum_solary

"""Function for test main file."""

test_argument = [
    ((('a', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),), 9, ([8, 7, 6], 58.33)),
    ((('a', [1, 0.1, 3]), ('b', [0, 5, 1.1])), None, ([5, 3, 1.1], 89.22)),
    ((('a', [1, 0.1, 3]), ('b', [0, 5, 1.1]), ('c', [10, 11.1, 14.1])), None,
     ([14.1, 11.1, 10], 77.53)),
    ((('a', [-1, -2, -3]), ('b', [0, -7, -1.1])), None, 0)
]


@pytest.mark.parametrize('args, salary_cap, answer', test_argument)
def test_func(
        args: Tuple[str, List[float]],
        salary_cap: None or float,
        answer: Tuple[List[float], float]):
    """
    Checks answers.
    Args:
        args: Tuple[str, List[float]] - accepts department name and their salaries
        answer: Tuple[List[float], float] - top three salaries in company and percentage of salary
        salary_cap: None or float - maximum salary
    Returns:
    """
    assert check_sum_solary(*args, salary_cap=salary_cap) == answer
