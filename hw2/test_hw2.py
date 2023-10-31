"""Test module for function process_data from hw2.py."""
import json
from contextlib import suppress

import pytest
from msgspec import ValidationError

from hw2.hw2 import process_data
from hw2.typesdev import Error, Users
from hw2.utils.test_data_initialiser import TestDataGenerator

TEST_DATA = TestDataGenerator()


@pytest.mark.parametrize('input_file_path, output_file_path, expected_output_data', TEST_DATA)
def test_process_data(
    input_file_path: str,
    output_file_path: str,
    expected_output_data: Users | Error,
) -> None:
    """Create function (extended by pytest decorator) that tests process_data function.

    Args:
        input_file_path: path to file with users data
        output_file_path: path file where we save necessary stats
        expected_output_data: dict with correct statistics
    """
    # Ignore errors since they will be checked anyway.
    with suppress(ValidationError, json.JSONDecodeError):
        process_data(input_file_path, output_file_path)

    with open(output_file_path) as output_file:
        output_data = json.load(output_file)

    assert output_data == expected_output_data
