"""get_top_salaries function test module."""

import pytest

from hw1 import get_top_salaries

TEST_DATA_WITHOUT_DEPARTMENTS = (
    # Обычные ожидаемые входные данные
    ((('Develop', [1000, 200, 500]),
      ('Marketing', [400, 600, 300]),
      ('Sales', [500, 700, 100]),
      ),
     ([100, 200, 300], 13.95),
     ),
    # Передана лишь 1 зарплата
    ((('Dev', [20]),),
     ([20], 100.0),
     ),
    # Самые низкие зарплаты равны
    ((('Develop', [20, 20, 20, 80, 20]),
      ('Marketing', [20, 20, 20, 80, 20]),
      ('Sales', [20, 20, 20, 80, 20]),
      ),
     ([20, 20, 20], 12.5),
     ),
    # Указан отдел и единственная зарплата, равная 0 - все ок, работаем
    ((('Dev', [0]),),
     ([0], 100.0),
     ),
    # Не переданы аргументы - игнорируем
    ((), ([], 0)),
)
TEST_DATA_WITH_DEPARTMENTS = (
    # Считаем зарплаты только с отделов Develop и Sales
    ((('Programmers', [1000, 200, 500]),
     ('DB', [400, 600, 300]),
     ('Analys', [500, 700, 100]),
      ),
     ('Programmers', 'Analys'),
     ([100, 200, 500], 26.67),
     ),
    # Одного из указанных отделов не существует - считаем только существующий (или выдаем ошибку?)
    ((('', [1000, 200, 500]),
     ('456', [400, 600, 300]),
     ('789', [500, 700, 100]),
      ),
     ('123', '789'),
     ([100, 500, 700], 100.0),
     ),
    # Передан пустой кортеж отделов - считаем все отделы
    ((('abc', [1000, 200, 500]),
     ('def', [400, 600, 300]),
     ('ghi', [500, 700, 100]),
      ),
     (),
     ([100, 200, 300], 13.95),
     ),
)
TEST_DATA_WITH_WRONG_VALUES = (
    ((('Develop', [80, 80, 80, -20, 80]),
      ('Marketing', [80, 80, 80, -20, 80]),
      ('Sales', [80, 80, 80, -20, 80, 80]),
      ),
     ),
    ((()), ([], 0)),
    ((('Dev',),)),
    ((([10, 20, 20, 80, 20],),
      ('Market', [20, 20, 20, 80, 20]),
      ('Sale', [20, 20, 20, 80, 20]),
      ),
     ),
    (((),), ('abc', 'ghi')),
)


@pytest.mark.parametrize('deps, expected', TEST_DATA_WITHOUT_DEPARTMENTS)
def test_get_top_salaries_without_departments(deps: tuple, expected: tuple):
    """Test get_top_salaries function with departments argument.

    Args:
        deps: tuple - tuples with name of departments and list of salaries.
        expected: tuple - expected function result.
    """
    assert get_top_salaries(*deps) == expected


@pytest.mark.parametrize('deps, req_deps, expected', TEST_DATA_WITH_DEPARTMENTS)
def test_get_top_salaries_with_departments(deps: tuple, req_deps: tuple[str], expected: tuple):
    """Test get_top_salaries function with departments argument.

    Args:
        deps: tuple - tuples with name of departments and list of salaries.
        req_deps: tuple - inside is a tuple of departments names whose salaries need to be counted.
        expected: tuple - expected function result.
    """
    assert get_top_salaries(*deps, required_deps=req_deps) == expected


@pytest.mark.xfail(TEST_DATA_WITH_WRONG_VALUES, reason=Exception)
def test_calcuate_with_negative_params(deps):
    """Test calculate with negative parametrs.

    Args:
        deps: tuple[float] - negative parameters.
    """
    assert get_top_salaries(*deps)
