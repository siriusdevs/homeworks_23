"""test for hw2.py."""
import json

import pytest

from hw2 import EmptyFileError, InvalidAddress, process_data

test_data = [('data_hw2.json', 'result_test_hw2.json', {
    'hosts_count': {
        'yandex.ru': 50.0,
        'gmail.com': 50.0,
    },
    'online_duration': {
        'lt_2_days': 0,
        'lt_1_week': 0,
        'lt_1_month': 0,
        'lt_6_months': 0,
        'mt_6_months': 100.0,
    },
},
),
]

test_empty_data = [('hw2/empty_data_hw2.json', 'empty_result_test_hw2.json')]

test_invalid_data = [('hw2/invalid_data_hw2.json', 'invalid_result_test_hw2.json')]


@pytest.mark.parametrize('input_file, output_file, output_data', test_data)
def test_process_data(input_file, output_file, output_data):
    """Test for funck process_data.

    Args:
        input_file (str): The path for the input file.
        output_file (str): The path for the output file
        output_data (dict): The test date result of the funck.
    """
    process_data(input_file_path=input_file, output_file_path=output_file)
    with open(output_file, 'r') as output:
        result_data = json.load(output)
    assert result_data == output_data


@pytest.mark.parametrize('input_file, output_file', test_empty_data)
@pytest.mark.xfail(raises=EmptyFileError)
def test_xfail_empty_data(input_file, output_file):
    """Test for funck process_data whith EmptyFileError.

    Args:
        input_file (str): The path for the input file.
        output_file (str): The path for the output file
    """
    process_data(input_file_path=input_file, output_file_path=output_file)


@pytest.mark.parametrize('input_file, output_file', test_invalid_data)
@pytest.mark.xfail(raises=InvalidAddress)
def test_xfail_invalid_data(input_file, output_file):
    """Test for funck process_data whith InvalidAddress.

    Args:
        input_file (str): The path for the input file.
        output_file (str): The path for the output file
    """
    process_data(input_file_path=input_file, output_file_path=output_file)
