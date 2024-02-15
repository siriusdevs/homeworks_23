"""Main file with task for hw1."""

import statistics
from typing import Dict, Optional


def salary_stats(
    departments: Dict[str, Dict[str, float]], limit: Optional[float] = None,
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
        return {
            'average': round(sum(salaries) / len(salaries), 2),
            'maximum': max(salaries),
            'median': round(statistics.median(salaries), 2),
        }
    return {
        'average': None,
        'maximum': None,
        'median': None,
    }
