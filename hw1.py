"""Module that includes the implemented function from Vasilenko's first task."""


from typing import Any, Dict, Generator, Iterable, Optional


def salary_stats(
    limit: Optional[int] = None,
    **departments: Dict[str, Dict[str, float]],
) -> Generator[Iterable | str, Any, Any]:
    """Create a function that returns a generator containing statistics about employee salaries.

    Args:
        limit (int): the maximum salary value to be considered.
        departments (dict): dict of the keyword arguments where the keys \
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

    all_salaries = []
    for employees_data in departments.values():
        salaries = employees_data.values()
        all_salaries.extend(salary for salary in salaries if salary <= limit)

    three_lowest_salaries = sorted(all_salaries)[:3]
    total_payed = sum(all_salaries)

    # prevent division by zero error
    if total_payed == 0:
        return three_lowest_salaries, '100%'

    lowests_percent_of_all_salaries = round(sum(three_lowest_salaries) * 100 / total_payed, 2)
    return three_lowest_salaries, f'{lowests_percent_of_all_salaries}%'
