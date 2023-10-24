"""Function for calculating the top 3 salaries and its percentage of all salaries."""


def top_salary(*deps: tuple[str, list[float]], lim: float = None) -> tuple[tuple, float]:
    """Calculate the top 3 salaries and its percentage of all salaries.

    Args:
        deps: tuple[str, list[float]] - department name and list of salaries.
        lim: float - salaries less than this value are considered, default is None.

    Returns:
        tuple[list, float]: top 3 salaries and percentage of it to all salaries.

    """
    all_salaries = []

    for _, salaries in deps:
        for salary in salaries:
            if (lim is not None and salary <= lim) or not lim:
                all_salaries.append(round(salary, 2))

    all_salaries.sort(reverse=True)
    if sum(all_salaries) == 0:
        return [], 0

    percent = (sum(all_salaries[:3]) / sum(all_salaries)) * 100

    return (all_salaries[:3], round(percent, 2))
