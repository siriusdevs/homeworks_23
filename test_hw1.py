"""Test hw1."""

import pytest

from hw1 import get_salaries

test_data_with_none = (
    (
        (
            ('vk', {'Smith': 200.0, 'Guy': 300.0}),
            ('tinkoff', {'Ahmed': 300.0, 'Zyrick': 400.0}),
            ('sber', {'Ravshan': 100.0, 'Maga': 600.0}),
        ),
        (
            [600.0, 400.0, 300.0],
            68.42,
        ),
    ),

    (
        (
            ('vk', {'Smith': 5.0, 'Robbinson': 10.0}),
            ('tinkoff', {'White': 8.0, 'Jefferson': 6.0}),
            ('sber', {'Bale': 4.0, 'Gosling': 6.0}),
        ),
        (
            [10.0, 8.0, 6.0],
            61.54,
        ),
    ),

    (
        (
            ('South', {'Dude': 2.0, 'Den': 3.0}),
            ('West', {'Mate': 4.0, 'Employee': 1.0}),
            ('East', {'Friend': 9.0, 'Guy': 3.0}),
        ),
        (
            [9.0, 4.0, 3.0],
            72.73,
        ),
    ),
)

test_data_without_none = (
    (
        (
            ('South', {'Alex': 2.0, 'Johan': 3.0}),
            ('West', {'Sarah': 4.0, 'Denis': 1.0}),
            ('East', {'Demian': 9.0, 'Folk': 3.0}),
        ),
        (
            'South',
        ),
        (
            [9.0, 4.0, 3.0],
            94.12,
        ),
    ),

    (
        (
            ('Reserve', {'Smith': 5.0, 'Robbinson': 10.0}),
            ('West', {'White': 8.0, 'Jefferson': 6.0}),
            ('North', {'Bale': 7.0, 'Gosling': 15.0}),
            ('Main', {'Kant': 4.0, 'Dude': 11.0}),
            ('Center', {'Black': 1.0, 'Malek': 3.0}),
        ),
        (
            'North', 'Main',
        ),
        (
            [10.0, 8.0, 6.0],
            72.73,
        ),
    ),
)


@pytest.mark.parametrize('source, expected', test_data_with_none)
def test_with_none(source: tuple[tuple], expected: tuple[list, float]):
    """Test data contains None in dept_except.

    Args:
        source (Tuple[tuple]): data for testing
        expected (Tuple[list, float]): expected values

    """
    assert get_salaries(*source) == expected


@pytest.mark.parametrize('source, dept_except, expected', test_data_without_none)
def test_without_none(source: tuple[tuple], dept_except: tuple[str], expected: tuple[list, float]):
    """Test data have some values in dept_except.

    Args:
        source (Tuple[tuple]): data for testing
        dept_except (Tuple[str]): exception for department data
        expected (Tuple[list, float]): expected values

    """
    assert get_salaries(*source, dept_except=dept_except) == expected
