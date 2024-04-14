"""Testing module 'hw2.py'."""

import json
import pytest
import modul

# Путь к файлу, в который функция сохраняет результаты
OUTPUT_PATH = 'hw2/tests_folder/output.json'

# Наборы данных для параметризации тестов
TEST_DATA = [
    ('hw2/tests_folder/test1.json', 'hw2/expected_folder/expected1.json'),
    ('hw2/tests_folder/test2.json', 'hw2/expected_folder/expected2.json')
]

@pytest.mark.parametrize('input_file, expected_file', TEST_DATA)
def test_process_data(input_file, expected_file):
    """
    Тестируем функцию process_data на различных наборах данных.
    Проверяем, что выходные данные соответствуют ожидаемым результатам.

    Args:
        input_file (str): Путь к входному файлу с тестовыми данными.
        expected_file (str): Путь к файлу с ожидаемыми результатами.
    """
    # Запускаем функцию обработки данных
    modul.process_data(input_file, OUTPUT_PATH)

    # Считываем ожидаемые результаты
    with open(expected_file, 'r') as file:
        expected_data = json.load(file)

    # Считываем полученные результаты
    with open(OUTPUT_PATH, 'r') as file:
        output_data = json.load(file)

    # Проверяем, что результаты соответствуют ожиданиям
    assert output_data == expected_data, "The processed data does not match expected results"

