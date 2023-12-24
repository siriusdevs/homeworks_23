"""Contains tests for hw2.py."""

import json
import os

import pytest
from hw2 import get_stat, process_data

REGION = 'region'
REGISTERED = 'registered'


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


def create_sample_input_file(tmp_path):
    """
    Test the process_data function when the input file is not found.

    Args:
        tmp_path (py.path.LocalPath): Temporary path provided by pytest.

    Returns:
        str: Path to the generated input file.
    """
    data_dict = {
        'user1': {REGION: 'Citi1', REGISTERED: '2022-01-01'},
        'user2': {REGION: 'Citi2', REGISTERED: '2022-02-01'},
    }
    input_file = tmp_path / 'input.json'
    with open(input_file, 'w') as file_path:
        json.dump(data_dict, file_path)
    return str(input_file)


def create_sample_output_file(tmp_path):
    """
    Test function for the 'get_stat' function.

    Args:
        tmp_path (py.path.LocalPath): Temporary path provided by pytest.

    Returns:
        str: Path to the generated output file.
    """
    return str(tmp_path / 'output.json')


def test_process_data_valid_files(tmp_path):
    """
    Test function for processing valid input files.

    Args:
        tmp_path (py.path.LocalPath): Temporary path provided by pytest.
    """
    sample_input_file = create_sample_input_file(tmp_path)
    sample_output_file = create_sample_output_file(tmp_path)

    result_obtained = process_data(sample_input_file, sample_output_file)
    assert result_obtained == 'Success'


def test_process_data_empty_data(tmp_path):
    """
    Test function for handling empty input data.

    Args:
        tmp_path (py.path.LocalPath): Temporary path provided by pytest.
    """
    empty_input_file = tmp_path / 'empty_input.json'
    with open(empty_input_file, 'w') as file_path:
        json.dump({}, file_path)

    sample_output_file = create_sample_output_file(tmp_path)

    with pytest.raises(ValueError, match='Received empty data'):
        process_data(str(empty_input_file), sample_output_file)


def test_get_stat():
    """Test function for the 'get_stat' function."""
    data_dict = {
        'user1': {REGION: 'City1', REGISTERED: '2022-01-01'},
        'user2': {REGION: 'City2', REGISTERED: '2022-02-01'},
    }
    result_obtained = get_stat(data_dict)
    assert 'city_distribution' in result_obtained
    assert 'year_distribution' in result_obtained


def test_process_data_file_not_found():
    """Test the process_data function when the input file is not found."""
    assert process_data('nonexist_file.json', 'output.json') == 'nonexist_file.json not found'
