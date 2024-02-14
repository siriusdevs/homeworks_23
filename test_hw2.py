"""test for hw2.py."""
import json

import pytest

from hw2 import process_data

test_data = [('data_hw2.json', 'result_test_hw2.py', {
    'hosts_count': {
        'yandex.ru': 50.0,
        'gmail.com': 50.0,
    },
    'online_duration': {
        'Less than 2 days': 0,
        'Less than 1 week': 0,
        'Less than 1 month': 0,
        'Less than 6 months': 50.0,
        'More than 6 months': 50.0,
    },
},
),
]


@pytest.mark.parametrize('input_file, output_file, output_data', test_data)
def test_process_data(input_file, output_file, output_data):
    """Test for funck process_data.

    Args:
        input_file (str): _description_
        output_file (str): _description_
        output_data (dict): _description_
    """
    process_data(input_file_path=input_file, output_file_path=output_file)
    with open(output_file, 'r') as output:
        result_data = json.load(output)
    assert result_data == output_data
