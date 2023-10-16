"""Testing top 3 salaries function."""


import pytest

from hw1 import top3_salaries_stats

test_deps = (
    (
        {
            'Goggle': {
                'Larson': 200.0,
                'Simon': 400.0,
                'Vincent': 600.0,
            },
            'Tyndex': {
                'Nikolay': 800.0,
                'Alexey': 200.0,
                'Helen': 500.0,
            },
            'Spectacle': {
                'Thomas': 700.0,
                'Van': 50.0,
            },
        },
        (),
        (
            (('Tyndex', 500.0), ('Goggle', 400.0), ('Spectacle', 375.0)),
            (('Spectacle', 375.0), ('Goggle', 400.0), ('Tyndex', 500.0))
        ),
    ),
    (
        {
            'RED': {
                'Medic': 900.0,
                'Sniper': 500.0,
                'Demoman': 600.0,
            },
            'BLU': {
                'Soldier': 1800.0,
                'Heavy': 900.0,
                'Scout': 1100.0,
            },
            'GRN': {},
            'YLW': {
                'Engieneer': 300.0,
                'Spy': 50.0,
            },
            'GRY': {
                'Grey': 10000.0,
            },
        },
        (),
        (
            (('GRY', 10000.0), ('BLU', 1266.67), ('RED', 666.67)),
            (('GRN', 0), ('YLW', 175.0), ('RED', 666.67))
        ),
    ),
    (
        {
            'Funi Sound': {
                'Keith': 1,
                'Gigi': 2,
            },
            'Bright Purple': {
                'David': 3,
                'Mary': 4,
            },
            'Mercs': {
                'Patrick': 2,
                'Daniel': 2,
                'Nancy': 2,
            },
            'Crusher': {
                'Samuel': 5,
                'Peter': 0,
            },
            'Front Tier': {
                'John': 10,
                'Steve': 4,
                'Skittles': 1,
            },
            'Classics': {
                'William': 5,
                'Hector': 6,
                'Garry': 0,
            },
        },
        (
            'Bright Purple',
            'Classics',
        ),
        (
            (('Front Tier', 5.0), ('Crusher', 2.5), ('Mercs', 2.0)),
            (('Funi Sound', 1.5), ('Mercs', 2.0), ('Crusher', 2.5))
        ),
    ),
    (
        {
            'Drivers': {
                'Dennis': 1000.0,
                'Ivan': 200.0,
                'Alex': 0,
            },
            'Bodyguards': {
                'Andrew': 2000.0,
                'Vladislav': 100.0,
                'Vitaliy': 900.0,
            },
            'Salesmen': {
                'Nikita': 6000.0,
                'Peter': 2400.0,
                'Michael': 500.0,
            },
        },
        ('Salesmen'),
        (
            (('Bodyguards', 1000.0), ('Drivers', 400.0)),
            (('Drivers', 400.0), ('Bodyguards', 1000.0))
        ),
    ),
)


@pytest.mark.parametrize('departments, excluding, expected', test_deps)
def test_deps_salaries(
    departments: dict[str, dict[float | int]],
    excluding: tuple[str, ...],
    expected: tuple[tuple[str, float | int], tuple[str, float | int]],
) -> None:
    """Test top 3 salaries function.

    Args:
        departments: dict - data for tests
        excluding: tuple - departments to be excluded
        expected: tuple - expected stats

    Asserts:
        state of answer - correct or not
    """
    assert top3_salaries_stats(departments, excluding) == expected
