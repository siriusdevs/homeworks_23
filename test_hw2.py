"""Contains tests for hw2.py."""

import json
import os

from hw2 import process_data


def test_process_data():
    """Test process_data function."""
    test_data = {
        'user1': {'region': 'Moscow', 'registered': '2020-01-01'},
        'user2': {'region': 'Moscow', 'registered': '2021-01-01'},
        'user3': {'region': 'Saint Petersburg', 'registered': '2020-01-01'},
    }

    with open('test_input.json', 'w') as input_file:
        json.dump(test_data, input_file)

    process_data('test_input.json', 'test_output.json')

    with open('test_output.json', 'r') as output_file:
        output_data = json.load(output_file)

    assert output_data['city_distribution'] == {'Moscow': 2/3*100, 'Saint Petersburg': 1/3*100}
    assert output_data['year_distribution'] == {'2020': 2/3*100, '2021': 1/3*100}
    os.remove('test_input.json')
    os.remove('test_output.json')


def test_data():
    """Test data."""
    process_data('./data_hw2.json', './data_hw2_output.json')
    with open('./data_hw2_output.json', 'r') as output_file:
        output_data = json.load(output_file)
    assert output_data == {
        'city_distribution': {
            'Sochi': 50.0,
            'Saint-Petersburg': 50.0,
        },
        'year_distribution': {
            '2012': 50.0,
            '2022': 50.0,
        },
    }
    os.remove('./data_hw2_output.json')
