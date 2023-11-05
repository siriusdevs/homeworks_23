"""A module that provides constants for hw2."""

import typing
from datetime import timedelta

JsonDict = dict[str, typing.Any]

ROUND_UPTO = 2


AGE_MAX = 'age_max'
AGE_MIN = 'age_min'
AGE_AVERAGE = 'age_average'
AGE_MEDIAN = 'age_median'


LESS_TWO_DAYS = 'active_in_last_two_days_average_age'
LESS_WEEK = 'active_in_last_week_average_age'
LESS_MONTH = 'active_in_last_month_average_age'
LESS_HALFYEAR = 'active_in_last_halfyear_average_age'

GREATER_HALFYEAR = 'not_active_in_last_halfyear_average_age'

TimeFilterType = str
LESS: TimeFilterType = 'LESS'
GREATER: TimeFilterType = 'GREATER'

YEAR_DAYS = 365
MONTH_DAYS = 30
TIMEDELTAS: tuple[TimeFilterType, str, timedelta] = (
    (LESS, LESS_TWO_DAYS, timedelta(days=2)),
    (LESS, LESS_WEEK, timedelta(weeks=1)),
    (LESS, LESS_MONTH, timedelta(days=MONTH_DAYS)),
    (LESS, LESS_HALFYEAR, timedelta(days=YEAR_DAYS/2)),
    (GREATER, GREATER_HALFYEAR, timedelta(days=YEAR_DAYS/2)),
)
