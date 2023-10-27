"""Module with the helper that can calculate users' statistics."""


def create_stats(stats: dict[str, int], users_count: int) -> dict[str, float]:
    """Create users' statistics (value will be in percents).

    Args:
        stats (dict[str, int]): The dict that has users' statistics.
        users_count (int): the count of all users.

    Returns:
        dict[str, float]: users' statistics in percents.
    """
    return {
        key: (count / users_count * 100) for (key, count) in stats.items()
    }
