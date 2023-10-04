"""Tests for module lowest salaries."""
import pytest

from hw1 import lowest_salaries

test_data = [
    (
        ('it', {
            'Nikiforov': 10.0,
            'Litvinov': 20.0,
            'Argun': 30.0,
            'Demyanenko': 40.0,
            'Startsev': 50.0,
        },
        ),
        (10.0, 20.0, 30.0, 0.4),
    ),
    (
        ('hr', {
            'Tyapkova': 10.0,
            'Kolkareva': 10.0,
            'Kuznentsova': 10.0,
        },
        ),
        (10.0, 10.0, 10.0, 1.0),
    ),
]

test_data_args = [
    (
        (
            ('design', {
                'Fernandez': 10.0,
                'Thompson': 20.0,
                'Davidson': 30.0,
                'Ramirez': 40.0,
                'Stevenson': 50.0,
            },
            ),
            ('tech_support', {
                'Daniel': 60.0,
                'Patel': 70.0,
                'Bolton': 80.0,
            },
            ),
        ),
        (10.0, 20.0, 30.0, 0.17),
    ),
]

test_data_kwargs = [
    (
        ('data_analitics', {
            'Vargas': 10.0,
            'Morgan': 20.0,
            'Hicks': 30.0,
            'Steele': 40.0,
            'Estrada': 50.0,
        },
        ),
        100.0,
        (10.0, 20.0, 30.0, 0.4),
    ),
    (
        ('administrators', {
            'Walters': 10.0,
            'Wolf': 20.0,
            'Reese': 30.0,
            'Daniels': 40.0,
            'Torres': 50.0,
        },
        ),
        30.0,
        (10.0, 20.0, 0.2),
    ),
    (
        ('security', {
            'Salazar': 10.0,
            'Osborne': 20.0,
            'Santiago': 30.0,
            'Luna': 40.0,
            'Wilson': 50.0,
        },
        ),
        0,
        (0, 0, 0, 0),
    ),
]

test_data_args_kwargs = [
    (
        (
            ('management', {
                'Rowe': 10.0,
                'Ford': 20.0,
                'Paul': 30.0,
                'Turner': 40.0,
                'Peters': 50.0,
            },
            ),
            ('programmers', {
                'Wang': 60.0,
                'Lamb': 70.0,
                'Davis': 80.0,
            },
            ),
        ),
        100.0,
        (10.0, 20.0, 30.0, 0.17),
    ),
    (
        (
            ('engeneers', {
                'Fitzgerald': 100.0,
                'Craig': 200.0,
                'Acosta': 300.0,
                'Mac': 400.0,
                'Henderson': 500.0,
            },
            ),
            ('network_administrators', {
                'Griffin': 600.0,
                'Coleman': 70.0,
                'Fox': 80.0,
            },
            ),
        ),
        200.0,
        (70.0, 80.0, 100.0, 0.11),
    ),
]


@pytest.mark.parametrize('args, expected', test_data)
def test_lowest_salaries(args, expected):
    """Checks the correctness of the lowest_salaries function.

    Args:
        args: contains info about one dept.
        expected: expected values of three smallest salaries, and their ratio to all.
    """
    assert lowest_salaries(args) == expected


@pytest.mark.parametrize('args, expected', test_data_args)
def test_lowest_salaries_args(args, expected):
    """Checks the correctness of the lowest_salaries function with several depts in args.

    Args:
        args: contains info about several depts.
        expected: expected values of three smallest salaries, and their ratio to all.
    """
    assert lowest_salaries(*args) == expected


@pytest.mark.parametrize('args, kwargs, expected', test_data_kwargs)
def test_lowest_salaries_kwargs(args, kwargs, expected):
    """Checks the correctness of the lowest_salaries function.

    Args:
        args: contains info about one dept.
        kwargs: contains numerical value of salary limit.
        expected: expected values of three smallest salaries, and their ratio to all.
    """
    assert lowest_salaries(args, salary_limit=kwargs) == expected


@pytest.mark.parametrize('args, kwargs, expected', test_data_args_kwargs)
def test_lowest_salaries_args_kwargs(args, kwargs, expected):
    """Checks correctness of the lowest_salaries function with several depts in args and kwarg.

    Args:
        args: contains info about several depts.
        kwargs: contains numerical value of salary limit.
        expected: expected values of three smallest salaries, and their ratio to all.
    """
    assert lowest_salaries(*args, salary_limit=kwargs) == expected
