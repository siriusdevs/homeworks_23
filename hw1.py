"""Salary stats."""
from typing import Dict


def salary_stats(
    company: Dict[str, Dict[str, float]],
    ceiling: float = None,
) -> tuple[list[float], float] | str:
    """
    Find top 3 salaries and a top salaries sum to all salaries ratio.

    Args:
        company: Dict[str, Dict[str, float]] - company departments, employees and their salaries.
        ceiling: float - the salary ceiling.

    Returns:
        tuple[list[float], float] - top 3 salaries and the ratio.
        or
        str - if your company is shady.
    """
    sal = []
    all_sal = 0
    for per in company.values():
        for num in per.values():
            if ceiling is None or num <= ceiling:
                sal.append(round(num, 2))
                all_sal += num
    sal.sort(reverse=True)
    top = sal[:3]
    if all_sal > 0:
        ratio = round(sum(top) / all_sal * 100, 2)
        return (top, ratio)
    return "That's a strange company. It does not pay it's workers or they have none of them."
