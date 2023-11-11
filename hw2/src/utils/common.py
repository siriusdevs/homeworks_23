"""Consist functions that can't be a part of any specific entity."""
import json
import os
from logging import Logger
from typing import Any, Hashable, NoReturn


def get_valid_dict_to_str(dct: dict[Hashable, Any]) -> str:
    """Return string representation of the dict in valid format for msgspec.

    Args:
        dct (dict): any dict

    Returns:
        Valid string representation of the dict for msgspec
    """
    return str(dct).replace("'", '"')


def find_insertion_index(nums: list[int], target: int) -> int:
    """Find the index for insertion using binary search and return it.

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


def create_file(file_path: str) -> NoReturn:
    """Create all the sub dirs for output_file if the path contains it.

    Args:
        file_path (str): path to file we need to check.
    """
    file_path = file_path.replace('\\', '/')
    if not os.path.exists(file_path):
        dir_tree = '/'.join(file_path.rsplit('/')[:-1])
        if not dir_tree:
            return
        os.makedirs(dir_tree)


def log_error_and_write_to_output_file(error_msg: str, output_file_path: str, logger: Logger):
    # Write error logs to the console and to an output file.
    logger.error(error_msg)
    with open(output_file_path, 'w') as output_file:
        json.dump(
            obj={
                'status': 'Error',
                'details': {
                    'msg': error_msg,
                },
            },
            fp=output_file,
        )
