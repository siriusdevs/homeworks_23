"""Salary stats."""


def salary_stats(
    company: dict[str, dict[str, float]],
    ceiling: float = None,
) -> tuple[list[float], float] | str:
    """
    Find top 3 salaries and a top salaries sum to all salaries ratio.

    Args:
        company: dict[str, dict[str, float]] - company departments, employees and their salaries.
        ceiling: float - the salary ceiling.

    Returns:
        tuple[list[float], float] - top 3 salaries and the ratio.
        or
        str - if your company is shady.
    """
    all_salaries = []
    salaries_sum = 0
    for department in company.values():
        for salary in department.values():
            if ceiling is None or salary <= ceiling:
                all_salaries.append(round(salary, 2))
                salaries_sum += salary
    all_salaries.sort(reverse=True)
    while len(all_salaries) < 3:
        all_salaries.append(0)
    top = all_salaries[:3]
    if salaries_sum > 0:
        ratio = round(sum(top) / salaries_sum * 100, 2)
        return top, ratio
    return top
