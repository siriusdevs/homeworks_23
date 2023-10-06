"""Homework №1. Module of departments stats."""
from typing import List


def department_statistics(
    *departments: tuple[str, List[float]],
    specific_departments: tuple[str] = None,
) -> tuple[List, List]:
    """
    Department statistics by salaries.

    Args:
        departments: tuple[str, List[float]] - names of departments and\
            their salaries of employees.
        specific_departments: tuple[str] - departments that need to be included in the statistics.\
            (default None).

    Exception:
        ZeroDivisionError: - division by zero occurs if an empty list of salaries was passed.

    Returns:
        Top 3 highest and lowest-paid departments.
    """
    filtered_departments_by_optional_arg = (
        tuple(
            filter(
                lambda department: department[0] in specific_departments, departments,
            ),
        )
        if specific_departments
        else departments
    )
    try:
        avg_salary_by_departments = (
            (
                department[0],
                round(sum(department[1]) / len(department[1]), 2),
            )
            for department in filtered_departments_by_optional_arg
        )
    except ZeroDivisionError:
        return 'You have entered empty list of department salaries.'
    else:
        sorted_departments_by_avg_salary = sorted(
            avg_salary_by_departments,
            key=lambda department: department[1],
        )
    return (sorted_departments_by_avg_salary[:3], sorted_departments_by_avg_salary[-3:])
