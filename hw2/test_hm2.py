"""Модуль тест для hm2."""

import json

import pytest

from hm2 import process_data

PERCENT25 = '25%'

TEST_DATA = (
    (
        'test_data/test_1.json',
        'result.json',
        {
            'statictik city': {
                'Saint-Petersburg': PERCENT25,
                'Sochi': '50%',
                'New-York': PERCENT25,
            },
            'statictik last login': {
                'было в сети менее полугода назад': '75%',
                'было в сети более полугода назад': PERCENT25,
            },
        },
    ),
    (
        'test_data/test_2.json',
        'result.json',
        {
            'statictik city': {
                'region not specified': '75%',
                'Sochi': PERCENT25,
            },
            'statictik last login': {
                'было в сети менее полугода назад': PERCENT25,
                'было в сети менее 2 дней назад': PERCENT25,
                'было в сети менее недели назад': PERCENT25,
                'было в сети менее месяца назад': PERCENT25,
            },
        },
    ),
    (
        'test_data/test_3.json',
        'result.json',
        {
            'statictik city': {
                'Las Vegas': PERCENT25,
                'Sochi': '50%',
                'New-York': PERCENT25,
            },
            'statictik last login': {
                'было в сети менее полугода назад': PERCENT25,
                'было в сети более полугода назад': '50%',
                'было в сети менее недели назад': PERCENT25,
            },
        },
    ),
)


@pytest.mark.parametrize('from_path, to_path, expected', TEST_DATA)
def test_process_data(from_path: str, to_path: str, expected: dict[str, str]) -> None:
    """Тест функции process_data.

    Args:
        from_path (str): тестовый файл с данными
        to_path (str): файл вывода
        expected (dict[str, str]): результат
    """
    process_data(from_path, to_path)
    with open(to_path, 'r') as filename:
        record_to_string = json.load(filename)
    assert record_to_string == expected
