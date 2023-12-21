"""Test module for the functions defined in hw2.py."""
import json
import os

from hw2 import calculate_email_host, calculate_registration_year, process_data

user_data = {
    'user': {
        'region': 'Saint-Petersburg',
        'registered': '2012-12-24',
        'last_login': '2023-10-01',
        'email': 'user@yandex.ru',
        'age': 36,
    },
    'user2': {
        'region': 'Sochi',
        'registered': '2022-10-30',
        'last_login': '2022-11-21',
        'email': 'user2@gmail.com',
        'age': 18,
    },
}


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
    process_data('./HW2/data_hw2.json', 'output_data.json')
    with open('output_data.json', 'r') as output_file:
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
    os.remove('output_data.json')
