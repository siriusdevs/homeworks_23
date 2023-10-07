"""Module that tests main.py."""

import pytest

import helpers.get_median
import hw1

DATA_TESTS_GET_MEDIAN = (
    (
        [],
        True,
        0,
    ),
    (
        [1],
        True,
        1.0,
    ),
    (
        [1, 2],
        True,
        1.5,
    ),
    (
        [1, 3, 2],
        False,
        2,
    ),
    (
        (1, 2, 3, 4),
        True,
        2.5,
    ),
    (
        [4, 2, 3, 1],
        True,
        2.5,
    ),
)


@pytest.mark.parametrize('sequence, is_sorted, expected', DATA_TESTS_GET_MEDIAN)
def test_get_median(sequence, is_sorted, expected) -> None:
    """Test function 'get_median' for correct values.

    Args:
        sequence (Sequences[int | float]): Sequence of random int or float value.
        is_sorted (bool): Is given sequence sorted or no? default - False.
        expected (float): Median value.
    """
    assert helpers.get_median.get_median(sequence, is_sorted) == expected


DATA_TESTS_GET_STATS = (
    (
        None,
        {
            'main': {
                'Alex': 100.0,
                'Ivan': 100.0,
                'Danil': 200.0,
                'Kirill': 300.0,
                'Sasha': 300.0,
            },
        },
        (200.0, 300.0, 200.0),
    ),
    (
        None,
        {
            'extra': {
                'Shurik': 100.0,
                'Katya': 200.0,
                'Vasya': 300.0,
                'Igor': 400.0,
            },
            'mega-extra': {
                'Who': 234.0,
                'Slava': 10000.0,
                'Rodic': 1200.0,
            },
        },
        (1776.29, 10000.0, 300.0),
    ),
    (
        250.0,
        {
            'new-department': {
                'Gora': 100.0,
                'Gosha': 200.0,
                'Grigoriy': 300.0,
                'Goyda': 400.0,
            },
        },
        (350.0, 400.0, 350.0),
    ),
    (
        0,
        {
            'Sirius': {},
        },
        (0, 0, 0),
    ),
    (
        1000,
        {
            'old-departments': {
                'Polina': 700,
            },
        },
        (0, 0, 0),
    ),
)


@pytest.mark.parametrize('min_salary, departments, expected', DATA_TESTS_GET_STATS)
def test_get_stats(min_salary, departments, expected) -> None:
    """Test function 'get_stats' for correct values.

    Args:
        min_salary (None | int | float): The lower limit of salaries that we consider.
        departments (dict[str, dict[str, float]]): departments that we consider salaries in.
        expected (tuple[float, float, float]): result calculation of the company.
    """
    assert hw1.get_stats(min_salary, **departments) == expected
