"""Test module main."""


from typing import Dict

import pytest

from hw1 import salary_stats

the_company = (
    (([5000.1, 1029.5, 120.12], 99.98),
     {
        'Deka': {
            'Freddie': 5000.1,
            'Marko': 1,
            'Fedia': 0,
        },
        'Caregivers': {
            'Me': 120.12355,
            'Notme': 1029.5,
        },
    },
        None,
    ),
    (([1029.5, 228.13, 120.12], 99.93),
     {
        'Dev-ops': {
            'Freddie': 5000.1,
            'Foxy': 1,
            'Bonny': 0,
        },
        'Programmers': {
            'Purple Guy': 120.12355,
            'Kid': 1029.5,
        },
        'Leads': {
            'Chika': 228.1337,
            'Golden Freddie': 1337.228,
        },
    },
        1050,
    ),
    ("That's a strange company. It does not pay it's workers or they have none of them.",
     {},
     None,
     ),
    ("That's a strange company. It does not pay it's workers or they have none of them.",
     {
         'Shady department 1': {
             'Anon 1': 0,
             'Anon 2': 0,
             'Anon 3': 0,
         },
         'Shady department 3': {
             'Blank': 0,
             'None': 0,
         },
     },
     None,
     ),
)


@pytest.mark.parametrize('expected, company, ceiling', the_company)
def test_salary_stats(
    expected: tuple[list, float] | str,
    company: Dict[str, Dict[str, float]],
    ceiling: float,
) -> None:
    """
    Test salary stats function.

    Args:
        expected: tuple[list, float] - the expected parameter
        company: Dict - the dict parameter
        ceiling: float - the ceiling parameter

    Asserts:
        True if the answer is correct
    """
    assert expected == salary_stats(company, ceiling)
