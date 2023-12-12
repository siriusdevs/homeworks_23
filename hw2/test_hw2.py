"""Tests for homework about processing user data statistics."""

import os
import json
import pytest

from hw2 import process_data


def test_process_data():
    """
    Test the process_data function.
    """
    input_file_path = "../data_hw2.json"
    output_file_path = "./output_data.json"

    process_data(input_file_path, output_file_path)

    assert os.path.exists(output_file_path)

    with open(output_file_path, "r") as output_file:
        statistics = json.load(output_file)

    assert "age_percentages" in statistics
    assert "online_percentages" in statistics

    assert statistics["age_percentages"]["0-18"] == 50.0
    assert statistics["age_percentages"]["18-25"] == 0
    assert statistics["age_percentages"]["25-45"] == 50.0
    assert statistics["age_percentages"]["45-60"] == 0
    assert statistics["age_percentages"]["60+"] == 0

    assert statistics["online_percentages"]["<2 days"] == 0.0
    assert statistics["online_percentages"]["1 week"] == 0.0
    assert statistics["online_percentages"]["1 month"] == 0.0
    assert statistics["online_percentages"]["6 months"] == 50.0
    assert statistics["online_percentages"][">6 months"] == 50.0

    os.remove(output_file_path)


if __name__ == "__main__":
    pytest.main()
