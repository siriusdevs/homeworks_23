"""Test for hw1."""


import pytest

from hw1 import calculate_salary_stats

VK = 'vk'
TINKOFF = 'tinkoff'

VK_DEPARTAMENT = {
    'Misha': 200000,
    'Andrey': 100000,
    'Denis': 50000,
}

TINKOFF_DEPARTAMENT = {
    'Igor': 80000,
    'Sasha': 50000,
    'Egor': 70000,
}

TOP_SALARIES = [200000, 100000, 80000]

VK_AND_TINKOFF_DEPARTAMENT = {VK: VK_DEPARTAMENT, TINKOFF: TINKOFF_DEPARTAMENT}

data_sales = [(VK_AND_TINKOFF_DEPARTAMENT, (TOP_SALARIES, 69.09))]
data_sales_with_limit = [(50000, VK_AND_TINKOFF_DEPARTAMENT, (TOP_SALARIES, 84.44))]


@pytest.mark.parametrize('kwargs, expected', data_sales)
def test_calculate_salary_without_limit(kwargs, expected):
    """Test calculate salary with one company.

    Args:
         kwargs: the function expects arg name - departament name, value - employees
         expected: the correct answer

    """
    assert calculate_salary_stats(**kwargs) == expected


@pytest.mark.parametrize('salary_limit, kwargs, expected', data_sales_with_limit)
def test_calculate_salary_with_limit(salary_limit, kwargs, expected):
    """Test calculate salary with one company.

    Args:
         salary_limit: limit below which salary is not taken into account
         kwargs: the function expects arg name - departament name, value - employees
         expected: the correct answer

    """
    assert calculate_salary_stats(salary_limit=salary_limit, **kwargs) == expected
