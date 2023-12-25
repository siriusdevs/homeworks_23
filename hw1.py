"""Count top 3 the salaries."""
from typing import Optional


def calculate_salary_stats(limit: Optional[int] = None, **departments: dict[str, float]) -> tuple:
    """
    Calculate the average salary for each category of employees.

    Args:
        limit: maximum salary limit, defaults to None.
        departments: each keyword arg is a dict of department employees and their salaries.

    Returns:
        tuple: a tuple containing the calculation results with the top
            highly paid and top low paid departments.
    """
    stats = {}

    for dep, employees in departments.items():
        salaries = employees.values()
        if limit is not None:
            salaries = [salary for salary in salaries if salary <= limit]
        average_salary = round(
            sum(salaries) / len(salaries), 2,
        ) if salaries else 0
        stats[dep] = average_salary

    sorted_salaries = sorted(
        stats, key=lambda depart: stats.get(depart),
    )
    top_low_paid = sorted_salaries[:3]
    top_highly_paid = sorted_salaries[-1:-4:-1]

    return top_low_paid, top_highly_paid
