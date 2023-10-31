"""Test module hw1."""

import pytest

from hw1 import salary_count

TEST_COMPANY_DATA = (
    (
        (
            ('HR', {'Alice': 60000.0, 'Bob': 55000.0, 'Carol': 58000.0}),
            ('Front', {'Egor': 60000.0, 'Roma': 55000.0, 'Car': 58000.0}),
        ),
        ['Front'],
        ([60000.0, 58000.0, 55000.0], 100.0),
    ),
    (
        (
            ('Programmers', {'Alice': 60000.0, 'Bob': 55000.0, 'Carol': 58000.0}),
            ('Back', {'Egor': 60000.0, 'Roma': 55000.0, 'Car': 58000.0}),
        ),
        ['Back'],
        ([60000.0, 58000.0, 55000.0], 100.0),
    ),
    (
        (
            ('Finance', {'David': 62000.0, 'Eve': 59000.0, 'Frank': 63000.0}),
            ('IT', {'Mary': 50001.0, 'Mike': 75000.0, 'Sarah': 55000.0}),
        ),
        ['Finance'],
        ([75000.0, 55000.0, 50001.0], 100.0),
    ),
    (
        (
            ('Finance', {'David': 62000.0, 'Eve': 59000.0, 'Frank': 63000.0}),
            ('IT', {'Anton': 50001.0, 'Mike': 75000.0, 'Sarah': 55000.0}),
            ('HR', {'Alice': 60000.0, 'Bob': 55000.0, 'Carol': 58000.0}),
        ),
        ['IT', 'HR'],
        ([63000.0, 62000.0, 59000.0], 100.0),
    ),
)


@pytest.mark.parametrize('company, excluded_departments, expected', TEST_COMPANY_DATA)
def test_salary_count_with_exclusion(
    company: tuple[str, dict[str, float]],
    excluded_departments: list[str],
    expected: tuple[list[float], float],
) -> None:
    """
    Test salary_count function with excluded_departments.

    Parameters:
        company: tuple[str,dict[str, float]] - the company parameters.
        excluded_departments: list[str] - departments to be excluded.
        expected: tuple[list[float], float] - the expected result.

    Asserts:
        True if the answer is correct.
    """
    total = salary_count(*company, excluded_departments=excluded_departments)
    assert total == expected


TEST_COMPANY_DATA_WITHOUT_EXCLUSION = (
    (
        (
            ('Sirius', {'Artyr': 60000.0, 'Igor': 55000.0, 'Franklin': 58000.0}),
        ),
        ([60000.0, 58000.0, 55000.0], 100.0),
    ),
    (
        (
            ('Math', {'Michael': 40000.0, 'Misha': 59000.0, 'Franklin': 63000.0}),
            ('Phys', {'Mary': 50001.0, 'Mike': 75000.0, 'Sarah': 55000.0}),
        ),
        ([75000.0, 63000.0, 59000.0], 57.6),
    ),
    (
        (
            ('Programmers', {'Aleks': 0, 'Mashka': 0, 'Areg': 0}),
        ),
        ([0, 0, 0], 0),
    ),
    (
        (
            ('Math', {'David': 62000.0, 'Eve': 59000.0, 'Frank': 63000.0}),
            ('Phys', {'Anton': 50001.0, 'Mikely': 75000.0, 'Sarahs': 55000.0}),
            ('Sirius', {'Oleg': 60000.0, 'Dima': 55000.0, 'Carolina': 58000.0}),
        ),
        ([75000.0, 63000.0, 62000.0], 37.24),
    ),
)


@pytest.mark.parametrize('company, expected', TEST_COMPANY_DATA_WITHOUT_EXCLUSION)
def test_salary_count_without_exclusion(
    company: tuple[str, dict[str, float]],
    expected: tuple[list[float], float],
) -> None:
    """
    Test salary_count function without excluded_departments.

    Parameters:
        company: tuple[str,dict[str, float]] - the company parameters.
        expected: tuple[list[float], float] - the expected result.

    Asserts:
        True if the answer is correct.
    """
    total = salary_count(*company, excluded_departments=None)
    assert total == expected
