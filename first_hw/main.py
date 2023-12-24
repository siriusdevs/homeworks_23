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
    salaries = sorted([round(salary_act, 2) for salary_act in salaries])
    return {
        'average': round(sum(salaries) / len(salaries), 2),
        'maximum': max(salaries) if salaries else None,
        'median': round(statistics.median(salaries), 2) if salaries else None,
    }
