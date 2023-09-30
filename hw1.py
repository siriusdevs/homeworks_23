'''Salary stats and percent's'''
from typing import List, Tuple, Optional


def top_salary(*args: Tuple[str, List[float]],
               name_departments: Optional[List[str]] = None) -> Tuple[List[float], float]:
    """
    Find top 3 salaries in the company, the ratio of the amount of this top to the total amount of
    payments in the company in percentages.

    Args:
        *args: Tuple[str, List[float]] - company departments and their salaries.
        name_departments: List[str] - the name departaments. Usually Optional[List[str]] = None.

    Returns:
        tuple[list[float], float] - top 3 salaries and the ratio  of the amount
        of this top to the total amount of payments.
    """
    department_salaries = {}
    for department_name, salaries in args:
        if name_departments is None or department_name in name_departments:
            department_salaries[department_name] = salaries

    all_salaries = [salary for salaries in department_salaries.values()
                    for salary in salaries]

    if not all_salaries:
        return [], 0.0

    top_salaries = sorted(all_salaries, reverse=True)[:3]
    total_top_salaries = sum(top_salaries)
    total_salaries = sum(all_salaries)
    percentage = round(total_top_salaries / total_salaries * 100, 2)

    return top_salaries, percentage
