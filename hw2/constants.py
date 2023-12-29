"""Constants for hw2."""

from datetime import timedelta
from typing import Any

ROUND_UPTO = 2

# data types
USERS_JSON = dict[str, Any]
STATS_JSON = dict[str, float]

# field names in json age stats
MINIMUM = 'minimum_age'
MAXIMUM = 'maximum_age'
AVERAGE = 'average_age'
MEDIAN = 'median_age'

LESS_TWO_DAYS = 'less_two_days'
LESS_WEEK = 'less_week'
LESS_MONTH = 'less_month'
LESS_HALF_YEAR = 'less_half_year'
GREATER_HALF_YEAR = 'greater_half_year'

# field names and deltas in json average age based on last login date
MONTH = 4
TIMEDELTAS = (
    (LESS_TWO_DAYS, timedelta(days=2)),
    (LESS_WEEK, timedelta(weeks=1)),
    (LESS_MONTH, timedelta(weeks=MONTH)),
    (LESS_HALF_YEAR, timedelta(weeks=6*MONTH)),
    (GREATER_HALF_YEAR, timedelta(weeks=6*MONTH)),
)
