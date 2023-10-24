"""Function for calculating the top 3 salaries and its percentage of all salaries."""


def calculate_salary(*deps: tuple[str, list[float]], lim: float = None):
    """Calculate the top 3 salaries and its percentage of all salaries.

    Args:
        deps: Tuple[str, List[float]] department name and list of salaries.
        lim: float numerical limit of salaries which default is None.

    Returns:
        tuple[tuple, float]: top 3 salaries and percentage of it to all salaries.

    """
    salaries = []

    for _, dep_salaries in deps:
        for salary in dep_salaries:
            if (lim is not None and salary <= lim) or not lim:
                salaries.append(round(salary, 2))

    salaries.sort(reverse=True)

    if sum(salaries) == 0:
        return [], 0

    percent = (sum(salaries[:3]) / sum(salaries)) * 100

    return (salaries[:3], round(percent, 2))
