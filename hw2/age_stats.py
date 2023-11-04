"""Provides types and functions for compution of users' age stats."""


import dataclasses
from typing import Iterable

ROUND_UPTO = 2


@dataclasses.dataclass
class AgeStats:
    """Basic stats for a list of ages."""

    min: float = 0
    max: float = 0
    average: float = 0
    median: float = 0

    def to_json(self) -> dict:
        """Convert AgeStats to a dict for json encoding.

        Returns:
            A dictionary with all fields
        """
        return dataclasses.asdict(self)


def get_age_stats(users: Iterable[dict]) -> AgeStats:
    """Compute age stats for a group of users.

    Args:
        users: group of users for which to compute stats

    Returns:
        age statistics
    """
    ages = [user['age'] for user in users]
    return AgeStats(
        min=min(ages),
        max=max(ages),
        average=round(_average(ages), 2),
        median=round(_median(ages), 2),
    ) if ages else AgeStats()


def _average(nums: Iterable[float]) -> float:
    return sum(nums) / len(nums)


def _median(nums: Iterable[float]) -> float:
    nums = sorted(nums)
    center = len(nums) // 2
    return (
        nums[center]
        if len(nums) % 2
        else _average(nums[center - 1:center + 1])
    )
