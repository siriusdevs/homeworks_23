"""Тесты для HW1."""

import pytest

from hw1 import salary_stats

AVERAGE_KEY = 'average'
MAXIMUM_KEY = 'maximum'
MEDIAN_KEY = 'median'


@pytest.mark.parametrize('departments, limit, expected', [
    ({}, None, {AVERAGE_KEY: None, MAXIMUM_KEY: None, MEDIAN_KEY: None}),
    (
        {'Sales': {}, 'HR': {}},
        None,
        {AVERAGE_KEY: None, MAXIMUM_KEY: None, MEDIAN_KEY: None},
    ),
    (
        {'Sales': {'John': 2000.0, 'Jane': 3000.0}, 'HR': {'Bob': 1500.0, 'Alice': 1800.0}},
        5000.0,
        {AVERAGE_KEY: None, MAXIMUM_KEY: None, MEDIAN_KEY: None},
    ),
    (
        {'Sales': {'John': 5000.0, 'Jane': 5000.0}, 'HR': {'Bob': 5000.0, 'Alice': 5000.0}},
        None,
        {AVERAGE_KEY: 5000.0, MAXIMUM_KEY: 5000.0, MEDIAN_KEY: 5000.0},
    ),
])
def test_salary_stats(departments, limit, expected):
    """
    Тест функции salary_stats.

    Args:
        departments (dict): Словарь, содержащий информацию о зарплатах для каждого отдела.
        limit (float): Предел для максимальной зарплаты.
        expected (dict): Словарь,с ожидаемыми значения для средней,максимальной,медианной зарплат.
    """
    stats = salary_stats(departments, limit)
    assert stats == expected
