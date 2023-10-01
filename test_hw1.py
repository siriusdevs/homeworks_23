"""Module for testing the main file."""


import pytest

from hw1 import work_statistics

company_departments_test = (
    ({
        'HR Department': {
            'John Smith': 50000,
            'Mary Johnson': 55000,
            'David Brown': 48000,
        },
        'Finance Department': {
            'Emily Davis': 60000,
            'Michael Wilson': 62000,
            'Sarah Lee': 55000,
        },
        'Marketing Department': {
            'Jennifer Clark': 58000,
            'Daniel Martinez': 54000,
            'Linda Hall': 56000,
        },
        'Engineering Department': {
            'Robert Taylor': 70000,
            'Susan Miller': 72000,
            'William White': 68000,
        },
        'Sales Department': {
            'Karen Harris': 30000,
            'Richard Jackson': 58000,
            'Patricia Anderson': 61000,
        },
    },
        (
        'Engineering Department',
        'Sales Department',
    ),
        (
        [48000, 50000, 54000],
        30.52,
    ),
    ),
    ({
        'HR Department': {
            'John Smith': 50000,
            'Mary Johnson': 55000,
            'David Brown': 48000,
        },
        'Finance Department': {
            'Emily Davis': 60000,
            'Michael Wilson': 62000,
            'Sarah Lee': 55000,
        },
        'Marketing Department': {
            'Jennifer Clark': 58000,
            'Daniel Martinez': 54000,
            'Linda Hall': 56000,
        },
        'Engineering Department': {
            'Robert Taylor': 70000,
            'Susan Miller': 72000,
            'William White': 68000,
        },
        'Sales Department': {
            'Karen Harris': 30000,
            'Richard Jackson': 58000,
            'Patricia Anderson': 61000,
        },
    },
        (),
        (
        [30000, 48000, 50000],
        14.94,
    ),
    ),
    ({
        'HR Department': {
            'John Smith': 40000,
            'Mary Johnson': 55000,
            'David Brown': 48000,
        },
        'Finance Department': {
            'Emily Davis': 60000,
            'Michael Wilson': 62000,
            'Sarah Lee': 55000,
        },
        'Marketing Department': {
            'Jennifer Clark': 58000,
            'Daniel Martinez': 54000,
            'Linda Hall': 0,
        },
        'Engineering Department': {
            'Robert Taylor': 1000,
            'Susan Miller': 72000,
            'William White': 68000,
        },
        'Sales Department': {
            'Karen Harris': 30000,
            'Richard Jackson': 58000,
            'Patricia Anderson': 61000,
        },
    },
        (
        'HR Departmen',
        'Sales Department',
    ),
        (
        [0, 1000, 40000],
        7.16,
    ),
    ),
)


@pytest.mark.parametrize('company_part, ex_company_part, expected', company_departments_test)
def test_work_statistics(company_part: dict, ex_company_part: tuple, expected: tuple):
    """Check if the statistics counts well or not.

    Args:
        company_part (dict): all departments with its respective employee names as keys.
        ex_company_part (tuple): used to exclude certain departments, defaults to ().
        expected (tuple): the right answer we should receive.
    """
    assert work_statistics(company_part, ex_company_part) == expected
