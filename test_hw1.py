"""Test module main."""


import pytest

from hw1 import salary_info

THE_COMPANY_DATA = (
    (
        (
            (
                'test1',
                {
                    'test1.1': 231.231,
                    'test1.2': 312.312,
                    'test1.3': 123.123,
                },
            ),
        ),
        ('a', 'b'),
        ['1: 123.12, 2: 231.23, 3: 312.31; 100.00%'],
    ),
    (
        (
            (
                'test2',
                {
                    'test2.1': 228.228,
                    'test2.2': 1337.337,
                },
            ),
        ),
        None,
        ['1: 228.23, 2: 1337.34, 3: 0.00; 100.00%'],
    ),
    (
        (
            (
                'test3',
                {
                    'test3.1': 228.228,
                    'test3.2': 1337.337,
                    'test3.3': 123.222,
                    'test3.4': 4321,
                    'test3.5': 1.111,
                },
            ),
        ),
        None,
        ['1: 1.11, 2: 123.22, 3: 228.23; 5.87%'],
    ),
    (
        (
            (
                'test4', {
                    'test4.1': 12.69,
                    'test4.2': 13.79,
                    'test4.3': 14.89,
                    'test4.4': 15.13,
                },
            ),
            (
                'test44', {
                    'test44.1': 250.19,
                    'test44.2': 198.4,
                    'test44.3': 50.44,
                    'test44.4': 100,
                },
            ),
        ),
        None,
        ['1: 12.69, 2: 13.79, 3: 14.89; 73.22%', '1: 50.44, 2: 100.00, 3: 198.40; 58.23%'],
    ),
    (
        (
            (
                'test5', {
                    'test5.1': 12.69,
                    'test5.2': 13.79,
                    'test5.3': 14.89,
                    'test5.4': 15.13,
                },
            ),
            (
                'test55', {
                    'test55.1': 250.19,
                    'test55.2': 198.4,
                    'test55.3': 50.44,
                    'test55.4': 100,
                },
            ),
        ),
        ('test55',),
        ['1: 12.69, 2: 13.79, 3: 14.89; 73.22%'],
    ),
    (
        (
            (
                'test66', {
                    'test6.1': 12.69,
                    'test6.2': 13.79,
                    'test6.3': 14.89,
                    'test6.4': 15.13,
                },
            ),
            (
                'test66', {
                    'test66.1': 250.19,
                    'test66.2': 198.4,
                    'test66.3': 50.44,
                    'test66.4': 100,
                },
            ),
        ),
        ('test6', 'test66'),
        [],
    ),
)


@pytest.mark.parametrize('sal_info, excluded, expected', THE_COMPANY_DATA)
def test_salary_stats(
    sal_info: tuple[str, dict[str, float]],
    excluded: tuple[str] | None,
    expected: list[str],
) -> None:
    """Test salary info function.

    Args:
        sal_info: tuple[str, dict[str, float]] - given parameter.
        excluded: tuple[str] - exluded parameter.
        expected: list[str] - expedcted parameter.

    Asserts:
        True if the answer is correct.
    """
    assert expected == salary_info(*sal_info, arg=excluded)
