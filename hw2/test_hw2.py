"""Test the process_data function."""
import json
from unittest.mock import MagicMock, mock_open, patch

import pytest

from hw2 import process_data

TEST_DATA_PATH = 'test_data.json'


def _get_mock_output(mock_object: MagicMock) -> str:
    """Extract the written content from the mock object.

    Args:
        mock_object (MagicMock): Mock object with write calls.

    Returns:
        str: Concatenated content of write calls.
    """
    return ''.join(
        [token.args[0] for token in mock_object().write.call_args_list],
    )


def _prepare_test_data():
    """Read test data from the file and prepare it for parameterization.

    Returns:
        list: List of tuples containing mock objects and expected answers.
    """
    with open(TEST_DATA_PATH, 'r') as test_data:
        tests = json.load(test_data)['tests']
        return [
            (
                mock_open(read_data=json.dumps(test['test'])),
                json.dumps(test['answer'], indent=4),
            )
            for test in tests
        ]


@pytest.mark.parametrize('mockup, answer', _prepare_test_data())
def test_process_data(mockup: MagicMock, answer: str):
    """Test the process_data function.

    Args:
        mockup (MagicMock): Mock object with loaded data from a test file.
        answer (str): Expected output in JSON format.

    Asserts:
        True if the actual output matches the expected answer.
    """
    with patch('builtins.open', mockup):
        process_data()
    assert _get_mock_output(mockup) == answer
