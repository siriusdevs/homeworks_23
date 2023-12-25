"""Testing module hw1.py."""
import pytest

from hw1 import calculate_salary_stats

DEPARTMENTS = (
    (
        {
            'Реклама': {'Дмитрий': 110000, 'Яна': 90000},
            'Дизайн': {'Маргарита': 70000, 'Алиса': 80000},
            'IT': {'Егор': 120000, 'Александр': 150000},
        },
        (
            ['Дизайн', 'Реклама', 'IT'],
            ['IT', 'Реклама', 'Дизайн'],
        ),
    ),
    (
        {
            'Радио': {'Максим': 1234.486, 'Алекс': 35345.232},
            'Телевизоры': {'Алексей': 5489.8968, 'Мария': 6590.4},
            'Миксеры': {'Дарья': 58894.059, 'Павел': 82584},
            'Ложки': {'Фернандо': 45753673.983},
        },
        (
            ['Телевизоры', 'Радио', 'Миксеры'],
            ['Ложки', 'Миксеры', 'Радио'],
        ),
    ),
)

NO_SALARY_DEPARTMENTS = (
    (
        {
            'Реклама': {'Дмитрий': 0, 'Яна': 0},
            'Дизайн': {'Маргарита': 0, 'Алиса': 0},
            'IT': {'Егор': 0, 'Александр': 0},
        },
        (
            ['Реклама', 'Дизайн', 'IT'],
            ['IT', 'Дизайн', 'Реклама'],
        ),
    ),
    (
        {
            'Продукты': {'Дмитрий': 0, 'Яна': 0},
            'Телефоны': {'Маргарита': 0, 'Алиса': 0},
            'IT': {'Егор': 0, 'Александр': 0},
        },
        (
            ['Продукты', 'Телефоны', 'IT'],
            ['IT', 'Телефоны', 'Продукты'],
        ),
    ),
)


@pytest.mark.parametrize('departments, expected', DEPARTMENTS)
def test_calculate_statistics(departments: dict, expected: tuple[list, list]):
    """Test case for the function with departments having salaries.

    Args:
        departments: containing names of departments and their respective employees' salaries.
        expected: expected result of fucntion.
    """
    assert calculate_salary_stats(**departments) == expected


@pytest.mark.parametrize('departments, expected', NO_SALARY_DEPARTMENTS)
def test_no_salary(departments: dict, expected: tuple[list, list]):
    """Test case for the function with departments having no salaries.

    Args:
        departments: containing names of departments and their respective employees' salaries.
        expected: expected result of fucntion.
    """
    assert calculate_salary_stats(**departments) == expected
