"""Function calculates top 3 salaries and their sum percentage of all salaries."""
from typing import Optional

from hw3 import check_type


def salary_stat(
    *args: tuple[str, list[float]],
    exclude: Optional[tuple[str]] = None,
) -> tuple[list[float], float]:
    """Return top 3 salaries and their sum percentage of all salaries.

    Args:
        args: tuple[str, list[float]]: department name and list of salaries.
        exclude: Optional[tuple[str]]: departments to exclude.

    Returns:
        tuple[list[float], float]: top 3 salaries and their sum percentage.
    """
    if exclude is None:
        exclude = ()
    salaries = []
    for department, department_salaries in args:
        if department not in exclude:
            for salary in department_salaries:
                check_type(salary, float, check_positive=True)
            salaries.extend(department_salaries)
    salaries.sort(reverse=True)
    top_salaries = salaries[:3]
    top_salaries_sum = sum(top_salaries)
    try:
        top_salaries_sum_percentage = top_salaries_sum / sum(salaries) * 100
    except ZeroDivisionError:
        top_salaries_sum_percentage = 0
    return top_salaries, round(top_salaries_sum_percentage, 2)
