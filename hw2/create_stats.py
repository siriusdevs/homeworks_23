"""Module with the helper that can calculate users' statistics."""

from functools import reduce
from typing import Optional


def create_stats(stats: dict[str, int], users_count: Optional[int] = None) -> dict[str, float]:
    """Create users' statistics (value will be in percents).

    Args:
        stats (dict[str, int]): The dict that has users' statistics.
        users_count (Optional[int]): \
            the count of all users, \
            it can be None and then it will be calculated automatic.

    Returns:
        dict[str, float]: users' statistics in percents.
    """
    if users_count is None:
        users_count = reduce(lambda start, current: start + current[1], stats.items(), 0)

    return {
        key: (count / users_count * 100) for (key, count) in stats.items()
    }
