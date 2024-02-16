"""Модуль с функциями для вычисления статистики по зарплатам."""

from typing import Dict, Optional


def calculate_median(numbers):
    """
    Рассчитывает медианное значение списка чисел.

    Args:
        numbers (list): Список числовых данных.

    Returns:
        float: Медианное значение данных.
    """
    sorted_numbers = sorted(numbers)
    len_numbers = len(sorted_numbers)
    if len_numbers % 2 == 0:
        return (sorted_numbers[len_numbers // 2 - 1] + sorted_numbers[len_numbers // 2]) / 2
    return sorted_numbers[len_numbers // 2]


def salary_stats(
    departments: Dict[str, Dict[str, float]],
    limit: Optional[float] = None,
) -> Dict[str, float]:
    """
    Функция считающая среднюю, максимальную и значение медианы у зарплат.

    Args:
        departments (Dict): отделы
        limit(Float or None): лимит зарплаты

    Returns:
        Dict: словарь значений у зарплаты
    """
    salaries = []
    for department in departments.values():
        for salary in department.values():
            if limit is None or salary >= limit:
                salaries.append(salary)
    if salaries:
        total_salary = sum(salaries)
        return {
            'average': round(total_salary / len(salaries), 2),
            'maximum': max(salaries),
            'median': round(calculate_median(salaries), 2),
        }
    return {
        'average': None,
        'maximum': None,
        'median': None,
    }
