"""Tests for hw2.py."""
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
