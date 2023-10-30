"""Module for testing hw1.py."""


import pytest

from hw1 import get_departments_rating

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
                'Ноунеймов': 90000,
                'Тестов': 100000,
            },
            'Отдел разработки': {
                'Данилов': 500000,
                'Иноземцев': 500000,
                'Ромоданов': 500000,
                'Татарников': 500000,
                'Тарасов': 500000,
            },
            'Отдел маркетинга и продаж': {
                'Челикович': 150000,
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
                'Ноунеймов': 90000,
                'Тестов': 100000,
            },
            'Отдел разработки': {
                'Данилов': 500000,
                'Иноземцев': 500000,
                'Ромоданов': 500000,
                'Татарников': 500000,
                'Тарасов': 500000,
            },
            'Отдел маркетинга и продаж': {
                'Челикович': 150000,
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
)


@pytest.mark.parametrize('deps, include_deps, expected', test_data)
def test_get_stats(deps: dict, include_deps: tuple | None, expected: tuple):
    """Check the correctness of the calculated statistics.

    Args:
        deps (dict): company departments with employee salaries.
        include_deps (tuple | None): departments included in the statistics, defaults to None.
        expected (tuple): the expected return.
    """
    assert get_departments_rating(deps, include_deps) == expected


invalid_test_data = (
    ({'Отдел разработки': {'Ноунеймов': -50000}}),
)


@pytest.mark.xfail(raises=Exception)
def test_invalid_numbers():
    """Check error handling."""
    get_departments_rating(invalid_test_data)
