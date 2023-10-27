"""Module for testing functions process_data, create_stats, increment_field."""

import json
from typing import TypeAlias

import create_stats
import increment_field
import main
import pytest

DATA_TEST_CREATE_STATS: tuple[tuple[dict, int, dict], ...] = (
    (
        {
            'yandex': 2,
            'mail.ru': 3,
        },
        5,
        {
            'yandex': 40.0,
            'mail.ru': 60.0,
        },
    ),
    (
        {},
        0,
        {},
    ),
)

DATA_TEST_INCREMENT_FIELD: tuple[tuple[dict, str, dict], ...] = (
    (
        {
            'a': 1,
        },
        'a',
        {
            'a': 2,
        },
    ),
    (
        {
            'b': 1,
        },
        'c',
        {
            'b': 1,
            'c': 1,
        },
    ),
)

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
    (
        f'{DIRECTORY}/third.json',
        FILE_PATH_FOR_OUTPUTTING,
        {
            'domains': {},
            'years': {},
        },
    ),
)


@pytest.mark.parametrize('stats, all_count, expected', DATA_TEST_CREATE_STATS)
def test_create_stats(stats: dict[str, int], all_count: int, expected: dict[str, float]) -> None:
    """Test create stats.

    Args:
        stats (dict[str, int]): dictionary that has int values in your field.
        all_count (int): the count of all registered entity.
        expected (dict[str, float]): dictionary that has percents value in your field.
    """
    assert create_stats.create_stats(stats, all_count) == expected


@pytest.mark.parametrize('dictionary, field, expected', DATA_TEST_INCREMENT_FIELD)
def test_increment_field(dictionary: dict[str, int], field: str, expected: dict[str, int]) -> None:
    """Test function increment field.

    Args:
        dictionary (dict[str, int]): given dictionary with element's count in field.
        field (str): dictionary's field key.
        expected (dict[str, int]): dictionary with incremented field.
    """
    increment_field.increment_field(dictionary, field)
    assert dictionary == expected


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
