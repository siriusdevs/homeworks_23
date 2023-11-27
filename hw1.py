"""Module, provides functions for solving task_1."""
from typing import Tuple


def get_all_salaries(departments: dict[str, dict]) -> list[float]:
    """Get a sorted list of all salaries across departments.

    Args:
        departments (dict): A dictionary representing departments and their workers.
            Keys are department names (str), and values are dictionaries of workers,
            where keys are worker names (str), and values are their salaries (float).

    Returns:
        list[float]: A sorted list of all salaries from all workers in the provided departments,
            in descending order.
    """
    all_salaries = [salary for workers in departments.values() for salary in workers.values()]

    return sorted(all_salaries, reverse=True)


def filter_top_salaries(all_salaries: list[float], limit_salary: int | float) -> list[float]:
    """Filter top salaries based on the provided salary limit.

    Args:
        all_salaries (list[float]): A list of all salaries to be filtered.
        limit_salary (int | float): The salary limit. Salaries above this limit will be excluded.

    Returns:
        list[float]: A list containing the top salaries (up to 3) based on the provided limit.
    """
    if limit_salary:
        top = list(filter(lambda salary: salary < limit_salary, all_salaries))[:3]
    else:
        top = all_salaries[:3]

    return top


def top_salary(
    limit_salary: int | float = None,
    **departments: dict[str, dict],
) -> Tuple[list[float], float]:
    """Calculate the top salaries and the percentage they represent.

    Args:
        limit_salary: The salary limit, default is None.
        departments (dict): A dictionary representing departments and their workers.

    Returns:
        tuple: A tuple containing a list of the top salaries (rounded to 2 decimal
        places) and the percentage these salaries represent (rounded to
        2 decimal places).
    """
    all_salaries = get_all_salaries(departments)
    top = filter_top_salaries(all_salaries, limit_salary)
    percent = round(sum(top) / sum(all_salaries) * 100, 2)

    return [round(salary, 2) for salary in top], percent


data = {
            'HR2': {'BobMArk': 4000.0, 'Mark': 4500.0, 'KAtya': 4200.0},
            'Sales2': {'Juse': 5500.0, 'Pasito': 5200.0},
        }

print(top_salary(**data))