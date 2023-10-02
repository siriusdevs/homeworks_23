"""Module that includes the implemented function from Vasilenko's first task."""


from typing import Optional


def process_lowest_sals(lowest_sals: list[float | int], salary: float) -> None:
    """Create a function that collects three lowest salaries into the list.

    Args:
        lowest_sals (list): list object that we need to fill.
        salary (float): value that we work with (add it into list on necessary index or skip).
    """
    if salary >= lowest_sals[2]:
        return

    second_lowest = lowest_sals[1]
    if salary < lowest_sals[0]:
        lowest_sals[2] = second_lowest
        lowest_sals[1] = lowest_sals[0]
        lowest_sals[0] = salary
        return
    if salary < lowest_sals[1]:
        lowest_sals[2] = second_lowest
        lowest_sals[1] = salary
        return
    lowest_sals[2] = salary


def salary_stats(
    limit: Optional[int] = None,
    **departments: dict[str, float],
) -> tuple[list[float], str]:
    """Create a function that returns a generator containing statistics about employee salaries.

    Args:
        limit (int): the maximum salary value to be considered.
        departments (dict): \
            dict of the keyword arguments where the keys \
            are the names of the departments and the values \
            are the dicts of the employees where the keys \
            are the names of the employees and values are their salaries.

    Returns:
        a tuple consisting of the list
        of the three lowest salaries
        and percent of its sum to all salaries
    """
    if not limit:
        limit = float('inf')

    total_payed = 0
    lowest_sals = [float('inf') for _ in range(3)]

    for employees_data in departments.values():
        salaries = employees_data.values()

        for salary in salaries:
            if salary <= limit:
                total_payed += salary
                process_lowest_sals(lowest_sals, salary)

    # prevent division by zero error
    if total_payed == 0:
        return [], '100%'

    lowests_percent_of_all_salaries = round(sum(lowest_sals) * 100 / total_payed, 2)
    return lowest_sals, f'{lowests_percent_of_all_salaries}%'
