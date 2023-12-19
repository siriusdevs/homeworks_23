"""Test module for function top_salary from hw1.py."""

import pytest
from hw1 import top_salary

RIGHT_DATA = (
    (
        ([], None), ([], 0),
    ),
    (
        (
            [('Teachers', [5000.00, 5500.50, 6000.75])],
            None,
        ),
        (
            [6000.75, 5500.5, 5000.0],
            100.0,
        ),
    ),
    (
        (
            [
                ('Church', [5000.00, 5500.50, 6000.75]),
                ('Deanery', [7000.25, 7200.30, 7500.50]),
                ('IT', [6000.00, 6200.00, 6500.00]),
            ],
            None,
        ),
        (
            [7500.5, 7200.3, 7000.25],
            38.14,
        ),
    ),
    (
        (
            [
                ('Teachers', [5000.00, 5500.50, 6000.75]),
                ('Boss', [7000.25]),
                ('Indian Developers', [6000.00000001, 6200.00, 6500.00]),
            ],
            None,
        ),
        (
            [7000.25, 6500.0, 6200.0],
            46.68,
        ),
    ),
)

WRONG_DATA = (
    (
        ([], None), ([], 0),
    ),
    (
        (
            [('Teachers', [0, 0, 0])],
            None,
        ),
        (
            [], 0,
        ),
    ),
)


@pytest.mark.parametrize('company, expected', RIGHT_DATA)
def test_right_data(company, expected):
    """Test the top_salary function with correct data.

    Args:
        company: A list of tuples, where each tuple contains the name of a company
            and a list of salaries.
        expected: A tuple containing the expected top salary and the expected
            average salary.
    """
    salary_result = top_salary(*company[0])
    assert salary_result[0] == expected[0]
    assert salary_result[1] == expected[1]


@pytest.mark.parametrize('company, expected', WRONG_DATA)
def test_wrong_data(company, expected):
    """Test the top_salary function with incorrect data.

    Args:
        company: A list of tuples, where each tuple contains the name of a company
            and a list of salaries.
        expected: A tuple containing the expected top salary and the expected
            average salary.
    """
    salary_result = top_salary(*company[0])
    assert salary_result[0] == expected[0]
    assert salary_result[1] == expected[1]
