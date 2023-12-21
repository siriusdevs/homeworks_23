"""Test module for the functions defined in hw2.py."""
import json
import os

from hw2 import calculate_email_host, calculate_registration_year, process_data

with open('./HW2/input/data_hw2.json', 'r') as user_file:
    user_data = json.load(user_file)


def test_calculate_email_host():
    """Test the calculate email host."""
    expected_result = {'gmail.com': 50.0, 'yandex.ru': 50.0}
    assert calculate_email_host(user_data) == expected_result


def test_calculate_registration_year():
    """Test the calculate registration year."""
    expected_result = {'2012': 50.0, '2022': 50.0}
    assert calculate_registration_year(user_data) == expected_result


def test_hw2():
    """Test the process data."""
    process_data('./HW2/input/data_hw2.json', './HW2/output/output_data.json')
    with open('./HW2/output/output_data.json', 'r') as output_file:
        output_data = json.load(output_file)
    assert output_data == {
        'email_host_percentages': {
            'yandex.ru': 50.0,
            'gmail.com': 50.0,
        },
        'registration_year_percentages': {
            '2012': 50.0,
            '2022': 50.0,
        },
    }
    os.remove('./HW2/output/output_data.json')
