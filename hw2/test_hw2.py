"""Test to check the functionality of the function."""
import json

import pytest

from hw2 import process_data

OUTPUT_TEST = 'output_test.json'

test1 = (
    ('data_hw2.json', 'output_example.json', OUTPUT_TEST),
)

test2 = (
    ('input.json', 'output.json', OUTPUT_TEST),
)

test3 = (
    ('example_empty.json', 'output_empty.json', OUTPUT_TEST),
)

test4 = (
    ('example_data2.json', 'output_error.json', OUTPUT_TEST),
)


@pytest.mark.parametrize('input_data1, expected_output, output_data', test1)
def test_example_data(input_data1: str, expected_output: str, output_data: str):
    """Function.

    Args:
        input_data1: str - file name with input data.
        expected_output: str - file name with expected output.
        output_data: str - file name with output data.

    Asserts:
        True if the function returns expected results.

    """
    process_data(input_data1, output_data)
    with open(output_data) as output:
        test_output = json.load(output)
    with open(expected_output) as expected:
        test_exp = json.load(expected)
    assert test_output == test_exp


@pytest.mark.parametrize('input_data2, expected_output, output_data', test2)
def test_input_data(input_data2: str, expected_output: str, output_data: str):
    """Function.

    Args:
        input_data2: str - file name with input data.
        expected_output: str - file name with expected output.
        output_data: str - file name with output data.

    Asserts:
        True if the function returns expected results.

    """
    process_data(input_data2, output_data)
    with open(output_data) as output:
        test_output = json.load(output)
    with open(expected_output) as expected:
        test_exp = json.load(expected)
    assert test_output == test_exp


@pytest.mark.parametrize('input_data3, expected_error, output_data', test3)
def test_error_data(input_data3: str, expected_error: str, output_data: str):
    """Function.

    Args:
        input_data3: str - file name with input data.
        expected_error: str - file name with expected output.
        output_data: str - file name with output data.

    Asserts:
        True if the function returns expected results.

    """
    process_data(input_data3, output_data)
    with open(output_data) as output:
        test_output = json.load(output)
    with open(expected_error) as expected:
        test_exp = json.load(expected)
    assert test_output == test_exp


@pytest.mark.parametrize('input_data4, expected_error, output_data', test4)
def test_unexist_data(input_data4: str, expected_error: str, output_data: str):
    """Function.

    Args:
        input_data4: str - file name with input data.
        expected_error: str - file name with expected output.
        output_data: str - file name with output data.

    Asserts:
        True if the function returns expected results.

    """
    process_data(input_data4, output_data)
    with open(output_data) as output:
        test_output = json.load(output)
    with open(expected_error) as expected:
        test_exp = json.load(expected)
    assert test_output == test_exp
