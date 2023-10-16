"""Test for hw1."""


import pytest

from hw1 import company_departament

TEST_CASES = (
    (
        {
            'first_departament': {
                'Albert': 50000002150.81,
                'Fedor': 150384.57,
                'Egor': 100263.01,
            },
            'second_departament': {
                'Dima': 90560.53,
                'Matvey': 85600.03,
            },
            'third_departament': {
                'Vlad': 500.33,
                'Grisha': 1349.32,
            },
            'fourth_departament': {
                'Marko': 5.25,
                'Kaplan': 10450.01,
            },
            'fifth_departament': {
                'Arab': 374.09,
                'Hans': 899.57,
            },
            'sixth_department': {
                'Vika': 80900.55,
                'Max': 200500.91,
            },
        },
        20.05,
        (
            ['fifth_departament', 'third_departament', 'fourth_departament'],
            ['second_departament', 'sixth_department', 'first_departament'],
        ),
    ), (
        {
            'first department': {
                'Who': 0.01,
                'Tima': 200.54,
                'Clown': 0.09,
            },
            'second department': {
                'Alena': 90.58,
                'Adolf': 6.05,
            },
            'third_department': {
                'Sasha': 550.09,
            },
            'fourth department': {
                'Marko': 102506.22,
                'Matvey': 70230.22,
                'Fedor': 10049403.22,
            },
            'fifth department': {
                'Dima': 4950.11,
                'Vitaly': 50103.11,
            },
            'sixth department': {
                'Clown': 2.99,
                'Vlad': 340.02,
            },
        },
        5.02,
        (
            ['second department', 'first department', 'sixth department'],
            ['third_department', 'fifth department', 'fourth department'],
        ),
    ), (
        {}, 25.11, ([], []),
    ),
)


@pytest.mark.parametrize('departments, min_salary, expected', TEST_CASES)
def test_salaries(
    departments: dict[str, dict[str, float]],
    min_salary: float,
    expected: tuple[list, list],
) -> None:
    """Test funcion for salaries.

    Args:
        min_salary: float | None = None - minimum salary, which is compared with each department.
        departments: dict[str, dict] - dict of department names and values.
        expected: tuple - answer about salary.

    Asserts:
        True if the answer is correct.
    """
    assert company_departament(departments, min_salary) == expected


TEST_CASES2 = (
    (
        {
            'department1': {
                'Claus': 29.01,
                'Iren': 3402.35,
                'Arab': 48.94,
            },
            'department2': {
                'Vlad': 90.203,
                'Fedor': 5245.03,
                'Goblin': 484.24,
            },
            'department3': {
                'Alina': 940.21,
                'Sasha': 54.02,
                'Frogg': 5840.23,
            },
            'department4': {
                'Artem': 490.02,
                'Popit': 74.32,
                'SimpleDimple': 483.02,
            },
            'department5': {
                'Mops': 49304.35,
                'What': 473.45,
                'Where': 905.06,
            },
            'department6': {
                'Frog': 9430.03,
                'Who': 484.09,
                'Gannibal': 3893.04,
            },
        },
        (
            ['department4', 'department1', 'department2'],
            ['department3', 'department6', 'department5'],
        ),
    ), (
        {}, ([], []),
    ),
)


@pytest.mark.parametrize('departments, expected', TEST_CASES2)
def test_salaries2(
    departments: dict[str, dict[str, float]],
    expected: tuple[list, list],
) -> None:
    """Test funcion for salaries.

    Args:
        departments: dict[str, dict] - dict of department names and values.
        expected: tuple - answer about salary.

    Asserts:
        True if the answer is correct.
    """
    assert company_departament(departments) == expected
