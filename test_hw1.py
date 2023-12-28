import pytest
from hw1 import statistics

TEST_DATA = (
    (
        (
            ('first_division', {'Ana': 2468.0, 'Sasha': 5673.9, 'Retyzia': 7654.6}),
            ('second_division', {'Katya': 28868.0, 'Welly': 387.4, 'Ilya': 4234.1}),
            ('third_division', {'Alla': 24511.3, 'Tonya': 61173.9, 'Denis': 222.6}),
            ('fourth_division', {'Roma': 4118.5, 'Sonya': 7233.7, 'John': 4277.2}),
            ('fifth_division', {'Marusya': 5000.2, 'Polina': 9999.1, 'Kirill': 4567.8}),
            ('sixth_division', {'Masha': 5222.2, 'Popi': 199.1, 'Nikita': 422.8}),
        ),
        None,
        ([61173.9, 28868.0, 24511.3], 65.0)
    ),
)


@pytest.mark.parametrize("divisions, lim, expected", TEST_DATA)
def test_statistics_1(divisions, lim, expected):
    """Test funcion of statistics.

    Args:
        divisions: tuple[str, dict[str, float]]
        limit: float | None = None
        expected: tuple[list, float]
    Asserts:
        True if the answer is correct.
    """
    assert statistics(*divisions, lim=lim) == expected


TEST_DATA1 = (
    (
        (
            ('first_division', {'Ana': 2345.0, 'Sasha': 756.0, 'Retyzia': 74366.6}),
            ('second_division', {'Katya': 345.6, 'Welly': 23366.9, 'Ilya': 4.6}),
            ('third_division', {'Alla': 2221.3, 'Tonya': 1143.5, 'Denis': 2345.4}),
            ('fourth_division', {'Roma': 223.6, 'Sonya': 343.2, 'John': 4447.6}),
            ('fifth_division', {'Marusya': 5033.2, 'Polina': 23459.1, 'Kirill': 45675.8}),
            ('sixth_division', {'Masha': 52552.2, 'Popi': 19239.1, 'Nikita': 6666.8}),
        ),
        5000.0,
        (([74366.6, 52552.2, 45675.8], 68.94)),
    ),
)


@pytest.mark.parametrize("divisions, lim, expected", TEST_DATA1)
def test_statistics(divisions, lim, expected) -> None:
    """Test funcion of statistics.

    Args:
        divisions: tuple[str, dict[str, float]]
        limit: float | None = None
        expected: tuple[list, float]
    Asserts:
        True if the answer is correct.
    """
    assert statistics(*divisions, lim=lim) == expected
