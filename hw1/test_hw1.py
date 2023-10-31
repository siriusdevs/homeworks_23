"""Module for testing hw1.py."""


import pytest
from typing import Optional

from hw1 import get_departments_rating, check_salary_for_negativity

test_data = (
    ({}, None, ([], [])),
    ({}, (), ([], [])),
    (
        {},
        (
            'Отдел финансов',
            'Отдел разработки',
            'Отдел маркетинга и продаж',
        ),
        ([], []),
    ),
    (
        {
            'Отдел финансов': {
                'Ноунеймов': 90000.,
                'Тестов': 100000.,
            },
            'Отдел разработки': {
                'Данилов': 500000.,
                'Иноземцев': 500000.,
                'Ромоданов': 500000.,
                'Татарников': 500000.,
                'Тарасов': 500000.,
            },
            'Отдел маркетинга и продаж': {
                'Челикович': 150000.,
            },
        },
        None,
        (
            [
                'Отдел разработки',
                'Отдел маркетинга и продаж',
                'Отдел финансов',
            ],
            [
                'Отдел финансов',
                'Отдел маркетинга и продаж',
                'Отдел разработки',
            ],
        ),
    ),
    (
        {
            'Отдел финансов': {
                'Ноунеймов': 90000.,
                'Тестов': 100000.,
            },
            'Отдел разработки': {
                'Данилов': 500000.,
                'Иноземцев': 500000.,
                'Ромоданов': 500000.,
                'Татарников': 500000.,
                'Тарасов': 500000.,
            },
            'Отдел маркетинга и продаж': {
                'Челикович': 150000.,
            },
        },
        (
            'Отдел финансов',
            'Отдел маркетинга и продаж',
        ),
        (
            [
                'Отдел маркетинга и продаж',
                'Отдел финансов',
            ],
            [
                'Отдел финансов',
                'Отдел маркетинга и продаж',
            ],
        ),
    ),
    (
        {
            'Отдел финансов': {
                'Ноунеймов': 90000.,
                'Тестов': 100000.,
            },
            'Отдел разработки': {
                'Данилов': 500000.,
                'Иноземцев': 500000.,
                'Ромоданов': 500000.,
                'Татарников': 500000.,
                'Тарасов': 500000.,
            },
            'Отдел маркетинга и продаж': {
                'Челикович': 150000.,
            },
            'Отдел тестирования': {}
        },
        (
            'Отдел финансов',
            'Отдел маркетинга и продаж',
            'Отдел тестирования'
        ),
        (
            [
                'Отдел маркетинга и продаж',
                'Отдел финансов',
            ],
            [
                'Отдел финансов',
                'Отдел маркетинга и продаж',
            ],
        ),
    ),
)


@pytest.mark.parametrize('departments, include_deps, expected', test_data)
def test_get_stats(departments: dict[str, dict[str, float]], include_deps: Optional[tuple[str]], expected: tuple):
    """Check the correctness of the calculated statistics.

    Args:
        deps (dict): company departments with employee salaries.
        include_deps (tuple | None): departments included in the statistics, defaults to None.
        expected (tuple): the expected return.
    """
    assert get_departments_rating(departments, include_deps) == expected


invalid_test_data = ({'Отдел разработки': {'Ноунеймов': -50000}}, None)



@pytest.mark.xfail(raises=ValueError)
def test_invalid_test_data():
    """Check error handling."""
    get_departments_rating(*invalid_test_data)

# salaries = staff.values()
# lenth = len(salaries)
# lenth = None if lenth == 0 else lenth
# average_salaries[department] = round(sum(salaries) / lenth, 2)

# average_salaries = sorted(average_salaries.values(), key=lambda average_salaries.keys(): average_salaries.keys())

# def sort_salaries(args):
#     pass