"""Test module for salary function of the company."""

from typing import Tuple, Type

import pytest

from hw1 import company_stats

CORRECT_DATA = (
    (
        (
            ('AI', {'Voronov': 50000.0, 'Alexander': 60000.0}),
            ('IT', {'Palochkin': 70000.0, 'Loginov': 80000.0, 'Yolkin': 82000.0}),
            ('HR', {'Shubin': 90000.0, 'MAXim': 100000.0}),
        ),
        (76000.0, 100000.0, 80000.0),
    ),
    (
        (
            ('Sales', {'Gustav': 1.0, 'Gusev': 2.0, 'Gusin': 3.0}),
            ('Marketing', {'Guskov': 4.0, 'Guslyakov': 5.0, 'Gusarov': 6.0}),
            ('Finance', {'Goose_(Duck)': 7.0, 'Goose': 8.0}),
        ),
        (4.5, 8.0, 4.5),
    ),
)

DATA_WITH_OPTIONAL = (
    (
        (
            ('THE_BEST_DEPARTMENT_OF_THE_COMPANY', {'TOTALY_TRUE_PROGRAMMER': 99.9}),
            ('Security', {'Kirov': 1000.0, 'Vladimir': 2000.0, 'Kenny': 500.0}),
            ('Quality', {'Maslov': 3000.0, 'Sytnikov': 4000.0, 'Usov': 3500.0}),
        ),
        ('Security', 'Quality'),
        (2333.33, 4000.0, 2500.0),
    ),
    (
        (
            ('Dogs', {'Bobik': 10.0, 'Deima': 30.0, 'Patrick': 50.0}),
            ('Cats', {'Felix': 20.0, 'Mosya': 40.0, 'Gosha': 60.0}),
        ),
        ('Cats'),
        (40.0, 60.0, 40.0),
    ),
)


ERROR_DATA = (
    (
        (
            ('Gamers', {'Pikulev': 0, 'Matuhin': -1000.0}),
        ),
        ValueError,
        'The salary should not be or less than zero.',
    ),
    (
        (
            ('Expelled.', {})
        ),
        ValueError,
        'The salary should not be empty',
    ),
)


@pytest.mark.parametrize('departments, expected', CORRECT_DATA)
def test_calculations(departments: Tuple, expected: Tuple[float]) -> None:
    """Checking salary calculations from departments.

    Args:
        departments: departments of the company.
        expected: expected correct result of the function.
    """
    assert company_stats(*departments) == expected


@pytest.mark.parametrize('departments, selected, expected', DATA_WITH_OPTIONAL)
def test_optional(departments: Tuple, selected: Tuple[str], expected: Tuple[float]) -> None:
    """Checking salary calculations from departments with optional argument.

    Args:
        departments: departments of the company.
        selected: вepartments to be included in the calculation.
        expected: expected correct result of the function.
    """
    assert company_stats(*departments, selected=selected) == expected


@pytest.mark.parametrize('departments, error_type, text', ERROR_DATA)
def test_errors(departments: Tuple, error_type: Type[Exception], text: str) -> None:
    """Checking raise exception with error ValueError.

    Args:
        departments: departments of the company.
        error_type: type of error.
        text: message from error.
    """
    with pytest.raises(error_type) as exception:
        company_stats(*departments)

        exception_text = exception.value.args[0]
        assert text == exception_text
