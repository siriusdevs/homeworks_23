"""Testing top 3 salaries function."""


import pytest

from hw1 import top3_salaries

test_deps = (
    (
        (
            (
                'Dept1.1', {
                    'Krivenko': 12,
                    'Sheina': 5000000,
                    'Grigoryan': 10000,
                }
            ),
            (
                'Dept1.2', {
                    'Noskov': 1000,
                    'Kristev': 10,
                    'Strarcev': 200000,
                }
            ),
            (
                'Dept1.3', {
                    'Skutin': 25000,
                    'Tihonov': 7000000,
                    'Belov': 999999999999,
                }
            ),
        ),
        (),
        (
            (('Dept1.3', 333335674999.67), ('Dept1.1', 1670004.0), ('Dept1.2', 67003.33)),
            (('Dept1.2', 67003.33), ('Dept1.1', 1670004.0), ('Dept1.3', 333335674999.67)),
        ),
        (
            (
                'Dept2.1', {
                    'Morozov': 1300,
                    'Sokolov': 25500,
                    'Ivanov': 90,
                },
            ),
            (
                'Dept2.2', {
                    'Komarova': 45000,
                    'Lykov': 13500,
                    'Shubin': 42000,
                },
            ),
            (
                'Dept2.3', {
                    'Lebedev': 1000,
                    'Dubina': 5000,
                    'Fedorov': 14000,
                },
            ),
        ),
        ('Dept2.1', 'Dept2.2'),
        (
            (('Dept2.2', 33500.0), ('Dept2.1', 8963.33)),
            (('Dept2.1', 8963.33), ('Dept2.2', 33500.0)),
        ),
        (
            (
                'Dept3.1', {
                    'Petrova': 1300,
                    'Drozdov': 870,
                    'Zubov': 0,
                },
            ),
            (
                'Dept3.2', {
                    'Nikonov': 12000,
                    'Polyakova': 31000,
                    'Orlova': 10,
                },
            ),
        ),
        ('Dept999'),
        (
            (),
            (),
        ),
    ),
)


@pytest.mark.parametrize('args, including, expected', test_deps)
def test_deps_salaries(
    *args,
    including: tuple[str, ...],
    expected: tuple[tuple[str, float | int], tuple[str, float | int]],
) -> None:
    """Test top 3 salaries function.

    Args:
        args: tuple - data for tests with departments
        excluding: tuple - departments to be included
        expected: tuple - expected stats

    Asserts:
        state of answer - correct or not
    """
    assert top3_salaries(*args, including=including) == expected
