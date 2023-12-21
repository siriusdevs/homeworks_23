"""Tests for hw2.py."""
import json
import os

from hw2 import process_data


def test_file_not_found():
    """Test for FileNotFoundError."""
    assert process_data('vydumanniy_file.json', 'test_output.json') == 1


def test_file_not_json():
    """Test for json.decoder.JSONDecodeError."""
    assert process_data('./HW2/input/decoderError.json', 'test_output.json') == 2


def test_output_file_not_found():
    """Test for FileNotFoundError."""
    assert process_data('./HW2/input/data_hw2.json', '/nesuchestvuyushaya_papka/1/1/1/1.json') == 3


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
