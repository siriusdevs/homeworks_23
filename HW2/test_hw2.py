"""Contains tests for hw2.py."""

import json
import os

from hw2 import process_data


def test_process_data():
    """Test process_data function."""
    process_data('./HW2/data_test.json', './data_test_output.json')

    with open('./data_test_output.json', 'r') as output_file:
        output_data = json.load(output_file)

    assert output_data == {
        'city_distribution': {
            'Moscow': 2/3*100,
            'Saint Petersburg': 1/3*100,
        },
        'year_distribution': {
            '2020': 2/3*100,
            '2021': 1/3*100,
        },
    }
    os.remove('./data_test_output.json')


def test_data():
    """Test data."""
    process_data('./HW2/data_hw2.json', './data_hw2_output.json')
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
