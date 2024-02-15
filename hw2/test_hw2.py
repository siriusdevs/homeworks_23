import pytest
from hw2 import process_data


# файл с входными данными
input_path = 'input.json'
# файл с выхожными данными
output_path = 'output.json'

@pytest.mark.parametrize(
    'input_path, output_path, expected_value', 
    (('input.json', 'output.json', None),
     ('input2.json', 'output.json', None)
    )
)
def test_process_data(input_path, output_path, expected_value):
    assert process_data(input_path, output_path) == expected_value


@pytest.mark.parametrize(
    'input_path, output_path, expected_value',
    (('int.json',  'output.json', None),
     ('int2.json', 'output.json', None)
    )
)
def test_process_data_incorect_paths(input_path, output_path, expected_value):
    assert process_data(input_path, output_path) == expected_value
