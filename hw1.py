"""Module for calculating salary stats."""

from typing import Optional


def get_salaries(
    *company: tuple[str, dict[str, float]],
    dept_except: Optional[str] = None,
) -> tuple[list, float]:
    """Count top 3 salaries and those part in all salaries.

    Args:
        company (tuple[str, dict[str, float]]): salaries in departments for each employee.
        dept_except (tuple[str], optional): Excluded departments. Defaults to None.

    Returns:
        tuple[list, float]: top 3 salaries and part of those in '%'.
    """
    salaries = []

    for department in company:
        if dept_except is None or (department[0] not in dept_except):
            salaries += department[1].values()

    top_three = sorted(salaries, reverse=True)[:3]
    sum_salaries = sum(salaries)

    if sum_salaries:
        in_percentage = (sum(top_three) / sum_salaries) * 100
    else:
        in_percentage = 0

    return [round(salary, 2) for salary in top_three], round(in_percentage, 2)
