"""Homework about company's department statistics."""

from typing import List, Tuple


def calculate_department_statistics(
        *departments: Tuple[str, dict],
        excluded_departments: List[str] = None,
        ) -> Tuple[List[Tuple[str, float]], List[Tuple[str, float]]]:
    """Calculates department statistics.

    Args:
        excluded_departments (List[str], optional): Departments to be excluded. Defaults to None.

    Returns:
        Tuple[List[Tuple[str, float]], List[Tuple[str, float]]]: Data of company's departments.
    """
    if excluded_departments is None:
        excluded_departments = []

    department_salaries = {}

    for department, employees in departments:
        if department not in excluded_departments:
            salaries = [salary for salary in employees.values()]
            average_salary = sum(salaries) / len(salaries) if salaries else 0
            department_salaries[department] = average_salary

    sorted_departments = sorted(department_salaries.items(), key=lambda x: x[1], reverse=True)

    top_3_highest = sorted_departments[:3]
    top_3_lowest = sorted_departments[-3:]

    top_3_highest = [(department, round(salary, 2)) for department, salary in top_3_highest]
    top_3_lowest = [(department, round(salary, 2)) for department, salary in top_3_lowest]

    return top_3_highest, top_3_lowest
