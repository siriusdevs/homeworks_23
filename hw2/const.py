import enum


class LoginCategories(enum.Enum):
    INTERVAL_NAME = [
        '6 months since last login',
        '3 months since last login',
        '1 month since last login',
        '2 weeks since last login',
        '1 week since last login',
        '2 days since last login',
    ]

class IntervalsCounter(enum.Enum):
    MONTH = 31
    INTERVALS = [
    (0, MONTH * 6),
    (1, MONTH * 3),
    (2, MONTH),
    (3, MONTH // 2),
    (4, MONTH // 4),
    (5, 2),
]
