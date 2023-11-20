"""hw2 module tests."""


import json
from unittest.mock import MagicMock, mock_open, patch

import pytest

from hw2 import process_data

TEST_DATA_PATH = "hw2/tests/test_data.json"


def get_mock_output(mock_object: MagicMock) -> str:
    """Get mock output.

    Args:
        mock_object: mock object

    Returns:
        str: mock output
    """
    return "".join(
        [token.args[0] for token in mock_object().write.call_args_list],
    )


def prepare_test_data():
    """Prepare data for tests.

    Returns:
        list: list of mockups and answers
    """
    with open(TEST_DATA_PATH, "r") as test_data:
        tests = json.load(test_data)["tests"]
        return [
            (
                mock_open(read_data=json.dumps(test["test"])),
                json.dumps(test["answer"], indent=4),
            )
            for test in tests
        ]


@pytest.mark.parametrize("mockup, answer", prepare_test_data())
def test_process_data(mockup: MagicMock, answer: str):
    """Test process_data function.

    Args:
        mockup: mock object - loaded data from testfile
        answer: dict

    Asserts:
        True if the answer is correct
    """
    with patch("builtins.open", mockup):
        process_data("", "")
    assert get_mock_output(mockup) == answer
