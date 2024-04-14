"""Testing module 'hw2.py'."""

import json
import pytest
import modul

# Путь к файлу, в который функция сохраняет результаты
OUTPUT_PATH = 'hw2/tests_folder/output.json'

# Наборы данных для параметризации тестов

# TEST_DIFFERENT_ARGUMENTS
TEST_DIFFERENT_ARGUMENTS = [
    ('hw2/tests_folder/test1.json', 'hw2/expected_folder/expected1.json'),
    ('hw2/tests_folder/test2.json', 'hw2/expected_folder/expected2.json')
]

# TEST_WITHOUT_DIFFERENT_ARGUMENTS
TEST_WITHOUT_DIFFERENT_ARGUMENTS = [
    ('hw2/tests_folder/test3.json', 'hw2/expected_folder/expected3.json'),
    ('hw2/tests_folder/test4.json', 'hw2/expected_folder/expected4.json'),
    ('hw2/tests_folder/test5.json', 'hw2/expected_folder/expected5.json')
]

# TEST_WITH_WRONG_TYPE_VARIABLES
TEST_WITH_WRONG_TYPE_VARIABLES = [
    ('hw2/tests_folder/test6.json', 'hw2/expected_folder/expected6.json')
]

# TEST_WITH_ERRORS
TEST_WITH_ERRORS = [
    ('hw2/tests_folder/test7.json', 'hw2/expected_folder/expected7.json'),
    ('hw2/tests_folder/test9.txt', 'hw2/expected_folder/expected9.json'),
    ('hw2/tests_folder/test10.txt', 'hw2/expected_folder/expected10.json'),
    ('hw2/tests_folder/test11.json', 'hw2/expected_folder/expected11.json')
]

# Тесты для различных наборов данных

@pytest.mark.parametrize('input_file, expected_file', TEST_DIFFERENT_ARGUMENTS)
def test_different_arguments(input_file, expected_file):
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


@pytest.mark.parametrize('input_file, expected_file', TEST_WITHOUT_DIFFERENT_ARGUMENTS)
def test_without_different_arguments(input_file, expected_file):
    """
    Тестируем функцию process_data на наборах данных с недостающими аргументами.
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


@pytest.mark.parametrize('input_file, expected_file', TEST_WITH_WRONG_TYPE_VARIABLES)
def test_with_wrong_type_variables(input_file, expected_file):
    """
    Тестируем функцию process_data на наборах данных с неправильными типами переменных.
    Проверяем, что выходные данные соответствуют ожидаемым результатам.

    Args:
        input_file (str): Путь к входному файлу с тестовыми данными.
        expected_file (str): Путь к файлу с ожидаемыми результатами.
    """
    # Запускаем функцию обработки данных
    try:
        modul.process_data(input_file, OUTPUT_PATH)
    except Exception as e:
        print("An error occurred:", e)
        return

    # Считываем ожидаемые результаты
    with open(expected_file, 'r') as file:
        expected_data = json.load(file)

    # Считываем полученные результаты
    with open(OUTPUT_PATH, 'r') as file:
        output_data = json.load(file)

    # Проверяем, что результаты соответствуют ожиданиям
    assert output_data == expected_data, "The processed data does not match expected results"


@pytest.mark.parametrize('input_file, expected_file', TEST_WITH_ERRORS)
def test_with_errors(input_file, expected_file):
    """
    Тестируем функцию process_data на наборах данных с ошибками.
    Проверяем, что выходные данные соответствуют ожидаемым результатам.

    Args:
        input_file (str): Путь к входному файлу с тестовыми данными.
        expected_file (str): Путь к файлу с ожидаемыми результатами.
    """
    # Запускаем функцию обработки данных
    try:
        modul.process_data(input_file, OUTPUT_PATH)
    except Exception as e:
        print("An error occurred:", e)
        return

    # Считываем ожидаемые результаты
    with open(expected_file, 'r') as file:
        expected_data = json.load(file)

    # Считываем полученные результаты
    with open(OUTPUT_PATH, 'r') as file:
        output_data = json.load(file)

    # Проверяем, что результаты соответствуют ожиданиям
    assert output_data == expected_data, "The processed data does not match expected results"