"""Module test for hw1."""


import pytest

from hw1 import salary_departments

all_departments = {
    'financy_department': {
        'Alex': 77000.9,
        'Victoria': 34000.2,
        'Platon': 45000.87,
        'Oleg': 68000.89,
        'Irina': 72000.74,
    },
    'hr_department': {
        'Svetlana': 46529.8,
        'Fiona': 47890.76,
        'Eleonora': 60780.5,
        'Efrem': 51000.56,
    },
    'administrative_depatment': {
        'Pavel': 33900.9,
        'Margarita': 54760.9,
        'Evgeny': 33900.9,
    },
    'technical_department': {
        'Alexander': 156000.8,
        'Roman': 136590.7,
    },
}
top_salaries = [156000.8, 136590.7, 77000.9]
top_salaries2 = [77000.9, 72000.74, 68000.89]
test_data = [(all_departments, (top_salaries, 40.0))]
test_data2 = [(all_departments, ('financy_department', 'hr_department'), (top_salaries2, 43.0))]
test_data_invalid = {
    'financy_department': {
    },
    'hr_department': {
    },
    'administrative_depatment': {
    },
    'technical_department': {
    },
}


@pytest.mark.parametrize('department_name, expected', test_data)
def test_salary_departments(department_name: dict[str, float], expected: tuple[list, float]):
    """Function test salary_departments.

    Args:
        department_name (dict[str, float]): test data.
        expected (tuple[list, float]): expected result.
    """
    assert salary_departments(**department_name) == expected


@pytest.mark.xfail(raises=ValueError)
def test_invalid_salary_departments():
    """Test the salary_departments function for errors."""
    salary_departments(test_data_invalid)


@pytest.mark.parametrize('department_name, required_departments, expected', test_data2)
def test_salary_departments_with_req(
    department_name: dict[str, float],
    required_departments: tuple[str],
    expected: tuple[list, float],
):
    """Function test salary_departments with required departments.

    Args:
        department_name (dict[str, float]): test data.
        required_departments (tuple[str]): selected departments.
        expected (tuple[list, float]): expected result.
    """
    assert salary_departments(required_departments, **department_name) == expected
