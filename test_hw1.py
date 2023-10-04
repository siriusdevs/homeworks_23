"""Tests for module lowest salaries."""
import pytest

from hw1 import lowest_salaries

test_data = [
    (
        ('it', {
            'nikiforov': 10.0,
            'litvinov': 20.0,
            'argun': 30.0,
            'demyanenko': 40.0,
            'startsev': 50.0,
        },
        ),
        (10.0, 20.0, 30.0, 0.4),
    ),
    (
        ('hr', {
            'tyapkova': 10.0,
            'kolkareva': 10.0,
            'kuznentsova': 10.0,
        },
        ),
        (10.0, 10.0, 10.0, 1.0),
    ),
]

test_data_args = [
    (
        (
            ('it', {
                'nikiforov': 10.0,
                'litvinov': 20.0,
                'argun': 30.0,
                'demyanenko': 40.0,
                'startsev': 50.0,
            },
            ),
            ('hr', {
                'tyapkova': 60.0,
                'kolkareva': 70.0,
                'kuznentsova': 80.0,
            },
            ),
        ),
        (10.0, 20.0, 30.0, 0.17),
    ),
]

test_data_kwargs = [
    (
        ('it', {                    # name of department
            'nikiforov': 10.0,      # surnames below
            'litvinov': 20.0,
            'argun': 30.0,
            'demyanenko': 40.0,
            'startsev': 50.0,
        },
        ),
        100.0,                      # salary limit
        (10.0, 20.0, 30.0, 0.4),    # expected values
    ),
    (
        ('design', {
            'mukaseev': 10.0,
            'kolkareva': 20.0,
            'tyrin': 30.0,
            'roganov': 40.0,
            'startsev': 50.0,
        },
        ),
        30.0,
        (10.0, 20.0, 0.2),
    ),
    (
        ('design', {
            'mukaseev': 10.0,
            'kolkareva': 20.0,
            'tyrin': 30.0,
            'roganov': 40.0,
            'startsev': 50.0,
        },
        ),
        0,
        (0, 0, 0, 0),
    ),
]

test_data_args_kwargs = [
    (
        (
            ('it', {
                'nikiforov': 10.0,
                'litvinov': 20.0,
                'argun': 30.0,
                'demyanenko': 40.0,
                'startsev': 50.0,
            },
            ),
            ('hr', {
                'tyapkova': 60.0,
                'kolkareva': 70.0,
                'kuznentsova': 80.0,
            },
            ),
        ),
        100.0,
        (10.0, 20.0, 30.0, 0.17),
    ),
    (
        (
            ('it', {
                'nikiforov': 100.0,
                'litvinov': 200.0,
                'argun': 300.0,
                'demyanenko': 400.0,
                'startsev': 500.0,
            },
            ),
            ('hr', {
                'tyapkova': 600.0,
                'kolkareva': 70.0,
                'kuznentsova': 80.0,
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
