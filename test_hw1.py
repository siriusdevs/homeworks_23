"""Testing for module "top_salaries", homework 1."""
import pytest

from hw1 import top_salary

TEST_BASIC = (
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
        5900, ([5500.0, 5200.0, 5000.0], 45.64),
    ),
    (
        {
            'IT2': {'John': 5000.0, 'Alice': 6000.0},
            'HR': {'Krut': 4000.0, 'Brat': 4500.0, 'Beda': 4200.0},
            'Jurnal': {'Lord': 5500.0, 'Sena': 5200.0},
        },
        12, ([], 0.),
    ),
)


@pytest.mark.parametrize('departments, limit_salary, expected', TEST_BASIC)
def test_top_salaries_basic(departments, limit_salary, expected):
    """Test function for `top_salary` to validate basic functionality.

    Args:
        departments: A dictionary representing departments and their workers.
        limit_salary: The salary limit.
        expected: The expected output.
    """
    assert top_salary(limit_salary, **departments) == expected


TEST_ERRORS = (
    (
        {
            'IT3': 'test',
            'HR2': {'BobMArk': 4000.0, 'Mark': 4500.0, 'KAtya': 4200.0},
            'Sales2': {'Juse': 5500.0, 'Pasito': 5200.0},
        },
        None, TypeError,
    ),
    (
        {},
        None, ValueError,
    ),
    (
        {
            12: {'Jame': 4500.0, 'Lisa': 300.0},
            'HR3': {'HQD': 1234.0, 'Mega': 523.0, 'Green': 100.0},
            'Sales3': {'Glad': 550.0, 'Golang': 12.0},
        },
        None, TypeError,
    ),
    (
        {
            'IT4': {12: 4500.0, 'Vlad': 300.0},
            'HR4': {'Marly': 1234.0, 'Dollar': 523.0, 'Moriarty': 100.0},
            'Sales4': {'Anna': 550.0, 'Huil': 12.0},
        },
        None, TypeError,
    ),
    (
        {
            'IT5': {'Jame': 1200, 'Kum': 300.0},
            'HR5': {'Igor': 1234.0, 'Francs': 523.0, 'Kip': 100.0},
            'Sales5': {'Formus': 550.0, 'Gtrw': 12.0},
        },
        None, TypeError,
    ),
    (
        {
            'IT6': {'Jame': 1200, 'Grow': 300.0},
            'HR6': {'James': 'test', 'Lucy': 523.0, 'Kepka': 100.0},
            'Sales6': {'Jol': 550.0, 'Iosrt': 12.0},
        },
        None, TypeError,
    ),
)


@pytest.mark.parametrize('departments, limit_salary, expected', TEST_ERRORS)
def test_top_salaries_errors(departments, limit_salary, expected):
    """Test function for `top_salary` to validate basic functionality.

    Args:
        departments: A dictionary representing departments and their workers.
        limit_salary: The salary limit.
        expected: The expected output.
    """
    with pytest.raises(expected):
        top_salary(limit_salary, **departments)
