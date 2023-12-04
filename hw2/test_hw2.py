"""Those are tests for hw2 sollution."""
import json

import pytest

from hw2 import process_data

OUT_FILE = 'out.json'
TEST_VALUES = 'input_file, output_file, expected'

test1 = (
    ('files/data_hw2.json', OUT_FILE, 'files/example2.json'),
)

test2 = (
    ('files/test_data_hw2.json', OUT_FILE, 'files/example.json'),
)

test3 = (
    ('files/unexistant.json', OUT_FILE, 'files/example_error.json'),
)

test4 = (
    ('files/empty.json', OUT_FILE, 'files/example_error.json'),
)


@pytest.mark.parametrize(TEST_VALUES, test1)
def test_comparison_valid_small(input_file: str, output_file: str, expected: str) -> None:
    """Designed to test function with first example input data.

    Args:
        input_file: str with path to test data file.
        output_file: str with path to test output file.
        expected: str with path to precalculated correct data.
    """
    process_data(input_file, output_file)
    with open(output_file) as res:
        test_res = json.load(res)
    with open(expected) as exp:
        awaited = json.load(exp)
    assert test_res == awaited


@pytest.mark.parametrize(TEST_VALUES, test2)
def test_comparison_valid_big(input_file, output_file, expected):
    """Designed to test function with second example input data.

    Args:
        input_file: str with path to test data file.
        output_file: str with path to test output file.
        expected: str with path to precalculated correct data.
    """
    process_data(input_file, output_file)
    with open(output_file) as res:
        test_res = json.load(res)
    with open(expected) as exp:
        awaited = json.load(exp)
    assert test_res == awaited


@pytest.mark.parametrize(TEST_VALUES, test3)
def test_comparison_unexsit(input_file, output_file, expected):
    """Designed to test function with second example input data.

    Args:
        input_file: str with path to test data file.
        output_file: str with path to test output file.
        expected: str with path to precalculated correct data.
    """
    process_data(input_file, output_file)
    with open(output_file) as res:
        test_res = json.load(res)
    with open(expected) as exp:
        awaited = json.load(exp)
    assert test_res == awaited


@pytest.mark.parametrize(TEST_VALUES, test4)
def test_comparison_empty(input_file, output_file, expected):
    """Designed to test function with second example input data.

    Args:
        input_file: str with path to test data file.
        output_file: str with path to test output file.
        expected: str with path to precalculated correct data.
    """
    process_data(input_file, output_file)
    with open(output_file) as res:
        test_res = json.load(res)
    with open(expected) as exp:
        awaited = json.load(exp)
    assert test_res == awaited
