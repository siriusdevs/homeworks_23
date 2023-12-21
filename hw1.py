"""Homework about company's department statistics."""


def calculate_department_statistics(
    *departments: tuple[str, dict],
    excluded_departments: list[str] = None,
) -> tuple[dict[str, float], dict[str, float]]:
    """Calculate department statistics.

    Args:
        *departments (tuple[str, dict]): Tuple of department name and employees dictionary.
        excluded_departments (list[str], optional): Departments to be excluded. Defaults to None.

    Returns:
        tuple[dict[str, float], dict[str, float]]: Data of company's departments.
    """
    excluded_departments = set(excluded_departments) if excluded_departments else set()

    department_salaries = {}

    for department, employees in departments:
        if department not in excluded_departments:
            average_salary = sum(employees.values()) / len(employees.values()) \
                if employees.values() else 0
            department_salaries[department] = average_salary

    sorted_departments = sorted(
        department_salaries.items(),
        key=lambda elem: elem[1],
        reverse=True,
    )

    top_three_highest = sorted_departments[:3]
    top_three_lowest = sorted_departments[-3:]

    return top_three_highest, top_three_lowest
