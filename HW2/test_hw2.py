"""Contains tests for hw2.py."""

import json
import os

import pytest
from hw2 import get_stat, process_data

REGION = 'region'
REGISTERED = 'registered'
TEST1_EXPECTED = {
    'city_distribution': {
        'Moscow': 2/3*100,
        'Saint Petersburg': 1/3*100,
    },
    'year_distribution': {
        '2020': 2/3*100,
        '2021': 1/3*100,
    },
}
TEST2_EXPECTED = {
    'city_distribution': {
        'Sochi': 50.0,
        'Saint-Petersburg': 50.0,
    },
    'year_distribution': {
        '2012': 50.0,
        '2022': 50.0,
    },
}
TEST_DATA = (
    ('./HW2/data_test.json', './data_test_output.json', TEST1_EXPECTED),
    ('./HW2/data_hw2.json', './data_hw2_output.json', TEST2_EXPECTED),
)


@pytest.mark.parametrize('input_file, output_file, expected', TEST_DATA)
def test(input_file, output_file, expected):
    """
    Test function for the `process_data` function.

    Args:
        input_file (str): Path to the input file containing test data.
        output_file (str): Path to the output file where `process_data` will write the result.
        expected: The expected result to compare with the output_data.
    """
    process_data(input_file, output_file)

    with open(output_file, 'r') as outputt_file:
        output_data = json.load(outputt_file)
    assert output_data == expected
    os.remove(output_file)


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

    process_data(empty_input_file, sample_output_file)
    with open(sample_output_file, 'r') as file_output:
        data_from_file = json.load(file_output)
    empty_dict = {}
    assert data_from_file == empty_dict


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
