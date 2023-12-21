"""Testing module hw2.py."""


import json
import os

import pytest

import hw2

TEST_DIFFERENT_ARGUMENTS = (
    (f'input{str(num)}.json', f'expected{str(num)}.json') for num in range(1, 3)
)


@pytest.mark.parametrize('path_in, expected_path', TEST_DIFFERENT_ARGUMENTS)
def test_diff_args(path_in, expected_path):
    """
    Test absolutly different arguments for the `hw2.process_data` function.

    Args:
        path_in (str): The input path to the test data.
        expected_path (str): The expected output path for the test data.
    """
    path_in = os.path.join('hw2', 'test_folde', 'tests_diff_args', path_in)
    path_out = os.path.join('hw2', 'test_folde', 'output.json')
    expected_path = os.path.join('hw2', 'test_folde', 'tests_diff_args', expected_path)
    hw2.process_data(path_in, path_out)

    with open(expected_path, 'r') as expected_file:
        expected = json.load(expected_file)

    with open(path_out, 'r') as output_file:
        output_data = json.load(output_file)
    assert output_data == expected


TEST_NO_ARGUMENTS = (
    (f'input{str(num)}.json', f'expected{str(num)}.json') for num in range(1, 3)
)


@pytest.mark.parametrize('path_in, expected_path', TEST_NO_ARGUMENTS)
def test_no_args(path_in: str, expected_path: str):
    """
    Test no useful arguments for the `hw2.process_data` function.

    Args:
        path_in: The input path to the test data.
        expected_path: The expected output path for the test data.
    """
    path_in = os.path.join('hw2', 'test_folde', 'tests_no_args', path_in)
    path_out = os.path.join('hw2', 'test_folde', 'output.json')
    expected_path = os.path.join('hw2', 'test_folde', 'tests_no_args', expected_path)
    hw2.process_data(path_in, path_out)

    with open(expected_path, 'r') as expected_file:
        expected = json.load(expected_file)

    with open(path_out, 'r') as output_file:
        output_data = json.load(output_file)
    assert output_data == expected


TEST_SIMPLE_ARGUMENTS = (
    (f'input{str(num)}.json', f'expected{str(num)}.json') for num in range(1, 4)
)


@pytest.mark.parametrize('path_in, expected_path', TEST_SIMPLE_ARGUMENTS)
def test_simple_args(path_in: str, expected_path: str):
    """
    Test with some or all simple arguments for the `hw2.process_data` function.

    Args:
        path_in: The input path to the test data.
        expected_path: The expected output path for the test data.
    """
    path_in = os.path.join('hw2', 'test_folde', 'tests_simple_args', path_in)
    path_out = os.path.join('hw2', 'test_folde', 'output.json')
    expected_path = os.path.join('hw2', 'test_folde', 'tests_simple_args', expected_path)
    hw2.process_data(path_in, path_out)

    with open(expected_path, 'r') as expected_file:
        expected = json.load(expected_file)

    with open(path_out, 'r') as output_file:
        output_data = json.load(output_file)
    assert output_data == expected


TEST_ERROR_EXTENSIONS = (
    (
        'input.txt',
        'output.json',
    ),
    (
        'input.odt',
        'output.txt',
    ),
    (
        'input.jpeg',
        'output.jpg',
    ),
)


@pytest.mark.parametrize('path_in, path_out', TEST_ERROR_EXTENSIONS)
def test_error_extensions(path_in: str, path_out: str):
    """
    Test for the `FileExtensionError` exception in `hw2.process_data` function.

    Args:
        path_in (str): The input path to the test data.
        path_out (str): The output path for the test data.
    """
    expected_message = 'FileExtensionError: extension of input file is wrong'

    hw2.process_data(path_in, path_out)
    _, path_out = hw2.check_extension(path_in, path_out)

    with open(path_out, 'r') as output_file:
        output_message = json.load(output_file)
    assert output_message == expected_message


TEST_ERROR_PATH = (
    (
        'abcd.json',
        'output.json',
    ),
    (
        'xyz.json',
        'chess.json',
    ),
    (
        'bobr_dobr.json',
        'catdog.json',
    ),
)


@pytest.mark.parametrize('path_in, path_out', TEST_ERROR_PATH)
def test_error_path(path_in: str, path_out: str):
    """
    Test for the `FileError` exception if paths don't exists in `hw2.process_data` function.

    Args:
        path_in (str): The input path to the test data.
        path_out (str): The output path for the test data.
    """
    expected_message = 'FileError: input file does not exists'
    hw2.process_data(path_in, path_out)

    if not os.path.exists(path_out) and os.path.isdir(path_out):
        path_out = os.path.join(path_out, 'default_output.json')

    with open(path_out, 'r') as output_file:
        output_message = json.load(output_file)
    os.remove(path_out)
    assert output_message == expected_message


def test_error_file_empty():
    """Test for the `FileError` exception if file is empty in `hw2.process_data` function."""
    expected_message = 'FileError: input file is empty'
    path_in = os.path.join('hw2', 'test_folde', 'tests_error_empty', 'input.json')
    path_out = os.path.join('hw2', 'test_folde', 'tests_error_empty', 'output.json')

    hw2.process_data(path_in, path_out)
    with open(path_out, 'r') as output_file:
        output_message = json.load(output_file)
    assert output_message == expected_message


TEST_CHECK_TYPE_IN_FILE = (
    [],
    5,
    5.5,
    'str',
    (),
    True,
    None,
)


@pytest.mark.parametrize('input_data,', TEST_CHECK_TYPE_IN_FILE)
def test_error_check_type_in_file(input_data):
    """Test case to verify the error handling when the input data type is not a dictionary.

    Args:
        input_data: The input data for the test.
    """
    expected_message = 'TypeError: Type of input data is not a dictionary'
    path_in = os.path.join('hw2', 'test_folde', 'tests_type_in_file', 'input.json')

    with open(path_in, 'w') as input_file:
        json.dump(input_data, fp=input_file, indent=4)

    path_out = os.path.join('hw2', 'test_folde', 'tests_type_in_file', 'output.json')
    hw2.process_data(path_in, path_out)
    with open(path_out, 'r') as output_file:
        output_message = json.load(output_file)
    assert output_message == expected_message
