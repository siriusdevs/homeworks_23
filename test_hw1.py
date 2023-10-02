
import pytest

from hw1 import calculate_salary_stats

vk_department = {
    "Alice": 50000.0,
    "Bob": 55000.0,
    "Carol": 438000.0,
    "David": 60000.0,
    "Misha": 100000.0,
    "Senya": 30000.0
}

sales_department = {
    "Eve": 62000.0,
    "Frank": 53000.0,
    "Grace": 58000.0,
    "Grisha": 1000.0
}

result_sales_departament = {'sales_departament': ([62000.0, 58000.0, 53000.0], 99.43)}
result_sales_departament_with_limit = {'vk_departament': ([438000.0, 100000.0, 60000.0], 91.58)}

result_sales_with_two_companies = {
    'sales_departament': ([62000.0, 58000.0, 53000.0], 99.43),
    'vk_departament': ([438000.0, 100000.0, 60000.0], 81.58)
}

data_sales = [({'sales_departament': sales_department}, result_sales_departament)]
data_vk = [({'vk_departament': vk_department}, result_sales_departament_with_limit)]

sales_vk_department_value = {
    'sales_departament': sales_department,
    'vk_departament': vk_department
}

data_two_companies = [(sales_vk_department_value, result_sales_with_two_companies)]


@pytest.mark.parametrize("kwargs, expected", data_sales)
def test_calculate_salary_stats_with_one_company(kwargs, expected):
    assert calculate_salary_stats(**kwargs) == expected


@pytest.mark.parametrize("kwargs, expected", data_two_companies)
def test_calculate_salary_two_companies(kwargs, expected):
    assert calculate_salary_stats(**kwargs) == expected


@pytest.mark.parametrize("kwargs, expected", data_vk)
def test_calculate_salary_stats_with_limit(kwargs, expected):
    assert calculate_salary_stats(salary_limit=50000.0, **kwargs) == expected
