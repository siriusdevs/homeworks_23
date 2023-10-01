'''Test module for function top_salary from hw1.py'''
import pytest
from hw1 import top_salary

data = (
    (
        ([], None), ([], 0),
    ),
    (
        (
            [('Teachers', [5000.00, 5500.50, 6000.75])],
            None,
        ),
        (
            [6000.75, 5500.5, 5000.0,],
            100.0,
        ),
    ),
    (
        (
            [
                ('Church', [5000.00, 5500.50, 6000.75]),
                ('Deanery', [7000.25, 7200.30, 7500.50]),
                ('IT', [6000.00, 6200.00, 6500.00]),
            ],
            None,
        ),
        (
            [7500.5, 7200.3, 7000.25],
            38.14,
        ),
    ),
)


@pytest.mark.parametrize('company, expected', data)
def test_top_salary(company, expected):
    result = top_salary(*company[0])
    assert result[0] == expected[0]
    assert result[1] == expected[1]
