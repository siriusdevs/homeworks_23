from typing import Optional, Dict, Generator, Iterable, Any


def salary_stats(
    limit: Optional[str] = None,
    **departments: Dict[str, Dict[str, float]]
) -> Generator[Iterable | str, Any, Any]:
    """
    A function that returns a generator containing statistics about employee salaries

    Args:
        limit: the value that represents max salary that will be considered
        departments: dict of the keyword arguments where the keys
                     are the names of the departments and the values
                     are the dicts of the employees where the keys
                     are the names of the employees and values are their salaries
    Returns:
        generator object which consists of the tuple of the three lowest salaries
        and percent of its sum to all salaries
    """

    limit = float("inf") if not limit else limit
    all_salaries = []
    for _, department in departments.items():
        salaries = department.values()
        all_salaries.extend(filter(lambda x: x <= limit, salaries))

    three_lowest_salaries = sorted(all_salaries)[:3]
    yield three_lowest_salaries

    total_payed = sum(all_salaries)
    if total_payed == 0:
        yield "100%"
        return
    yield f"{round(sum(three_lowest_salaries) * 100 / total_payed, 2)}%"
