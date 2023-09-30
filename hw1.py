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

    Yields:
        tuple of the three lowest salaries
        and percent of its sum to all salaries
    """
    if not limit:
        limit = float('inf')

    all_salaries = []
    for _, employees_data in departments.items():
        salaries = employees_data.values()
        all_salaries.extend(salaries)
    all_salaries = list(filter(lambda salary: salary <= limit))

    three_lowest_salaries = sorted(all_salaries)[:3]
    yield three_lowest_salaries

    total_payed = sum(all_salaries)
    if total_payed == 0:
        yield '100%'
        return

    lowests_percent_of_all_salaries = round(sum(three_lowest_salaries) * 100 / total_payed, 2)
    yield f'{lowests_percent_of_all_salaries}%'
