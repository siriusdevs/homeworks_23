"""Testing for module 'top_departments' from hw1."""
import pytest

from hw1 import top_departments

DATA1 = {
    'development': {
        'Egor': 120000,
        'Matvey': 175000,
        'Juliana': 80000,
        'Petr': 20000.5,
    },
    'system_administration': {
        'Danil': 96000.6,
        'Diana': 50000,
        'Ivan': 15000.7,
        'Anastasia': 23000.3,
    },
    'information_security': {
        'Alex': 30000.1,
        'Asia': 110000.8,
        'Daniil': 15000.4,
        'Jacqueline': 126000.9,
    },
    'support_specialist': {'Artem': 49800.6, 'Sergei': 67839, 'Maria': 51078.7},
    'hr': {'Ekaterina': 79456.9, 'Rima': 34256, 'Boris': 109674.3, 'Vladimir': 9810.52},
    'accounting': {'Rina': 56734.9, 'Oleg': 87350, 'Konstantin': 27459.96},
}

DATA2 = {
    'department1': {
        'worker1': 34598.8,
        'worker2': 34567.09,
        'worker3': 3263430.38,
        'worker4': 1423749.567,
    },
    'department2': {
        'worker5': 204383.63,
        'worker6': 35278.937,
        'worker7': 236282,
        'worker8': 53839.5839,
    },
    'department3': {'worker9': 134529.0638, 'worker10': 74940.098},
    'department4': {'worker11': 546389, 'worker12': 54637.098, 'worker13': 243598.548},
    'department5': {
        'worker14': 243637.78,
        'worker15': 3527.95,
        'worker16': 5364.064,
        'worker17': 64759,
    },
    'department6': {'worker18': 245667, 'worker19': 456798, 'worker20': 456782},
    'department7': {'worker21': 456789, 'worker22': 62930.69, 'worker23': 98280},
    'department8': {
        'worker24': 453638,
        'worker25': 4262892.046,
        'worker26': 2368.09,
        'worker27': 123409.3487,
    },
}

DATA3 = {
    'sales': {'worker1': 56789.367, 'worker2': 93738.63783, 'worker3': 473930.838},
    'arts': {'worker4': 647399.9, 'worker5': 28339.937},
    'architecture': {
        'worker6': 87434.98,
        'worker7': 2898976.345,
        'worker8': 975579,
        'worker9': 256809.5567,
    },
    'programming': {'worker10': 749840.098},
    'training': {'worker11': 132679.938, 'worker12': 45678.098},
    'dance': {'worker13': 45678.08, 'worker14': 234598.57},
    'smm': {'worker15': 348527.95, 'worker16': 12380.064, 'worker17': 234560},
    'ecology': {'worker18': 134567.456},
}

DATA4 = {}

LIMIT1 = 100000

LIMIT2 = 535000

LIMIT3 = 20000

EXPECTED_DATA1 = (
    ['development', 'information_security', 'hr'],
    ['system_administration', 'support_specialist', 'accounting'],
)

EXPECTED_DATA2 = (
    ['department8', 'department1', 'department6'],
    ['department5', 'department3', 'department2'],
)

EXPECTED_DATA3 = ([], [])

EXPECTED_DATA4 = (
    ['accounting', 'support_specialist', 'development'],
    ['information_security', 'hr', 'system_administration'],
)

EXPECTED_DATA5 = (
    ['department6', 'department7', 'department8'],
    ['department1', 'department5', 'department3'],
)

EXPECTED_DATA6 = (['smm'], ['smm'])

test_all_departments = (
    (DATA1, EXPECTED_DATA1, None),
    (DATA2, EXPECTED_DATA2, None),
    (DATA4, EXPECTED_DATA3, None),
    (DATA1, EXPECTED_DATA4, LIMIT1),
    (DATA2, EXPECTED_DATA5, LIMIT2),
    (DATA3, EXPECTED_DATA6, LIMIT3),
)


@pytest.mark.parametrize('departments, expected, limit', test_all_departments)
def test_top_departments(
    departments: dict[str, dict],
    expected: tuple,
    limit: float | None,
):
    """Test detective function with test_all_departments.

    Args:
        departments: dict - list of all departments, their employees and their salaries.
        limit: float - the num limit above which salaries are not taken, default (None).
        expected: dict - an actual expected result.

    Asserts:
        True if the function returns expected results.

    """
    assert top_departments(departments, limit) == expected
