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
    include_deps: Optional[tuple[str]] = None,
) -> tuple[list]:
    """Calculate the top 3 highest and the top 3 lowest paid departments in the company.

    Args:
        departments (dict[str, dict[str, int]]): company departments with employee salaries.
        include_deps (Optional[Tuple[str]] = None): departments included in the statistics, \
            defaults to None.

    Returns:
        Tuple[list]: the top 3 highest and the top 3 lowest paid departments in the company.
    """
    average_salaries = {}
    for department, staff in departments.items():
        if not include_deps or department in include_deps:
            check_salary_for_negativity(staff)

            salaries = staff.values()
            lenth = len(salaries)
            if lenth != 0:
                average_salaries[department] = round(sum(salaries) / lenth, 2)

    average_salaries = sorted(average_salaries.items(), key=lambda el: el[1])
    average_salaries = [sorted_salary for sorted_salary, _ in average_salaries]

    return average_salaries[:-4:-1], average_salaries[:3]
