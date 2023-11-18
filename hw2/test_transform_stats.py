"""Module for testing (transform_stats)'s functions."""

import pytest
import transform_stats

DATA_TEST_TRANSFORM_STATS: tuple[tuple[dict, int, dict], ...] = (
    (
        {
            'yandex': 2,
            'mail.ru': 3,
        },
        5,
        {
            'yandex': 40.0,
            'mail.ru': 60.0,
        },
    ),
    (
        {},
        0,
        {},
    ),
)

DATA_TEST_TRANSFORM_STATS_INCORRECT: tuple[dict[str, int], ...] = (
    {
        'cat.ru': 0,
        'xes.ru': 0,
    },
    {},
)


@pytest.mark.parametrize('stats, sum_count, expected', DATA_TEST_TRANSFORM_STATS)
def test_transform_stats(stats: dict[str, int], sum_count: int, expected: dict) -> None:
    """Test transform stats.

    Args:
        stats (dict[str, int]): dictionary that has int values in its field.
        sum_count (int): the count of all registered entity.
        expected (dict): dictionary that has percents value in its field.
    """
    assert transform_stats.transform_stats(stats, sum_count) == expected


@pytest.mark.parametrize('stats', DATA_TEST_TRANSFORM_STATS_INCORRECT)
@pytest.mark.xfail(raises=transform_stats.SumCountEqualsZeroForNoneEmpty)
def test_transform_stats_incorrect(stats: dict[str, int]) -> None:
    """Test transform stats incorrect values.

    Args:
        stats (dict[str, int]): dictionary that has int values in its field.
    """
    transform_stats.transform_stats(stats)
