"""A module for testing hw1 get_stats function."""

import pytest

from hw1 import get_stats

test_data = [
    ((), None, (0, 0, 0)),
    (
        (
            ('Meat processing plant', {'Zubarev': 1000, 'Sterlyagov': 80}),
            ('Bakery', {'Grigoryan': 60, 'Kardashian': 90}),
        ),
        None,
        (1000, 307.5, 85.0),
    ),
    (
        (
            ('Confectionery', {'Hadid': 100, 'Polovinkin': 80}),
            ('Agrocomplex', {'Bronin': 60, 'Miheeva': 90}),
        ),
        85,
        (100, 95.0, 95.0),
    ),
    (
        (
            ('Safety Department', {'Ivanova': 90, 'Noskov': 70, 'Pushkin': 80}),
            ('Reception', {'Petrova': 60, 'Smirnov': 100, 'Lebedev': 30}),
            ('Accounting', {'Tokareva': 50, 'Novosyolova': 10, 'Lobastov': 20}),
        ),
        20,
        (100, 62.5, 65.0),
    ),
]


@pytest.mark.parametrize('departments, limit, expected', test_data)
def test_get_stats(departments: tuple, limit, expected):
    """Test get_stats function with test_data.

    Args:
        departments: departments with salaries to be passed to get_stats.
        limit: the salary limit below which will not be taken into account.
        expected: an actual expected get_stats result.

    Asserts:
        True if get_stats returns expected answers.
    """
    result_from_get_stats = get_stats(*departments, limit=limit)
    assert result_from_get_stats == expected
