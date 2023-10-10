"""Test module hw1."""

import pytest

from hw1 import salary_count

test_company_data = (
    (
        (
            ('HR', {'Alice': 60000.0, 'Bob': 55000.0, 'Carol': 58000.0}),
        ),
        None,
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


@pytest.mark.parametrize('args, excluded_departments, expected', test_company_data)
def test_salary_count(
    args: tuple[str, dict[str, float]],
    excluded_departments: list[str] | None,
    expected: tuple[list[float], float],
) -> None:
    """
    Test salary_count function.

    Parameters:
        args: tuple[str,dict[str, float]] - the args parameters.
        excluded_departments: list[str] | None - departments to be excluded.
        expected: tuple[list[float], float] - the expected result.

    Asserts:
        True if the answer is correct.
    """
    total = salary_count(*args, excluded_departments=excluded_departments)
    assert total == expected
