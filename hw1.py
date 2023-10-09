"""Homework №1. Module of departments stats."""


def department_statistics(
    *departments: tuple[str, list[float]],
    specific_departments: tuple[str] = None,
) -> tuple[list, list]:
    """
    Department (dept.) statistics by salaries.

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
    try:
        avg_salary_by_depts = (
            (
                department[0],
                round(sum(department[1]) / len(department[1]), 2),
            )
            for department in departments
            if department[0] in (specific_departments or department[0])
        )
    except ZeroDivisionError:
        return 'You have entered empty list of department salaries.'
    else:
        sorted_depts_by_avg_salary = [
            department[0]
            for department in sorted(
                avg_salary_by_depts,
                key=lambda department: department[1],
            )
        ]
    return (sorted_depts_by_avg_salary[:3], sorted_depts_by_avg_salary[-3:])
