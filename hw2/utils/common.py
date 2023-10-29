"""Module that consists functions that can't be a part of the certain entity."""
from typing import Any, Hashable


def get_valid_dict_to_str(dct: dict[Hashable, Any]) -> str:
    """Create function that returns string representation of the dict in valid format for msgspec.

    Args:
        dct (dict): any dict

    Returns:
        Valid string representation of the dict for msgspec
    """
    return str(dct).replace("'", '"')


def find_insertion_index(nums: list[int], target: int) -> int:
    """Create function that finds the index for insertion using binary search and returns it.

    Args:
        nums (list[int]): the list where we want to insert the target number
        target (int): the value we want to insert into the list

    Returns:
        Index to insert
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left
