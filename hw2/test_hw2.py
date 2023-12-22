"""File with tests for hw2."""
import json
import os
import shutil

import pytest
import test_answers
import testcases
from hw2 import analyze_json


POSITIVE_TEST_ID = (
    (1, True),
    (2, True),
    (3, True),
)

NEGATIVE_TEST_ID = ((4, True), (5, True), (6, True), (7, True))


def create_file(subfolder: str, filename: str) -> str:
    """
    Create a new file in the specified subfolder.

    Args:
        subfolder: The directory where the file will be created.
        filename: The name of the file to be created.

    Returns:
        The path to the newly created file.

    This function checks if the subfolder exists, creates it if it doesn't, and then
    creates an empty file with the given filename within this subfolder.
    """
    file_path = os.path.join(subfolder, filename)
    if not os.path.exists(subfolder):
        os.makedirs(subfolder)

    with open(file_path, 'w') as new_file:
        new_file.write('')

    return file_path


def prepare_data(test_id: int, positive: bool = True) -> tuple[str, str]:
    """
    Prepare test data by writing it to a JSON file.

    Args:
        test_id: The identifier for the test.
        positive: Flag to determine if the test is positive or negative.

    Returns:
        A tuple containing the paths to the JSON file with test data and the result file.

    This function selects the test data based on the test_id and the nature of the test
    (positive or negative), writes it to a JSON file, and prepares a path for the result file.
    """
    test_data = testcases.positive_test_data[test_id] \
        if positive else testcases.negative_test_data[test_id]

    to_json = test_data
    path_to_json = create_file('./tests/', f'test_{test_id}.json')
    with open(path_to_json, 'w') as json_to_write:
        json_to_write.write(json.dumps(to_json))
    path_to_result = create_file('./tests/res/', f'res_{test_id}.json')

    return path_to_json, path_to_result


def get_result(path_to_result: str) -> str:
    """
    Read and return the content of a result file.

    Args:
        path_to_result: The path to the result file.

    Returns:
        The content of the result file as a string.
    """
    with open(path_to_result, 'r') as result_json:
        result_line = result_json.read()
    return result_line


def positive_tests(test_id: int) -> bool:
    """
    Execute positive tests based on provided test ID.

    Args:
        test_id: The identifier for the test case.

    Returns:
        A boolean indicating whether the test passed (True) or failed (False).
    """
    path_to_json, path_to_result = prepare_data(test_id)
    analyze_json(path_to_json, path_to_result)

    return get_result(path_to_result) == test_answers.test_answers[test_id]


def negative_tests(test_id: int) -> bool:
    """
    Execute negative tests based on provided test ID.

    Args:
        test_id: The identifier for the test case.

    Returns:
        A boolean indicating whether the test passed (True) or failed (False).

    This function expects the analyze_json function to raise a SystemExit
    exception for negative test cases. If the exception occurs, it checks the result.
    """
    path_to_json, path_to_result = prepare_data(test_id, positive=False)
    try:
        analyze_json(path_to_json, path_to_result)
    except SystemExit:
        return get_result(path_to_result) == test_answers.test_answers[test_id]


@pytest.mark.parametrize('test_id, expected', POSITIVE_TEST_ID)
def test_positive_hw2(test_id: int, expected: bool) -> None:
    """
    Test positive scenarios for homework 2.

    Args:
        test_id: The identifier for the test case.
        expected: The expected boolean outcome of the test.

    This function asserts whether the positive_tests function returns
    the expected outcome for each parameterized test case. After running
    the test, it cleans up the test environment.
    """
    assert positive_tests(test_id=test_id) == expected
    shutil.rmtree('./tests', ignore_errors=True)


@pytest.mark.parametrize('test_id, expected', NEGATIVE_TEST_ID)
def test_negative_hw2(test_id: int, expected: bool) -> None:
    """
    Test negative scenarios for homework 2.

    Args:
        test_id: The identifier for the test case.
        expected: The expected boolean outcome of the test.

    This function asserts whether the negative_tests function returns
    the expected outcome for each parameterized test case. After running
    the test, it cleans up the test environment.
    """
    assert negative_tests(test_id=test_id) == expected
    shutil.rmtree('./tests', ignore_errors=True)
