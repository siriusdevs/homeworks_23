"""Testing module for hw2."""

import json

import pytest

import hw2

TEST_PROCESS_DATA = (
    (
        'input/data_hw2.json',
        'output/output_data_hw2.json',
        'expected/expected_data_hw2.json',
    ),
    (
        'input/clients.json',
        'output/output_clients.json',
        'expected/expected_clients.json',
    ),
    (
        'input/clients2.json',
        'output/output_clients2.json',
        'expected/expected_clients2.json',
    ),
    (
        'input/unfinished.json',
        'output/output_unfinished.json',
        'expected/expected_unfinished.json',
    ),
)

TEST_EXIST_FILE = (
    (
        'input/gdz.json',
        'output/result.json',
    ),
    (
        'input/reshalka.json',
        'output/result.json',
    ),
)

TEST_EMPTY_FILE = (
    (
        'input/empty.json',
        'output/stat.json',
    ),
    (
        'input/nothing.json',
        'output/stat.json',
    ),
)

TEST_EXTENSION = (
    (
        'input/input.txt',
        'output/output.json',
    ),
    (
        'input/clients.json',
        'output/output.txt',
    ),
)

TEST_WRONG_JSON = (
    (
        'input/wrong.json',
        'output/output.json',
    ),
    (
        'input/broken.json',
        'output/output.json',
    ),
)


@pytest.mark.parametrize('input_path, output_path, expected_path', TEST_PROCESS_DATA)
def test_process_data(input_path: str, output_path: str, expected_path: str) -> None:
    """
    Test function for correct outputs.

    Args:
        input_path (str): The input JSON file.
        output_path (str): The output JSON file with output results.
        expected_path (str): The path to JSON file with expected results.
    """
    hw2.process_data(input_path, output_path)

    with open(expected_path, 'r') as expected_file:
        expected = json.load(expected_file)

    with open(output_path, 'r') as output_file:
        output = json.load(output_file)

    assert output == expected


@pytest.mark.parametrize('input_file, output_file', TEST_EXIST_FILE)
def test_exist_file(input_file: str, output_file: str) -> None:
    """
    Test function for exists input JSON files.

    Args:
        input_file(str): The input JSON file.
        output_file (str): The JSON file with output results.
    """
    with pytest.raises(ValueError):
        hw2.process_data(input_file, output_file)


@pytest.mark.parametrize('input_file, output_file', TEST_EMPTY_FILE)
def test_empty_file(input_file: str, output_file: str) -> None:
    """
    Test function for empty input JSON files.

    Args:
        input_file (str): The input JSON file.
        output_file (str): The JSON file with output results.
    """
    with pytest.raises(ValueError):
        hw2.process_data(input_file, output_file)


@pytest.mark.parametrize('input_file, output_file', TEST_EXTENSION)
def test_extension(input_file: str, output_file: str) -> None:
    """
    Test function for extensions JSON of input and output files.

    Args:
        input_file (str): The input path to JSON file.
        output_file (str): The output path to JSON file with output results.
    """
    with pytest.raises(TypeError):
        hw2.process_data(input_file, output_file)


@pytest.mark.parametrize('input_path, output_path', TEST_WRONG_JSON)
def test_wrong_json(input_path: str, output_path: str) -> None:
    """
    Test function for incorrect JSON files.

    Args:
        input_path (str): The input path to JSON file.
        output_path (str): The output path to JSON file with output results.
    """
    with pytest.raises(ValueError):
        hw2.process_data(input_path, output_path)
