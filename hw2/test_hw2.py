"""Module for testing hw2.py."""


import json

import hw2_exceptions
import pytest

from hw2 import process_data

valid_test_data = (
    (
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/valid_data/input_data/input_1.json',
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/valid_data/output_data/output_1.json',
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/expected_data/expected_1.json',
    ),
    (
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/valid_data/input_data/input_2.json',
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/valid_data/output_data/output_2.json',
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/expected_data/expected_2.json',
    ),
    (
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/valid_data/input_data/input_3.json',
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/valid_data/output_data/output_3.json',
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/expected_data/expected_3.json',
    ),
    (
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/valid_data/input_data/input_4.json',
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/valid_data/output_data/output_4.json',
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/expected_data/expected_4.json',
    ),
    (
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/valid_data/input_data/input_5.json',
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/valid_data/output_data/output_5.json',
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/expected_data/expected_5.json',
    ),
)

invalid_test_data = (
    (123, '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/valid_data/output_data/output_1.json'),
    (
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/invalid_data/not_json.txt',
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/valid_data/output_data/output_1.json',
    ),
    (
        'non_existent_file.json',
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/valid_data/output_data/output_1.json',
    ),
    (
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/invalid_data/empty.json',
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/valid_data/output_data/output_1.json',
    ),
    (
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/invalid_data/input_1.json',
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/valid_data/output_data/output_1.json',
    ),
    (
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/invalid_data/input_2.json',
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/valid_data/output_data/output_1.json',
    ),
    (
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/invalid_data/input_3.json',
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/valid_data/output_data/output_1.json',
    ),
    (
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/invalid_data/input_4.json',
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/valid_data/output_data/output_1.json',
    ),
    (
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/invalid_data/input_5.json',
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/valid_data/output_data/output_1.json',
    ),
    (
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/invalid_data/input_6.json',
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/valid_data/output_data/output_1.json',
    ),

    ('/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/valid_data/input_data/input_1.json', 123),
    (
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/valid_data/input_data/input_1.json',
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/invalid_data/not_json.txt',
    ),
    (
        '/media/ilya/KINGSTON/homeworks_/homeworks_23/hw2/test_data/IO_data/valid_data/input_data/input_1.json',
        'non_existent_file.json',
    ),
)


@pytest.mark.parametrize('input_file_path, output_file_path, expected', valid_test_data)
def test_process_data(input_file_path: str, output_file_path: str, expected: tuple):
    """Test process_data function from hw2.py.

    Args:
        input_file_path (str): path to the input json file.
        output_file_path (str): path to the output json file.
        expected (tuple): expected data.
    """
    process_data(input_file_path, output_file_path)
    with open(output_file_path, 'r') as output_file:
        output_data = json.loads(output_file.read())
    with open(expected, 'r') as expected_file:
        expected_data = json.loads(expected_file.read())
    assert output_data == expected_data


@pytest.mark.xfail(raises=TypeError)
def test_input_file_path_not_str():
    """Test the error for the fact that the input file path is not str."""
    process_data(*invalid_test_data[0])


@pytest.mark.xfail(raises=hw2_exceptions.FileIsNotJsonError)
def test_input_file_extension_other_than_json():
    """Test the error for the fact that the input file has a extension other than .json."""
    process_data(*invalid_test_data[1])


@pytest.mark.xfail(raises=FileNotFoundError)
def test_input_file_not_found():
    """Test the error for the fact that the input file was not found."""
    process_data(*invalid_test_data[2])


@pytest.mark.xfail(raises=hw2_exceptions.FileIsEmptyError)
def test_input_file_empty():
    """Test the error for the fact that the input file is empty."""
    process_data(*invalid_test_data[3])


@pytest.mark.xfail(raises=TypeError)
def test_user_data_not_dict():
    """Test the error for the fact that the user_data is not a dict."""
    process_data(*invalid_test_data[4])


@pytest.mark.xfail(raises=TypeError)
def test_user_char_not_int_or_str():
    """Test the error for the fact that the user_char is not an int or str."""
    process_data(*invalid_test_data[5])


@pytest.mark.xfail(raises=IndexError)
def test_number_user_chars_not_equal():
    """Test the error for the fact that the number of user characteristics \
        is not equal to len_valid_chars."""
    process_data(*invalid_test_data[6])


@pytest.mark.xfail(raises=ValueError)
def test_user_char_invalid_name():
    """Test the error for the fact that user characteristic name has an invalid name."""
    process_data(*invalid_test_data[7])


@pytest.mark.xfail(raises=TypeError)
def test_user_char_not_str():
    """Test the error for the fact that the user_char is not a str."""
    process_data(*invalid_test_data[8])


@pytest.mark.xfail(raises=TypeError)
def test_user_char_not_int():
    """Test the error for the fact that the user_chars[-1] is not a int."""
    process_data(*invalid_test_data[9])


@pytest.mark.xfail(raises=TypeError)
def test_output_file_path_not_str():
    """Test the error for the fact that the output file path is not str."""
    process_data(*invalid_test_data[10])


@pytest.mark.xfail(raises=hw2_exceptions.FileIsNotJsonError)
def test_output_file_extension_other_than_json():
    """Test the error for the fact that the output file has a extension other than .json."""
    process_data(*invalid_test_data[11])


@pytest.mark.xfail(raises=FileNotFoundError)
def test_output_file_not_found():
    """Test the error for the fact that the output file was not found."""
    process_data(*invalid_test_data[12])
