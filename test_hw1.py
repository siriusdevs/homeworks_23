"""get_top_salaries function test module."""

from typing import Tuple

import pytest

from hw1 import get_top_salaries

test_data_without_departments = (
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
    # Указан список зарплат, но не указан отдел - игнорируем
    ((([123],),),
     ([], 0),
     ),
    # В одном кортеже не указано имя отдела. Игнорируем именно его
    ((([10, 20, 20, 80, 20],),
      ('Market', [20, 20, 20, 80, 20]),
      ('Sale', [20, 20, 20, 80, 20]),
      ),
     ([20, 20, 20], 18.75),
     ),
    # Указан отдел, но не указаны зарплаты
    ((('Dev',),),
     ([], 0),
     ),
    # Передан пустой кортеж - игнорируем
    ((()), ([], 0)),
    # Не переданы аргументы - игнорируем
    ((), ([], 0)),
)
test_data_with_departments = (
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
    # Передан пустой кортеж и кортеж отделов - не считаем, данных нет
    (((),), ('abc', 'ghi'), ([], 0)),
)
test_data_with_negative_value = (
    # Отрицательная зарплата. Такой не бывает - возвращаем ошибку.
    ((('Develop', [80, 80, 80, -20, 80]),
      ('Marketing', [80, 80, 80, -20, 80]),
      ('Sales', [80, 80, 80, -20, 80, 80]),
      ),
     ),
)


@pytest.mark.parametrize('args, expected', test_data_without_departments)
def test_get_top_salaries_without_departments(args: tuple, expected: tuple):
    """Test get_top_salaries function with departments argument.

    Args:
        args: tuple - a tuple of tuples with name of departments and list of salaries.
        expected: tuple - expected function result.
    """
    assert get_top_salaries(*args) == expected


@pytest.mark.parametrize('args, deps, expected', test_data_with_departments)
def test_get_top_salaries_with_departments(args: tuple, deps: Tuple[str], expected: tuple):
    """Test get_top_salaries function with departments argument.

    Args:
        args: tuple - a tuple of tuples with name of departments and list of salaries.
        deps: tuple - a tuple with a tuple of departments names whose salaries need to be counted.
        expected: tuple - expected function result.
    """
    assert get_top_salaries(*args, required_deps=deps) == expected


@pytest.mark.xfail(test_data_with_negative_value, reason=Exception)
def test_calcuate_with_negative_params(args):
    """Test calculate with negative parametrs.

    Args:
        args: Tuple[float] - negative parameters.
    """
    assert get_top_salaries(*args)
