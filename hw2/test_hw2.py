"""Test functions from hw2.py."""

import json
from datetime import datetime

import hw2

AGE = 'age'


def test_last_login_date():
    """Test for last_login_date function."""
    user_info = {'last_login': '2022-01-01'}
    year = 2022
    assert hw2.last_login_date(user_info) == datetime(year, 1, 1)


def test_stats_by_time():
    """Test for stats_by_time function."""
    information = {
        'user1': {'last_login': '2023-12-22', AGE: 30},
        'user2': {'last_login': '2022-02-01', AGE: 25},
    }
    expected_result = {
        'less_than_2_days': 0,
        'less_than_1_week': 30,
        'less_than_1_month': 0,
        'less_than_6_months': 0,
        'more_than_6_months': 25,
    }
    assert hw2.stats_by_time(information) == expected_result


def test_process_data():
    """Test for process_data function."""
    input_file = './hw2/input/data_hw2.json'
    output_file = './hw2/output/data_output.json'
    expected_output = 'The program was completed without errors.'
    assert hw2.process_data(input_file, output_file) == expected_output


def test_calculate_average():
    """Test for calculate_average function."""
    time_stats = {
        'less_than_2_days': [20, 30, 40],
        'less_than_1_week': [25, 35],
        'less_than_1_month': [30, 40, 50],
        'less_than_6_months': [],
        'more_than_6_months': [],
    }
    hw2.calculate_average(time_stats)
    assert time_stats == {
        'less_than_2_days': 30.0,
        'less_than_1_week': 30.0,
        'less_than_1_month': 40.0,
        'less_than_6_months': 0,
        'more_than_6_months': 0,
    }


def test_get_age_group():
    """Test for get_age_group function."""
    example_list = (15, 20, 30, 55, 65)

    assert hw2.get_age_group(example_list[0]) == '0-18'
    assert hw2.get_age_group(example_list[1]) == '18-25'
    assert hw2.get_age_group(example_list[2]) == '25-45'
    assert hw2.get_age_group(example_list[3]) == '45-60'
    assert hw2.get_age_group(example_list[4]) == '60+'


def test_get_age_stats():
    """Test for get_age_stats function."""
    input_dict = {
        'user1': {AGE: 20},
        'user2': {AGE: 25},
        'user3': {AGE: 30},
        'user4': {AGE: 55},
        'user5': {AGE: 65},
    }
    assert hw2.get_age_stats(input_dict) == {
        '0-18': 0,
        '18-25': 1,
        '25-45': 2,
        '45-60': 1,
        '60+': 1,
    }


def test_process_data_invalid_file_path():
    """Test process_data function with an invalid file path."""
    input_file = 'nonexistent_data.json'
    output_file = 'output.json'
    expected_output = f'file {input_file} does not exist!'
    assert hw2.process_data(input_file, output_file) == expected_output


def test_process_data_with_data1():
    """Test to process the input data and write the result to the output file."""
    input_data = './hw2/input/example_data1.json'
    expected_output = './hw2/output/lead_example_data1.json'
    actual_output = './hw2/output/ans_example_data1.json'

    # Выполняем функцию, которую тестируем
    hw2.process_data(input_data, actual_output)

    # Сравниваем файлы реального и ожидаемого результата
    with open(actual_output) as actual_file:
        actual_result = json.load(actual_file)

    with open(expected_output) as expected_file:
        expected_result = json.load(expected_file)

    assert actual_result == expected_result


def test_process_data_with_data2():
    """Test to process the input data and write the result to the output file."""
    input_data = './hw2/input/example_data2.json'
    expected_output = './hw2/output/lead_example_data2.json'
    actual_output = './hw2/output/ans_example_data2.json'

    # Выполняем функцию, которую тестируем
    hw2.process_data(input_data, actual_output)

    # Сравниваем файлы реального и ожидаемого результата
    with open(actual_output) as actual_file:
        actual_result = json.load(actual_file)

    with open(expected_output) as expected_file:
        expected_result = json.load(expected_file)

    assert actual_result == expected_result


def test_process_data_with_data3():
    """Test to process the input data and write the result to the output file."""
    input_data = './hw2/input/example_data3.json'
    expected_output = './hw2/output/lead_example_data3.json'
    actual_output = './hw2/output/ans_example_data3.json'

    # Выполняем функцию, которую тестируем
    hw2.process_data(input_data, actual_output)

    # Сравниваем файлы реального и ожидаемого результата
    with open(actual_output) as actual_file:
        actual_result = json.load(actual_file)

    with open(expected_output) as expected_file:
        expected_result = json.load(expected_file)

    assert actual_result == expected_result
