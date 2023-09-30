"""Test module hw1."""


from typing import Dict, Tuple

import pytest

from hw1 import top_three_salaries

test_cases = (
    (
        {
            'rapper': {
                'Marko': 0,
                'Jay-Z': 10,
            },
            'singer': {
                'Freddie Mercury': 1000,
                'Matvey': 500,
            },
            'actor': {
                'Bruce Lee': 10000,
                'Jackie Chan': 50000,
            },
            'politician': {
                'Putin': 12345,
                'Biden': 67890,
            },
            'barbarian': {
                'Hog Rider': 99999,
                'PEKKA': 99999,
            },
        },
        (('rapper', 'singer', 'actor'), ('actor', 'politician', 'barbarian')),
    ), (
        {
            'tech': {
                'Alex': 55,
                'Jason': 1134,
            },
            'CTO': {
                'Azuro': 10000,
                'Cloudapi': 50000,
            },
        },
        (('tech', 'CTO'), ('tech', 'CTO')),
    ), (
        {
            'animatronik': {
                'Freddy': 55,
                'Chika': 1237.112,
            },
            'worker': {
                'Andy': 200,
                'Vlad': 200.2,
            },
            'principal': {
                'Vladimir': 10000.123,
                'Andrew': 50000.54,
                'Kirill': 0,
            },
            'developer': {
                'Jane': 1e9,
                'Iris': 1e7,
            },
            'architector': {
                'Ben': 13,
            },
            'cashier': {
                'Molly': 12312.12,
            },
            'carrier': {
                'Maga': 2279,
            },
            'names': ('animatronik', 'worker', 'principal', 'developer', 'architector', 'cashier'),
        },
        (('architector', 'worker', 'animatronik'), ('cashier', 'principal', 'developer')),
    ),
)


@pytest.mark.parametrize('kwargs, expected', test_cases)
def test_top_three_salaries(
    kwargs: Dict[str, Dict[str, float] | Tuple[str, ...]],
    expected: Tuple[Tuple[str, ...], Tuple[str, ...]],
) -> None:
    """
    Test salary stats function.

    Args:
        kwargs: Dict[str, Dict[str, float] | Tuple[str, ...]] - given data
        expected: Tuple[Tuple[str, ...], Tuple[str, ...]] - the dict parameter

    Asserts:
        True if the answer is correct
    """
    assert top_three_salaries(**kwargs) == expected
