"""Module that consists functions that can't be a part of the certain entity."""
import json
import os
from typing import Any, Hashable, NoReturn, Optional

from hw2.src import bbtypes


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


def validate_file_path(file_path: str, output_file_path: Optional[str] = None) -> NoReturn:
    """Create a function that checks whether the file exists or not.

    Args:
        file_path (str): path to file we need to check.
        output_file_path (Optional[str]): path to file that we write an error message in.

    Raises:
        FileNotFoundError: if the specified path to file is incorrect.
    """
    if not os.path.exists(file_path):
        if output_file_path:
            process_output_file(output_file_path)

            with open(output_file_path, 'w') as output_file:
                json.dump(
                    obj=create_error_object(msg=f'Invalid path to data file ({file_path})'),
                    fp=output_file,
                )
        raise FileNotFoundError(
            f'The specified path to file ({file_path}) is incorrect. File does not exist',
        )


def process_output_file(output_file_path: str) -> NoReturn:
    """Create a function that creates all the sub dirs for output_file if the path contains it.

    Args:
        output_file_path (str): path to file we need to check.
    """
    output_file_path = output_file_path.replace('\\', '/')
    if not os.path.exists(output_file_path):
        dir_tree = '/'.join(output_file_path.rsplit('/')[:-1])
        os.makedirs(dir_tree)


def create_error_object(msg: str) -> bbtypes.Error:
    """Create a function that returns the bbtypes.Error object with the custom message.

    Args:
        msg (str): custom message.

    Returns:
        The bbtypes.Error object
    """
    return {
        'status': 'Error',
        'details': {
            'msg': msg,
        },
    }
