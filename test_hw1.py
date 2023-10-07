"""Test hw1."""

import pytest

from hw1 import get_salaries

test_data = (
    (
        (
            ('1', {'Smith': 200.0, 'Guy': 300.0}),
            ('2', {'Ahmed': 300.0, 'Zyrick': 400.0}),
            ('3', {'Ravshan': 100.0, 'Maga': 600.0}),
        ),
        None,
        (
            [600.0, 400.0, 300.0],
            68.42,
        ),
    ),

    (
        (
            ('1st', {'Smith': 5.0, 'Robbinson': 10.0}),
            ('2nd', {'White': 8.0, 'Jefferson': 6.0}),
            ('3rd', {'Bale': 4.0, 'Gosling': 6.0}),
        ),
        None,
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
        None,
        (
            [9.0, 4.0, 3.0],
            72.73,
        ),
    ),

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
            ('1st', {'Smith': 5.0, 'Robbinson': 10.0}),
            ('2nd', {'White': 8.0, 'Jefferson': 6.0}),
            ('3rd', {'Bale': 7.0, 'Gosling': 15.0}),
            ('4th', {'Kant': 4.0, 'Dude': 11.0}),
            ('5th', {'Black': 1.0, 'Malek': 3.0}),
        ),
        (
            '3rd', '4th',
        ),
        (
            [10.0, 8.0, 6.0],
            72.73,
        ),
    ),
)


@pytest.mark.parametrize('source, dept_except, expected', test_data)
def test_get_salaries(source: tuple[tuple], dept_except: tuple[str], expected: tuple[list, float]):
    """Testing...

    Args:
        source (Tuple[tuple]): data for testing
        dept_except (Tuple[str]): exception for department data
        expected (Tuple[list, float]): expected values

    """
    assert get_salaries(*source, dept_except=dept_except) == expected
