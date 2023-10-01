"""Calculates top and bottom three salaries."""


def top_three_salaries(
    names: tuple[str, ...] | None = None,
    **departments: dict[str, float],
) -> tuple[tuple[str, ...], tuple[str, ...]]:
    """
    Extract top and bottom three salaries.

    Args:
        names: tuple[str, ...] | None - Optional tuple of names for return.
        departments: dict[str, int] - dict of department names and their values.

    Returns:
        tuple[tuple[float, ...], tuple[float, ...]] - inner tuples are with lowest and
        highest salaries
    """
    avg_salaries = []
    for department in departments.keys():
        if names is None or department in names:
            dep_salaries = departments[department].values()
            avg_salary = sum(dep_salaries) / max(len(dep_salaries), 1)
            avg_salaries.append([department, avg_salary])

    avg_salaries.sort(key=lambda dep: dep[1])
    lowest = [low[0] for low in avg_salaries[:3]]
    highest = [high[0] for high in avg_salaries[-3:]]
    return tuple(lowest), tuple(highest)
