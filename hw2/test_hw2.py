"""Module for testing the main file."""

import json

import pytest

from hw2 import process_data

test_data = {
    (
        './data_hw2.json',
        './hw2/test_result/test_1.json',
        './hw2/test_answer/answer_test_1.json',
    ),
    (
        './hw2/data_file/data_file_1.json',
        './hw2/test_result/test_2.json',
        './hw2/test_answer/answer_test_2.json',
    ),
    (
        './hw2/data_file/data_file_2.json',
        './hw2/test_result/test_3.json',
        './hw2/test_answer/answer_test_3.json',
    ),
    (
        './hw2/data_file/data_file_3.json',
        './hw2/test_result/test_4.json',
        './hw2/test_answer/answer_test_4.json',
    ),
}


@pytest.mark.parametrize('data_file_for_stats, output_file, expected', test_data)
def test_process_data(data_file_for_stats: str, output_file: str, expected: tuple):
    """_summary_.

    Args:
        data_file_for_stats (str): _description_
        output_file (str): _description_
        expected (tuple): _description_
    """
    process_data(data_file_for_stats, output_file)
    with open(output_file, 'r') as data_file_res:
        data_file_result = json.loads(data_file_res.read())
    with open(expected, 'r') as data_file_ans:
        data_file_answer = json.loads(data_file_ans.read())
    assert data_file_result == data_file_answer
