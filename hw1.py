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
    sal = []
    all_sal = 0
    for department in company.values():
        for salary in department.values():
            if ceiling is None or salary <= ceiling:
                sal.append(round(salary, 2))
                all_sal += salary
    sal.sort(reverse=True)
    top = sal[:3]
    if all_sal > 0:
        ratio = round(sum(top) / all_sal * 100, 2)
        return top, ratio
    return top
