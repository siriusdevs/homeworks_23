"""Tests for homework about processing user data statistics."""

import json
import os

from hw2 import calculate_percentages, process_data

age_percentages = 'age_percentages'
online_percentages = 'online_percentages'
input_file_path = 'data_hw2.json'
output_file_path = 'output_data.json'
invalid_input_file = 'nonexistent_file.json'
age_mapping = {'0-18': 50.0, '18-25': 0, '25-45': 50.0, '45-60': 0, '60+': 0}
online_mapping = {'<2 days': 0, '1 week': 0, '1 month': 0, '6 months': 50.0, '>6 months': 50.0}


def test_process_data():
    """Test the process_data function."""
    process_data(input_file_path, output_file_path)

    assert os.path.exists(output_file_path)

    with open(output_file_path, 'r') as output_file:
        statistics = json.load(output_file)

    assert all(
        statistics[age_percentages][age] == expected for age, expected in age_mapping.items()
    )
    assert all(
        statistics[online_percentages][day] == expected for day, expected in online_mapping.items()
    )

    os.remove(output_file_path)


def test_process_data_invalid_input_file():
    """Test the process_data function for invalid input file."""
    incorrect_path = invalid_input_file
    answer = process_data(incorrect_path, output_file_path)
    assert answer == {'msg': 'Input file not found'}


def test_calculate_percentages():
    """Test the calculate_percentages function."""
    counts = {'0-18': 10, '18-25': 20, '25-45': 30, '45-60': 20, '60+': 20}
    total = sum(counts.values())

    expected = {cat: (count / total) * 100 for cat, count in counts.items()}

    actual = calculate_percentages(counts, total)

    assert actual == expected
