"""Test module for HW2."""
import json
import os

import pytest
from freezegun import freeze_time

from hw2 import InvalidFilePath, process_data

POSITIVE_TESTS = 'hw2/test_data/positive/'

MOCK_TIME = '2023-12-16 21:40:00'

TMP_USERS_DATA_FILE = 'tmp_users_data.json'
TMP_TESTS_DATA_FILE = 'tmp_test_data.json'


NEGATIVE_TESTS = (
    ('hw2/test_data/negative/invalid_age_type.json', TypeError),
    ('hw2/test_data/negative/invalid_age_value.json', ValueError),
    ('hw2/test_data/negative/invalid_date.json', ValueError),
    ('hw2/invalid_file_path.json.json', InvalidFilePath),
)


@freeze_time(MOCK_TIME)
def test_positive_tests():
    """Asserts that the processed user data corresponds to the test data."""
    for path in os.listdir(POSITIVE_TESTS):
        path_to_test_data = os.path.join(POSITIVE_TESTS, path)
        with open(path_to_test_data, 'r') as file_with_test:
            test_data = json.load(file_with_test)

        users = test_data['test_data']
        answer = test_data['answer']
        with open(TMP_TESTS_DATA_FILE, 'w') as users_file:
            json.dump(users, users_file)

        process_data(TMP_TESTS_DATA_FILE, TMP_USERS_DATA_FILE)

        assert os.path.exists(TMP_USERS_DATA_FILE)
        with open(TMP_USERS_DATA_FILE, 'r') as process_users:
            process_users = json.load(process_users)
            assert process_users == answer

    os.remove(TMP_USERS_DATA_FILE)
    os.remove(TMP_TESTS_DATA_FILE)


@pytest.mark.parametrize('input_file, expected', NEGATIVE_TESTS)
def test_invalid_age(input_file: str, expected: type):
    """Asserts that the test data raises exceptions.

    Args:
        input_file: str - path to input json file.
        expected: type - an exception that must be raised when the program is executed.
    """
    with pytest.raises(expected):
        process_data(input_file, TMP_TESTS_DATA_FILE)
