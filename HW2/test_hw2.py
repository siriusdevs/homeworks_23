import pytest

import json

import os

from HW2.hw2 import process_data

def test_process_data():
    test_data = {
        "client1": {"age": 20, "last_login": "2022-01-01"},
        "client2": {"age": 30, "last_login": "2022-02-01"},
        "client3": {"age": 40, "last_login": "2022-03-01"},
    }

    with open("test_data.json", "w") as f:
        json.dump(test_data, f)


    process_data("test_data.json", "test_result.json")


    with open("test_result.json", "r") as f:
        result = json.load(f)


    assert result["age_percentages"] == [0.0, 33.33, 33.33, 33.33, 0.0]
    assert result["last_online_percentages"] == [100.0, 0.0, 0.0, 0.0, 0.0]
    
    os.remove("test_data.json")
    os.remove("test_result.json")


def test_example():
    """Test for example."""
    process_data('./HW2/input/data_hw2.json', './HW2/output/test_output.json')
    with open('./HW2/output/test_output.json', 'r') as output_file:
        output_dict = json.load(output_file)
        assert output_dict == {
            'age_stats': {
                '0-18': 0,
                '18-25': 1,
                '25-45': 1,
                '45-60': 0,
                '60+': 0,
            },
            'last_login_stats': {
                'less2days': 0,
                'less1week': 0,
                'less1month': 0,
                'less6months': 1,
                '6months+': 1,
            },
        }

    os.remove('./HW2/output/test_output.json')
