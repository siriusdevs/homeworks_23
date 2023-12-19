"""Test to check the functionality of the function."""
import json

import pytest

from hw2 import process_data

OUTPUT_TEST = 'output/output_test.json'

test_example = (
    ('input/data_hw2.json', 'output/output_example.json', OUTPUT_TEST),
)

test_correct = (
    ('input/correct.json', 'output/output_correct.json', OUTPUT_TEST),
)

test_empty = (
    ('input/empty.json', 'output/output_empty.json', OUTPUT_TEST),
)

test_unexist = (
    ('input/unexist_example.json', 'output/unexist_error.json', OUTPUT_TEST),
)

test_date = (
    ('input/uncorrect_date.json', 'output/date_error.json', OUTPUT_TEST),
)


@pytest.mark.parametrize('input_data1, expected_output, output_data', test_example)
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


@pytest.mark.parametrize('input_data2, expected_output, output_data', test_correct)
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


@pytest.mark.parametrize('input_data3, expected_error, output_data', test_empty)
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


@pytest.mark.parametrize('input_data4, expected_error, output_data', test_unexist)
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


@pytest.mark.parametrize('input_data1, expected_output, output_data', test_date)
def test_uncorrect_data(input_data1: str, expected_output: str, output_data: str):
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
