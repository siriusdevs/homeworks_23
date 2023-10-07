"""Unit tests for modul hw1."""

from typing import Tuple

import pytest

from hw1 import get_best_salaries

dept1 = {'a': 1, 'b': 2, 'c': 3}
dept2 = {'d': 4, 'e': 5, 'f': 6}
dept3 = {'g': 7, 'h': 8, 'i': 9}

test_dict = {'dept1': dept1, 'dept2': dept2, 'dept3': dept3}
test_data = (
    (
        ('dept3',),
        ([('f', 6), ('e', 5), ('d', 4)], 71.43),
        test_dict,
    ),
    (
        ('dept3', 'dept2'),
        ([('c', 3), ('b', 2), ('a', 1)], 100.0),
        test_dict,
    ),
    (
        (None, ),
        ([('i', 9), ('h', 8), ('g', 7)], 53.33),
        test_dict,
    ),
)


@pytest.mark.parametrize('ignored_depts, expected, dept_employees', test_data)
def test_colculating_best_salaries(ignored_depts: Tuple, expected: Tuple, dept_employees) -> None:
    """Test get_best_salaries function.

    Args:
        ignored_depts (Tuple): depts ignored when calculating statistics.
        dept_employees: the key is the name of the department, the value is a dictionary.
        expected (Tuple): test value.
    """
    assert get_best_salaries(ignored_depts, **dept_employees) == expected
