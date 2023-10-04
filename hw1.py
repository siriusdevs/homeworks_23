"""Homework №1. Module of departments stats."""
from typing import List, Tuple


def dept_stat(*args: Tuple[str, List[float]], cur_dept: Tuple[str] = None) -> Tuple[List, List]:
    """
    Department salaries stats.

    Args:
        args: Tuple[str, List[float]] - names of departments and their salaries of employees.
        cur_dept: Tuple[str] - departments that need to be included in the statistics.\
            (default None).

    Raises:
        ZeroDivisionError: - division by zero.

    Returns:
        Top 3 highest and lowest-paid departments.
    """
    depts = (
        tuple(filter(lambda elem: elem[0] in cur_dept, args))
        if cur_dept else args
    )
    try:
        dept_mean_salary = (
            (
                elem[0],
                round(sum(elem[1]) / len(elem[1]), 2),
            ) for elem in depts
        )
    except ZeroDivisionError:
        raise ZeroDivisionError('Division by zero.')
    else:
        sorted_dept = sorted(dept_mean_salary, key=lambda elem: elem[1])
    return (sorted_dept[:3], sorted_dept[-3:])
