"""Salary stats."""
from typing import Dict, Tuple


def salary_stats(company: Dict[str, Dict[str, float]], ceiling: float = None) -> Tuple:
    """
    Find top 3 salaries and a top salaries sum to all salaries ratio.

    Args:
        company: Dict[str, Dict[str, float]] - company departments, employees and their salaries.
        ceiling: float - the salary ceiling.

    Returns:
        Tuple[list[float], float] - top 3 salaries and the ratio
    """
    sal = []
    for per in company.values():
        for num in per.values():
            if ceiling is None or num <= ceiling:
                sal.append(round(num, 2))
    sal.sort(reverse=True)
    all_sal = sum(sal)
    top = sal[:3]
    return (top, round(sum(top) / all_sal * 100, 2))
