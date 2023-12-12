"""Module, provides functions for solving task_1."""


def get_all_salaries(departments: dict[str, dict], limit_salary: int | float) -> list[float]:
    """Get a sorted list of all salaries across departments.

    Args:
        departments (dict): A dictionary representing departments and their workers.
        limit_salary (int | float): The salary limit. Salaries above this limit will be excluded.

    Returns:
        list[float]: A sorted list of all salaries from all workers in the provided departments,
            in descending order.
    """
    if limit_salary:
        all_salaries = [
            salary
            for workers in departments.values()
            for salary in workers.values()
            if salary < limit_salary
        ]
    else:
        all_salaries = [
            salary
            for workers in departments.values()
            for salary in workers.values()
        ]

    return sorted(all_salaries, reverse=True)


def top_salary(
    limit_salary: int | float = None,
    **departments: dict[str, dict],
) -> tuple[list[float], float]:
    """Calculate the top salaries and the percentage they represent.

    Args:
        limit_salary: The salary limit, default is None.
        departments (dict): A dictionary representing departments and their workers.

    Returns:
        tuple: A tuple containing a list of the top salaries (rounded to 2 decimal
        places) and the percentage these salaries represent (rounded to
        2 decimal places).
    """
    all_salaries = get_all_salaries(departments, limit_salary)
    top = all_salaries[:3]

    if sum(all_salaries) == 0:
        percent = 0
    else:
        percent = round(sum(top) / sum(all_salaries) * 100, 2)

    return [round(salary, 2) for salary in top], percent
