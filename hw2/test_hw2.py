"""Testing module 'hw2.py."""

import json

import pytest

import hw2

PATH = 'hw2/tests_folder/output.json'
PATH_ERROR = 'hw2/error.json'


TEST_DIFFERENT_ARGUMENTS = (
    ('hw2/tests_folder/test1.json', 'hw2/expected_folder/1.json'),
    ('hw2/tests_folder/test2.json', 'hw2/expected_folder/2.json'),
)


TEST_WITHOUT_DIFFERENT_ARGUMENTS = (
    ('hw2/tests_folder/test3.json', 'hw2/expected_folder/3.json'),
    ('hw2/tests_folder/test4.json', 'hw2/expected_folder/4.json'),
    ('hw2/tests_folder/test5.json', 'hw2/expected_folder/5.json'),
)


TEST_WITH_WRONG_TYPE_VARIABLES = (
    ('hw2/tests_folder/test6.json', 'hw2/expected_folder/6.json'),
)


TEST_WITH_ERRORS = (
    ('hw2/tests_folder/test7.json', 'hw2/expected_folder/7.json'),
    ('hw2/tests_folder/test9.txt', 'hw2/expected_folder/9.json'),
    ('hw2/tests_folder/test10.txt', 'hw2/expected_folder/10.json'),
    ('hw2/tests_folder/tes11.json', 'hw2/expected_folder/11.json'),
)


@pytest.mark.parametrize('input_path1, expected_path1', TEST_DIFFERENT_ARGUMENTS)
def test_diff_args(input_path1: str, expected_path1: str):
    """
    Test absolutly different arguments for the `hw2.process_data` function.

    Args:
        input_path1: Path to Input file.
        expected_path1: Path to file with expected data.
    """
    hw2.process_data(input_path1, PATH)

    with open(expected_path1) as expected_file:
        expected_data = json.load(expected_file)

    with open(PATH) as output_file:
        output_data = json.load(output_file)
    assert output_data == expected_data


@pytest.mark.parametrize('input_path, expected_path', TEST_WITHOUT_DIFFERENT_ARGUMENTS)
def test_no_args(input_path: str, expected_path: str):
    """Test wtih some missing arguments for the `hw2.process_data` function.

    Args:
        input_path: Path to Input file.
        expected_path: Path to file with expected data.
    """
    hw2.process_data(input_path, PATH)
    with open(expected_path) as expected_file:
        expected_data = json.load(expected_file)

    with open(PATH) as output_file:
        output_data = json.load(output_file)
    assert output_data == expected_data


@pytest.mark.parametrize('input_path, expected_path', TEST_WITH_WRONG_TYPE_VARIABLES)
def test_wrong_type(input_path: str, expected_path: str):
    """Test wtih wrong type variables for the `hw2.process_data` function.

    Args:
        input_path: Path to Input file.
        expected_path: Path to file with expected data.
    """
    hw2.process_data(input_path, PATH)

    with open(expected_path) as expected_file:
        expected_data = json.load(expected_file)

    with open(PATH) as output_file:
        output_data = json.load(output_file)
    assert output_data == expected_data


@pytest.mark.parametrize('input_path, expected_path', TEST_WITH_ERRORS)
def test_errors(input_path: str, expected_path: str):
    """Test wtih wrong type variables for the `hw2.process_data` function.

    Args:
        input_path: Path to Input file.
        expected_path: Path to file with expected data.
    """
    hw2.process_data(input_path, PATH)

    with open(expected_path) as expected_file:
        expected_data = json.load(expected_file)

    with open(PATH_ERROR) as output_file:
        output_data = json.load(output_file)
    assert output_data == expected_data
