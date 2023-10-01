"""This module include test of function get_statistic."""

import pytest

from hw1 import get_statistic

TEST_GET_DATAS = (
    (
        10000,
        {
            'Sales Departaments': {'Staffer1': 50000.0},
        },
        (0, 0, 0),
    ),
    (
        150000,
        {
            'Dep1': {'Staff1': 50000.0, 'Staff2': 60000.0, 'Staff3': 70000.0},
        },
        (60000.0, 70000.0, 60000.0),
    ),
    (
        120000,
        {
            'Dep1': {'Staff3': 50000.0, 'Staff4': 60000.0, 'Staff5': 70000.0},
            'Dep2': {'Staff6': 80000.0, 'Staff7': 90000.0},
        },
        (70000.0, 90000.0, 70000.0),
    ),
    (
        80000,
        {
            'Dep1': {'Staff1': 50000.0, 'Staff2': 60000.0, 'Staff3': 70000.0},
            'Dep2': {'Staffer4': 80000.0, 'Staff5': 90000.0},
        },
        (65000.0, 80000.0, 65000.0),
    ),
    (
        None,
        {
            'Sales Departaments': {'Staffer1': 50000.0},
        },
        (50000.0, 50000.0, 50000.0),
    ),
)


@pytest.mark.parametrize('limit,departments_data,expected', TEST_GET_DATAS)
def test_get_stat(limit: int, departments_data: dict, expected: tuple) -> None:
    """A function that tests get_statistic function.

    Args:
        limit: A numerical limit above which salaries need not be taken
        departamens_data: dictionary with the names departments as keys,\
            the dictionary with employee names as keys\
            and salaries as values.
        expected: expected function output.
    """
    assert get_statistic(departments_data, limit) == expected
