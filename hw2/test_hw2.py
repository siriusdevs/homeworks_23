import json
from datetime import datetime

import pytest

from hw2 import av_user_age, convert_date, process_data

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
        {LT_DAYS: [30], LT_WEEK: [30], LT_MONTH: [30], LT_HALF_YEAR: [30], GT_HALF_YEAR: [25]},
    ),
    (
        {AGE: 40, LAST_LOGIN: '2023-12-18'},
        {LT_DAYS: [], LT_WEEK: [], LT_MONTH: [], LT_HALF_YEAR: [35], GT_HALF_YEAR: []},
        {LT_DAYS: [], LT_WEEK: [40], LT_MONTH: [40], LT_HALF_YEAR: [35, 40], GT_HALF_YEAR: []},
    ),
)


@pytest.mark.parametrize('user, ages, expected', age)
def test_av_user_age(user, expected, ages):
    assert av_user_age(user, ages) == expected

files = (
    (
        'tests/test1.json',
        'output.json',
        'tests/test1_answer.json',
    ),
    (
        'tests/test2.json',
        'output.json',
        'tests/test2_answer.json',
    ),
    (
        'tests/test3.json',
        'output.json',
        'tests/test3_answer.json',
    ),
    (
        'tests/test4.json',
        'output.json',
        'tests/test4_answer.json',
    ),
    (
        'tests/test5.json',
        'output.json',
        'tests/test5_answer.json',
    ),
    (
        'tests/test6.json',
        'output.json',
        'tests/test6_answer.json',
    ),
    (
        'tests/test7.json',
        'output.json',
        'tests/test7_answer.json',
    ),
)

@pytest.mark.parametrize('inp, out, expected', files)
def test_process_data(inp, out, expected):
    process_data(inp, out)
    assert json.load(open(out, 'r')) == json.load(open(expected, 'r'))
