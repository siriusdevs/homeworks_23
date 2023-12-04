"""Module for testing (increment_field)'s functions."""

import increment_field
import pytest

DATA_TEST_INCREMENT_FIELD: tuple[tuple[dict, str, dict], ...] = (
    (
        {
            'a': 1,
        },
        'a',
        {
            'a': 2,
        },
    ),
    (
        {
            'b': 1,
        },
        'c',
        {
            'b': 1,
            'c': 1,
        },
    ),
)


@pytest.mark.parametrize('dictionary, field, expected', DATA_TEST_INCREMENT_FIELD)
def test_increment_field(dictionary: dict[str, int], field: str, expected: dict[str, int]) -> None:
    """Test function increment field.

    Args:
        dictionary (dict[str, int]): given dictionary with element's count in field.
        field (str): dictionary's field key.
        expected (dict[str, int]): dictionary with incremented field.
    """
    increment_field.increment_field(dictionary, field)
    assert dictionary == expected
