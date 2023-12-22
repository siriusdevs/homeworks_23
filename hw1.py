"""
The function calculates the salary of the company's departments.

Напишите функцию, которая принимает любое количество позиционных аргументов,
где каждый аргумент - это кортеж формата( название отдела компании (str),
{словарь фамилий сотрудников этого отдела (str) и их зарплат (float)} ).
Функция должна возвращать статистику: средняя, максимальная и медианная зарплата в компании.
Функция также должна принимать опциональный аргумент, который по умолчанию равен None.
Этот аргумент - кортеж названий отделов, которые нужно включить в статистику (их и только их).
Все числа в выводе функции округлять до второго знака после запятой.
Оформить файл по flake8 с учетом данного вам setup.cfg.
Написать тесты. Проверка линтера и тесты должны работать в github workflows.
"""

from typing import List, Optional, Tuple

ROUND_UPTO = 2


def company_stats(
    *departments: Tuple[str, dict],
    selected: Optional[Tuple[str]] = None,
) -> Tuple[float]:
    """Calculate the salary of employees, optionally including only the specified departments.

    Args:
        departments: all departments of the company.
        selected: departments that are included in the statistics.

    Raises:
        ValueError: if entered an empty salary or all salaries is zero

    Returns:
        Company statistics on average, maximum and median salary.
    """
    all_salaries = []

    for department, employees in departments:
        if selected is None or department in selected:
            for salary in employees.values():
                all_salaries.append(salary)

    if not all_salaries:
        raise ValueError('The salary should not be empty.')
    if sum(all_salaries) <= 0:
        raise ValueError('The salary should not be or less than zero.')

    avg_salary = round(sum(all_salaries) / len(all_salaries), ROUND_UPTO)
    max_salary = round(max(all_salaries), ROUND_UPTO)
    median_salary = round(get_median(all_salaries), ROUND_UPTO)

    return avg_salary, max_salary, median_salary


def get_median(salary: List[float]) -> float:
    """Calculate median salary.

    Args:
        salary: salary of employees from departments.

    Returns:
        float: median of salary.
    """
    lenght = len(salary)
    index = lenght // 2
    if lenght % 2:
        return sorted(salary)[index]
    return sum(sorted(salary)[index - 1:index + 1]) / 2
