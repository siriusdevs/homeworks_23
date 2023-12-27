"""Modul for testing."""

import pytest
from hw_1 import get_salaries

TEST_DATA_WITH_NONE = (
    (
        (
            ('Finance department', {'Gary': 52000.0, 'Mary': 53000.0, 'John': 60000.0}),
            ('Marketing department', {'Tom': 44000.0, 'Sam': 43000.0, 'Sarah': 50000.0}),
            ('Sales department', {'Biba': 44000.0, 'Boba': 43000.0, 'Vlad': 50000.0}),
        ),
        (
            [60000.0, 53000.0, 52000.0], 0.38,
        ),
    ),
    (
        (
            ('Finance department', {'Gary': 52450, 'Mary': 53340, 'John': 23500}),
            ('Marketing department', {'Tom': 43400, 'Sam': 45670, 'Sarah': 67000}),
            ('Sales department', {'Biba': 44547, 'Boba': 43452, 'Vlad': 50670}),
        ),
        (
            [67000, 53340, 52450], 0.41,
        ),
    ),
)

TEST_DATA_WITHOUT_NONE = (
    (
        (
            ('Finance department', {'Gary': 52000.0, 'Mary': 53000.0, 'John': 60000.0}),
            ('Marketing department', {'Tom': 44000.0, 'Sam': 43000.0, 'Sarah': 50000.0}),
            ('Sales department', {'Biba': 44000.0, 'Boba': 43000.0, 'Vlad': 50000.0}),
        ),
        (
                'Finance department'
        ),
        (
            [50000.0, 50000.0, 44000.0], 0.53,
        ),
    ),
    (
        (
            ('Finance department', {'Gary': 52450, 'Mary': 53340, 'John': 23500}),
            ('Marketing department', {'Tom': 43400, 'Sam': 45670, 'Sarah': 67000}),
            ('Sales department', {'Biba': 44547, 'Boba': 43452, 'Vlad': 50670}),
        ),
        (
            'Finance department', 'Marketing department'
        ),
        (
            [50670, 44547, 43452], 1.0,
        ),
    ),
)


@pytest.mark.parametrize('source, expected', TEST_DATA_WITH_NONE)
def test_with_none(source: tuple[tuple[str, dict[str]]], expected: tuple[list, float]):
    """Test data with dept_exp = None.

    Args:
        source (tuple[tuple[str, dict[str]]]): data for testing.
        expected (tuple[list, float]): expected values.
    """
    assert get_salaries(*source) == expected


@pytest.mark.parametrize('source, dept_exept, expected', TEST_DATA_WITHOUT_NONE)
def test_without_none(
    source: tuple[tuple[str, dict[str]]],
    dept_exept: list[str],
    expected: tuple[list, float]
):
    """Test data have some velues in dept_exp.

    Args:
        source (tuple[tuple[str, dict[str]]]): data for testing.
        dept_exept (list[str]): exception for department data.
        expected (tuple[list, float]): expected values.
    """
    assert get_salaries(*source, dept_exp=dept_exept) == expected
