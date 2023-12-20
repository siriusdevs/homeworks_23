"""Модуль тест для hw2."""

import json

import pytest

from hw2 import process_data

TEST_DATA = (
    (
        'test_data/test_1.json',
        'test_data/result_1.json',
    ),
    (
        'test_data/test_2.json',
        'test_data/result_2.json',
    ),
    (
        'test_data/test_3.json',
        'test_data/result_3.json',
    ),
)


@pytest.mark.parametrize('from_path, expected', TEST_DATA)
def test_process_data(from_path: str, expected: str) -> None:
    """Тест функции process_data.

    Args:
        from_path (str): тестовый файл с данными
        expected (str): результат
    """
    process_data(from_path, 'result.json')
    with open('result.json', 'r') as file_result:
        with open(expected, 'r') as file_expected:
            assert json.load(file_result) == json.load(file_expected)


FAILED_TEST_DATA = (
    (
        'test_data/no_file11.json',
        'test_data/result_1.json',
        'Файла test_data/no_file11.json не существует!',
    ),
    (
        'test_data/test_1.json',
        'test_data/no_file22.json',
        'Файла test_data/no_file22.json не существует!',
    ),
    (
        'test_data/empty_file.json',
        'test_data/empty_file.json',
        'Файл test_data/empty_file.json пустой!',
    ),
    (
        'test_data/test_invalid_date.json',
        'test_data/result.json',
        'Некорректная дата',
    ),
)


@pytest.mark.parametrize('from_path, to_path, expected', FAILED_TEST_DATA)
def test_process_data2(from_path: str, to_path: str, expected: str) -> None:
    """Тест функции process_data на ошибки.

    Args:
        from_path (str): тестовый файл с данными
        to_path (str): файл вывода
        expected (str): результат
    """
    res = process_data(from_path, to_path)
    assert res == expected
