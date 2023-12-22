"""pytest: a convenient testing framework for Python."""
import pytest

from hw1 import salary

departments1 = (
    (
        (
            'testing department',
            {
                'Ivanov': 1000.45,
                'Trofimov': 20000.78,
                'Tenigin': 300.43,
                'Rindin': 50000.41,
            },
        ),
        (
            (
                [20000.78, 1000.45, 300.43], 29.88,
            )
        ),
        (50000),
    ),

    (
        (
            'testing department',
            {
                'Ivanov': 1000.45,
                'Trofimov': 20000.78,
                'Tenigin': 300.43,
                'Rindin': 50000.41,
            },
        ),
        (
            ([50000.41, 20000.78, 1000.45], 99.58)
        ),
        (None),
    ),

    (
        (
            'testing department',
            {
                'Ivanov': 0,
                'Trofimov': 20000.78,
                'Tenigin': 300.43,
                'Rindin': 0,
            },
        ),
        (
            ([20000.78, 300.43, 0], 100.0)
        ),
        (60000),
    ),
)


@pytest.mark.parametrize('test_departments, expected, maxs', departments1)
def test_hw1(test_departments, expected, maxs):
    """.

    the function is testing another function

    Args:
        test_departments: tuple  - a tuple with departments and salaries
        expected: typle - tuple with answers
        maxs : (int or None) - maximum salary limit.

    Return:
        expected: list - value to function
    """
    assert salary(test_departments, maxs=maxs) == expected
