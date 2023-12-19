"""Модуль тест для hm2."""

import json

import pytest
from hm2 import process_data

TEST_DATA = (
    (
        'hw2/test_data/test_1.json',
        'hw2/test_data/result_1.json',
    ),
    (
        'hw2/test_data/test_2.json',
        'hw2/test_data/result_2.json',
    ),
    (
        'hw2/test_data/test_3.json',
        'hw2/test_data/result_3.json',
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
        'hw2/test_data/no_file11.json',
        'hw2/test_data/result_1.json',
        'Файла hw2/test_data/no_file11.json не существует!',
    ),
    (
        'hw2/test_data/test_1.json',
        'hw2/test_data/no_file22.json',
        'Файла hw2/test_data/no_file22.json не существует!',
    ),
    (
        'hw2/test_data/empty_file.json',
        'hw2/test_data/empty_file.json',
        'Файл hw2/test_data/empty_file.json пустой!',
    ),
    (
        'hw2/test_data/test_invalid_date.json',
        'hw2/test_data/result.json',
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
