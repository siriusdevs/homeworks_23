"""Unit tests for modul hw1."""

from types import MappingProxyType

import pytest

from hw1 import get_best_salaries

DEPT1 = MappingProxyType({'a': 1, 'b': 2, 'c': 3})
DEPT2 = MappingProxyType({'d': 4, 'e': 5, 'f': 6})
DEPT3 = MappingProxyType({'g': 7, 'h': 8, 'i': 9})

TEST_DICT = MappingProxyType({'dept1': DEPT1, 'dept2': DEPT2, 'dept3': DEPT3})
TEST_DATA = (
    (
        ('dept1',),
        ([9, 8, 7], 61.54),
        TEST_DICT,
    ),
    (
        ('dept3', 'dept2'),
        ([3, 2, 1], 100.0),
        TEST_DICT,
    ),
    (
        (None, ),
        ([9, 8, 7], 53.33),
        TEST_DICT,
    ),
    (
        ('dept1', 'dept2', 'dept3'),
        ([], 0),
        TEST_DICT,
    ),
)


@pytest.mark.parametrize('ignored_depts, expected, dept_employees', TEST_DATA)
def test_colculating_best_salaries(ignored_depts: tuple, expected: tuple, dept_employees) -> None:
    """Test get_best_salaries function.

    Args:
        ignored_depts (tuple): depts ignored when calculating statistics.
        dept_employees: the key is the name of the department, the value is a dictionary.
        expected (tuple): test value.
    """
    assert get_best_salaries(ignored_depts, **dept_employees) == expected
