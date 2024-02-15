"""Тесты для HW1."""

import pytest

from hw1 import salary_stats

AVERAGE_KEY = 'average'
MAXIMUM_KEY = 'maximum'
MEDIAN_KEY = 'median'


DEP_SALES = 'Sales'
DEP_HR = 'HR'


@pytest.mark.parametrize('departments, limit, expected', [
    ({}, None, {AVERAGE_KEY: None, MAXIMUM_KEY: None, MEDIAN_KEY: None}),
    (
        {DEP_SALES: {}, DEP_HR: {}},
        None,
        {AVERAGE_KEY: None, MAXIMUM_KEY: None, MEDIAN_KEY: None},
    ),
    (
        {DEP_SALES: {'Artem': 2000.0, 'Egor': 3000.0}, DEP_HR: {'Dima': 1500.0, 'Sonya': 1800.0}},
        5000.0,
        {AVERAGE_KEY: None, MAXIMUM_KEY: None, MEDIAN_KEY: None},
    ),
    (
        {DEP_SALES: {'Artem': 5000.0, 'Egor': 5000.0}, DEP_HR: {'Dima': 5000.0, 'Sonya': 5000.0}},
        None,
        {AVERAGE_KEY: 5000.0, MAXIMUM_KEY: 5000.0, MEDIAN_KEY: 5000.0},
    ),
    (
        {DEP_SALES: {'Artem': 6000.0, 'Egor': 7000.0}, DEP_HR: {'Dima': 8000.0, 'Sonya': 9000.0}},
        5000.0,
        {AVERAGE_KEY: 7500.0, MAXIMUM_KEY: 9000.0, MEDIAN_KEY: 7500.0},
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
