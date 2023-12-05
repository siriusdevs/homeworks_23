"""Contains all hw2 constants."""

from datetime import timedelta
from types import MappingProxyType

AGE_INPUT_FIELD_NAME = 'age'
DATE_INPUT_FIELD_NAME = 'last_login'

AGE_OUTPUT_FIELD_NAME = 'age_percent'
DATE_OUTPUT_FIELD_NAME = 'last_login_date_percent'

OUTPUT_AGE_STATICTIC_FORM = MappingProxyType({
    '0-18': (0, 18),
    '18-25': (18, 25),
    '25-45': (25, 45),
    '45-60': (45, 60),
    '60+': (60, float('inf')),
})

DAY_PER_MOUNTH = 30
DAYS_PER_HALF_YEAR = 182

OUTPUT_DATE_STATISTIC_FORM = MappingProxyType({
    'less 2 day': (timedelta(days=0), timedelta(days=2)),
    'week': (timedelta(days=2), timedelta(weeks=1)),
    'month': (timedelta(weeks=1), timedelta(DAY_PER_MOUNTH)),
    'half year': (timedelta(DAY_PER_MOUNTH), timedelta(DAYS_PER_HALF_YEAR)),
    'more half year': (timedelta(DAYS_PER_HALF_YEAR), timedelta.max),
})
