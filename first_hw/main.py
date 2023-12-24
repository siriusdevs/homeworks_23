import statistics
from typing import Dict, Optional


def salary_stats(
    departments: Dict[str, Dict[str, float]], limit: Optional[float] = None
) -> Dict[str, float]:
    salaries = []
    for department in departments.values():
        for salary in department.values():
            if limit is None or salary >= limit:
                salaries.append(salary)
    salaries = sorted([round(salary, 2) for salary in salaries])
    return {
        'average': round(sum(salaries) / len(salaries), 2),
        'maximum': max(salaries) if salaries else None,
        'median': round(statistics.median(salaries), 2) if salaries else None,
    }
