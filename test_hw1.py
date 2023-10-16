"""Test for hw1."""


import pytest

from hw1 import calculate_salary

VK = 'vk'
TINKOFF = 'tinkoff'

vk_departament = {
    'Misha': 200000,
    'Andrey': 100000,
    'Denis': 50000,
}

tinkoff_departament = {
    'Igor': 80000,
    'Sasha': 50000,
    'Egor': 70000,
}

top_salaries = [200000, 100000, 80000]

vk_and_tinkoff_departament = {VK: vk_departament, TINKOFF: tinkoff_departament}

data_sales = [(vk_and_tinkoff_departament, (top_salaries, 69.09))]
data_sales_with_limit = [(60000, vk_and_tinkoff_departament, (top_salaries, 84.44))]


@pytest.mark.parametrize('departaments, expected', data_sales)
def test_calculate_salary_without_limit(departaments, expected):
    """Test calculate salary with one company.

    Args:
         departaments: the function expects arg name - departament name, value - employees
         expected: the correct answer

    """
    assert calculate_salary(**departaments) == expected


@pytest.mark.parametrize('salary_limit, departaments, expected', data_sales_with_limit)
def test_calculate_salary_with_limit(salary_limit, departaments, expected):
    """Test calculate salary with one company.

    Args:
         salary_limit: limit below which salary is not taken into account
         departaments: the function expects arg name - departament name, value - employees
         expected: the correct answer

    """
    assert calculate_salary(salary_limit=salary_limit, **departaments) == expected
