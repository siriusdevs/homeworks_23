"""process_data function test module."""

import json
import os

import pytest

from hw2 import process_data

OUTPUT_FILE = 'files/output.json'
INPUT_PATH = 'files/input/'
EXAMPLE_PATH = 'files/example/'

test_data = (
    ('empty.json'),
    ('empty_object.json'),
    ('empty_list.json'),
    ('correct.json'),
    ('unexistent.json'),
    ('incorrect_email.json'),
    ('non_existent_field.json'),
    ('empty_field.json'),
)


def compare(example_file: str) -> bool:
    """Compare file data.

    Args:
        example_file: str - path to file with expected data.

    Returns:
        bool: are files equal?
    """
    with open(OUTPUT_FILE) as out:
        test_result = json.load(out)
    with open(example_file) as ex:
        expected = json.load(ex)
    return test_result == expected


@pytest.mark.parametrize('file_name', test_data)
def test_process_data(file_name: str):
    """Test process_data function.

    Args:
        file_name: str - name of input file and file with expected data.
    """
    input_file = f'{INPUT_PATH}{file_name}'
    example_file = f'{EXAMPLE_PATH}{file_name}'
    process_data(input_file, OUTPUT_FILE)
    assert compare(example_file)
    os.remove(OUTPUT_FILE)
