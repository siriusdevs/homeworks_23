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
            if lim:
                if salary <= lim:
                    all_salaries.append(round(salary, 2))
            else:
                all_salaries.append(round(salary, 2))
    all_salaries.sort(reverse=True)
    all_sum = sum(all_salaries)
    if all_sum == 0:
        return [], 0
    top_salaries = all_salaries[:3]
    percent = sum(top_salaries) / all_sum * 100
    return top_salaries, round(percent, 2)
