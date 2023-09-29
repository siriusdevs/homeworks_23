import pytest
from hw_1 import SalaryStats, get_salary_stats

# (args, kwargs, expected)
test_data = (
    (tuple(), {}, SalaryStats(maximum=0.0, average=0.0, median=0.0)),
)


@pytest.mark.parametrize('args, kwargs, expected', test_data)
def test_get_salary_stats(args, kwargs, expected):
    assert get_salary_stats(*args, **kwargs) == expected
