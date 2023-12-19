"""Testing for module "top_salaries", homework 1."""
import pytest

from hw1 import top_salary

TESTS = (
    (
        {
            'DataBase': {'John': 5000.0, 'Alice': 6000.0},
            'HeadHunter': {'Bob': 4000.0, 'Carol': 4500.0, 'David': 4200.0},
            'Sales': {'Emily': 5500.0, 'Frank': 5200.0},
        },
        None, ([6000.0, 5500.0, 5200.0], 48.55),
    ),
    (
        {
            'InformationalTechnology': {'Ivan': 4500.0, 'Lida': 300.0},
            'HeadDrupper': {'Bob': 1234.0, 'Carol': 523.0, 'David': 100.0},
            'Marketing': {'Emily': 550.0, 'Frank': 12.0},
        },
        None, ([4500.0, 1234.0, 550.0], 87.05),
    ),
    (
        {
            'IT': {'Petya': 5000.0, 'Alice': 6000.0},
            'HR': {'Bob': 4000.0, 'Carol': 4500.0, 'David': 4200.0},
            'Depatrment': {'Emily': 5500.0, 'Frank': 5200.0},
        },
        5900, ([5500.0, 5200.0, 5000.0], 55.28),
    ),
    (
        {
            'IT2': {'John': 5000.0, 'Alice': 6000.0},
            'HR': {'Krut': 4000.0, 'Brat': 4500.0, 'Beda': 4200.0},
            'Jurnal': {'Lord': 5500.0, 'Sena': 5200.0},
        },
        12, ([], 0.),
    ),
    (
        {
            'HR2': {'BobMArk': 4000.0, 'Mark': 4500.0, 'KAtya': 4200.0},
            'Sales2': {'Juse': 5500.0, 'Pasito': 5200.0},
        },
        None, ([5500.0, 5200.0, 4500.0], 64.96),
    ),
    (
        {
            'HR2': {'BobMArk': 0, 'Mark': 0, 'KAtya': 0},
            'Sales2': {'Juse': 0, 'Pasito': 0},
        },
        None, ([0, 0, 0], 0),
    ),
)


@pytest.mark.parametrize('departments, limit_salary, expected', TESTS)
def test_top_salaries_basic(departments, limit_salary, expected):
    """Test function for `top_salary` to validate basic functionality.

    Args:
        departments: A dictionary representing departments and their workers.
        limit_salary: The salary limit.
        expected: The expected output.
    """
    assert top_salary(limit_salary, **departments) == expected
