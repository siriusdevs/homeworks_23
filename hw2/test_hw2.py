"""Module for test hw2."""

from pathlib import Path

import pytest
from main import process_data

DIRECTORY = 'hw2/test_data_hw2/'
test_data = [(f'data_hw2_{cnt}.json', f'output_hw2_{cnt}.json') for cnt in range(5)]


@pytest.mark.parametrize('source, expected', test_data)
def test_hw2(source: str, expected: str) -> None:
    """_summary_.

    Args:
        source (str): _description_
        expected (str): _description_
    """
    process_data(DIRECTORY + source, f'{DIRECTORY}output_hw2_test.json')
    with open(DIRECTORY + expected) as exp_file:
        with open(f'{DIRECTORY}output_hw2_test.json') as test_file:
            assert exp_file.read() == test_file.read()
    Path(f'{DIRECTORY}output_hw2_test.json').unlink()
