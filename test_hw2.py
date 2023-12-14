"""This module include test for function process_data."""
import json
from enum import IntEnum

import pytest

from hw2 import process_data


class FileNumberEnum(IntEnum):
    """Enumeration class representing board for files."""

    leftboardvalid = 1
    rightboardvalid = 10
    leftdoardinvalid = 10
    rightboardinvalid = 12


def make_test_data(leftboard: int, rightboard: int) -> tuple:
    """Create test data.

    Args:
        leftboard: left border for file
        rightboard: right border for file

    Returns:
        tuple with test data.
    """
    res = []
    for num in range(leftboard, rightboard):
        output_file = f'hw2/output/{num}.json'
        input_file = f'hw2/input/{num}.json'
        expected = f'hw2/expected/{num}.json'
        with open(expected, 'r') as expected_file:
            expected_data = json.load(expected_file)
        res.append((input_file, output_file, expected_data))
    return tuple(res)


VALID_DATA = make_test_data(FileNumberEnum.leftboardvalid, FileNumberEnum.rightboardvalid)
INVALID_DATA = make_test_data(FileNumberEnum.leftdoardinvalid, FileNumberEnum.rightboardinvalid)


@pytest.mark.parametrize('input_file_path, output_file_path, expected_data', VALID_DATA)
def test_valid(input_file_path: str, output_file_path: str, expected_data: dict) -> None:
    """Checking for the normality of files.

    Args:
        input_file_path (str): _description_
        output_file_path (str): _description_
        expected_data (dict): _description_
    """
    process_data(input_file_path, output_file_path)
    with open(output_file_path, 'r') as output_file:
        output_expected = json.load(output_file)
    assert output_expected == expected_data


@pytest.mark.parametrize('input_file_path, output_file_path, expected_data', INVALID_DATA)
def test_invalid(input_file_path: str, output_file_path: str, expected_data: dict) -> None:
    """_summary_.

    Args:
        input_file_path (str): _description_
        output_file_path (str): _description_
        expected_data (dict): _description_
    """
    output = process_data(input_file_path, output_file_path)
    assert output == expected_data
