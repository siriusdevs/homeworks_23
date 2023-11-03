"""Module, that has one function "check_arguments" and "top_salary", homework 1."""
from itertools import chain


def check_arguments(departments: dict[str, ...], limit_salary: int | float):
    """Check the validity of the arguments.

    Args:
        departments: A dictionary representing departments and their workers
            where the keys are department names (str) and the values are dictionaries of workers
            where the keys are worker names (str) and the values are their salaries (float).
        limit_salary: An optional argument representing the salary limit.

    Raises:
        ValueError: If no arguments are provided in the departments dictionary.
        TypeError: If the department or workers is not of the correct type.
        TypeError: If the worker or salary is not of the correct type.
        TypeError: If the optional argument limit_salary is not an int or float.
    """
    if not departments:
        raise ValueError('No one argument in departments')

    for department, workers in departments.items():
        if not isinstance(department, str) or not isinstance(workers, dict):
            raise TypeError('Wrong type of department or workers')

        for worker, salary in workers.items():
            if not isinstance(worker, str) or not isinstance(salary, float):
                raise TypeError('Wrong type of worker or salary')

    if limit_salary and not isinstance(limit_salary, (int, float)):
        raise TypeError(f'Optional argument limit_salary must be int or float, '
                        f'but got {type(limit_salary).__name__}')


def top_salary(
    limit_salary: int | float = None,
    **departments: dict[str, dict],
) -> (list[float], float):
    """Calculates the top salaries and the percentage they represent.

    Args:
        limit_salary: The salary limit. Default is None.
        **departments: Variable keyword arguments representing departments
            and their workers. The keys are department names (str) and the values are
            dictionaries of workers where the keys are worker names (str) and the
            values are their salaries (float).

    Returns:
        tuple: A tuple containing a list of the top salaries (rounded to 2 decimal places) and
            the percentage these salaries represent (rounded to 2 decimal places).

    Raises:
        ValueError: If there are no arguments in the departments.
    """
    check_arguments(departments, limit_salary)

    all_salaries = sorted(list(chain.from_iterable(workers.values() for workers in
                                                   departments.values())), reverse=True)

    if limit_salary:
        top = list(filter(lambda salary: salary < limit_salary, all_salaries))[:3]
    else:
        top = all_salaries[:3]

    percent = round(sum(top) / sum(all_salaries) * 100, 2)

    return [round(salary, 2) for salary in top], percent
