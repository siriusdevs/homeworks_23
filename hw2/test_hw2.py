"""Module for test hw2."""

from pathlib import Path

import pytest
from helper import DIRECTORY, opener, write_to_json
from task2 import process_data

test_data = [(f'data_hw2_{cnt}.json', f'output_hw2_{cnt}.json') for cnt in range(5)]


@pytest.mark.parametrize('source, expected', test_data)
def test_hw2(source: str, expected: str) -> None:
    """Test output stats hw2.

    Args:
        source (str): input and output files paths
        expected (str): expected file
    """
    process_data(DIRECTORY + source, f'{DIRECTORY}output_hw2_test.json')
    with open(DIRECTORY + expected) as exp_file:
        with open(f'{DIRECTORY}output_hw2_test.json') as test_file:
            assert exp_file.read() == test_file.read()
    Path(f'{DIRECTORY}output_hw2_test.json').unlink()


@pytest.mark.xfail(strict=True, raises=SystemExit)
def test_valid_json():
    """Validity test."""
    opener(f'{DIRECTORY}data_empty.json')
    opener(f'{DIRECTORY}data_invalid.json')


@pytest.mark.xfail(strict=True, raises=SystemExit)
def test_exists_json_or_dir():
    """Test for file or directory existence."""
    opener(f'{DIRECTORY}some_invalid_file_or_dir')
    write_to_json(f'{DIRECTORY}some_invalid_dir/some_file.txt')
