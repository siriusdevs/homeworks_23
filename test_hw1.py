"""Tests for HW1."""
from typing import Type

import pytest

from hw1 import statistics

TEST_DATA = (
    (
        (
            ('Отдел All', [1, 2, 3]),
            ('Отдел Bob', [4, 5, 6]),
            ('Отдел Citrus', [7, 8, 9, 10]),
        ),
        (5.5, 10, 5.5),
    ),
    (
        (
            ('Отдел Qwerty', [1, 2, 3]),
            ('Отдел Help', [4, 5, 6]),
            ('Отдел Cats', [7, 8, 9]),
        ),
        (5, 9, 5),
    ),
)

TEST_DATA_WITH_NAMES = (
    (
        (
            ('Отдел Owner', [3, 6, 7]),
            ('Отдел Enter', [3, 5, 6, 7]),
            ('Отдел Arlekino', [4, 9, 8]),
        ),
        ('Отдел Arlekino', 'Отдел Enter'),
        (6.0, 9, 6),
    ),
    (
        (
            ('Отдел Sigma', [3, 6, 7]),
            ('Отдел Delta', [3, 5, 6, 7]),
            ('Отдел Alpha', [4, 9, 8, 10]),
        ),
        ('Отдел Alpha', 'Отдел Delta'),
        (6.5, 10, 6.5),
    ),
    (
        (
            ('Отдел Animal', [0, 6, 7]),
            ('Отдел Dogs', [4, 3, 2, 8]),
            ('Отдел Head', [2, 9, 5]),
        ),
        ('Отдел Animal', 'Отдел Head'),
        (4.83, 9, 5.5),
    ),
)

TEST_ERRORS = (
    (
        (
            ('Отдел All', [0, 0, 0]),
            ('Отдел Bob', [0, 0, 0]),
            ('Отдел Citrus', [0, 0, 0, 0]),
        ),
        ValueError,
        'Salaries should not be 0',
    ),
    (
        (
            ('Отдел All', []),
            ('Отдел Bob', []),
            ('Отдел Citrus', []),
        ),
        ValueError,
        'You entered an empty salary',
    ),
)


@pytest.mark.parametrize('salaries, expected', TEST_DATA)
def test_salaries(salaries: tuple, expected: tuple) -> None:
    """Test function statistics: average, maximum and median salary of employees.

    Args:
        salaries: all salaries
        expected: value for current test
    """
    assert statistics(*salaries) == expected


@pytest.mark.parametrize('salaries, names, expected', TEST_DATA_WITH_NAMES)
def test_salaries_with_names(salaries: tuple, names: tuple, expected: tuple) -> None:
    """Test function with names of departments that need to be included in the statistics.

    Args:
        salaries: all salaries
        names: departments that need to be included in the statistics
        expected: value for current test
    """
    assert statistics(*salaries, department_names=names) == expected


@pytest.mark.parametrize('salaries, error_type, error_text', TEST_ERRORS)
def test_errors(salaries: tuple, error_type: Type[Exception], error_text: str) -> None:
    """Test errors that may occur during program execution.

    Args:
        salaries: all salaries
        error_type: type of error
        error_text: message about error
    """
    with pytest.raises(error_type) as exception:
        statistics(*salaries)

        exception_text = exception.value.args[0]
        assert error_text == exception_text
