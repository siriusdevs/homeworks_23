"""Modul for testing."""

import pytest

from hw1 import get_salaries

TEST_DATA_WITH_NONE = (
    (
        (
            ('Finance department', {'Gary': 52000.0, 'Mary': 53000.0, 'Johny': 60000.0}),
            ('Marketing department', {'Tom': 44000.0, 'Sam': 43000.0, 'Sarah': 50000.0}),
            ('Sales department', {'Biba': 44000.0, 'Boba': 43000.0, 'Vlad': 50000.0}),
        ),
        (
            [60000.0, 53000.0, 52000.0], 38,
        ),
    ),
    (
        (
            ('Finance department', {'Sonya': 52450.0, 'Mary': 53340.0, 'Vova': 23500.0}),
            ('Marketing department', {'Tom': 43400.0, 'Alexandr': 45670.0, 'Sasha': 67000.0}),
            ('Sales department', {'Biba': 44547.0, 'Boba': 43452.0, 'Dasha': 50670.0}),
        ),
        (
            [67000.0, 53340.0, 52450.0], 41,
        ),
    ),
)

TEST_DATA_WITHOUT_NONE = (
    (
        (
            ('Social department', {'Gary': 52000.0, 'Mary': 53000.0, 'John': 60000.0}),
            ('Gigachad department', {'Angela': 44000.0, 'Sus': 43000.0, 'Sarah': 50000.0}),
            ('Some department', {'Mixail': 44000.0, 'User': 43000.0, 'Vlad': 50000.0}),
        ),
        (
            'Social department',
        ),
        (
            [50000.0, 50000.0, 44000.0], 53,
        ),
    ),
    (
        (
            ('Security department', {'Rin': 52450.0, 'Masha': 53340.0, 'John': 23500.0}),
            ('Another department', {'Tom': 43400.0, 'Sem': 45670.0, 'Liza': 67000.0}),
            ('Sales department', {'Varya': 44547.0, 'Bob': 43452.0, 'Vlad': 50670.0}),
        ),
        (
            'Security department', 'Another department',
        ),
        (
            [50670.0, 44547.0, 43452.0], 100,
        ),
    ),
)


@pytest.mark.parametrize('source, expected', TEST_DATA_WITH_NONE)
def test_with_none(source: tuple[tuple], expected: tuple[list, float]):
    """Test data with dept_exp = None.

    Args:
        source (tuple[tuple]): data for testing.
        expected (tuple[list, float]): expected values.
    """
    assert get_salaries(*source) == expected


@pytest.mark.parametrize('source, dept_exept, expected', TEST_DATA_WITHOUT_NONE)
def test_without_none(
    source: tuple[tuple],
    dept_exept: list[str],
    expected: tuple[list, float],
):
    """Test data have some velues in dept_exp.

    Args:
        source (tuple[tuple]): data for testing.
        dept_exept (list[str]): exception for department data.
        expected (tuple[list, float]): expected values.
    """
    assert get_salaries(*source, dept_exp=dept_exept) == expected
