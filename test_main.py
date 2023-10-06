"""Test for hw1."""


import pytest

from main import company_departament

test_cases = (
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
            },
        },
        5.02,
        (
            ['second department', 'first department', 'third_department'],
            ['third_department', 'fifth department', 'fourth department'],
        ),
    ),
)


@pytest.mark.parametrize('departments, min_salary, expected', test_cases)
def test_salaries(
    departments: dict[str, dict[str, float]],
    min_salary: float,
    expected: tuple[list, list],
) -> None:
    """Test funcion for salaries.

    Args:
        min_salary: float | None = None.
        departments: dict[str, int] - dict of department names and values.
        expected: tuple - answer about salary.

    Asserts:
        True if the answer is correct.
    """
    assert company_departament(departments, min_salary) == expected
