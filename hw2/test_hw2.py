"""Contain tests for function process_data from hw2.py."""
import json

import pytest

from hw2.hw2 import process_data
from hw2.src.bbtypes import Error, Users
from hw2.src.utils import TestDataGenerator

TEST_DATA = TestDataGenerator()


@pytest.mark.parametrize('input_file_path, output_file_path, expected_output_data', TEST_DATA)
def test_process_data(
    input_file_path: str,
    output_file_path: str,
    expected_output_data: Users | Error,
) -> None:
    """Test process_data function.

    Args:
        input_file_path: path to file with users data
        output_file_path: path file where we save necessary stats
        expected_output_data: dict with correct statistics
    """
    # Ignore errors since they will be checked anyway.
    process_data(input_file_path, output_file_path)

    with open(output_file_path) as output_file:
        output_data = json.load(output_file)

    assert output_data == expected_output_data
