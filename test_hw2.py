"""A module for testing hw2 process_data function."""

import json

import pytest

from hw2 import process_data

test_data = [
    ('data_hw2.json', 'output_hw2.json', 'data_hw2_out.json'),
    ('inp_cats.json', 'out_cats.json', 'cats.json'),
    ('inp_parrots.json', 'out_parrots.json', 'parrots.json'),
]


@pytest.mark.parametrize('input_file, output_file, expected', test_data)
def test_process_data(input_file: str, output_file: str, expected):
    """Test process_data function with test_data.

    Args:
        input_file (str): Json file with input test data.
        output_file (str): Json file with output test data.
        expected (_type_): Json file with expected output data.

    Asserts:
        True if process_data makes expected json file.
    """
    process_data(input_file, output_file)
    with open(output_file, 'rt') as o_f:
        output_f = json.load(o_f)
    with open(expected, 'rt') as e_f:
        expected_f = json.load(e_f)
    assert output_f == expected_f
