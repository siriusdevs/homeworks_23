"""Module, that has one function "best_wage", homework1."""
from typing import List, Tuple


def best_wage(*departments: Tuple[str, dict], exclude_deps: Tuple[str] = None) -> Tuple[List[int | float], str] | str:
    """Find 3 best salaries and their percentage to total amount of payments.

    Args:
        exclude_deps: excluded department's names.
        departments: departments and dictionary of names and salaries.

    Returns:
        Tuple: 3 best salaries and their percentage to total amount of payments.
        str: error handling
    """
    total_salary = 0
    permitted_wages = []
    for department in departments:
        for salary in department[1].values():
            total_salary += salary
            if exclude_deps is None or department[0] not in exclude_deps:
                permitted_wages.append(salary)
    try:
        if not permitted_wages:
            raise ZeroDivisionError
    except ZeroDivisionError:
        return 'Недостаточно не исключенных отделов для использования функции'

    permitted_wages = sorted(permitted_wages, reverse=True)[:3]
    permitted_wages = [round(permitted_wages[top], 2) for top in range(len(permitted_wages))]
    percent_best_salary = round(sum(permitted_wages) / total_salary * 100, 2)
    return permitted_wages, percent_best_salary
