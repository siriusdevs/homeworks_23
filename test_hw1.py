"""Test module for function salary_stats from hw1.py."""

import pytest

from hw1 import salary_stats

TEST_SALARIES = (
    (
        None,
        {
            'Отдел1': {'Сотрудник1': 1000, 'Сотрудник2': 2000, 'Сотрудник3': 3000},
            'Отдел2': {'Сотрудник4': 4000, 'Сотрудник5': 5000, 'Сотрудник6': 6000},
            'Отдел3': {'Сотрудник7': 7000, 'Сотрудник8': 8000, 'Сотрудник9': 9000},
        },
        ([1000, 2000, 3000], '13.33%'),
    ),
    (
        7000,
        {
            'Отдел6': {'Bob': 1000, 'Lil Pump': 2000, 'Ivan': 3000},
            'Отдел7': {'John': 4000, 'Emily': 5000, 'Сотрудник6': 6000},
            'Отдел8': {'Peter': 7000, 'Сотрудник8': 8000, 'Сотрудник9': 9000},
        },
        ([1000, 2000, 3000], '21.43%'),
    ),
    (
        None,
        {
            'Отдел9': {'Сотрудник13': 6500, 'Сотр4удник2': 4110, 'Сотрудник30': 3500},
            'Отдел10': {'Сотрудник445': 54000, 'Со1трудник5': 30000, 'Сотрудник62': 76000},
            'Отдел11': {'Сотрудник71': 107000, 'Сотрудник8': 8500, 'Сотрудник91': 92000},
        },
        ([3500, 4110, 6500], '3.7%'),
    ),
    (
        80000,
        {
            'Отдел12': {'Сотрудник12': 65000, 'Сотрудник24': 4110, 'Сотрудник13': 35000},
            'Отдел13': {'Сотрудник41': 54000, 'Сотрудник51': 30000, 'Сотрудник46': 76000},
            'Отдел14': {'Сотрудник73': 107000, 'Сотрудник83': 8500, 'Сотрудник59': 92000},
        },
        ([4110, 8500, 30000], '15.63%'),
    ),
    (
        1,
        {
            'Отдел1': {'Сотрудник1': 1000},
            'Отдел2': {'Сотрудник4': 4000},
        },
        ([], '100%'),
    ),
)


@pytest.mark.parametrize('limit, departments, expected', TEST_SALARIES)
def test_salary_stats(limit: int | None, departments: dict, expected: tuple[str]) -> None:
    """Created function that tests salary_stats function.

    Args:
        limit (int): the maximum salary value to be considered.
        departments (dict): dict of the keyword arguments where the keys \
            are the names of the departments and the values \
            are the dicts of the employees where the keys \
            are the names of the employees and values are their salaries.
        expected (tuple): expected value from function.
    """
    assert tuple(salary_stats(limit, **departments)) == expected
