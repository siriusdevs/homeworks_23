"""Module for calculating statistics of salaries of employees of company departments."""


from typing import Optional


def check_salary_for_negativity(staff: dict[str, float]) -> None:
    """Check the salary assignment is greater than zero.

    Args:
        staff (dict): department staff.

    Raises:
        ValueError: if one of the employees has a salary less than zero.
    """
    for employee, salary in staff.items():
        if salary < 0:
            raise ValueError(f'{employee} имеет отрицательную зарплату.')


def get_departments_rating(
    departments: dict[str, dict[str, float]],
    included_deps: Optional[tuple[str, ...]] = None,
) -> tuple[list, list]:
    """Calculate the top 3 highest and the top 3 lowest paid departments in the company.

    Args:
        departments (dict[str, dict[str, int]]): company departments with employee salaries.
        included_deps (Optional[Tuple[str, ...]] = None): departments included in the statistics, \
            defaults to None.

    Returns:
        Tuple[list, list]: the top 3 highest and the top 3 lowest paid departments in the company.
    """
    average_salaries = {}
    included_deps = set(included_deps) if included_deps is not None else set()
    for department_name, staff in departments.items():
        if not included_deps or department_name in included_deps:
            check_salary_for_negativity(staff)

            salaries = staff.values()
            lenth = len(salaries)
            if lenth != 0:
                average_salaries[department_name] = round(sum(salaries) / lenth, 2)

    sorted_departments = sorted(average_salaries.items(), key=lambda el: el[1])
    sorted_departments = [sorted_department for sorted_department, _ in sorted_departments]

    return sorted_departments[:-4:-1], sorted_departments[:3]
