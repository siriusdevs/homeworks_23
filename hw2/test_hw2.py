"""Module for testing main's functions."""

import json
from typing import TypeAlias

import main
import pytest

DIRECTORY = 'dataset_hw2'
FILE_PATH_FOR_OUTPUTTING = f'{DIRECTORY}/__file_for_testing__.json'

UsersOutput: TypeAlias = dict[str, dict[str, float]]

DATA_TEST_DATA_PROCESS: tuple[tuple[str, str, UsersOutput], ...] = (
    (
        f'{DIRECTORY}/first.json',
        FILE_PATH_FOR_OUTPUTTING,
        {
            'domains': {
                'gmail.com': 40.0,
                'yandex.ru': 60.0,
            },
            'years': {
                '18': 40.0,
                '31': 20.0,
                '32': 20.0,
                '35': 20.0,
            },
        },
    ),
    (
        f'{DIRECTORY}/second.json',
        FILE_PATH_FOR_OUTPUTTING,
        {
            'domains': {
                'yandex.ru': 100.0,
            },
            'years': {
                '18': 20.0,
                '19': 20.0,
                '31': 20.0,
                '32': 20.0,
                '35': 20.0,
            },
        },
    ),
)


@pytest.mark.parametrize('from_path, to_path, expected', DATA_TEST_DATA_PROCESS)
def test_data_process(from_path: str, to_path: str, expected: dict[str, float]) -> None:
    """Test main's function data_process.

    Args:
        from_path (str): file path with users' data.
        to_path (str): file path that has calculated users' data.
        expected (dict): expected data.
    """
    main.process_data(from_path, to_path)

    with open(FILE_PATH_FOR_OUTPUTTING) as test_file:
        test_result = json.load(test_file)
        assert test_result == expected
