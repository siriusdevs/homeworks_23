"""A module that provides constants for hw2."""

import typing
from datetime import timedelta

JsonDict = dict[str, typing.Any]

AGE_MAX = 'age_max'
AGE_MIN = 'age_min'
AGE_AVERAGE = 'age_average'
AGE_MEDIAN = 'age_median'


LESS_TWO_DAYS = 'less_two_days'
LESS_WEEK = 'less_week'
LESS_MONTH = 'less_month'
LESS_HALFYEAR = 'less_halfyear'

GREATER_HALFYEAR = 'greater_halfyear'

TimeFilterType = str
LESS: TimeFilterType = 'LESS'
GREATER: TimeFilterType = 'GREATER'

YEAR_DAYS = 365
TIMEDELTAS: tuple[TimeFilterType, str, timedelta] = (
    (LESS, LESS_TWO_DAYS, timedelta(days=2)),
    (LESS, LESS_WEEK, timedelta(weeks=1)),
    (LESS, LESS_MONTH, timedelta(weeks=4)),
    (LESS, LESS_HALFYEAR, timedelta(days=YEAR_DAYS/2)),
    (GREATER, GREATER_HALFYEAR, timedelta(days=YEAR_DAYS/2)),
)
