import pytest
import json
from hw2 import process_data


test_data = [('data_hw2.json', 'result_test_hw2.py', {
    "hosts_count": {
        "yandex.ru": 50.0,
        "gmail.com": 50.0
    },
    "online_duration": {
        "Less than 2 days": 0.0,
        "Less than 1 week": 0.0,
        "Less than 1 month": 0.0,
        "Less than 6 months": 50.0,
        "More than 6 months": 50.0
    }
})]


@pytest.mark.parametrize("input_file, output_file, data", test_data)
def test_process_data(input_file, output_file, data):
    process_data(input_file_path=input_file, output_file_path=output_file)
    with open(output_file, 'r') as output_data:
        result = json.load(output_data)
    assert result == data
