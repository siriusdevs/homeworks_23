"""Module for solution HW1."""

from typing import Any

# Напишите функцию, которая принимает любые ключевые аргументы,
# но ожидает, что название аргумента будет названием отдела компании (str),
# а значение для аргумента - словарем,
# где имена сотрудников (str) служат в качестве ключей,
# а зарплаты (float) - в качестве значений .
# Функция должна возвращать статистику:
# топ 3 зарплат в компании списком,
# отношение суммы этого топа ко всему размеру выплат в компании, в процентах.
# Функция также должна принимать опциональный аргумент,
# который по умолчанию равен None.
# Этот аргумент - числовой предел, ниже которого зарплаты учитывать не нужно.
# Все числа в выводе функции округлять до второго знака после запятой.
# Оформить файл по flake8 с учетом данного вам setup.cfg.
# Написать тесты.
# Проверка линтера и тесты должны работать в github workflows.


def check(value_to_check: Any, value_type: tuple, value_name: str) -> None:
    """Check type of given value.

    Args:
        value_to_check (Any): value that need to check
        value_type (tuple): target type
        value_name (str): name of value that need to check

    Raises:
        TypeError: if given wrong type of value
    """
    if not isinstance(value_to_check, value_type):
        raise TypeError(f'{value_name} type is not valid')


def salaries_statistic(
    dprts: dict[str, dict[str, float]],
    min_salary: float | None = None,
) -> tuple:
    """Calculate salaries statistics in given departments.

    Args:
        dprts (dict[str, dict[str, float]]): Names of depatments \
            with dicts of workers-their.
        min_salary (float | None, optional): Minimal salarie limit to sort \
              workers salaries in future. Defaults to None.

    Raises:
        ValueError: if wrong value given.

    Returns:
        tuple: returns top 3 salaries in departaments, \
            precentage of top 3 sum to total salary sum
    """
    answer = []
    super_total_salary = 0
    check(dprts, dict, 'dprts')
    if min_salary:
        check(min_salary, (float, int), 'min_salary')
    for departament_name, departament in dprts.items():
        total_salary = 0
        check(departament, dict, 'department')
        for name, salary in departament.items():
            check(name, str, 'name')
            check(departament_name, str, 'department_name')
            check(salary, (float, int), 'salary')
            salary = round(salary, 2)
            if min_salary is None or salary >= min_salary:
                total_salary += salary
                super_total_salary += salary
        answer.append(round(total_salary, 2))
    answer = sorted(answer, reverse=True)[:3]
    try:
        ratio_top_salaries = round((sum(answer) / super_total_salary) * 100, 2)
    except ZeroDivisionError:
        raise ValueError('super_total_salary = 0, на ноль делить нельзя.')
    return answer, f'{ratio_top_salaries}%'

print(salaries_statistic({
    'ARCHIVE_OTDEL': {
        'Rubiya': 7820.0,
        'Aurora Galicina': 1007.0,
        'Liticiya Mangovna': 9810.0,
        'Ditrian Aksilim': 4500.0,
        'Edvard Kallin1': 79680.5,
    },
    'HUMOR_CENTER': {
        'Zahar Starcev': 1070.0,
        'Jakob': 8750.0,
        'Ellise': 5340.5,
        'Bred Pit': 9000.0,
        'Charli': 3500.5,
    },
    'MENEGERS': {
        'Karlael': 1000.0,
        'Bella': 4000.5,
        'Dzhasper': 3000.5,
        'Anna': 2300.0,
        'Victoriya': 6000.0,
    },
    'VET_DOCTORS': {
        'Vladlen': 3400.0,
        'Mariya': 7020.5,
        'Ognislav': 3409.95,
        'Erimei': 2304.5,
        'Prahlada': 2098.0,
    },
},3000))