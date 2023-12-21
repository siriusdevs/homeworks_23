"""Tests for hw2.py."""
import json
import os

import pytest
from hw2 import process_data

TEST_DATA = (
    ('vydumanniy_file.json', 'test_output.json', 1),
    ('./HW2/input/decoderError.json', 'test_output.json', 2),
    ('./HW2/input/data_hw2.json', '/nesuchestvuyushaya_papka/1/1/1/1.json', 3),
)


@pytest.mark.parametrize('input_file, output_file, expected', TEST_DATA)
def test_with_error_code(input_file: str, output_file: str, expected: int):
    """
    Сhecking returned error codes.

    Args:
        input_file (str): name of input file.
        output_file (str): name of output file.
        expected (int): expected function error code.
    """
    assert process_data(input_file, output_file) == expected


def test_example():
    """Test for example."""
    process_data('./HW2/input/data_hw2.json', './HW2/output/test_output.json')
    with open('./HW2/output/test_output.json', 'r') as output_file:
        output_dict = json.load(output_file)
        assert output_dict == {
            'age_stats': {
                '0-18': 0,
                '18-25': 1,
                '25-45': 1,
                '45-60': 0,
                '60+': 0,
            },
            'last_login_stats': {
                'less2days': 0,
                'less1week': 0,
                'less1month': 0,
                'less6months': 1,
                '6months+': 1,
            },
        }
    os.remove('./HW2/output/test_output.json')
