"""Test module for HW2."""
import json
import os

from freezegun import freeze_time

from hw2 import process_data

POSITIVE_TESTS = 'hw2/test_data/positive/'
NEGATIVE_TESTS = 'hw2/test_data/negative/'

MOCK_TIME = '2023-12-16 21:40:00'

TMP_USERS_DATA_FILE = 'tmp_users_data.json'
TMP_TESTS_DATA_FILE = 'tmp_test_data.json'


def _test_aggregate_users_stats(path_to_tests: str):
    for path in os.listdir(path_to_tests):
        path_to_test_data = os.path.join(path_to_tests, path)
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


@freeze_time(MOCK_TIME)
def test_positive_tests():
    """Asserts that the processed user data corresponds to the test data."""
    _test_aggregate_users_stats(POSITIVE_TESTS)


@freeze_time(MOCK_TIME)
def test_negative_tests():
    """Asserts that the test data contains an error."""
    _test_aggregate_users_stats(NEGATIVE_TESTS)
