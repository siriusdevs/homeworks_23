"""Module for calculating salaries for employees."""

from typing import Optional, TypeAlias

import helpers.get_median

Employees: TypeAlias = dict[str, float]  # name, salary
CompanyInfo: TypeAlias = tuple[float, ...]  # average, maximum and median salary


def get_stats(min_salary: Optional[int | float] = None, **departments: Employees) -> CompanyInfo:
    """Calculate average, maximum and medium salary for the company.

    Args:
        min_salary: The lower limit of salaries that we consider, default - None.
        departments: \
            Departments that we consider salaries in, \
            They have to be given through keyword params.

    Returns:
        Calculated average, maximum and medium salary in the company,
        result is a tuple with three float values.
    """
    salary_sum: float = 0
    max_salary: float = 0
    filtered_salaries: list[float] = []

    for employees in departments.values():
        for salary in employees.values():
            if (min_salary is not None) and (salary < min_salary):
                continue

            salary_sum += salary
            max_salary = max(salary, max_salary)
            filtered_salaries.append(salary)

    salaries_length = len(filtered_salaries)
    average_salary = salary_sum / max(salaries_length, 1)

    return tuple(round(info_salary, 2) for info_salary in (
        average_salary,
        max_salary,
        helpers.get_median.get_median(filtered_salaries),
    ))
