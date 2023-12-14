"""Module for test hw2."""

from pathlib import Path

import pytest
from task2 import process_data

DIRECTORY = 'hw2/test_data_hw2/'
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
