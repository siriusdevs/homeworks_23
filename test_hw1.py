"""Unit tests for modul hw1."""

from types import MappingProxyType

import pytest

from hw1 import get_best_salaries

DEPT1 = 'dept1'
DEPT2 = 'dept2'
DEPT3 = 'dept3'

DEPT1_DIR = MappingProxyType({'a': 1, 'b': 2, 'c': 3})
DEPT2_DIR = MappingProxyType({'d': 4, 'e': 5, 'f': 6})
DEPT3_DIR = MappingProxyType({'g': 7, 'h': 8, 'i': 9})

TEST_DICT_THREE_DEPTS = MappingProxyType(
    {
        DEPT1: DEPT1_DIR, DEPT2: DEPT2_DIR, DEPT3: DEPT3_DIR,
    },
)
TEST_DICT_ONE_DEPTS = MappingProxyType({DEPT1: DEPT1_DIR})

TEST_DATA = (
    (
        (DEPT1,),
        ([9, 8, 7], 61.54),
        TEST_DICT_THREE_DEPTS,
    ),
    (
        (DEPT3, DEPT2),
        ([3, 2, 1], 100.0),
        TEST_DICT_THREE_DEPTS,
    ),
    (
        (DEPT1, DEPT2, DEPT3),
        ([], 0),
        TEST_DICT_THREE_DEPTS,
    ),
)

# Test get_better_salaries with default arguments.
TEST_DATA_DEFAULT = (
    (
        ([3, 2, 1], 100.0),
        TEST_DICT_ONE_DEPTS,
    ),
    (
        ([9, 8, 7], 53.33),
        TEST_DICT_THREE_DEPTS,
    ),
)


@pytest.mark.parametrize('ignored_depts, expected, dept_employees', TEST_DATA)
def test_colculating_best_salaries(
    ignored_depts: tuple, expected: tuple, dept_employees: dict[str, dict[str, int]],
) -> None:
    """Test get_best_salaries function.

    Args:
        ignored_depts (tuple): depts ignored when calculating statistics.
        dept_employees: the key is the name of the department, the value is a dictionary.
        expected (tuple): test value.
    """
    assert get_best_salaries(ignored_depts, **dept_employees) == expected


@pytest.mark.parametrize('expected, dept_employees', TEST_DATA_DEFAULT)
def test_calculating_best_salaries_default(
    expected: tuple, dept_employees: dict[str, dict[str, int]],
) -> None:
    """Test get_best_salaries function without ignore_depts argument.

    Args:
        dept_employees: the key is the name of the department, the value is a dictionary.
        expected (tuple): test value.
    """
    assert get_best_salaries(**dept_employees) == expected
