"""Those are tests for hw2 sollution."""
import json

import pytest

from hw2 import process_data

TEST_VALUES = 'input_file, output_file, expected'

test1 = (
    (
        'files_for_tests/DATA/data_hw2.json',
        'files_for_tests/RESULT/result.json',
        'files_for_tests/EXPECTED/expected.json',
    ),
)

test2 = (
    (
        'files_for_tests/DATA/data1_hw2.json',
        'files_for_tests/RESULT/result1.json',
        'files_for_tests/EXPECTED/expected1.json',
    ),
)

test3 = (
    (
        'files_for_tests/DATA/data2_hw2.json',
        'files_for_tests/RESULT/result2.json',
        'files_for_tests/EXPECTED/expected2.json',
    ),
)

test4 = (
    (
        'files_for_tests/DATA/data3_hw2.json',
        'files_for_tests/RESULT/result3.json',
        'files_for_tests/EXPECTED/expected3.json',
    ),
)


@pytest.mark.parametrize(TEST_VALUES, test1)
def test_comparison_valid_small(input_file: str, output_file: str, expected: str) -> None:
    """Designed to test function with 1 example input data.

    Args:
        input_file: str with path to test data file.
        output_file: str with path to test output file.
        expected: str with path to precalculated correct data.
    """
    process_data(input_file, output_file)
    with open(output_file) as res:
        test_result = json.load(res)
    with open(expected) as exp:
        expected_result = json.load(exp)
    assert test_result == expected_result


@pytest.mark.parametrize(TEST_VALUES, test2)
def test_comparison_valid_big(input_file, output_file, expected):
    """Designed to test function with 2 example input data.

    Args:
        input_file: str with path to test data file.
        output_file: str with path to test output file.
        expected: str with path to precalculated correct data.
    """
    process_data(input_file, output_file)
    with open(output_file) as res:
        test_resultult = json.load(res)
    with open(expected) as exp:
        expected_result = json.load(exp)
    assert test_resultult == expected_result


@pytest.mark.parametrize(TEST_VALUES, test3)
def test_comparison_unexsit(input_file, output_file, expected):
    """Designed to test function with 3 example input data.

    Args:
        input_file: str with path to test data file.
        output_file: str with path to test output file.
        expected: str with path to precalculated correct data.
    """
    process_data(input_file, output_file)
    with open(output_file) as res:
        test_result = json.load(res)
    with open(expected) as exp:
        expected_result = json.load(exp)
    assert test_result == expected_result


@pytest.mark.parametrize(TEST_VALUES, test4)
def test_comparison_empty(input_file, output_file, expected):
    """Designed to test function with 4 example input data.

    Args:
        input_file: str with path to test data file.
        output_file: str with path to test output file.
        expected: str with path to precalculated correct data.
    """
    process_data(input_file, output_file)
    with open(output_file) as res:
        test_result = json.load(res)
    with open(expected) as exp:
        expected_result = json.load(exp)
    assert test_result == expected_result
