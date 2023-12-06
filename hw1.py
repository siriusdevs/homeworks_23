from typing import Any

"""
Напишите функцию, которая принимает любые ключевые аргументы,
но ожидает, что название аргумента будет названием отдела компании (str),
а значение для аргумента - словарем,
где имена сотрудников (str) служат в качестве ключей,
а зарплаты (float) - в качестве значений .
Функция должна возвращать статистику:
топ 3 зарплат в компании списком,
отношение суммы этого топа ко всему размеру выплат в компании, в процентах.
Функция также должна принимать опциональный аргумент,
который по умолчанию равен None.
Этот аргумент - числовой предел, ниже которого зарплаты учитывать не нужно.
Все числа в выводе функции округлять до второго знака после запятой.
Оформить файл по flake8 с учетом данного вам setup.cfg.
Написать тесты.
Проверка линтера и тесты должны работать в github workflows.
"""


def check(value: Any, value_type: type, value_name: str) -> None:
    """Check type of given value.

    Args:
        value (Any): value that need to check
        value_type (type): target type
        value_name (str): name of value that need to check

    Raises:
        TypeError: if given wrong type of value
    """
    if not isinstance(value, value_type):
        raise TypeError(f'{value_name} type is not {value_type.__name__}')


def salaries_statistic(
        dprts: dict[str, dict[str, float]],
        min_salary: float | None = None,
        ) -> tuple:
    """this module is designed to work with args
    (unpack departments to count sum of sellaries in all of them,
    to sort it if we hawe limit, like min_salary ),
    to make top 3 sum of sellaries in departments,
    to count precentage of top 3 sum to total salarie sum,
    to find Type and Value errors if there are in args.


    Args:
        departaments (dict[str, dict[str, float]]):
        /Names of depatments with dicts of workers-their salaries
        min_salary (float | None, optional):
        /Minimal salarie limit to sort workers salaries in future.
        /Defaults to None.

    Raises:
        ValueError: if wrong value given

    Returns:
        _type_:
        /returns top 3 salaries in departaments,
        /precentage of top 3 sum to total salary sum
    """
    answer = []
    answer1 = []
    super_total_salary = 0
    for departament_name, departament in dprts.items():
        total_salary = 0
        for name, salary in departament.items():
            check(name, str, 'name')
            check(departament_name, str, 'department_name')
            check(salary, float, 'salary')
            salary = round(salary, 2)
            super_total_salary += salary
            if not min_salary:
                total_salary += salary
            else:
                check(min_salary, float, 'min_salary')
                if salary >= min_salary:
                    total_salary += salary
        answer.append(total_salary)
    if super_total_salary == 0:
        raise ValueError('super_total_salary = 0, на ноль делить нельзя.')
    answer = sorted(answer, reverse=True)[0:3]
    [answer1.append(round(number, 2)) for number in answer]
    return answer1, f'{round((sum(answer)/super_total_salary)*100, 2)}%'
