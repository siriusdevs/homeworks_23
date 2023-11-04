"""A module that provides constants for hw2."""

import datetime

LESS_TWO_DAYS = 'less_two_days'
LESS_WEEK = 'less_week'
LESS_MONTH = 'less_month'
LESS_HALFYEAR = 'less_halfyear'

GREATER_HALFYEAR = 'greater_halfyear'

YEAR_DAYS = 365
TIMEDELTAS_LESS = (
    (LESS_TWO_DAYS, datetime.timedelta(days=2)),
    (LESS_WEEK, datetime.timedelta(weeks=1)),
    (LESS_MONTH, datetime.timedelta(weeks=4)),
    (LESS_HALFYEAR, datetime.timedelta(days=YEAR_DAYS/2)),
)


TIMEDELTAS_GREATER = (
    (GREATER_HALFYEAR, datetime.timedelta(days=YEAR_DAYS/2)),
)
