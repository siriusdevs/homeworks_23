"""Testing top 3 salaries function."""
import pytest

from hw1 import top3_salaries

test_deps = (
    (
        (
            ('Dept', {'Krivenko': 1200}),
        ), None, ((('Dept', 1200.0),), (('Dept', 1200.0),)),
    ),
    (
        (
            ('nastyxa', {'Belov': 20000}),
        ), None, ((('nastyxa', 20000.0),), (('nastyxa', 20000.0),)),
    ),
    (
        (
            ('argun', {'grigoryan': 20000}),
        ), None, ((('argun', 20000.0),), (('argun', 20000.0),)),
    ),
)


@pytest.mark.parametrize('args, including, expected', test_deps)
def test_deps_salaries(
    args,
    including: tuple[str, ...],
    expected: tuple[tuple[str, float | int], tuple[str, float | int]],
) -> None:
    """Test top 3 salaries function.

    Args:
        args: tuple - data for tests with departments
        including: tuple - departments to be included
        expected: tuple - expected stats

    Return:
        state of answer - correct or not
    """
    assert top3_salaries(*args, including=including) == expected
