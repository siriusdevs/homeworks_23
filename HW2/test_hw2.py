"""My docstring."""
import json
import os

import pytest
from hw2 import calculate_email_host, calculate_registration_year, process_data

TEST_DATA_FILES = (
    (
        'not_found_file.json',
        'output/test_output.json',
        'Input file not found!',
        FileNotFoundError,
    ),
    (
        './HW2/input/json_decoder_error.json',
        'output/test_output.json',
        'File is not json!',
        ValueError,
    ),
    (
        './HW2/input/empty_json.json',
        'output/test_output.json',
        'Received empty data',
        ValueError,
    ),
)

SUCCESSFUL_TEST = (
    (
        './HW2/input/data1_hw2.json',
        './HW2/output/output_data.json',
        {
            'email_host_percentages': {
                'yandex.ru': 50.,
                'gmail.com': 50.,
            },
            'registration_year_percentages': {
                '2012': 50.,
                '2022': 50.,
            },
        },
    ),
    (
        './HW2/input/data2_hw2.json',
        './HW2/output/output_data.json',
        {
            'email_host_percentages': {
                'yahoo.com': 100.,
            },
            'registration_year_percentages': {
                '2016': 50.,
                '2014': 50.,
            },
        },
    ),
    (
        './HW2/input/empty_key.json',
        './HW2/output/output_data.json',
        {
            'email_host_percentages': {
                'yahoo.com': 50.,
            },
            'registration_year_percentages': {
                '2016': 50.,
            },
        },
    ),
)


@pytest.mark.parametrize('input_file, output_file, expected, error', TEST_DATA_FILES)
def test_with_error_code(input_file: str, output_file: str, expected: str, error: type):
    """
    Check returned error codes.

    Args:
        input_file (str): The path to the input file path.
        output_file (str): The path to the output file path.
        expected (str): Expexted error code value.
        error (type): The error that should be caused.
    """
    with pytest.raises(error):
        process_data(input_file, output_file)
    assert os.path.exists(output_file)
    with open(output_file) as final_file:
        error_text = final_file.read()
    assert error_text == expected


@pytest.mark.parametrize('input_file, output_file, expected', SUCCESSFUL_TEST)
def test_functional(input_file: str, output_file: str, expected: str):
    """
    Test module for functional.

    Args:
        input_file (str): The path to the input file path.
        output_file (str): The path to the output file path.
        expected (str): Expexted output value.
    """
    process_data(input_file, output_file)
    assert os.path.exists(output_file)
    with open(output_file) as final_file:
        output_data = json.load(final_file)
    assert output_data == expected


with open('./HW2/input/data1_hw2.json', 'r') as user_file:
    user_data = json.load(user_file)


def test_calculate_email_host():
    """Test the calculate email host."""
    expected_result = {'gmail.com': 50.0, 'yandex.ru': 50.0}
    assert calculate_email_host(user_data) == expected_result


def test_calculate_registration_year():
    """Test the calculate registration year."""
    expected_result = {'2012': 50.0, '2022': 50.0}
    assert calculate_registration_year(user_data) == expected_result
