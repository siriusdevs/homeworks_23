"""Those are tests for hw2 sollution."""
import json

import pytest

from hw2 import process_data

test1 = (
    ('data_hw2.json', 'out.json', 'example2.json'),
)

test2 = (
    ('test_data_hw2.json', 'out.json', 'example.json'),
)


@pytest.mark.parametrize('input_file, output_file, expected', test1)
def test_comparison_frst(input_file: str, output_file: str, expected: str) -> None:
    """Designed to test function with first example input data.

    Args:
        input_file: str with path to test data file.
        output_file: str with path to test output file.
        expected: str with path to precalculated correct data.

    """
    process_data(input_file, output_file)
    with open(output_file) as res:
        test_res = json.load(res)
    with open(expected) as exp:
        awaited = json.load(exp)
    assert test_res == awaited


@pytest.mark.parametrize('input_file, output_file, expected', test2)
def test_comparison_snd(input_file, output_file, expected):
    """Designed to test function with second example input data.

    Args:
        input_file: str with path to test data file.
        output_file: str with path to test output file.
        expected: str with path to precalculated correct data.

    """
    process_data(input_file, output_file)
    with open(output_file) as res:
        test_res = json.load(res)
    with open(expected) as exp:
        awaited = json.load(exp)
    assert test_res == awaited


@pytest.mark.xfail
def test_for_none_file():
    """Test that fails code by asking to read non-existing file."""
    assert process_data('non_exiting_file.json', 'new.json')


@pytest.mark.xfail
def test_for_empty_file():
    """Test that fails code by trying to read empty file."""
    assert process_data('empty.json', 'new.json')
