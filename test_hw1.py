"""test for hw1.py."""
import pytest

from hw1 import top3

test_data = [
    (
        (
            ('Department 1', {'John Smith': 50000, 'Jane Doe': 60000}),
            ('Department 2', {'Alice Johnson': 70000, 'Bob Smith': 80000}),
            ('Department 3', {'Mike Brown': 90000, 'Emily Davis': 100000}),
        ),
        [['Department 3', 'Department 2', 'Department 1'],
         ['Department 1', 'Department 2', 'Department 3'],
         ],
    ),
    (
        (
            ('Department A', {'John Doe': 60000, 'Jane Smith': 50000}),
            ('Department B', {'Alice Davis': 80000, 'Bob Johnson': 70000}),
            ('Department C', {'Mike Smith': 100000, 'Emily Brown': 90000}),
        ),
        [['Department C', 'Department B', 'Department A'],
         ['Department A', 'Department B', 'Department C'],
         ],
    ),
]


@pytest.mark.parametrize('departments, expected_result', test_data)
def test_top3(departments, expected_result):
    """Test for funck top3.

    Args:
        departments (tuple): The departments for the test data.
        expected_result (list): The test date result of the funck.
    """
    result_data = top3(*departments)
    assert result_data == expected_result
