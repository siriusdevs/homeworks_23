"""Test module main."""


from typing import Dict, List, Tuple

import pytest

from hw_one import salary_stats

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
)


@pytest.mark.parametrize('expected, company, ceiling', the_company)
def test_salary_stats(
    expected: Tuple[List, float],
    company: Dict[str, Dict[str, float]],
    ceiling: float,
) -> None:
    """
    Test salary stats function.

    Args:
        expected: Tuple[List, float] - the expected parameter
        company: Dict - the dict parameter
        ceiling: float - the ceiling parameter

    Asserts:
        True if the answer is correct
    """
    assert expected == salary_stats(company, ceiling)
