"""Tests for hw2."""

import json

import pytest

from hw2 import av_user_age, process_data

LT_DAYS = 'lt_2_days'
LT_WEEK = 'lt_week'
LT_MONTH = 'lt_month'
LT_HALF_YEAR = 'lt_half_year'
GT_HALF_YEAR = 'gt_half_year'
AGE = 'age'
LAST_LOGIN = 'last_login'

age = (
    (
        {AGE: 25, LAST_LOGIN: '2023-1-1'},
        {},
        {LT_DAYS: [], LT_WEEK: [], LT_MONTH: [], LT_HALF_YEAR: [], GT_HALF_YEAR: [25]},
    ),
    (
        {AGE: 30, LAST_LOGIN: '2023-12-17'},
        {},
        {LT_DAYS: [], LT_WEEK: [30], LT_MONTH: [30], LT_HALF_YEAR: [30], GT_HALF_YEAR: []},
    ),
    (
        {AGE: 35, LAST_LOGIN: '2023-6-30'},
        {},
        {LT_DAYS: [], LT_WEEK: [], LT_MONTH: [], LT_HALF_YEAR: [35], GT_HALF_YEAR: []},
    ),
    (
        {AGE: 40, LAST_LOGIN: '2023-12-18'},
        {},
        {LT_DAYS: [], LT_WEEK: [40], LT_MONTH: [40], LT_HALF_YEAR: [40], GT_HALF_YEAR: []},
    ),
    (
        {AGE: 30, LAST_LOGIN: '2023-12-20'},
        {LT_DAYS: [], LT_WEEK: [], LT_MONTH: [], LT_HALF_YEAR: [], GT_HALF_YEAR: [25]},
        {LT_DAYS: [], LT_WEEK: [30], LT_MONTH: [30], LT_HALF_YEAR: [30], GT_HALF_YEAR: [25]},
    ),
    (
        {AGE: 40, LAST_LOGIN: '2023-12-18'},
        {LT_DAYS: [], LT_WEEK: [], LT_MONTH: [], LT_HALF_YEAR: [35], GT_HALF_YEAR: []},
        {LT_DAYS: [], LT_WEEK: [40], LT_MONTH: [40], LT_HALF_YEAR: [35, 40], GT_HALF_YEAR: []},
    ),
)


@pytest.mark.parametrize('user, ages, expected', age)
def test_av_user_age(user, ages, expected):
    """
    Test function for av_user_age.

    Args:
        user (dict): The user dictionary containing the user's details.
        ages (dict): The age dictionary to be updated.
        expected (dict): The expected result.
    """
    assert av_user_age(user, ages) == expected


OUTPUT = 'output.json'

files = (
    (
        'hw2/tests/test1.json',
        OUTPUT,
        'hw2/tests/test1_answer.json',
    ),
    (
        'hw2/tests/test2.json',
        OUTPUT,
        'hw2/tests/test2_answer.json',
    ),
    (
        'hw2/tests/test3.json',
        OUTPUT,
        'hw2/tests/test3_answer.json',
    ),
    (
        'hw2/tests/test4.json',
        OUTPUT,
        'hw2/tests/test4_answer.json',
    ),
    (
        'hw2/tests/test5.json',
        OUTPUT,
        'hw2/tests/test5_answer.json',
    ),
    (
        'hw2/tests/test6.json',
        OUTPUT,
        'hw2/tests/test6_answer.json',
    ),
    (
        'hw2/tests/test7.json',
        OUTPUT,
        'hw2/tests/test7_answer.json',
    ),
)


@pytest.mark.parametrize('inp, out, exp', files)
def test_process_data(inp, out, exp):
    """
    Test function for process_data.

    Args:
        inp (str): The path to the input JSON file containing the user data.
        out (str): The path to the output JSON file where the results will be dumped.
        exp (str): The path to the expected output JSON file.
    """
    process_data(inp, out)
    with (  # noqa: WPS316
        open(out, 'r') as output,
        open(exp, 'r') as expected,
    ):
        assert json.load(output) == json.load(expected)
