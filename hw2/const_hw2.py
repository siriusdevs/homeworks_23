"""A module that provides constants for hw2."""

from datetime import timedelta

from . import fields_hw2, types_hw2

ROUND_UPTO = 2


LESS_FILTER: types_hw2.TimeFilterType = 'LESS'
GREATER_FILTER: types_hw2.TimeFilterType = 'GREATER'

_HALFYEAR_DAYS = 180
_MONTH_DAYS = 30
TIMEDELTAS = (
    (LESS_FILTER, fields_hw2.LESS_TWO_DAYS, timedelta(days=2)),
    (LESS_FILTER, fields_hw2.LESS_WEEK, timedelta(weeks=1)),
    (LESS_FILTER, fields_hw2.LESS_MONTH, timedelta(days=_MONTH_DAYS)),
    (LESS_FILTER, fields_hw2.LESS_HALFYEAR, timedelta(days=_HALFYEAR_DAYS)),
    (GREATER_FILTER, fields_hw2.GREATER_HALFYEAR, timedelta(days=_HALFYEAR_DAYS)),
)
