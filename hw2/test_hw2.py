import pytest

from hw2 import process_data

import json
 
from enum import IntEnum


class FileNumberEnum(IntEnum):
    """Enumeration class representing board for files."""

    leftboardvalid = 1
    rightboardvalid = 3
    leftdoardinvalid = 3
    rightboardinvalid = 6


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
        output_file = f'tests/output/{num}.json'
        input_file = f'tests/input/{num}.json'
        expected = f'tests/expected/{num}.json'
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
        input_file_path: the path to the input JSON file containing user data
        output_file_path: the path to the output JSON file where processed data will be saved
        expected_data: expected result
    """
    process_data(input_file_path, output_file_path)
    with open(output_file_path, 'r') as output_file:
        output_expected = json.load(output_file)
    assert output_expected == expected_data


@pytest.mark.parametrize('input_file_path, output_file_path, expected_data', INVALID_DATA)
def test_invalid(input_file_path: str, output_file_path: str, expected_data: dict) -> None:
    """Cheking invalid files.

    Args:
        input_file_path: the path to the input JSON file containing user data
        output_file_path: the path to the output JSON file where processed data will be saved
        expected_data: expected result
    """
    output = process_data(input_file_path, output_file_path)
    assert output == expected_data